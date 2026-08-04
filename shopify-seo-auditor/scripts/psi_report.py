#!/usr/bin/env python3
"""
Pull Core Web Vitals for a few URLs from the PageSpeed Insights API.

Reports CrUX field data first (what real users experienced, which is what
Google uses) and falls back to Lighthouse lab metrics when a URL has too
little traffic to have field data.

The API works without a key at a low quota. For more volume, set
PAGESPEED_API_KEY in the environment.

Usage:
    python psi_report.py URL [URL ...]
    python psi_report.py --strategy desktop URL
    python psi_report.py --json URL
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# Google's Core Web Vitals thresholds: (good, needs-improvement) upper bounds.
THRESHOLDS = {
    "LARGEST_CONTENTFUL_PAINT_MS": (2500, 4000, "ms", "LCP"),
    "INTERACTION_TO_NEXT_PAINT": (200, 500, "ms", "INP"),
    "CUMULATIVE_LAYOUT_SHIFT_SCORE": (0.1, 0.25, "", "CLS"),
    "FIRST_CONTENTFUL_PAINT_MS": (1800, 3000, "ms", "FCP"),
    "EXPERIMENTAL_TIME_TO_FIRST_BYTE": (800, 1800, "ms", "TTFB"),
}


def verdict(metric_id, value):
    if metric_id not in THRESHOLDS:
        return "?"
    good, poor, _, _ = THRESHOLDS[metric_id]
    if metric_id == "CUMULATIVE_LAYOUT_SHIFT_SCORE":
        value = value / 100.0
    if value <= good:
        return "GOOD"
    if value <= poor:
        return "NEEDS WORK"
    return "POOR"


def fmt(metric_id, value):
    if metric_id == "CUMULATIVE_LAYOUT_SHIFT_SCORE":
        return f"{value / 100.0:.3f}"
    return f"{value}ms"


def query(url, strategy, timeout):
    params = {"url": url, "strategy": strategy, "category": "performance"}
    key = os.environ.get("PAGESPEED_API_KEY")
    if key:
        params["key"] = key
    req = urllib.request.Request(
        f"{ENDPOINT}?{urllib.parse.urlencode(params)}",
        headers={"User-Agent": "PikkaSEOAudit/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = json.loads(e.read().decode("utf-8")).get("error", {}).get("message", "")
        except Exception:
            pass
        if e.code == 429 and not key:
            detail = ("the shared anonymous quota is exhausted (it usually is). "
                      "Get a free key at https://developers.google.com/speed/docs/insights/v5/get-started "
                      "and set PAGESPEED_API_KEY.")
        return {"_error": f"HTTP {e.code}: {detail or e.reason}"}
    except Exception as e:
        return {"_error": f"{type(e).__name__}: {e}"}


def summarize(url, data, strategy):
    lines = [f"### {url}  [{strategy}]"]
    if "_error" in data:
        lines.append(f"  ERROR: {data['_error']}")
        lines.append("")
        return "\n".join(lines)

    field = data.get("loadingExperience", {}).get("metrics", {})
    origin = data.get("originLoadingExperience", {}).get("metrics", {})

    if field:
        lines.append("  FIELD DATA (CrUX, real users — this is what Google acts on):")
        for mid, m in field.items():
            label = THRESHOLDS.get(mid, (0, 0, "", mid))[3]
            p75 = m.get("percentile")
            lines.append(f"    {label:5} p75 {fmt(mid, p75):>10}   {verdict(mid, p75)}")
    else:
        lines.append("  FIELD DATA: none (URL has too little traffic in CrUX)")
        if origin:
            lines.append("  ORIGIN-LEVEL field data (whole domain):")
            for mid, m in origin.items():
                label = THRESHOLDS.get(mid, (0, 0, "", mid))[3]
                p75 = m.get("percentile")
                lines.append(f"    {label:5} p75 {fmt(mid, p75):>10}   {verdict(mid, p75)}")

    lh = data.get("lighthouseResult", {})
    score = lh.get("categories", {}).get("performance", {}).get("score")
    if score is not None:
        lines.append(f"  LAB (Lighthouse) performance score: {round(score * 100)}/100")

    audits = lh.get("audits", {})
    heavy = audits.get("total-byte-weight", {}).get("displayValue")
    if heavy:
        lines.append(f"  Total page weight: {heavy}")

    # Third-party weight is the usual Shopify culprit: apps, not the theme.
    tp = audits.get("third-party-summary", {})
    items = (tp.get("details") or {}).get("items") or []
    if items:
        top = sorted(items, key=lambda i: i.get("blockingTime", 0), reverse=True)[:5]
        lines.append("  Heaviest third parties (main-thread blocking):")
        for it in top:
            name = (it.get("entity") or {}).get("text") or it.get("entity") or "?"
            lines.append(f"    {str(name)[:40]:40} blocking {it.get('blockingTime', 0):>6.0f}ms"
                         f"   transfer {it.get('transferSize', 0) / 1024:>7.0f}KB")

    opps = []
    for aid, a in audits.items():
        if a.get("details", {}).get("type") == "opportunity":
            saving = a.get("details", {}).get("overallSavingsMs", 0)
            if saving >= 100:
                opps.append((saving, a.get("title", aid)))
    if opps:
        lines.append("  Top opportunities:")
        for saving, title in sorted(opps, reverse=True)[:5]:
            lines.append(f"    {saving:>6.0f}ms  {title}")

    lines.append("")
    return "\n".join(lines)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Core Web Vitals via the PageSpeed Insights API.")
    ap.add_argument("urls", nargs="+", help="URLs to measure (keep it to a handful)")
    ap.add_argument("--strategy", choices=["mobile", "desktop"], default="mobile",
                    help="Default mobile — it is what Google indexes with")
    ap.add_argument("--timeout", type=float, default=90, help="Per-request timeout (default 90)")
    ap.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    ap.add_argument("--json", action="store_true", help="Emit raw API JSON")
    args = ap.parse_args()

    if not os.environ.get("PAGESPEED_API_KEY"):
        print("# no PAGESPEED_API_KEY set — using the free quota, expect rate limits",
              file=sys.stderr)

    out = []
    for i, url in enumerate(args.urls):
        if i:
            time.sleep(args.delay)
        print(f"# measuring {i+1}/{len(args.urls)}: {url}", file=sys.stderr)
        data = query(url, args.strategy, args.timeout)
        out.append((url, data))

    if args.json:
        print(json.dumps({u: d for u, d in out}, indent=2, ensure_ascii=False))
    else:
        for url, data in out:
            print(summarize(url, data, args.strategy))


if __name__ == "__main__":
    main()

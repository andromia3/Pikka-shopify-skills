#!/usr/bin/env python3
"""
Fetch a sample of store URLs and extract the SEO signals an audit needs.

Read-only: issues GET requests only, never sends credentials, never submits
forms, never follows a redirect silently. Standard library only.

Usage:
    python seo_fetch.py URL [URL ...]
    python seo_fetch.py --file urls.txt
    python seo_fetch.py --sample https://store.com    # derive a Shopify sample
    python seo_fetch.py --json URL                    # raw JSON instead of report

Options:
    --delay SECONDS   Pause between requests (default 1.0)
    --timeout SECONDS Per-request timeout (default 15)
    --max N           Hard cap on URLs fetched (default 60)
"""

import argparse
import gzip
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA = "PikkaSEOAudit/1.0 (+https://github.com/Pikka-Shopify/Pikka-shopify-skills)"
MAX_REDIRECTS = 10


class SEOParser(HTMLParser):
    """Collects the head/body signals an SEO audit reads on each page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self.meta_description = None
        self.meta_robots = None
        self.canonical = None
        self.hreflang = []          # [(hreflang, href)]
        self.h1 = []
        self.jsonld_types = []
        self.jsonld_errors = 0
        self.pagination_links = []  # hrefs containing ?page=
        self.internal_links = 0
        self.external_links = 0
        self.images = 0
        self.images_no_alt = 0
        self._in_title = False
        self._in_h1 = False
        self._in_jsonld = False
        self._svg_depth = 0     # <svg><title> is an icon label, not the page title
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "svg":
            self._svg_depth += 1
            return
        if self._svg_depth:
            return
        if tag == "title":
            # Only the first <title> outside <svg> is the page title.
            if self.title is None:
                self._in_title = True
                self._buf = []
        elif tag == "h1":
            self._in_h1 = True
            self._buf = []
        elif tag == "meta":
            name = (a.get("name") or a.get("property") or "").lower()
            if name == "description":
                self.meta_description = (a.get("content") or "").strip()
            elif name == "robots":
                self.meta_robots = (a.get("content") or "").strip().lower()
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            href = a.get("href")
            if rel == "canonical" and href:
                self.canonical = href.strip()
            elif rel == "alternate" and a.get("hreflang") and href:
                self.hreflang.append((a["hreflang"].strip(), href.strip()))
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._in_jsonld = True
            self._buf = []
        elif tag == "a":
            href = a.get("href") or ""
            if "page=" in href:
                self.pagination_links.append(href)
            if href.startswith("http"):
                self.external_links += 1
            elif href.startswith("/"):
                self.internal_links += 1
        elif tag == "img":
            self.images += 1
            if not (a.get("alt") or "").strip():
                self.images_no_alt += 1

    def handle_endtag(self, tag):
        if tag == "svg":
            self._svg_depth = max(0, self._svg_depth - 1)
            return
        if self._svg_depth:
            return
        text = "".join(self._buf).strip()
        if tag == "title" and self._in_title:
            self.title = re.sub(r"\s+", " ", text)
            self._in_title = False
        elif tag == "h1" and self._in_h1:
            self.h1.append(re.sub(r"\s+", " ", text))
            self._in_h1 = False
        elif tag == "script" and self._in_jsonld:
            self._in_jsonld = False
            self._collect_jsonld(text)
        self._buf = []

    def handle_data(self, data):
        if self._in_title or self._in_h1 or self._in_jsonld:
            self._buf.append(data)

    def _collect_jsonld(self, raw):
        try:
            data = json.loads(raw)
        except (ValueError, TypeError):
            self.jsonld_errors += 1
            return

        def walk(node):
            if isinstance(node, dict):
                t = node.get("@type")
                if isinstance(t, str):
                    self.jsonld_types.append(t)
                elif isinstance(t, list):
                    self.jsonld_types.extend(str(x) for x in t)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(data)


def fetch(url, timeout):
    """GET a URL, following redirects manually so the chain stays visible."""
    chain = []
    current = url
    started = time.monotonic()
    for _ in range(MAX_REDIRECTS):
        req = urllib.request.Request(
            current,
            headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,application/xml"},
            method="GET",
        )
        opener = urllib.request.build_opener(NoRedirect)
        try:
            resp = opener.open(req, timeout=timeout)
        except urllib.error.HTTPError as e:
            resp = e
        except Exception as e:  # network, DNS, TLS
            return {"url": url, "error": f"{type(e).__name__}: {e}", "chain": chain}

        status = resp.getcode()
        if status in (301, 302, 303, 307, 308):
            location = resp.headers.get("Location")
            if not location:
                break
            nxt = urllib.parse.urljoin(current, location)
            chain.append({"from": current, "status": status, "to": nxt})
            current = nxt
            continue

        body = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            try:
                body = gzip.decompress(body)
            except OSError:
                pass
        charset = resp.headers.get_content_charset() or _sniff_charset(body) or "utf-8"
        return {
            "url": url,
            "final_url": current,
            "status": status,
            "chain": chain,
            "content_type": resp.headers.get("Content-Type", ""),
            "x_robots_tag": resp.headers.get("X-Robots-Tag"),
            "bytes": len(body),
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "html": body.decode(charset, errors="replace"),
        }
    return {"url": url, "error": "too many redirects", "chain": chain}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _sniff_charset(body):
    """Read <meta charset> when the response headers don't declare one."""
    head = body[:4096].decode("ascii", errors="ignore")
    m = re.search(r'<meta[^>]+charset=["\']?([\w-]+)', head, re.I)
    return m.group(1) if m else None


def analyze(result):
    """Turn a fetch result into the flat record the audit reasons about."""
    if "error" in result:
        return {"url": result["url"], "error": result["error"], "chain": result.get("chain", [])}

    rec = {k: result.get(k) for k in ("url", "final_url", "status", "chain", "bytes", "elapsed_ms", "x_robots_tag")}
    html = result["html"]

    if "html" not in result.get("content_type", ""):
        rec["note"] = f"non-HTML content ({result.get('content_type')})"
        return rec

    p = SEOParser()
    try:
        p.feed(html)
    except Exception as e:
        rec["parse_error"] = str(e)

    rec.update({
        "title": p.title,
        "title_len": len(p.title) if p.title else 0,
        "meta_description": p.meta_description,
        "meta_description_len": len(p.meta_description) if p.meta_description else 0,
        "meta_robots": p.meta_robots,
        "canonical": p.canonical,
        "canonical_is_self": _same_url(p.canonical, rec["final_url"]) if p.canonical else None,
        "h1": p.h1,
        "h1_count": len(p.h1),
        "hreflang": p.hreflang,
        "hreflang_count": len(p.hreflang),
        "jsonld_types": sorted(set(p.jsonld_types)),
        "jsonld_parse_errors": p.jsonld_errors,
        "has_crawlable_pagination": len(p.pagination_links) > 0,
        "internal_links": p.internal_links,
        "images": p.images,
        "images_missing_alt": p.images_no_alt,
    })
    return rec


def _same_url(a, b):
    def norm(u):
        s = urllib.parse.urlsplit(u)
        return (s.netloc.lower().replace("www.", ""), s.path.rstrip("/") or "/")
    try:
        return norm(a) == norm(b)
    except Exception:
        return None


def shopify_sample(base):
    """Derive the standard Shopify template sample from a store root."""
    base = base.rstrip("/")
    return [
        base,
        f"{base}/robots.txt",
        f"{base}/sitemap.xml",
        f"{base}/collections/all",
        f"{base}/collections/all?page=2",
        f"{base}/search?q=test",
    ]


def report(records):
    """Compact human/LLM-readable output. One block per URL."""
    lines = []
    for r in records:
        lines.append(f"### {r['url']}")
        if "error" in r:
            lines.append(f"  ERROR: {r['error']}")
            if r.get("chain"):
                lines.append(f"  redirects: {_chain(r['chain'])}")
            lines.append("")
            continue
        lines.append(f"  status: {r['status']}   bytes: {r.get('bytes')}   response time: {r.get('elapsed_ms')}ms")
        if r.get("chain"):
            lines.append(f"  REDIRECT CHAIN ({len(r['chain'])} hop(s)): {_chain(r['chain'])}")
        if r.get("note"):
            lines.append(f"  note: {r['note']}")
            lines.append("")
            continue
        if r.get("x_robots_tag"):
            lines.append(f"  X-Robots-Tag: {r['x_robots_tag']}")
        lines.append(f"  title ({r['title_len']}): {r.get('title')!r}")
        lines.append(f"  meta description ({r['meta_description_len']}): {_trunc(r.get('meta_description'))!r}")
        lines.append(f"  meta robots: {r.get('meta_robots')}")
        lines.append(f"  canonical: {r.get('canonical')}  (self-referential: {r.get('canonical_is_self')})")
        lines.append(f"  h1 x{r['h1_count']}: {[_trunc(h, 60) for h in r.get('h1', [])]}")
        if r["hreflang_count"]:
            lines.append(f"  hreflang x{r['hreflang_count']}: {r['hreflang'][:8]}{' ...' if r['hreflang_count'] > 8 else ''}")
        else:
            lines.append("  hreflang: none")
        lines.append(f"  JSON-LD types: {r.get('jsonld_types') or 'none'}"
                     + (f"  (parse errors: {r['jsonld_parse_errors']})" if r.get("jsonld_parse_errors") else ""))
        lines.append(f"  crawlable pagination links: {r.get('has_crawlable_pagination')}")
        lines.append(f"  internal links: {r.get('internal_links')}   images: {r.get('images')} "
                     f"({r.get('images_missing_alt')} missing alt)")
        lines.append("")
    return "\n".join(lines)


def _chain(chain):
    return " -> ".join(f"[{h['status']}] {h['to']}" for h in chain)


def _trunc(s, n=120):
    if not s:
        return s
    return s if len(s) <= n else s[: n - 1] + "…"


def main():
    # Accented content must survive the console on every platform.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Extract SEO signals from a sample of URLs (read-only).")
    ap.add_argument("urls", nargs="*", help="URLs to fetch")
    ap.add_argument("--file", help="File with one URL per line")
    ap.add_argument("--sample", metavar="STORE_URL", help="Derive a standard Shopify sample from a store root")
    ap.add_argument("--delay", type=float, default=1.0, help="Seconds between requests (default 1.0)")
    ap.add_argument("--timeout", type=float, default=15, help="Per-request timeout (default 15)")
    ap.add_argument("--max", type=int, default=60, help="Hard cap on URLs (default 60)")
    ap.add_argument("--json", action="store_true", help="Emit raw JSON instead of the compact report")
    args = ap.parse_args()

    urls = list(args.urls)
    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            urls += [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    if args.sample:
        urls += shopify_sample(args.sample)

    seen, ordered = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)

    if not ordered:
        ap.error("no URLs given (pass URLs, --file, or --sample)")
    if len(ordered) > args.max:
        print(f"# capped at {args.max} URLs (got {len(ordered)}); raise with --max", file=sys.stderr)
        ordered = ordered[: args.max]

    records = []
    for i, u in enumerate(ordered):
        if i:
            time.sleep(args.delay)
        print(f"# fetching {i+1}/{len(ordered)}: {u}", file=sys.stderr)
        records.append(analyze(fetch(u, args.timeout)))

    if args.json:
        print(json.dumps(records, indent=2, ensure_ascii=False))
    else:
        print(report(records))


if __name__ == "__main__":
    main()

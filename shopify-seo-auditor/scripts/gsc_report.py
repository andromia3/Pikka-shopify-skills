#!/usr/bin/env python3
"""
Aggregate a Search Console export into the few numbers an audit reasons about.

A GSC export routinely runs to tens of thousands of rows — far past what fits
in a conversation. This collapses it into brand/non-brand split, striking
distance opportunities, low-CTR pages, and cannibalisation candidates.

Works with the standard "Export > CSV" files (Queries.csv, Pages.csv) and with
any CSV carrying Query and/or Page plus Clicks, Impressions, CTR, Position.

Usage:
    python gsc_report.py Queries.csv --brand "nooance,nooance paris"
    python gsc_report.py Pages.csv
    python gsc_report.py export.csv --brand mybrand --top 25
"""

import argparse
import csv
import io
import sys

# Header aliases: GSC localises exports, so match loosely.
FIELDS = {
    "query": ["query", "requête", "requete", "consulta", "suchanfrage", "zoekopdracht"],
    "page": ["page", "url", "página", "pagina", "seite"],
    "clicks": ["clicks", "clics", "clic", "klicks", "clics totales"],
    "impressions": ["impressions", "impresiones", "impressionen", "vertoningen"],
    "ctr": ["ctr", "taux de clic", "click through rate"],
    "position": ["position", "posición", "posicion", "durchschnittliche position", "positie"],
}


def detect_columns(header):
    resolved = {}
    lowered = [h.strip().lower().lstrip("﻿") for h in header]
    for field, aliases in FIELDS.items():
        for i, h in enumerate(lowered):
            if any(h == a or h.startswith(a) for a in aliases):
                resolved[field] = i
                break
    return resolved


def to_float(raw):
    if raw is None:
        return 0.0
    s = str(raw).strip().replace("%", "").replace(" ", "").replace("\xa0", "").replace(" ", "")
    if not s:
        return 0.0
    # European decimal comma, but only when there is no thousands dot.
    if "," in s and "." not in s:
        s = s.replace(",", ".")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


def load(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        sample = fh.read(8192)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        except csv.Error:
            dialect = csv.excel
        reader = csv.reader(fh, dialect)
        rows = list(reader)

    if not rows:
        sys.exit("empty file")

    cols = detect_columns(rows[0])
    if "clicks" not in cols or "impressions" not in cols:
        sys.exit(f"could not find Clicks/Impressions columns in header: {rows[0]}")

    out = []
    for row in rows[1:]:
        if not row or len(row) < len(cols):
            continue
        rec = {
            "query": row[cols["query"]].strip() if "query" in cols else None,
            "page": row[cols["page"]].strip() if "page" in cols else None,
            "clicks": to_float(row[cols["clicks"]]),
            "impressions": to_float(row[cols["impressions"]]),
            "ctr": to_float(row[cols["ctr"]]) if "ctr" in cols else None,
            "position": to_float(row[cols["position"]]) if "position" in cols else None,
        }
        if rec["ctr"] is None and rec["impressions"]:
            rec["ctr"] = rec["clicks"] / rec["impressions"] * 100
        out.append(rec)
    return out, cols


def is_brand(text, terms):
    if not text or not terms:
        return False
    t = text.lower()
    return any(term in t for term in terms)


def section(title):
    return f"\n## {title}\n"


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Summarise a Search Console CSV export.")
    ap.add_argument("csv_path", help="Path to the GSC export")
    ap.add_argument("--brand", default="", help="Comma-separated brand terms, for the brand/non-brand split")
    ap.add_argument("--top", type=int, default=20, help="Rows per table (default 20)")
    args = ap.parse_args()

    terms = [t.strip().lower() for t in args.brand.split(",") if t.strip()]
    rows, cols = load(args.csv_path)
    has_query, has_page = "query" in cols, "page" in cols

    total_clicks = sum(r["clicks"] for r in rows)
    total_impr = sum(r["impressions"] for r in rows)

    print(f"# Search Console summary — {args.csv_path}")
    print(f"\nRows: {len(rows)}   Clicks: {total_clicks:,.0f}   Impressions: {total_impr:,.0f}"
          f"   Overall CTR: {(total_clicks / total_impr * 100) if total_impr else 0:.2f}%")

    # --- Brand vs non-brand -------------------------------------------------
    if has_query:
        if terms:
            brand = [r for r in rows if is_brand(r["query"], terms)]
            nonbrand = [r for r in rows if not is_brand(r["query"], terms)]
            bc = sum(r["clicks"] for r in brand)
            nc = sum(r["clicks"] for r in nonbrand)
            print(section("Brand vs non-brand"))
            print(f"Brand:     {bc:>10,.0f} clicks ({bc / total_clicks * 100 if total_clicks else 0:5.1f}%)"
                  f"   {len(brand)} queries")
            print(f"Non-brand: {nc:>10,.0f} clicks ({nc / total_clicks * 100 if total_clicks else 0:5.1f}%)"
                  f"   {len(nonbrand)} queries")
            print("\nA store living on brand traffic has no organic acquisition engine — "
                  "it is being found by people who already know it.")
        else:
            print("\n(no --brand given; skipping the brand/non-brand split — "
                  "it is usually the single most telling number)")

    pool = [r for r in rows if not is_brand(r["query"], terms)] if (has_query and terms) else rows

    # --- Striking distance --------------------------------------------------
    if "position" in cols:
        near = [r for r in pool if 4 <= (r["position"] or 99) <= 20 and r["impressions"] >= 50]
        near.sort(key=lambda r: r["impressions"], reverse=True)
        print(section(f"Striking distance (position 4-20, >=50 impressions) — {len(near)} found"))
        if near:
            label = "Query" if has_query else "Page"
            print(f"{label[:60]:60} {'Impr':>8} {'Clicks':>7} {'CTR':>7} {'Pos':>6}")
            for r in near[: args.top]:
                key = (r["query"] or r["page"] or "")[:60]
                print(f"{key:60} {r['impressions']:>8,.0f} {r['clicks']:>7,.0f} "
                      f"{r['ctr'] or 0:>6.1f}% {r['position']:>6.1f}")
            print("\nThese already rank. Moving them is cheaper than creating new pages.")

    # --- Low CTR at good positions -----------------------------------------
    if "position" in cols:
        weak = [r for r in pool
                if (r["position"] or 99) <= 10 and r["impressions"] >= 100 and (r["ctr"] or 0) < 2.0]
        weak.sort(key=lambda r: r["impressions"], reverse=True)
        print(section(f"Ranking well but not clicked (top 10, >=100 impr, CTR <2%) — {len(weak)} found"))
        if weak:
            label = "Query" if has_query else "Page"
            print(f"{label[:60]:60} {'Impr':>8} {'CTR':>7} {'Pos':>6}")
            for r in weak[: args.top]:
                key = (r["query"] or r["page"] or "")[:60]
                print(f"{key:60} {r['impressions']:>8,.0f} {r['ctr'] or 0:>6.1f}% {r['position']:>6.1f}")
            print("\nUsually a title/meta relevance problem, or a SERP feature taking the click.")

    # --- Cannibalisation ----------------------------------------------------
    if has_query and has_page:
        by_query = {}
        for r in pool:
            if r["impressions"] < 20:
                continue
            by_query.setdefault(r["query"], []).append(r)
        multi = {q: v for q, v in by_query.items() if len(v) > 1}
        print(section(f"Cannibalisation candidates (one query, several URLs) — {len(multi)} found"))
        if multi:
            ranked = sorted(multi.items(), key=lambda kv: sum(r["impressions"] for r in kv[1]), reverse=True)
            for q, group in ranked[: args.top]:
                print(f"\n  {q}  ({sum(r['impressions'] for r in group):,.0f} impressions across {len(group)} URLs)")
                for r in sorted(group, key=lambda r: r["impressions"], reverse=True)[:4]:
                    print(f"      pos {r['position'] or 0:5.1f}  {r['impressions']:>7,.0f} impr  {r['page']}")
            print("\nPick one owner URL per intent; consolidate or differentiate the rest.")
    elif has_query:
        print("\n(cannibalisation check needs an export carrying both Query and Page — "
              "the default Queries.csv has queries only)")

    # --- Top pages ----------------------------------------------------------
    if has_page and not has_query:
        top = sorted(rows, key=lambda r: r["clicks"], reverse=True)[: args.top]
        print(section("Top pages by clicks"))
        for r in top:
            print(f"{r['clicks']:>8,.0f} clicks {r['impressions']:>9,.0f} impr  {r['page'][:90]}")
        concentration = sum(r["clicks"] for r in top)
        if total_clicks:
            print(f"\nTop {len(top)} pages carry {concentration / total_clicks * 100:.0f}% of organic clicks.")


if __name__ == "__main__":
    main()

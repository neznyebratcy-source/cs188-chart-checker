#!/usr/bin/env python3
"""First-pass constraint checker for chart descriptions (CS 188 Core 3).

Reads examples/chart1_data.csv, computes ground-truth facts, then checks the
two sample descriptions against the constraints in docs/constraints.md.
Stdlib only.
"""
import csv, re, sys
from pathlib import Path

BASE = Path(__file__).parent / "examples"
UNIT = "units"  # chart1 y-axis unit, from the chart's data table

def load():
    rows = list(csv.DictReader(open(BASE / "chart1_data.csv")))
    labels = [r["month"] for r in rows]
    series = {c: [float(r[c]) for r in rows] for c in rows[0] if c != "month"}
    return labels, series

def facts(labels, series):
    out = {}
    for name, vals in series.items():
        trend = "rises" if vals[-1] > vals[0] else "falls" if vals[-1] < vals[0] else "flat"
        mx = max(vals); mn = min(vals)
        out[name] = dict(start=vals[0], end=vals[-1], trend=trend,
                         max=(mx, labels[vals.index(mx)]),
                         min=(mn, labels[vals.index(mn)]),
                         values=set(vals))
    return out

def check(text, labels, series, f):
    low = text.lower()
    problems, ok, missing = [], [], []

    # 4. units
    if "kilogram" in low and UNIT != "kilograms":
        problems.append(f"units: description says kilograms, chart unit is {UNIT}")
    # 2. trend claims like "apples rise/fall ..."
    for name in series:
        m = re.search(name + r"\s+(rise|rises|rose|fall|falls|fell|increase|increases|decrease|decreases)", low)
        if m:
            claimed = "rises" if m.group(1).startswith(("rise", "rose", "increase")) else "falls"
            if claimed != f[name]["trend"]:
                problems.append(f"trend: description says {name} {claimed}, data {f[name]['trend']} "
                                f"({f[name]['start']:.0f} -> {f[name]['end']:.0f})")
            else:
                ok.append(f"trend: {name} {claimed} - matches data")
    # 1. numbers must exist in the data
    allvals = set().union(*[s["values"] for s in f.values()])
    for num in re.findall(r"\d+(?:\.\d+)?", text):
        if float(num) not in allvals:
            problems.append(f"values: number {num} in description does not appear in the data")
    # 3. peak claims, tied to the series named in the same sentence
    MONTHS = {m: m for m in ["january","february","march","april","may","june",
                             "july","august","september","october","november","december"]}
    ABBR = {full: full[:3].capitalize() for full in MONTHS}
    for sent in re.split(r"[.!\n]", low):
        pm = re.search(r"peak\w*\s+in\s+(\w+)", sent)
        if not pm:
            continue
        month = ABBR.get(pm.group(1), pm.group(1).capitalize())
        for name in series:
            if name in sent:
                real_month, real_val = f[name]["max"][1], f[name]["max"][0]
                if month != real_month:
                    problems.append(f"max: description puts the {name} peak in {month}, "
                                    f"real max is {real_val:.0f} in {real_month}")
                else:
                    ok.append(f"max: {name} peak in {month} - matches data")
    # 5. completeness: every series mentioned?
    for name in series:
        if name not in low:
            missing.append(f"missing: series '{name}' is never mentioned")
    return ok, problems, missing

def main():
    labels, series = load()
    f = facts(labels, series)
    for fn in ["chart1_description_correct.txt", "chart1_description_wrong.txt"]:
        text = (BASE / fn).read_text()
        ok, problems, missing = check(text, labels, series, f)
        print(f"== {fn}")
        for s in ok: print("  PASS   ", s)
        for s in problems: print("  CONFLICT", s)
        for s in missing: print("  MISSING ", s)
        if not problems and not missing: print("  all checks passed")

if __name__ == "__main__":
    sys.exit(main())


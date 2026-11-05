# cs188-chart-checker

# CS 188 Core 3 prototype: chart description checker

Idea: a blind user gets a chart description (alt text / screen reader output) and
has no way to tell if it is right. This prototype checks a description against
the chart's actual data using a small set of constraints and reports, in plain
language: what matches, what conflicts, and what is missing.

## Core scenario

1. Input: a chart's data (CSV) + a text description of that chart.
2. Run the constraint checks (see `docs/constraints.md`).
3. Output: a short report a screen reader can read out:
   - matches: claims in the description that agree with the data
   - conflicts: claims that disagree with the data
   - missing: important things in the data the description never mentions

## Repo layout

- `docs/constraints.md` - the constraint list, what each check does
- `examples/` - test charts (data + description) with known right/wrong claims
- `checker.py` - first pass at running the checks on the examples

## Run the examples

```
python3 checker.py
```

## Status

Skeleton for Core Assignment 3 (first prototype). Demo: Nov 17.

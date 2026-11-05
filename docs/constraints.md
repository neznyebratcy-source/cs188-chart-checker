# Constraint list (v1)

Each check compares one kind of claim in a chart description against the
chart's underlying data. Output of every check: pass / fail / not mentioned.

1. **Values**
   Numbers stated in the description must match the data values for the
   points they refer to (exact match for integers, small tolerance for
   rounded values).
   Catches: invented numbers, swapped values between series.

2. **Trend direction**
   If the description says a series rises / falls / stays flat over a range,
   the data over that range must actually do that (compare first vs last,
   and overall direction).
   Catches: "increased steadily" for data that drops.

3. **Max / min points and labels**
   Stated maximum and minimum values, and the categories/labels attached to
   them, must be the true max/min of the data.
   Catches: wrong peak, right value but wrong category.

4. **Axis titles, ranges, units**
   Axis titles, stated ranges, and units in the description must match the
   chart's axes.
   Catches: wrong units (dollars vs thousands of dollars), wrong time range.

5. **Completeness**
   Every series in the data, and any extreme or unusual point (big spike,
   drop to zero), should be mentioned in the description. Unmentioned ones
   are reported as "missing".
   Catches: a whole series silently dropped from the description.

## Not in v1

- Charts without recoverable data (photo of a chart, no data table / SVG).
- Judging wording quality or reading level. We only check facts.


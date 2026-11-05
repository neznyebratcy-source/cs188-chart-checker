# Test examples

chart1: fruit sales, two series (apples, oranges), Jan-Jun.

- `chart1_description_correct.txt` - every claim agrees with the data.
  Expected: all checks pass, nothing missing.
- `chart1_description_wrong.txt` - planted errors:
  - wrong units (kilograms, data is units sold) -> check 4 fails
  - trend reversed (says apples fall, they rise) -> check 2 fails
  - values swapped (27 was June, not January) -> check 1 fails
  - wrong peak (says February 14, real peak is June 27) -> check 3 fails
  - invented value (oranges never reach 20) -> check 1 fails
  - oranges trend/extremes barely covered -> check 5 partial


#!/usr/bin/env python3
"""Exact conservative checks for NEAR_CUTOFF_REMOVAL.md.

The proof itself is analytic. These checks verify its rational constants.
The final floating-point evaluation is illustrative and explicitly labelled.
Only Python's standard library is used.
"""
from fractions import Fraction as Q
import json
import math

U = 3 * 10**12
# e > 8/3 follows already from the first five terms of its series.
e_lower = sum((Q(1, math.factorial(j)) for j in range(5)), Q(0))
assert e_lower > Q(8, 3)
assert Q(8, 3)**30 > U  # Hence log(U)+1 < 31.
# e^(3/4) > 2 follows from four series terms.
exp_three_fourths_lower = sum(
    (Q(3, 4)**j / math.factorial(j) for j in range(4)), Q(0)
)
assert exp_three_fourths_lower > 2
# pi > 3 and d=25 therefore give e^(-pi*d)<e^-75<2^-100.
derivative_bound = Q(4, 15) * U**2 * 31 / 2**100
numerator_bound = Q(2) * U * 31 / 2**100
assert derivative_bound < Q(1, 10000)
assert numerator_bound < Q(1, 10000)
# Count every interval (y,y+15], y >= 1e5.
# Using pi<22/7, e<3, e>8/3: log y>10, log7<2, log2<1.
assert 3**10 < 10**5
assert Q(8, 3)**2 > 7
count_lower_bound = Q(7, 4) * 10 - 2*2 - Q(1, 4) - 8
assert count_lower_bound > 0
out = {
    "status": "exact_rational_constants_passed",
    "verified_height": U,
    "deletion_height": U - 70,
    "retained_first_upper_offset": 15,
    "retained_second_interval_offsets": [30, 45],
    "minimum_retained_rate_gap": 15,
    "minimum_tail_gap": 25,
    "exp_three_fourths_lower_rational": str(exp_three_fourths_lower),
    "derivative_tail_upper_rational": str(derivative_bound),
    "derivative_tail_upper_decimal": float(derivative_bound),
    "numerator_tail_upper_rational": str(numerator_bound),
    "numerator_tail_upper_decimal": float(numerator_bound),
    "interval_zero_count_lower_rational": str(count_lower_bound),
    "illustrative_binary64_direct_derivative_bound":
        (4/15)*U**2*(math.log(U)+1)*math.exp(-25*math.pi),
    "limitation": "No new zero verification; no finite-to-cofinal inference."
}
print(json.dumps(out, indent=2))


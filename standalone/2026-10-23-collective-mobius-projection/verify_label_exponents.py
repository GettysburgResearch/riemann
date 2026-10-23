"""Finite exact algebra only; does not certify functional equations or estimates."""
from fractions import Fraction as F
import json

checks = 0

def check(truth, label):
    global checks
    if not truth:
        raise RuntimeError(label)
    checks += 1

# All fixed-prime branches in P7/P10/P11, including reduction 6 -> 0.
for a in range(1, 6):
    for eps in (0, 1):
        j = (a + eps) % 6
        for selected in (False, True):
            if selected and j == 5:
                continue
            p7 = -F(23, 12) * eps + F(j - 6 if selected else j, 12)
            check(p7 <= F(a, 12), ("P7", a, eps, selected))
            for eps_cost in (F(11, 12), F(7, 12)):
                residue_weight = (
                    -eps_cost * eps
                    + (F(j - 6, 12) if selected else F(j, 12))
                )
                check(residue_weight <= F(a, 12),
                      ("P10/P11", a, eps, selected, str(eps_cost)))

# S2 at Y=D for K<=D^(1/7), and Y=D^(5/6)K^(7/6) above it.
# All expressions are affine in k, so endpoints suffice on each interval.
def s2_exponents(y, k):
    return (
        2*y/3, F(5, 6)-y/6, 2*k-y/3,
        F(5, 6)+7*k/6-y/3, 1+2*k-4*y/3,
        1+7*k/6-y/2,
    )

for k in (F(0), F(1, 7)):
    for exponent in s2_exponents(F(1), k):
        check(exponent <= F(2, 3), ("S2 short", str(k), str(exponent)))
for k in (F(1, 7), F(1)):
    y = F(5, 6)+7*k/6
    target = F(5, 9)+7*k/9
    for exponent in s2_exponents(y, k):
        check(exponent <= target, ("S2 long", str(k), str(exponent)))

# S5's volume and plateau domination for k in [0,1/7].
for k in (F(0), F(1, 7)):
    target = F(11, 12)+7*k/12
    for exponent in (F(1, 2)+7*k/2, 2*k, F(5, 6)+7*k/6):
        check(exponent <= target, ("S5", str(k), str(exponent)))

# The exact P14 consumer.
h, k = F(6, 7), F(1, 32)
terms = (h+k, F(11, 12)+13*k/12, h/3+F(2, 3))
check(terms == (F(199, 224), F(365, 384), F(20, 21)), "benchmark terms")
check(max(terms) == F(20, 21), "benchmark maximum")
old = h/6+F(5, 6)
check(old == F(41, 42), "old exponent")
check(old-max(terms) == F(1, 42), "saving")
check(k < F(1, 7), "pole range")
check(k < h*F(1, 4), "Gram range with delta=1/4")
for threshold in ((2*h-1)/13, 5*(1-h)/6, F(1, 7), h/2):
    check(k < threshold, ("P15", str(threshold)))

# Negative control: larger K can defeat the claimed improvement.
k_bad = F(1, 10)
check(F(11, 12)+13*k_bad/12 > old, "negative control")

print(json.dumps({
    "scope": "exact finite exponent algebra, not analytic proof",
    "checks": checks,
    "projection_exponent": str(max(terms)),
    "inherited_exponent": str(old),
    "saving": str(old-max(terms)),
}, indent=2))

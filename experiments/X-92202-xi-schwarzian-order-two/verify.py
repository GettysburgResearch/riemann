#!/usr/bin/env python3
"""Finite diagnostics for L-92202/T-92201."""
from fractions import Fraction
from decimal import Decimal, getcontext
import json
import math
from pathlib import Path

getcontext().prec = 80


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def inv(z):
    n = z[0] * z[0] + z[1] * z[1]
    return (z[0] / n, -z[1] / n)


def div(z, w):
    return mul(z, inv(w))


def powg(z, n):
    out = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = mul(out, z)
    return out


def scale(a, z):
    return (a * z[0], a * z[1])


def derivatives(t, poles):
    tz = (t, Fraction(0))
    values = []
    for k in range(4):
        value = (Fraction(0), Fraction(0))
        coefficient = Fraction(math.factorial(k)) * ((-1) ** k)
        for weight, pole in poles:
            value = add(value, scale(coefficient * weight, inv(powg(add(tz, pole), k + 1))))
        values.append(value)
    return values


def direct(t, poles):
    _, p1, p2, p3 = derivatives(t, poles)
    return sub(scale(Fraction(2), mul(p1, p3)), scale(Fraction(3), mul(p2, p2)))


def pairwise(t, poles):
    tz = (t, Fraction(0))
    out = (Fraction(0), Fraction(0))
    for wa, sa in poles:
        ua = add(tz, sa)
        for wb, sb in poles:
            ub = add(tz, sb)
            term = div(powg(sub(sa, sb), 2), mul(powg(ua, 4), powg(ub, 4)))
            out = add(out, scale(Fraction(6) * wa * wb, term))
    return out


poles = [
    (Fraction(2), (Fraction(5), Fraction(0))),
    (Fraction(3), (Fraction(7), Fraction(2))),
    (Fraction(3), (Fraction(7), Fraction(-2))),
    (Fraction(1), (Fraction(20), Fraction(0))),
]
D1 = direct(Fraction(3, 2), poles)
D2 = pairwise(Fraction(3, 2), poles)
assert D1 == D2 and D1[1] == 0

H = Decimal(3_000_175_332_800)
domination_ratio = H * H / (Decimal(4320) * (H + 3).ln())
assert domination_ratio > Decimal("1e19")
separated_pair_angle = Decimal(str(2 * math.atan(0.501))) + Decimal(8) / H
anchor_pair_angle = (
    Decimal(str(2 * math.atan(float(Decimal(3) / (Decimal(2) * H)))))
    + Decimal(str(4 * math.atan(float(Decimal(2) / H))))
)
assert separated_pair_angle < Decimal(str(math.pi / 2))
assert anchor_pair_angle < Decimal("1e-10")


def fourth_numerator(t, poles):
    p1 = -sum(weight / (t + pole) ** 2 for weight, pole in poles)
    p2 = 2 * sum(weight / (t + pole) ** 3 for weight, pole in poles)
    p3 = -6 * sum(weight / (t + pole) ** 4 for weight, pole in poles)
    return (2 * p1 * p3 - 3 * p2 * p2).real


Htest = 1000.0
synthetic = [(2.0, (Htest / 2) ** 2)]
for b, a, multiplicity in [
    (Htest + 0.10, 0.49, 2),
    (Htest + 0.35, -0.47, 1),
    (Htest + 1.20, 0.45, 3),
    (Htest + 1.75, -0.40, 2),
]:
    c = b * b - a * a
    d = 2 * a * b
    synthetic.extend(
        [(2 * multiplicity, complex(c, d)), (2 * multiplicity, complex(c, -d))]
    )

sample_t = [0.25, 1, 1e3, 1e6, 1e9, 1e12]
sample_values = [fourth_numerator(t, synthetic) for t in sample_t]
assert min(sample_values) > 0

result = {
    "status": "PASS_XI_SCHWARZIAN_ORDER_TWO",
    "exact_fourth_power_identity": {"real": str(D1[0]), "imag": str(D1[1])},
    "published_constant_gates": {
        "H": str(H),
        "domination_margin_ratio": float(domination_ratio),
        "separated_pair_angle_upper": float(separated_pair_angle),
        "anchor_pair_angle_upper": float(anchor_pair_angle),
    },
    "synthetic_hostile_control": {
        "sample_t": sample_t,
        "sample_schwarzian_numerator": sample_values,
        "minimum": min(sample_values),
    },
}
out = Path(__file__).resolve().parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
print(result["status"])
print(json.dumps(result, indent=2, sort_keys=True))

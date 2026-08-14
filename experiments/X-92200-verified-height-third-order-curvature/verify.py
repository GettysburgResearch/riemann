#!/usr/bin/env python3
"""Finite diagnostics for L-92200/L-92201.

This verifies exact finite algebra and the enormous numerical margins in the
published-constant inequalities. It does not prove the analytic zero-product
or the external source locks.
"""
from __future__ import annotations
from fractions import Fraction
from decimal import Decimal, getcontext
import json
import math
from pathlib import Path

getcontext().prec = 80


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gsub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def ginv(z):
    n = z[0] * z[0] + z[1] * z[1]
    return (z[0] / n, -z[1] / n)


def gdiv(z, w):
    return gmul(z, ginv(w))


def gpow(z, n):
    out = (Fraction(1), Fraction(0))
    for _ in range(n):
        out = gmul(out, z)
    return out


def gscale(a, z):
    return (a * z[0], a * z[1])


def curvature_direct(t, poles):
    p = (Fraction(0), Fraction(0))
    p1 = (Fraction(0), Fraction(0))
    p2 = (Fraction(0), Fraction(0))
    tz = (t, Fraction(0))
    for weight, pole in poles:
        u = gadd(tz, pole)
        p = gadd(p, gscale(weight, ginv(u)))
        p1 = gadd(p1, gscale(-weight, ginv(gpow(u, 2))))
        p2 = gadd(p2, gscale(2 * weight, ginv(gpow(u, 3))))
    return gsub(gmul(p, p2), gscale(Fraction(2), gmul(p1, p1)))


def curvature_pairwise(t, poles):
    tz = (t, Fraction(0))
    out = (Fraction(0), Fraction(0))
    for wa, sa in poles:
        ua = gadd(tz, sa)
        for wb, sb in poles:
            ub = gadd(tz, sb)
            numerator = gpow(gsub(sa, sb), 2)
            denominator = gmul(gpow(ua, 3), gpow(ub, 3))
            out = gadd(out, gscale(wa * wb, gdiv(numerator, denominator)))
    return out


poles_exact = [
    (Fraction(2), (Fraction(5), Fraction(0))),
    (Fraction(3), (Fraction(7), Fraction(2))),
    (Fraction(3), (Fraction(7), Fraction(-2))),
    (Fraction(1), (Fraction(20), Fraction(0))),
]
t_exact = Fraction(3, 2)
D1 = curvature_direct(t_exact, poles_exact)
D2 = curvature_pairwise(t_exact, poles_exact)
assert D1 == D2
assert D1[1] == 0

w = Fraction(3)
c = Fraction(7)
d = Fraction(2)
t = Fraction(3, 2)
den = ((t + c) * (t + c) + d * d) ** 3
self_negative = -Fraction(8) * w * w * d * d / den
assert self_negative < 0

H = Decimal(3_000_175_332_800)
L = H.ln()
local_count_ratio = (
    (Decimal(2) / Decimal(str(math.pi)) + Decimal("0.224")) * L
    + Decimal("0.556") * L.ln()
    + Decimal("5.020")
) / L
assert local_count_ratio < Decimal(2)

domination_ratio = H * H / (Decimal(2160) * (H + 3).ln())
assert domination_ratio > Decimal("1e20")

separated_pair_angle = Decimal(str(2 * math.atan(0.501))) + Decimal(6) / H
anchor_pair_angle = (
    Decimal(str(2 * math.atan(float(Decimal(3) / (Decimal(2) * H)))))
    + Decimal(str(3 * math.atan(float(Decimal(2) / H))))
)
assert separated_pair_angle < Decimal(str(math.pi / 2))
assert anchor_pair_angle < Decimal("1e-10")


def p_complex(t, poles):
    return sum(weight / (t + pole) for weight, pole in poles)


def curvature_complex(t, poles):
    p = p_complex(t, poles)
    p1 = -sum(weight / (t + pole) ** 2 for weight, pole in poles)
    p2 = 2 * sum(weight / (t + pole) ** 3 for weight, pole in poles)
    return (p * p2 - 2 * p1 * p1).real


Htest = 1000.0
poles = [(2.0, (Htest / 2.0) ** 2)]
for b, a, multiplicity in [
    (Htest + 0.10, 0.49, 2),
    (Htest + 0.35, -0.47, 1),
    (Htest + 1.20, 0.45, 3),
    (Htest + 1.75, -0.40, 2),
]:
    cc = b * b - a * a
    dd = 2 * a * b
    poles.extend(
        [
            (2.0 * multiplicity, complex(cc, dd)),
            (2.0 * multiplicity, complex(cc, -dd)),
        ]
    )

sample_t = [0.25, 1.0, 1e3, 1e6, 1e9, 1e12]
sample_curvature = [curvature_complex(x, poles) for x in sample_t]
assert min(sample_curvature) > 0

result = {
    "status": "PASS_VERIFIED_HEIGHT_THIRD_ORDER_CURVATURE",
    "exact_pairwise_identity": {"real": str(D1[0]), "imag": str(D1[1])},
    "exact_lone_offline_self_term": str(self_negative),
    "published_constant_gates": {
        "H": str(H),
        "local_count_bound_ratio_at_H": float(local_count_ratio),
        "domination_margin_ratio": float(domination_ratio),
        "separated_pair_angle_upper": float(separated_pair_angle),
        "anchor_pair_angle_upper": float(anchor_pair_angle),
    },
    "synthetic_hostile_control": {
        "H_scaled": Htest,
        "sample_t": sample_t,
        "sample_curvature": sample_curvature,
        "minimum_sample_curvature": min(sample_curvature),
    },
}

out = Path(__file__).resolve().parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n")
print(result["status"])
print(json.dumps(result, indent=2, sort_keys=True))

"""Exact supplied-estimate comparison, not an arithmetic lower bound."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json


def require(value, detail):
    if not value:
        raise RuntimeError(detail)


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def scale(c, a):
    return {k: c * v for k, v in a.items() if c * v}


def multiply(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = tuple(sorted(ka + kb))
            out[key] = out.get(key, F(0)) + va * vb
    return {k: v for k, v in out.items() if v}


# Coefficients of independent R, delta, theta and 1; the 1/kappa terms
# are checked as symbolic coefficients rather than sampled kappa values.
e2_lower = {"R": F(1, 2), "1": F(1, 2),
            "theta": F(-1, 2), "delta/kappa": F(-1, 24)}
e4 = {"R": F(3, 4), "1": F(1, 4), "theta": F(-1, 2)}
difference = add(e2_lower, scale(-1, e4))
require(difference == {"R": F(-1, 4), "1": F(1, 4),
                       "delta/kappa": F(-1, 24)}, "N7 subtraction")
require(F(1, 6) - 1 / (24 * F(13, 18)) == F(17, 156),
        "N7 positive endpoint")
require(F(12, 25) < F(13, 18), "critical witness interval")

# Clear the common denominator 4q in N10 and compare coefficients.
# 4q E_2q = (4q-2)R+2+(q-2)kappa-2q theta.
# 4q E_4 = 3qR+q-2q theta.
one, q, r, k, theta = [{name: F(1)} for name in
                       [(), ("q",), ("R",), ("kappa",), ("theta",)]]
q_minus_two = add(q, scale(-2, one))
numerator_high = add(
    add(multiply(add(scale(4, q), scale(-2, one)), r), scale(2, one)),
    add(multiply(q_minus_two, k), scale(-2, multiply(q, theta))))
numerator_fourth = add(
    add(scale(3, multiply(q, r)), q), scale(-2, multiply(q, theta)))
left = add(numerator_high, scale(-1, numerator_fourth))
right = multiply(q_minus_two, add(add(r, k), scale(-1, one)))
require(left == right, "N10 exact polynomial identity")

# Exact endpoint interpolation after introducing m_star. The defining
# relation is K-R-theta0/2 = (delta/2-theta0)*m_star.
delta, t0, t, ms, d, ly = [{(name,): F(1)}
                           for name in ["delta", "theta0", "theta",
                                        "m_star", "d", "l_y"]]
den = add(scale(F(1, 2), delta), scale(-1, t0))
slope = add(multiply(d, add(one, scale(-1, ms))), scale(-1, ly))
shift = add(t, scale(-1, t0))
# E(theta)-E4 and EL-E4, independently from their N(theta) formulas.
e_shift = add(
    multiply(d, scale(-1, multiply(shift, ms))),
    multiply(add(d, scale(-1, ly)), shift))
e_left = add(
    multiply(d, scale(-1, multiply(den, ms))),
    multiply(add(d, scale(-1, ly)), den))
require(multiply(den, e_shift) == multiply(shift, e_left),
        "N16 full endpoint interpolation")
require(e_shift == multiply(shift, slope), "N15 affine segment slope")

# Upper intersection location: denominator/2 - numerator =
# (R+delta-1)/4. Positivity of the numerator follows from N7.
K = add(scale(F(3, 4), r), scale(F(1, 4), one))
num = add(add(K, scale(-1, r)), scale(F(-1, 2), t0))
half_minus_num = add(scale(F(1, 2), den), scale(-1, num))
require(half_minus_num == scale(F(1, 4), add(add(r, delta), scale(-1, one))),
        "N13 intersection lies before half-length")

# q=XY, L=Y: powers in X,Y of all three original direct-Gram terms.
direct_powers = [
    (F(1), F(0)),
    (F(1) - F(1, 6), F(1, 6)),
    (F(1) - 2, 2 - 1),
]
require(direct_powers == [(F(1), F(0)), (F(5, 6), F(1, 6)),
                          (F(-1), F(1))], "N11 normalization")
require(F(1, 2) * F(1, 6) == F(1, 12), "existing b/12 saving")

directory = Path(__file__).resolve().parent
files = ["NUMERATOR_MOMENT_BARRIERS.md", "verify_numerator_barriers.py"]
receipt = {
    "status": "PASS",
    "scope": "Exact comparison of displayed supplied exponents only.",
    "checks": ["second-moment gap", "uniform positive endpoint",
               "critical witness interval", "higher-moment identity",
               "local-buffer endpoint interpolation",
               "intersection location", "direct-Gram normalization"],
    "sha256": {f: sha256((directory / f).read_bytes()).hexdigest() for f in files},
}
(directory / "numerator_barriers.json").write_text(
    json.dumps(receipt, indent=2) + "\n", encoding="utf8")
print(json.dumps(receipt, indent=2))

"""Exact algebra checks only; this does not certify an analytic theorem."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json


def require(condition, detail="exact check failed"):
    if not condition:
        raise RuntimeError(detail)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    # omega**2 = -1-omega
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def scale(n, x):
    return (n * x[0], n * x[1])


def power(x, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def mod9(x):
    return (x[0] % 9, x[1] % 9)


omega = (0, 1)
lam = (1, 2)
one = (1, 0)
zero = (0, 0)
roots = [power(omega, n) for n in range(3)]
units = roots + [scale(-1, x) for x in roots]


def primary(a, b):
    return add(one, add(scale(a, power(lam, 2)), scale(b, power(lam, 3))))


def trace(x):
    return 2 * x[0] - x[1]


checks = {}
classes = {(a, b): mod9(primary(a, b)) for a, b in product(range(3), repeat=2)}
require(len(set(classes.values())) == 9)
for (a, b), c in classes.items():
    require(mod9(power(c, 3)) == one)
    for (u, v), d in classes.items():
        require(mod9(mul(c, d)) == classes[((a + u) % 3, (b + v) % 3)])
    for zeta in units:
        numerator = trace(mul(zeta, add(primary(a, b), (-1, 0))))
        require(numerator % 3 == 0)
        require((numerator // 3) % 3 == (-a * trace(zeta)) % 3)
checks["primary_group_and_additive_profile"] = {
    "classes": 9, "multiplication_pairs": 81, "unit_profile_cases": 54
}


def accumulate(series, index, value):
    series[index] = add(series.get(index, zero), value)
    if series[index] == zero:
        del series[index]


def series_add(target, source):
    for index, value in source.items():
        accumulate(target, index, value)


def series_mul(left, right, cap):
    out = {}
    for (i, j), a in left.items():
        for (u, v), b in right.items():
            if i + u <= cap and j + v <= cap:
                accumulate(out, (i + u, j + v), mul(a, b))
    return out


def subset(mask):
    return [i for i in range(2) if (mask >> i) & 1]


def gauss(mask, reciprocity):
    # A twisted multiplicative model: g(p0)=omega, g(p1)=omega**2.
    out = one
    for i in subset(mask):
        out = mul(out, roots[i + 1])
    if mask == 3:
        out = mul(out, roots[(-reciprocity) % 3])
    return out


def cubic(cmask, kmask, reciprocity):
    if cmask & kmask:
        return zero
    exponent = sum(reciprocity for i in subset(cmask) for j in subset(kmask)
                   if i != j)
    return roots[(-exponent) % 3]  # conjugate cubic symbol


def character(index, values):
    return mul(power(values[0], index[0]), power(values[1], index[1]))


def qseries(kmask, reciprocity, values, cap):
    # The formal variables are p_i**(-w). q_i are formal norm constants.
    square_roots = (2, 5)
    out = {}
    for cmask in range(4):
        if cmask & kmask:
            continue
        for d0, d1 in product(range(cap // 3 + 1), repeat=2):
            if (kmask & 1 and d0) or (kmask & 2 and d1):
                continue
            index = ((cmask & 1) + 3 * d0, ((cmask >> 1) & 1) + 3 * d1)
            if max(index) > cap:
                continue
            coefficient = mul(gauss(cmask, reciprocity),
                              cubic(cmask, kmask, reciprocity))
            coefficient = mul(coefficient, character(index, values))
            coefficient = scale(square_roots[0] ** d0 * square_roots[1] ** d1,
                                coefficient)
            accumulate(out, index, coefficient)
    return out


cap = 10
norms = (4, 25)
formal_cases = 0
for reciprocity in range(3):
    for values in product(units, repeat=2):
        for rmask in range(4):
            # Direct fully completed dual, including signed Ramanujan factors.
            left = {}
            for index, coefficient in qseries(0, reciprocity, values, cap).items():
                ramanujan = 1
                for i in subset(rmask):
                    ramanujan *= norms[i] - 1 if index[i] else -1
                accumulate(left, index, scale(ramanujan, coefficient))
            right = {}
            for kmask in range(4):
                if kmask & ~rmask:
                    continue
                kindex = (kmask & 1, (kmask >> 1) & 1)
                prefactor = mul(gauss(kmask, reciprocity), character(kindex, values))
                prefactor = scale(
                    (norms[0] if kmask & 1 else 1) *
                    (norms[1] if kmask & 2 else 1), prefactor)
                term = series_mul({kindex: prefactor},
                                  qseries(kmask, reciprocity, values, cap), cap)
                for i in subset(rmask & ~kmask):
                    zindex = (3, 0) if i == 0 else (0, 3)
                    qz = scale(norms[i] * (2 if i == 0 else 5),
                               power(values[i], 3))
                    term = series_mul(term, {(0, 0): (-1, 0), zindex: qz}, cap)
                series_add(right, term)
            require(left == right, (reciprocity, values, rmask))
            formal_cases += 1
checks["dual_resummation_formal_series"] = {
    "cases": formal_cases, "prime_variables": 2, "maximum_exponent_each": cap,
    "coefficient_ring": "Z[omega]", "norm_constants": list(norms),
    "scope": "formal algebra, not actual prime enumeration"
}

# Exact rational exponent identities and optimization regions.
for beta in (F(1, 2), F(7, 8), F(9, 10), F(999, 1000), F(1)):
    p = (2 * beta + 1) / 6
    require(F(3, 2) - F(9, 5) * p == 3 * (2 - beta) / 5)
    require(F(1, 2) - F(3, 5) * p == (2 - beta) / 5)
    require(((F(5, 6) - p) /
            (F(3, 2) - F(9, 5) * p)) == F(5, 9))
    require((p + F(3, 2) - F(4, 5) * p) / 2 == F(3, 4) + p / 10)
p = F(11, 24)
require(F(3, 2) - F(4, 5) * p == F(17, 15))
require(F(1, 2) - F(3, 5) * p == F(9, 40))
require(F(3, 4) + p / 10 == F(191, 240))
require(F(5, 6) - F(191, 240) == F(3, 80))
require(F(5, 6) - F(4, 5) == F(1, 30))
for sigma in (F(1, 3), F(11, 24), F(1, 2), F(9, 16)):
    # Cube powers after applying the three original large-sieve terms.
    require(F(1, 2) - 3 * sigma - 3 * (F(1, 2) - sigma) == -1)
    require(F(1, 2) - 3 * sigma - 3 * (1 - sigma) == F(-5, 2))
    require(F(1, 2) - 3 * sigma - 3 * (F(5, 6) - sigma) == -2)
    # Y = B^(4/5) R^(3/5) H^(6/5): cubic and dual terms match.
    left = (F(1, 3) + F(4, 5) * (F(5, 6) - sigma),
            F(3, 5) * (F(5, 6) - sigma),
            F(6, 5) * (F(5, 6) - sigma))
    right = (1 - F(4, 5) * sigma,
             F(1, 2) - F(3, 5) * sigma,
             1 - F(6, 5) * sigma)
    require(left == right)
checks["rational_exponents"] = "passed"

directory = Path(__file__).resolve().parent
files = ["AVERAGED_TYPE_I.md", "QUADRATIC_TWIST_EXTENSION.md",
         "DUAL_RESUMMATION.md", "verify_type_i.py"]
receipt = {
    "status": "PASS",
    "scope": "Exact finite algebra and exponent checks only; no analytic proof certification.",
    "checks": checks,
    "sha256": {name: sha256((directory / name).read_bytes()).hexdigest() for name in files},
}
(directory / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n",
                                             encoding="utf8")
print(json.dumps(receipt, indent=2))

#!/usr/bin/env python3
"""Exact algebra checks for POSITIVE_PRIMITIVE_ANGULAR_M2.md.

Only Python's standard library is required. The inversion check is an
exact polynomial certificate: each cleared entry has degree at most
three in each of x,b,y, and vanishes on a four-point tensor grid.

These checks do not prove the spectral/elliptic arguments, and do not
claim any sparse cube-indexed moment or zero-free improvement.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path


@dataclass(frozen=True)
class G:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, G) else G(F(x))

    def __add__(self, other):
        v = self.coerce(other)
        return G(self.a + v.a, self.b + v.b)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) + (-self)

    def __mul__(self, other):
        v = self.coerce(other)
        return G(self.a * v.a - self.b * v.b,
                 self.a * v.b + self.b * v.a)

    __rmul__ = __mul__

    def conj(self):
        return G(self.a, -self.b)


def mat(rows):
    return [[G.coerce(x) for x in row] for row in rows]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def scale(c, a):
    return [[G.coerce(c) * a[i][j] for j in range(2)] for i in range(2)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]


def sum_mat(ms):
    out = mat([[0, 0], [0, 0]])
    for m in ms:
        out = add(out, m)
    return out


checks = {}


def require(name, condition):
    if not condition:
        raise RuntimeError(name)
    checks[name] = checks.get(name, 0) + 1


I = G(F(0), F(1))
sig = [mat([[0, 1], [1, 0]]),
       mat([[0, -I], [I, 0]]),
       mat([[1, 0], [0, -1]])]

# Inversion w -> (-bar(z)/r^2, y/r^2), with j* = N/r.
# Multiply its three principal-symbol identities by r^5/y and its
# zero-order identity by r^3. Every resulting entry is a polynomial
# of degree <=3 in each coordinate. The 4x4x4 grid is therefore a
# complete identity certificate, not a floating-point spot check.
for x, b, y in product(range(-1, 3), repeat=3):
    r2 = x * x + b * b + y * y
    coords = [x, b, y]
    n = mat([[x - I * b, y], [-y, x + I * b]])
    dn = [mat([[1, 0], [0, 1]]),
          mat([[-I, 0], [0, I]]),
          mat([[0, 1], [-1, 0]])]
    for k in range(3):
        sign = -1 if k == 0 else 1
        lhs = sum_mat(
            scale(sign * ((r2 if a == k else 0) - 2 * coords[k] * coords[a]),
                  mul(sig[a], n))
            for a in range(3)
        )
        rhs = scale(r2, mul(n, sig[k]))
        for i, j in product(range(2), repeat=2):
            require("dirac_inversion_principal", lhs[i][j] == rhs[i][j])
    first = scale(y, sum_mat(
        mul(sig[a], add(scale(r2, dn[a]), scale(-coords[a], n)))
        for a in range(3)
    ))
    zero = add(add(first, scale(-r2, mul(sig[2], n))),
               scale(r2, mul(n, sig[2])))
    for i, j in product(range(2), repeat=2):
        require("dirac_inversion_zero_order", zero[i][j] == G())

# Formal first-column Dirac identity from the two Bessel recurrences.
# A and B stand for K_nu and K_(nu+1); no numerical special-function
# evaluation is being used.
for nu, a, b, rr, phase in product(range(-2, 3), [1, 3], [2, 5], [1, 7],
                                   [G(1), G(-1), I, -I]):
    f1, f2 = -I * phase * a, G(-b)
    v1 = -I * phase * ((F(1, 2) + nu) * a - rr * b)
    v2 = G((F(1, 2) + nu) * b + rr * a)
    d1 = -I * v1 + rr * phase * f2
    d2 = rr * phase.conj() * f1 + I * v2
    eig = -I * (nu + F(1, 2))
    require("dirac_fourier_column_1", d1 == eig * f1)
    require("dirac_fourier_column_1", d2 == eig * f2)

# The coefficient reconstruction is exactly the scalar Wronskian
# combination once the common arithmetic coefficient is on the right.
for phase, rr, ip, ii, kn, kn1 in product([G(1), G(-1), I, -I],
                                          [1, 3], [2, 7], [3, 5],
                                          [1, 4], [2, 9]):
    aa, bb = I * phase.conj() * rr * ip, G(rr * ii)
    k11, k21 = -I * phase * kn, G(-kn1)
    require("wronskian_column_algebra",
            aa * k11 - bb * k21 == G(rr * (ip * kn + ii * kn1)))

# One-prime all-row decomposition and the exact norm scale.
# Each valuation class is affine in its fourth-power exponent; the
# range below checks every class and several repetitions.
for valuation in range(65):
    rem = valuation % 4
    aa = int(rem == 1)
    bb = int(rem == 2)
    cc = int(rem == 3)
    dd = int(rem == 0 and valuation > 0)
    r4 = (valuation - aa - 2 * bb - 3 * cc - 4 * dd) // 4
    require("canonical_valuation",
            min(r4, aa, bb, cc, dd) >= 0 and
            aa + 2 * bb + 3 * cc + 4 * dd + 4 * r4 == valuation)
    for ee in range(bb + 1):
        for ff in range(dd + 1):
            nval = aa + 2 * (bb - ee) + 3 * cc + 2 * ff
            original = nval + 2 * ee + 2 * ff + 4 * (dd - ff) + 4 * r4
            require("primitive_reindex", original == valuation)

# Exact exponents. Two distinct sigma values certify each affine
# equality; the additional samples record its intended analytic range.
for sigma in [F(1), F(9, 8), F(5, 4), F(3, 2), F(2)]:
    e_amp = F(5, 2) - 3 * sigma
    f_amp = F(1, 2) - sigma
    require("e_sum_exponent", 2 * e_amp - 2 == 3 - 6 * sigma)
    require("f_sum_exponent", 2 * f_amp - 2 == -1 - 2 * sigma)
    require("external_Q_exponent", 2 * f_amp + 2 == 3 - 2 * sigma)
    require("convergent_scale_sums", 3 - 6 * sigma <= -3 and -1 - 2 * sigma <= -3)

# On every residue class of the quartic symbol, the inverse orientation
# is cubic. The arithmetic angular factor cancels out of this test.
for chi in [G(1), G(-1), I, -I]:
    chi3 = chi * chi * chi
    require("cube_character_orientation", chi3.conj() == chi)
    require("cube_character_orientation", chi3 == chi.conj())

root = Path(__file__).resolve().parent
note = root / "POSITIVE_PRIMITIVE_ANGULAR_M2.md"
report = {
    "status": "PASS",
    "note_sha256": sha256(note.read_bytes()).hexdigest(),
    "check_count": sum(checks.values()),
    "checks": checks,
    "scope": "Exact matrix/Dirac algebra and primitive row exponents only",
    "polynomial_certificate": (
        "Dirac inversion only: the displayed cleared principal-symbol and "
        "zero-order expressions have degree at most three in each of x,b,y; "
        "vanishing on the four-point tensor grid therefore proves those "
        "polynomial identities. The finite Bessel-recurrence checks are "
        "algebra samples, not an analytic special-function proof."
    ),
    "not_certified": ["analytic continuation and elliptic estimates",
                      "sparse cube-indexed mean square",
                      "zero-free boundary improvement"],
}
out = root / "positive_angular_check_report.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))

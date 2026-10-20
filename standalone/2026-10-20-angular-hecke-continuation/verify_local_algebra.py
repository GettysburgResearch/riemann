#!/usr/bin/env python3
"""Exact finite algebra only; not a verifier of the analytic theorems.

Run with Python 3.10+ and no third-party dependencies. Acceptance uses
explicit exceptions, and is unchanged by Python's -O option.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
import json


def require(condition, message):
    if not condition:
        raise ValueError(message)


@dataclass(frozen=True)
class G:
    """A Gaussian rational with exact real and imaginary coordinates."""
    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other):
        return G(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def conjugate(self):
        return G(self.re, -self.im)


ZERO, ONE, I, HALF = G(), G(Q(1)), G(Q(0), Q(1)), G(Q(1, 2))
Z = ((ZERO, ZERO), (ZERO, ZERO))
E = ((ZERO, ONE), (ZERO, ZERO))
F = ((ZERO, ZERO), (ONE, ZERO))
W = ((ZERO, -ONE), (ONE, ZERO))


def scale(c, a):
    return tuple(tuple(c * a[j][k] for k in range(2)) for j in range(2))


def add(a, b):
    return tuple(tuple(a[j][k] + b[j][k] for k in range(2))
                 for j in range(2))


def multiply(a, b):
    return tuple(tuple(sum((a[j][k] * b[k][l] for k in range(2)), ZERO)
                       for l in range(2)) for j in range(2))


def bracket(a, b):
    return add(multiply(a, b), scale(-ONE, multiply(b, a)))


def adjoint(a):
    return tuple(tuple(a[k][j].conjugate() for k in range(2))
                 for j in range(2))


def pair_scale(c, a):
    return tuple(scale(c, x) for x in a)


def pair_add(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def real_embedding(z, a):
    # sl2(C) as a REAL Lie algebra, then complexified to two factors.
    return scale(z, a), scale(z.conjugate(), a)


def component(a, sign):
    return pair_scale(HALF, pair_add(
        real_embedding(ONE, a),
        pair_scale(G(Q(0), Q(sign)), real_embedding(I, a))))


def pair_bracket(a, b):
    return tuple(bracket(x, y) for x, y in zip(a, b))


def weyl(a):
    return tuple(multiply(multiply(W, x), scale(-ONE, W)) for x in a)


def polynomial(coefficients, x):
    result = Q(0)
    for coefficient in coefficients:
        result = result * x + coefficient
    return result


def interval_multiply(a, b):
    values = [x * y for x in a for y in b]
    return min(values), max(values)


def interval_polynomial(coefficients, x):
    result = (Q(0), Q(0))
    for coefficient in coefficients:
        lo, hi = interval_multiply(result, x)
        result = lo + coefficient, hi + coefficient
    return result


def affine_interval(interval, slope, intercept=Q(0)):
    values = [slope * x + intercept for x in interval]
    return min(values), max(values)


def interval_json(interval):
    return [str(x) for x in interval]


def rational_polynomial_add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out


def rational_polynomial_multiply(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def run_checks():
    ep, em, fp, fm = (component(a, s) for a, s in
                      ((E, -1), (E, 1), (F, -1), (F, 1)))
    require(ep == (E, Z) and em == (Z, E), "E factor separation")
    require(fp == (F, Z) and fm == (Z, F), "F factor separation")
    require(pair_bracket(ep, fm) == (Z, Z), "[E+,F-]=0")
    require(pair_bracket(em, fp) == (Z, Z), "[E-,F+]=0")
    require(pair_bracket(ep, fp) != (Z, Z), "same-factor mutation")
    require(pair_bracket(em, fm) != (Z, Z), "other same-factor mutation")
    require(weyl(ep) == pair_scale(-ONE, fp), "Ad(w)E+=-F+")
    require(weyl(em) == pair_scale(-ONE, fm), "Ad(w)E-=-F-")
    for z in (ONE, I):
        compact = add(scale(z, E), scale(-z.conjugate(), F))
        require(adjoint(compact) == scale(-ONE, compact), "su(2) identity")

    # Exact affine formula, followed by representative degrees.
    # For EVERY integer m>=0, a_m=m/2+1/3 >= 1/3 and b_m=m/2+2/3.
    shifts = {m: (Q(m, 2) + Q(1, 3), Q(m, 2) + Q(2, 3))
              for m in (0, 1, 2, 6)}
    require(shifts[0] == (Q(1, 3), Q(2, 3)), "spherical shifts")
    require(shifts[1] == (Q(5, 6), Q(7, 6)), "source degree-one shifts")
    require(shifts[2] == (Q(4, 3), Q(5, 3)), "Gaussian example shifts")
    require(Q(1, 3) > Q(1, 4) and not Q(1, 3) > Q(1, 3),
            "strip is strict; endpoint mutation")

    # Gaussian pullback: a=(1,-1), lambda=(1,1). The matrix with
    # these columns has nonzero determinant, so no real (h,c), except
    # (0,0), can satisfy h*a=c*lambda. This is not finite-h sampling.
    angular, eisenstein = (1, -1), (1, 1)
    determinant = angular[0] * eisenstein[1] - angular[1] * eisenstein[0]
    require(determinant == 2, "Gaussian all-power nonresonance")
    theta = tuple(a - b for a, b in zip(angular, eisenstein))
    require(theta == (0, -2) and any(theta), "one surviving degree")
    require(not any((0, 0)), "all-spherical angular cancellation unavailable")

    coefficients = (133488, -376596, 384534, -167541, 26231)
    root = (Q(874886647039963, 10**15), Q(874886647039965, 10**15))
    values = tuple(polynomial(coefficients, x) for x in root)
    derivative = interval_polynomial((533952, -1129788, 769068, -167541), root)
    require(values[0] * values[1] < 0, "quartic strict sign change")
    require(derivative[0] > 0 or derivative[1] < 0, "unique bracketed root")
    require(Q(1, 2) < root[0] < root[1] < Q(7, 8), "root domain")

    protection = affine_interval(root, Q(1, 6), Q(1, 2))
    type_i_x = affine_interval(root, Q(1, 3), Q(1, 6))
    type_i_r = affine_interval(root, Q(-1, 6), Q(5, 12))
    require(protection[1] < Q(47, 72) < Q(2, 3), "principal improvement")
    require(type_i_x[1] < Q(11, 24) < Q(1, 2), "Type-I improvement")
    for beta, p, q, threshold in (
        (Q(11, 12), Q(17, 36), Q(19, 72), Q(26, 57)),
        (Q(7, 8), Q(11, 24), Q(13, 48), Q(6, 13)),
    ):
        require((2 * beta + 1) / 6 == p, "Type-I X substitution")
        require((5 - 2 * beta) / 12 == q == (1 - p) / 2,
                "Type-I level substitution")
        require((Q(5, 6) - p) / (1 + q - p) == threshold,
                "short-divisor threshold substitution")
        require((1 - p) / (1 + q - p) == Q(2, 3), "linear-saving threshold")

    # F_q(1)<2 for every real q>=2, not a finite prime test.
    # Set x=sqrt(q)>1 and clear the positive denominator x^2(x^5-1):
    # (2*x^2-1)(x^5-1)+(x^4-1) = 2*x^2(x^5-1)-(x^5-x^4).
    left = rational_polynomial_add(
        rational_polynomial_multiply([-1, 0, 2], [-1, 0, 0, 0, 0, 1]),
        [-1, 0, 0, 0, 1])
    right = rational_polynomial_add(
        rational_polynomial_multiply([0, 0, 2], [-1, 0, 0, 0, 0, 1]),
        [0, 0, 0, 0, 1, -1])
    require(left == right, "dual local rational-function identity")

    return {
        "accepted": True,
        "scope": "Exact finite Lie algebra, rational identities, and one isolated quartic root; no analytic theorem is certified.",
        "arithmetic": "Gaussian rationals and rational interval arithmetic; no floating point",
        "lie_algebra": {
            "model": "complexification of real sl2(C) as two sl2(C) factors",
            "opposite_factor_brackets": "zero",
            "same_factor_negative_controls": "nonzero",
            "weyl_and_compact_identities": "verified",
            "not_verified": "existence or automorphic realization of the exceptional representation",
        },
        "mellin_shifts": {str(m): interval_json(pair) for m, pair in shifts.items()},
        "gaussian_example": {"angular": angular, "eisenstein": eisenstein,
                             "theta": theta, "determinant": determinant},
        "quartic": {"coefficients_descending": coefficients,
                    "isolating_interval": interval_json(root),
                    "endpoint_values": interval_json(values),
                    "derivative_interval": interval_json(derivative)},
        "principal_threshold_interval": interval_json(protection),
        "type_i_X_exponent_interval": interval_json(type_i_x),
        "type_i_level_exponent_interval": interval_json(type_i_r),
        "dual_local_identity": "F_q(1)=2-(q^(5/2)-q^2)/(q*(q^(5/2)-1))<2 for q>=2; monotonicity in s>=1 is proved in the review",
        "unverified_analytic_inputs": [
            "Liu's exceptional representation, local tables, sieves, and contour assembly",
            "the angular and balanced-unitary moment and continuation proofs",
            "the source tangent comparison certificates and global zero-free theorem",
            "Dunn-Radziwill's functional equation and analytic continuation",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))

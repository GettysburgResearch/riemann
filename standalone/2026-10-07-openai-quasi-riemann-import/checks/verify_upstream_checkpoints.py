#!/usr/bin/env python3
"""Exact selected checkpoints in OpenAI math family 003; Python stdlib only.

Upstream commit: adc7f1241b42e322a6451854ab7e4b4c146bf78a
Run: python3 verify_upstream_checkpoints.py

This selective algebra audit is NOT an end-to-end verification of the papers
or their Lean formalization. It does not verify analytic estimates, infinite
sums, uniformity, contour shifts, or induction admissibility.
"""

from fractions import Fraction as Q
import json
import math

UPSTREAM_COMMIT = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
checks = []
VARIABLES = ("theta", "H", "X", "F", "B", "delta", "x", "y", "s")
ZERO_EXP = (0,) * len(VARIABLES)


class Laurent:
    """Small exact sparse Laurent-polynomial ring for these identities."""
    def __init__(self, terms):
        self.terms = {e: Q(c) for e, c in terms.items() if c}

    @staticmethod
    def const(c):
        return Laurent({ZERO_EXP: c})

    @staticmethod
    def var(name):
        exponents = list(ZERO_EXP)
        exponents[VARIABLES.index(name)] = 1
        return Laurent({tuple(exponents): 1})

    @staticmethod
    def lift(other):
        return other if isinstance(other, Laurent) else Laurent.const(other)

    def __add__(self, other):
        terms = self.terms.copy()
        for e, c in self.lift(other).terms.items():
            terms[e] = terms.get(e, 0) + c
        return Laurent(terms)

    __radd__ = __add__

    def __neg__(self):
        return Laurent({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        terms = {}
        for e1, c1 in self.terms.items():
            for e2, c2 in self.lift(other).terms.items():
                e = tuple(a + b for a, b in zip(e1, e2))
                terms[e] = terms.get(e, 0) + c1 * c2
        return Laurent(terms)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            assert len(self.terms) == 1, "Only monomials are invertible here"
            e, c = next(iter(self.terms.items()))
            return Laurent({tuple(n * a for a in e): c ** n})
        result = Laurent.const(1)
        for _ in range(n):
            result = result * self
        return result

    def __truediv__(self, other):
        return self * (self.lift(other) ** -1)

    def substitute(self, name, value):
        index = VARIABLES.index(name)
        result = Laurent.const(0)
        for e, c in self.terms.items():
            retained = list(e)
            retained[index] = 0
            result += Laurent({tuple(retained): c}) * self.lift(value) ** e[index]
        return result


def exact(name, expression, source):
    assert not Laurent.lift(expression).terms, (name, Laurent.lift(expression).terms)
    checks.append({"name": name, "kind": "symbolic_identity", "source": source})


def require(name, condition, source):
    assert condition, name
    checks.append({"name": name, "kind": "exact_inequality", "source": source})


theta, H, X, F, B, delta, x, y, s = map(Laurent.var, VARIABLES)
row_exponent = 1 + theta
amplifier_exponent = row_exponent / 6
exact("sixth_power_extraction_square_exponent",
      2 + theta - amplifier_exponent - (Q(11, 6) + 5 * theta / 6),
      "Oct5 eq:prime-extract")
exact("sixth_power_extraction_sum_exponent",
      (2 + theta - amplifier_exponent) / 2 - (Q(11, 12) + 5 * theta / 12),
      "Oct5 eq:prime-extract")
exact("sixth_power_extraction_error_exponent",
      2 - 2 * amplifier_exponent - (Q(5, 3) - theta / 3), "Oct5 eq:prime-extract")
for divides in (0, 1):
    exact(f"common_support_prime_cancellation_{divides}",
          (1 + divides) - divides - (1 - divides) - divides,
          "Oct5 Lemma 7.3 (lem:second-transfer), signed preimage regrouping")
Sigma, L = X * F, X / B  # B is the positive norm of the cube divisor cubed.
child_bound = H * L / (Sigma * F)
exact("child_row_scale", child_bound - H / (B * F ** 2), "Oct5 eq:transfer-scales")
exact("cutoff_contraction_boundary",
      child_bound.substitute("B", X ** 2 / H ** 2) - H * (H / Sigma) ** 2,
      "Oct5 Proposition 5.1 (prop:canonical), induction")

lx, ly, ell, h, imbalance = Q(17, 48), Q(23, 48), Q(1, 6), Q(13, 16), Q(1, 8)
exact("compensated_geometry", h - (1 - lx + ell), "Sep30 old-eq:5.1")
exact("compensated_low_exponent", lx / 2 + imbalance / 12 - Q(3, 16),
      "Sep30 Proposition 15.3, old-eq:5.10")
exact("compensated_mellin_exponent", lx / 2 + s - 1 + h / 6 - (s - Q(11, 16)),
      "Sep30 old-eq:5.11")

alpha = Q(5, 6)
Dx = 3 - Q(17, 9) * x
Px = (2 - Q(8, 9) * x) * (1 - x)
J = (alpha - delta) * Dx + delta * Px
# t=1+delta*Px/(2J); clear 2*J*Dx in R_short(t)-R_long(t).
exact("balanced_row_count_crossing_cleared",
      delta * Px * J - delta ** 2 * Px ** 2 - (alpha - delta) * delta * Px * Dx,
      "Sep30 Proposition 19.2 and eq:target-cutoff")
# R*=1-delta+(alpha-delta)*delta*Px/(2J), E=C0+2delta/3+xdelta/6-h(1-R*).
negative_E_times_J = J * (Q(1, 48) - 2 * delta / 3 - x * delta / 6 + h * delta)
negative_E_times_J -= h * (alpha - delta) * delta * Px / 2
Jy = J.substitute("x", Q(1, 2) - y)
negative_EJ_y = negative_E_times_J.substitute("x", Q(1, 2) - y)
v = 51 + 41 * y
certificate = ((3 + 5 * y) * ((4 * v * delta - 79) ** 2 + 49)
               + 4 * y * (4 * v * delta
                          * ((1 + 3 * y) * (15 + 32 * y) * delta + 9 - 13 * y)
                          + 265 + 3485 * y))
exact("positive_endpoint_certificate", 10368 * v * negative_EJ_y - certificate,
      "Sep30 Lemma 20.2, eq:balanced-endpoint-certificate")
exact("endpoint_denominator_polynomial",
      108 * Jy - (185 + 170 * y + (-138 + 12 * y + 96 * y ** 2) * delta),
      "Sep30 Lemma 20.2")
require("endpoint_positive_linear_factor", 9 - 13 * Q(1, 2) == Q(5, 2),
        "Sep30 Lemma 20.2, 0 <= y <= 1/2")
exact("endpoint_ratio_bound", 17 * (3 + 5 * y) - v - 44 * y,
      "Sep30 Lemma 20.2, v <= 17(3+5y)")
exact("Dx_lower_endpoint", Dx.substitute("x", Q(1, 2)) - Q(37, 18),
      "Sep30 Lemma 20.2, Dx decreases on [0,1/2]")
exact("Dx_upper_endpoint", Dx.substitute("x", 0) - 3, "Sep30 Lemma 20.2")
exact("Px_lower_endpoint", Px.substitute("x", Q(1, 2)) - Q(7, 9),
      "Sep30 Lemma 20.2, Px decreases on [0,1/2]")
exact("Px_upper_endpoint", Px.substitute("x", 0) - 2, "Sep30 Lemma 20.2")
require("J_lower_bound", alpha * Q(7, 9) == Q(35, 54),
        "Sep30 Lemma 20.2, J/alpha is a convex combination of Dx and Px")
require("J_upper_bound", alpha * 3 == Q(5, 2), "Sep30 Lemma 20.2")
require("certificate_margin", Q(49, 440640) > Q(1, 10000), "Sep30 Lemma 20.2")
exact("adaptive_margin", 1 - h / 4 - Q(51, 64), "Sep30 eq:adaptive-endpoint")
exact("prime_supply_margin", ell / h - Q(7, 37) - Q(23, 1443),
      "Sep30 Proposition 19.2 and Section 20")
exact("floor_margin", -Q(1, 48) + Q(3, 4) / 50 + Q(7, 1200), "Sep30 eq:floor-bound")
exact("intermediate_margin", -Q(529, 2400) + Q(25, 96) * alpha + Q(49, 14400),
      "Sep30 eq:adaptive-intermediate")


# Exact finite-prime spot checks of the Oct5 Gauss conversion (eq:convert2).
# For n=a+b*omega of prime norm p, all sums live in Q(zeta_(6p)). Multiplying
# the normalized identity by p removes its square roots. The remaining
# integral polynomial must vanish modulo Phi_(6p). Both conjugate primary
# generators are checked above each of seven rational split primes.
def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b:
                    result[i + j] += a * b
    return trim(result)


def sub(p, q):
    result = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        result[i] += a
    for i, a in enumerate(q):
        result[i] -= a
    return trim(result)


def divmod_monic(p, q):
    p = p.copy()
    assert q[-1] == 1
    quotient = [0] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and any(p):
        degree, coefficient = len(p) - len(q), p[-1]
        quotient[degree] += coefficient
        for j, a in enumerate(q):
            p[degree + j] -= coefficient * a
        trim(p)
    return trim(quotient), trim(p)


def monomial(exponent, coefficient=1):
    return [0] * exponent + [coefficient]


def primary_generators(p):
    radius = math.isqrt(2 * p) + 2
    return [(a, b) for a in range(-radius, radius + 1)
            for b in range(-radius, radius + 1)
            if a * a - a * b + b * b == p and (a - 1) % 3 == 0 and b % 3 == 0]


def gauss_polynomial(p, a, b, j):
    order = 6 * p
    omega_mod_p = (-a * pow(b, -1, p)) % p
    sixth_root_mod_p = (1 + omega_mod_p) % p
    char_log = {pow(sixth_root_mod_p, k, p): k for k in range(6)}
    assert len(char_log) == 6
    values = {u: char_log[pow(u, (p - 1) // 6, p)] for u in range(1, p)}
    coefficients = [0] * order
    for u, k in values.items():
        coefficients[(p * k * j - 6 * b * u) % order] += 1
    return trim(coefficients), values


prime_cases = []
for p in (7, 13, 19, 31, 37, 43, 61):
    generators = primary_generators(p)
    assert len(generators) == 2, (p, generators)
    # Phi_(6p)(z) = Phi_6(z^p)/Phi_6(z) for primes p not dividing 6.
    numerator = [0] * (2 * p + 1)
    numerator[0], numerator[p], numerator[2 * p] = 1, -1, 1
    cyclo, cyclo_remainder = divmod_monic(numerator, [1, -1, 1])
    assert cyclo_remainder == [0]
    for a, b in generators:
        tau_minus, logs = gauss_polynomial(p, a, b, -1)
        tau_2, _ = gauss_polynomial(p, a, b, 2)
        tau_3, _ = gauss_polynomial(p, a, b, 3)
        chi4_conj = monomial((-p * logs[4]) % (6 * p))
        chi_minus = monomial(p * logs[p - 1])
        n_conj = monomial(4 * p, b)
        n_conj[0] = a
        negative_lhs = [-a for a in mul(mul(tau_minus, tau_3), chi4_conj)]
        rhs = mul(mul(chi_minus, n_conj), tau_2)
        _, remainder = divmod_monic(sub(negative_lhs, rhs), cyclo)
        assert remainder == [0], (p, a, b, remainder)
        prime_cases.append({"norm": p, "primary_generator": [a, b]})
checks.append({"name": "gauss_conversion_split_prime_cases", "kind": "exact_cyclotomic_reduction",
               "source": "Oct5 eq:convert2 and Appendix A.1", "cases": prime_cases})

print(json.dumps({"upstream_commit": UPSTREAM_COMMIT, "status": "PASS",
                  "scope": "Selected algebraic checkpoints only; not an analytic or Lean proof audit",
                  "check_count": len(checks), "checks": checks}, indent=2))

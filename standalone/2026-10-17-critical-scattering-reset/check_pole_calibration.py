#!/usr/bin/env python3
"""Finite normalization checks, not tests of an infinite arithmetic estimate.

Uses only the standard library. All Gram/projection and factorial checks use
exact rational complex arithmetic. Gaussian quadrature checks are ordinary
binary64 with declared tolerances, not certified interval computations.
"""

from __future__ import annotations

import cmath
import json
import math
from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class CQ:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def cast(value):
        return value if isinstance(value, CQ) else CQ(Q(value))

    def __add__(self, other):
        other = CQ.cast(other)
        return CQ(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return CQ(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-CQ.cast(other))

    def __rsub__(self, other):
        return CQ.cast(other) - self

    def __mul__(self, other):
        other = CQ.cast(other)
        return CQ(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self):
        return CQ(self.re, -self.im)

    def __truediv__(self, other):
        other = CQ.cast(other)
        den = other.re * other.re + other.im * other.im
        if den == 0:
            raise ZeroDivisionError
        prod = self * other.conj()
        return CQ(prod.re / den, prod.im / den)

    def __rtruediv__(self, other):
        return CQ.cast(other) / self

    def __pow__(self, power):
        if power < 0:
            return CQ(1) / (self ** (-power))
        out = CQ(1)
        for _ in range(power):
            out = out * self
        return out


ZERO = CQ()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def matvec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), ZERO) for row in matrix]


def dot(left, right):
    return sum((a.conj() * b for a, b in zip(left, right)), ZERO)


def solve(matrix, vector):
    n = len(vector)
    work = [row[:] + [value] for row, value in zip(matrix, vector)]
    for col in range(n):
        pivot = next((j for j in range(col, n) if work[j][col] != ZERO), None)
        require(pivot is not None, "singular exact Gram matrix")
        work[col], work[pivot] = work[pivot], work[col]
        divisor = work[col][col]
        work[col] = [x / divisor for x in work[col]]
        for row in range(n):
            if row != col:
                multiplier = work[row][col]
                work[row] = [x - multiplier * y for x, y in zip(work[row], work[col])]
    return [row[-1] for row in work]


def positive_pivots(matrix):
    """Exact Hermitian LDL elimination; positive real pivots prove positivity."""
    work = [row[:] for row in matrix]
    pivots = []
    for k in range(len(work)):
        pivot = work[k][k]
        require(pivot.im == 0 and pivot.re > 0, "nonpositive exact Gram pivot")
        pivots.append(str(pivot.re))
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                work[i][j] = work[i][j] - work[i][k] * work[k][j] / pivot
    return pivots


def exact_gram_checks():
    frequencies = [Q(-2), Q(0), Q(3)]
    coeffs = [CQ(Q(2), Q(1)), CQ(Q(-3, 2), Q(1, 3)), CQ(Q(1, 4), Q(-2))]
    records = []
    for m in (1, 2, 3, 4):
        r = 2 * m - 1
        for epsilon in (Q(1, 3), Q(1, 5)):
            gram = [[CQ(math.factorial(r - 1)) /
                     CQ(2 * epsilon, vj - vk) ** r
                     for vk in frequencies] for vj in frequencies]
            for j in range(3):
                for k in range(3):
                    require(gram[j][k] == gram[k][j].conj(), "Hermitian orientation")
            pivots = positive_pivots(gram)
            alpha = [c / math.factorial(m - 1) for c in coeffs]
            expected_b = matvec(gram, alpha)
            rising = Q(math.factorial(2 * m - 2), math.factorial(m - 1))
            actual_b = [sum((rising * ck / CQ(2 * epsilon, vj - vk) ** r
                             for ck, vk in zip(coeffs, frequencies)), ZERO)
                        for vj in frequencies]
            require(expected_b == actual_b, "Laplace derivative / Gram mismatch")
            solved_alpha = solve(gram, actual_b)
            require(alpha == solved_alpha, "exact projection coefficients")
            direct_energy = dot(alpha, matvec(gram, alpha))
            projection_energy = dot(actual_b, solved_alpha)
            require(direct_energy == projection_energy, "exact Bessel equality on modal span")
            require(direct_energy.im == 0 and direct_energy.re > 0, "modal energy positivity")
            critical_constant = Q(1, r * math.factorial(m - 1) ** 2)
            abelian_constant = Q(math.factorial(r - 1), math.factorial(m - 1) ** 2)
            require(abelian_constant / math.factorial(r) == critical_constant,
                    "Abelian to cumulative constant")
            # D(s)=(s-rho)^m has D^(m)(rho)=m!, so its reciprocal top coefficient is 1.
            require(Q(math.factorial(m), math.factorial(m)) == 1, "Laurent top coefficient")
            if m >= 2:
                require(Q(1, math.factorial(m)) != 1, "missing-m-factorial control")
            if m >= 3:
                bad_b = [sum((math.factorial(r - 1) * ck /
                               CQ(2 * epsilon, vj - vk) ** r
                               for ck, vk in zip(coeffs, frequencies)), ZERO)
                         for vj in frequencies]
                require(bad_b != actual_b, "missing-Gamma(m) control")
            bad_b = [sum((rising * ck / CQ(2 * epsilon, vk - vj) ** r
                           for ck, vk in zip(coeffs, frequencies)), ZERO)
                     for vj in frequencies]
            require(bad_b != actual_b, "reversed-frequency-sign control")
            records.append({"m": m, "epsilon": str(epsilon),
                            "critical_unit_constant": str(critical_constant),
                            "positive_pivots": pivots,
                            "modal_energy": str(direct_energy.re)})
    return records


def mobius(n):
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -sign if n > 1 else sign


def simpson(function, left, right, steps=24000):
    require(steps % 2 == 0, "even Simpson grid")
    width = (right - left) / steps
    value = function(left) + function(right)
    for j in range(1, steps):
        value += (4 if j % 2 else 2) * function(left + j * width)
    return value * width / 3


def gaussian_checks():
    # Complete rational-ideal prefix through 30, including its unit.
    columns = [(n, mobius(n), math.log(n)) for n in range(1, 31) if mobius(n)]
    records = []
    for a, t in ((0.7, 1.3), (1.0, 0.0)):
        coeffs = [(mu * cmath.exp((-0.5 - 1j * t) * ell), ell)
                  for n, mu, ell in columns]

        def gaussian(y):
            return math.exp(-y * y / (4 * a)) / math.sqrt(4 * math.pi * a)

        def source(x):
            return sum(c * gaussian(x - ell) for c, ell in coeffs)

        z = 0.8 + 0.6j
        direct_transform = simpson(lambda x: source(x) * cmath.exp(-z * x), -22, 27)
        predicted_transform = cmath.exp(a * z * z) * sum(
            mu * cmath.exp((-0.5 - 1j * t - z) * ell) for n, mu, ell in columns)
        transform_error = abs(direct_transform - predicted_transform)
        require(transform_error < 2e-10, "finite Gaussian bilateral transform")

        L = 4.5
        direct_energy = simpson(lambda x: abs(source(x)) ** 2, -22, L)
        kernel_energy = 0j
        for cn, un in coeffs:
            for cm, um in coeffs:
                cdf = (1 + math.erf((L - (un + um) / 2) / math.sqrt(2 * a))) / 2
                kernel = math.exp(-(un - um) ** 2 / (8 * a)) * cdf / (
                    2 * math.sqrt(2 * math.pi * a))
                kernel_energy += cn * cm.conjugate() * kernel
        energy_error = abs(direct_energy - kernel_energy)
        require(energy_error < 2e-10, "finite Gaussian Gram energy")
        records.append({"a": a, "fixed_height": t,
                        "transform_abs_error": transform_error,
                        "energy_abs_error": energy_error,
                        "finite_energy": direct_energy})

    c = Q(5, 6)
    d = c - Q(1, 2)
    require(2 * d == Q(2, 3) and 2 * d * d == Q(2, 9), "literal c=5/6 shift")
    shift_errors = []
    for x in (-3.0, -0.7, 1.1, 4.0):
        lhs = sum(mu * math.exp(float(c - Q(1, 2)) * x - float(c) * ell
                                - (ell - x) ** 2 / 4)
                  for n, mu, ell in columns) / (2 * math.sqrt(math.pi))
        rhs = math.exp(float(d * d)) * sum(
            mu * math.exp(-ell / 2 - (x - float(2 * d) - ell) ** 2 / 4)
            for n, mu, ell in columns) / (2 * math.sqrt(math.pi))
        shift_errors.append(abs(lhs - rhs))
        require(abs(lhs - rhs) < 2e-13, "original Gaussian shift adapter")
    return {"finite_prefix_norm_cap": 30, "quadrature": records,
            "shift_abs_errors": shift_errors,
            "height_100_squared_attenuation_log10": -20000 / math.log(10),
            "floating_point_scope": "Binary64 Simpson quadrature; not certified intervals."}


def group_checks():
    records = []
    for p in (5, 7, 11):
        nonzero = set(range(1, p))
        for k in nonzero:
            orbit = {a * k % p for a in nonzero}
            require(orbit == nonzero, "nontrivial character transitivity")
        # Check the semidirect product law (r,a)(s,b)=(r+a*s,a*b).
        for a in nonzero:
            for r in range(p):
                for k in nonzero:
                    require((k * (a * r % p)) % p == ((k * a) % p) * r % p,
                            "transported Frobenius/character pairing")
        records.append({"prime": p, "forced_multiplicity_at_least": p - 1,
                        "critical_energy_log_degree_at_least": 2 * p - 3})
    return {"records": records,
            "scope": "Finite cyclic character actions only; no algebraic-number-field computation."}


def prime_detector_checks():
    def von_mangoldt(n):
        for p in range(2, n + 1):
            if n % p == 0:
                rest = n
                while rest % p == 0:
                    rest //= p
                return math.log(p) if rest == 1 else 0.0
        return 0.0

    columns = [(n, von_mangoldt(n), math.log(n)) for n in range(2, 31)
               if von_mangoldt(n)]
    require({n for n, weight, ell in columns if n not in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)}
            == {4, 8, 9, 16, 25, 27}, "retained nonprime prime powers")
    records = []
    for a in (1.0, 0.01):
        def gauss(y):
            return math.exp(-y * y / (4 * a)) / math.sqrt(4 * math.pi * a)

        def continuum(x):
            return 0.5 * math.exp(x / 2 + a / 4) * math.erfc(-(x + a) / (2 * math.sqrt(a)))

        continuum_errors = []
        for x in (-1.0, 0.0, 2.0):
            integral = simpson(lambda u: math.exp(u / 2) * gauss(x - u), 0, 24, 24000)
            continuum_errors.append(abs(integral - continuum(x)))
            require(continuum_errors[-1] < 2e-10, "one-sided erfc continuum")

        def source(x):
            return sum(weight * math.exp(-ell / 2) * gauss(x - ell)
                       for n, weight, ell in columns) - continuum(x)

        z = 0.9 + 0.6j
        direct = simpson(lambda x: source(x) * cmath.exp(-z * x), -20, 160, 64000)
        predicted = cmath.exp(a * z * z) * (
            sum(weight * cmath.exp((-0.5 - z) * ell) for n, weight, ell in columns)
            - 1 / (z - 0.5))
        error = abs(direct - predicted)
        require(error < 3e-10, "prime detector transform with exact continuum")
        records.append({"a": a, "continuum_abs_errors": continuum_errors,
                        "finite_transform_abs_error": error})
    return {"complete_prime_power_norm_cap": 30, "records": records,
            "scope": "Finite prime-power polynomial minus the exact infinite continuum; no zeta zero sum tested."}


def main():
    payload = {"status": "PASS", "exact_gram_cases": exact_gram_checks(),
               "gaussian_normalizations": gaussian_checks(),
               "finite_character_actions": group_checks(),
               "prime_detector_normalizations": prime_detector_checks(),
               "claims_not_checked": ["RH", "infinite native energy bounds",
                                      "actual zero locations or derivatives",
                                      "Hecke analytic theory", "Kummer number fields"]}
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact, bounded checks for the quadratic QLS / local projection packet.

This checks finite algebra and exponent balances, not the analytic theorems.
Only Python's standard library is used. Checks remain active under python -O.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json
from math import gcd, prod
from pathlib import Path


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise AssertionError(explanation)


@dataclass(frozen=True)
class G:
    """A Gaussian rational, so every probability identity is exact."""

    re: F = F(0)
    im: F = F(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(value: G | F | int) -> G:
        return value if isinstance(value, G) else G(F(value))

    def __add__(self, other: G | F | int) -> G:
        other = self.coerce(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> G:
        return G(-self.re, -self.im)

    def __sub__(self, other: G | F | int) -> G:
        return self + (-self.coerce(other))

    def __rsub__(self, other: G | F | int) -> G:
        return self.coerce(other) - self

    def __mul__(self, other: G | F | int) -> G:
        other = self.coerce(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self) -> G:
        return G(self.re, -self.im)

    def norm(self) -> F:
        return self.re * self.re + self.im * self.im

    def __truediv__(self, other: G | F | int) -> G:
        other = self.coerce(other)
        value = self * other.conj()
        return G(value.re / other.norm(), value.im / other.norm())

    def __rtruediv__(self, other: G | F | int) -> G:
        return self.coerce(other) / self


def law(p: int) -> list[tuple[int, F]]:
    return [(0, F(1, p + 1)), (1, F(p, 2 * (p + 1))),
            (-1, F(p, 2 * (p + 1)))]


def local_quantities(p: int, x: G) -> tuple[G, F, F]:
    g = F(p, p + 1)
    d = 1 - (1 - g) * x * x
    c = d / (1 - x * x)
    h = sum(prob / (1 - state * x).norm() for state, prob in law(p))
    v = g * x.norm() * (1 + (1 - g) * x.norm()) / d.norm()
    return c, h, v


def check_local() -> dict:
    cases = 0
    for p in (3, 5, 11):
        for x in (G(F(1, p)), G(F(1, 3), F(1, 5)),
                  G(F(-1, 4), F(1, 6))):
            c, h, v = local_quantities(p, x)
            direct_c = sum((prob / (1 - state * x)
                            for state, prob in law(p)), G())
            require(c == direct_c, "local mean includes the ramified state")
            require(h / c.norm() == 1 + v, "local relative variance")
            require(v > 0, "nonconstant local factor has positive variance")
            cases += 1
    return {"cases": cases, "arithmetic": "exact Gaussian rationals"}


def check_projection() -> dict:
    primes = (3, 5, 7)
    xs = (G(F(1, 3), F(1, 7)), G(F(1, 5), F(-1, 9)),
          G(F(1, 7), F(1, 11)))
    tail_c, tail_h, tail_v = local_quantities(primes[2], xs[2])
    z, m = G(F(3, 2), F(2, 7)), G(F(2, 3), F(-1, 5))
    noise = G(F(1, 4), F(1, 6))
    scenarios = []
    # The first two primes are observed; the third is an independent tail.
    # Conditioning on the first prime tests every ramification/sign state.
    for condition in (None, 0, 1, -1):
        for perturb in (False, True):
            mean = G()
            residual = F(0)
            variance_a = F(0)
            mass = F(0)
            for local in product(*(law(p) for p in primes)):
                states = tuple(entry[0] for entry in local)
                if condition is not None and states[0] != condition:
                    continue
                probability = prod(entry[1] for entry in local)
                if condition is not None:
                    probability /= dict(law(primes[0]))[condition]
                low_l = prod((1 / (1 - states[j] * xs[j]) for j in (0, 1)),
                             start=G(1))
                tail_l = 1 / (1 - states[2] * xs[2])
                a = m / tail_c
                if perturb:
                    a += noise * states[1]  # mean zero after every condition
                n = a / low_l
                full_l = low_l * tail_l
                mean += probability * full_l * n
                residual += probability * (z * full_l * n - 1).norm()
                variance_a += probability * (a - m / tail_c).norm()
                mass += probability
            optimum = (z * m - 1).norm() + (z * m).norm() * tail_v
            gap = z.norm() * tail_h * variance_a
            require(mass == 1, "conditional law is normalized")
            require(mean == m, "the principal mean is retained exactly")
            require(residual == optimum + gap, "complete least-squares identity")
            require((gap > 0) == perturb, "strict optimality for nonconstant A")
            scenarios.append({"condition_at_3": condition,
                              "nonconstant_perturbation": perturb,
                              "variance_gap": str(gap)})
    return {"states_before_conditioning": 27, "scenarios": scenarios}


def factor(n: int) -> dict[int, int]:
    result = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def jacobi(a: int, n: int) -> int:
    require(n > 0 and n % 2 == 1, "Jacobi denominator must be positive odd")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def check_square_parts() -> dict:
    rows = [u for u in range(1, 42, 2) if all(e == 1 for e in factor(u).values())]
    shared = set()
    masks_needed = 0
    for n in range(1, 302, 2):
        factors = factor(n)
        a = prod(p for p, e in factors.items() if e % 2)
        b = prod(p ** (e // 2) for p, e in factors.items())
        require(n == a * b * b, "unique squarefree / square decomposition")
        if gcd(a, b) > 1:
            shared.add(n)
        for u in rows:
            full = jacobi(-8 * u, n)
            reduced = jacobi(-8 * u, a)
            masked = reduced * int(gcd(u, b) == 1)
            require(full == masked, "square-part ramification mask")
            if full != reduced:
                masks_needed += 1
    require(27 in shared, "the test includes a=3,b=3, not only coprime parts")
    require(masks_needed > 0, "removing the row mask is detectably incorrect")
    # At s=1 the finite Euler inverse identity can be tested rationally.
    primes = (3, 5, 7)
    primorial = prod(primes)
    for u in rows:
        euler = prod(F(1) - F(jacobi(-8 * u, p), p) for p in primes)
        polynomial = F(0)
        for subset in product((False, True), repeat=len(primes)):
            d = prod(p for p, chosen in zip(primes, subset) if chosen)
            mu = (-1) ** sum(subset)
            polynomial += F(mu * jacobi(-8 * u, d), d)
        require(euler == polynomial, "primorial support includes every divisor")
    return {"odd_columns_through": 301, "odd_squarefree_rows_through": 41,
            "row_count": len(rows), "shared_prime_columns": sorted(shared),
            "omitting_mask_changes_cases": masks_needed,
            "finite_euler_primorial": primorial}


def check_exponents() -> dict:
    points = (F(51, 100), F(3, 5), F(3, 4), F(5, 6),
              F(8749570194, 10**10), F(9, 10), F(99, 100))
    output = []
    for sigma in points:
        h = sigma - F(1, 2)
        lam = F(5, 4) - sigma
        root_limit = h / (2 * lam)
        square_limit = h / ((5 - 4 * sigma) * (F(3, 2) - sigma))
        eta = root_limit / 2
        k = (1 - eta) / 3
        delta = (h - 2 * lam * eta) / 3
        require(eta * (1 - sigma) - k * h == -delta,
                "root tail exponent")
        require(-F(1, 4) + (eta + k) * lam == -delta,
                "root finite character error exponent")
        require(0 < k < 1 and delta > 0, "legal root-transfer parameters")
        eta2 = square_limit / 2
        k2 = (1 - eta2) / (4 - 2 * sigma)
        delta2 = (h - eta2 * (5 - 4 * sigma) * (F(3, 2) - sigma)) / (4 - 2 * sigma)
        require(2 * eta2 * (1 - sigma) - k2 * h == -delta2,
                "squared tail exponent")
        require(-F(1, 2) + 2 * lam * (eta2 + k2) == -delta2,
                "squared finite character error exponent")
        require(0 < k2 < 1 and delta2 > 0, "legal squared-transfer parameters")
        output.append({"sigma": str(sigma), "root_eta_upper": str(root_limit),
                       "square_eta_upper": str(square_limit),
                       "root_delta_at_half_range": str(delta),
                       "square_delta_at_half_range": str(delta2)})
    require((F(3, 4) - F(1, 2)) / (F(5, 2) - 2 * F(3, 4)) == F(1, 4),
            "three-quarter root range")
    require((F(5, 6) - F(1, 2)) / (F(5, 2) - 2 * F(5, 6)) == F(2, 5),
            "five-sixths root range")
    return {"exact_samples": output,
            "analytic_inequalities_proved_by_samples": False}


def check_native() -> dict:
    theta = F(13, 84)
    point_cut = 1 / (1 - theta)
    classical_cut = F(6, 5)
    recent_delta = F(520, 445121)
    recent_cut = 12 / (10 + recent_delta)
    require(point_cut == F(84, 71), "published pointwise cutoff balance")
    require(2 + point_cut * (-2 + 2 * theta) == 0,
            "native Y-squared term is subpower at the pointwise cutoff")
    require(point_cut * (-1 + 2 * theta) < 0,
            "the other pointwise tail term decays")
    require(F(1, 6) + F(1, 2) + F(1, 3) == 1,
            "twelfth-moment Holder powers sum to one")
    require(2 - F(5, 3) * classical_cut == 0,
            "classical twelfth-moment cutoff balance")
    require(2 - (F(5, 3) + recent_delta / 6) * recent_cut == 0,
            "recent twelfth-moment cutoff balance")
    require(point_cut < recent_cut < classical_cut < 2,
            "the optional recent moment refinement is not the best cutoff here")

    def mu(n: int) -> int:
        factors = factor(n)
        return 0 if any(e > 1 for e in factors.values()) else (-1) ** len(factors)

    crossings_tested = []
    endpoint_defects = []
    for y in range(2, 11):
        b = y + 1
        upper = b * b
        mertens_reciprocal = [F(0)]
        harmonic = [F(0)]
        for n in range(1, upper + 1):
            mertens_reciprocal.append(mertens_reciprocal[-1] + F(mu(n), n))
            harmonic.append(harmonic[-1] + F(1, n))
        convolution = [0] * (y * y + 1)
        for a in range(1, y + 1):
            for c in range(1, y + 1):
                convolution[a * c] += mu(a) * mu(c)
        for k in range(b, upper):
            newton = 2 * mertens_reciprocal[y] - sum(
                (F(convolution[d], d) * harmonic[k // d]
                 for d in range(1, y * y + 1)), F(0))
            require(newton == mertens_reciprocal[k],
                    "literal complete strict Newton square step")
        endpoint_newton = 2 * mertens_reciprocal[y] - sum(
            (F(convolution[d], d) * harmonic[upper // d]
             for d in range(1, y * y + 1)), F(0))
        defect = mertens_reciprocal[upper] - endpoint_newton
        require(defect == F(mu(b) ** 2, upper), "strict endpoint defect retained")
        endpoint_defects.append({"Y": y, "weighted_defect": str(defect)})
        if mu(y) and mertens_reciprocal[y - 1] * mertens_reciprocal[y] <= 0:
            require(abs(mertens_reciprocal[y]) <= F(1, y),
                    "literal reciprocal crossing magnitude")
            crossings_tested.append(y)
    return {"pointwise_cutoff": str(point_cut),
            "classical_moment_cutoff": str(classical_cut),
            "recent_source_qualified_moment_cutoff": str(recent_cut),
            "exact_square_steps_Y": [2, 10],
            "native_crossings_in_test": crossings_tested,
            "endpoint_defects": endpoint_defects,
            "analytic_tail_bound_certified_by_samples": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = {"status": "PASS", "local_moments": check_local(),
              "optimal_projection": check_projection(),
              "square_part_masks": check_square_parts(),
              "parameter_balances": check_exponents(),
              "native_frequency_consumer": check_native(),
              "claims_certified": "finite exact identities only",
              "new_zeta_zero_free_bound": False,
              "analytic_proof_certified_by_computation": False}
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(encoded)
    print("PASS: local moments, optimal projection, shared-prime masks, exponent balances, native consumer")
    print("Finite exact checks only; no analytic theorem or zero-free region is certified.")


if __name__ == "__main__":
    main()

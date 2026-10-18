#!/usr/bin/env python3
"""Exact, bounded checks for PROOF.md. Standard library only.

The arithmetic is int/Fraction, including complex rational Euler variables.
Finite probability models test algebra; they do not certify an infinite Euler
product, a family asymptotic, an approximate functional equation, or RH.
The final conductor table is an observation with exact finite arithmetic.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class QC:
    re: F = F(0)
    im: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, QC) else QC(F(x))

    def __add__(self, other):
        other = QC.of(other)
        return QC(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return QC(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-QC.of(other))

    def __rsub__(self, other):
        return QC.of(other) - self

    def __mul__(self, other):
        other = QC.of(other)
        return QC(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def conjugate(self):
        return QC(self.re, -self.im)

    def __truediv__(self, other):
        other = QC.of(other)
        den = other.norm2()
        if not den:
            raise ZeroDivisionError("exact complex zero")
        ans = self * other.conjugate()
        return QC(ans.re / den, ans.im / den)

    def __rtruediv__(self, other):
        return QC.of(other) / self

    def __pow__(self, n):
        if n < 0:
            return QC(1) / (self ** (-n))
        ans, base = QC(1), self
        while n:
            if n & 1:
                ans = ans * base
            base = base * base
            n //= 2
        return ans


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n):
    fac = factor(n)
    return 0 if any(e > 1 for e in fac.values()) else (-1) ** len(fac)


def jacobi(a, n):
    require(n > 0 and n % 2 == 1, "Jacobi denominator must be positive odd")
    a %= n
    ans = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                ans = -ans
        a, n = n, a
        if a % 4 == n % 4 == 3:
            ans = -ans
        a %= n
    return ans if n == 1 else 0


def chi_actual(u, n):
    return 0 if n % 2 == 0 else jacobi(-8 * u, n)


def a_from_local(u, n):
    ans = 1
    for p, e in factor(n).items():
        c = chi_actual(u, p)
        ans *= -(1 + c) if e == 1 else c if e == 2 else 0
    return ans


def product(values, one=1):
    ans = one
    for x in values:
        ans *= x
    return ans


def finite_states(primes):
    for values in itertools.product((-1, 0, 1), repeat=len(primes)):
        state = dict(zip(primes, values))
        prob = product(F(p, 2 * (p + 1)) if state[p] else F(1, p + 1)
                       for p in primes)
        yield state, prob


def chi_state(state, n):
    return product(state.get(p, 0) ** e for p, e in factor(n).items())


def g(n):
    return product((F(p, p + 1) for p in factor(n)), F(1))


def sf_support(n, primes):
    fac = factor(n)
    return all(p in primes and e == 1 for p, e in fac.items())


def smooth_support(n, primes):
    return all(p in primes for p in factor(n))


def critical_energy(prefix, endpoint):
    endpoint = F(endpoint)
    ans = F(0)
    for j in range(1, math.ceil(endpoint)):
        hi = min(F(j + 1), endpoint)
        if hi > j:
            ans += prefix[j] ** 2 * (F(1, j) - 1 / hi)
    return ans


def check_inverse_coefficients():
    fields = (1, 3, 5, 7, 11, 13, 15, 21, 35, 105)
    for u in fields:
        require(u % 2 == 1 and mobius(u) != 0, "invalid fundamental discriminant")
        for n in range(1, 241):
            convolution = sum(mobius(d) * mobius(n // d) * chi_actual(u, n // d)
                              for d in range(1, n + 1) if n % d == 0)
            require(convolution == a_from_local(u, n),
                    f"full inverse coefficient mismatch: u={u}, n={n}")
    return {"fields": len(fields), "all_integer_indices_through": 240,
            "includes": ["ramification at 2", "odd ramification", "split p^2", "inert p^2"]}


def check_native_moments():
    primes, bound = (3, 5, 7), 10
    mu = [0] + [mobius(n) for n in range(1, bound + 1)]
    mertens, acc = [0], 0
    for n in range(1, bound + 1):
        acc += mu[n]
        mertens.append(acc)
    states = list(finite_states(primes))
    require(sum(prob for _, prob in states) == 1, "probabilities do not sum to one")
    sources = []
    for state, prob in states:
        source = [0]
        for x in range(1, bound + 1):
            source.append(sum(mu[m] * chi_state(state, m) * mertens[x // m]
                              for m in range(1, x + 1)))
        sources.append((source, prob))
    for x in range(1, bound + 1):
        mean = sum(prob * source[x] for source, prob in sources)
        require(mean == mertens[x], f"native mean mismatch at {x}")
    for x, y in itertools.product((3, 6, 10), repeat=2):
        direct = sum(prob * source[x] * source[y] for source, prob in sources)
        diagonal = sum(g(m) * mertens[x // m] * mertens[y // m]
                       for m in range(1, min(x, y) + 1) if sf_support(m, primes))
        require(direct == diagonal, f"native covariance mismatch at {x},{y}")
    direct_energy = sum(prob * critical_energy(source, bound) for source, prob in sources)
    diagonal_energy = sum(g(m) / m * critical_energy(mertens, F(bound, m))
                          for m in range(1, bound + 1) if sf_support(m, primes))
    require(direct_energy == diagonal_energy, "critical energy dilation identity mismatch")
    rational_energy = critical_energy(mertens, bound)
    multiplier = sum(g(m) / m for m in range(1, bound + 1) if sf_support(m, primes))
    require(rational_energy <= direct_energy <= multiplier * rational_energy,
            "finite critical capture inequalities failed")
    return {"finite_prime_model": list(primes), "states": len(states),
            "all_native_means_through": bound, "covariance_points": [3, 6, 10],
            "ordinary_critical_energy": str(rational_energy),
            "family_critical_energy": str(direct_energy),
            "retained_dilation_multiplier": str(multiplier)}


def check_full_residual():
    primes, bound = (3, 5, 7), 30
    all_primes = [n for n in range(2, bound + 1) if factor(n) == {n: 1}]
    # Formal multiplicative variables; deliberately complex to test conjugation.
    xp = {p: QC(F(1, p + 1), F(1 if p % 4 == 1 else -1, 2 * p + 3))
          for p in all_primes}
    weight = lambda n: product((xp[p] ** e for p, e in factor(n).items()), QC(1))
    rational_m = [QC()]
    for n in range(1, bound + 1):
        rational_m.append(rational_m[-1] + mobius(n) * weight(n))
    local_c, tp, vp = {}, {}, {}
    for p in primes:
        gp, x = F(p, p + 1), xp[p]
        dp = 1 - (1 - gp) * x * x
        local_c[p] = dp / (1 - x * x)
        tp[p] = gp * x * x / dp
        vp[p] = gp * x.norm2() * (1 + (1 - gp) * x.norm2()) / dp.norm2()
    c = product(local_c.values(), QC(1))
    tv = lambda n: product((tp[p] ** e for p, e in factor(n).items()), QC(1))
    vv = lambda n: product((vp[p] for p in factor(n)), F(1))
    radicals = [n for n in range(1, product(primes) + 1)
                if sf_support(n, primes)]
    states = list(finite_states(primes))

    def mollifier(state, cutoff):
        return sum((mobius(n) * chi_state(state, n) * weight(n) * rational_m[cutoff // n]
                    for n in range(1, cutoff + 1) if sf_support(n, primes)), QC())

    def s_component(cutoff, r):
        return sum((mobius(n) * tv(n // math.gcd(n, r)) * rational_m[cutoff // n]
                    for n in range(1, cutoff + 1) if sf_support(n, primes)), QC())

    scalar = QC(F(7, 5), F(-2, 5))
    for cutoff in (1, 3, 8, 15, 30):
        samples, corrected_samples = [], []
        for state, prob in states:
            lvalue = product((1 / (1 - state[p] * xp[p]) for p in primes), QC(1))
            y = lvalue * mollifier(state, cutoff)
            corrected_m = sum((tv(b) * mollifier(state, cutoff // b)
                               for b in range(1, cutoff + 1) if smooth_support(b, primes)), QC()) / c
            samples.append((y, prob))
            corrected_samples.append((lvalue * corrected_m, prob))
        expected = sum((prob * y for y, prob in samples), QC())
        predicted = c * s_component(cutoff, 1)
        require(expected == predicted, f"full-product mean mismatch X={cutoff}")
        direct = sum(prob * (scalar * y - 1).norm2() for y, prob in samples)
        rhs = (scalar * predicted - 1).norm2()
        rhs += (scalar * c).norm2() * sum(vv(r) * s_component(cutoff, r).norm2()
                                        for r in radicals if r > 1)
        require(direct == rhs, f"positive full residual decomposition mismatch X={cutoff}")
        corrected_mean = sum((prob * y for y, prob in corrected_samples), QC())
        require(corrected_mean == rational_m[cutoff], f"square-alias removal mismatch X={cutoff}")
        require(sum(prob * (QC() * y - 1).norm2() for y, prob in samples) == 1,
                "common-zero residual must be exactly one")
        # Direct inverse convolution, independent of the field-state average.
        recovered = sum((tv(b) * s_component(cutoff // b, 1)
                         for b in range(1, cutoff + 1) if smooth_support(b, primes)), QC())
        require(recovered == rational_m[cutoff], f"causal inverse failed X={cutoff}")
    return {"finite_prime_model": list(primes), "states": len(states),
            "cutoffs": [1, 3, 8, 15, 30], "arithmetic": "complex rational",
            "checked": ["mean with ramified square aliases", "all nonnegative variance components",
                        "zero common scalar", "explicit de-biased mollifier", "causal inverse"]}


def actual_family_observations():
    bound, table = 20, []
    mertens = [0]
    for n in range(1, bound + 1):
        mertens.append(mertens[-1] + mobius(n))
    limiting_energy = sum(g(m) / m * critical_energy(mertens, F(bound, m))
                          for m in range(1, bound + 1) if m % 2 and mobius(m))
    for q in (100, 1000, 10000):
        count = total_end = 0
        sums_of_squares = [0] * (bound + 1)
        for u in range(q + 1, 2 * q + 1):
            if u % 2 == 0 or mobius(u) == 0:
                continue
            count += 1
            acc = 0
            for n in range(1, bound + 1):
                acc += a_from_local(u, n)
                sums_of_squares[n] += acc * acc
            total_end += acc
        family_energy = sum(F(sums_of_squares[j], count) * (F(1, j) - F(1, j + 1))
                            for j in range(1, bound))
        table.append({"Q": q, "actual_fields": count,
                      "mean_A_20_minus_M_20": str(F(total_end, count) - mertens[bound]),
                      "critical_energy_minus_limiting_diagonal": str(family_energy - limiting_energy)})
    return {"scope": "finite observations, not a proof of a limiting rate",
            "horizon": bound, "limiting_critical_diagonal": str(limiting_energy), "table": table}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"status": "PASS", "arithmetic_contract": "exact integers and fractions; no tolerances",
              "inverse_coefficients": check_inverse_coefficients(),
              "native_mean_covariance_energy": check_native_moments(),
              "full_residual_and_debiasing": check_full_residual(),
              "actual_discriminant_observations": actual_family_observations(),
              "not_certified": ["infinite products", "analytic family limits", "approximate functional equation",
                                "all-horizon upper cancellation", "zero-free strip", "RH"]}
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()

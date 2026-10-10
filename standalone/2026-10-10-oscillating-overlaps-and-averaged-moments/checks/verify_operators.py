#!/usr/bin/env python3
"""Finite exact checks of the mean-removal algebra over Eisenstein ideals.

This authenticates finite divisor counts, convolution coefficients and Gram
matrices. It does not verify an infinite operator bound or a moment estimate.
Only the Python standard library is required. Checks remain active under -O.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import isqrt
import json


COUNTS = {}


def require(predicate, category, witness):
    COUNTS[category] = COUNTS.get(category, 0) + 1
    if not predicate:
        raise ArithmeticError((category, witness))


@dataclass(frozen=True)
class C6:
    """Q(zeta_6), represented as a + b*zeta_6, zeta_6^2=zeta_6-1."""

    a: Q = Q(0)
    b: Q = Q(0)

    @staticmethod
    def lift(value):
        return value if isinstance(value, C6) else C6(Q(value), Q(0))

    def __add__(self, other):
        other = self.lift(other)
        return C6(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return C6(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.lift(other)

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        other = self.lift(other)
        a, b, c, d = self.a, self.b, other.a, other.b
        return C6(a*c - b*d, a*d + b*c + b*d)

    __rmul__ = __mul__

    def conjugate(self):
        return C6(self.a + self.b, -self.b)

    def norm(self):
        return self.a*self.a + self.a*self.b + self.b*self.b

    def inverse(self):
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError
        c = self.conjugate()
        return C6(c.a/n, c.b/n)

    def __truediv__(self, other):
        return self * self.lift(other).inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        answer = C6(Q(1))
        base = self
        while exponent:
            if exponent & 1:
                answer = answer * base
            base = base * base
            exponent //= 2
        return answer


ZERO, ONE, ZETA = C6(), C6(Q(1)), C6(Q(0), Q(1))
UNITS = ((1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1))


def emul(x, y):
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def enorm(x):
    a, b = x
    return a*a - a*b + b*b


def canonical(x):
    return min(emul(x, unit) for unit in UNITS)


def lattice_ideals(bound):
    radius = isqrt(2*bound) + 1
    ideals = set()
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            x = (a, b)
            if 0 < enorm(x) <= bound:
                ideals.add(canonical(x))
    return sorted(ideals, key=lambda x: (enorm(x), x))


def zeta_coefficient(n):
    # Independent rational-prime factorization count for zeta_K.
    result, prime = 1, 2
    while prime*prime <= n:
        exponent = 0
        while n % prime == 0:
            n //= prime
            exponent += 1
        if exponent:
            if prime % 3 == 1:
                result *= exponent + 1
            elif prime % 3 == 2 and exponent % 2:
                return 0
        prime += 1
    if n > 1:
        if n % 3 == 1:
            result *= 2
        elif n % 3 == 2:
            return 0
    return result


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    value = ZERO
    for j, entry in enumerate(matrix[0]):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        value += ((-1)**j) * entry * det(minor)
    return value


def main():
    roots = [ZETA**j for j in range(6)]
    for z in roots:
        require(z**6 == ONE, "cyclotomic_roots", z)
        require(z*z.conjugate() == ONE, "cyclotomic_roots", z)

    cap = 512
    ideals = lattice_ideals(cap)
    by_norm = [0] * (cap + 1)
    for v in ideals:
        by_norm[enorm(v)] += 1
    J = [0] * (cap + 1)
    for n in range(1, cap + 1):
        require(by_norm[n] == zeta_coefficient(n), "independent_ideal_counts", n)
        J[n] = J[n-1] + by_norm[n]

    # Actual split prime ideals (7, omega-2) and (13, omega-3).
    primes = ((7, 2), (13, 3))
    flags = {}
    for v in ideals:
        flags[v] = tuple((v[0] + omega*v[1]) % p == 0 for p, omega in primes)
        for p, omega in primes:
            original = (v[0] + omega*v[1]) % p == 0
            require((omega*omega + omega + 1) % p == 0,
                    "prime_ideal_embedding", (p, omega))
            for unit in UNITS:
                x = emul(v, unit)
                require(((x[0] + omega*x[1]) % p == 0) == original,
                        "unit_invariant_masks", (v, p, unit))

    ranges = (1, 2, 3, 7, 13, 26, 49, 91, 128, 256, 512)
    for Y in ranges:
        bases = [v for v in ideals if enorm(v) <= Y]
        for e7, e13 in product(range(5), repeat=2):
            radical = (7 if e7 else 1) * (13 if e13 else 1)
            actual = sum((not e7 or flags[v][0]) and (not e13 or flags[v][1]) for v in bases)
            predicted = J[Y // radical] if radical <= Y else 0
            require(actual == predicted, "exact_replica_divisibility", (Y, e7, e13))
            # The coefficient in the average of the literal geometric masks.
            eta_d = ZETA**(e7 + 5*e13)
            direct = sum((eta_d for v in bases
                          if (not e7 or flags[v][0]) and (not e13 or flags[v][1])), ZERO)
            require(direct / len(bases) == eta_d * Q(predicted, len(bases)),
                    "mean_operator_coefficients", (Y, e7, e13))

    inverse_checks = []
    for p in (3, 7, 13, 19):
        for eta in roots + [ZERO]:
            order = 16
            mean = [ONE] + [eta**j * Q(1, p) for j in range(1, order + 1)]
            inv = [ONE] + [-eta**j * Q(1, p) * Q(p-1, p)**(j-1)
                           for j in range(1, order + 1)]
            for j in range(order + 1):
                convolution = sum((mean[i]*inv[j-i] for i in range(j+1)), ZERO)
                require(convolution == (ONE if j == 0 else ZERO),
                        "explicit_local_inverse", (p, eta, j))
            inverse_checks.append((p, str(eta.a), str(eta.b)))

    # Actual finite-base Gram matrices of three distinct real Mellin modes.
    # These verify finite positivity only, independently of the infinite proof.
    gram_determinants = {}
    for Y in (1, 7, 13, 91, 256, 512):
        bases = [v for v in ideals if enorm(v) <= Y]
        vectors = []
        for v in bases:
            vector = []
            for sigma in (1, 2, 3):
                response = ONE
                for i, (p, _) in enumerate(primes):
                    if flags[v][i]:
                        eta = ZETA if i == 0 else ZETA**5
                        response /= ONE - eta * Q(1, p**sigma)
                vector.append(response)
            vectors.append(vector)
        gram = [[sum((v[i]*v[j].conjugate() for v in vectors), ZERO) / len(bases)
                 for j in range(3)] for i in range(3)]
        for i, j in product(range(3), repeat=2):
            require(gram[i][j] == gram[j][i].conjugate(), "finite_gram_hermitian", (Y, i, j))
        minors = []
        for size in (1, 2, 3):
            d = det([row[:size] for row in gram[:size]])
            require(d.b == 0 and d.a >= 0, "finite_gram_positive", (Y, size))
            if Y >= 13:
                require(d.a > 0, "finite_mode_separation", (Y, size))
            minors.append(str(d.a))
        gram_determinants[str(Y)] = minors[-1]

    report = {
        "status": "PASS",
        "arithmetic": "integers and fractions in Q(zeta_6); no floating point",
        "checks": COUNTS,
        "total_checks": sum(COUNTS.values()),
        "ideal_norm_cap": cap,
        "ideal_count_at_cap": len(ideals),
        "base_cutoffs": ranges,
        "split_prime_ideals": [{"rational_prime": p, "omega_residue": w} for p, w in primes],
        "local_inverse_max_exponent": 16,
        "finite_gram_determinants": gram_determinants,
        "scope": "Finite local inverses, actual ideal divisibility counts, and finite Gram matrices only; not an infinite moment or zero-free proof.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

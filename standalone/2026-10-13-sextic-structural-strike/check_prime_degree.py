#!/usr/bin/env python3
"""Finite exact checks of the distinct-moment partition identity and masks.

All complex arithmetic is in Q(sqrt(-3)). These are finite algebra checks,
not a proof of the prime ideal theorem, an asymptotic row lower bound, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path


class Q3:
    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, other):
        if not isinstance(other, Q3):
            other = Q3(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Q3) else Q3(-other))

    def __mul__(self, other):
        if not isinstance(other, Q3):
            other = Q3(other)
        return Q3(self.a * other.a - 3 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            raise ValueError("only nonnegative powers are used")
        out = Q3(1)
        for _ in range(n):
            out = out * self
        return out

    def conjugate(self):
        return Q3(self.a, -self.b)

    def norm(self):
        return self.a * self.a + 3 * self.b * self.b

    def __eq__(self, other):
        if not isinstance(other, Q3):
            other = Q3(other)
        return self.a == other.a and self.b == other.b


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def partitions(n):
    if n == 0:
        yield ()
        return
    for part in partitions(n - 1):
        yield part + ((n - 1,),)
        for i in range(len(part)):
            yield part[:i] + (part[i] + (n - 1,),) + part[i + 1:]


def partition_coefficient(part):
    return math.prod((-1) ** (len(block) - 1) * math.factorial(len(block) - 1)
                     for block in part)


def direct_distinct(vector, k):
    out = Q3()
    indices = range(len(vector))
    for union in itertools.combinations(indices, 2 * k):
        for left in itertools.combinations(union, k):
            left_set = set(left)
            right = tuple(i for i in union if i not in left_set)
            z = Q3(1)
            for i in left:
                z *= vector[i]
            for i in right:
                z *= vector[i].conjugate()
            out += z * math.factorial(k) ** 2
    return out


def partition_distinct(vector, k, parts, wrong_factorial=False):
    power_sums = {}
    for r in range(2 * k + 1):
        for s in range(2 * k + 1 - r):
            if r + s:
                power_sums[r, s] = sum((z ** r * z.conjugate() ** s
                                       for z in vector), Q3())
    out = Q3()
    for part in parts:
        z = Q3(1)
        for block in part:
            r = sum(i < k for i in block)
            s = len(block) - r
            z *= power_sums[r, s]
        coeff = (math.prod((-1) ** (len(block) - 1) for block in part)
                 if wrong_factorial else partition_coefficient(part))
        out += z * coeff
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    proof_bytes = args.proof.read_bytes()
    roots = tuple(Q3(F(1, 2), F(1, 2)) ** i for i in range(6))
    require(roots[0] == 1 and all(z ** 6 == 1 for z in roots), "sixth roots")
    counts = {"partition_identity_vectors": 0, "explicit_collision_inequalities": 0,
              "real_distinct_polynomials": 0, "zero_entries_retained": 0,
              "partition_total_absolute_weights": 0,
              "sixth_power_finite_field_masks": 0,
              "prime_rooting_coefficient_cases": 0,
              "moment_threshold_rational_cases": 0}
    negative = {"omitted_partition_factorial_detected": False,
                "nonunit_zero_replaced_by_one_detected": False,
                "prime_rooting_missing_minus_detected": False,
                "distinct_polynomial_need_not_be_positive": False}
    for k in range(1, 5):
        parts = list(partitions(2 * k))
        A = math.factorial(2 * k) - 1
        require(sum(abs(partition_coefficient(p)) for p in parts) == A + 1,
                "partition coefficient absolute sum")
        counts["partition_total_absolute_weights"] += 1
        lengths = [0, 1, 2, 4, 6, 8] if k < 4 else [1, 4, 8]
        for n in lengths:
            for pattern in range(3 if k < 4 else 1):
                vector = []
                for i in range(n):
                    if pattern == 0:
                        z = Q3(1)
                    elif pattern == 1:
                        z = roots[(2 * i + 1) % 6] * F(1 + (i % 2), 2)
                    else:
                        z = Q3() if i % 3 == 0 else roots[(i * i + 3) % 6]
                    vector.append(z)
                    counts["zero_entries_retained"] += int(z == 0)
                actual = direct_distinct(vector, k)
                via_partition = partition_distinct(vector, k, parts)
                require(actual == via_partition, "partition identity")
                counts["partition_identity_vectors"] += 1
                require(actual.b == 0, "Hermitian reality")
                counts["real_distinct_polynomials"] += 1
                if actual.a < 0:
                    negative["distinct_polynomial_need_not_be_positive"] = True
                B = sum(vector, Q3())
                V = sum((z.norm() for z in vector), F(0))
                for delta in [F(1, 2), F(1, 3), F(1, 10)]:
                    C = F(A ** k) * delta ** (1 - k)
                    rhs = delta * B.norm() ** k + C * (1 + V) ** k
                    require(abs(actual.a - B.norm() ** k) <= rhs,
                            "explicit collision bound")
                    counts["explicit_collision_inequalities"] += 1
                if k >= 2 and n == 1:
                    wrong = partition_distinct(vector, k, parts, True)
                    if wrong != actual:
                        negative["omitted_partition_factorial_detected"] = True

    # Actual finite-field character identity at split rational primes. Euler's
    # sextic symbol is x^((p-1)/6) for nonzero x; zero is retained literally.
    for p in [7, 13, 19, 31, 37, 43]:
        for a in range(p):
            sixth_power_row = pow(a, 6, p)
            symbol = (pow(sixth_power_row, (p - 1) // 6, p)
                      if sixth_power_row else 0)
            require(symbol == int(a != 0), "literal sixth-power character mask")
            counts["sixth_power_finite_field_masks"] += 1
            if a == 0:
                require(symbol != 1, "zero witness")
                negative["nonunit_zero_replaced_by_one_detected"] = True

    # Formal prime-rooting: arbitrary positive additive prime weights prove
    # the coefficient identity; the analytic application uses log Np.
    weights = [F(2), F(3), F(5), F(7), F(11)]
    for mask in range(1, 1 << len(weights)):
        primes = [i for i in range(len(weights)) if mask & (1 << i)]
        degree = len(primes)
        mu = (-1) ** degree
        total_weight = sum(weights[i] for i in primes)
        rooted = sum((-(-1) ** (degree - 1)) * weights[i] / total_weight
                     for i in primes)
        require(rooted == mu, "native prime-rooting coefficient")
        counts["prime_rooting_coefficient_cases"] += 1
        wrong = -rooted
        if wrong != mu:
            negative["prime_rooting_missing_minus_detected"] = True

    for k in range(1, 13):
        for den in range(1, 13):
            for num in range(1, 73):
                h = F(num, den)
                gap = 2 * k + h / 6 - (k + h)
                require((gap > 0) == (h < F(6 * k, 5)), "threshold algebra")
                counts["moment_threshold_rational_cases"] += 1

    require(all(negative.values()), "one or more negative controls were not triggered")
    result = {
        "status": "PASS",
        "proof_sha256": hashlib.sha256(proof_bytes).hexdigest(),
        "proof_bytes": len(proof_bytes),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "arithmetic": "exact Fraction arithmetic in Q(sqrt(-3)); exact finite-field powers",
        "counts": counts,
        "negative_controls": negative,
        "scope": "finite partition identities, explicit constants, literal zero masks, rooting signs, exponent algebra",
        "not_certified": ["prime ideal theorem", "infinite asymptotic lower bounds",
                          "Dedekind zeta continuation", "native composite singleton bound", "RH"]
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()

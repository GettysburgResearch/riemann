#!/usr/bin/env python3
"""Exact finite replay for the all-order collision-removal packet.

Standard library only. These checks test algebra, not infinite arithmetic moments.
No acceptance condition uses Python's removable `assert` statement.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from typing import Iterator

BASE = "670a76c1a3a8f325c43c1755b1cfc24d313a3e3c"
COUNTS: dict[str, int] = defaultdict(int)


class CheckFailure(RuntimeError):
    pass


def require(condition: bool, group: str, message: str) -> None:
    COUNTS[group] += 1
    if not condition:
        raise CheckFailure(f"{group}: {message}")


def compositions(total: int, slots: int) -> Iterator[tuple[int, ...]]:
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def multinomial(a: tuple[int, ...]) -> int:
    return math.factorial(sum(a)) // math.prod(math.factorial(x) for x in a)


@lru_cache(None)
def positive_coefficient(a: tuple[int, ...]) -> int:
    if not any(a):
        return 1
    value = 0
    for i, x in enumerate(a):
        if x:
            child = list(a)
            child[i] -= 1
            value += positive_coefficient(tuple(child))
    if all(x <= 1 for x in a):
        value += (-1) ** sum(a)
    return value


def expansion_coefficient(a: tuple[int, ...]) -> int:
    """Independent expansion of numerator times a geometric series."""
    support = [i for i, x in enumerate(a) if x]
    value = 0
    for mask in range(1 << len(support)):
        remainder = list(a)
        bits = 0
        for j, index in enumerate(support):
            if mask >> j & 1:
                remainder[index] -= 1
                bits += 1
        value += (-1) ** bits * multinomial(tuple(remainder))
    return value


def inverse_coefficient(a: tuple[int, ...]) -> int:
    return 1 if not any(a) else 1 - sum(x > 0 for x in a)


def local_replay() -> dict[str, int]:
    tuples = 0
    inverse_tests = 0
    for k in range(1, 9):
        collapsed_plus = []
        collapsed_minus = []
        for degree in range(9):
            plus_sum = minus_sum = 0
            for a in compositions(degree, k):
                c = positive_coefficient(a)
                require(c == expansion_coefficient(a), "local_expansion", str(a))
                require(c >= 0, "positivity", str(a))
                if sum(x > 0 for x in a) == 1:
                    require(c == 0, "one_slot_vanishing", str(a))
                plus_sum += c
                minus_sum += abs(inverse_coefficient(a))
                tuples += 1
                # A separate formal convolution, not just the recurrence.
                if k <= 5 and degree <= 6:
                    conv = 0
                    for b in itertools.product(*(range(x + 1) for x in a)):
                        rem = tuple(x - y for x, y in zip(a, b))
                        conv += positive_coefficient(b) * inverse_coefficient(rem)
                    require(conv == int(degree == 0), "inverse_convolution", str(a))
                    inverse_tests += 1
            direct_plus = sum((-1) ** j * math.comb(k, j) * k ** (degree - j)
                              for j in range(min(k, degree) + 1))
            direct_minus = (1 if degree == 0 else
                            k * math.comb(k + degree - 2, degree - 1)
                            - math.comb(k + degree - 1, degree))
            require(plus_sum == direct_plus, "scalar_collapse", f"plus {k} {degree}")
            require(minus_sum == direct_minus, "scalar_collapse", f"minus {k} {degree}")
            collapsed_plus.append(plus_sum)
            collapsed_minus.append(minus_sum)
        r = math.comb(k, 2)
        for seq in (collapsed_plus, collapsed_minus):
            e = [sum((-1) ** j * math.comb(r, j) * seq[m - 2 * j]
                     for j in range(min(r, m // 2) + 1)) for m in range(9)]
            require(e[:3] == [1, 0, 0], "pair_pole_removal", f"k={k}")
        t = F(1, 4 * k)
        rp = (1 - t) ** k / (1 - k * t)
        rm = 2 - (1 - k * t) / (1 - t) ** k
        require(sum(v * t ** i for i, v in enumerate(collapsed_plus)) <= rp,
                "positive_series_prefix", f"plus {k}")
        require(sum(v * t ** i for i, v in enumerate(collapsed_minus)) <= rm,
                "positive_series_prefix", f"minus {k}")
    derangement = 1
    for k in range(1, 17):
        derangement = k * derangement + (-1) ** k
        require(positive_coefficient((1,) * k) == derangement,
                "derangement_boundary", str(k))
    for a in range(1, 13):
        for b in range(1, 13):
            require(positive_coefficient((a, b)) == math.comb(a + b - 2, a - 1),
                    "binary_closed_form", f"{a} {b}")
    return {"multiindices": tuples, "inverse_convolutions": inverse_tests,
            "maximum_full_local_order": 8, "maximum_derangement_order": 16}


# Q(zeta_6), represented as a+b*zeta_6 with zeta_6^2=zeta_6-1.
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    a, b = z
    c, d = w
    return a * c - b * d, a * d + b * c + b * d


def scale(z, t):
    return z[0] * t, z[1] * t


def power(z, n: int):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, z)
        z = mul(z, z)
        n >>= 1
    return out


def product_complex(values):
    out = ONE
    for value in values:
        out = mul(out, value)
    return out


def norm_ideal(exponents: tuple[int, int]) -> int:
    # Two distinct split-prime ideal norms. Only the free ideal monoid is used.
    return 7 ** exponents[0] * 13 ** exponents[1]


def phase(exponents: tuple[int, int], phases):
    return mul(power(phases[0], exponents[0]), power(phases[1], exponents[1]))


def profile(t: F) -> F:
    # A rational finite fixture, not a C-infinity analytic test.
    lo, hi = F(1, 10), F(2)
    return (t - lo) * (hi - t) if lo < t < hi else F(0)


def squarefree_sum(x: F, phases):
    out = ZERO
    for exponents in itertools.product(range(2), repeat=2):
        w = profile(F(norm_ideal(exponents), 1) / x)
        out = add(out, scale(phase(exponents, phases), (-1) ** sum(exponents) * w))
    return out


def disjoint_sum(xs: tuple[F, ...], phases, exclude_first: bool = False):
    k = len(xs)
    out = ZERO
    # Each prime is unused, or belongs to exactly one factor.
    for places in itertools.product(range(k + 1), repeat=2):
        if exclude_first and places[0]:
            continue
        exponents = [[0, 0] for _ in xs]
        for p, place in enumerate(places):
            if place:
                exponents[place - 1][p] = 1
        weights = [profile(F(norm_ideal(tuple(e)), 1) / x)
                   for e, x in zip(exponents, xs)]
        sign = (-1) ** sum(bool(p) for p in places)
        total_exp = tuple(int(p != 0) for p in places)
        out = add(out, scale(phase(total_exp, phases), sign * math.prod(weights)))
    return out


def ideals_below(limit: F, first_only: bool = False):
    out = []
    a = 0
    while 7 ** a <= limit:
        b = 0
        while 7 ** a * 13 ** b <= limit:
            out.append((a, b))
            if first_only:
                break
            b += 1
        a += 1
    return out


def finite_row_replay() -> dict[str, int]:
    cases = 0
    masked_cases = 0
    scale_vectors = [(F(12), F(12)), (F(12), F(60)), (F(60), F(12)),
                     (F(90), F(90)), (F(12), F(12), F(12)),
                     (F(12), F(60), F(90)), (F(60), F(60), F(60))]
    phase_vectors = [(ROOTS[0], ROOTS[0]), (ROOTS[1], ROOTS[2]),
                     (ROOTS[3], ROOTS[3]), (ZERO, ROOTS[1]),
                     (ROOTS[4], ZERO), (ZERO, ZERO)]
    for xs in scale_vectors:
        k = len(xs)
        for phases in phase_vectors:
            lhs = product_complex(squarefree_sum(x, phases) for x in xs)
            original_disjoint = disjoint_sum(xs, phases)
            forward = inverse = ZERO
            for ds in itertools.product(*(ideals_below(2 * x) for x in xs)):
                e7 = tuple(d[0] for d in ds)
                e13 = tuple(d[1] for d in ds)
                ck = positive_coefficient(e7) * positive_coefficient(e13)
                dk = inverse_coefficient(e7) * inverse_coefficient(e13)
                if not ck and not dk:
                    continue
                ys = tuple(x / norm_ideal(d) for x, d in zip(xs, ds))
                ph = phase((sum(e7), sum(e13)), phases)
                if ck:
                    forward = add(forward, scale(mul(ph, disjoint_sum(ys, phases)), ck))
                if dk:
                    prod = product_complex(squarefree_sum(y, phases) for y in ys)
                    inverse = add(inverse, scale(mul(ph, prod), dk))
            require(forward == lhs, "finite_forward", f"{xs} {phases}")
            require(inverse == original_disjoint, "finite_inverse", f"{xs} {phases}")
            cases += 1
            if ZERO in phases:
                masked_cases += 1
            restored = ZERO
            for ds in itertools.product(*(ideals_below(2 * x, True) for x in xs)):
                powers = tuple(d[0] for d in ds)
                ck = multinomial(powers)
                ys = tuple(x / norm_ideal(d) for x, d in zip(xs, ds))
                ph = power(phases[0], sum(powers))
                restored = add(restored, scale(mul(ph, disjoint_sum(ys, phases)), ck))
            require(restored == disjoint_sum(xs, phases, True),
                    "moving_exclusion", f"{xs} {phases}")
    for root in ROOTS:
        require(power(root, 6) == ONE, "sixth_power_masks", str(root))
    require(power(ZERO, 6) == ZERO, "sixth_power_masks", "zero must remain zero")
    return {"forward_and_inverse_cases": cases, "cases_with_zero_phases": masked_cases,
            "moving_exclusion_cases": cases, "fixture_prime_ideal_norms": [7, 13],
            "warning": "Finite free-ideal-monoid and rational-weight identities, not an arithmetic moment experiment."}


def exponent_replay() -> dict[str, str]:
    def alpha(k: int, h: F, defect: F) -> F:
        return F(1, 2) + (defect + F(5, 6) * h) / (2 * k)
    expected = {(2, F(0)): F(17, 24), (2, F(1, 2)): F(5, 6),
                (2, F(2, 3)): F(7, 8), (3, F(0)): F(23, 36),
                (3, F(1)): F(29, 36)}
    for (k, defect), wanted in expected.items():
        require(alpha(k, F(1), defect) == wanted, "extraction_fractions", str((k, defect)))
    for k in range(2, 33):
        r = math.comb(k, 2)
        require(2 * r == k * (k - 1), "energy_log_exponent", str(k))
        for h in (F(1, 2), F(1), F(11, 10), F(6), F(10)):
            # Direct reading of the prime-row moment exponent.
            direct = (F(k) + F(1, 3) + h - h / 6) / (2 * k)
            require(direct == alpha(k, h, F(1, 3)), "defect_extraction", f"{k} {h}")
    return {f"k={k},lambda={defect}": str(value) for (k, defect), value in expected.items()}


def rejection_replay() -> int:
    # Each mutant is an actual incorrect predicate which must raise our guard.
    tests = [lambda: require(0 == positive_coefficient((1, 1)), "mutant_guard", "dropped pair"),
             lambda: require(1 - 3 == inverse_coefficient((2, 1)), "mutant_guard", "total degree"),
             lambda: require(power(ZERO, 6) == ONE, "mutant_guard", "lost zero mask"),
             lambda: require(F(17, 24) + F(1, 2) / 2 == F(5, 6),
                             "mutant_guard", "wrong moment root")]
    rejected = 0
    for test in tests:
        try:
            test()
        except CheckFailure:
            rejected += 1
        else:
            raise CheckFailure("A deliberate mutation was accepted")
    return rejected


def reconstruct() -> dict:
    local = local_replay()
    finite = finite_row_replay()
    fractions = exponent_replay()
    mutations = rejection_replay()
    return {"schema": "all-order-collision-replay-v1", "base_commit": BASE,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "local": local, "finite_rows": finite, "conditional_fractions": fractions,
            "rejected_deliberate_mutations": mutations,
            "predicate_counts": dict(sorted(COUNTS.items())),
            "successful_predicates": sum(COUNTS.values()) - mutations,
            "not_proved_by_computation": ["infinite kernel asymptotic", "arithmetic higher moments",
                                           "zero-free improvement", "RH", "independent proof review"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    try:
        result = reconstruct()
        payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
        if args.check is not None:
            retained = json.loads(args.check.read_text(encoding="utf-8"))
            if retained != result:
                raise CheckFailure("Retained JSON differs from full reconstruction")
        if args.output is not None:
            args.output.write_text(payload, encoding="utf-8")
        print(payload, end="")
        return 0
    except (CheckFailure, OSError, ValueError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

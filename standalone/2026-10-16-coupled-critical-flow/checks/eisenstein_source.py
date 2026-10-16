#!/usr/bin/env python3
"""Exact finite diagnostics; not an asymptotic moment certificate.

Arithmetic is in Z[zeta_6] and in actual Eisenstein residue fields.
Run from any directory; stdout is deterministic JSON. No third-party packages.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction

Pair = tuple[int, int]
ZERO: Pair = (0, 0)
ONE: Pair = (1, 0)
ROOTS: tuple[Pair, ...] = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
counts: dict[str, int] = defaultdict(int)


def check(value: bool, category: str) -> None:
    counts[category] += 1
    if not value:
        raise RuntimeError(f"failed predicate: {category}, case {counts[category]}")


def add(x: Pair, y: Pair) -> Pair:
    return x[0] + y[0], x[1] + y[1]


def mul(x: Pair, y: Pair) -> Pair:
    # zeta_6^2 = zeta_6 - 1.
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c + b * d


def conj(x: Pair) -> Pair:
    return x[0] + x[1], -x[1]


def norm(x: Pair) -> int:
    a, b = x
    return a * a + a * b + b * b


def scale(x: Pair, n: int) -> Pair:
    return n * x[0], n * x[1]


def power(x: Pair, n: int) -> Pair:
    out = ONE
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out


def emul(x: Pair, y: Pair) -> Pair:
    # omega^2 = -omega - 1, NOT the zeta_6 relation.
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def en(x: Pair) -> int:
    a, b = x
    return a * a - a * b + b * b


UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))


def canonical(x: Pair) -> Pair:
    return min(emul(x, unit) for unit in UNITS)


def elements(cap: int) -> list[Pair]:
    # N(a+b omega) >= (a^2+b^2)/2 gives a rigorous bounding box.
    bound = math.isqrt(2 * cap) + 1
    return [(a, b) for a in range(-bound, bound + 1)
            for b in range(-bound, bound + 1) if 0 < en((a, b)) <= cap]


def prime(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def divides(generator: Pair, x: Pair) -> bool:
    a, b = generator
    numerator = emul(x, (a - b, -b))
    q = en(generator)
    return numerator[0] % q == 0 and numerator[1] % q == 0


def residue_power(x: Pair, exponent: int, p: int) -> Pair:
    out = ONE
    while exponent:
        if exponent & 1:
            z = emul(out, x)
            out = z[0] % p, z[1] % p
        z = emul(x, x)
        x = z[0] % p, z[1] % p
        exponent >>= 1
    return out


def prime_character(generator: Pair, u: Pair) -> int | None:
    """Exponent of the literal sextic symbol (u / generator)_6, or None."""
    q = en(generator)
    if prime(q):  # split prime, norm p
        p = q
        a, b = generator
        omega = (-a * pow(b % p, -1, p)) % p
        x = (u[0] + u[1] * omega) % p
        if x == 0:
            return None
        target = pow(x, (p - 1) // 6, p)
        zeta = (1 + omega) % p
        return next(j for j in range(6) if pow(zeta, j, p) == target)
    p = math.isqrt(q)  # inert prime, norm p^2
    if p * p != q or not prime(p) or p % 3 != 2:
        raise ValueError("not an allowed Eisenstein prime ideal")
    x = u[0] % p, u[1] % p
    if x == ZERO:
        return None
    target = residue_power(x, (q - 1) // 6, p)
    return next(j for j in range(6) if residue_power((1, 1), j, p) == target)


def poly_product(left: dict[tuple[int, ...], Pair],
                 right: dict[tuple[int, ...], Pair]) -> dict[tuple[int, ...], Pair]:
    out: dict[tuple[int, ...], Pair] = {}
    for a, c in left.items():
        for b, d in right.items():
            key = tuple((x + y) % 6 for x, y in zip(a, b))
            out[key] = add(out.get(key, ZERO), mul(c, d))
    return {key: value for key, value in out.items() if value != ZERO}


def group_power(columns: list[tuple[tuple[int, ...], Pair]], k: int,
                rough: tuple[int, ...]) -> dict[tuple[int, ...], Pair]:
    base: dict[tuple[int, ...], Pair] = {}
    for factors, coefficient in columns:
        key = tuple(int(p in factors) for p in rough)
        base[key] = add(base.get(key, ZERO), coefficient)
    out = {(0,) * len(rough): ONE}
    for _ in range(k):
        out = poly_product(out, base)
    return out


def projected_moment(columns: list[tuple[tuple[int, ...], Pair]], k: int,
                     rough: tuple[int, ...]) -> int:
    return sum(norm(c) for c in group_power(columns, k, rough).values())


def direct_random_average(columns: list[tuple[tuple[int, ...], Pair]], k: int,
                          rough: tuple[int, ...]) -> Fraction:
    total = 0
    for phases in itertools.product(range(6), repeat=len(rough)):
        value = ZERO
        for factors, coefficient in columns:
            e = sum(j for p, j in zip(rough, phases) if p in factors) % 6
            value = add(value, mul(coefficient, ROOTS[e]))
        total += norm(value) ** k
    return Fraction(total, 6 ** len(rough))


def tuple_selector(columns: list[tuple[tuple[int, ...], Pair]], k: int,
                   rough: tuple[int, ...]) -> Pair:
    """A separate literal 2k-tuple expansion, only used for small fixtures."""
    left_terms = []
    for indices in itertools.product(range(len(columns)), repeat=k):
        coeff = ONE
        exponents = [0] * len(rough)
        for index in indices:
            factors, c = columns[index]
            coeff = mul(coeff, c)
            for j, p in enumerate(rough):
                exponents[j] += int(p in factors)
        left_terms.append((tuple(exponents), coeff))
    out = ZERO
    for a, c in left_terms:
        for b, d in left_terms:
            if all((x - y) % 6 == 0 for x, y in zip(a, b)):
                out = add(out, mul(c, conj(d)))
    return out


def finite_checks() -> dict[str, object]:
    for a, b in itertools.product(range(6), repeat=2):
        check(mul(ROOTS[a], ROOTS[b]) == ROOTS[(a + b) % 6], "root_products")
        check(norm(ROOTS[a]) == 1, "root_norms")
    # Genuine split, conjugate split, and inert ideal characters.
    generators = ((-3, -2), (-3, -1), (-4, -3), (-5, 0))
    check([en(p) for p in generators] == [7, 7, 13, 25], "prime_ideal_norms")
    for generator in generators:
        q = en(generator)
        p = q if prime(q) else math.isqrt(q)
        reps = [(a, 0) for a in range(p)] if prime(q) else list(itertools.product(range(p), repeat=2))
        chars = [prime_character(generator, u) for u in reps]
        check(chars.count(None) == 1, "literal_zero_fibers")
        for j in range(6):
            check(chars.count(j) == (q - 1) // 6, "uniform_unit_fibers")
        for x, y in itertools.product(reps, repeat=2):
            a = prime_character(generator, x)
            b = prime_character(generator, y)
            c = prime_character(generator, emul(x, y))
            expected = None if a is None or b is None else (a + b) % 6
            check(c == expected, "field_multiplicativity")
    # Rational local Rankin algebra for every fixed-order fixture.
    for m in (3, 4, 6, 8):
        for k in range(1, 13):
            coefficients = [0] * (2 * k + 1)
            for a, b in itertools.product(range(k + 1), repeat=2):
                if (a - b) % m == 0:
                    coefficients[a + b] += math.comb(k, a) * math.comb(k, b)
            check(coefficients[:3] == [1, 0, k * k], "local_leading_terms")
            for r in (Fraction(1, 7), Fraction(2, 5), Fraction(1, 2)):
                value = sum(c * r ** j for j, c in enumerate(coefficients))
                check(value <= 1 + k * k * r * r + 4 ** k * r ** 3,
                      "local_remainder_majorant")
    # Three independent exact computations of the same conditional moment.
    for zero_index in (None, 0, 1, 2):
        for low_phase in range(6):
            columns = []
            for factors in ((), (0,), (1,), (2,), (0, 1), (1, 2)):
                if zero_index in factors:
                    c = ZERO
                else:
                    c = ROOTS[(3 * len(factors) + low_phase * int(0 in factors)
                               + 2 * int(1 in factors) + 4 * int(2 in factors)) % 6]
                columns.append((factors, c))
            for k in (1, 2, 3):
                rough = (1, 2)
                j = projected_moment(columns, k, rough)
                check(j == direct_random_average(columns, k, rough), "projection_vs_average")
                check(tuple_selector(columns, k, rough) == (j, 0), "projection_vs_tuples")
    # Negative controls: reject common false substitutions.
    alias_columns = [((), ONE), ((0,), (-1, 0))]
    check(projected_moment(alias_columns, 6, (0,)) == 926, "sixth_power_alias")
    check(926 != math.comb(12, 6), "negative_drop_sixth_alias")
    erased = [((), ONE), ((0,), ZERO)]
    check(projected_moment(erased, 2, (0,)) == 1, "zero_mask_retained")
    check(projected_moment(erased, 2, (0,)) != projected_moment(alias_columns, 2, (0,)),
          "negative_redraw_nonunits")
    check(norm(add(ONE, (-1, 0))) < projected_moment(alias_columns, 1, (0,)),
          "negative_native_dominates_projection")
    plus_columns = [((), ONE), ((0,), ONE)]
    check(norm(add(ONE, ONE)) > projected_moment(plus_columns, 1, (0,)),
          "negative_projection_dominates_native")
    return {"sixth_order_alias_value": 926,
            "without_aliases_incorrect_value": math.comb(12, 6),
            "negative_controls": 4}


def arithmetic_table() -> list[dict[str, object]]:
    cap = 128
    ideals = sorted(set(canonical(u) for u in elements(cap)), key=lambda u: (en(u), u))
    good = [u for u in ideals if math.gcd(en(u), 6) == 1]
    primes = [u for u in good if prime(en(u)) or
              (math.isqrt(en(u)) ** 2 == en(u)
               and prime(math.isqrt(en(u))) and math.isqrt(en(u)) % 3 == 2)]
    # The norm-p^2 test above can include split-prime squares only if p%3=2,
    # where the inert ideal is unique. Ramified primes were removed.
    factored = []
    for u in good:
        factors = tuple(j for j, p in enumerate(primes) if divides(p, u))
        if math.prod(en(primes[j]) for j in factors) == en(u):
            factored.append((u, factors))
    rows = elements(64)
    cache = {u: [prime_character(p, u) for p in primes] for u in rows}
    output = []
    for d in (8, 16, 32, 64):
        selected = [(u, f) for u, f in factored if d <= en(u) <= 2 * d]
        physical_rows = [u for u in rows if en(u) <= d]
        for y in (3, 7, 13, 25):
            used = {p for _, f in selected for p in f}
            rough = tuple(sorted(p for p in used if en(primes[p]) > y))
            total_native = total_projected = negative_rows = positive_rows = 0
            abs_accounting = 0
            for u in physical_rows:
                columns = []
                chars = cache[u]
                for _, factors in selected:
                    phase = None if any(chars[j] is None for j in factors) else (
                        3 * len(factors) + sum(chars[j] for j in factors)) % 6
                    columns.append((factors, ZERO if phase is None else ROOTS[phase]))
                summed = ZERO
                for _, c in columns:
                    summed = add(summed, c)
                native = norm(summed) ** 2
                projected = projected_moment(columns, 2, rough)
                abs_columns = [(f, ONE if c != ZERO else ZERO) for f, c in columns]
                absolute = projected_moment(abs_columns, 2, rough)
                check(0 <= projected <= absolute, "native_projection_absolute_majorant")
                check(native - projected >= -absolute, "one_sided_remainder_floor")
                total_native += native
                total_projected += projected
                abs_accounting += absolute
                negative_rows += native < projected
                positive_rows += native > projected
            output.append({"D": d, "H": d, "small_prime_norm_cutoff": y,
                           "columns": len(selected), "rows": len(physical_rows),
                           "native_fourth_moment": total_native,
                           "projected_fourth_moment": total_projected,
                           "absolute_sector_count": abs_accounting,
                           "signed_rough_remainder": total_native - total_projected,
                           "negative_remainder_rows": negative_rows,
                           "positive_remainder_rows": positive_rows})
    check(any(r["negative_remainder_rows"] for r in output), "native_negative_remainder_exists")
    check(any(r["positive_remainder_rows"] for r in output), "native_positive_remainder_exists")
    return output


def main() -> None:
    controls = finite_checks()
    table = arithmetic_table()
    report = {"status": "PASS", "arithmetic": "exact integers and fractions; no floating point",
              "scope": "finite algebra and bounded native Eisenstein fixtures, not an asymptotic proof",
              "diagnostics": controls, "predicate_counts": dict(sorted(counts.items())),
              "total_predicates": sum(counts.values()), "native_table": table}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

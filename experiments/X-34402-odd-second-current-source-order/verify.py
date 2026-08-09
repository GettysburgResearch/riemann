#!/usr/bin/env python3
"""Exact formal-log replay for R-34402 and L-34408.

Every log(p) log(q) is treated as an independent formal monomial.  No
floating-point logarithm or numerical sign test is used.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

ROW_LIMIT = 40
ARITH_LIMIT = 4 * ROW_LIMIT

Monomial = tuple[int, int]
Poly = Counter[Monomial]


def divisors(n: int) -> list[int]:
    out: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n: int) -> int:
    fac = factor(n)
    if any(a >= 2 for a in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def odd_lambda(n: int) -> Counter[int]:
    fac = factor(n)
    if len(fac) != 1:
        return Counter()
    p, _a = next(iter(fac.items()))
    if p == 2:
        return Counter()
    return Counter({p: 1})


def log_of_integer(n: int) -> Counter[int]:
    return Counter(factor(n))


def multiply_linear(a: Counter[int], b: Counter[int]) -> Poly:
    out: Poly = Counter()
    for p, cp in a.items():
        for q, cq in b.items():
            out[tuple(sorted((p, q)))] += cp * cq
    return +out


def add_poly(target: Poly, source: Poly, scale: int = 1) -> None:
    for monomial, coeff in source.items():
        target[monomial] += scale * coeff
        if target[monomial] == 0:
            del target[monomial]


def odd_selberg_coefficient(n: int) -> Poly:
    # Lambda_odd(n) log n.
    out = multiply_linear(odd_lambda(n), log_of_integer(n))

    # (Lambda_odd * Lambda_odd)(n).
    for d in divisors(n):
        add_poly(out, multiply_linear(odd_lambda(d), odd_lambda(n // d)))
    return +out


def odd_source(n: int) -> int:
    return mobius(n) if n % 2 else 0


def convolve_source_with_c(n: int, c: list[Poly]) -> Poly:
    out: Poly = Counter()
    for d in divisors(n):
        coefficient = odd_source(d)
        if coefficient:
            add_poly(out, c[n // d], coefficient)
    return +out


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def carry_poly(sequence: list[Poly], n: int, j: int) -> Poly:
    out: Poly = Counter()
    for q in range(1, n + 1):
        coefficient = carry(n, j, q)
        if coefficient:
            add_poly(out, sequence[q], coefficient)
    return +out


def prefix(sequence: list[Poly]) -> list[Poly]:
    out: list[Poly] = [Counter() for _ in sequence]
    running: Poly = Counter()
    for n in range(1, len(sequence)):
        add_poly(running, sequence[n])
        out[n] = running.copy()
    return out


def prefix_defect(pref: list[Poly], n: int, j: int) -> Poly:
    out = pref[n].copy()
    add_poly(out, pref[j], -1)
    add_poly(out, pref[n - j], -1)
    return +out


def serialize(poly: Poly) -> dict[str, int]:
    return {
        f"log({p})*log({q})": coeff
        for (p, q), coeff in sorted(poly.items())
    }


def main() -> None:
    c: list[Poly] = [Counter() for _ in range(ARITH_LIMIT + 1)]
    t: list[Poly] = [Counter() for _ in range(ARITH_LIMIT + 1)]
    for n in range(1, ARITH_LIMIT + 1):
        c[n] = odd_selberg_coefficient(n)
    for n in range(1, ARITH_LIMIT + 1):
        t[n] = convolve_source_with_c(n, c)

    c_prefix = prefix(c)

    checked_rows = 0
    for n in range(2, ROW_LIMIT + 1):
        for j in range(1, n):
            t_relative = carry_poly(t, 4 * n, 4 * j)
            add_poly(t_relative, carry_poly(t, n, j), -1)

            correct = prefix_defect(c_prefix, 4 * n, 4 * j)
            add_poly(correct, prefix_defect(c_prefix, 2 * n, 2 * j))
            assert t_relative == correct, (n, j, t_relative, correct)
            checked_rows += 1

    # Exact smallest source-order mutation e=(2,1).
    e_n, e_j = 2, 1
    t_relative = carry_poly(t, 8, 4)
    add_poly(t_relative, carry_poly(t, 2, 1), -1)

    wrong = carry_poly(c, 8, 4)
    add_poly(wrong, carry_poly(c, 4, 2))

    expected_correct: Poly = Counter({(5, 5): 1, (7, 7): 1})
    expected_wrong: Poly = Counter({(3, 3): 1, (5, 5): 1, (7, 7): 1})
    discrepancy = wrong.copy()
    add_poly(discrepancy, t_relative, -1)

    assert t_relative == expected_correct
    assert wrong == expected_wrong
    assert discrepancy == Counter({(3, 3): 1})

    data = {
        "schema": "X-34402-odd-second-current-source-order-v1",
        "classification": "EXACT_FORMAL_LOG_SOURCE_ORDER_CORRECTION_VERIFIED",
        "row_limit": ROW_LIMIT,
        "relative_rows_checked": checked_rows,
        "correct_identity": (
            "T_odd(4e)-T_odd(e)=D_C(4e)+D_C(2e)"
        ),
        "rejected_identity": (
            "T_odd(4e)-T_odd(e)=S_odd(4e)+S_odd(2e)"
        ),
        "counterexample_row": {"n": e_n, "j": e_j},
        "true_relative_second_current": serialize(t_relative),
        "claimed_selberg_sum": serialize(wrong),
        "exact_discrepancy": serialize(discrepancy),
        "arithmetic": "formal independent log(p)*log(q) monomials",
        "does_not_prove": [
            "all-row positivity of D_C",
            "reflected dissipative recurrence",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    data["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"

    result_path = Path(__file__).with_name("results") / "verification.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

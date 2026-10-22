#!/usr/bin/env python3
"""Verify and explore the multiplicity-profile charge identities.

The script checks the exact integer identities behind the refined c=2 and c=3
frontiers and emits charge tables for arbitrary c. It uses exact Fractions.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def positive_part(x: Fraction) -> Fraction:
    return max(x, Fraction(0))


def k(c: Fraction, m: int) -> Fraction:
    if c <= 0 or m < 1:
        raise ValueError("c must be positive and m a positive integer")
    return c * c - positive_part(c - m) ** 2


def p2_on(m: int) -> int:
    return 2 * max(m - 2, 0)


def p2_pair(m: int) -> int:
    return 4 * max(m - 1, 0)


def p3_on(m: int) -> int:
    return max(3 * m - 7, 0) if m >= 3 else 0


def p3_pair(m: int) -> int:
    return 6 * m - 5


def verify(max_m: int) -> None:
    c2 = Fraction(2)
    c3 = Fraction(3)
    for m in range(1, max_m + 1):
        # 2N+S1 charge identity, per on-line point.
        lhs2_on = 2 * m + (1 if m == 1 else 0)
        rhs2_on = k(c2, m) + p2_on(m)
        assert Fraction(lhs2_on) == rhs2_on, (m, lhs2_on, rhs2_on)

        # Per reflected pair: N contributes 2m, hence 2N contributes 4m.
        lhs2_pair = 4 * m
        rhs2_pair = c2 * c2 + p2_pair(m)
        assert Fraction(lhs2_pair) == rhs2_pair, (m, lhs2_pair, rhs2_pair)

        # 3N+2D charge identity, per on-line point.
        lhs3_on = 3 * m + 2
        rhs3_on = k(c3, m) + p3_on(m)
        assert Fraction(lhs3_on) == rhs3_on, (m, lhs3_on, rhs3_on)

        # Per reflected pair: 3N gives 6m and 2D gives 4.
        lhs3_pair = 6 * m + 4
        rhs3_pair = c3 * c3 + p3_pair(m)
        assert Fraction(lhs3_pair) == rhs3_pair, (m, lhs3_pair, rhs3_pair)


def parse_fraction(text: str) -> Fraction:
    try:
        return Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(str(exc)) from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-multiplicity", type=int, default=12)
    parser.add_argument("--c", type=parse_fraction, default=Fraction(2))
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    if args.max_multiplicity < 3:
        raise SystemExit("max multiplicity must be at least 3")
    verify(args.max_multiplicity)

    table = []
    for m in range(1, args.max_multiplicity + 1):
        charge = k(args.c, m)
        table.append(
            {
                "m": m,
                "k_c": f"{charge.numerator}/{charge.denominator}",
                "p2_on": p2_on(m),
                "p2_pair": p2_pair(m),
                "p3_on": p3_on(m),
                "p3_pair": p3_pair(m),
            }
        )

    payload = {
        "status": "PASS_ZETA23_MULTIPLICITY_FRONTIER",
        "c": f"{args.c.numerator}/{args.c.denominator}",
        "max_multiplicity": args.max_multiplicity,
        "table": table,
        "identities": {
            "simple": "2N+S1 = charge_c2 + P2",
            "distinct": "3N+2D = charge_c3 + P3",
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Reproduce the scalar constants in the Zeta23 paper and this import packet.

This is a symbolic/numerical consistency checker, not a proof of the analytic
asymptotics. It uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Row:
    lam: float
    H: float
    Hd: float
    F: float
    c_opt_support_le_one: float | None
    H_opt_support_le_one: float | None


def h(lam: float) -> float:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    return 2.0 - 1.0 / lam - lam / 3.0


def hd(lam: float) -> float:
    return 0.5 * (1.0 + h(lam))


def f(lam: float) -> float:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    return lam / (1.0 + lam * lam / 3.0)


def c_opt(lam: float, arithmetic_variance: float = 1.0) -> float:
    """Optimal unsaturated scalar-window efficiency.

    For the generalized functional

        lam (int v)^2 / [int v^2 + m lam^2 int int |s-t|v(s)v(t)],

    the optimizer is cos(sqrt(2m)*lam*s) and the efficiency is the formula
    below, while the optimizer remains positive on the interval.
    """

    if lam <= 0 or arithmetic_variance <= 0:
        raise ValueError("lambda and arithmetic_variance must be positive")
    theta = lam * math.sqrt(arithmetic_variance / 2.0)
    return (
        math.sqrt(2.0 / arithmetic_variance)
        * math.tan(theta)
        / (1.0 + theta * math.tan(theta))
    )


def rows(lambdas: Iterable[float]) -> list[Row]:
    result: list[Row] = []
    for lam in lambdas:
        c = c_opt(lam) if lam <= 1.0 else None
        result.append(
            Row(
                lam=lam,
                H=h(lam),
                Hd=hd(lam),
                F=f(lam),
                c_opt_support_le_one=c,
                H_opt_support_le_one=(2.0 - 1.0 / c) if c is not None else None,
            )
        )
    return result


def run_self_checks() -> None:
    tol = 5e-13
    assert abs(h(1.0) - 2.0 / 3.0) < tol
    assert abs(hd(1.0) - 5.0 / 6.0) < tol
    assert abs(f(1.0) - 3.0 / 4.0) < tol

    c_mt = c_opt(1.0)
    expected = (
        math.sqrt(2.0)
        * math.tan(1.0 / math.sqrt(2.0))
        / (1.0 + (1.0 / math.sqrt(2.0)) * math.tan(1.0 / math.sqrt(2.0)))
    )
    assert abs(c_mt - expected) < tol
    assert 0.67249 < 2.0 - 1.0 / c_mt < 0.67251

    # Raw Fejer main term divided by lambda^2 gives kappa.
    for lam in (0.2, 0.5, 0.9, 1.0):
        raw = lam + lam**3 / 3.0
        kappa = raw / lam**2
        assert abs(kappa - (1.0 / lam + lam / 3.0)) < tol
        assert abs((2.0 - kappa) - h(lam)) < tol


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lambdas",
        nargs="*",
        type=float,
        default=[0.6, 0.75, 0.9, 1.0],
        help="positive support parameters",
    )
    parser.add_argument("--json", type=Path, help="optional JSON output path")
    args = parser.parse_args()

    run_self_checks()
    data = rows(args.lambdas)
    payload = {
        "status": "PASS_ZETA23_CONSTANTS",
        "rows": [asdict(row) for row in data],
        "montgomery_taylor": {
            "c": c_opt(1.0),
            "simple_on_line": 2.0 - 1.0 / c_opt(1.0),
            "distinct": 0.5 * (3.0 - 1.0 / c_opt(1.0)),
        },
    }

    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

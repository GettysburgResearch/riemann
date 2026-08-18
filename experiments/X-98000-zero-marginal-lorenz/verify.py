#!/usr/bin/env python3
"""Exact/high-precision replay for T-98000.

The analytic squarefree-shell asymptotic uses the classical PNT and squarefree
density theorem. This replay certifies the finite cell constants, exact Lorenz
algebra, and Mellin numerator bookkeeping; it does not prove either zero-hinge
arithmetic sign or RH.
"""
from __future__ import annotations

import hashlib
import json
from decimal import Context, Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from pathlib import Path

PREC = 110
CTX = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
HERE = Path(__file__).resolve().parent
VERDICT = "PASS_T98000_ZERO_MARGINAL_LORENZ_COLLAPSE"


def qstar(m: int) -> Decimal:
    if m == 1:
        return Decimal(0)
    if m == 2:
        return Decimal(15)
    if m == 3:
        return Decimal(6)
    if m == 4:
        return Decimal(3)
    return Decimal(6)


def sqrt_d(x: int | Decimal) -> Decimal:
    with localcontext(CTX):
        return Decimal(x).sqrt()


def log_d(x: int | Decimal) -> Decimal:
    with localcontext(CTX):
        return Decimal(x).ln()


def prefix_a(n: int) -> Decimal:
    with localcontext(CTX):
        return sum((qstar(m) / sqrt_d(m) for m in range(1, n + 1)), Decimal(0))


def prefix_b(n: int) -> Decimal:
    with localcontext(CTX):
        return sum(
            (
                qstar(m) * log_d(m) / sqrt_d(m)
                for m in range(2, n + 1)
                if qstar(m) != 0
            ),
            Decimal(0),
        )


def derivative_numerator_right(n: int) -> Decimal:
    """G_n(n+1) on the cell n<Y<n+1."""
    with localcontext(CTX):
        y = Decimal(n + 1)
        s = sqrt_d(y)
        a = prefix_a(n)
        q = a * log_d(y) - prefix_b(n)
        return a * (Decimal(4) * s - Decimal(3)) - Decimal(2) * s * q


def pos(x: Fraction) -> Fraction:
    return max(x, Fraction(0))


def lorenz_dual(even, odd, lam: Fraction) -> Fraction:
    t_odd = sum((t for t, r in odd), Fraction(0))
    r_odd = sum((r for t, r in odd), Fraction(0))
    return (
        lam * t_odd
        + sum((pos(r - lam * t) for t, r in even), Fraction(0))
        - r_odd
    )


def one_switch_envelope(even, target: Fraction) -> Fraction:
    """`even` is already sorted by decreasing r/t."""
    used = Fraction(0)
    value = Fraction(0)
    for t, r in even:
        if used + t <= target:
            used += t
            value += r
        else:
            if target > used:
                value += (target - used) * r / t
                used = target
            break
    if used != target:
        raise AssertionError("target outside capacity")
    return value


def run():
    finite = [derivative_numerator_right(n) for n in range(2, 8)]
    assert all(v > 0 for v in finite)

    sqrt2 = sqrt_d(2)
    sqrt3 = sqrt_d(3)
    c = Decimal(27) / 2 - Decimal(9) / sqrt2
    d = Decimal(39) / 2 - Decimal(9) / sqrt2
    q4 = (
        Decimal(15) * log_d(2) / sqrt2
        + Decimal(6) * log_d(Decimal(4) / 3) / sqrt3
    )
    constant = q4 - Decimal(48) + c * log_d(4)
    kappa = Decimal(36) + Decimal(4) * d + Decimal(2) * constant
    tail_margin = Decimal(2) * c * log_d(8) - kappa
    assert tail_margin > Decimal("0.65")

    shell_constant = Decimal(4) * log_d(2) + Decimal(3) * sqrt2 - Decimal(6)
    assert shell_constant > Decimal(1)

    # Exact one-switch Lorenz fixture: ratios 5, 3, 0 in source-index order.
    even = [
        (Fraction(2), Fraction(10)),
        (Fraction(3), Fraction(9)),
        (Fraction(5), Fraction(0)),
    ]
    odd = [(Fraction(4), Fraction(7)), (Fraction(2), Fraction(1))]
    target = sum((t for t, r in odd), Fraction(0))
    envelope = one_switch_envelope(even, target)
    assert envelope == Fraction(19)
    values = {
        lam: lorenz_dual(even, odd, lam)
        for lam in [Fraction(0), Fraction(3), Fraction(5), Fraction(6)]
    }
    assert values[Fraction(0)] == envelope - sum(r for t, r in odd)
    assert values[Fraction(0)] == Fraction(11)
    assert min(values.values()) == values[Fraction(0)]

    # Target Mellin kernel identity.
    s = Fraction(7, 3)
    lhs = Fraction(4, 1) / (s - Fraction(1, 2)) - Fraction(3, 1) / s
    rhs = (s + Fraction(3, 2)) / (s * (s - Fraction(1, 2)))
    assert lhs == rhs

    core = {
        "schema": "riemann.t98000.zero-marginal-lorenz.v1",
        "ratio_monotonicity": {
            "finite_right_endpoint_margins": [str(v) for v in finite],
            "analytic_tail_start": 8,
            "tail_margin_at_8": str(tail_margin),
            "range": "[0,6)",
            "strict_after": 2,
        },
        "one_switch_order": True,
        "zero_marginal_shell": {
            "constant": str(shell_constant),
            "coefficient": "(3/pi^2)*(4log2+3sqrt2-6)",
            "eventually_positive": True,
        },
        "lorenz_fixture": {
            "envelope": str(envelope),
            "dual_at_zero": str(values[Fraction(0)]),
            "marginal_lambda": "0",
        },
        "target_mellin_identity": True,
        "cpsl67_proved": False,
        "gpc67_proved": False,
        "gtc67_proved": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return core


def main():
    result = run()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()

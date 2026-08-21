#!/usr/bin/env python3
"""Exact formal regression for the bottom-two carry-charge criterion.

Standard-library only. This verifies finite rational/carry algebra with formal
target coordinates w_2,...,w_N. It does not prove the bottom-charge sign,
Landau's analytic hypotheses, or RH.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

MAX_N = 80
FORMAL_N = 40


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    parity = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def beta(n: int, q: int) -> Fraction:
    if q < 2 or q > n:
        return Fraction(0)
    return Fraction((n // q) * (q - 1 - (n % q)), n + 1)


def b2(n: int) -> Fraction:
    return Fraction(mobius(n)) - (
        Fraction(mobius(n // 2)) if n % 2 == 0 else Fraction(0)
    )


def omega2(n: int) -> Fraction:
    return (
        Fraction(mobius(n))
        - (Fraction(3, 2) * mobius(n // 2) if n % 2 == 0 else 0)
        + (Fraction(1, 2) * mobius(n // 4) if n % 4 == 0 else 0)
    )


Formal = dict[int, Fraction]


def add(a: Formal, b: Formal, scale: Fraction = Fraction(1)) -> Formal:
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, Fraction(0)) + scale * value
        if out[key] == 0:
            del out[key]
    return out


def scale(a: Formal, scalar: Fraction) -> Formal:
    return {key: scalar * value for key, value in a.items() if scalar * value}


def inverse_forms(nmax: int) -> dict[int, Formal]:
    """Solve B^T c=w over the formal basis {w_q}."""
    c: dict[int, Formal] = {}
    for n in range(nmax, 1, -1):
        residual: Formal = {n: Fraction(1)}
        for m in range(n + 1, nmax + 1):
            residual = add(residual, c[m], -beta(m, n))
        diagonal = beta(n, n)
        assert diagonal > 0
        c[n] = scale(residual, 1 / diagonal)
    return c


def frac_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    # 1. Exact filter identity omega_2=(I-1/2 delta_2*)b_2.
    filter_rows = 0
    for n in range(1, MAX_N + 1):
        rhs = b2(n) - (Fraction(1, 2) * b2(n // 2) if n % 2 == 0 else 0)
        assert omega2(n) == rhs
        filter_rows += 1

    # 2. Exact compact carry image: only rows n=2,3 survive.
    carry_rows = 0
    image: dict[int, Fraction] = {}
    for n in range(2, MAX_N + 1):
        value = sum((omega2(q) * beta(n, q) for q in range(2, n + 1)), Fraction(0))
        expected = Fraction(-5, 6) if n == 2 else Fraction(-1, 2) if n == 3 else Fraction(0)
        assert value == expected
        image[n] = value
        carry_rows += 1

    # 3. Formal triangular inversion and bottom-charge identity.
    forms = inverse_forms(FORMAL_N)
    bottom = add(scale(forms[2], Fraction(5)), scale(forms[3], Fraction(3)))
    riesz = {q: omega2(q) for q in range(2, FORMAL_N + 1) if omega2(q)}
    assert add(bottom, riesz, Fraction(6)) == {}

    # 4. Direct matrix pairing is identical to the formal result.
    for n in range(2, FORMAL_N + 1):
        coefficient = Fraction(5) * forms[2].get(n, 0) + Fraction(3) * forms[3].get(n, 0)
        assert coefficient == -6 * omega2(n)

    # 5. Mutations must fail the compact image.
    def mutated(n: int, middle: Fraction, outer: Fraction) -> Fraction:
        return (
            Fraction(mobius(n))
            + (middle * mobius(n // 2) if n % 2 == 0 else 0)
            + (outer * mobius(n // 4) if n % 4 == 0 else 0)
        )

    mutations = [
        (Fraction(-1), Fraction(1, 2)),
        (Fraction(-3, 2), Fraction(0)),
        (Fraction(-3, 2), Fraction(1)),
    ]
    rejected = 0
    for middle, outer in mutations:
        vals = []
        for n in range(2, 20):
            vals.append(
                sum(
                    (mutated(q, middle, outer) * beta(n, q) for q in range(2, n + 1)),
                    Fraction(0),
                )
            )
        if any(
            vals[n - 2]
            != (Fraction(-5, 6) if n == 2 else Fraction(-1, 2) if n == 3 else 0)
            for n in range(2, 20)
        ):
            rejected += 1
    assert rejected == len(mutations)

    result = {
        "schema": "X-26202-bottom-charge-v1",
        "classification": "EXACT_BOTTOM_TWO_CARRY_CHARGE_ALGEBRA_VERIFIED",
        "max_carry_row": MAX_N,
        "formal_inverse_endpoint": FORMAL_N,
        "checks": {
            "filter_rows": filter_rows,
            "compact_carry_rows": carry_rows,
            "formal_target_coordinates": FORMAL_N - 1,
            "mutations_rejected": rejected,
        },
        "compact_image": {
            "row_2": frac_text(image[2]),
            "row_3": frac_text(image[3]),
            "rows_4_through_max": "0",
        },
        "formal_identity": "5*c_X(2)+3*c_X(3)=-6*sum_{q=2}^X omega_2(q)w_X(q)",
        "proof_boundary": (
            "finite rational and formal algebra only; eventual bottom-charge "
            "nonnegativity, the Landau transfer, and RH are not certified"
        ),
    }

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["result_sha256_without_digest"] = hashlib.sha256(canonical).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(json.dumps(result["checks"], sort_keys=True))
    print(result["result_sha256_without_digest"])


if __name__ == "__main__":
    main()

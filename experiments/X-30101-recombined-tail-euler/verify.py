#!/usr/bin/env python3
"""Exact regression for R-30101 and L-30102.

Uses only integers, fractions.Fraction, hashlib, and json.
It verifies the source-changing distinction between the ordinary recombined tail
and the artificially alternating D_k tail, plus the exact interlacing telescope.
It proves no asymptotic theorem and no RH conclusion.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def A(q: int, s: int, k: int) -> Fraction:
    return Fraction(1, (2 * k * q - 1) ** s)


def B(q: int, s: int, k: int) -> Fraction:
    return Fraction(1, ((2 * k + 1) * q) ** s)


def D(q: int, s: int, k: int) -> Fraction:
    return A(q, s, k) - B(q, s, k)


def G(q: int, s: int, k: int) -> Fraction:
    return Fraction(1, ((2 * k - 1) * q) ** s) - A(q, s, k)


def main() -> None:
    d1 = D(1, 1, 1)
    d2 = D(1, 1, 2)
    assert d1 == Fraction(2, 3)
    assert d2 == Fraction(2, 15)

    ordinary_two = d1 + d2
    artificial_alternating_two = d1 - d2
    assert ordinary_two == Fraction(4, 5)
    assert artificial_alternating_two == Fraction(8, 15)
    assert ordinary_two != artificial_alternating_two

    # The Hausdorff geometric kernels differ after recombination.
    y = Fraction(1, 2)
    K = 2
    ordinary_kernel = y**K / (1 - y)
    alternating_kernel = y**K / (1 + y)
    assert ordinary_kernel == Fraction(1, 2)
    assert alternating_kernel == Fraction(1, 6)

    interlacing_rows = 0
    for q in range(1, 17):
        for s in range(1, 5):
            for K in range(1, 9):
                common_partial = Fraction(0)
                gap_partial = Fraction(0)
                boundary = Fraction(1, ((2 * K - 1) * q) ** s)
                for L in range(K, 25):
                    d = D(q, s, L)
                    g = G(q, s, L)
                    assert d > 0
                    assert g >= 0
                    common_partial += d
                    gap_partial += g
                    rhs = boundary - B(q, s, L) - gap_partial
                    assert common_partial == rhs
                    assert common_partial <= boundary
                    interlacing_rows += 1

    direct_pairing_rows = 0
    for q in range(1, 12):
        for s in range(1, 4):
            for K in range(1, 7):
                for L in range(K, 15):
                    direct = sum(
                        (A(q, s, k) - B(q, s, k) for k in range(K, L + 1)),
                        Fraction(0),
                    )
                    recombined = sum(
                        (D(q, s, k) for k in range(K, L + 1)),
                        Fraction(0),
                    )
                    assert direct == recombined
                    direct_pairing_rows += 1

    result = {
        "classification": "EXACT_RECOMBINED_COMMON_TAIL_EULER_MISMATCH_VERIFIED",
        "q1_s1_D1": str(d1),
        "q1_s1_D2": str(d2),
        "two_term_ordinary_common_tail": str(ordinary_two),
        "two_term_artificial_alternating_tail": str(artificial_alternating_two),
        "hausdorff_ordinary_kernel_y_half_K2": str(ordinary_kernel),
        "hausdorff_alternating_kernel_y_half_K2": str(alternating_kernel),
        "interlacing_identity_rows": interlacing_rows,
        "direct_pairing_rows": direct_pairing_rows,
        "proof_boundary": (
            "Exact distinction between ordinary recombined tail and artificial "
            "alternating tail; exact interlacing telescope. No RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    assert result["proof_object_sha256"] == (
        "6d0b3839f4c1062229a226535abd6fc6e1289b47ac57b13a7a8fd1972fe99338"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

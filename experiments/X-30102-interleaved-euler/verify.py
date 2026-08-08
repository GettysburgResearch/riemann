#!/usr/bin/env python3
"""Exact finite regression for L-30103.

The proof in L-30103 is analytic. This checker independently verifies the
finite rational consequences for integer exponents and exact zero-extended
Euler transforms. It proves no all-real-s theorem and no RH conclusion.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def c_value(q: int, s: int, K: int, n: int) -> Fraction:
    if n % 2 == 0:
        j = n // 2
        x = 2 * (K + j) * q - 1
    else:
        j = (n - 1) // 2
        x = (2 * (K + j) + 1) * q
    return Fraction(1, x**s)


def difference(values: list[Fraction]) -> list[Fraction]:
    return [values[i] - values[i + 1] for i in range(len(values) - 1)]


def zero_extended_difference(values: list[Fraction]) -> list[Fraction]:
    return [
        values[i] - (values[i + 1] if i + 1 < len(values) else Fraction(0))
        for i in range(len(values))
    ]


def main() -> None:
    even_difference_rows = 0
    for q in range(1, 25):
        for s in range(1, 5):
            for K in range(1, 11):
                values = [c_value(q, s, K, n) for n in range(80)]
                current = values
                for _m in range(13):
                    for n in range(0, len(current), 2):
                        assert current[n] >= 0
                        even_difference_rows += 1
                    current = difference(current)
                    if not current:
                        break

    euler_rows = 0
    positive_remainders = 0
    for q in range(1, 13):
        for s in range(1, 4):
            for K in range(1, 8):
                for pairs in range(2, 11):
                    values = [c_value(q, s, K, n) for n in range(2 * pairs)]
                    alternating = sum(
                        ((Fraction(1) if n % 2 == 0 else Fraction(-1)) * v
                         for n, v in enumerate(values)),
                        Fraction(0),
                    )
                    for M in range(1, 7):
                        jets = Fraction(0)
                        current = values
                        for m in range(M):
                            jets += Fraction(1, 2 ** (m + 1)) * current[0]
                            current = zero_extended_difference(current)

                        remainder = sum(
                            ((Fraction(1) if n % 2 == 0 else Fraction(-1)) * v
                             for n, v in enumerate(current)),
                            Fraction(0),
                        )
                        rhs = jets + Fraction(1, 2**M) * remainder
                        assert rhs == alternating

                        # Pairing the exact Mth-difference remainder gives
                        # the sum of (M+1)st differences at even starts.
                        paired = Fraction(0)
                        for n in range(0, len(current), 2):
                            even = current[n]
                            odd = current[n + 1] if n + 1 < len(current) else Fraction(0)
                            paired += even - odd
                        assert paired == remainder
                        assert remainder >= 0
                        euler_rows += 1
                        positive_remainders += 1

    result = {
        "classification": "EXACT_INTERLEAVED_EULER_POSITIVITY_REPLAYED",
        "even_start_difference_rows": even_difference_rows,
        "exact_euler_rows": euler_rows,
        "positive_exact_remainders": positive_remainders,
        "proof_boundary": (
            "Finite rational replay for integer exponents and zero-extended "
            "tails only; analytic all-s proof is L-30103; no source-module or RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact finite regression for L-30103.

The proof in L-30103 concerns the infinite/Abel common tail before terminal
zero extension. This checker verifies its finite interior consequences and also
records that zero extension can create a signed terminal collar. It uses only
standard-library exact arithmetic and proves no source-module or RH conclusion.
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
    paired_difference_rows = 0
    positive_partial_remainder_rows = 0

    for q in range(1, 25):
        for s in range(1, 5):
            for K in range(1, 11):
                levels = [[c_value(q, s, K, n) for n in range(100)]]
                for _m in range(1, 14):
                    levels.append(difference(levels[-1]))

                for m, current in enumerate(levels[:-1]):
                    next_values = levels[m + 1]
                    for n in range(0, len(next_values), 2):
                        assert current[n] >= 0
                        assert current[n] - current[n + 1] == next_values[n]
                        assert next_values[n] >= 0
                        even_difference_rows += 1
                        paired_difference_rows += 1

                    # Finite partial sums of the positive paired remainder.
                    max_pairs = min(12, (len(next_values) + 1) // 2)
                    for J in range(1, max_pairs + 1):
                        partial = sum(
                            (next_values[2 * j] for j in range(J)),
                            Fraction(0),
                        )
                        assert partial >= 0
                        positive_partial_remainder_rows += 1

    # Exact Euler algebra for genuinely finite zero-extended sequences. The
    # identity remains true, but the terminal collar need not be positive.
    zero_extended_euler_rows = 0
    negative_terminal_collar_cases = 0
    first_witness = None

    for q in range(1, 10):
        for s in range(1, 4):
            for K in range(1, 6):
                for pairs in range(2, 9):
                    values = [c_value(q, s, K, n) for n in range(2 * pairs)]
                    alternating = sum(
                        ((Fraction(1) if n % 2 == 0 else Fraction(-1)) * value
                         for n, value in enumerate(values)),
                        Fraction(0),
                    )
                    for M in range(1, 7):
                        jets = Fraction(0)
                        current = values
                        for m in range(M):
                            jets += Fraction(1, 2 ** (m + 1)) * current[0]
                            current = zero_extended_difference(current)

                        remainder = sum(
                            ((Fraction(1) if n % 2 == 0 else Fraction(-1)) * value
                             for n, value in enumerate(current)),
                            Fraction(0),
                        )
                        assert jets + Fraction(1, 2**M) * remainder == alternating

                        if remainder < 0:
                            negative_terminal_collar_cases += 1
                            if first_witness is None:
                                first_witness = (q, s, K, pairs, M, remainder)
                        zero_extended_euler_rows += 1

    assert first_witness == (1, 1, 1, 2, 5, Fraction(-13, 15))

    result = {
        "classification": (
            "EXACT_INTERLEAVED_EULER_INTERIOR_POSITIVITY_AND_COLLAR_SCOPE_VERIFIED"
        ),
        "even_start_difference_rows": even_difference_rows,
        "paired_difference_identity_rows": paired_difference_rows,
        "positive_partial_remainder_rows": positive_partial_remainder_rows,
        "zero_extended_euler_identity_rows": zero_extended_euler_rows,
        "negative_terminal_collar_cases": negative_terminal_collar_cases,
        "first_terminal_collar_witness": str(first_witness),
        "proof_boundary": (
            "Exact finite rational replay of even-start interior positivity and "
            "Euler algebra; zero extension can create a signed terminal collar, "
            "which is not part of the infinite positive remainder. No source-module "
            "or RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    assert result["proof_object_sha256"] == (
        "b954f0f4d80c7cd6482c052979ec40dccbcd061525dc8217e737b6ec8f188b37"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

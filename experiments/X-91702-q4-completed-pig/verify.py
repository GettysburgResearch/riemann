#!/usr/bin/env python3
"""Exact finite replay for the algebraic part of T-93010.

The checker verifies:
- the cellwise complete carry field and mean-source identity;
- the exact variance/coercivity decomposition;
- the termwise Mellin kernel identity;
- the finite scale-four Dirichlet-series coefficient identity.

It does not authenticate von Koch's theorem, analytic continuation, a zeta-zero
statement, endpoint PIG, or RH.
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from pathlib import Path
from typing import List, Sequence, Tuple

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"
Formal = Tuple[Fraction, Fraction]  # a + b * L, with L a formal log(4)


def fadd(x: Formal, y: Formal) -> Formal:
    return x[0] + y[0], x[1] + y[1]


def fscale(q: Fraction, x: Formal) -> Formal:
    return q * x[0], q * x[1]


def prefix(coeff: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(0)]
    running = Fraction(0)
    for value in coeff[1:]:
        running += value
        out.append(running)
    return out


def rows(coeff: Sequence[Fraction]) -> List[Fraction]:
    n = len(coeff) - 1
    csum = prefix(coeff)
    return [csum[n] - csum[j] - csum[n - j - 1] for j in range(n)]


def mean_source(coeff: Sequence[Fraction]) -> Fraction:
    n = len(coeff) - 1
    return sum(
        (coeff[m] * (Fraction(2 * m, n) - 1) for m in range(1, n + 1)),
        Fraction(0),
    )


def pairwise_gap(values: Sequence[Fraction]) -> Fraction:
    return sum(
        ((values[a] - values[b]) ** 2 for a in range(len(values)) for b in range(a + 1, len(values))),
        Fraction(0),
    )


def run_random_field_cases(rng: random.Random) -> Tuple[int, int]:
    identities = 0
    mutations = 0
    for n in range(2, 49):
        for _ in range(17):
            coeff = [Fraction(0)] + [
                Fraction(rng.randint(-11, 13), rng.randint(1, 9)) for _ in range(n)
            ]
            value = rows(coeff)
            direct_mean = sum(value, Fraction(0)) / n
            source_mean = mean_source(coeff)
            assert direct_mean == source_mean
            identities += 1

            sumsq = sum((z * z for z in value), Fraction(0))
            total = sum(value, Fraction(0))
            assert n * sumsq - total * total == pairwise_gap(value)
            identities += 1

            pig = sumsq / (n * n)
            decomposition = source_mean * source_mean / n + pairwise_gap(value) / (n**3)
            assert pig == decomposition
            assert source_mean * source_mean <= n * pig
            identities += 2

            # Wrong endpoint reflection N-j instead of N-j-1 is detected.
            csum = prefix(coeff)
            wrong = [csum[n] - csum[j] - csum[n - j] for j in range(n)]
            if sum(wrong, Fraction(0)) / n != source_mean:
                mutations += 1
            else:
                raise AssertionError("reflection mutation escaped")

    return identities, mutations


def run_mellin_kernel_cases() -> int:
    identities = 0
    for m in range(1, 73):
        for z in range(2, 19):
            # Integral of (2m/X-1) X^{-z-1} from m to infinity,
            # evaluated by the two elementary antiderivatives.
            lhs = Fraction(2, z + 1) * Fraction(1, m**z) - Fraction(1, z) * Fraction(1, m**z)
            rhs = Fraction(z - 1, z * (z + 1)) * Fraction(1, m**z)
            assert lhs == rhs
            identities += 1
    return identities


def run_scale_four_dirichlet_cases(rng: random.Random) -> Tuple[int, int]:
    identities = 0
    mutations = 0
    for cutoff in range(8, 57):
        lambdas = [Fraction(0)] + [
            Fraction(rng.randint(-7, 11), rng.randint(1, 8)) for _ in range(cutoff)
        ]
        coeff: List[Formal] = [(Fraction(0), Fraction(0)) for _ in range(cutoff + 1)]
        for m in range(1, cutoff + 1):
            rational = lambdas[m]
            if m % 4 == 0:
                rational -= 4 * lambdas[m // 4]
            log_coeff = Fraction(3) if (m & (m - 1) == 0 and m >= 4 and (m.bit_length() - 1) % 2 == 0) else Fraction(0)
            # The bit test above selects m=4^r.
            coeff[m] = rational, log_coeff

        for z in range(2, 8):
            lhs: Formal = (Fraction(0), Fraction(0))
            for m in range(1, cutoff + 1):
                lhs = fadd(lhs, fscale(Fraction(1, m**z), coeff[m]))

            base = sum((lambdas[m] * Fraction(1, m**z) for m in range(1, cutoff + 1)), Fraction(0))
            shifted = sum(
                (lambdas[k] * Fraction(1, k**z) for k in range(1, cutoff // 4 + 1)),
                Fraction(0),
            )
            atom = sum(
                (Fraction(1, (4**r) ** z) for r in range(1, 20) if 4**r <= cutoff),
                Fraction(0),
            )
            rhs: Formal = (base - Fraction(4, 4**z) * shifted, 3 * atom)
            assert lhs == rhs
            identities += 1

            # Omitting the factor four in the shifted source must be detected
            # whenever the shifted finite sum is nonzero.
            wrong: Formal = (base - Fraction(1, 4**z) * shifted, 3 * atom)
            if shifted != 0:
                assert wrong != lhs
                mutations += 1

    return identities, mutations


def main() -> None:
    rng = random.Random(91702)
    field_identities, reflection_mutations = run_random_field_cases(rng)
    mellin_identities = run_mellin_kernel_cases()
    dirichlet_identities, shift_mutations = run_scale_four_dirichlet_cases(rng)

    payload = {
        "verdict": "PASS_X_91702_Q4_COMPLETED_ENDPOINT_PIG",
        "arithmetic": "EXACT_RATIONAL_WITH_FORMAL_LOG4",
        "field_and_variance_identities": field_identities,
        "reflection_mutations_detected": reflection_mutations,
        "mellin_kernel_identities": mellin_identities,
        "scale_four_dirichlet_identities": dirichlet_identities,
        "scale_four_mutations_detected": shift_mutations,
        "proves": [
            "finite mean-source identity",
            "finite variance/coercivity identity",
            "termwise Mellin kernel algebra",
            "finite scale-four source transform algebra",
        ],
        "does_not_prove": [
            "von Koch estimate",
            "analytic continuation or zero safety",
            "polylogarithmic endpoint PIG",
            "Riemann Hypothesis",
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["verdict"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

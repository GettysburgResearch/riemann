#!/usr/bin/env python3
"""Exact finite-algebra replay for L-91723.

The checker authenticates every new rational constant and integer-square
comparison. It does not replay the imported analytic mismatch/collar bounds.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json


def check_constants() -> dict[str, object]:
    adjacent = Fraction(19, 2)
    ordinary_tail = 3 * adjacent
    detail_tail = ordinary_tail + Fraction(1, 2) * ordinary_tail
    collar = Fraction(200)
    combined = collar + detail_tail
    relative_numerator = combined * Fraction(3, 4)

    assert ordinary_tail == Fraction(57, 2)
    assert detail_tail == Fraction(171, 4)
    assert combined == Fraction(971, 4)
    assert relative_numerator == Fraction(2913, 16)

    # 2913/(16 sqrt(2)) < 129.
    lhs_square = 2913**2
    rhs_square = 2 * (16 * 129) ** 2
    assert lhs_square < rhs_square

    return {
        "adjacent_mismatch_constant": str(adjacent),
        "all_q_ordinary_mismatch_constant": str(ordinary_tail),
        "all_q_detail_mismatch_constant": str(detail_tail),
        "collar_plus_mismatch_constant": str(combined),
        "relative_before_q_ge_2": str(relative_numerator),
        "integer_square_left": lhs_square,
        "integer_square_right": rhs_square,
        "uniform_relative_constant": 129,
    }


def check_thinning_algebra() -> dict[str, object]:
    # tau_K(1+129/sqrt(K)) = (sqrt(K)+129)/(sqrt(K)+130).
    # The strict leftover numerator is exactly one.
    assert 130 - 129 == 1

    # tau_K <= K/(K+178) for every K>=2:
    # after squaring positive sides it is enough that 178^2 <= 130^2 K.
    assert 178**2 <= 130**2 * 2

    # sqrt(67)<33/4 and the resulting score loss is below 4290.
    assert 16 * 67 < 33**2
    assert 520 * 33 == 4 * 4290

    return {
        "new_thinning": "sqrt(K)/(sqrt(K)+130)",
        "relative_error": "129/sqrt(K)",
        "strict_detail_slack": "Omega_X(q)/(sqrt(K)+130)",
        "terminal_comparison_from_K": 2,
        "terminal_square_left": 178**2,
        "terminal_square_right_at_K2": 130**2 * 2,
        "sqrt67_upper": "33/4",
        "score_loss_upper": 4290,
    }


def check_symbolic_samples() -> dict[str, object]:
    # Rational surrogate x=sqrt(K)>0. The identity is algebraic in x and
    # can be checked exactly on hostile rational values without deciding the
    # theorem by samples.
    xs = [
        Fraction(1, 1000),
        Fraction(1),
        Fraction(7, 3),
        Fraction(100),
        Fraction(10**6),
    ]
    records = []
    for x in xs:
        tau = x / (x + 130)
        used = tau * (1 + Fraction(129, 1) / x)
        slack = 1 - used
        assert used == (x + 129) / (x + 130)
        assert slack == 1 / (x + 130)
        assert slack > 0
        records.append(
            {
                "sqrtK_surrogate": str(x),
                "used_fraction": str(used),
                "slack_fraction": str(slack),
            }
        )
    return {"hostile_exact_surrogates": records}


def mutation_tests() -> dict[str, object]:
    detected = 0

    # A denominator equal to the error constant loses strict reserve.
    x = Fraction(13)
    bad = x / (x + 129) * (1 + Fraction(129, 1) / x)
    assert bad == 1
    detected += 1

    # 128 is too small for the certified 129/sqrt(K) error.
    bad2 = x / (x + 128) * (1 + Fraction(129, 1) / x)
    assert bad2 > 1
    detected += 1

    # The old K/(K+178) reserve is not comparable to 129/sqrt(K)
    # uniformly as K grows: at K=10^8 the latter is much larger.
    K = 10**8
    old_reserve = Fraction(178, K + 178)
    certified_error_lower_marker = Fraction(129, 10**4)
    assert old_reserve < certified_error_lower_marker
    detected += 1

    return {"mutations_detected": detected}


def main() -> None:
    payload: dict[str, object] = {
        "classification": "PASS_FACTOR67_ALL_COLUMN_SQRTK_RESERVE",
        "constant_reduction": check_constants(),
        "thinning_algebra": check_thinning_algebra(),
        "symbolic_samples": check_symbolic_samples(),
        "mutation_tests": mutation_tests(),
        "imported_not_replayed": [
            "factor-67 adjacent mismatch bound |epsilon_X(n)| < 19/2 n^(-3/2)",
            "all-column B-spline collar bound < 200/(q sqrt(K))",
            "terminal omission reserve 5033 X^(-3/2)",
            "root Hall, rough ownership, common port and endpoint consumer",
        ],
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path("results/verification.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact conductor-cost frontier for coherent FFPS local phase tensors.

For a squarefree product M of distinct marked odd primes, the source-locked
local theorem gives squared principal leverage L(M)=prod (p-1)/(p+1).
This producer proves the exact budget optimizer, records small rational
frontiers, and separates the classical primorial asymptotic from the still
open global FFPS moment and individualization problems.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "ffps_coherent_tensor_cost_frontier.json"
NOTE_PATH = HERE / "FFPS_COHERENT_TENSOR_COST_FRONTIER.md"
TEST_PATH = ROOT / "tests" / "test_ffps_coherent_tensor_cost_frontier.py"
DEPENDENCY_PATH = HERE / "ffps_principal_leverage.json"

DEPENDENCY_LF_SHA256 = (
    "cdf514d8f8b76b7d2569ea6852c8f4dcc8590c0ad72822d3bee711711cfd3ee3"
)
DEPENDENCY_SCHEMA = "riemann.function_field.ffps_principal_leverage.v2"
SOURCE_COMMIT_751 = "37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2"
MAX_PRIME_CONTROL = 127
MAX_EXHAUSTIVE_SUBSETS = 4_096
FRONTIER_PRIME_COUNT = 13
EXHAUSTIVE_PRIME_COUNT = 8


def _sha256_lf(path: Path) -> str:
    raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(raw).hexdigest()


def _fraction_pair(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_odd_primes(count: int) -> tuple[int, ...]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("prime count must be a nonnegative integer")
    result = []
    candidate = 3
    while len(result) < count:
        if candidate > MAX_PRIME_CONTROL:
            raise ValueError("requested prime prefix exceeds the control cap")
        if is_prime(candidate):
            result.append(candidate)
        candidate += 2
    return tuple(result)


def _validate_prime_set(primes: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    normalized = tuple(primes)
    if any(not is_prime(prime) or prime == 2 for prime in normalized):
        raise ValueError("tensor coordinates require odd primes")
    if len(set(normalized)) != len(normalized):
        raise ValueError("tensor coordinates require distinct primes")
    return tuple(sorted(normalized))


def squarefree_conductor(primes: tuple[int, ...] | list[int]) -> int:
    result = 1
    for prime in _validate_prime_set(primes):
        result *= prime
    return result


def squared_leverage(primes: tuple[int, ...] | list[int]) -> Fraction:
    result = Fraction(1)
    for prime in _validate_prime_set(primes):
        result *= Fraction(prime - 1, prime + 1)
    return result


def optimal_prefix_under_budget(budget: int) -> tuple[int, ...]:
    """Return the exact leverage-minimizing marked-prime set for M<=budget."""

    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 1:
        raise ValueError("conductor budget must be a positive integer")
    selected = []
    product = 1
    candidate = 3
    while True:
        while not is_prime(candidate):
            candidate += 2
        if candidate > MAX_PRIME_CONTROL:
            if product * candidate <= budget:
                raise ValueError("conductor budget exceeds the certified prime cap")
            break
        if product * candidate > budget:
            break
        selected.append(candidate)
        product *= candidate
        candidate += 2
    return tuple(selected)


def minimal_conductor_for_target(target: Fraction | int) -> dict[str, object]:
    target = Fraction(target)
    if not 0 < target < 1:
        raise ValueError("leverage target must lie strictly between zero and one")
    primes = []
    leverage = Fraction(1)
    candidate = 3
    while leverage > target:
        while not is_prime(candidate):
            candidate += 2
        if candidate > MAX_PRIME_CONTROL:
            raise ValueError("target lies beyond the certified prime cap")
        primes.append(candidate)
        leverage *= Fraction(candidate - 1, candidate + 1)
        candidate += 2
    return {
        "target_squared_leverage_at_most": _fraction_pair(target),
        "optimal_primes": primes,
        "minimal_squarefree_conductor": squarefree_conductor(primes),
        "attained_squared_leverage": _fraction_pair(leverage),
        "previous_prefix_squared_leverage": _fraction_pair(
            squared_leverage(primes[:-1])
        ),
    }


def exhaustive_budget_audit(primes: tuple[int, ...]) -> dict[str, int]:
    primes = _validate_prime_set(list(primes))
    subset_count = 2 ** len(primes)
    if subset_count > MAX_EXHAUSTIVE_SUBSETS:
        raise ValueError("exhaustive budget audit exceeds its subset cap")
    comparisons = 0
    for size in range(len(primes) + 1):
        for subset in combinations(primes, size):
            budget = squarefree_conductor(list(subset))
            optimum = optimal_prefix_under_budget(budget)
            if squared_leverage(list(subset)) < squared_leverage(list(optimum)):
                raise ArithmeticError(
                    "a non-prefix subset beat the exact budget optimizer"
                )
            comparisons += 1
    if comparisons != subset_count:
        raise ArithmeticError("exhaustive subset accounting drifted")
    return {"prime_count": len(primes), "subsets_checked": comparisons}


def build_fixture() -> dict[str, object]:
    if _sha256_lf(DEPENDENCY_PATH) != DEPENDENCY_LF_SHA256:
        raise ArithmeticError("source-locked FFPS leverage dependency changed")
    dependency = json.loads(DEPENDENCY_PATH.read_text(encoding="utf-8"))
    if dependency.get("schema") != DEPENDENCY_SCHEMA:
        raise ArithmeticError("FFPS leverage dependency schema drifted")
    theorem = dependency.get("principal_leverage_theorem")
    if not isinstance(theorem, dict):
        raise TypeError("FFPS leverage theorem is missing")
    if theorem.get("tensor_formula") != (
        "for distinct marked phases, squared leverage is product_i (p_i-1)/(p_i+1)"
    ):
        raise ArithmeticError("source tensor formula drifted")

    frontier_primes = first_odd_primes(FRONTIER_PRIME_COUNT)
    rows = []
    for count in range(1, len(frontier_primes) + 1):
        prefix = frontier_primes[:count]
        rows.append(
            {
                "marked_prime_count": count,
                "largest_marked_prime": prefix[-1],
                "optimal_primes": list(prefix),
                "minimal_squarefree_conductor": squarefree_conductor(list(prefix)),
                "optimal_squared_leverage": _fraction_pair(
                    squared_leverage(list(prefix))
                ),
            }
        )

    targets = [
        minimal_conductor_for_target(target)
        for target in (
            Fraction(1, 2),
            Fraction(1, 3),
            Fraction(1, 4),
            Fraction(1, 5),
            Fraction(1, 10),
        )
    ]
    exhaustive = exhaustive_budget_audit(first_odd_primes(EXHAUSTIVE_PRIME_COUNT))

    fixture: dict[str, object] = {
        "schema": "riemann.function_field.ffps_coherent_tensor_cost_frontier.v1",
        "status": "EXACT_FINITE_BUDGET_OPTIMUM_AND_CLASSICAL_PRIMORIAL_ASYMPTOTIC",
        "source_frontier": {
            "pr": 751,
            "commit": SOURCE_COMMIT_751,
            "live_target": "T-106121 / FFPS106121",
            "dependency": DEPENDENCY_PATH.name,
            "dependency_schema": DEPENDENCY_SCHEMA,
            "dependency_sha256_lf": DEPENDENCY_LF_SHA256,
        },
        "exact_budget_theorem": {
            "model": (
                "M is the squarefree product of distinct marked odd-prime phase coordinates; "
                "L(M)=product_(p|M)(p-1)/(p+1) is squared principal leverage"
            ),
            "fixed_cardinality": (
                "among all k-coordinate tensors, the first k odd primes uniquely minimize both "
                "the conductor product and the squared leverage"
            ),
            "fixed_budget": (
                "if P_k<=X<P_(k+1) for odd primorial prefixes P_k, the unique leverage "
                "minimum under M<=X is the first-k-prime tensor"
            ),
            "proof": (
                "(p-1)/(p+1) is strictly increasing in p; sorted distinct odd primes satisfy "
                "p_i>=the i-th odd prime; no k+1 prime product fits below P_(k+1), and every "
                "additional feasible factor is strictly below one"
            ),
            "finite_frontier": rows,
            "target_frontier": targets,
            "exhaustive_regression": exhaustive,
        },
        "conductor_asymptotic": {
            "odd_primorial": "M_x=product_(3<=p<=x) p",
            "source_leverage_asymptotic": (
                "L(M_x)~3*zeta(2)*exp(-2*EulerGamma)/(log x)^2"
            ),
            "prime_number_theorem_input": "log M_x=theta(x)-log(2)~x",
            "conductor_form": ("L(M_x)~3*zeta(2)*exp(-2*EulerGamma)/(log log M_x)^2"),
            "target_cost_form": (
                "to reach L approximately epsilon on the optimal primorial frontier requires "
                "log log M approximately sqrt(3*zeta(2)*exp(-2*EulerGamma)/epsilon)"
            ),
            "polynomial_saving_no_go": (
                "for every fixed delta>0, M_x^delta*L(M_x) tends to infinity; the local "
                "tensor factor alone is not an M^(-delta) individualization saving"
            ),
        },
        "interpretation": {
            "positive": (
                "coherent-before-square tensorization really contracts and the exact cheapest "
                "finite design always uses the smallest available marked primes"
            ),
            "negative": (
                "measured against squarefree conductor cost, even the optimal contraction is "
                "only inverse-square log-log; pure local tensor leverage cannot pay a polynomial "
                "family-size loss"
            ),
            "still_live": [
                "arithmetic cancellation beyond the local Gram factor",
                "cross-prime Fourier or incidence structure",
                "an amplifier that isolates the principal member before positive squaring",
                "rigidity converting one exceptional member into a family-wide anomaly",
            ],
        },
        "scope": {
            "exact_budget_theorem_all_distinct_odd_primes": True,
            "finite_frontier_prime_cap": MAX_PRIME_CONTROL,
            "global_ffps_moment_proved": False,
            "source_realization_of_every_formal_tensor_proved": False,
            "principal_member_individualized": False,
            "rh_or_grh_proved": False,
        },
        "provenance": {
            "producer_sha256_lf": _sha256_lf(Path(__file__)),
            "note_sha256_lf": _sha256_lf(NOTE_PATH),
            "test_sha256_lf": _sha256_lf(TEST_PATH),
            "resource_caps": {
                "maximum_prime_control": MAX_PRIME_CONTROL,
                "maximum_exhaustive_subsets": MAX_EXHAUSTIVE_SUBSETS,
                "exhaustive_subsets_used": exhaustive["subsets_checked"],
            },
        },
    }
    return fixture


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = _canonical(build_fixture())
    if args.check:
        if (
            not OUTPUT_PATH.is_file()
            or OUTPUT_PATH.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("FFPS coherent tensor cost fixture drifted")
        print("PASS_FFPS_COHERENT_TENSOR_COST_FRONTIER")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

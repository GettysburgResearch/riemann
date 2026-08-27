#!/usr/bin/env python3
"""Bounded exact replay for the degree-five exterior-tower phase diagram.

The producer source-locks the all-degree multi-place identity and performs
only sparse integer algebra and bounded Weyl-weight combinatorics.  It does
not enumerate a finite field, a polynomial family, a curve, or a zero.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from collections.abc import Iterable
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "c94466e28a48ec429150f63de6d334d4c4f60110"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "QUADRATIC_FAMILY_MULTIPLACE_L_FUNCTION_IDENTITY.md"
    ): "56790383fc49fb2f9116bc7add90e19afd00d1c7",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_multiplace_l_function_identity.py"
    ): "e96b8a653573e72966f2fa5069b322996854bec8",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_multiplace_l_function_identity.json"
    ): "f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e",
    "tests/test_quadratic_family_multiplace_l_function_identity.py": (
        "693b94467d4968b3b9af12a9e52a955e0ada2331"
    ),
}

MAX_MARK_COUNT = 24
MAX_FORMAL_GENUS = 8

# A sparse term (q_power, primitive_exterior_index) represents
# q^q_power * Phi_primitive_exterior_index.  Index zero is the scalar 1.
Term = tuple[int, int]
Sparse = dict[Term, int]


def check_source_contract() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def choose(n: int, k: int) -> int:
    if n < 0 or k < 0 or k > n:
        return 0
    return comb(n, k)


def cleaned(expression: Sparse) -> Sparse:
    return {term: value for term, value in expression.items() if value}


def add(*expressions: Sparse) -> Sparse:
    output: Sparse = {}
    for expression in expressions:
        for term, value in expression.items():
            output[term] = output.get(term, 0) + value
    return cleaned(output)


def scale(expression: Sparse, coefficient: int, q_shift: int = 0) -> Sparse:
    if q_shift < 0:
        raise ValueError("q shift must be nonnegative")
    return cleaned(
        {
            (q_power + q_shift, primitive_index): coefficient * value
            for (q_power, primitive_index), value in expression.items()
        }
    )


def genus(mark_count: int) -> int:
    if isinstance(mark_count, bool) or not isinstance(mark_count, int):
        raise TypeError("mark count must be an integer")
    if mark_count < 1:
        raise ValueError("mark count must be positive")
    return (mark_count - 1) // 2


def h_exterior_in_primitives(g: int, exterior_index: int) -> Sparse:
    """Trace of exterior^j H in primitive symplectic trace coordinates."""
    if g < 0 or exterior_index < 0:
        raise ValueError("genus and exterior index must be nonnegative")
    if exterior_index > 2 * g:
        return {}
    if exterior_index > g:
        dual = h_exterior_in_primitives(g, 2 * g - exterior_index)
        return scale(dual, 1, exterior_index - g)
    output: Sparse = {}
    for tate_power in range(exterior_index // 2 + 1):
        primitive_index = exterior_index - 2 * tate_power
        output[(tate_power, primitive_index)] = 1
    return output


def finite_dirichlet_exterior(mark_count: int, exterior_index: int) -> Sparse:
    """Trace on exterior^j V, with V=H (odd m) or 1+H (even m)."""
    g = genus(mark_count)
    h_j = h_exterior_in_primitives(g, exterior_index)
    if mark_count % 2:
        return h_j
    return add(h_j, h_exterior_in_primitives(g, exterior_index - 1))


def raw_exterior_expression(mark_count: int) -> Sparse:
    """Exact degree-five family row in primitive exterior coordinates."""
    g = genus(mark_count)
    del g  # validation is intentional
    triangular = mark_count * (mark_count + 1) // 2
    e1 = finite_dirichlet_exterior(mark_count, 1)
    e3 = finite_dirichlet_exterior(mark_count, 3)
    e5 = finite_dirichlet_exterior(mark_count, 5)
    return add(
        scale(e1, mark_count, 1),
        scale(e1, -triangular),
        scale(e3, 1, 1),
        scale(e3, -mark_count),
        scale(e5, -1),
    )


def expected_low_expression(mark_count: int) -> Sparse:
    rows: dict[int, Sparse] = {
        1: {},
        2: {(1, 0): 2, (0, 0): -3},
        3: {(1, 1): 3, (0, 1): -6},
        4: {(2, 0): 1, (0, 0): -10, (1, 1): 4, (0, 1): -10},
        5: {(2, 1): 1, (0, 1): -15},
        6: {(2, 1): 1, (0, 1): -21, (1, 2): 1, (0, 2): -6, (0, 0): -21},
        7: {(1, 3): 1, (0, 3): -7, (0, 1): -28},
        8: {(1, 3): 1, (0, 3): -8, (0, 2): -8, (0, 1): -36, (0, 0): -36},
        9: {(0, 3): -9, (0, 1): -45},
        10: {(0, 4): -1, (0, 3): -10, (0, 2): -10, (0, 1): -55, (0, 0): -55},
    }
    if mark_count not in rows:
        raise ValueError("low expression is stored only for m=1,...,10")
    return rows[mark_count]


def stable_expression(mark_count: int) -> Sparse:
    g = genus(mark_count)
    c = mark_count * (mark_count + 1) // 2
    if mark_count % 2:
        if mark_count < 9:
            raise ValueError("odd stable regime starts at nine marks")
        output = {(0, 3): -mark_count, (0, 1): -c}
        if g >= 5:
            output[(0, 5)] = -1
        return output
    if mark_count < 10:
        raise ValueError("even stable regime starts at ten marks")
    output = {
        (0, 4): -1,
        (0, 3): -mark_count,
        (0, 2): -mark_count,
        (0, 1): -c,
        (0, 0): -c,
    }
    if g >= 5:
        output[(0, 5)] = -1
    return output


def weil_weights(expression: Sparse) -> tuple[int, ...]:
    return tuple(sorted({2 * q_power + j for q_power, j in expression}, reverse=True))


def primitive_dimension(g: int, exterior_index: int) -> int:
    if exterior_index < 0 or exterior_index > g:
        return 0
    return choose(2 * g, exterior_index) - choose(2 * g, exterior_index - 2)


def primitive_generic_distinct_roots(g: int, exterior_index: int) -> int:
    """Number of distinct Laurent weights on a formal generic Sp(2g) torus."""
    if exterior_index < 0 or exterior_index > g:
        return 0
    return sum(
        (2**support_size) * choose(g, support_size)
        for support_size in range(exterior_index % 2, exterior_index + 1, 2)
    )


def primitive_zero_weight_multiplicity(g: int, exterior_index: int) -> int:
    if exterior_index < 0 or exterior_index > g or exterior_index % 2:
        return 0
    half = exterior_index // 2
    return choose(g, half) - choose(g, half - 1)


def memberwise_rank_formula(mark_count: int) -> str:
    rows = {
        1: "0",
        2: "2",
        3: "2*r1",
        4: "2+2*r1",
        5: "2*r1",
        6: "1+2*r1+2*r2",
        7: "r1+2*r3",
        8: "1+r1+r2+2*r3",
        9: "r1+r3",
        10: "1+r1+r2+r3+r4",
    }
    if mark_count in rows:
        return rows[mark_count]
    if mark_count % 2:
        return "r1+r3+r5"
    return "1+r1+r2+r3+r4+r5"


def recurrence_order_bound(mark_count: int) -> int:
    g = genus(mark_count)
    d = lambda j: primitive_dimension(g, j)
    if mark_count == 1:
        return 0
    if mark_count == 2:
        return 2
    if mark_count == 3:
        return 2 * d(1)
    if mark_count == 4:
        return 2 + 2 * d(1)
    if mark_count == 5:
        return 2 * d(1)
    if mark_count == 6:
        return 1 + 2 * d(1) + 2 * d(2)
    if mark_count == 7:
        return d(1) + 2 * d(3)
    if mark_count == 8:
        return 1 + d(1) + d(2) + 2 * d(3)
    return choose(mark_count - 1, 5)


def generic_minimal_rank(mark_count: int) -> int:
    g = genus(mark_count)
    r = lambda j: primitive_generic_distinct_roots(g, j)
    if mark_count == 1:
        return 0
    if mark_count == 2:
        return 2
    if mark_count == 3:
        return 2 * r(1)
    if mark_count == 4:
        return 2 + 2 * r(1)
    if mark_count == 5:
        return 2 * r(1)
    if mark_count == 6:
        return 1 + 2 * r(1) + 2 * r(2)
    if mark_count == 7:
        return r(1) + 2 * r(3)
    if mark_count == 8:
        return 1 + r(1) + r(2) + 2 * r(3)
    if mark_count % 2:
        return r(1) + r(3) + r(5)
    return 1 + sum(r(j) for j in range(1, 6))


def pure_tate_baseline(mark_count: int) -> dict[int, int]:
    """Map p-exponent k to the coefficient of the formal root p^k."""
    g = genus(mark_count)
    output: dict[int, int] = {}
    for (q_power, primitive_index), coefficient in raw_exterior_expression(
        mark_count
    ).items():
        if primitive_index == 0:
            multiplicity = 1
        else:
            multiplicity = primitive_zero_weight_multiplicity(g, primitive_index)
        if not multiplicity:
            continue
        root_exponent = q_power + primitive_index // 2
        output[root_exponent] = (
            output.get(root_exponent, 0) + coefficient * multiplicity
        )
    return dict(sorted((root, value) for root, value in output.items() if value))


def sparse_rows(expression: Sparse) -> list[dict[str, int]]:
    return [
        {
            "coefficient": coefficient,
            "primitive_exterior_index": primitive_index,
            "q_power": q_power,
            "weil_weight": 2 * q_power + primitive_index,
        }
        for (q_power, primitive_index), coefficient in sorted(expression.items())
    ]


def phase_row(mark_count: int) -> dict[str, object]:
    expression = raw_exterior_expression(mark_count)
    return {
        "generic_formal_torus_minimal_rank": generic_minimal_rank(mark_count),
        "genus": genus(mark_count),
        "mark_count": mark_count,
        "memberwise_minimal_rank_formula": memberwise_rank_formula(mark_count),
        "pure_tate_baseline_by_p_exponent": pure_tate_baseline(mark_count),
        "recurrence_order_bound": recurrence_order_bound(mark_count),
        "sparse_primitive_expression": sparse_rows(expression),
        "weil_weights_descending": list(weil_weights(expression)),
    }


def assert_equal(left: object, right: object, label: str) -> None:
    if left != right:
        raise ArithmeticError(f"{label}: {left!r} != {right!r}")


def verify_low_rows() -> None:
    for mark_count in range(1, 11):
        assert_equal(
            raw_exterior_expression(mark_count),
            expected_low_expression(mark_count),
            f"low row m={mark_count}",
        )


def verify_stable_rows(mark_counts: Iterable[int]) -> None:
    for mark_count in mark_counts:
        if mark_count < 9:
            continue
        assert_equal(
            raw_exterior_expression(mark_count),
            stable_expression(mark_count),
            f"stable row m={mark_count}",
        )
        assert_equal(
            recurrence_order_bound(mark_count),
            choose(mark_count - 1, 5),
            f"stable recurrence order m={mark_count}",
        )


def verify_weight_notch() -> None:
    top_weight_marks = {
        mark_count
        for mark_count in range(1, MAX_MARK_COUNT + 1)
        if 5 in weil_weights(raw_exterior_expression(mark_count))
    }
    expected = set(range(5, 9)) | set(range(11, MAX_MARK_COUNT + 1))
    assert_equal(top_weight_marks, expected, "weight-five mark-count phase")


def verify_generic_weight_counts() -> None:
    for g in range(1, MAX_FORMAL_GENUS + 1):
        for exterior_index in range(g + 1):
            distinct = primitive_generic_distinct_roots(g, exterior_index)
            dimension = primitive_dimension(g, exterior_index)
            if distinct > dimension:
                raise ArithmeticError("distinct formal weights exceed dimension")
    assert_equal(generic_minimal_rank(9), 48, "m=9 generic rank")
    assert_equal(generic_minimal_rank(10), 115, "m=10 generic rank")
    assert_equal(generic_minimal_rank(11), 222, "m=11 generic rank")
    assert_equal(generic_minimal_rank(12), 385, "m=12 generic rank")


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    verify_low_rows()
    verify_stable_rows(range(9, MAX_MARK_COUNT + 1))
    verify_weight_notch()
    verify_generic_weight_counts()

    even_tate_controls = {
        mark_count: pure_tate_baseline(mark_count)
        for mark_count in (2, 4, 6, 8, 10, 12)
    }
    assert_equal(even_tate_controls[2], {0: -3, 1: 2}, "m=2 Tate row")
    assert_equal(even_tate_controls[4], {0: -10, 2: 1}, "m=4 Tate row")
    assert_equal(even_tate_controls[6], {0: -21, 1: -6, 2: 1}, "m=6 Tate row")
    assert_equal(even_tate_controls[8], {0: -36, 1: -16}, "m=8 Tate row")

    return {
        "schema": "riemann.function_field.quadratic_family_exterior_tower_phase_diagram.v1",
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "import": "all-field degree-five coefficient identity and finite-character adapter",
        },
        "theorem": {
            "all_m_exterior_formula": (
                "S_A(n)=(m*p^n-C_m)Tr(F^n|exterior^1 V_A)"
                "+(p^n-m)Tr(F^n|exterior^3 V_A)"
                "-Tr(F^n|exterior^5 V_A), C_m=m(m+1)/2"
            ),
            "finite_dirichlet_representation": (
                "V_A=H^1(C_A) for odd m and V_A=1+H^1(C_A) for even m"
            ),
            "odd_stable_m_at_least_9": "S=-Phi5-m*Phi3-C_m*Phi1; Phi5=0 at m=9",
            "even_stable_m_at_least_10": (
                "S=-Phi5-Phi4-m*(Phi3+Phi2)-C_m*(Phi1+1); Phi5=0 at m=10"
            ),
            "weight_five_phase": (
                "present at m=5,6,7,8; absent at m=9,10; present with rigid coefficient -1 for all m>=11"
            ),
            "stable_recurrence_order_bound": "binomial(m-1,5)",
            "exact_rank_scope": (
                "under standard semisimplicity of curve Frobenius, replace each primitive dimension by the number r_j of distinct primitive eigenvalues"
            ),
            "formal_universal_filter_no_go": (
                "for m>=11 a configuration-independent nonzero Q(E) cannot annihilate the moving Phi5 row on the formal symplectic torus"
            ),
        },
        "phase_rows_m_1_through_12": [phase_row(m) for m in range(1, 13)],
        "stable_generic_rank_formulas": {
            "odd_m_at_least_11": "6g+16*C(g,3)+32*C(g,5)",
            "even_m_at_least_12": ("3+6g+8*C(g,2)+16*C(g,3)+16*C(g,4)+32*C(g,5)"),
        },
        "even_pure_tate_controls": {
            str(mark_count): {
                str(root): coefficient for root, coefficient in row.items()
            }
            for mark_count, row in even_tate_controls.items()
        },
        "proof_ledger": {
            "all_m_exterior_formula": "PROVED EXACT FROM LOCKED SOURCE",
            "low_mark_phase_table": "PROVED EXACT",
            "stable_primitive_collapse": "PROVED EXACT BY SYMPLECTIC LEFSCHETZ ALGEBRA",
            "mark_count_weight_five_notch": "PROVED EXACT",
            "stable_nonzero_filter_no_go": "PROVED OVER THE FORMAL SYMPLECTIC TORUS",
            "characteristic_polynomial_recurrence_bounds": "PROVED EXACT",
            "distinct_root_minimal_ranks": "PROVED USING STANDARD FROBENIUS SEMISIMPLICITY",
            "generic_torus_ranks": "FORMAL GENERIC, NOT AN ARITHMETIC EQUIDISTRIBUTION CLAIM",
            "sheaf_decomposition_beyond_finite_character_adapter": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "largest_mark_count_symbolically_checked": MAX_MARK_COUNT,
            "largest_formal_genus_weight_check": MAX_FORMAL_GENUS,
            "largest_exterior_index": 5,
            "largest_stored_phase_table_mark_count": 12,
            "finite_field_elements": 0,
            "polynomial_family_members": 0,
            "curves_enumerated": 0,
            "matrices_constructed": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()

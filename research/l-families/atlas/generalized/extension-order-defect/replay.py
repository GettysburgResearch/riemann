"""Primitive boundary modules, two scalar shadows and exact S3 Euler correction."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from functools import lru_cache
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
OLD = HERE.parent / "koszul-analytic-parent"
OLD_PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PREFIX = "research/l-families/atlas/generalized/extension-order-defect/"
FREEZE = "c3cdd2528595cbf22c31d88a40c8a611b6385752"
PINS = (
    (
        "constructible_pole_clearing_replay.py",
        "92b5297222f054e963e5dbb7be6a3edfbdd7db2d",
        "b957296cf28ac371d982d9f4325cfb992229b6b6c1280a6c7f7893a4bffce3e5",
    ),
    (
        "CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md",
        "7ed7f6d68327df4c5f395142503253b19e8938e4",
        "5182dde9511c093f9ba8f1f5fe554e6d7db1a45f724a42d52c9b11af882a0224",
    ),
    (
        "S3_WEIGHT_CIRCLE_POLE_DIVISOR.md",
        "381ee262cbd59f671a23f29fa19a9dd6f856463b",
        "0f5f303150da5e1d5dc181617b481ce6ab87003a30613693b8e59692cc04336f",
    ),
)
OWNED = (
    PREFIX + "EXTENSION_ORDER_DEFECT.md",
    PREFIX + "README.md",
    PREFIX + "replay.py",
    "tests/test_extension_order_defect.py",
)
FIXTURE = HERE / "verification.json"


def need(condition: bool, message: str):
    if not condition:
        raise ValueError(message)


def integer(value, low: int, high: int):
    need(
        type(value) is int and low <= value <= high,
        "bounded primitive integer required",
    )


def digest(data: bytes):
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen():
    for name, blob, expected in PINS:
        actual = subprocess.check_output(
            ["git", "rev-parse", FREEZE + ":" + OLD_PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(actual == blob, "extension-order dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "extension-order frozen source hash mismatch")
        need(
            digest((OLD / name).read_bytes()) == expected,
            "working extension-order source changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location(
    "frozen_constructible_source", OLD / "constructible_pole_clearing_replay.py"
)
need(
    SPEC is not None and SPEC.loader is not None,
    "authenticated source import unavailable",
)
SOURCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SOURCE)


def mul(a, b, cut: int):
    out = [0] * (cut + 1)
    for i, x in enumerate(a[: cut + 1]):
        for j, y in enumerate(b[: cut + 1 - i]):
            out[i + j] += x * y
    return out


def divide(a, b, cut: int):
    need(b and b[0] == 1, "formal unit denominator required")
    out = [0] * (cut + 1)
    for n in range(cut + 1):
        out[n] = (a[n] if n < len(a) else 0) - sum(
            b[j] * out[n - j] for j in range(1, min(n, len(b) - 1) + 1)
        )
    return out


def power(poly, exponent: int, cut: int):
    integer(exponent, -(10**7), 10**7)
    integer(cut, 0, 64)
    need(poly and poly[0] == 1, "normalized determinant polynomial required")
    remaining = abs(exponent)
    out = [1] + [0] * cut
    factor = list(poly)
    while remaining:
        if remaining % 2:
            out = mul(out, factor, cut)
        remaining //= 2
        if remaining:
            factor = mul(factor, factor, cut)
    return divide([1], out, cut) if exponent < 0 else out


def substitute(poly, order: int, sign: int, cut: int):
    integer(order, 1, 32)
    need(type(sign) is int and sign in (-1, 1), "exact source sign required")
    out = [0] * (cut + 1)
    for n, value in enumerate(poly):
        if order * n <= cut:
            out[order * n] = value * sign**n
    return out


@lru_cache(maxsize=512)
def _compositions(total: int, length: int):
    if length == 1:
        return ((total,),)
    return tuple(
        (first,) + rest
        for first in range(total + 1)
        for rest in _compositions(total - first, length - 1)
    )


def compositions(total: int, length: int):
    integer(total, 0, 12)
    integer(length, 1, 4)
    return _compositions(total, length)


def swap_last(values):
    return values[:-2] + (values[-1], values[-2])


def reflection_state(state):
    v, w, s = state
    return swap_last(v), swap_last(w), swap_last(s)


def primitive_c2(grade: int, letters: int = 3):
    """Orbit bases and explicit disjoint-support injection, not character averaging."""
    integer(grade, 0, 8)
    need(
        type(letters) is int and letters in (3, 4),
        "three/four-letter permutation source required",
    )
    need(letters == 3 or grade <= 3, "S4 primitive holdout stops at degree three")
    before = after = generic = 0
    component_rows = []
    for k in range(grade // 2 + 1):
        r = grade - 2 * k
        a_basis = tuple(
            (v, w)
            for v in compositions(r, letters - 1)
            for w in compositions(r, letters)
        )
        s_basis = compositions(k, letters - 1)
        states = tuple((v, w, s) for v, w in a_basis for s in s_basis)
        representatives = {min(state, reflection_state(state)) for state in states}
        a_orbits = {
            min(pair, (swap_last(pair[0]), swap_last(pair[1]))) for pair in a_basis
        }
        used = set()
        columns = 0
        for av, aw in sorted(a_orbits):
            orbit = {(av, aw), (swap_last(av), swap_last(aw))}
            for invariant_exp in compositions(k, letters - 2):
                fixed = invariant_exp[:-1]
                moving_degree = invariant_exp[-1]
                image = {}
                for v, w in orbit:
                    for u in range(moving_degree + 1):
                        s_exp = fixed + (u, moving_degree - u)
                        image[(v, w, s_exp)] = comb(moving_degree, u)
                need(
                    image
                    and all(
                        image.get(reflection_state(state)) == coefficient
                        for state, coefficient in image.items()
                    ),
                    "literal after-source image is not reflection invariant",
                )
                support = {min(state, reflection_state(state)) for state in image}
                need(
                    support <= representatives and not (support & used),
                    "source injection lost disjoint nonzero column supports",
                )
                used.update(support)
                columns += 1
        need(
            columns <= len(representatives),
            "explicit comparison injection has excessive rank",
        )
        generic += len(states)
        before += len(representatives)
        after += columns
        component_rows.append(
            {
                "symmetric_generator_degree": k,
                "Segre_grade": r,
                "ambient_dimension": len(states),
                "before_orbit_basis_size": len(representatives),
                "after_independent_columns": columns,
            }
        )
    return {
        "grade": grade,
        "permutation_letters": letters,
        "generic_dimension": generic,
        "after_dimension": after,
        "before_dimension": before,
        "cokernel_dimension": before - after,
        "injection_certified_by_disjoint_orbit_coordinate_supports": True,
        "components": component_rows,
    }


def cyclotomic_add(a, b):
    return a[0] + b[0], a[1] + b[1]


def cyclotomic_mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def primitive_fourier_source():
    one, omega, omega2 = (1, 0), (0, 1), (-1, -1)
    plus, minus = (one, omega2, omega), (one, omega, omega2)
    for vector, eigen in ((plus, omega), (minus, omega2)):
        cycle = (vector[2], vector[0], vector[1])
        need(
            cycle == tuple(cyclotomic_mul(eigen, value) for value in vector),
            "literal permutation cycle lost its Fourier eigenvector",
        )
        need(
            cyclotomic_add(cyclotomic_add(vector[0], vector[1]), vector[2]) == (0, 0),
            "Fourier vector escaped the actual standard subspace",
        )
    need(
        (plus[0], plus[2], plus[1]) == minus,
        "residual reflection must swap the two Fourier weights",
    )
    minor = cyclotomic_add(
        cyclotomic_mul(plus[0], minus[1]),
        tuple(-x for x in cyclotomic_mul(plus[1], minus[0])),
    )
    need(minor != (0, 0), "standard Fourier vectors are dependent")
    return {
        "minimal_polynomial": [1, 1, 1],
        "W_trivial_vector": [one, one, one],
        "V_plus": plus,
        "V_minus": minus,
        "literal_cycle_and_reflection_checked": True,
        "nonzero_standard_minor": minor,
    }


def fourier_weight(state):
    v, w, s = state
    return (v[0] - v[1] + w[1] - w[2] + s[0] - s[1]) % 3


def primitive_infinity(grade: int):
    integer(grade, 0, 8)
    primitive_fourier_source()
    before = after = fixed_before = fixed_after = 0
    if grade % 2 == 0:
        for k in range(grade // 2 + 1):
            r = grade - 2 * k
            states = [
                (v, w, s)
                for v in compositions(r, 2)
                for w in compositions(r, 3)
                for s in compositions(k, 2)
            ]
            invariant = {state for state in states if fourier_weight(state) == 0}
            need(
                all(reflection_state(state) in invariant for state in invariant),
                "normalizer reflection does not preserve C3 invariant basis",
            )
            fixed = sum(reflection_state(state) == state for state in invariant)
            before += len(invariant)
            fixed_before += fixed
            if k == 0:
                after += len(invariant)
                fixed_after += fixed
    dimension, trace = before - after, fixed_before - fixed_after
    need(
        dimension >= trace >= 0 and (dimension - trace) % 2 == 0,
        "actual quotient reflection cycles have invalid multiplicities",
    )
    return {
        "grade": grade,
        "before_dimension": before,
        "after_dimension": after,
        "cokernel_dimension": dimension,
        "before_residual_trace": fixed_before,
        "after_residual_trace": fixed_after,
        "cokernel_residual_trace": trace,
        "cokernel_residual_plus_minus_multiplicities": [
            (dimension + trace) // 2,
            (dimension - trace) // 2,
        ],
        "after_basis_is_literal_k_zero_subset": True,
    }


def primitive_zero(grade: int):
    integer(grade, 0, 8)
    weights = [0, 0, 0]
    fixed = 0
    if grade % 2 == 0:
        for k in range(grade // 2 + 1):
            r = grade - 2 * k
            for v in compositions(r, 2):
                for w in compositions(r, 3):
                    for s in compositions(k, 2):
                        state = (v, w, s)
                        weights[fourier_weight(state)] += 1
                        fixed += reflection_state(state) == state
    need(
        weights[1] == weights[2],
        "literal standard/permutation source lost conjugate Fourier weights",
    )
    return {
        "grade": grade,
        "after_equals_before_on_the_same_basis": True,
        "common_class_traces_e_s_c": [sum(weights), fixed, weights[0] - weights[1]],
        "cokernel_dimension": 0,
    }


P_OLD = [1, 1, 3, 1]
R_OLD = [1, 0, 3, 1, 1]
J_INF = [1, 3, 10, 7, 3]
K_INF = [1, 2, 20, 14, 22, 10, 3]


def rational_local(kind: str, which: str, cut: int = 24, epsilon: int = 1):
    integer(cut, 0, 32)
    need(
        kind in ("old", "infinity_split", "infinity_nonsplit"),
        "actual nonzero-defect stratum required",
    )
    need(
        which in ("after", "before", "difference", "ratio"),
        "declared scalar construction required",
    )
    need(
        type(epsilon) is int and epsilon in (-1, 1),
        "actual residue-field sign required",
    )
    if kind == "old":
        after_den = mul(power([1, -1], 5, cut), power([1, 1], 3, cut), cut)
        before_den = mul(
            mul(power([1, -1], 6, cut), power([1, 1], 3, cut), cut), [1, 0, 1], cut
        )
        after = substitute(divide(P_OLD, after_den, cut), 1, epsilon, cut)
        before = substitute(divide(R_OLD, before_den, cut), 1, epsilon, cut)
    elif kind == "infinity_split":
        after_den = mul(power([1, -1], 4, cut), [1, 1, 1], cut)
        before_den = mul(power([1, -1], 6, cut), power([1, 1, 1], 2, cut), cut)
        after = substitute(divide(J_INF, after_den, cut), 2, 1, cut)
        before = substitute(divide(K_INF, before_den, cut), 2, 1, cut)
    else:
        after = substitute(power([1, -1], -2, cut), 2, 1, cut)
        before = substitute(
            divide([1], mul(power([1, -1], 3, cut), [1, 1], cut), cut), 2, 1, cut
        )
    if which == "after":
        return after
    if which == "before":
        return before
    if which == "difference":
        return [c - b for b, c in zip(after, before)]
    return divide(before, after, cut)


def molien_before(kind: str, cut: int = 24, epsilon: int = 1):
    integer(cut, 2, 24)
    need(
        kind in ("old", "infinity_split", "infinity_nonsplit"),
        "actual source stratum required",
    )
    generic = (
        {
            h: SOURCE.local_source("good", h, 1, min(cut, 16))["declared_B_series"]
            for h in ("e", "s", "c")
        }
        if cut <= 16
        else {}
    )
    # For larger formal controls use the frozen Segre representation series,
    # not the new closed rational numerator.
    if not generic:
        generic = {
            h: divide(
                SOURCE.M.segre_series(h, cut),
                substitute(SOURCE.standard_determinant(h), 2, 1, cut),
                cut,
            )
            for h in ("e", "s", "c")
        }
    if kind == "old":
        numerator = [a + b for a, b in zip(generic["e"], generic["s"])]
        divisor = 2
    elif kind == "infinity_split":
        numerator = [
            a + 2 * b if n % 2 == 0 else 0
            for n, (a, b) in enumerate(zip(generic["e"], generic["c"]))
        ]
        divisor = 3
    else:
        numerator, divisor = (
            [a if n % 2 == 0 else 0 for n, a in enumerate(generic["s"])],
            1,
        )
    need(all(a % divisor == 0 for a in numerator), "Molien source average not integral")
    out = [a // divisor for a in numerator]
    return substitute(out, 1, epsilon if kind == "old" else 1, cut)


def primitive_comparison(cut: int = 8):
    integer(cut, 0, 8)
    old, infinity, zero = [], [], []
    old_b = rational_local("old", "after", cut)
    old_c = rational_local("old", "before", cut)
    inf_b = rational_local("infinity_split", "after", cut)
    inf_c = rational_local("infinity_split", "before", cut)
    inf_bs = rational_local("infinity_nonsplit", "after", cut)
    inf_cs = rational_local("infinity_nonsplit", "before", cut)
    for n in range(cut + 1):
        row = primitive_c2(n)
        need(
            [row["after_dimension"], row["before_dimension"]] == [old_b[n], old_c[n]],
            "literal C2 orbit source contradicts the all-grade rational identity",
        )
        old.append(row)
        row = primitive_infinity(n)
        need(
            [
                row["after_dimension"],
                row["before_dimension"],
                row["after_residual_trace"],
                row["before_residual_trace"],
            ]
            == [inf_b[n], inf_c[n], inf_bs[n], inf_cs[n]],
            "literal infinity quotient source contradicts its residual Molien table",
        )
        infinity.append(row)
        row = primitive_zero(n)
        if n >= 2:
            expected = [
                SOURCE.local_source("zero", h, 1, n)["declared_B_series"][n]
                for h in ("e", "s", "c")
            ]
            need(
                row["common_class_traces_e_s_c"] == expected,
                "zero comparison disagrees with the actual frozen source",
            )
        zero.append(row)
    return {
        "primitive_max_grade": cut,
        "old_C2": old,
        "infinity_with_residual_Frobenius": infinity,
        "central_quadratic_zero": zero,
        "S4_standard_permutation_C2_holdout": [primitive_c2(n, 4) for n in range(4)],
    }


def ordinary_cokernel_graded(kind: str, cut: int = 12, epsilon: int = 1):
    integer(cut, 4, 24)
    need(
        kind in ("old", "infinity_split", "infinity_nonsplit"),
        "actual defect stratum required",
    )
    dimensions = rational_local(
        "old" if kind == "old" else "infinity_split", "difference", cut
    )
    traces = rational_local(kind, "difference", cut, epsilon)
    result = [1] + [0] * cut
    eigen_rows = []
    for n in range(1, cut + 1):
        if kind == "old":
            plus = dimensions[n] if epsilon**n == 1 else 0
            minus = dimensions[n] - plus
        else:
            need(
                (dimensions[n] + traces[n]) % 2 == 0,
                "residual trace has wrong quotient parity",
            )
            plus, minus = (
                (dimensions[n] + traces[n]) // 2,
                (dimensions[n] - traces[n]) // 2,
            )
        need(
            plus >= 0 and minus >= 0,
            "actual cokernel determinant has negative multiplicity",
        )
        for sign, multiplicity in ((1, plus), (-1, minus)):
            factor = substitute([1, -sign], n, 1, cut)
            result = mul(result, power(factor, -multiplicity, cut), cut)
        if dimensions[n]:
            eigen_rows.append(
                {
                    "grade": n,
                    "dimension": dimensions[n],
                    "Frobenius_plus_minus": [plus, minus],
                }
            )
    return {
        "ordinary_graded_determinant": result,
        "finite_grade_eigenmultiplicities": eigen_rows,
    }


def scalar_shadow_control(kind: str, epsilon: int = 1):
    ratio = rational_local(kind, "ratio", 12, epsilon)
    ordinary = ordinary_cokernel_graded(kind, 12, epsilon)
    need(
        ratio != ordinary["ordinary_graded_determinant"],
        "additive cokernel determinant was silently identified with the nonlinear ratio",
    )
    if kind == "old":
        need(
            ratio[3:5] == [3 * epsilon, 0]
            and ordinary["ordinary_graded_determinant"][3:5] == [3 * epsilon, 9],
            "first scalar-shadow discrepancy moved from degree four",
        )
    return {
        "stratum": kind,
        "residue_sign": epsilon,
        "Hilbert_ratio": ratio,
        **ordinary,
        "first_difference_grade": next(
            n
            for n, (a, b) in enumerate(
                zip(ratio, ordinary["ordinary_graded_determinant"])
            )
            if a != b
        ),
    }


def global_boundary_control(index: int, cut: int = 16):
    integer(index, 0, 2)
    integer(cut, 4, 24)
    inventory = SOURCE.D.branch_inventory(index)
    q = inventory["parameters"][0]
    infinity = "infinity_split" if q % 3 == 1 else "infinity_nonsplit"
    before = rational_local(infinity, "before", cut)
    after = rational_local(infinity, "after", cut)
    ratio = rational_local(infinity, "ratio", cut)
    ordinary = ordinary_cokernel_graded(infinity, cut)["ordinary_graded_determinant"]
    positive = 0
    for row in inventory["closed_branch_rows"]:
        degree, sign, count = row["degree"], row["chi"], row["count"]
        local_b = substitute(rational_local("old", "after", cut, sign), degree, 1, cut)
        local_c = substitute(rational_local("old", "before", cut, sign), degree, 1, cut)
        local_ratio = substitute(
            rational_local("old", "ratio", cut, sign), degree, 1, cut
        )
        local_ordinary = substitute(
            ordinary_cokernel_graded("old", cut, sign)["ordinary_graded_determinant"],
            degree,
            1,
            cut,
        )
        after, before = (
            mul(after, power(local_b, count, cut), cut),
            mul(before, power(local_c, count, cut), cut),
        )
        ratio, ordinary = (
            mul(ratio, power(local_ratio, count, cut), cut),
            mul(ordinary, power(local_ordinary, count, cut), cut),
        )
        positive += count if sign == 1 else 0
    need(
        before == mul(after, ratio, cut),
        "actual all-branch Euler correction failed finite product comparison",
    )
    need(
        ratio[4] == (13 if q % 3 == 1 else 1),
        "full global ratio lost the infinity degree-four witness",
    )
    need(
        ordinary != ratio,
        "actual global source masks every distinction between the two scalar shadows",
    )
    return {
        "parameters": inventory["parameters"],
        "actual_closed_branch_rows": inventory["closed_branch_rows"],
        "rational_boundary_Hilbert_ratio": ratio,
        "ordinary_graded_boundary_determinant": ordinary,
        "after_bad_product": after,
        "before_bad_product": before,
        "rational_ratio_pole_order_at_one": (2 if q % 3 == 1 else 1) + positive,
        "no_degree_four_field_enumerated": not inventory[
            "degree_four_field_enumerated"
        ],
        "first_difference_grade": next(
            n for n, (a, b) in enumerate(zip(ratio, ordinary)) if a != b
        ),
    }


def all_grade_rational_controls():
    rows = []
    for kind in ("old", "infinity_split", "infinity_nonsplit"):
        for epsilon in (-1, 1) if kind == "old" else (1,):
            before = rational_local(kind, "before", 24, epsilon)
            need(
                before == molien_before(kind, 24, epsilon),
                "closed all-grade numerator disagrees with the independent source Molien sum",
            )
            rows.append(
                {
                    "stratum": kind,
                    "residue_sign": epsilon,
                    "before_prefix": before,
                    "after_prefix": rational_local(kind, "after", 24, epsilon),
                    "additive_defect_prefix": rational_local(
                        kind, "difference", 24, epsilon
                    ),
                }
            )
    return rows


def arithmetic_nonvanishing_controls():
    reciprocal_old = list(reversed(R_OLD))
    reciprocal_inf = list(reversed(K_INF))
    # Coefficients are low-to-high: reversing a constant-one numerator
    # gives a monic reciprocal, whose constant term is the old leading term.
    need(
        reciprocal_old[-1] == reciprocal_inf[-1] == 1
        and reciprocal_old[0] == 1
        and reciprocal_inf[0] == 3,
        "new reciprocal numerator escaped characteristic-independent prime support",
    )
    return {
        "old_C2_reciprocal_low_to_high": reciprocal_old,
        "split_infinity_reciprocal_low_to_high": reciprocal_inf,
        "constant_term_prime_support": [[], [3]],
        "hypothesis_characteristic_p_greater_than_three": True,
        "arithmetic_pole_divisor_equals_after_source_by_proof_not_finite_fit": True,
        "new_nonarithmetic_poles_excluded_by_common_good_factor_extraction": True,
    }


def build_payload():
    authenticate_frozen()
    return {
        "schema": "extension-order-boundary-module-v1",
        "provenance": {
            "freeze": FREEZE,
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((ROOT / name).read_bytes()) for name in OWNED
            },
        },
        "literal_Fourier_source": primitive_fourier_source(),
        "primitive_invariant_comparison": primitive_comparison(),
        "all_grade_Molien_controls": all_grade_rational_controls(),
        "two_distinct_scalar_shadows": [
            scalar_shadow_control("old", epsilon) for epsilon in (-1, 1)
        ]
        + [
            scalar_shadow_control(kind)
            for kind in ("infinity_split", "infinity_nonsplit")
        ],
        "actual_global_boundary_factors": [
            global_boundary_control(index) for index in range(3)
        ],
        "arithmetic_pole_transfer": arithmetic_nonvanishing_controls(),
        "not_claimed": [
            "cokernel is a quotient algebra",
            "ordinary L(Q) equals nonlinear Hilbert ratio",
            "derived cone supplies new higher defect groups",
            "canonical among every source with the same scalar function",
            "same zero divisor or Taylor coefficients",
            "new fields or global S4 pole theorem",
            "infinite-rank cohomology, operator-domain extension or archimedean transfer",
        ],
    }


def check_payload(candidate):
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "extension-order fixture differs from authenticated primitive replay",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(
            json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")), sort_keys=True)
            == json.dumps(payload, sort_keys=True),
            "extension-order fixture mismatch",
        )
    print(
        "PASS actual extension-order boundary module, residual Frobenius and distinct scalar shadows"
    )


if __name__ == "__main__":
    main()

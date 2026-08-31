#!/usr/bin/env python3
"""Literal C6 infinity covariants and relative A2 matrix-factorization controls."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/extension-order-defect/"
PINS = (
    (
        "0018b73f60e42bc793d172c381547de34322d8ca",
        PREFIX + "EXTENSION_ORDER_DEFECT.md",
        "dfb7fcbf1115846664fa99e71116a3635b14d7a0",
    ),
    (
        "cfcfa42264a4ce5fc5846ac468c0c51c4cab9267",
        PREFIX + "INVARIANT_GENERATOR_BASE.md",
        "9174c003f6ab9c04d3ab4aa02afda45e28b96ad9",
    ),
    (
        "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93",
        "research/l-families/atlas/generalized/koszul-analytic-parent/MATHEMATICS.md",
        "02d8cda2a0c50876d378eb1eeb29df85b3b096b3",
    ),
)
MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_FIXTURE_BYTES = 2 * 1024 * 1024
FIXTURE = HERE / "cyclic_infinity.verification.json"
OWNED = (
    HERE / "CYCLIC_INFINITY_INVARIANT_MODULE.md",
    HERE / "CYCLIC_INFINITY_PREREGISTRATION.md",
    HERE / "CYCLIC_INFINITY_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_extension_order_cyclic_infinity.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label):
    require(type(value) is int and low <= value <= high, label)
    return value


def exact_bool(value):
    require(type(value) is bool, "literal quadratic projection switch")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate():
    result = []
    for commit, path, expected in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_SOURCE_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(len(raw) == size and blob == expected, "frozen source authentication")
        result.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": sha256(raw).hexdigest(),
            }
        )
    return result


def segre_monomial(value):
    require(type(value) is tuple and len(value) == 5, "Segre monomial tuple")
    m, a, b, c, d = value
    integer(m, 0, 8, "Segre degree cap")
    for entry in (a, b, c, d):
        integer(entry, 0, m, "Segre exponent")
    require(b + c + d == m, "Segre column total")
    return value


def charge(value):
    m, a, _b, c, d = segre_monomial(value)
    return (2 * m - a + c + 2 * d) % 3


def segre_basis(degree, character=None):
    integer(degree, 0, 8, "Segre degree cap")
    if character is not None:
        integer(character, 0, 2, "C3 character")
    result = []
    for a in range(degree + 1):
        for b in range(degree + 1):
            for c in range(degree - b + 1):
                value = (degree, a, b, c, degree - b - c)
                if character is None or charge(value) == character:
                    result.append(value)
    return tuple(result)


def divides(factor, value):
    fm, fa, fb, fc, fd = segre_monomial(factor)
    m, a, b, c, d = segre_monomial(value)
    return fa <= a and fm - fa <= m - a and fb <= b and fc <= c and fd <= d


def multiply_segre(left, right):
    segre_monomial(left)
    segre_monomial(right)
    return segre_monomial(tuple(a + b for a, b in zip(left, right, strict=True)))


def old_invariant_factor(value, even_source):
    segre_monomial(value)
    exact_bool(even_source)
    step = 2 if even_source else 1
    require(not even_source or value[0] % 2 == 0, "actual C6 even source")
    for degree in range(step, value[0] + 1, step):
        for factor in segre_basis(degree, 0):
            if divides(factor, value):
                return factor
    return None


def covariant_minimal(character, even_source=True, cutoff=8):
    integer(character, 1, 2, "nontrivial C3 character")
    exact_bool(even_source)
    integer(cutoff, 0, 8, "covariant cutoff")
    result = []
    for degree in range(2 if even_source else 1, cutoff + 1, 2 if even_source else 1):
        for value in segre_basis(degree, character):
            if old_invariant_factor(value, even_source) is None:
                result.append(value)
    return tuple(result)


def degree_four_old_span(character):
    integer(character, 1, 2, "nontrivial C3 character")
    products = {
        multiply_segre(left, right)
        for left in segre_basis(2, 0)
        for right in segre_basis(2, character)
    }
    basis = set(segre_basis(4, character))
    require(products <= basis, "actual degree-four product image")
    return {
        "basis_dimension": len(basis),
        "old_rank": len(products),
        "old_monomials": [list(x) for x in sorted(products)],
        "new_monomials": [list(x) for x in sorted(basis - products)],
    }


def combined_monomial(value):
    require(type(value) is tuple and len(value) == 7, "combined monomial tuple")
    base = segre_monomial(value[:5])
    p, q = value[5:]
    integer(p, 0, 4, "added standard exponent")
    integer(q, 0, 4, "added standard exponent")
    require(base[0] + 2 * (p + q) <= 8, "combined grading cap")
    return value


def combined_degree(value):
    combined_monomial(value)
    return value[0] + 2 * (value[5] + value[6])


def combined_basis(degree, even_source=True):
    integer(degree, 0, 8, "combined degree cap")
    exact_bool(even_source)
    result = []
    for m in range(degree + 1):
        if (even_source and m % 2) or (degree - m) % 2:
            continue
        power = (degree - m) // 2
        for value in segre_basis(m):
            for p in range(power + 1):
                q = power - p
                if (charge(value) + p + 2 * q) % 3 == 0:
                    result.append(value + (p, q))
    return tuple(result)


def reducible_over_full_base(value, even_source=True):
    combined_monomial(value)
    exact_bool(even_source)
    p, q = value[5:]
    if p >= 3 or q >= 3 or (p and q):
        return True
    return old_invariant_factor(value[:5], even_source) is not None


def combined_minimal(even_source=True, cutoff=8):
    exact_bool(even_source)
    integer(cutoff, 0, 8, "minimal generator cutoff")
    return tuple(
        value
        for degree in range(cutoff + 1)
        for value in combined_basis(degree, even_source)
        if not reducible_over_full_base(value, even_source)
    )


def phi(value):
    combined_monomial(value)
    m, a, b, c, d, p, q = value
    return (m, m - a, b, d, c, q, p)


def int_polynomial_multiply(left, right):
    require(
        type(left) is list
        and type(right) is list
        and len(left) <= 33
        and len(right) <= 33,
        "small integer polynomial",
    )
    require(
        all(type(x) is int for x in left + right), "integer polynomial coefficients"
    )
    result = [0] * max(1, len(left) + len(right) - 1)
    require(len(result) <= 65, "polynomial product cap")
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def residual_action(basis):
    require(
        type(basis) is tuple and len(set(basis)) == len(basis), "literal quotient basis"
    )
    index = {value: i for i, value in enumerate(basis)}
    permutation = []
    for value in basis:
        target = phi(value)
        require(
            target in index and phi(target) == value,
            "normalizer preserves quotient basis and squares to identity",
        )
        permutation.append(index[target])
    used, cycles = set(), []
    for i in range(len(basis)):
        if i not in used:
            cycle, j = [], i
            while j not in used:
                used.add(j)
                cycle.append(j)
                j = permutation[j]
            require(j == i and len(cycle) in (1, 2), "actual involution cycle")
            cycles.append(cycle)
    determinant = [1]
    for cycle in cycles:
        determinant = int_polynomial_multiply(
            determinant, [1] + [0] * (len(cycle) - 1) + [-1]
        )
    return {
        "dimension": len(basis),
        "permutation": permutation,
        "cycles": cycles,
        "trace": sum(len(c) == 1 for c in cycles),
        "trace_square": len(basis),
        "determinant": determinant,
    }


def rational_series(numerator, denominator, cutoff):
    integer(cutoff, 0, 8, "rational series cutoff")
    require(
        denominator
        and denominator[0] == 1
        and all(type(x) is int for x in numerator + denominator),
        "normalized integer rational series",
    )
    result = []
    for n in range(cutoff + 1):
        value = numerator[n] if n < len(numerator) else 0
        value -= sum(
            denominator[j] * result[n - j]
            for j in range(1, min(n, len(denominator) - 1) + 1)
        )
        result.append(value)
    return result


def power_polynomial(value, exponent):
    integer(exponent, 0, 8, "polynomial power cap")
    result = [1]
    for _ in range(exponent):
        result = int_polynomial_multiply(result, value)
    return result


def uvw_poly(value):
    require(type(value) is dict and len(value) <= 32, "free hypersurface polynomial")
    result = {}
    for monomial, coefficient in value.items():
        require(type(monomial) is tuple and len(monomial) == 3, "uvw monomial")
        require(
            all(type(x) is int and 0 <= x <= 8 for x in monomial), "uvw exponent cap"
        )
        require(
            6 * monomial[0] + 4 * monomial[1] + 6 * monomial[2] <= 32,
            "weighted polynomial cap",
        )
        require(
            type(coefficient) is int and abs(coefficient) <= 1024,
            "bounded integer polynomial coefficient",
        )
        if coefficient:
            result[monomial] = coefficient
    return result


def add_poly(left, right):
    result = dict(uvw_poly(left))
    for monomial, coefficient in uvw_poly(right).items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return uvw_poly(result)


def multiply_poly(left, right):
    result = {}
    for monomial, coefficient in uvw_poly(left).items():
        for other, entry in uvw_poly(right).items():
            target = tuple(a + b for a, b in zip(monomial, other, strict=True))
            result[target] = result.get(target, 0) + coefficient * entry
    return uvw_poly(result)


def matrices():
    u, v, w = {(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1}
    v2 = {(0, 2, 0): 1}
    return [[w, {(0, 2, 0): -1}], [{(0, 1, 0): -1}, u]], [[u, v2], [v, w]]


def multiply_matrix(left, right):
    require(
        len(left) == len(right) == 2 and all(len(row) == 2 for row in left + right),
        "two by two polynomial matrices",
    )
    return [
        [
            add_poly(
                multiply_poly(left[i][0], right[0][j]),
                multiply_poly(left[i][1], right[1][j]),
            )
            for j in range(2)
        ]
        for i in range(2)
    ]


def substitute_pq(poly):
    result = {}
    for (u, v, w), coefficient in uvw_poly(poly).items():
        target = (3 * u + v, v + 3 * w)
        result[target] = result.get(target, 0) + coefficient
    return {key: value for key, value in result.items() if value}


def normal_form(value):
    require(
        type(value) is tuple
        and len(value) == 3
        and all(type(x) is int and 0 <= x <= 8 for x in value),
        "normal-form monomial",
    )
    u, v, w = value
    common = min(u, w)
    return (u - common, v + 3 * common, w - common)


def t_basis(degree):
    integer(degree, -16, 16, "weighted T degree cap")
    if degree < 0:
        return ()
    return tuple(
        (u, v, w)
        for u in range(degree // 6 + 1)
        for v in range(degree // 4 + 1)
        for w in range(degree // 6 + 1)
        if 6 * u + 4 * v + 6 * w == degree and not (u and w)
    )


def free_basis(degree, shifts):
    integer(degree, 0, 16, "weighted map degree cap")
    require(
        type(shifts) is tuple
        and len(shifts) == 2
        and all(type(x) is int and 0 <= x <= 16 for x in shifts),
        "two weighted free shifts",
    )
    return tuple(
        (i, monomial)
        for i, shift in enumerate(shifts)
        for monomial in t_basis(degree - shift)
    )


def graded_matrix(matrix, degree, source_shifts, target_shifts):
    source_basis = free_basis(degree, source_shifts)
    target_basis = free_basis(degree, target_shifts)
    target_index = {value: i for i, value in enumerate(target_basis)}
    result = [[0] * len(source_basis) for _ in target_basis]
    for j, (component, monomial) in enumerate(source_basis):
        for i in range(2):
            for entry, coefficient in uvw_poly(matrix[i][component]).items():
                image = (
                    i,
                    normal_form(
                        tuple(a + b for a, b in zip(monomial, entry, strict=True))
                    ),
                )
                require(image in target_index, "matrix preserves exact weighted degree")
                result[target_index[image]][j] += coefficient
    return source_basis, target_basis, result


def presentation_matrix(degree):
    integer(degree, 0, 16, "presentation degree cap")
    source_basis = free_basis(degree, (2, 4))
    power = degree // 2
    targets = tuple(
        (p, power - p)
        for p in range(power + 1)
        if degree % 2 == 0 and (p + 2 * (power - p)) % 3 == 1
    )
    index = {value: i for i, value in enumerate(targets)}
    result = [[0] * len(source_basis) for _ in targets]
    for j, (component, (u, v, w)) in enumerate(source_basis):
        p, q = 3 * u + v, v + 3 * w
        p, q = (p + 1, q) if component == 0 else (p, q + 2)
        require((p, q) in index, "literal covariant presentation image")
        result[index[p, q]][j] = 1
    return source_basis, targets, result


def linear_data(matrix, columns):
    integer(columns, 0, 16, "small linear column cap")
    require(
        type(matrix) is list
        and len(matrix) <= 16
        and all(
            type(row) is list
            and len(row) == columns
            and all(type(x) is int for x in row)
            for row in matrix
        ),
        "small exact matrix",
    )
    rows = [[Fraction(value) for value in row] for row in matrix]
    pivot_columns, pivot_row = [], 0
    for column in range(columns):
        selected = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][column]), None
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [
                    a - scale * b for a, b in zip(rows[i], rows[pivot_row], strict=True)
                ]
        pivot_columns.append(column)
        pivot_row += 1
    kernel = []
    for column in range(columns):
        if column not in pivot_columns:
            vector = [Fraction(0)] * columns
            vector[column] = Fraction(1)
            for i, pivot in enumerate(pivot_columns):
                vector[pivot] = -rows[i][column]
            kernel.append([[value.numerator, value.denominator] for value in vector])
    return {
        "rank": pivot_row,
        "nullity": columns - pivot_row,
        "pivot_columns": pivot_columns,
        "kernel_basis": kernel,
    }


def integer_matrix_product(left, right, right_columns):
    integer(right_columns, 0, 16, "matrix product column cap")
    inner = len(right)
    require(
        all(len(row) == inner for row in left)
        and all(len(row) == right_columns for row in right),
        "compatible small matrices",
    )
    return [
        [sum(row[k] * right[k][j] for k in range(inner)) for j in range(right_columns)]
        for row in left
    ]


def polynomial_json(poly):
    return [
        {"uvw": list(key), "coefficient": value}
        for key, value in sorted(uvw_poly(poly).items())
    ]


def mf_control(degree):
    integer(degree, 0, 16, "matrix-factorization degree cap")
    d1, d2 = matrices()
    f0, targets, pi = presentation_matrix(degree)
    f1, target_f0, first = graded_matrix(d1, degree, (8, 10), (2, 4))
    f2, target_f1, second = graded_matrix(d2, degree, (14, 16), (8, 10))
    require(target_f0 == f0 and target_f1 == f1, "same marked source and target bases")
    require(
        not any(any(row) for row in integer_matrix_product(pi, first, len(f1))),
        "literal presentation kills D1",
    )
    require(
        not any(any(row) for row in integer_matrix_product(first, second, len(f2))),
        "literal D1 kills D2",
    )
    pi_data, first_data, second_data = (
        linear_data(pi, len(f0)),
        linear_data(first, len(f1)),
        linear_data(second, len(f2)),
    )
    require(pi_data["rank"] == len(targets), "covariant presentation surjects")
    require(
        pi_data["nullity"] == first_data["rank"]
        and first_data["nullity"] == second_data["rank"],
        "selected exact kernel/image equalities",
    )
    return {
        "degree": degree,
        "F0_basis": [[i, list(m)] for i, m in f0],
        "F1_basis": [[i, list(m)] for i, m in f1],
        "F2_basis": [[i, list(m)] for i, m in f2],
        "P1_basis": [list(m) for m in targets],
        "presentation_matrix": pi,
        "D1_matrix": first,
        "D2_matrix": second,
        "presentation": pi_data,
        "D1": first_data,
        "D2": second_data,
    }


def build():
    provenance = authenticate()
    actual = combined_minimal(True)
    calibration = combined_minimal(False)
    actual_counts = {
        str(n): sum(combined_degree(value) == n for value in actual) for n in range(9)
    }
    calibration_counts = {
        str(n): sum(combined_degree(value) == n for value in calibration)
        for n in range(9)
    }
    require(
        actual_counts
        == {str(n): {0: 1, 4: 12, 6: 16, 8: 4}.get(n, 0) for n in range(9)},
        "actual C6 minimal-generator prediction",
    )
    require(
        calibration_counts
        == {str(n): {0: 1, 3: 4, 4: 4, 5: 4, 6: 4}.get(n, 0) for n in range(9)},
        "untwisted C3 calibration prediction",
    )
    covariants = []
    for character in (1, 2):
        generators = covariant_minimal(character)
        require(
            len(generators) == 8
            and sum(x[0] == 2 for x in generators) == 6
            and sum(x[0] == 4 for x in generators) == 2,
            "actual even-source covariant generators",
        )
        held_out = []
        for degree in (6, 8):
            basis = segre_basis(degree, character)
            require(
                all(any(divides(g, value) for g in generators) for value in basis),
                "held-out monomial generation",
            )
            held_out.append(
                {"degree": degree, "basis_count": len(basis), "all_generated": True}
            )
        old = degree_four_old_span(character)
        require(
            old["basis_dimension"] == 25 and old["old_rank"] == 23,
            "literal degree-four old-product rank",
        )
        covariants.append(
            {
                "character": character,
                "degree_two_basis": [list(x) for x in segre_basis(2, character)],
                "minimal_generators": [list(x) for x in generators],
                "degree_four": old,
                "held_out_grades": held_out,
            }
        )
    actions = []
    for degree in (0, 4, 6, 8):
        basis = tuple(value for value in actual if combined_degree(value) == degree)
        action = residual_action(basis)
        require(
            action["trace"] == (1 if degree == 0 else 0),
            "actual residual normalizer trace",
        )
        actions.append({"degree": degree, "basis": [list(x) for x in basis], **action})
    denominator = int_polynomial_multiply(
        power_polynomial([1, -1], 6), power_polynomial([1, 1, 1], 2)
    )
    predicted = rational_series([1, 2, 20, 14, 22, 10, 3], denominator, 4)
    literal_dimensions = [len(combined_basis(2 * n, True)) for n in range(5)]
    require(
        literal_dimensions == predicted,
        "frozen full C6 Molien function versus independent monomials",
    )
    d1, d2 = matrices()
    first, second = multiply_matrix(d1, d2), multiply_matrix(d2, d1)
    f = {(1, 0, 1): 1, (0, 3, 0): -1}
    expected = [[f, {}], [{}, f]]
    require(
        first == expected and second == expected,
        "matrix factorization before hypersurface quotient",
    )
    require(
        all(
            not substitute_pq(entry)
            for matrix in (first, second)
            for row in matrix
            for entry in row
        ),
        "independent p/q substitution",
    )
    payload = {
        "schema": "riemann.extension_order.cyclic_infinity.v1",
        "sources": provenance,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "actual_inertia": "C6: C3 weights and quadratic-even Segre projection",
        "covariants": covariants,
        "actual_minimal_monomials": [list(x) for x in actual],
        "actual_minimal_by_degree": actual_counts,
        "untwisted_calibration_monomials": [list(x) for x in calibration],
        "untwisted_calibration_by_degree": calibration_counts,
        "residual_normalizer": actions,
        "full_C_dimensions_even_grades_0_to_8": literal_dimensions,
        "independent_frozen_Molien_coefficients": predicted,
        "generic_rank_control": {
            "independent_group_order": 9,
            "diagonal_group_order": 3,
            "rank_from_fixed_field_theorem": 3,
            "minimal_generator_count": len(actual),
        },
        "matrix_factorization": {
            "D1": [[polynomial_json(entry) for entry in row] for row in d1],
            "D2": [[polynomial_json(entry) for entry in row] for row in d2],
            "D1_D2": [[polynomial_json(entry) for entry in row] for row in first],
            "D2_D1": [[polynomial_json(entry) for entry in row] for row in second],
            "weighted_shift": 12,
            "graded_controls": [mf_control(n) for n in (8, 10, 14, 16)],
        },
        "scope": {
            "actual_quadratic_inertia_retained": True,
            "all_grade_generation_from_proof_not_finite_fit": True,
            "old_cokernel_is_a_module_over_repaired_base": False,
            "whole_base_free_periodic_resolution_supplied": False,
            "relative_covariant_complex_supplied": True,
            "new_arithmetic_field_counts": False,
            "analytic_radius_inferred_from_trace": False,
        },
    }
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    return payload


def no_float(_value):
    raise ValueError("floating or nonfinite JSON value")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    require(
        type(raw) is str and len(raw.encode()) <= MAX_FIXTURE_BYTES, "JSON byte cap"
    )
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def verify_payload(actual, expected):
    require(
        canonical(actual) == canonical(expected),
        "strict full primitive replay mismatch",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        raw = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
        require(len(raw.encode()) <= MAX_FIXTURE_BYTES, "fixture byte cap")
        FIXTURE.write_text(raw, encoding="utf-8", newline="\n")
        print("wrote cyclic infinity primitive verification")
    else:
        require(FIXTURE.stat().st_size <= MAX_FIXTURE_BYTES, "fixture byte cap")
        verify_payload(read_json(FIXTURE.read_text(encoding="utf-8")), result)
        print("cyclic infinity primitive verification PASS")


if __name__ == "__main__":
    main()

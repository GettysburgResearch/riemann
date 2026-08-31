#!/usr/bin/env python3
"""Exact normalization-chart, covariant-generator and actual Lie-source controls."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/extension-order-defect/"
LIE_PREFIX = "research/l-families/atlas/generalized/koszul-analytic-parent/"
PINS = (
    (
        "d4fcbe331751e1e506cc2f38864c0c1580df92e8",
        PREFIX + "CYCLIC_INFINITY_INVARIANT_MODULE.md",
        "66540ad1ff0818cd04b9a75ad75b3eb50abe9466",
    ),
    (
        "d4fcbe331751e1e506cc2f38864c0c1580df92e8",
        PREFIX + "cyclic_infinity_replay.py",
        "8a8964436633d7528a19928388563b6af321ff6e",
    ),
    (
        "0018b73f60e42bc793d172c381547de34322d8ca",
        PREFIX + "EXTENSION_ORDER_DEFECT.md",
        "dfb7fcbf1115846664fa99e71116a3635b14d7a0",
    ),
    (
        "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93",
        LIE_PREFIX + "GLOBAL_KOSZUL_LIE_COHOMOLOGY.md",
        "6fc43276dc337c68ae4c3d9f70de22a114d14fa3",
    ),
    (
        "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93",
        LIE_PREFIX + "global_lie_cohomology_replay.py",
        "f6420dd1053cd1aab611747b2dec7c4310d55a96",
    ),
    (
        "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93",
        LIE_PREFIX + "global_lie_cohomology.verification.json",
        "67845de2de4c49c0a11b58bbf09efbe183897174",
    ),
)
MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_FIXTURE_BYTES = 2 * 1024 * 1024
MAX_POLYNOMIAL_DEGREE = 36
FIXTURE = HERE / "normalization.verification.json"
OWNED = (
    HERE / "NORMALIZATION_AND_INFINITE_BASE.md",
    HERE / "NORMALIZATION_PREREGISTRATION.md",
    HERE / "NORMALIZATION_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_extension_order_normalization.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label):
    require(type(value) is int and low <= value <= high, label)
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


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


def authenticate():
    provenance, sources = [], {}
    for commit, path, expected in PINS:
        ref = f"{commit}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_SOURCE_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(len(raw) == size and blob == expected, "frozen source authentication")
        sources[path] = raw
        provenance.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": sha256(raw).hexdigest(),
            }
        )
    return provenance, sources


def load_frozen_c6(raw):
    require(type(raw) is bytes and 0 < len(raw) <= MAX_SOURCE_BYTES, "source bytes")
    module = types.ModuleType("normalization_frozen_c6")
    module.__file__ = str(HERE / "cyclic_infinity_replay.py")
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def polynomial(value):
    require(
        type(value) is list and 1 <= len(value) <= MAX_POLYNOMIAL_DEGREE + 1,
        "polynomial degree cap",
    )
    require(all(type(x) is int for x in value), "integer polynomial coefficients")
    return value


def trim(value):
    polynomial(value)
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value


def poly_add(*values):
    require(1 <= len(values) <= 8, "polynomial summand cap")
    for value in values:
        polynomial(value)
    result = [0] * max(map(len, values))
    for value in values:
        for i, x in enumerate(value):
            result[i] += x
    return trim(result)


def poly_multiply(left, right):
    polynomial(left)
    polynomial(right)
    require(
        len(left) + len(right) - 2 <= MAX_POLYNOMIAL_DEGREE,
        "polynomial product degree cap",
    )
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def square_substitution(value):
    polynomial(value)
    require(2 * (len(value) - 1) <= MAX_POLYNOMIAL_DEGREE, "square substitution cap")
    result = [0] * (2 * len(value) - 1)
    for i, x in enumerate(value):
        result[2 * i] = x
    return trim(result)


def sym_square_series(value):
    result = poly_add(poly_multiply(value, value), square_substitution(value))
    require(all(x % 2 == 0 for x in result), "symmetric square integrality")
    return [x // 2 for x in result]


def monomial_exponents(value, length=3, cap=8):
    require(type(value) is tuple and len(value) == length, "literal exponent tuple")
    for x in value:
        integer(x, 0, cap, "monomial exponent cap")
    require(sum(value) <= cap, "monomial total length cap")
    return value


def fixed_locus_control():
    weights = tuple((a + b) % 3 for a in (1, 2) for b in (0, 1, 2))
    minors = []
    for positive, negative in (((0, 4), (1, 3)), ((0, 5), (2, 3)), ((1, 5), (2, 4))):
        terms = []
        for sign, pair in ((1, positive), (-1, negative)):
            exponent = tuple(pair.count(i) for i in range(6))
            terms.append({"coefficient": sign, "exponents": list(exponent)})
        require(
            len(
                {
                    sum(a * b for a, b in zip(weights, term["exponents"], strict=True))
                    % 3
                    for term in terms
                }
            )
            == 1,
            "minor weight homogeneity",
        )
        minors.append(terms)
    specialized = [
        [term for term in minor if all(term["exponents"][i] == 0 for i in (0, 1, 3, 5))]
        for minor in minors
    ]
    require(
        specialized == [[], [], [{"coefficient": -1, "exponents": [0, 0, 1, 0, 1, 0]}]],
        "literal fixed Segre equation",
    )
    return {
        "coordinate_order": ["a", "b", "c", "d", "e", "f"],
        "weights": list(weights),
        "actual_minors": minors,
        "fixed_specialization": specialized,
        "dimension_A": 4,
        "geometric_fixed_dimension_A": 1,
        "geometric_fixed_codimension_A": 3,
        "fixed_P_codimension": 2,
        "scheme_fixed_A_reduced_claimed": False,
    }


def add_exponents(left, right):
    require(
        type(left) is tuple and type(right) is tuple and len(left) == len(right) == 3,
        "chart exponent triples",
    )
    require(all(type(x) is int for x in left + right), "integer chart exponents")
    return tuple(a + b for a, b in zip(left, right, strict=True))


def chart_relations(y_z_power=2):
    integer(y_z_power, 0, 4, "y exponent cap")
    s, u, v, w = (3, 0, 0), (0, 3, 0), (0, 1, 1), (0, 0, 3)
    x, y = (1, 1, 0), (y_z_power, 0, 1)
    rows = [
        ("x^3=s*u", tuple(3 * a for a in x), add_exponents(s, u)),
        ("x*y=s*v", add_exponents(x, y), add_exponents(s, v)),
        (
            "y^3=s^2*w",
            tuple(3 * a for a in y),
            add_exponents(tuple(2 * a for a in s), w),
        ),
        ("u*w=v^3", add_exponents(u, w), tuple(3 * a for a in v)),
    ]
    require(all(left == right for _, left, right in rows), "scaled A2 chart relation")
    return [
        {"identity": name, "left": list(left), "right": list(right)}
        for name, left, right in rows
    ]


def chart_reduce(value):
    z, p, q = monomial_exponents(value)
    require((2 * z + p + 2 * q) % 3 == 0, "diagonal invariant chart monomial")
    difference = z - p - 2 * q
    require(difference % 3 == 0, "invariant chart multiple of three")
    s = difference // 3
    require(3 * s + p + 2 * q == z, "chart round trip")
    return (s, p, q)


def chart_control():
    rows = []
    for z in range(9):
        for p in range(9 - z):
            for q in range(9 - z - p):
                if (2 * z + p + 2 * q) % 3 == 0:
                    rows.append(
                        {"z_p_q": [z, p, q], "s_x_y": list(chart_reduce((z, p, q)))}
                    )
    return {
        "relations": chart_relations(),
        "bounded_monomials": rows,
        "s_is_inverted": True,
        "all_grade_descent_proved_separately": True,
    }


def matrix(value):
    require(type(value) is list and 1 <= len(value) <= 16, "matrix row cap")
    require(
        all(type(row) is list and len(row) == len(value) for row in value),
        "square matrix",
    )
    require(all(type(x) is int for row in value for x in row), "integer matrix entries")
    return value


def matrix_product(left, right):
    matrix(left)
    matrix(right)
    require(len(left) == len(right), "matrix dimensions")
    return [
        [
            sum(a * b for a, b in zip(row, column, strict=True))
            for column in zip(*right, strict=True)
        ]
        for row in left
    ]


def identity(n):
    integer(n, 1, 16, "matrix dimension cap")
    return [[int(i == j) for j in range(n)] for i in range(n)]


def fibre_control():
    basis = ((0, 0), (1, 0), (0, 1), (2, 0), (0, 2))
    index = {x: i for i, x in enumerate(basis)}
    maps = []
    for increment in ((1, 0), (0, 1)):
        action = [[0] * 5 for _ in basis]
        for j, value in enumerate(basis):
            target = tuple(a + b for a, b in zip(value, increment, strict=True))
            if target in index:
                action[index[target]][j] = 1
            else:
                require(
                    target[0] >= 3 or target[1] >= 3 or all(target),
                    "fibre relation covers discarded product",
                )
        maps.append(action)
    p, q = maps
    zero = [[0] * 5 for _ in basis]
    require(
        matrix_product(matrix_product(p, p), p) == zero
        and matrix_product(matrix_product(q, q), q) == zero
        and matrix_product(p, q) == zero,
        "actual origin fibre relations",
    )
    phi = [[int(i == index[(value[1], value[0])]) for value in basis] for i in range(5)]
    require(matrix_product(phi, phi) == identity(5), "residual normalizer square")
    require(
        matrix_product(matrix_product(phi, p), phi) == q,
        "normalizer interchanges actual multiplication",
    )
    weights = [(a + 2 * b) % 3 for a, b in basis]
    counts = [weights.count(i) for i in range(3)]
    trace = [counts[0] - counts[2], counts[1] - counts[2]]
    return {
        "basis_p_q": [list(x) for x in basis],
        "multiplication_p": p,
        "multiplication_q": q,
        "residual_phi": phi,
        "residual_phi_square": matrix_product(phi, phi),
        "C3_weights": weights,
        "C3_trace_in_basis_1_omega": trace,
        "C3_characteristic_polynomial": poly_multiply(
            [1, -1], poly_multiply([1, 1, 1], [1, 1, 1])
        ),
        "phi_characteristic_polynomial": poly_multiply(
            [1, -1], poly_multiply([1, 0, -1], [1, 0, -1])
        ),
        "fibre_length": len(basis),
        "generic_field_degree": 3,
        "full_homogeneous_vertex_minimum": 33,
        "finite_flat_at_origin": False,
    }


def generators(value):
    require(type(value) is tuple and len(value) <= 6, "generator list cap")
    for row in value:
        require(
            type(row) is tuple and len(row) == 2, "generator degree/character tuple"
        )
        integer(row[0], 1, 8, "positive generator degree cap")
        integer(row[1], 0, 2, "generator character")
    return value


def exponent_tuples(total, size):
    if size == 0:
        if total == 0:
            yield ()
        return
    if size == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in exponent_tuples(total - first, size - 1):
            yield (first,) + tail


def positive_invariant_divisor(value, source):
    generators(source)
    monomial_exponents(value, length=len(source), cap=8)
    for divisor in product(*(range(x + 1) for x in value)):
        if (
            any(divisor)
            and sum(a * row[1] for a, row in zip(divisor, source, strict=True)) % 3 == 0
        ):
            return divisor
    return None


def literal_covariants(source, cutoff=4):
    generators(source)
    integer(cutoff, 2, 8, "polynomial length cutoff")
    result = {1: [], 2: []}
    for length in range(1, cutoff + 1):
        for value in exponent_tuples(length, len(source)):
            charge = sum(x * row[1] for x, row in zip(value, source, strict=True)) % 3
            if charge and positive_invariant_divisor(value, source) is None:
                result[charge].append(value)
    return result


def covariant_prediction(source):
    generators(source)
    result = {1: [], 2: []}
    for i, (_degree, charge) in enumerate(source):
        if charge:
            value = tuple(int(j == i) for j in range(len(source)))
            result[charge].append(value)
    for i, (_degree, charge) in enumerate(source):
        for j in range(i, len(source)):
            if charge and source[j][1] == charge:
                value = tuple(int(k == i) + int(k == j) for k in range(len(source)))
                result[2 * charge % 3].append(value)
    return {charge: sorted(values) for charge, values in result.items()}


def generator_series(source, charge):
    generators(source)
    integer(charge, 1, 2, "nontrivial character")
    result = [0] * 9
    for degree, weight in source:
        if weight == charge:
            result[degree] += 1
    return trim(result)


def minimal_from_covariant_series(first, second):
    return poly_add([1], poly_multiply([0, 0, 6, 0, 2], poly_add(first, second)))


def general_minimal_formula(source):
    h1, h2 = generator_series(source, 1), generator_series(source, 2)
    return minimal_from_covariant_series(
        poly_add(h1, sym_square_series(h2)), poly_add(h2, sym_square_series(h1))
    )


def synthetic_control(source, cutoff=4):
    literal = literal_covariants(source, cutoff)
    predicted = covariant_prediction(source)
    require(
        all(sorted(literal[charge]) == predicted[charge] for charge in (1, 2)),
        "literal covariant minimal quotient",
    )
    series = []
    for charge in (1, 2):
        value = [0] * 17
        for monomial in literal[charge]:
            degree = sum(a * row[0] for a, row in zip(monomial, source, strict=True))
            value[degree] += 1
        series.append(trim(value))
    minimum = minimal_from_covariant_series(*series)
    require(
        minimum == general_minimal_formula(source),
        "full minimal series from independent monomials",
    )
    linear = minimal_from_covariant_series(
        generator_series(source, 1), generator_series(source, 2)
    )
    return {
        "generators_degree_charge": [list(x) for x in source],
        "polynomial_length_cutoff": cutoff,
        "literal_Pbar1": [list(x) for x in literal[1]],
        "literal_Pbar2": [list(x) for x in literal[2]],
        "minimal_polynomial": minimum,
        "linear_only_lower_bound": linear,
        "linear_only_is_full": minimum == linear,
    }


def power_class(class_index, power):
    integer(class_index, 0, 2, "S3 class index")
    integer(power, 1, 16, "S3 power cap")
    if class_index == 1:
        return power % 2
    if class_index == 2:
        return 0 if power % 3 == 0 else 2
    return 0


def scaled_log_coefficient(class_index, degree):
    integer(class_index, 0, 2, "S3 class index")
    integer(degree, 1, 16, "source degree cap")
    if class_index == 0:
        return 4 + (-1) ** (degree + 1) * 2**degree
    if class_index == 1:
        return 4 if degree % 2 == 0 else 0
    return 3 if degree % 3 == 0 else 0


def source_lie_rows(cutoff=16):
    integer(cutoff, 1, 16, "source degree cap")
    rows = []
    for n in range(1, cutoff + 1):
        traces = []
        for class_index in range(3):
            old = sum(
                (-1) ** (d + 1)
                * d
                * rows[d - 1]["class_traces"][power_class(class_index, n // d)]
                for d in range(1, n)
                if n % d == 0
            )
            numerator = (-1) ** (n + 1) * (scaled_log_coefficient(class_index, n) - old)
            require(numerator % n == 0, "PBW integer character")
            traces.append(numerator // n)
        dim, s, c = traces
        require(
            (dim + 3 * s + 2 * c) % 6 == 0
            and (dim - 3 * s + 2 * c) % 6 == 0
            and (dim - c) % 3 == 0,
            "S3 multiplicity integrality",
        )
        multiplicities = [
            (dim + 3 * s + 2 * c) // 6,
            (dim - 3 * s + 2 * c) // 6,
            (dim - c) // 3,
        ]
        require(
            all(x >= 0 for x in multiplicities)
            and dim == multiplicities[0] + multiplicities[1] + 2 * multiplicities[2],
            "actual S3 representation dimensions",
        )
        rows.append(
            {"grade": n, "class_traces": traces, "multiplicities": multiplicities}
        )
    return rows


def compare_source_rows(rows, frozen):
    require(type(rows) is list and 1 <= len(rows) <= 16, "PBW source row cap")
    require(
        type(frozen) is dict and type(frozen.get("actual_Lie_cohomology_rows")) is list,
        "frozen actual Lie rows",
    )
    old = frozen["actual_Lie_cohomology_rows"]
    require(len(old) >= len(rows), "frozen source coverage")
    for n, row in enumerate(rows, start=1):
        expected = {
            key: old[n - 1][key] for key in ("grade", "class_traces", "multiplicities")
        }
        verify_payload(row, expected)
    return True


def actual_minimal_polynomial(rows, cutoff):
    integer(cutoff, 2, 16, "actual ladder cutoff")
    require(
        cutoff % 2 == 0 and type(rows) is list and len(rows) >= cutoff,
        "even covered ladder cutoff",
    )
    c = [0] * (cutoff + 1)
    for n in range(2, cutoff + 1, 2):
        row = rows[n - 1]
        require(
            type(row) is dict
            and type(row.get("multiplicities")) is list
            and len(row["multiplicities"]) == 3,
            "source multiplicity row",
        )
        c[n] = integer(
            row["multiplicities"][2], 0, 2**16, "source standard multiplicity"
        )
    covariants = poly_add(
        [2 * x for x in c], poly_multiply(c, c), square_substitution(c)
    )
    full = poly_add([1], poly_multiply([0, 0, 6, 0, 2], covariants))
    linear = poly_add([1], poly_multiply([0, 0, 6, 0, 2], [2 * x for x in c]))
    require(
        all(full[i] == 0 for i in range(1, len(full), 2)), "actual even source grading"
    )
    require(full != linear, "quadratic covariants cannot be omitted")
    return {
        "cutoff": cutoff,
        "C_polynomial": c,
        "full_minimal_polynomial": full,
        "linear_only_lower_bound": linear,
        "number_of_minimal_generators": sum(full),
        "generic_field_degree": 3,
        "expanded_Lie_generator_basis": False,
    }


def harmonic_calibration():
    rows = []
    for j in (2, 3, 7, 16):
        left = sum((Fraction(1, k * (j - k)) for k in range(1, j)), Fraction())
        right = 2 * sum((Fraction(1, k) for k in range(1, j)), Fraction()) / j
        require(left == right, "exact harmonic convolution identity")
        rows.append({"j": j, "sum": [left.numerator, left.denominator]})
    leading = (Fraction(6, 4) + Fraction(2, 16)) / 18
    return {
        "harmonic_identity_controls": rows,
        "leading_constant_even_half_grade": [leading.numerator, leading.denominator],
        "all_grade_asymptotic_from_proof": True,
        "asymptotic_fitted_from_samples": False,
        "uniform_O_remainder_claimed": False,
    }


def build():
    provenance, source_bytes = authenticate()
    # Every dependency is authenticated before any executable import or artifact parse.
    c6 = load_frozen_c6(source_bytes[PREFIX + "cyclic_infinity_replay.py"])
    frozen_lie = read_json(
        source_bytes[LIE_PREFIX + "global_lie_cohomology.verification.json"].decode(
            "utf-8"
        )
    )
    actual_covariants = []
    for charge in (1, 2):
        basis = c6.covariant_minimal(charge, cutoff=4)
        counts = [sum(value[0] == n for value in basis) for n in range(5)]
        require(counts == [0, 0, 6, 0, 2], "frozen actual A covariant polynomial")
        actual_covariants.append(
            {
                "character": charge,
                "monomials": [list(x) for x in basis],
                "polynomial": counts,
            }
        )
    c6_minimum = c6.combined_minimal(True, 8)
    literal_c6 = [
        sum(c6.combined_degree(value) == n for value in c6_minimum) for n in range(9)
    ]
    pair = synthetic_control(((2, 1), (2, 2)), 8)
    require(
        literal_c6 == pair["minimal_polynomial"] and sum(literal_c6) == 33,
        "new formula versus actual combined Segre monomials",
    )
    rows = source_lie_rows()
    compare_source_rows(rows, frozen_lie)
    synthetic = [pair] + [
        synthetic_control(source)
        for source in (
            ((1, 1), (3, 1)),
            ((1, 0), (2, 1), (2, 2), (3, 1), (4, 2)),
            ((1, 0), (2, 0), (4, 0)),
            ((3, 2),),
            ((2, 0), (1, 1), (1, 2), (3, 1), (3, 2), (4, 0)),
        )
    ]
    payload = {
        "schema": "riemann.extension_order.normalization.v1",
        "sources": provenance,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "fixed_locus": fixed_locus_control(),
        "scaled_source_chart": chart_control(),
        "actual_origin_fibre": fibre_control(),
        "actual_A_covariants": actual_covariants,
        "actual_C6_minimal_polynomial": literal_c6,
        "literal_polynomial_covariant_controls": synthetic,
        "independent_PBW_source_rows": rows,
        "all_sixteen_rows_match_frozen_source": True,
        "actual_ladder_minimal_polynomials": [
            actual_minimal_polynomial(rows, n) for n in (2, 4, 8, 12, 16)
        ],
        "held_out_ladder_cutoff": 16,
        "asymptotic_calibration": harmonic_calibration(),
        "scope": {
            "normalization_relative_to_prescribed_field_and_base": True,
            "arbitrary_Euler_source_uniqueness": False,
            "old_C_over_B_cokernel_is_a_Bprime_module": False,
            "all_degree_covariant_series_proved_not_extrapolated": True,
            "infinite_finiteness_iff_finitely_many_nontrivial_generator_directions": True,
            "infinite_algebra_CM_claimed": False,
            "new_arithmetic_field_counts": False,
            "analytic_frame_selected_by_normalization": False,
            "ordinary_Fredholm_domain_enlarged": False,
        },
    }
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    return payload


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
        print("wrote normalization and exact invariant-base controls")
    else:
        require(FIXTURE.stat().st_size <= MAX_FIXTURE_BYTES, "fixture byte cap")
        verify_payload(read_json(FIXTURE.read_text(encoding="utf-8")), result)
        print("normalization and exact invariant-base controls PASS")


if __name__ == "__main__":
    main()

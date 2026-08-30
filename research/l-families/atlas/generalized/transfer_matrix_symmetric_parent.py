"""Exact replay for the finite-rank symmetric-parent and determinant packet."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
from collections.abc import Iterable, Sequence
from fractions import Fraction
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
ATLAS_ROOT = PACKET_ROOT.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "transfer_matrix_symmetric_parent.json"
SOURCE_MANIFEST_PATH = PACKET_ROOT / "transfer_matrix_symmetric_parent.sources.json"
NOTE_PATH = PACKET_ROOT / "TRANSFER_MATRIX_SYMMETRIC_PARENT.md"
TEST_PATH = REPO_ROOT / "tests" / "test_transfer_matrix_symmetric_parent.py"

EXPECTED_SOURCE_MANIFEST_SHA256_LF = (
    "282f627f3288350d238c979ec99d33a46f87d10a99f2d8b9f06f293b4943d829"
)
EXPECTED_BASE_COMMIT = "cdaa8bcb863b0aa30044fc599efdf4ac549a5c38"
DEFAULT_MAX_DEGREE = 8
MAX_ALLOWED_DEGREE = 14
DEFAULT_MAX_RANK = 5
MAX_ALLOWED_RANK = 7
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 100_000


def _load_atlas_core():
    path = ATLAS_ROOT / "core" / "atlas_core.py"
    spec = importlib.util.spec_from_file_location("glo764_parent_atlas_core", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load atlas canonicalization core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ATLAS_CORE = _load_atlas_core()
Polynomial = tuple[Fraction, ...]
ExponentPair = tuple[int, int]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _canonical_sha256(value: object) -> str:
    return ATLAS_CORE.sha256_hex(value)


def _git_blob_at(commit: str, path: str) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", f"{commit}:{path}"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise RuntimeError("git object lookup could not be executed") from exc
    blob = result.stdout.strip()
    if (
        result.returncode != 0
        or len(blob) != 40
        or any(character not in "0123456789abcdef" for character in blob)
    ):
        raise RuntimeError(f"git object lookup failed: {commit}:{path}")
    return blob


def _validate_nonnegative_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def fraction_text(value: Fraction | int) -> str:
    rational = Fraction(value)
    if rational.denominator == 1:
        return str(rational.numerator)
    return f"{rational.numerator}/{rational.denominator}"


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        raise ValueError("polynomials must have at least one coefficient")
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            result[left_degree + right_degree] += left_coefficient * right_coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def denominator_from_weights(weights: Sequence[Fraction | int]) -> Polynomial:
    denominator: Polynomial = (Fraction(1),)
    for weight in weights:
        denominator = multiply_polynomials(
            denominator, (Fraction(1), -Fraction(weight))
        )
    return denominator


def convolution_at(
    denominator: Sequence[Fraction], sequence: Sequence[Fraction], index: int
) -> Fraction:
    _validate_nonnegative_integer(index, "index")
    return sum(
        denominator[degree] * sequence[index - degree]
        for degree in range(min(index, len(denominator) - 1) + 1)
    )


def symmetric_power_terms(
    power: int,
    *,
    alpha: Fraction,
    beta: Fraction,
    c_alpha: Fraction,
    c_beta: Fraction,
) -> tuple[tuple[Fraction, Fraction, ExponentPair], ...]:
    """Return (coefficient, weight, exponent pair) for a_r**power."""
    _validate_nonnegative_integer(power, "power")
    return tuple(
        (
            Fraction(math.comb(power, j)) * c_alpha ** (power - j) * c_beta**j,
            alpha ** (power - j) * beta**j,
            (power - j, j),
        )
        for j in range(power + 1)
    )


def scalar_sequence(
    length: int,
    *,
    alpha: Fraction,
    beta: Fraction,
    c_alpha: Fraction,
    c_beta: Fraction,
) -> tuple[Fraction, ...]:
    _validate_nonnegative_integer(length, "length")
    return tuple(
        c_alpha * alpha**index + c_beta * beta**index for index in range(length)
    )


def power_shadow_sequence(
    power: int,
    length: int,
    *,
    alpha: Fraction,
    beta: Fraction,
    c_alpha: Fraction,
    c_beta: Fraction,
) -> tuple[Fraction, ...]:
    return tuple(
        value**power
        for value in scalar_sequence(
            length,
            alpha=alpha,
            beta=beta,
            c_alpha=c_alpha,
            c_beta=c_beta,
        )
    )


def parent_matrix_coefficient_sequence(
    power: int,
    length: int,
    *,
    alpha: Fraction,
    beta: Fraction,
    c_alpha: Fraction,
    c_beta: Fraction,
) -> tuple[Fraction, ...]:
    terms = symmetric_power_terms(
        power,
        alpha=alpha,
        beta=beta,
        c_alpha=c_alpha,
        c_beta=c_beta,
    )
    return tuple(
        sum(coefficient * weight**index for coefficient, weight, _ in terms)
        for index in range(length)
    )


def exponent_triangle(maximum_degree: int) -> tuple[ExponentPair, ...]:
    _validate_nonnegative_integer(maximum_degree, "maximum_degree")
    return tuple(
        (left, degree - left)
        for degree in range(maximum_degree + 1)
        for left in range(degree + 1)
    )


def filtered_exponent_pairs(degrees: Iterable[int]) -> tuple[ExponentPair, ...]:
    normalized = []
    for degree in degrees:
        _validate_nonnegative_integer(degree, "degree")
        normalized.append(degree)
    return tuple(
        (left, degree - left)
        for degree in sorted(set(normalized))
        for left in range(degree + 1)
    )


def determinant_one_exponents(
    pairs: Iterable[ExponentPair],
) -> tuple[int, ...]:
    return tuple(sorted({left - right for left, right in pairs}))


def numerical_weights(
    pairs: Iterable[ExponentPair], *, alpha: Fraction, beta: Fraction
) -> tuple[Fraction, ...]:
    return tuple(alpha**left * beta**right for left, right in pairs)


def filtered_parent_dimension(degrees: Iterable[int]) -> int:
    normalized = []
    for degree in degrees:
        _validate_nonnegative_integer(degree, "degree")
        normalized.append(degree)
    return sum(degree + 1 for degree in set(normalized))


def exponent_simplex(rank: int, maximum_degree: int) -> tuple[tuple[int, ...], ...]:
    """Return nonnegative rank-tuples with coordinate sum at most maximum_degree."""
    _validate_nonnegative_integer(rank, "rank")
    _validate_nonnegative_integer(maximum_degree, "maximum_degree")
    if rank == 0:
        raise ValueError("rank must be positive")

    def rows(dimensions: int, remaining: int) -> Iterable[tuple[int, ...]]:
        if dimensions == 1:
            for value in range(remaining + 1):
                yield (value,)
            return
        for value in range(remaining + 1):
            for tail in rows(dimensions - 1, remaining - value):
                yield (value,) + tail

    return tuple(rows(rank, maximum_degree))


def determinant_one_canonical_exponent(exponent: Sequence[int]) -> tuple[int, ...]:
    if not exponent:
        raise ValueError("exponent vector must be nonempty")
    values = []
    for coordinate in exponent:
        _validate_nonnegative_integer(coordinate, "exponent coordinate")
        values.append(coordinate)
    minimum = min(values)
    return tuple(coordinate - minimum for coordinate in values)


def determinant_one_character_classes(
    rank: int, maximum_degree: int
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            {
                determinant_one_canonical_exponent(exponent)
                for exponent in exponent_simplex(rank, maximum_degree)
            }
        )
    )


def verify_sources_manifest() -> dict[str, object]:
    if _lf_sha256(SOURCE_MANIFEST_PATH) != EXPECTED_SOURCE_MANIFEST_SHA256_LF:
        raise RuntimeError("sources manifest hash mismatch")
    manifest = json.loads(SOURCE_MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("sources manifest base commit mismatch")
    if manifest.get("schema") != (
        "riemann.atlas.generalized.transfer_matrix_symmetric_parent.sources.v1"
    ):
        raise RuntimeError("sources manifest schema mismatch")
    verified: list[dict[str, object]] = []
    for source_record in manifest["sources"]:
        path = REPO_ROOT / source_record["path"]
        actual_hash = _lf_sha256(path)
        if actual_hash != source_record["file_sha256_lf_normalized"]:
            raise RuntimeError(f"source hash mismatch: {source_record['path']}")
        actual_blob = _git_blob_at(manifest["base_commit"], source_record["path"])
        if actual_blob != source_record["git_blob"]:
            raise RuntimeError(f"source git blob mismatch: {source_record['path']}")
        row: dict[str, object] = {
            "path": source_record["path"],
            "role": source_record["role"],
            "file_sha256_lf_normalized": actual_hash,
            "git_blob": actual_blob,
        }
        if "payload_sha256" in source_record:
            source = json.loads(path.read_text(encoding="utf-8"))
            if source.get("schema") != source_record["schema"]:
                raise RuntimeError(f"source schema mismatch: {source_record['path']}")
            unhashed = dict(source)
            claimed_payload = unhashed.pop("payload_sha256", None)
            actual_payload = _canonical_sha256(unhashed)
            if (
                claimed_payload != source_record["payload_sha256"]
                or actual_payload != claimed_payload
            ):
                raise RuntimeError(f"source payload mismatch: {source_record['path']}")
            row["schema"] = source["schema"]
            row["payload_sha256"] = actual_payload
        verified.append(row)
    return {
        "path": _relative(SOURCE_MANIFEST_PATH),
        "file_sha256_lf_normalized": EXPECTED_SOURCE_MANIFEST_SHA256_LF,
        "base_commit": manifest["base_commit"],
        "verified_sources": verified,
        "scope_firewall": manifest["scope_firewall"],
    }


def _power_row(power: int) -> dict[str, object]:
    alpha = Fraction(3)
    beta = Fraction(2)
    c_alpha = Fraction(3)
    c_beta = Fraction(-2)
    terms = symmetric_power_terms(
        power,
        alpha=alpha,
        beta=beta,
        c_alpha=c_alpha,
        c_beta=c_beta,
    )
    length = 3 * (power + 1) + 5
    shadow = power_shadow_sequence(
        power,
        length,
        alpha=alpha,
        beta=beta,
        c_alpha=c_alpha,
        c_beta=c_beta,
    )
    parent = parent_matrix_coefficient_sequence(
        power,
        length,
        alpha=alpha,
        beta=beta,
        c_alpha=c_alpha,
        c_beta=c_beta,
    )
    if shadow != parent:
        raise ArithmeticError("symmetric-parent matrix coefficient identity failed")
    weights = tuple(term[1] for term in terms)
    denominator = denominator_from_weights(weights)
    for index in range(len(denominator) - 1, length):
        if convolution_at(denominator, shadow, index):
            raise ArithmeticError("power-shadow denominator failed to annihilate")
    if len(set(weights)) != power + 1 or any(not term[0] for term in terms):
        raise ArithmeticError("minimal-denominator witness degenerated")
    return {
        "k": power,
        "parent": f"Sym^{power}(A)",
        "parent_dimension": power + 1,
        "terms": [
            {
                "exponent_pair": list(pair),
                "coefficient": fraction_text(coefficient),
                "weight": fraction_text(weight),
            }
            for coefficient, weight, pair in terms
        ],
        "shadow_equals_parent_matrix_coefficient_through_index": length - 1,
        "minimal_denominator_coefficients_ascending": [
            fraction_text(value) for value in denominator
        ],
        "minimal_denominator_degree": len(denominator) - 1,
        "tail_annihilation_checked_through_index": length - 1,
    }


def _zero_eigenvalue_row() -> dict[str, object]:
    terms = symmetric_power_terms(
        1,
        alpha=Fraction(0),
        beta=Fraction(1),
        c_alpha=Fraction(1),
        c_beta=Fraction(1),
    )
    weights = tuple(term[1] for term in terms)
    sequence = power_shadow_sequence(
        1,
        6,
        alpha=Fraction(0),
        beta=Fraction(1),
        c_alpha=Fraction(1),
        c_beta=Fraction(1),
    )
    denominator = denominator_from_weights(weights)
    numerator = tuple(
        convolution_at(denominator, sequence, index)
        for index in range(len(sequence))
    )
    if weights != (Fraction(0), Fraction(1)) or len(set(weights)) != 2:
        raise ArithmeticError("zero-eigenvalue weights are not the hostile witness")
    if sequence != (
        Fraction(2),
        Fraction(1),
        Fraction(1),
        Fraction(1),
        Fraction(1),
        Fraction(1),
    ):
        raise ArithmeticError("zero-eigenvalue transient sequence changed")
    if denominator != (Fraction(1), Fraction(-1)):
        raise ArithmeticError("zero-eigenvalue denominator did not lose a factor")
    if numerator[:2] != (Fraction(2), Fraction(-1)) or any(numerator[2:]):
        raise ArithmeticError("zero-eigenvalue reduced numerator is incorrect")
    return {
        "k": 1,
        "eigenvalues": ["0", "1"],
        "eigen_coordinates": ["1", "1"],
        "weights": [fraction_text(weight) for weight in weights],
        "weights_pairwise_distinct": True,
        "all_weights_nonzero": False,
        "sequence_prefix": [fraction_text(value) for value in sequence],
        "generating_function": "(2-T)/(1-T)",
        "reduced_denominator_coefficients_ascending": [
            fraction_text(value) for value in denominator
        ],
        "reduced_denominator_degree": len(denominator) - 1,
        "excluded_k_plus_1_conclusion": 2,
        "tail_annihilation_starts_at_index": 2,
    }


def _spectrum_row(maximum_degree: int) -> dict[str, object]:
    pairs = exponent_triangle(maximum_degree)
    generic_weights = numerical_weights(pairs, alpha=Fraction(2), beta=Fraction(3))
    determinant_one_weights = numerical_weights(
        pairs, alpha=Fraction(2), beta=Fraction(1, 2)
    )
    dependent_weights = numerical_weights(pairs, alpha=Fraction(2), beta=Fraction(4))
    determinant_projection = determinant_one_exponents(pairs)
    triangular = (maximum_degree + 1) * (maximum_degree + 2) // 2
    if len(pairs) != triangular or len(set(generic_weights)) != triangular:
        raise ArithmeticError("generic exponent triangle count failed")
    if len(determinant_projection) != 2 * maximum_degree + 1:
        raise ArithmeticError("determinant-one quotient count failed")
    if len(set(determinant_one_weights)) != len(determinant_projection):
        raise ArithmeticError("determinant-one numerical witness degenerated")
    return {
        "d": maximum_degree,
        "filtered_parent_dimension": filtered_parent_dimension(
            range(maximum_degree + 1)
        ),
        "generic_two_torus": {
            "witness": {"alpha": "2", "beta": "3"},
            "exponent_pair_count": len(pairs),
            "distinct_weight_count": len(set(generic_weights)),
            "predicted_triangular_count": triangular,
        },
        "determinant_one": {
            "witness": {"alpha": "2", "beta": "1/2"},
            "projected_exponents": list(determinant_projection),
            "distinct_weight_count": len(set(determinant_one_weights)),
            "predicted_linear_count": 2 * maximum_degree + 1,
        },
        "multiplicatively_dependent_counterfeit": {
            "witness": {"alpha": "2", "beta": "4"},
            "distinct_weight_count": len(set(dependent_weights)),
            "strictly_below_generic_count": (
                len(set(dependent_weights)) < triangular
                if maximum_degree >= 2
                else None
            ),
        },
    }


def _higher_rank_row(rank: int, maximum_degree: int) -> dict[str, object]:
    exponents = exponent_simplex(rank, maximum_degree)
    classes = determinant_one_character_classes(rank, maximum_degree)
    generic_count = math.comb(rank + maximum_degree, rank)
    positive_count = math.comb(maximum_degree, rank) if maximum_degree >= rank else 0
    quotient_count = generic_count - positive_count
    if len(exponents) != generic_count:
        raise ArithmeticError("higher-rank exponent-simplex count failed")
    if len(classes) != quotient_count:
        raise ArithmeticError("higher-rank determinant quotient count failed")
    if any(min(character) != 0 for character in classes):
        raise ArithmeticError("determinant quotient representative is not canonical")
    return {
        "rank": rank,
        "d": maximum_degree,
        "generic_character_count": generic_count,
        "all_positive_exponent_count": positive_count,
        "determinant_one_character_count": len(classes),
        "formula": "binomial(n+d,n)-binomial(d,n)",
        "canonical_representatives_have_minimum_zero": True,
        "sample_canonical_representatives": [
            list(character) for character in classes[: min(12, len(classes))]
        ],
    }


def _survival_ladder() -> dict[str, object]:
    levels = {
        "L0": "well-defined and branch-independent",
        "L1": "coefficient or local multiplicativity",
        "L2": "formal Euler product",
        "L3": "uniform bounded-degree rational local factors",
        "L4": "weight, determinant, duality, and ramified-prime coherence",
        "L5": "canonical conductor, gamma factors, and root number",
        "L6": "analytic continuation and functional equation",
        "L7": "twist, tensor, induction, and contragredient compatibility",
        "L8": "automorphic, motivic, spectral, dynamical, or categorical realization",
        "L9": "principled explicit formula, positivity, or zero theory",
    }
    rows = [
        {
            "object": "integer monomial shadow a_r^k with parent Sym^k(A)",
            "statuses": {
                "L0": "PROVED_PASS",
                "L1": "CONDITIONAL_ON_PRIMEWISE_MULTIPLICATIVE_INPUT",
                "L2": "FORMAL_IF_L1_INPUT_IS_SUPPLIED",
                "L3": "PROVED_PASS_LOCAL_DEGREE_AT_MOST_K_PLUS_1",
                "L4": "OPEN_GLOBAL_COHERENCE_PROBLEM",
                "L5": "NOT_ESTABLISHED",
                "L6": "NOT_ESTABLISHED",
                "L7": "LOCAL_SYMMETRIC_TENSOR_FUNCTORIALITY_ONLY",
                "L8": "HONEST_LOCAL_LINEAR_PARENT_ONLY",
                "L9": "NOT_ESTABLISHED",
            },
            "first_unresolved_level": "L4",
        },
        {
            "object": "polynomial scalar transform Phi(a_r)",
            "statuses": {
                "L0": "PROVED_PASS",
                "L1": "PROVED_FAIL_UNIVERSALLY_EXCEPT_NORMALIZED_MONOMIALS_IN_SOURCE_PACKET",
                "L2": "NOT_ESTABLISHED_IN_GENERAL",
                "L3": "PROVED_PASS_VIA_DIRECT_SUM_OF_SYMMETRIC_PARENTS",
                "L4": "NOT_ESTABLISHED",
                "L5": "NOT_ESTABLISHED",
                "L6": "NOT_ESTABLISHED",
                "L7": "DIRECT_SUM_PARENT_IS_FUNCTORIAL_LOCALLY",
                "L8": "HONEST_LOCAL_PARENT_BUT_NOT_A_GLOBAL_REALIZATION",
                "L9": "NOT_ESTABLISHED",
            },
            "first_failure_level": "L1",
        },
    ]
    return {"levels": levels, "rows": rows}


def build_fixture(
    *,
    max_degree: int = DEFAULT_MAX_DEGREE,
    max_rank: int = DEFAULT_MAX_RANK,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _validate_nonnegative_integer(max_degree, "max_degree")
    if max_degree < 4:
        raise ValueError("max_degree must include calibration degrees through four")
    if max_degree > MAX_ALLOWED_DEGREE:
        raise ValueError(f"max_degree must not exceed {MAX_ALLOWED_DEGREE}")
    _validate_nonnegative_integer(max_rank, "max_rank")
    if max_rank < 2:
        raise ValueError("max_rank must include rank two")
    if max_rank > MAX_ALLOWED_RANK:
        raise ValueError(f"max_rank must not exceed {MAX_ALLOWED_RANK}")
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")
    work_units = sum((degree + 1) ** 3 for degree in range(max_degree + 1)) + sum(
        math.comb(rank + degree, rank)
        for rank in range(2, max_rank + 1)
        for degree in range(max_degree + 1)
    )
    if work_units >= resource_cap:
        raise RuntimeError("declared exact replay would meet or exceed exclusive cap")

    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.transfer_matrix_symmetric_parent.v1",
        "status": "PROPOSED_EXACT_LOCAL_PARENT_THEOREM_EXTERNAL_NOVELTY_UNREVIEWED",
        "programme_issue": 764,
        "claims": {
            "GLO764.TENSOR_PARENT_IDENTITY": {
                "status": "PROVED_IN_NOTE_AND_EXACTLY_REPLAYED",
                "statement": "(ell(A^r v))^k is the corresponding matrix coefficient of (Sym^k A)^r",
                "scope": "arbitrary finite-rank characteristic-zero linear algebra and integer k>=0",
            },
            "GLO764.GENERIC_POWER_MINIMAL_DENOMINATOR": {
                "status": "PROVED_IN_NOTE_AND_EXACTLY_REPLAYED",
                "statement": "with nonzero eigenvalues and eigen-coordinates and k+1 distinct symmetric weights, the reduced denominator has degree k+1",
            },
            "GLO764.DETERMINANT_ONE_SPECTRAL_COMPRESSION": {
                "status": "PROVED_IN_NOTE_AND_EXACTLY_REPLAYED",
                "statement": "the full filtered rank-two spectrum through d drops from binomial(d+2,2) generically to 2d+1 on det=1",
            },
            "GLO764.HIGHER_RANK_DETERMINANT_QUOTIENT": {
                "status": "PROVED_IN_NOTE_AND_EXACTLY_REPLAYED",
                "statement": "the full filtered rank-n spectrum through d drops from binomial(n+d,n) to binomial(n+d,n)-binomial(d,n) on the generic determinant-one torus",
                "mechanism": "quotient the exponent simplex by the all-ones character and choose the unique representative with minimum coordinate zero",
            },
            "GLO764.FINITE_PARENT_INTERPOLATION_OBSTRUCTION": {
                "status": "PROVED_FROM_AUTHENTICATED_SOURCE_THEOREM_AND_FINITE_RESOLVENT_IDENTITY",
                "scope": "positive-real branch for the fixed hyperbolic recurrence x>2",
                "statement": "u_r(x)^lambda is an exact finite-dimensional matrix coefficient iff lambda is a nonnegative integer",
                "open_beyond_scope": "infinite-dimensional, nuclear, regularized, categorical, and complex-rank parents",
            },
        },
        "sources_manifest": verify_sources_manifest(),
        "nonunit_determinant_power_parent": {
            "base_sequence": {
                "formula": "a_r=3*3^r-2*2^r",
                "initial_values": [1, 5],
                "recurrence": "a_(r+2)=5*a_(r+1)-6*a_r",
                "eigenvalues": ["3", "2"],
                "determinant": "6",
            },
            "rows": [_power_row(power) for power in range(max_degree + 1)],
        },
        "filtered_parent_spectrum": {
            "degrees": list(range(max_degree + 1)),
            "rows": [_spectrum_row(degree) for degree in range(max_degree + 1)],
            "load_bearing_parameter": "delta=alpha*beta; setting delta=1 forgets one exponent coordinate",
            "held_out_prediction": "freeing determinant generically restores triangular rather than linear spectral growth across degrees",
        },
        "higher_rank_determinant_quotient": {
            "maximum_rank": max_rank,
            "maximum_degree": max_degree,
            "rows": [
                _higher_rank_row(rank, degree)
                for rank in range(2, max_rank + 1)
                for degree in range(max_degree + 1)
            ],
            "generic_formula": "binomial(n+d,n)",
            "determinant_one_formula": "binomial(n+d,n)-binomial(d,n)",
            "asymptotic_for_fixed_n_at_least_2": "n/(n-1)! * d^(n-1) + O_n(d^(n-2))",
            "further_frontier": "quotient exponent polytopes by higher-rank monomial-relation lattices",
        },
        "finite_parent_interpolation_obstruction": {
            "source_classification": "sum_r u_r(x)^lambda*T^r is rational iff lambda is a nonnegative integer",
            "finite_matrix_coefficient_implication": "phi((I-T*B)^(-1)w) is rational",
            "integer_parent": "u_r=ell(A^r v), hence u_r^k is a matrix coefficient of Sym^k(A)",
            "classification": "finite-dimensional exact matrix-coefficient parent iff lambda is a nonnegative integer",
            "not_excluded": [
                "infinite-dimensional or nuclear operators",
                "regularized determinants",
                "Deligne or other complex-rank tensor categories",
                "categorical traces",
                "approximate or weakened shadows",
            ],
        },
        "hostile_controls": {
            "zero_eigen_coordinate": "removes some symmetric weights and invalidates minimality, but not the parent identity",
            "zero_eigenvalue_transient": _zero_eigenvalue_row(),
            "root_of_unity_ratio": "collides weights within a fixed symmetric power",
            "multiplicatively_dependent_roots": "collide weights across different polynomial degrees",
            "special_polynomial_coefficients": "can cancel scalar-shadow poles even when the direct-sum parent retains them",
            "resolvent_matrix_coefficient_is_not_determinant_inverse": True,
            "parent_does_not_identify_coefficient_power_with_symmetric_power_l_factor": True,
            "fitted_scalar_realization_is_not_the_parent": True,
        },
        "survival_ladder": _survival_ladder(),
        "literature_firewall": {
            "integer_power_recurrence_generating_functions_are_classical": True,
            "references": [
                {
                    "authors": "Pantelimon Stanica",
                    "title": "Generating Functions, Weighted and Non-Weighted Sums for Powers of Second-Order Recurrence Sequences",
                    "url": "https://arxiv.org/abs/math/0010149",
                    "boundary": "closed generating functions for integer powers of second-order recurrences",
                },
                {
                    "authors": "Pavel Etingof",
                    "title": "Representation theory in complex rank, I",
                    "url": "https://arxiv.org/abs/1401.6321",
                    "boundary": "established interpolating tensor categories; not excluded by a finite-dimensional vector-space obstruction",
                },
            ],
            "tensor_parent_is_standard_representation_theory": True,
            "external_specialist_novelty_review_required": True,
        },
        "scope_firewall": {
            "local_finite_rank_linear_algebra_only": True,
            "integer_symmetric_powers_only": True,
            "matrix_coefficient_shadow_is_not_promoted_to_a_determinant_l_factor": True,
            "does_not_construct_a_global_Euler_product": True,
            "does_not_supply_ramified_factors_completion_or_functional_equation": True,
            "does_not_prove_automorphy_motivic_origin_or_a_zero_theorem": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": "integer exponent lattices, rational binomial expansions, exact polynomial products, and recurrence convolutions",
            "maximum_degree": max_degree,
            "maximum_allowed_degree": MAX_ALLOWED_DEGREE,
            "maximum_rank": max_rank,
            "maximum_allowed_rank": MAX_ALLOWED_RANK,
            "declared_work_units": work_units,
            "work_unit_cap_exclusive": resource_cap,
            "float_operations": 0,
            "random_samples": 0,
            "external_symbolic_engine": False,
            "prime_curve_field_zero_or_conductor_enumerations": 0,
        },
        "producer": {
            "script": _relative(SCRIPT_PATH),
            "script_sha256_lf_normalized": _lf_sha256(SCRIPT_PATH),
            "note": _relative(NOTE_PATH),
            "note_sha256_lf_normalized": _lf_sha256(NOTE_PATH),
            "test": _relative(TEST_PATH),
            "test_sha256_lf_normalized": _lf_sha256(TEST_PATH),
        },
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def _serialized_fixture() -> str:
    return json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the stored JSON equals a fresh exact build",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if (
            not OUTPUT_PATH.exists()
            or OUTPUT_PATH.read_text(encoding="utf-8") != serialized
        ):
            raise SystemExit("stored symmetric-parent fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

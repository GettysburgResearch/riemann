"""Exact replay for the nonintegral local-power rationality obstruction.

The analytic nonrationality proof is resident in the companion note.  This
dependency-free producer authenticates its inherited normalization and
recomputes the finite Laurent-polynomial, numerator, recurrence, Hankel, and
survival-ledger certificates used by that proof packet.
"""

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
OUTPUT_PATH = PACKET_ROOT / "nonintegral_local_power_rationality.json"
SOURCE_MANIFEST_PATH = PACKET_ROOT / "nonintegral_local_power_rationality.sources.json"
NOTE_PATH = PACKET_ROOT / "NONINTEGRAL_LOCAL_POWER_RATIONALITY.md"
TEST_PATH = REPO_ROOT / "tests" / "test_nonintegral_local_power_rationality.py"

EXPECTED_SOURCE_MANIFEST_SHA256_LF = (
    "99df382aaf78cec91f474f6a10cdce6a41370f9a2ad3c68645bb2cd571ceca6b"
)
EXPECTED_BASE_COMMIT = "10446e8ea9c55162c317810f63c1f7a379466459"
MAX_ALLOWED_K = 12
DEFAULT_MAX_K = 8
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 50_000


def _load_atlas_core():
    path = ATLAS_ROOT / "core" / "atlas_core.py"
    spec = importlib.util.spec_from_file_location("glo764_atlas_core", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load atlas canonicalization core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ATLAS_CORE = _load_atlas_core()


Laurent = dict[int, int]
XPolynomial = tuple[int, ...]


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


def _clean_laurent(value: Laurent) -> Laurent:
    return {
        exponent: coefficient for exponent, coefficient in value.items() if coefficient
    }


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return _clean_laurent(result)


def laurent_scale(value: Laurent, scalar: int) -> Laurent:
    return _clean_laurent(
        {exponent: scalar * coefficient for exponent, coefficient in value.items()}
    )


def laurent_shift(value: Laurent, shift: int) -> Laurent:
    return {exponent + shift: coefficient for exponent, coefficient in value.items()}


def laurent_multiply(left: Laurent, right: Laurent) -> Laurent:
    result: Laurent = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    return _clean_laurent(result)


def laurent_power(value: Laurent, exponent: int) -> Laurent:
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("Laurent exponent must be an integer")
    if exponent < 0:
        raise ValueError("Laurent exponent must be nonnegative")
    result: Laurent = {0: 1}
    factor = value
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = laurent_multiply(result, factor)
        remaining //= 2
        if remaining:
            factor = laurent_multiply(factor, factor)
    return result


def hecke_laurent(index: int) -> Laurent:
    """Return u_index(a+a^-1)=sum_{j=0}^index a^(index-2j)."""
    if isinstance(index, bool) or not isinstance(index, int):
        raise TypeError("Hecke index must be an integer")
    if index < 0:
        raise ValueError("Hecke index must be nonnegative")
    return {index - 2 * j: 1 for j in range(index + 1)}


def denominator_laurent(power: int) -> list[Laurent]:
    """Coefficients in T of prod_j (1-a^(power-2j) T)."""
    _validate_power(power)
    coefficients: list[Laurent] = [{0: 1}]
    for weight in range(power, -power - 1, -2):
        updated: list[Laurent] = [{} for _ in range(len(coefficients) + 1)]
        for degree, coefficient in enumerate(coefficients):
            updated[degree] = laurent_add(updated[degree], coefficient)
            updated[degree + 1] = laurent_add(
                updated[degree + 1],
                laurent_scale(laurent_shift(coefficient, weight), -1),
            )
        coefficients = updated
    return coefficients


def numerator_laurent(power: int) -> list[Laurent]:
    """Reduced numerator obtained exactly from D(T) sum_r u_r^power T^r."""
    _validate_power(power)
    denominator = denominator_laurent(power)
    scan_limit = 3 * (power + 1)
    coefficients: list[Laurent] = []
    for index in range(scan_limit + 1):
        coefficient: Laurent = {}
        for degree in range(min(index, len(denominator) - 1) + 1):
            sequence_term = laurent_power(hecke_laurent(index - degree), power)
            coefficient = laurent_add(
                coefficient,
                laurent_multiply(denominator[degree], sequence_term),
            )
        coefficients.append(coefficient)
    for index in range(power + 1, len(coefficients)):
        if coefficients[index]:
            raise ArithmeticError(
                f"denominator failed to annihilate power {power} at index {index}"
            )
    numerator = coefficients[: power + 1]
    while len(numerator) > 1 and not numerator[-1]:
        numerator.pop()
    return numerator


def _xpoly_clean(coefficients: Iterable[int]) -> XPolynomial:
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result or [0])


def xpoly_add(left: XPolynomial, right: XPolynomial) -> XPolynomial:
    length = max(len(left), len(right))
    result = [0] * length
    for index in range(length):
        result[index] = (left[index] if index < len(left) else 0) + (
            right[index] if index < len(right) else 0
        )
    return _xpoly_clean(result)


def xpoly_scale(value: XPolynomial, scalar: int) -> XPolynomial:
    return _xpoly_clean(scalar * coefficient for coefficient in value)


def xpoly_shift(value: XPolynomial) -> XPolynomial:
    return (0,) + value


def dickson_polynomials(maximum: int) -> list[XPolynomial]:
    if maximum < 0:
        raise ValueError("Dickson maximum must be nonnegative")
    values: list[XPolynomial] = [(2,)]
    if maximum == 0:
        return values
    values.append((0, 1))
    for _ in range(2, maximum + 1):
        values.append(xpoly_add(xpoly_shift(values[-1]), xpoly_scale(values[-2], -1)))
    return values


def symmetric_laurent_to_x(value: Laurent) -> XPolynomial:
    """Convert an inversion-invariant Laurent polynomial using a^n+a^-n=D_n(x)."""
    if not value:
        return (0,)
    maximum = max(abs(exponent) for exponent in value)
    for exponent in range(1, maximum + 1):
        if value.get(exponent, 0) != value.get(-exponent, 0):
            raise ArithmeticError("Laurent polynomial is not inversion invariant")
    dickson = dickson_polynomials(maximum)
    result: XPolynomial = (value.get(0, 0),)
    for exponent in range(1, maximum + 1):
        coefficient = value.get(exponent, 0)
        if coefficient:
            result = xpoly_add(result, xpoly_scale(dickson[exponent], coefficient))
    return _xpoly_clean(result)


def denominator_in_x(power: int) -> list[XPolynomial]:
    return [symmetric_laurent_to_x(value) for value in denominator_laurent(power)]


def numerator_in_x(power: int) -> list[XPolynomial]:
    return [symmetric_laurent_to_x(value) for value in numerator_laurent(power)]


def xpoly_text(value: XPolynomial) -> str:
    pieces: list[str] = []
    for degree in range(len(value) - 1, -1, -1):
        coefficient = value[degree]
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else "+"
        magnitude = abs(coefficient)
        if degree == 0:
            atom = str(magnitude)
        elif degree == 1:
            atom = "x" if magnitude == 1 else f"{magnitude}*x"
        else:
            atom = f"x^{degree}" if magnitude == 1 else f"{magnitude}*x^{degree}"
        if not pieces:
            pieces.append(atom if coefficient > 0 else f"-{atom}")
        else:
            pieces.append(f"{sign}{atom}")
    return "".join(pieces) if pieces else "0"


def polynomial_in_t_record(coefficients: list[XPolynomial]) -> dict[str, object]:
    return {
        "coefficient_order": "ascending powers of T; each x coefficient also ascending",
        "x_coefficient_vectors": [list(value) for value in coefficients],
        "x_coefficient_text": [xpoly_text(value) for value in coefficients],
    }


def generalized_binomial(value: Fraction, index: int) -> Fraction:
    if index < 0:
        raise ValueError("binomial index must be nonnegative")
    result = Fraction(1)
    for offset in range(index):
        result *= value - offset
        result /= offset + 1
    return result


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def rational_power_hostile_control(
    value: Fraction, terms: int = 10
) -> dict[str, object]:
    coefficients = [generalized_binomial(value, index) for index in range(terms)]
    pole_exponents = [Fraction(2 * index) - value for index in range(terms)]
    return {
        "lambda": fraction_text(value),
        "binomial_coefficients": [
            fraction_text(coefficient) for coefficient in coefficients
        ],
        "all_displayed_coefficients_nonzero": all(coefficients),
        "pole_exponents_2j_minus_lambda": [
            fraction_text(item) for item in pole_exponents
        ],
        "displayed_poles_pairwise_distinct": len(set(pole_exponents)) == terms,
        "finite_prefix_is_not_the_nonrationality_proof": True,
    }


def hecke_integer(trace: int, index: int) -> int:
    if index < 0:
        raise ValueError("Hecke index must be nonnegative")
    previous, current = 1, trace
    if index == 0:
        return previous
    for _ in range(1, index):
        previous, current = current, trace * current - previous
    return current


def determinant_fraction(matrix: list[list[Fraction]]) -> Fraction:
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("determinant input must be a nonempty square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    determinant = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]), None
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        determinant *= pivot_value
        for entry in range(column, len(work)):
            work[column][entry] /= pivot_value
        for row in range(column + 1, len(work)):
            multiplier = work[row][column]
            if multiplier:
                for entry in range(column, len(work)):
                    work[row][entry] -= multiplier * work[column][entry]
    return sign * determinant


def reciprocal_hankel_control(trace: int, maximum_size: int) -> dict[str, object]:
    sequence = [
        Fraction(1, hecke_integer(trace, index)) for index in range(2 * maximum_size)
    ]
    determinants: list[Fraction] = []
    for size in range(1, maximum_size + 1):
        matrix = [
            [sequence[row + column] for column in range(size)] for row in range(size)
        ]
        determinants.append(determinant_fraction(matrix))
    return {
        "trace": trace,
        "lambda": "-1",
        "sizes": list(range(1, maximum_size + 1)),
        "determinants": [fraction_text(value) for value in determinants],
        "all_displayed_nonzero": all(determinants),
        "finite_hankel_prefix_is_not_an_infinite_rank_proof": True,
    }


def polynomial_root_exponents(nonzero_degrees: Iterable[int]) -> tuple[int, ...]:
    degrees = tuple(sorted(set(nonzero_degrees)))
    if any(
        isinstance(degree, bool) or not isinstance(degree, int) for degree in degrees
    ):
        raise TypeError("polynomial degrees must be integers")
    if any(degree < 0 for degree in degrees):
        raise ValueError("polynomial degrees must be nonnegative")
    return tuple(
        sorted(
            {degree - 2 * index for degree in degrees for index in range(degree + 1)}
        )
    )


def multiplicativity_identity(coefficients: Sequence[Fraction | int]) -> bool:
    normalized = [Fraction(value) for value in coefficients]
    left: dict[tuple[int, int], Fraction] = {}
    right: dict[tuple[int, int], Fraction] = {}
    for degree, coefficient in enumerate(normalized):
        if coefficient:
            left[(degree, degree)] = coefficient
    for left_degree, left_coefficient in enumerate(normalized):
        for right_degree, right_coefficient in enumerate(normalized):
            coefficient = left_coefficient * right_coefficient
            if coefficient:
                right[(left_degree, right_degree)] = coefficient
    return left == right


def normalized_multiplicative_monomial(
    coefficients: Sequence[Fraction | int],
) -> int | None:
    normalized = [Fraction(value) for value in coefficients]
    if (
        not normalized
        or sum(normalized) != 1
        or not multiplicativity_identity(normalized)
    ):
        return None
    support = [index for index, coefficient in enumerate(normalized) if coefficient]
    if len(support) != 1 or normalized[support[0]] != 1:
        raise ArithmeticError(
            "formal coefficient comparison returned an impossible support"
        )
    return support[0]


def _validate_power(power: int) -> None:
    if isinstance(power, bool) or not isinstance(power, int):
        raise TypeError("power must be an integer")
    if power < 0:
        raise ValueError("power must be nonnegative")


def verify_sources_manifest() -> dict[str, object]:
    if _lf_sha256(SOURCE_MANIFEST_PATH) != EXPECTED_SOURCE_MANIFEST_SHA256_LF:
        raise RuntimeError("sources manifest hash mismatch")
    manifest = json.loads(SOURCE_MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("sources manifest base commit mismatch")
    if manifest.get("schema") != (
        "riemann.atlas.generalized.nonintegral_local_power.sources.v1"
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


def _integer_row(power: int) -> dict[str, object]:
    weights = tuple(range(power, -power - 1, -2))
    denominator = denominator_in_x(power)
    numerator = numerator_in_x(power)
    return {
        "k": power,
        "characteristic_weight_exponents": list(weights),
        "weights_pairwise_distinct": len(set(weights)) == power + 1,
        "partial_fraction_coefficients_without_common_factor": [
            {
                "j": index,
                "signed_binomial": ((-1) ** index) * math.comb(power, index),
                "q_exponent": index,
                "nonzero": True,
            }
            for index in range(power + 1)
        ],
        "denominator": polynomial_in_t_record(denominator),
        "numerator": polynomial_in_t_record(numerator),
        "minimal_denominator_degree_for_x_gt_2": power + 1,
        "tail_annihilation_checked_through_index": 3 * (power + 1),
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
            "object": "integer coefficient monomial z^k",
            "statuses": {
                "L0": "PROVED_PASS",
                "L1": "PROVED_PASS_FOR_MULTIPLICATIVE_INPUT_COEFFICIENTS",
                "L2": "PROVED_PASS_AS_A_FORMAL_EULER_PRODUCT",
                "L3": "PROVED_PASS_LOCAL_DEGREE_K_PLUS_1",
                "L4": "PARTIAL_SYM_K_DENOMINATOR_WITH_NONTRIVIAL_NUMERATOR_DEFECT",
                "L5": "NOT_ESTABLISHED_BY_THIS_PACKET",
                "L6": "NOT_ESTABLISHED_BY_THIS_PACKET",
                "L7": "NOT_ESTABLISHED_BY_THIS_PACKET",
                "L8": "NOT_ESTABLISHED_BY_THIS_PACKET",
                "L9": "NOT_ESTABLISHED_BY_THIS_PACKET",
            },
            "first_unresolved_level": "L4",
        },
        {
            "object": "noninteger complex power on the positive trace chamber",
            "statuses": {
                "L0": "PROVED_PASS_ONLY_AFTER_FIXING_X_GT_2_AND_POSITIVE_REAL_LOG",
                "L1": "NOT_GLOBAL_BRANCH_COHERENT",
                "L2": "NOT_ESTABLISHED",
                "L3": "PROVED_FAIL_INFINITELY_MANY_MEROMORPHIC_POLES",
                "L4": "NOT_REACHED",
                "L5": "NOT_REACHED",
                "L6": "NOT_REACHED",
                "L7": "NOT_REACHED",
                "L8": "NOT_EXCLUDED_IN_INFINITE_DIMENSIONAL_OR_CATEGORICAL_SETTINGS",
                "L9": "NOT_REACHED",
            },
            "first_failure_level": "L3",
        },
        {
            "object": "arbitrary polynomial coefficient transform Phi",
            "statuses": {
                "L0": "PROVED_PASS",
                "L1": "PROVED_PASS_UNIVERSALLY_IFF_PHI_IS_A_MONOMIAL_AFTER_NORMALIZATION",
                "L2": "CONDITIONAL_ON_L1",
                "L3": "PROVED_PASS_LOCAL_ORDER_AT_MOST_2_DEG_PHI_PLUS_1",
                "L4": "NOT_ESTABLISHED_IN_GENERAL",
                "L5": "NOT_ESTABLISHED",
                "L6": "NOT_ESTABLISHED",
                "L7": "NOT_ESTABLISHED",
                "L8": "NOT_ESTABLISHED",
                "L9": "NOT_ESTABLISHED",
            },
            "warning": "L3 can survive while L1 fails; the ladder is diagnostic, not a logical implication without hypotheses",
        },
    ]
    return {"levels": levels, "rows": rows}


def build_fixture(
    *,
    max_k: int = DEFAULT_MAX_K,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    if isinstance(max_k, bool) or not isinstance(max_k, int):
        raise TypeError("max_k must be an integer")
    if max_k < 4:
        raise ValueError("max_k must include the k=2,3,4 calibration rows")
    if max_k > MAX_ALLOWED_K:
        raise ValueError(f"max_k must not exceed {MAX_ALLOWED_K}")
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")

    work_units = sum((power + 1) ** 4 for power in range(max_k + 1)) + 5**3 + 400
    if work_units >= resource_cap:
        raise RuntimeError("declared exact replay would meet or exceed exclusive cap")

    sources_manifest = verify_sources_manifest()
    integer_rows = [_integer_row(power) for power in range(max_k + 1)]
    expected_examples = {
        2: [[1], [1]],
        3: [[1], [0, 2], [1]],
        4: [[1], [-1, 0, 3], [-1, 0, 3], [1]],
    }
    for power, expected in expected_examples.items():
        actual = integer_rows[power]["numerator"]["x_coefficient_vectors"]
        if actual != expected:
            raise ArithmeticError(
                f"unexpected numerator defect for k={power}: {actual}"
            )

    all_degree_roots = polynomial_root_exponents(range(max_k + 1))
    parity_roots = polynomial_root_exponents(range(max_k % 2, max_k + 1, 2))
    multiplicativity_controls = []
    for coefficients in (
        (1,),
        (0, 1),
        (0, 0, 1),
        (1, 1),
        (0, 2),
        (0, 0, 0),
        (Fraction(1, 2), Fraction(1, 2)),
    ):
        multiplicativity_controls.append(
            {
                "coefficients_ascending": [
                    fraction_text(Fraction(value)) for value in coefficients
                ],
                "formal_multiplicativity_identity": multiplicativity_identity(
                    coefficients
                ),
                "normalized_monomial_exponent": normalized_multiplicative_monomial(
                    coefficients
                ),
            }
        )

    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.nonintegral_local_power_rationality.v1",
        "status": "PROPOSED_EXACT_LOCAL_THEOREM_EXTERNAL_NOVELTY_UNREVIEWED",
        "programme_issue": 764,
        "claims": {
            "GLO764.LOCAL_POWER_RATIONALITY": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "for each fixed real x>2 in the hyperbolic non-tempered chamber and complex lambda under the positive-real logarithm",
                "statement": "sum_r u_r(x)^lambda*T^r is rational in T iff lambda is a nonnegative integer",
                "proof_mechanism": "binomial meromorphic continuation with finitely versus infinitely many distinct actual poles",
            },
            "GLO764.INTEGER_MINIMAL_DENOMINATOR": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_EXACTLY_REPLAYED",
                "scope": "k>=0, x>2, determinant-one normalization",
                "statement": "the reduced denominator is product_(j=0)^k (1-alpha^(k-2j)T)",
            },
            "GLO764.POLYNOMIAL_RECURRENCE_BOUND": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_EXACTLY_REPLAYED",
                "scope": "nonzero Phi in C[z]",
                "statement": "local recurrence order is at most 2*deg(Phi)+1; cancellation may lower it",
            },
            "GLO764.POLYNOMIAL_MULTIPLICATIVITY_RIGIDITY": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_FORMALLY_REPLAYED",
                "scope": "Phi in C[z], Phi(1)=1, identity in C[X,Y]",
                "statement": "Phi(XY)=Phi(X)Phi(Y) iff Phi=X^m for a unique m>=0",
            },
        },
        "normalization": {
            "trace_domain": "real x>2 (hyperbolic non-tempered determinant-one chamber)",
            "tempered_GL2_trace_chamber": "[-2,2] is not treated",
            "alpha": "(x+sqrt(x^2-4))/2 > 1",
            "q": "alpha^(-2) in (0,1)",
            "recurrence": "u_0=1; u_1=x; u_(r+2)=x*u_(r+1)-u_r",
            "binet": "u_r=alpha^r*(1-q^(r+1))/(1-q)",
            "complex_power": "u_r^lambda=exp(lambda*log(u_r)) with the real logarithm of u_r>0",
            "power_series_radius": "alpha^(-Re(lambda))",
        },
        "sources_manifest": sources_manifest,
        "integer_power_replay": {
            "maximum_k": max_k,
            "rows": integer_rows,
            "required_numerator_defects": {
                "k2": "1+T",
                "k3": "1+2*x*T+T^2",
                "k4": "(1+T)*(1+(3*x^2-2)*T+T^2)",
            },
        },
        "noninteger_hostile_controls": {
            "binomial_pole_prefixes": [
                rational_power_hostile_control(Fraction(-1)),
                rational_power_hostile_control(Fraction(1, 2)),
                rational_power_hostile_control(Fraction(3, 2)),
                rational_power_hostile_control(Fraction(-3, 2)),
            ],
            "negative_one_exact_hankel": reciprocal_hankel_control(3, 5),
            "analytic_proof_not_a_finite_hankel_inference": True,
            "excluded_domain_controls": [
                {
                    "case": "x=2",
                    "reason": "coalesced alpha=1 boundary requires a different proof",
                },
                {
                    "case": "x<-2",
                    "reason": "u_r changes sign and no positive-real logarithm is canonical",
                },
                {
                    "case": "abs(x)<2",
                    "reason": "oscillation and coefficient zeros create branch and definition failures",
                },
                {
                    "case": "raw determinant q_local!=1",
                    "reason": "requires a separately normalized two-parameter theorem",
                },
            ],
        },
        "polynomial_transform_replay": {
            "all_degrees_0_through_d": {
                "d": max_k,
                "root_exponents": list(all_degree_roots),
                "order": len(all_degree_roots),
                "sharp_upper_bound_2d_plus_1": 2 * max_k + 1,
            },
            "one_parity_only": {
                "d": max_k,
                "root_exponents": list(parity_roots),
                "order": len(parity_roots),
            },
            "formal_multiplicativity_controls": multiplicativity_controls,
            "single_fixed_L_function_is_not_a_universality_hypothesis": True,
        },
        "survival_ladder": _survival_ladder(),
        "literature_firewall": {
            "integer_power_formula_is_classical": True,
            "hadamard_closure_is_classical": True,
            "references": [
                {
                    "authors": "Pantelimon Stanica",
                    "title": "Generating Functions, Weighted and Non-Weighted Sums for Powers of Second-Order Recurrence Sequences",
                    "url": "https://arxiv.org/abs/math/0010149",
                    "boundary": "closed generating functions for nonnegative integer powers of nondegenerate second-order recurrences",
                },
                {
                    "authors": "Umberto Zannier",
                    "title": "A proof of Pisot's d-th root conjecture",
                    "url": "https://arxiv.org/abs/math/0010024",
                    "boundary": "Hadamard roots chosen in arithmetic recurrence settings; not the fixed positive-real complex power studied here",
                },
                {
                    "authors": "Andrea Ferretti and Umberto Zannier",
                    "title": "Equations in the Hadamard ring of rational functions",
                    "url": "https://arxiv.org/abs/math/0701772",
                    "boundary": "algebraic equations and roots in Hadamard rings; requires a specialist comparison before any novelty claim",
                },
                {
                    "authors": "Gessica Alecci, Stefano Barbero, and Nadir Murru",
                    "title": "Some notes on the algebraic structure of linear recurrent sequences",
                    "url": "https://arxiv.org/abs/2302.13867",
                    "boundary": "modern account of Hadamard closure and characteristic-root bookkeeping",
                },
            ],
            "search_is_not_a_priority_proof": True,
            "external_specialist_novelty_review_required": True,
        },
        "scope_firewall": {
            "local_positive_chamber_theorem_only": True,
            "x_gt_2_is_hyperbolic_non_tempered": True,
            "tempered_GL2_trace_chamber_not_treated": True,
            "not_an_automorphic_nonintegral_symmetric_power_no_go": True,
            "does_not_classify_arbitrary_holomorphic_Phi": True,
            "does_not_treat_branch_choices_or_zero_coefficients_globally": True,
            "does_not_construct_or_rule_out_an_infinite_dimensional_interpolation": True,
            "does_not_construct_a_global_Euler_product": True,
            "does_not_prove_convergence_of_any_defect_Euler_product": True,
            "does_not_supply_ramified_factors_gamma_factors_or_a_functional_equation": True,
            "does_not_prove_automorphy_motivic_origin_or_a_zero_theorem": True,
            "no_RH_GRH_or_zero_distribution_consequence": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": (
                "integer and rational Laurent-polynomial, recurrence, "
                "Hankel, and formal coefficient algebra"
            ),
            "maximum_k": max_k,
            "maximum_allowed_k": MAX_ALLOWED_K,
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
            raise SystemExit("stored nonintegral local-power fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

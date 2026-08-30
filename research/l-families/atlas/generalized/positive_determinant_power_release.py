"""Exact replay for the positive-determinant coefficient-power release."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
from collections.abc import Sequence
from fractions import Fraction
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
ATLAS_ROOT = PACKET_ROOT.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "positive_determinant_power_release.json"
SOURCE_MANIFEST_PATH = PACKET_ROOT / "positive_determinant_power_release.sources.json"
NOTE_PATH = PACKET_ROOT / "POSITIVE_DETERMINANT_POWER_RELEASE.md"
TEST_PATH = REPO_ROOT / "tests" / "test_positive_determinant_power_release.py"

EXPECTED_SOURCE_MANIFEST_SHA256_LF = (
    "6c4b007ce204ea2e9cfd6cb46907e31633a9123e1d9846be226b100a1e3da7eb"
)
EXPECTED_BASE_COMMIT = "522493abae0f8e5526ceff4192d73b2cc617c069"
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/NONINTEGRAL_LOCAL_POWER_RATIONALITY.md": (
        "5eeb1e7c6129646ac646c697276bcd4adb04aa0c"
    ),
    "research/l-families/atlas/generalized/nonintegral_local_power_rationality.json": (
        "67e5dfa63684078586e4727530d7b9e66d557636"
    ),
    "research/l-families/atlas/generalized/nonintegral_local_power_rationality.sources.json": (
        "db48a8a7f44d2e768b248a162cf3c48c71ac4494"
    ),
    "research/l-families/atlas/generalized/TRANSFER_MATRIX_SYMMETRIC_PARENT.md": (
        "9aef6f8a780e9dff5c3b7a53c012c0956be036dc"
    ),
    "research/l-families/atlas/generalized/transfer_matrix_symmetric_parent.json": (
        "4a569b7e97197fb7b04856be2d602e4ddaadb43f"
    ),
    "research/l-families/atlas/core/atlas_core.py": (
        "adea1dbb5f189f65357f39e1fe6bf1548bd77acc"
    ),
}
DEFAULT_MAX_POWER = 8
MAX_ALLOWED_POWER = 14
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 100_000


def _load_atlas_core():
    path = ATLAS_ROOT / "core" / "atlas_core.py"
    spec = importlib.util.spec_from_file_location(
        "glo764_positive_determinant_atlas_core", path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load atlas canonicalization core")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ATLAS_CORE = _load_atlas_core()
Polynomial = tuple[Fraction, ...]
PowerTerm = tuple[Fraction, Fraction, tuple[int, int]]


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


def _nonnegative_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def _exact_fraction(value: Fraction | int, name: str) -> Fraction:
    if isinstance(value, (bool, float)):
        raise TypeError(f"{name} must be an exact integer or fraction")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise TypeError(f"{name} must be an exact integer or fraction") from exc


def positive_root_pair(
    alpha: Fraction | int, beta: Fraction | int
) -> tuple[Fraction, Fraction]:
    left = _exact_fraction(alpha, "alpha")
    right = _exact_fraction(beta, "beta")
    if right <= 0 or left <= right:
        raise ValueError("roots must satisfy alpha > beta > 0")
    return left, right


def fraction_text(value: Fraction | int) -> str:
    rational = Fraction(value)
    if rational.denominator == 1:
        return str(rational.numerator)
    return f"{rational.numerator}/{rational.denominator}"


def recurrence_sequence(
    length: int, *, alpha: Fraction | int, beta: Fraction | int
) -> tuple[Fraction, ...]:
    _nonnegative_integer(length, "length")
    left, right = positive_root_pair(alpha, beta)
    if length == 0:
        return ()
    trace = left + right
    determinant = left * right
    values = [Fraction(1)]
    if length == 1:
        return tuple(values)
    values.append(trace)
    while len(values) < length:
        values.append(trace * values[-1] - determinant * values[-2])
    return tuple(values)


def binet_sequence(
    length: int, *, alpha: Fraction | int, beta: Fraction | int
) -> tuple[Fraction, ...]:
    _nonnegative_integer(length, "length")
    left, right = positive_root_pair(alpha, beta)
    return tuple(
        (left ** (index + 1) - right ** (index + 1)) / (left - right)
        for index in range(length)
    )


def integer_power_terms(
    power: int, *, alpha: Fraction | int, beta: Fraction | int
) -> tuple[PowerTerm, ...]:
    _nonnegative_integer(power, "power")
    left, right = positive_root_pair(alpha, beta)
    gap_power = (left - right) ** power
    return tuple(
        (
            Fraction((-1) ** j * math.comb(power, j))
            * left ** (power - j)
            * right**j
            / gap_power,
            left ** (power - j) * right**j,
            (power - j, j),
        )
        for j in range(power + 1)
    )


def power_parent_sequence(
    power: int,
    length: int,
    *,
    alpha: Fraction | int,
    beta: Fraction | int,
) -> tuple[Fraction, ...]:
    _nonnegative_integer(length, "length")
    terms = integer_power_terms(power, alpha=alpha, beta=beta)
    return tuple(
        sum(coefficient * weight**index for coefficient, weight, _ in terms)
        for index in range(length)
    )


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


def denominator_from_weights(weights: Sequence[Fraction]) -> Polynomial:
    if not weights:
        raise ValueError("at least one weight is required")
    denominator: Polynomial = (Fraction(1),)
    for weight in weights:
        denominator = multiply_polynomials(
            denominator, (Fraction(1), -Fraction(weight))
        )
    return denominator


def convolution_at(
    denominator: Sequence[Fraction], sequence: Sequence[Fraction], index: int
) -> Fraction:
    _nonnegative_integer(index, "index")
    return sum(
        denominator[degree] * sequence[index - degree]
        for degree in range(min(index, len(denominator) - 1) + 1)
    )


def normalized_sequences(
    length: int,
    *,
    alpha: Fraction | int,
    beta: Fraction | int,
    positive_sqrt_delta: Fraction | int,
) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    _nonnegative_integer(length, "length")
    left, right = positive_root_pair(alpha, beta)
    scale = _exact_fraction(positive_sqrt_delta, "positive_sqrt_delta")
    if scale <= 0 or scale * scale != left * right:
        raise ValueError("positive_sqrt_delta must be positive and square to alpha*beta")
    a = left / scale
    a_inverse = right / scale
    if a <= 1 or a * a_inverse != 1:
        raise ArithmeticError("determinant-one normalization failed")
    original = recurrence_sequence(length, alpha=left, beta=right)
    normalized = recurrence_sequence(length, alpha=a, beta=a_inverse)
    if any(
        original[index] != scale**index * normalized[index]
        for index in range(length)
    ):
        raise ArithmeticError("u_r=s^r*v_r transport identity failed")
    return original, normalized


def verify_sources_manifest() -> dict[str, object]:
    actual_manifest_hash = _lf_sha256(SOURCE_MANIFEST_PATH)
    if actual_manifest_hash != EXPECTED_SOURCE_MANIFEST_SHA256_LF:
        raise RuntimeError("positive-determinant sources manifest hash mismatch")
    manifest = json.loads(SOURCE_MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest.get("schema") != (
        "riemann.atlas.generalized.positive_determinant_power_release.sources.v1"
    ):
        raise RuntimeError("positive-determinant sources manifest schema mismatch")
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("positive-determinant source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise TypeError("positive-determinant sources must be a list")
    source_index = {row.get("path"): row for row in sources}
    if len(source_index) != len(sources) or set(source_index) != set(
        EXPECTED_SOURCE_OBJECTS
    ):
        raise RuntimeError("positive-determinant source path set mismatch")

    verified: list[dict[str, object]] = []
    for path, expected_blob in EXPECTED_SOURCE_OBJECTS.items():
        row = source_index[path]
        if row.get("git_blob") != expected_blob:
            raise RuntimeError(f"manifest Git blob mismatch for {path}")
        actual_blob = _git_blob_at(EXPECTED_BASE_COMMIT, path)
        if actual_blob != expected_blob:
            raise RuntimeError(f"authenticated Git blob mismatch for {path}")
        actual_hash = _lf_sha256(REPO_ROOT / path)
        if actual_hash != row.get("file_sha256_lf_normalized"):
            raise RuntimeError(f"working-tree source hash mismatch for {path}")
        record = dict(row)
        if "payload_sha256" in row:
            source_payload = json.loads((REPO_ROOT / path).read_text(encoding="utf-8"))
            claimed_payload = source_payload.pop("payload_sha256", None)
            actual_payload = _canonical_sha256(source_payload)
            if (
                claimed_payload != row.get("payload_sha256")
                or actual_payload != claimed_payload
            ):
                raise RuntimeError(f"source payload mismatch for {path}")
        verified.append(record)
    return {
        "manifest": _relative(SOURCE_MANIFEST_PATH),
        "file_sha256_lf_normalized": actual_manifest_hash,
        "base_commit": EXPECTED_BASE_COMMIT,
        "verified_sources": verified,
        "corollary_audit": manifest["corollary_audit"],
        "scope_firewall": manifest["scope_firewall"],
    }


def _power_row(power: int, alpha: Fraction, beta: Fraction) -> dict[str, object]:
    terms = integer_power_terms(power, alpha=alpha, beta=beta)
    weights = tuple(term[1] for term in terms)
    coefficients = tuple(term[0] for term in terms)
    length = 3 * (power + 1) + 7
    base = recurrence_sequence(length, alpha=alpha, beta=beta)
    shadow = tuple(value**power for value in base)
    parent = power_parent_sequence(power, length, alpha=alpha, beta=beta)
    if shadow != parent:
        raise ArithmeticError("integer power expansion failed")
    if any(weight <= 0 for weight in weights) or len(set(weights)) != power + 1:
        raise ArithmeticError("positive integer-power weights degenerated")
    if any(coefficient == 0 for coefficient in coefficients):
        raise ArithmeticError("integer-power coefficient vanished")
    denominator = denominator_from_weights(weights)
    if len(denominator) - 1 != power + 1:
        raise ArithmeticError("sharp denominator degree failed")
    for index in range(power + 1, length):
        if convolution_at(denominator, shadow, index):
            raise ArithmeticError("sharp denominator failed tail annihilation")
    return {
        "k": power,
        "terms": [
            {
                "exponent_pair": list(exponents),
                "coefficient": fraction_text(coefficient),
                "weight": fraction_text(weight),
            }
            for coefficient, weight, exponents in terms
        ],
        "all_coefficients_nonzero": True,
        "all_weights_positive_and_pairwise_distinct": True,
        "minimal_denominator_coefficients_ascending": [
            fraction_text(value) for value in denominator
        ],
        "minimal_denominator_degree": len(denominator) - 1,
        "tail_annihilation_checked_through_index": length - 1,
    }


def _root_pair_row(
    alpha: Fraction, beta: Fraction, max_power: int
) -> dict[str, object]:
    length = 3 * (max_power + 1) + 7
    recurrence = recurrence_sequence(length, alpha=alpha, beta=beta)
    binet = binet_sequence(length, alpha=alpha, beta=beta)
    if recurrence != binet:
        raise ArithmeticError("Binet and recurrence sequences disagree")
    return {
        "alpha": fraction_text(alpha),
        "beta": fraction_text(beta),
        "trace_t": fraction_text(alpha + beta),
        "determinant_delta": fraction_text(alpha * beta),
        "strict_hyperbolic_inequality": "t>2*sqrt(delta)",
        "sequence_prefix": [fraction_text(value) for value in recurrence[:10]],
        "binet_equals_recurrence_through_index": length - 1,
        "integer_power_rows": [
            _power_row(power, alpha, beta) for power in range(max_power + 1)
        ],
    }


def _normalization_row(
    alpha: Fraction, beta: Fraction, positive_sqrt_delta: Fraction
) -> dict[str, object]:
    length = 16
    original, normalized = normalized_sequences(
        length,
        alpha=alpha,
        beta=beta,
        positive_sqrt_delta=positive_sqrt_delta,
    )
    a = alpha / positive_sqrt_delta
    integer_lambda_rows = []
    for exponent in (-2, -1, 0, 1, 2, 3):
        scale_power = positive_sqrt_delta**exponent
        if any(
            original[index] ** exponent
            != scale_power**index * normalized[index] ** exponent
            for index in range(length)
        ):
            raise ArithmeticError("integer logarithmic transport control failed")
        integer_lambda_rows.append(
            {
                "lambda": exponent,
                "s_to_lambda": fraction_text(scale_power),
                "transport_checked_through_index": length - 1,
            }
        )
    return {
        "alpha": fraction_text(alpha),
        "beta": fraction_text(beta),
        "delta": fraction_text(alpha * beta),
        "positive_sqrt_delta_s": fraction_text(positive_sqrt_delta),
        "a": fraction_text(a),
        "a_inverse": fraction_text(1 / a),
        "normalized_trace_x": fraction_text(a + 1 / a),
        "u_r_equals_s_to_r_v_r_through_index": length - 1,
        "integer_lambda_transport_controls": integer_lambda_rows,
        "all_complex_lambda_transport": "PROVED_BY_POSITIVE_LOG_ADDITIVITY_IN_NOTE",
    }


def _survival_ladder() -> dict[str, object]:
    return {
        "levels": [f"L{level}" for level in range(10)],
        "rows": [
            {
                "object": "positive-determinant integer power",
                "L0": "PASS_POSITIVE_LOG_BRANCH_INDEPENDENT",
                "L1": "CONDITIONAL_ON_PRIMEWISE_MULTIPLICATIVE_INPUT",
                "L2": "FORMAL_IF_L1_INPUT_IS_SUPPLIED",
                "L3": "PASS_EXACT_DEGREE_k_PLUS_1",
                "first_unresolved_level": "L4",
            },
            {
                "object": "positive-determinant noninteger power",
                "L0": "PASS_POSITIVE_LOG_FIXED",
                "L1": "NO_GLOBAL_COHERENCE_PROVED",
                "L3": "FAIL_NONRATIONAL_BY_TRANSPORTED_SOURCE_THEOREM",
                "first_failure_levels": ["L1", "L3"],
            },
            {
                "object": "complex or nonpositive determinant",
                "L0": "FAIL_WITHOUT_SQUARE_ROOT_AND_LOG_BRANCH_DATA",
                "first_failure_level": "L0",
            },
        ],
        "L4_through_L9_not_established": True,
    }


def build_fixture(
    *,
    max_power: int = DEFAULT_MAX_POWER,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _nonnegative_integer(max_power, "max_power")
    if max_power < 4:
        raise ValueError("max_power must include calibration powers through four")
    if max_power > MAX_ALLOWED_POWER:
        raise ValueError(f"max_power must not exceed {MAX_ALLOWED_POWER}")
    if isinstance(resource_cap, bool) or not isinstance(resource_cap, int):
        raise TypeError("resource_cap must be an integer")
    if resource_cap <= 0:
        raise ValueError("resource_cap must be positive")

    root_pairs = (
        (Fraction(3), Fraction(2)),
        (Fraction(4), Fraction(1)),
        (Fraction(9), Fraction(4)),
        (Fraction(2), Fraction(1, 2)),
    )
    work_units = len(root_pairs) * sum(
        (power + 1) ** 3 for power in range(max_power + 1)
    )
    if work_units >= resource_cap:
        raise RuntimeError("declared exact replay would meet or exceed exclusive cap")

    source_lock = verify_sources_manifest()
    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.positive_determinant_power_release.v1",
        "status": "EXACT_TRANSPORT_COROLLARY_NO_NEW_MECHANISM_OR_NOVELTY_CLAIM",
        "programme_issue": 764,
        "claims": {
            "GLO764.POSITIVE_DETERMINANT_POWER_RATIONALITY": {
                "status": "PROVED_AS_COROLLARY_OF_AUTHENTICATED_SOURCE_THEOREM",
                "statement": "for alpha>beta>0 under the positive log, sum_r u_r^lambda*T^r is rational iff lambda is a nonnegative integer",
            },
            "GLO764.POSITIVE_DETERMINANT_INTEGER_MINIMAL_DENOMINATOR": {
                "status": "PROVED_NATIVELY_AND_EXACTLY_REPLAYED",
                "statement": "at k>=0 the reduced denominator is product_j(1-alpha^(k-j)*beta^j*T), of degree k+1",
            },
            "GLO764.POSITIVE_DETERMINANT_BRANCH_GATE": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "statement": "the transport uses only the unique positive sqrt(delta) and positive-real logarithms; other determinant chambers are excluded",
            },
        },
        "audit_verdict": {
            "independent_nonrationality_theorem": False,
            "exact_relation_to_source": "G_(lambda;t,delta)(T)=G_(lambda;x,1)(sqrt(delta)^lambda*T)",
            "why_packetized": "closes the positive determinant coordinate release with a source lock, branch firewall, and sharp transported integer denominator",
        },
        "sources": source_lock,
        "normalization": {
            "root_chamber": "alpha>beta>0",
            "trace": "t=alpha+beta",
            "determinant": "delta=alpha*beta>0",
            "equivalent_trace_chamber": "t>2*sqrt(delta)",
            "recurrence": "u_0=1; u_1=t; u_(r+2)=t*u_(r+1)-delta*u_r",
            "binet": "u_r=(alpha^(r+1)-beta^(r+1))/(alpha-beta)",
            "positive_scale": "s=sqrt(delta)>0",
            "determinant_one_root": "a=sqrt(alpha/beta)>1",
            "transport": "u_r=s^r*v_r and G_(lambda;t,delta)(T)=G_(lambda;x,1)(s^lambda*T)",
            "complex_power": "positive-real logarithm only",
        },
        "root_pair_corpus": [
            _root_pair_row(alpha, beta, max_power) for alpha, beta in root_pairs
        ],
        "determinant_normalization_controls": [
            _normalization_row(Fraction(4), Fraction(1), Fraction(2)),
            _normalization_row(Fraction(9), Fraction(4), Fraction(6)),
            _normalization_row(Fraction(2), Fraction(1, 2), Fraction(1)),
        ],
        "hostile_controls": {
            "equal_roots": "REJECTED_COALESCED_BOUNDARY",
            "reversed_roots": "REJECTED_ORDERING_FAILURE",
            "zero_root": "REJECTED_STRICT_POSITIVITY_FAILURE",
            "negative_root": "REJECTED_POSITIVE_LOG_FAILURE",
            "negative_square_root": "REJECTED_BRANCH_AND_SIGN_CHANGE",
            "complex_determinant": "EXCLUDED_REQUIRES_SQUARE_ROOT_AND_LOG_BRANCH_DATA",
            "integer_denominator_requires_distinct_nonzero_weights": True,
        },
        "survival_ladder": _survival_ladder(),
        "scope_firewall": source_lock["scope_firewall"],
        "resource_contract": {
            "arithmetic_class": "EXACT_RATIONAL",
            "exact_method": "integer and fractional recurrences, Binet identities, binomial power terms, and polynomial convolutions",
            "maximum_power": max_power,
            "maximum_allowed_power": MAX_ALLOWED_POWER,
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
        help="verify that the stored canonical fixture is current",
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if not OUTPUT_PATH.exists():
            raise SystemExit("stored positive-determinant fixture is missing")
        if OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored positive-determinant fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

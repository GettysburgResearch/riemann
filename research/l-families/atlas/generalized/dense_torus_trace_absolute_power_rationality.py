"""Exact bounded replay for dense-torus absolute trace powers.

The companion note proves the continuous dense-orbit and cusp arguments.
This producer checks root-of-unity trace-zero certificates, exact multinomial
support, determinant-one injectivity, root-lattice counts, and source locks.
It does not infer an analytic theorem from finite rows.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from collections.abc import Iterator, Sequence
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
PACKET_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[4]
OUTPUT_PATH = PACKET_ROOT / "dense_torus_trace_absolute_power_rationality.json"
SOURCES_PATH = PACKET_ROOT / "dense_torus_trace_absolute_power_rationality.sources.json"
NOTE_PATH = PACKET_ROOT / "DENSE_TORUS_TRACE_ABSOLUTE_POWER_RATIONALITY.md"
TEST_PATH = REPO_ROOT / "tests" / "test_dense_torus_trace_absolute_power_rationality.py"

EXPECTED_BASE_COMMIT = "902b7dfeb12c5bee9028d97b420e3c2f42ac31fd"
EXPECTED_SOURCES_SHA256_LF = (
    "901ee79a73442c531f110284ec26e69013c59b3b65d0f7b3bbb1a8fefaefd7c1"
)
EXPECTED_SOURCE_OBJECTS = {
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md": (
        "8f27df80a4983b4d393ee3a2477a744afaeb1d3a"
    ),
    "research/l-families/atlas/generalized/IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md": (
        "e6308d8e4b9122598f7857b34967f058a64a4f59"
    ),
    "research/l-families/atlas/generalized/RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md": (
        "9548280426316237de50c7e71e2dd704aa68f00b"
    ),
    "research/l-families/atlas/generalized/TRANSFER_MATRIX_SYMMETRIC_PARENT.md": (
        "9aef6f8a780e9dff5c3b7a53c012c0956be036dc"
    ),
}

DEFAULT_MAX_N = 5
DEFAULT_MAX_M = 4
MAX_ALLOWED_N = 7
MAX_ALLOWED_M = 5
DEFAULT_RESOURCE_CAP_EXCLUSIVE = 1_000_000
SINGLE_EXPANSION_CAP_EXCLUSIVE = 300_000

Exponent = tuple[int, ...]


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def _normalized_bytes(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def _lf_sha256(path: Path) -> str:
    return hashlib.sha256(_normalized_bytes(path.read_bytes())).hexdigest()


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


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


def _git_blob_bytes(blob: str) -> bytes:
    try:
        result = subprocess.run(
            ["git", "cat-file", "blob", blob],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        raise RuntimeError("git blob read could not be executed") from exc
    if result.returncode != 0:
        raise RuntimeError(f"git blob read failed: {blob}")
    return result.stdout


def _validate_integer(value: int, name: str, lower: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < lower:
        raise ValueError(f"{name} must be at least {lower}")


def _validate_rank_power(n: int, m: int) -> None:
    _validate_integer(n, "n", 2)
    _validate_integer(m, "m", 0)
    if n > MAX_ALLOWED_N:
        raise ValueError(f"n exceeds allowed maximum {MAX_ALLOWED_N}")
    if m > MAX_ALLOWED_M:
        raise ValueError(f"m exceeds allowed maximum {MAX_ALLOWED_M}")


def weak_compositions(total: int, parts: int) -> Iterator[Exponent]:
    _validate_integer(total, "total", 0)
    _validate_integer(parts, "parts", 1)
    if total > MAX_ALLOWED_M or parts > MAX_ALLOWED_N:
        raise ValueError("composition request exceeds bounded replay range")

    def walk(remaining: int, count: int, prefix: Exponent) -> Iterator[Exponent]:
        if count == 1:
            yield prefix + (remaining,)
            return
        for first in range(remaining + 1):
            yield from walk(remaining - first, count - 1, prefix + (first,))

    yield from walk(total, parts, ())


def positive_compositions(total: int, parts: int) -> Iterator[Exponent]:
    _validate_integer(total, "total", 1)
    _validate_integer(parts, "parts", 1)
    if total > MAX_ALLOWED_M or parts > MAX_ALLOWED_N:
        raise ValueError("composition request exceeds bounded replay range")
    if parts > total:
        return
    for row in weak_compositions(total - parts, parts):
        yield tuple(value + 1 for value in row)


def multinomial(total: int, exponents: Exponent) -> int:
    _validate_integer(total, "total", 0)
    if not exponents or len(exponents) > MAX_ALLOWED_N:
        raise ValueError("multinomial exponent vector has invalid bounded length")
    if total > MAX_ALLOWED_M:
        raise ValueError("multinomial total exceeds bounded replay range")
    for value in exponents:
        _validate_integer(value, "multinomial exponent", 0)
    if sum(exponents) != total:
        raise ValueError("multinomial exponents must sum to total")
    denominator = math.prod(math.factorial(value) for value in exponents)
    return math.factorial(total) // denominator


def root_lattice_shell_count(n: int, s: int) -> int:
    _validate_rank_power(n, s)
    if s == 0:
        return 1
    return sum(
        math.comb(n, a)
        * math.comb(n - a, b)
        * math.comb(s - 1, a - 1)
        * math.comb(s - 1, b - 1)
        for a in range(1, min(n - 1, s) + 1)
        for b in range(1, min(n - a, s) + 1)
    )


def root_lattice_ball_count(n: int, m: int) -> int:
    _validate_rank_power(n, m)
    return sum(root_lattice_shell_count(n, s) for s in range(m + 1))


def root_lattice_compact_count(n: int, m: int) -> int:
    _validate_rank_power(n, m)
    return sum(
        math.comb(n - 1, k) ** 2 * math.comb(m - k + n - 1, n - 1)
        for k in range(min(n - 1, m) + 1)
    )


def root_lattice_ball(n: int, m: int) -> set[Exponent]:
    """Enumerate by disjoint sign supports, independently of trace expansion."""
    _validate_rank_power(n, m)
    result: set[Exponent] = {(0,) * n}
    positions = tuple(range(n))
    for s in range(1, m + 1):
        for a in range(1, min(n - 1, s) + 1):
            for b in range(1, min(n - a, s) + 1):
                for positive_positions in itertools.combinations(positions, a):
                    remaining = tuple(
                        index for index in positions if index not in positive_positions
                    )
                    for negative_positions in itertools.combinations(remaining, b):
                        for positive in positive_compositions(s, a):
                            for negative in positive_compositions(s, b):
                                vector = [0] * n
                                for index, value in zip(positive_positions, positive):
                                    vector[index] = value
                                for index, value in zip(negative_positions, negative):
                                    vector[index] = -value
                                result.add(tuple(vector))
    return result


def determinant_one_character(exponent: Exponent) -> Exponent:
    if len(exponent) < 2 or len(exponent) > MAX_ALLOWED_N:
        raise ValueError("character vector length is outside the bounded rank range")
    for value in exponent:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("character exponents must be integers")
    return tuple(value - exponent[-1] for value in exponent[:-1])


def exact_trace_coefficients(
    n: int, m: int, *, resource_cap: int = SINGLE_EXPANSION_CAP_EXCLUSIVE
) -> dict[Exponent, int]:
    _validate_rank_power(n, m)
    _validate_integer(resource_cap, "resource_cap", 1)
    composition_count = math.comb(m + n - 1, n - 1)
    pair_units = composition_count**2
    if pair_units >= resource_cap:
        raise RuntimeError(
            f"expansion pair units {pair_units} reach exclusive cap {resource_cap}"
        )
    compositions = tuple(weak_compositions(m, n))
    if len(compositions) != composition_count:
        raise ArithmeticError("weak-composition count disagrees with stars and bars")
    weighted = [(row, multinomial(m, row)) for row in compositions]
    result: dict[Exponent, int] = {}
    for alpha, alpha_weight in weighted:
        for beta, beta_weight in weighted:
            exponent = tuple(left - right for left, right in zip(alpha, beta))
            result[exponent] = result.get(exponent, 0) + alpha_weight * beta_weight
    return result


def trace_zero_curve_certificate(n: int) -> dict[str, object]:
    _validate_integer(n, "n", 2)
    if n > MAX_ALLOWED_N:
        raise ValueError(f"n exceeds allowed maximum {MAX_ALLOWED_N}")
    modulus = 2 * n
    exponents = [(n - 1 + 2 * j) % modulus for j in range(n)]
    ratio_order = modulus // math.gcd(2, modulus)
    product_exponent = sum(exponents) % modulus
    derivative_nonzero = exponents[0] != exponents[1]
    if ratio_order != n or product_exponent != 0 or not derivative_nonzero:
        raise ArithmeticError("trace-zero curve certificate failed")
    return {
        "n": n,
        "root_model": "eta=exp(pi*i/n), q_j=eta^(n-1+2(j-1)), j=1,...,n",
        "q_eta_exponents_mod_2n": exponents,
        "geometric_ratio_order": ratio_order,
        "trace_zero_reason": "complete geometric n-cycle of a nontrivial nth root",
        "product_eta_exponent_mod_2n": product_exponent,
        "determinant_equals_one": True,
        "curve": "(q_1 exp(it), q_2 exp(-it), q_3, ..., q_n)",
        "trace_derivative": "i(q_1-q_2)",
        "trace_derivative_nonzero": True,
    }


def exact_support_row(n: int, m: int) -> dict[str, object]:
    coefficients = exact_trace_coefficients(n, m)
    expected_support = root_lattice_ball(n, m)
    if set(coefficients) != expected_support:
        raise ArithmeticError("trace support is not the declared root-lattice ball")
    count = len(coefficients)
    if count != root_lattice_ball_count(n, m):
        raise ArithmeticError("composition support count failed")
    if count != root_lattice_compact_count(n, m):
        raise ArithmeticError("compact binomial support count failed")
    if any(coefficient <= 0 for coefficient in coefficients.values()):
        raise ArithmeticError("trace expansion lost coefficient positivity")
    if sum(coefficients.values()) != n ** (2 * m):
        raise ArithmeticError("coefficient mass fails evaluation at the identity")
    if any(
        coefficients[tuple(-value for value in exponent)] != coefficient
        for exponent, coefficient in coefficients.items()
    ):
        raise ArithmeticError("inversion symmetry failed")
    quotient_characters = {
        determinant_one_character(exponent) for exponent in coefficients
    }
    if len(quotient_characters) != count:
        raise ArithmeticError("determinant-one quotient created a support collision")
    records = [
        {"exponent": list(exponent), "coefficient": coefficients[exponent]}
        for exponent in sorted(coefficients)
    ]
    return {
        "n": n,
        "m": m,
        "lambda_2m": 2 * m,
        "analytic_positive_exponent_chamber": m > 0,
        "m_zero_is_polynomial_control_only": m == 0,
        "support_count": count,
        "dense_orbit_minimal_order": count if m > 0 else None,
        "composition_pair_units": math.comb(m + n - 1, n - 1) ** 2,
        "coefficient_mass_at_identity": sum(coefficients.values()),
        "all_coefficients_positive": True,
        "full_torus_character_count": count,
        "determinant_one_character_count": len(quotient_characters),
        "determinant_one_no_collisions": True,
        "support_and_coefficients_sha256": _canonical_sha256(records),
        "representative_coefficients": [
            records[0],
            next(row for row in records if row["exponent"] == [0] * n),
            records[-1],
        ],
    }


def verify_sources_manifest() -> dict[str, object]:
    actual_hash = _lf_sha256(SOURCES_PATH)
    if actual_hash != EXPECTED_SOURCES_SHA256_LF:
        raise RuntimeError("dense-torus sources manifest hash mismatch")
    manifest = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    if manifest.get("base_commit") != EXPECTED_BASE_COMMIT:
        raise RuntimeError("dense-torus source base commit mismatch")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or any(not isinstance(row, dict) for row in sources):
        raise TypeError("dense-torus sources must be a list of objects")
    index = {row.get("path"): row for row in sources}
    if len(index) != len(sources) or set(index) != set(EXPECTED_SOURCE_OBJECTS):
        raise RuntimeError("dense-torus source path set mismatch")
    verified: list[dict[str, object]] = []
    for path, expected_blob in EXPECTED_SOURCE_OBJECTS.items():
        row = index[path]
        if row.get("git_blob") != expected_blob:
            raise RuntimeError(f"manifest Git blob mismatch for {path}")
        actual_blob = _git_blob_at(EXPECTED_BASE_COMMIT, path)
        if actual_blob != expected_blob:
            raise RuntimeError(f"authenticated Git blob mismatch for {path}")
        normalized_blob = _normalized_bytes(_git_blob_bytes(actual_blob))
        blob_hash = hashlib.sha256(normalized_blob).hexdigest()
        if blob_hash != row.get("file_sha256_lf_normalized"):
            raise RuntimeError(f"Git blob content hash mismatch for {path}")
        if _lf_sha256(REPO_ROOT / path) != blob_hash:
            raise RuntimeError(f"working-tree source hash mismatch for {path}")
        verified.append(dict(row))
    references = manifest.get("external_references")
    if not isinstance(references, list) or len(references) != 2:
        raise RuntimeError("expected two external literature boundary records")
    return {
        "manifest": _relative(SOURCES_PATH),
        "manifest_sha256_lf_normalized": actual_hash,
        "base_commit": EXPECTED_BASE_COMMIT,
        "git_blob_contents_compared_to_working_tree": True,
        "verified_sources": verified,
        "external_references": references,
        "scope_firewall": manifest["scope_firewall"],
    }


def _analytic_proof_obligations() -> dict[str, object]:
    return {
        "positive_orbit_tail": "every tail is dense in the stated compact torus",
        "recurrence_extension": "a continuous recurrence residual vanishing on the tail vanishes everywhere",
        "fourier_multiplier": "Q(chi(tau))*fhat(chi)=0",
        "character_evaluation": "density makes chi -> chi(tau) injective",
        "finite_spectrum": "a nonzero polynomial has only finitely many roots",
        "complex_cusp": "a simple trace zero gives |t|^lambda times a nonzero real-analytic factor",
        "cusp_conclusion": "analyticity forces lambda to be a positive even integer",
        "determinant_one_support_injection": "sum(v)=sum(w)=0 and v-w=k*(1,...,1) force k=0",
        "finite_replay_is_not_universal_proof": True,
    }


def build_fixture(
    *,
    max_n: int = DEFAULT_MAX_N,
    max_m: int = DEFAULT_MAX_M,
    resource_cap: int = DEFAULT_RESOURCE_CAP_EXCLUSIVE,
) -> dict[str, object]:
    _validate_rank_power(max_n, max_m)
    _validate_integer(resource_cap, "resource_cap", 1)
    expansion_pair_units = sum(
        math.comb(m + n - 1, n - 1) ** 2
        for n in range(2, max_n + 1)
        for m in range(max_m + 1)
    )
    root_vector_units = sum(
        root_lattice_ball_count(n, m)
        for n in range(2, max_n + 1)
        for m in range(max_m + 1)
    )
    declared_work_units = expansion_pair_units + root_vector_units
    if declared_work_units >= resource_cap:
        raise RuntimeError(
            f"declared work {declared_work_units} reaches exclusive cap {resource_cap}"
        )
    source_lock = verify_sources_manifest()
    rows = [
        exact_support_row(n, m)
        for n in range(2, max_n + 1)
        for m in range(max_m + 1)
    ]
    trace_zero_rows = [trace_zero_curve_certificate(n) for n in range(2, max_n + 1)]
    degree_table = [
        {
            "n": n,
            "m_values": list(range(max_m + 1)),
            "counts": [root_lattice_ball_count(n, m) for m in range(max_m + 1)],
        }
        for n in range(2, max_n + 1)
    ]
    fixture: dict[str, object] = {
        "schema": "riemann.atlas.generalized.dense_torus_trace_absolute_power_rationality.v1",
        "programme_issue": {
            "number": 764,
            "url": "https://github.com/gfreund123/riemann/issues/764",
        },
        "claims": {
            "GLO764.DENSE_TORUS_FINITE_CHARACTER": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "continuous function on a compact torus with dense cyclic translation",
                "conclusion": "eventual recurrence iff finite character support",
            },
            "GLO764.DENSE_UNITARY_TRACE_ABSOLUTE_GATE": {
                "status": "PROVED_IN_COMPANION_NOTE",
                "scope": "n>=2, Re(lambda)>0, dense full or determinant-one unitary torus",
                "classification": "rational iff lambda is a positive even integer",
            },
            "GLO764.TRACE_EVEN_POWER_ROOT_LATTICE_SUPPORT": {
                "status": "PROVED_IN_COMPANION_NOTE_AND_FINITE_ROWS_EXACTLY_REPLAYED",
                "support": "v in Z^n, sum(v)=0, sum(abs(v))<=2m",
                "degree": "A_(n-1) root-lattice ball count",
                "same_count_on_full_and_determinant_one_tori": True,
            },
        },
        "source_lock": source_lock,
        "trace_zero_curve_certificates": trace_zero_rows,
        "exact_polynomial_controls": {
            "row_count": len(rows),
            "rows_sha256": _canonical_sha256(rows),
            "rows": rows,
            "degree_table": degree_table,
            "all_rank_two_counts_are_2m_plus_1": all(
                root_lattice_ball_count(2, m) == 2 * m + 1
                for m in range(max_m + 1)
            ),
            "all_rank_three_counts_are_1_plus_3m_m_plus_1": all(
                root_lattice_ball_count(3, m) == 1 + 3 * m * (m + 1)
                for m in range(max_m + 1)
            ),
        },
        "analytic_proof_obligations": _analytic_proof_obligations(),
        "scope_firewall": {
            "rank_one_is_a_counterexample_and_excluded": True,
            "dense_full_or_determinant_one_orbit_required": True,
            "nondense_diagonal_constant_absolute_trace_counterexample_recorded": True,
            "strictly_positive_real_part_required": True,
            "zero_value_fixed_to_zero": True,
            "m_zero_rows_are_polynomial_controls_not_lambda_zero_claims": True,
            "no_prime_indexed_global_family_constructed": True,
            "no_ramified_factors_completion_or_functional_equation": True,
            "no_automorphy_motive_or_RH_GRH_consequence": True,
            "finite_dimensional_constant_state_space_only": True,
            "external_novelty_unreviewed": True,
        },
        "resource_contract": {
            "arithmetic_class": "EXACT_INTEGER_MULTINOMIAL_ROOT_EXPONENT",
            "maximum_n": max_n,
            "maximum_m": max_m,
            "maximum_allowed_n": MAX_ALLOWED_N,
            "maximum_allowed_m": MAX_ALLOWED_M,
            "expansion_pair_units": expansion_pair_units,
            "root_vector_units": root_vector_units,
            "declared_work_units": declared_work_units,
            "work_unit_definition": "one multinomial pair or one independently enumerated root-lattice vector",
            "work_unit_cap_exclusive": resource_cap,
            "single_expansion_pair_cap_exclusive": SINGLE_EXPANSION_CAP_EXCLUSIVE,
            "float_operations": 0,
            "random_samples": 0,
            "external_symbolic_engine": False,
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
        "--check", action="store_true", help="fail unless the stored fixture is current"
    )
    args = parser.parse_args(argv)
    serialized = _serialized_fixture()
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != serialized:
            raise SystemExit("stored dense-torus trace fixture is stale")
        print(f"verified {OUTPUT_PATH}")
        return 0
    OUTPUT_PATH.write_text(serialized, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

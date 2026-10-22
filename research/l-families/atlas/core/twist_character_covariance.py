from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, sqrt
from pathlib import Path
from typing import Any

from atlas_core import ATLAS_ROOT, fraction_json, read_json, semantic_identity, sha256_hex, write_json
from local_euler import elliptic_trace, primes_up_to
from run_pilot import artifact_binding, hash_object, programme_ref, raw_sha256


RAW_RESULT_SCHEMA = "research/l-families/atlas/detectors/raw-schemas/twist-character-covariance-result.schema.json"
DEFINITION = (
    "For fundamental discriminants d with 1<|d|<=X and gcd(d,11)=1, evaluate the exact finite raw Gram "
    "matrix G_X(p,q)=|D(X)|^(-1) sum_d chi_d(p)chi_d(q), its centered covariance, and the mean, second "
    "moment, and variance of sum_p a_p(E)chi_d(p)/sqrt(p) at good primes p,q<=43."
)
BOUNDS = [256, 512, 1024, 2048]
PRIME_BOUND = 43
BASE_CONDUCTOR = 11
BASE_SLUG = "EC.11.R0"
COORDINATE_FORMULAS = {
    "notation": (
        "For aligned indices i,j, let p_i=primes[i], a_i=traces[i], "
        "s_i=character_sums[i], R_ij=raw_gram.numerators[i][j], "
        "H_ij=centered_covariance.numerators[i][j], and N=discriminant_count."
    ),
    "marginal_counts": (
        "positive_i=(R_ii+s_i)/2, negative_i=(R_ii-s_i)/2, zero_i=N-R_ii; "
        "mean chi_i=s_i/N, local density_i=R_ii/N, asymptotic comparator_i=p_i/(p_i+1), "
        "and density error_i=R_ii/N-p_i/(p_i+1)."
    ),
    "mean": "E[W]=sum_i (a_i s_i/(N p_i)) sqrt(p_i).",
    "second_moment": (
        "E[W^2]=sum_i a_i^2 R_ii/(N p_i) + "
        "sum_{i<j} (2 a_i a_j R_ij/(N p_i p_j)) sqrt(p_i p_j)."
    ),
    "centered_variance": (
        "Var(W)=sum_i a_i^2 H_ii/(N^2 p_i) + "
        "sum_{i<j} (2 a_i a_j H_ij/(N^2 p_i p_j)) sqrt(p_i p_j)."
    ),
    "reconstruction": (
        "The aligned integer sufficient statistics and these formulas reconstruct every exact "
        "multiquadratic mean, second-moment, and centered-variance coordinate; the three stored "
        "decimals use the positive real embedding only for display."
    ),
}


def is_squarefree(value: int) -> bool:
    remaining = abs(value)
    if remaining == 0:
        return False
    prime = 2
    while prime * prime <= remaining:
        if remaining % (prime * prime) == 0:
            return False
        prime += 1
    return True


def is_fundamental_discriminant(value: int) -> bool:
    if value == 0:
        return False
    if value % 4 == 1:
        return is_squarefree(value)
    if value % 4 == 0:
        quotient = value // 4
        return quotient % 4 in {2, 3} and is_squarefree(quotient)
    return False


def fundamental_discriminants(bound: int, coprime_to: int) -> list[int]:
    if bound < 2 or coprime_to < 1:
        raise ValueError("bound must be >=2 and coprime_to positive")
    return [
        value
        for value in range(-bound, bound + 1)
        if abs(value) > 1 and gcd(value, coprime_to) == 1 and is_fundamental_discriminant(value)
    ]


def kronecker_at_prime(discriminant: int, prime: int) -> int:
    if prime < 2 or any(prime % divisor == 0 for divisor in range(2, int(sqrt(prime)) + 1)):
        raise ValueError("prime must be prime")
    if prime == 2:
        if discriminant % 2 == 0:
            return 0
        return 1 if discriminant % 8 in {1, 7} else -1
    residue = discriminant % prime
    if residue == 0:
        return 0
    symbol = pow(residue, (prime - 1) // 2, prime)
    return -1 if symbol == prime - 1 else 1


def fraction_record(value: Fraction) -> dict[str, int | str]:
    return fraction_json(value.numerator, value.denominator)


def correlation_record(prime: int, other_prime: int, value: Fraction) -> dict[str, Any]:
    return {
        "p": prime,
        "q": other_prime,
        "value": fraction_record(value),
        "absolute_value": fraction_record(abs(value)),
    }


def radical_decimal(rational: Fraction, coordinates: list[tuple[int, Fraction]]) -> str:
    value = float(rational)
    for radicand, coefficient in coordinates:
        value += coefficient.numerator / coefficient.denominator * sqrt(radicand)
    return format(value, ".12g")


def summarize_partition(
    discriminants: list[int],
    primes: list[int],
    traces: dict[int, int],
    *,
    bound: int,
    partition: str,
) -> dict[str, Any]:
    count = len(discriminants)
    if count == 0:
        raise ValueError("empty discriminant partition")
    characters = {
        prime: [kronecker_at_prime(discriminant, prime) for discriminant in discriminants]
        for prime in primes
    }
    character_sums = {prime: sum(characters[prime]) for prime in primes}
    means = {prime: Fraction(character_sums[prime], count) for prime in primes}
    densities = {
        prime: Fraction(sum(value * value for value in characters[prime]), count)
        for prime in primes
    }
    raw_correlations: list[tuple[Fraction, int, int, Fraction]] = []
    centered_correlations: list[tuple[Fraction, int, int, Fraction]] = []
    raw_numerators = [
        [
            sum(
                left * right
                for left, right in zip(characters[prime], characters[other_prime], strict=True)
            )
            for other_prime in primes
        ]
        for prime in primes
    ]
    centered_numerators = [
        [
            count * raw_numerators[row_index][column_index]
            - character_sums[prime] * character_sums[other_prime]
            for column_index, other_prime in enumerate(primes)
        ]
        for row_index, prime in enumerate(primes)
    ]
    mean_coordinates: list[tuple[int, Fraction]] = []
    second_coordinates: list[tuple[int, Fraction]] = []
    variance_coordinates: list[tuple[int, Fraction]] = []
    for prime in primes:
        coefficient = Fraction(traces[prime], prime) * means[prime]
        if coefficient:
            mean_coordinates.append((prime, coefficient))
    for index, prime in enumerate(primes):
        for other_index, other_prime in enumerate(primes[index + 1:], start=index + 1):
            raw = Fraction(raw_numerators[index][other_index], count)
            centered = Fraction(centered_numerators[index][other_index], count * count)
            raw_correlations.append((abs(raw), prime, other_prime, raw))
            centered_correlations.append((abs(centered), prime, other_prime, centered))
            second_coefficient = (
                Fraction(2 * traces[prime] * traces[other_prime], prime * other_prime)
                * raw
            )
            if second_coefficient:
                second_coordinates.append((prime * other_prime, second_coefficient))
            variance_coefficient = (
                Fraction(2 * traces[prime] * traces[other_prime], prime * other_prime)
                * centered
            )
            if variance_coefficient:
                variance_coordinates.append((prime * other_prime, variance_coefficient))
    max_raw = max(raw_correlations)
    max_centered = max(centered_correlations)
    mean_square_raw = sum((item[3] * item[3] for item in raw_correlations), Fraction()) / len(raw_correlations)
    mean_square_centered = sum(
        (item[3] * item[3] for item in centered_correlations),
        Fraction(),
    ) / len(centered_correlations)
    second_diagonal = sum(
        Fraction(traces[prime] * traces[prime], prime) * densities[prime]
        for prime in primes
    )
    variance_diagonal = sum(
        Fraction(traces[prime] * traces[prime], prime)
        * (densities[prime] - means[prime] * means[prime])
        for prime in primes
    )
    return {
        "bound": bound,
        "partition": partition,
        "discriminant_count": count,
        "first_discriminant": discriminants[0],
        "last_discriminant": discriminants[-1],
        "character_sums": [character_sums[prime] for prime in primes],
        "correlation_matrices": {
            "raw_gram": {"denominator": count, "numerators": raw_numerators},
            "centered_covariance": {
                "denominator": count * count,
                "numerators": centered_numerators,
            },
        },
        "off_diagonal": {
            "pair_count": len(raw_correlations),
            "max_absolute_raw": correlation_record(max_raw[1], max_raw[2], max_raw[3]),
            "max_absolute_centered": correlation_record(max_centered[1], max_centered[2], max_centered[3]),
            "mean_square_raw": fraction_record(mean_square_raw),
            "mean_square_centered": fraction_record(mean_square_centered),
        },
        "unitary_prime_sum": {
            "definition": "W_d=sum_{p<=43,p!=11} a_p chi_d(p)/sqrt(p)",
            "second_moment_diagonal_rational": fraction_record(second_diagonal),
            "centered_variance_diagonal_rational": fraction_record(variance_diagonal),
            "mean_decimal_display_only": radical_decimal(Fraction(), mean_coordinates),
            "second_moment_decimal_display_only": radical_decimal(
                second_diagonal, second_coordinates
            ),
            "centered_variance_decimal_display_only": radical_decimal(
                variance_diagonal, variance_coordinates
            ),
        },
    }


def build_result(source_manifest: dict[str, Any]) -> dict[str, Any]:
    record = next(item for item in source_manifest["records"] if item["curve_label"] == "11.a2")
    primes = [prime for prime in primes_up_to(PRIME_BOUND) if prime not in record["bad_primes"]]
    traces = {prime: elliptic_trace(prime, record["ainvs"]) for prime in primes}
    summaries: list[dict[str, Any]] = []
    for bound in BOUNDS:
        family = fundamental_discriminants(bound, BASE_CONDUCTOR)
        for partition, discriminants in (
            ("ALL", family),
            ("POSITIVE", [value for value in family if value > 0]),
            ("NEGATIVE", [value for value in family if value < 0]),
        ):
            summaries.append(summarize_partition(
                discriminants,
                primes,
                traces,
                bound=bound,
                partition=partition,
            ))
    return {
        "schema": "riemann.atlas.raw.twist_character_covariance.v1",
        "definition": DEFINITION,
        "base_curve": {
            "label": record["curve_label"],
            "ainvs": record["ainvs"],
            "conductor": record["conductor"],
            "excluded_bad_primes": record["bad_primes"],
        },
        "family_definition": "fundamental discriminants d with 1<|d|<=X and gcd(d,11)=1; uniform measure; no root-number split",
        "family": {
            "parameter": "fundamental_discriminant",
            "absolute_value_minimum_exclusive": 1,
            "absolute_value_bounds": BOUNDS,
            "coprime_to": BASE_CONDUCTOR,
            "measure": "UNIFORM",
            "partitions": ["ALL", "POSITIVE", "NEGATIVE"],
            "root_number_partition": "NONE",
        },
        "exact_identities": {
            "raw_gram": "G=V^T V/N for V[d,p]=chi_d(p), hence G is positive semidefinite.",
            "centered_covariance": "Cov=V^T(N I-1 1^T)V/N^2, hence Cov is positive semidefinite.",
            "moment_coordinates": "Distinct squarefree radicands are exact multiquadratic basis coordinates; decimal displays use the positive real embedding.",
        },
        "exact_coordinate_formulas": COORDINATE_FORMULAS,
        "prime_bound": PRIME_BOUND,
        "primes": primes,
        "traces": [traces[prime] for prime in primes],
        "bounds": BOUNDS,
        "summaries": summaries,
    }


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use the fixed imported 11.a2 model and omit its bad prime 11.",
        "Use primitive Kronecker characters indexed by fundamental discriminants coprime to 11.",
        "Keep ALL/POSITIVE/NEGATIVE partitions separate; none is a root-number split.",
        "Use unitary prime coefficients a_p*chi_d(p)/sqrt(p); retain exact rational and radical coordinates.",
    ]
    identity_kernel = {
        "version": 1,
        "slug": "GL2.TWIST_CHARACTER.COVARIANCE",
        "mathematical_definition": DEFINITION,
        "kernel_convention": "CUSTOM",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization,
        "contract_revision": 1,
    }
    semantic_id, identity_sha256 = semantic_identity("DETECTOR", identity_kernel["slug"], identity_kernel)
    implementation_relative = "research/l-families/atlas/core/twist_character_covariance.py"
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact finite conductor-coprime quadratic-character covariance",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "Fundamental discriminants coprime to 11 through 2048 and good primes through 43; no root-number, rank, zero, or asymptotic conclusion.",
        "supersedes": [],
        "detector_kind": "COEFFICIENT_DISPERSION",
        "mathematical_definition": DEFINITION,
        "kernel_convention": "CUSTOM",
        "central_zero_policy": "NOT_APPLICABLE",
        "required_inputs": [
            {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "required": True, "coverage_requirement": "COMPLETE"},
            {"name": "local_euler_factors", "input_type": "LOCAL_EULER_FACTORS", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
            {"name": "family_parameter", "input_type": "FAMILY_PARAMETER", "required": True, "coverage_requirement": "FINITE_COMPLETE"},
        ],
        "parameters": [
            {"name": "discriminant_bounds", "value_type": "INTEGER_LIST", "required": True, "domain": "frozen nested positive bounds", "constraints": {"nonempty": True, "unique": True, "strictly_increasing": True, "element_minimum": 2, "frozen_value": BOUNDS}},
            {"name": "prime_bound", "value_type": "INTEGER", "required": True, "domain": "frozen value 43", "constraints": {"minimum": 2, "frozen_value": PRIME_BOUND}},
            {"name": "base_conductor", "value_type": "INTEGER", "required": True, "domain": "frozen value 11", "constraints": {"minimum": 1, "frozen_value": BASE_CONDUCTOR}},
            {"name": "partition_policy", "value_type": "ENUM", "required": True, "domain": "ALL_POSITIVE_NEGATIVE", "constraints": {"enum_values": ["ALL_POSITIVE_NEGATIVE"]}},
        ],
        "normalization_requirements": [
            {"field": "lfunction_spec_bindings", "requirement": normalization[0], "comparison_role": "IDENTITY"},
            {"field": "configuration.discriminant_bounds", "requirement": normalization[1], "comparison_role": "IDENTITY"},
            {"field": "result.summaries.partition", "requirement": normalization[2], "comparison_role": "FIREWALL"},
            {"field": "result.artifact.{exact_coordinate_formulas,summaries[]}", "requirement": normalization[3], "comparison_role": "SCALING"},
        ],
        "invariances": [
            {"code": "GRAM_POSITIVITY", "statement": "The full character matrix G_X(p,q) is positive semidefinite because it is an exact finite Gram matrix.", "status": "PROVED"},
            {"code": "CENTERED_COVARIANCE_POSITIVITY", "statement": "The centered character covariance is positive semidefinite by the exact centered-scatter identity.", "status": "PROVED"},
            {"code": "DIAGONAL_LOCAL_DENSITY", "statement": "G_X(p,p) equals the exact proportion of discriminants not divisible by p.", "status": "PROVED"},
            {"code": "RADICAL_MOMENT_EXPANSION", "statement": "The unitary prime-sum mean, second moment, and centered variance have exact multiquadratic coordinates reconstructed from the aligned sufficient statistics by the declared formulas.", "status": "PROVED"},
        ],
        "family_adapters": [
            {"family": "EC11A2_CONDUCTOR_COPRIME_UNCONDITIONED_CHARACTERS", "status": "REQUIRED_AVAILABLE", "adapter_path": implementation_relative, "correction": "This is a character/coefficient family only; root numbers and central ranks are deliberately absent."},
            {"family": "EC11A2_ROOT_NUMBER_SPLIT", "status": "REQUIRED_OPEN", "adapter_path": None, "correction": "Source and verify the exact twist root-number formula before partitioning."},
        ],
        "theorem_links": [
            {"semantic_id": "TWIST-RECIPROCAL-PRIME-M2", "status": "PROPOSED", "scope": "Finite conductor-coprime unconditioned precursor; the target still needs root-number conditioning and uniform off-diagonal bounds."},
        ],
        "failure_modes": [
            {"code": "SIGN_AS_ROOT_NUMBER", "description": "Positive/negative discriminant is not the same as twist root number.", "hostile_control": "Every partition is labeled non-root-number and no epsilon is emitted."},
            {"code": "DENSITY_EQUALS_ONE", "description": "chi_d(p)^2 vanishes when p divides d.", "hostile_control": "Each raw-Gram diagonal retains the exact nonzero count; zero and signed counts reconstruct with N and the character sum."},
            {"code": "FINITE_ORTHOGONALITY_AS_LIMIT", "description": "Finite off-diagonal correlations do not prove their asymptotic cancellation.", "hostile_control": "All four bounds and the exact maximum/RMS are retained without a fitted exponent."},
            {"code": "IMPORTED_MODEL_AS_CERTIFICATE", "description": "The base Weierstrass model is imported discovery data.", "hostile_control": "The evaluation remains DISCOVERY_ONLY despite exact downstream arithmetic."},
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["MIXED"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": implementation_relative,
            "entry_point": "build_result",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / implementation_relative),
        },
        "formalization_refs": [{"state": "DEFINITION_READY", "target": "Fundamental-discriminant predicate, prime Kronecker symbol, Gram identities, and sufficient-statistic coordinate reconstruction.", "path": None}],
        "notes": "This experiment isolates the character orthogonality input to Target C before any root-number split is attempted.",
    }


def run(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    config = read_json(root / "config" / "pilot.json")
    source_relative = "research/l-families/atlas/sources/lmfdb-curves.json"
    implementation_relative = "research/l-families/atlas/core/twist_character_covariance.py"
    local_relative = "research/l-families/atlas/core/local_euler.py"
    source_manifest = read_json(root.parents[2] / source_relative)
    result = build_result(source_manifest)
    specs = []
    for path in sorted((root / "specs").glob("*.json")):
        candidate = read_json(path)
        if candidate["identity_kernel"]["slug"] == BASE_SLUG:
            specs.append(candidate)
    if len(specs) != 1:
        raise ValueError(f"expected exactly one {BASE_SLUG} spec")
    spec = specs[0]
    detector = build_detector(root)
    spec_binding = {"semantic_id": spec["semantic_id"], "record_sha256": sha256_hex(spec)}
    detector_binding = {"semantic_id": detector["semantic_id"], "record_sha256": sha256_hex(detector)}
    source_binding = artifact_binding(root, source_relative, "base_curve_source_manifest", "PARTIAL", None)
    implementation_binding = artifact_binding(root, implementation_relative, "twist_character_adapter", "FINITE_COMPLETE", None, "RAW_BYTES")
    local_binding = artifact_binding(root, local_relative, "local_trace_arithmetic", "FINITE_COMPLETE", None, "RAW_BYTES")
    adapter_bindings = [implementation_binding, local_binding]
    values = {
        "discriminant_bounds": BOUNDS,
        "prime_bound": PRIME_BOUND,
        "base_conductor": BASE_CONDUCTOR,
        "partition_policy": "ALL_POSITIVE_NEGATIVE",
    }
    fulfillments = [
        {"name": "lfunction_spec", "input_type": "LFUNCTION_SPEC", "coverage_class": "COMPLETE", "sources": [spec["semantic_id"]]},
        {"name": "local_euler_factors", "input_type": "LOCAL_EULER_FACTORS", "coverage_class": "FINITE_COMPLETE", "sources": [source_relative, local_relative]},
        {"name": "family_parameter", "input_type": "FAMILY_PARAMETER", "coverage_class": "FINITE_COMPLETE", "sources": [implementation_relative]},
    ]
    implementation_sha256 = raw_sha256(root.parents[2] / implementation_relative)
    slug = "GL2.EC11A2.FUNDAMENTAL_DISCRIMINANT.CHARACTER_COVARIANCE"
    identity_kernel = {
        "version": 1,
        "slug": slug,
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapter_bindings,
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": [source_binding["sha256"]],
        "input_fulfillments_sha256": sha256_hex(fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity("EVAL", slug, identity_kernel)
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_binding = {
        "role": "detector_result",
        "path": result_relative,
        "sha256": sha256_hex(result),
        "hash_mode": "CANONICAL_JSON_UTF8_NFC",
        "coverage_class": "FINITE_COMPLETE",
        "media_type": "application/json",
        "schema_path": RAW_RESULT_SCHEMA,
        "notes": "Exact aligned sufficient statistics reconstruct all character marginals and rational/radical coordinates; decimal fields are display-only.",
    }
    evaluation = {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact unconditioned conductor-coprime 11.a2 quadratic-character covariance through |d|<=2048",
        "revision": 1,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": "All declared fundamental discriminants coprime to 11 through 2048 and all good primes through 43; no root-number split.",
        "supersedes": [],
        "subject": {"kind": "L_FUNCTION_SET", "description": "Quadratic-character coefficient twists of the fixed 11.a2 Euler data"},
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapter_bindings,
        "configuration": {"values": values, "canonical_sha256": sha256_hex(values)},
        "evaluation_scope": "FAMILY_MOMENT",
        "input_bindings": [source_binding],
        "input_fulfillments": fulfillments,
        "arithmetic": {
            "class": "MIXED",
            "directed": False,
            "rounding_contract": "Integer sufficient statistics and rational diagonals are exact; reconstructed radical coordinates are exact; decimal moment fields are display-only binary64 conversions.",
            "serialization_contract": "Aligned integer vectors, common-denominator matrices, and reduced rational triples in canonical UTF-8 NFC JSON.",
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": "Every fundamental discriminant 1<|d|<=2048 coprime to 11, nested at four bounds, and every good prime p<=43.",
            "omissions": ["root-number split", "primes above 43", "discriminants above 2048", "central ranks", "zero ordinates", "asymptotic error bound"],
        },
        "rigor_level": "DISCOVERY_ONLY",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": "python research/l-families/atlas/core/twist_character_covariance.py --check",
            "code_commit": config["code_commit"],
            "implementation_path": implementation_relative,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "NOT_APPLICABLE",
            "artifact": result_binding,
            "summary": "Exact aligned sufficient statistics for local marginals, full character Gram/covariance matrices, and reconstructible unitary prime-sum mean, second moment, and variance coordinates at four nested bounds.",
        },
        "result_hashes": [hash_object(result_binding["sha256"], "canonical JSON twist-character covariance result", "CANONICAL_JSON_UTF8_NFC")],
        "interpretation": {
            "status": "EXACT_FINITE",
            "statement": "Given the imported 11.a2 model, the finite character covariance sufficient statistics and all coordinates reconstructed by the declared formulas are exact for the conductor-coprime unconditioned families.",
            "smallest_gap": "Source and verify the root-number partition, then prove local-density and off-diagonal estimates uniformly when the prime window grows with the discriminant bound.",
            "theorem_claim_id": None,
        },
        "assumptions": [{"code": "BASE_CURVE_MODEL_IMPORTED", "statement": "The displayed 11.a2 Weierstrass model identifies the intended base L-function.", "status": "HEURISTIC"}],
        "firewalls": [
            {"code": "NO_ROOT_SPLIT", "statement": "Discriminant sign is retained only as an archimedean partition and is never called a root number."},
            {"code": "FINITE_NOT_ASYMPTOTIC", "statement": "Four finite bounds do not prove character orthogonality or a power-saving error."},
            {"code": "CHARACTERS_NOT_ZEROS", "statement": "No central rank or zero ordinate is evaluated."},
            {"code": "DENSITY_CORRECTION_RETAINED", "statement": "The diagonal keeps chi_d(p)^2 and its p/(p+1) comparator rather than replacing it by one."},
        ],
        "notes": "This is the conductor-coprime but root-number-unconditioned coefficient-family precursor to the root-number-split theorem target, not the target itself.",
    }
    return detector, evaluation, result


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the exact finite quadratic-twist character covariance pilot.")
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument("--check", action="store_true", help="Recompute and compare without modifying checked-in artifacts.")
    args = parser.parse_args()
    root = args.root.resolve()
    detector, evaluation, result = run(root)
    detector_path = root / "detectors" / f"{detector['semantic_id']}.json"
    evaluation_path = root / "evaluations" / f"{evaluation['semantic_id']}.json"
    result_path = root.parents[2] / evaluation["result"]["artifact"]["path"]
    if args.check:
        expected = ((detector_path, detector), (evaluation_path, evaluation), (result_path, result))
        mismatches = [str(path) for path, value in expected if not path.is_file() or read_json(path) != value]
        if mismatches:
            raise SystemExit(f"twist-character covariance artifacts differ: {mismatches}")
        print("OK: exact twist-character covariance artifacts match")
        return
    write_json(detector_path, detector)
    write_json(evaluation_path, evaluation)
    write_json(result_path, result)
    print("PASS_TWIST_CHARACTER_COVARIANCE bounds=4 partitions=3 discriminants_max=1142 primes=13")


if __name__ == "__main__":
    main()

from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
from typing import Any

from atlas_core import (
    ATLAS_ROOT,
    fraction_json,
    read_json,
    semantic_identity,
    sha256_hex,
    write_json,
)
from local_euler import elliptic_trace, primes_up_to
from run_pilot import (
    artifact_binding,
    hash_object,
    make_lfunction_spec,
    programme_ref,
    raw_sha256,
)
from twist_character_covariance import (
    BOUNDS,
    COORDINATE_FORMULAS,
    PRIME_BOUND,
    fundamental_discriminants,
    is_fundamental_discriminant,
    kronecker_at_prime,
    summarize_partition,
)


BASE_CONDUCTOR = 11
FAMILY_SPEC_SLUG = "GL2.EC11A2.QUADRATIC_TWISTS.CONDUCTOR_COPRIME"
DETECTOR_SLUG = "GL2.TWIST_ROOT_NUMBER.COVARIANCE"
EVALUATION_SLUG = "GL2.EC11A2.FUNDAMENTAL_DISCRIMINANT.ROOT_NUMBER_COVARIANCE"
PARTITIONS = ("ROOT_NUMBER_PLUS", "ROOT_NUMBER_MINUS")

ROOT_NUMBER_SOURCE = "research/l-families/atlas/sources/quadratic-twist-root-number.json"
CURVE_SOURCE = "research/l-families/atlas/sources/lmfdb-curves.json"
IMPLEMENTATION = "research/l-families/atlas/core/twist_root_number_covariance.py"
SHARED_COVARIANCE_ADAPTER = "research/l-families/atlas/core/twist_character_covariance.py"
LOCAL_TRACE_ADAPTER = "research/l-families/atlas/core/local_euler.py"
RAW_RESULT_SCHEMA = (
    "research/l-families/atlas/detectors/raw-schemas/"
    "twist-root-number-covariance-result.schema.json"
)

DEFINITION = (
    "For fundamental discriminants d with 1<|d|<=X and gcd(d,11)=1, partition by the imported "
    "theorem epsilon_d=sign(d)*(d/11), then evaluate in each sign cohort the exact finite raw Gram "
    "matrix and centered covariance of chi_d(p), their exact off-diagonal Gram contrast "
    "Delta_X=G_{X,+}-G_{X,-}, the exact cross-cohort character-mean and local-density marginal "
    "contrasts, and the exact rational/multiquadratic coordinates of the 11.a2 unitary prime "
    "sum at the 13 good primes p<=43."
)

EXPECTED_COUNTS = {
    256: {"ROOT_NUMBER_PLUS": 65, "ROOT_NUMBER_MINUS": 76, "total": 141},
    512: {"ROOT_NUMBER_PLUS": 140, "ROOT_NUMBER_MINUS": 145, "total": 285},
    1024: {"ROOT_NUMBER_PLUS": 281, "ROOT_NUMBER_MINUS": 289, "total": 570},
    2048: {"ROOT_NUMBER_PLUS": 568, "ROOT_NUMBER_MINUS": 574, "total": 1142},
}

EXPECTED_GRAM_CONTRASTS = {
    256: {
        "pair": (37, 41),
        "signed_value": Fraction(-83, 247),
        "mean_square": Fraction(22556369, 1903480800),
        "rms_display": "0.108858",
        "sqrt_total_count_times_rms_display": "1.292617",
    },
    512: {
        "pair": (29, 41),
        "signed_value": Fraction(156, 1015),
        "mean_square": Fraction(398459, 91837200),
        "rms_display": "0.065869",
        "sqrt_total_count_times_rms_display": "1.112000",
    },
    1024: {
        "pair": (7, 31),
        "signed_value": Fraction(9594, 81209),
        "mean_square": Fraction(815350219, 257201165559),
        "rms_display": "0.056304",
        "sqrt_total_count_times_rms_display": "1.344228",
    },
    2048: {
        "pair": (5, 31),
        "signed_value": Fraction(3713, 40754),
        "mean_square": Fraction(3293698081, 2072788867968),
        "rms_display": "0.039862",
        "sqrt_total_count_times_rms_display": "1.347092",
    },
}

EXPECTED_MARGINAL_CONTRASTS = {
    256: {
        "character_mean": {
            "prime": 43,
            "signed_value": Fraction(129, 494),
            "mean_square": Fraction(2665799, 158623400),
            "rms_display": "0.129637",
            "sqrt_total_count_times_rms_display": "1.539358",
        },
        "local_density": {
            "prime": 5,
            "signed_value": Fraction(367, 4940),
            "mean_square": Fraction(265861, 158623400),
            "rms_display": "0.040940",
            "sqrt_total_count_times_rms_display": "0.486131",
        },
    },
    512: {
        "character_mean": {
            "prime": 43,
            "signed_value": Fraction(97, 580),
            "mean_square": Fraction(407331, 42857360),
            "rms_display": "0.097490",
            "sqrt_total_count_times_rms_display": "1.645824",
        },
        "local_density": {
            "prime": 5,
            "signed_value": Fraction(37, 1015),
            "mean_square": Fraction(8409, 30612400),
            "rms_display": "0.016574",
            "sqrt_total_count_times_rms_display": "0.279799",
        },
    },
    1024: {
        "character_mean": {
            "prime": 13,
            "signed_value": Fraction(-9714, 81209),
            "mean_square": Fraction(400113670, 85733721853),
            "rms_display": "0.068315",
            "sqrt_total_count_times_rms_display": "1.630997",
        },
        "local_density": {
            "prime": 23,
            "signed_value": Fraction(128, 4777),
            "mean_square": Fraction(15654922, 85733721853),
            "rms_display": "0.013513",
            "sqrt_total_count_times_rms_display": "0.322617",
        },
    },
    2048: {
        "character_mean": {
            "prime": 37,
            "signed_value": Fraction(-14843, 163016),
            "mean_square": Fraction(348116455, 172732405664),
            "rms_display": "0.044893",
            "sqrt_total_count_times_rms_display": "1.517080",
        },
        "local_density": {
            "prime": 23,
            "signed_value": Fraction(1677, 81508),
            "mean_square": Fraction(1809069, 13287108128),
            "rms_display": "0.011668",
            "sqrt_total_count_times_rms_display": "0.394317",
        },
    },
}


def _curve_record(curve_manifest: dict[str, Any]) -> dict[str, Any]:
    matches = [
        record
        for record in curve_manifest.get("records", [])
        if record.get("curve_label") == "11.a2"
    ]
    if len(matches) != 1:
        raise ValueError("expected exactly one 11.a2 curve-manifest record")
    record = matches[0]
    frozen = {
        "ainvs": [0, -1, 1, -10, -20],
        "conductor": 11,
        "bad_primes": [11],
        "root_number": "+1",
    }
    observed = {key: record.get(key) for key in frozen}
    if observed != frozen:
        raise ValueError(f"11.a2 source metadata drifted: {observed}")
    return record


def _validate_root_number_source(source_manifest: dict[str, Any]) -> None:
    if source_manifest.get("schema") != "riemann.atlas.source.quadratic_twist_root_number.v1":
        raise ValueError("unexpected quadratic-twist root-number source schema")
    source_keys = {source.get("key") for source in source_manifest.get("sources", [])}
    if source_keys != {"ROHRLICH_1996", "CONREY_EQ19"}:
        raise ValueError(f"unexpected root-number source keys: {source_keys}")
    specialization = source_manifest.get("specialization_11_a2", {})
    expected = {
        "base_conductor": 11,
        "imported_base_root_number": "+1",
        "formula": "epsilon_d=sign(d)*(d/11)",
    }
    observed = {key: specialization.get(key) for key in expected}
    if observed != expected:
        raise ValueError(f"11.a2 root-number specialization drifted: {observed}")


def root_number_for_discriminant(discriminant: int) -> int:
    """Return the theorem-backed 11.a2 twist sign on its exact coprime domain."""

    if not is_fundamental_discriminant(discriminant):
        raise ValueError("d must be a fundamental discriminant")
    if gcd(discriminant, BASE_CONDUCTOR) != 1:
        raise ValueError("the coprime root-number formula excludes 11 dividing d")
    sign = 1 if discriminant > 0 else -1
    symbol = kronecker_at_prime(discriminant, BASE_CONDUCTOR)
    if symbol not in {-1, 1}:
        raise ValueError("coprimality must force a nonzero Kronecker symbol")
    return sign * symbol


def root_number_partitions(bound: int) -> dict[str, list[int]]:
    if bound not in EXPECTED_COUNTS:
        raise ValueError(f"unfrozen discriminant bound: {bound}")
    family = fundamental_discriminants(bound, BASE_CONDUCTOR)
    partitions = {
        "ROOT_NUMBER_PLUS": [
            discriminant
            for discriminant in family
            if root_number_for_discriminant(discriminant) == 1
        ],
        "ROOT_NUMBER_MINUS": [
            discriminant
            for discriminant in family
            if root_number_for_discriminant(discriminant) == -1
        ],
    }
    observed = {
        "ROOT_NUMBER_PLUS": len(partitions["ROOT_NUMBER_PLUS"]),
        "ROOT_NUMBER_MINUS": len(partitions["ROOT_NUMBER_MINUS"]),
        "total": len(family),
    }
    if observed != EXPECTED_COUNTS[bound]:
        raise ValueError(f"root-number cohort counts drifted at X={bound}: {observed}")
    if sorted(partitions["ROOT_NUMBER_PLUS"] + partitions["ROOT_NUMBER_MINUS"]) != family:
        raise ValueError("root-number cohorts are not a disjoint exhaustive partition")
    return partitions


def _sqrt_decimal_display(value: Fraction, digits: int = 6) -> str:
    """Round sqrt(value) to fixed decimals using exact integer comparisons only."""

    if value < 0:
        raise ValueError("square-root display requires a nonnegative exact rational")
    if digits < 0:
        raise ValueError("display digits must be nonnegative")
    scale = 10**digits
    scaled_numerator = value.numerator * scale * scale
    floor_root = isqrt(scaled_numerator // value.denominator)
    twice_floor_plus_one = 2 * floor_root + 1
    midpoint_left = 4 * scaled_numerator
    midpoint_right = value.denominator * twice_floor_plus_one * twice_floor_plus_one
    if midpoint_left > midpoint_right or (
        midpoint_left == midpoint_right and floor_root % 2 == 1
    ):
        floor_root += 1
    if digits == 0:
        return str(floor_root)
    integer, fractional = divmod(floor_root, scale)
    return f"{integer}.{fractional:0{digits}d}"


def build_root_cohort_gram_contrast(
    summaries: list[dict[str, Any]],
    primes: list[int],
) -> dict[str, Any]:
    """Derive exact G_plus-G_minus off-diagonal summaries from aligned Gram stats."""

    by_key: dict[tuple[int, str], dict[str, Any]] = {}
    for summary in summaries:
        key = (int(summary["bound"]), str(summary["partition"]))
        if key in by_key:
            raise ValueError(f"duplicate root-cohort summary {key}")
        by_key[key] = summary
    expected_keys = {(bound, partition) for bound in BOUNDS for partition in PARTITIONS}
    if set(by_key) != expected_keys:
        raise ValueError("root-cohort summaries are not aligned at every frozen bound")

    pair_count = len(primes) * (len(primes) - 1) // 2
    if pair_count != 78:
        raise ValueError(f"expected 78 off-diagonal prime pairs, found {pair_count}")
    rows: list[dict[str, Any]] = []
    for bound in BOUNDS:
        plus = by_key[(bound, "ROOT_NUMBER_PLUS")]
        minus = by_key[(bound, "ROOT_NUMBER_MINUS")]
        plus_gram = plus["correlation_matrices"]["raw_gram"]
        minus_gram = minus["correlation_matrices"]["raw_gram"]
        plus_count = int(plus["discriminant_count"])
        minus_count = int(minus["discriminant_count"])
        if plus_gram["denominator"] != plus_count or minus_gram["denominator"] != minus_count:
            raise ValueError(f"raw Gram denominator does not match cohort count at X={bound}")

        contrasts: list[tuple[int, int, Fraction]] = []
        for left_index, left_prime in enumerate(primes):
            for right_index in range(left_index + 1, len(primes)):
                right_prime = primes[right_index]
                value = Fraction(
                    plus_gram["numerators"][left_index][right_index], plus_count
                ) - Fraction(
                    minus_gram["numerators"][left_index][right_index], minus_count
                )
                contrasts.append((left_prime, right_prime, value))
        if len(contrasts) != pair_count:
            raise ArithmeticError(f"off-diagonal pair count drifted at X={bound}")
        maximum = max(contrasts, key=lambda entry: abs(entry[2]))
        mean_square = sum((entry[2] ** 2 for entry in contrasts), Fraction()) / pair_count
        total_count = plus_count + minus_count
        rms_display = _sqrt_decimal_display(mean_square)
        scaled_rms_display = _sqrt_decimal_display(total_count * mean_square)

        expected = EXPECTED_GRAM_CONTRASTS[bound]
        observed_invariant = {
            "pair": (maximum[0], maximum[1]),
            "signed_value": maximum[2],
            "mean_square": mean_square,
            "rms_display": rms_display,
            "sqrt_total_count_times_rms_display": scaled_rms_display,
        }
        if observed_invariant != expected:
            raise ArithmeticError(
                f"root-cohort Gram contrast drifted at X={bound}: {observed_invariant}"
            )
        rows.append(
            {
                "bound": bound,
                "total_discriminant_count": total_count,
                "maximum_absolute": {
                    "p": maximum[0],
                    "r": maximum[1],
                    "signed_value": fraction_json(
                        maximum[2].numerator, maximum[2].denominator
                    ),
                    "absolute_value": fraction_json(
                        abs(maximum[2]).numerator, abs(maximum[2]).denominator
                    ),
                },
                "mean_square": fraction_json(
                    mean_square.numerator, mean_square.denominator
                ),
                "rms_decimal_display_only": rms_display,
                "sqrt_total_count_times_rms_decimal_display_only": scaled_rms_display,
            }
        )
    return {
        "definition": "Delta_X(p,r)=G_{X,+}(p,r)-G_{X,-}(p,r) for aligned good primes p<r.",
        "source": "derived only from the emitted ROOT_NUMBER_PLUS and ROOT_NUMBER_MINUS raw Gram sufficient statistics",
        "pair_count": pair_count,
        "summaries": rows,
        "firewall": (
            "The RMS displays and sqrt(N_total)-scaled displays summarize four exact finite rows; "
            "they are not a fitted decay exponent, asymptotic rate, or theorem."
        ),
    }


def _marginal_channel_record(
    *,
    bound: int,
    channel: str,
    values: list[tuple[int, Fraction]],
    total_count: int,
) -> dict[str, Any]:
    if len(values) != 13:
        raise ValueError(f"{channel} at X={bound} must contain exactly 13 prime contrasts")
    maximum = max(values, key=lambda entry: abs(entry[1]))
    mean_square = sum((value**2 for _, value in values), Fraction()) / len(values)
    rms_display = _sqrt_decimal_display(mean_square)
    scaled_rms_display = _sqrt_decimal_display(total_count * mean_square)
    expected = EXPECTED_MARGINAL_CONTRASTS[bound][channel]
    observed_invariant = {
        "prime": maximum[0],
        "signed_value": maximum[1],
        "mean_square": mean_square,
        "rms_display": rms_display,
        "sqrt_total_count_times_rms_display": scaled_rms_display,
    }
    if observed_invariant != expected:
        raise ArithmeticError(
            f"root-cohort {channel} marginal contrast drifted at X={bound}: "
            f"{observed_invariant}"
        )
    return {
        "values": [
            {
                "prime": prime,
                "signed_value": fraction_json(value.numerator, value.denominator),
            }
            for prime, value in values
        ],
        "maximum_absolute": {
            "prime": maximum[0],
            "signed_value": fraction_json(maximum[1].numerator, maximum[1].denominator),
            "absolute_value": fraction_json(
                abs(maximum[1]).numerator, abs(maximum[1]).denominator
            ),
        },
        "mean_square": fraction_json(mean_square.numerator, mean_square.denominator),
        "rms_decimal_display_only": rms_display,
        "sqrt_total_count_times_rms_decimal_display_only": scaled_rms_display,
    }


def build_root_cohort_marginal_contrast(
    summaries: list[dict[str, Any]],
    primes: list[int],
) -> dict[str, Any]:
    """Derive exact mean and local-density contrasts from emitted sufficient stats."""

    if len(primes) != 13:
        raise ValueError(f"expected 13 aligned good primes, found {len(primes)}")
    by_key: dict[tuple[int, str], dict[str, Any]] = {}
    for summary in summaries:
        key = (int(summary["bound"]), str(summary["partition"]))
        if key in by_key:
            raise ValueError(f"duplicate root-cohort summary {key}")
        by_key[key] = summary
    expected_keys = {(bound, partition) for bound in BOUNDS for partition in PARTITIONS}
    if set(by_key) != expected_keys:
        raise ValueError("root-cohort summaries are not aligned at every frozen bound")

    rows: list[dict[str, Any]] = []
    for bound in BOUNDS:
        plus = by_key[(bound, "ROOT_NUMBER_PLUS")]
        minus = by_key[(bound, "ROOT_NUMBER_MINUS")]
        plus_count = int(plus["discriminant_count"])
        minus_count = int(minus["discriminant_count"])
        total_count = plus_count + minus_count
        plus_gram = plus["correlation_matrices"]["raw_gram"]
        minus_gram = minus["correlation_matrices"]["raw_gram"]
        if plus_gram["denominator"] != plus_count or minus_gram["denominator"] != minus_count:
            raise ValueError(f"raw Gram denominator does not match cohort count at X={bound}")
        if len(plus["character_sums"]) != 13 or len(minus["character_sums"]) != 13:
            raise ValueError(f"character-sum vector is not aligned at X={bound}")

        character_mean_values = [
            (
                prime,
                Fraction(plus["character_sums"][index], plus_count)
                - Fraction(minus["character_sums"][index], minus_count),
            )
            for index, prime in enumerate(primes)
        ]
        local_density_values = [
            (
                prime,
                Fraction(plus_gram["numerators"][index][index], plus_count)
                - Fraction(minus_gram["numerators"][index][index], minus_count),
            )
            for index, prime in enumerate(primes)
        ]
        rows.append(
            {
                "bound": bound,
                "total_discriminant_count": total_count,
                "character_mean": _marginal_channel_record(
                    bound=bound,
                    channel="character_mean",
                    values=character_mean_values,
                    total_count=total_count,
                ),
                "local_density": _marginal_channel_record(
                    bound=bound,
                    channel="local_density",
                    values=local_density_values,
                    total_count=total_count,
                ),
            }
        )
    return {
        "definitions": {
            "character_mean": "s_{X,+}(p)/N_{X,+}-s_{X,-}(p)/N_{X,-}",
            "local_density": "G_{X,+}(p,p)-G_{X,-}(p,p)",
        },
        "source": (
            "derived only from emitted aligned character_sums and raw Gram diagonals; no family "
            "enumeration or new prime scan"
        ),
        "prime_count": 13,
        "primes": primes,
        "summaries": rows,
        "firewall": (
            "The marginal RMS displays and sqrt(N_total)-scaled displays summarize four exact "
            "finite rows only; they are not fitted rates, asymptotic laws, or theorems."
        ),
    }


def build_result(
    curve_manifest: dict[str, Any],
    root_number_source: dict[str, Any],
) -> dict[str, Any]:
    _validate_root_number_source(root_number_source)
    record = _curve_record(curve_manifest)
    primes = [
        prime
        for prime in primes_up_to(PRIME_BOUND)
        if prime not in record["bad_primes"]
    ]
    traces = {prime: elliptic_trace(prime, record["ainvs"]) for prime in primes}
    summaries: list[dict[str, Any]] = []
    for bound in BOUNDS:
        partitions = root_number_partitions(bound)
        for partition in PARTITIONS:
            summaries.append(
                summarize_partition(
                    partitions[partition],
                    primes,
                    traces,
                    bound=bound,
                    partition=partition,
                )
            )
    cohort_counts = [
        {"bound": bound, **EXPECTED_COUNTS[bound]}
        for bound in BOUNDS
    ]
    gram_contrast = build_root_cohort_gram_contrast(summaries, primes)
    marginal_contrast = build_root_cohort_marginal_contrast(summaries, primes)
    return {
        "schema": "riemann.atlas.raw.twist_root_number_covariance.v1",
        "definition": DEFINITION,
        "theorem_import": {
            "source_manifest": ROOT_NUMBER_SOURCE,
            "formula": "epsilon_d=epsilon(11.a2)*chi_d(-11)=sign(d)*(d/11)",
            "base_root_number": "+1",
            "hypotheses": "d fundamental, 1<|d|<=X, and gcd(d,11)=1",
            "conditionality": (
                "Partition membership is exact conditional on Rohrlich's/Conrey's imported theorem "
                "and the imported 11.a2 identification, conductor, and base sign."
            ),
        },
        "base_curve": {
            "label": record["curve_label"],
            "ainvs": record["ainvs"],
            "conductor": record["conductor"],
            "excluded_bad_primes": record["bad_primes"],
            "imported_root_number": record["root_number"],
        },
        "family_definition": (
            "fundamental discriminants d with 1<|d|<=X and gcd(d,11)=1; separate uniform "
            "ROOT_NUMBER_PLUS and ROOT_NUMBER_MINUS measures defined by sign(d)*(d/11)"
        ),
        "family": {
            "parameter": "fundamental_discriminant",
            "absolute_value_minimum_exclusive": 1,
            "absolute_value_bounds": BOUNDS,
            "coprime_to": BASE_CONDUCTOR,
            "measure": "UNIFORM_WITHIN_PARTITION",
            "partitions": list(PARTITIONS),
            "root_number_formula": "sign(d)*(d/11)",
        },
        "exact_identities": {
            "root_number_partition": (
                "Conditional on the imported sign theorem and base metadata, epsilon_d is exactly "
                "+1 or -1 and the two emitted cohorts are disjoint and exhaustive."
            ),
            "raw_gram": "Within each cohort G=V^T V/N for V[d,p]=chi_d(p), hence G is positive semidefinite.",
            "centered_covariance": (
                "Within each cohort Cov=V^T(N I-1 1^T)V/N^2, hence Cov is positive semidefinite."
            ),
            "root_cohort_gram_contrast": (
                "For every aligned p<r, Delta_X(p,r) is the exact Fraction difference of the "
                "two emitted raw Gram entries; its maximum and 78-pair mean square use no new scan."
            ),
            "root_cohort_marginal_contrast": (
                "For each aligned prime, both mean and raw-Gram-diagonal cohort differences are "
                "exact Fractions derived from emitted sufficient statistics; their 13-prime mean "
                "squares require no new scan."
            ),
            "moment_coordinates": (
                "Distinct squarefree radicands are exact multiquadratic basis coordinates; decimal "
                "displays use the positive real embedding."
            ),
        },
        "exact_coordinate_formulas": COORDINATE_FORMULAS,
        "cohort_counts": cohort_counts,
        "root_cohort_gram_contrast": gram_contrast,
        "root_cohort_marginal_contrast": marginal_contrast,
        "prime_bound": PRIME_BOUND,
        "primes": primes,
        "traces": [traces[prime] for prime in primes],
        "bounds": BOUNDS,
        "summaries": summaries,
    }


def _publication_source(
    source: dict[str, Any],
    *,
    identifier: str,
    year: str,
) -> dict[str, Any]:
    locator = source.get("stable_url", source.get("author_pdf"))
    return {
        "role": "root_number_theorem",
        "source_kind": "PUBLICATION",
        "identifier": identifier,
        "locator": locator,
        "version_or_retrieved_utc": year,
        "coverage": source["pinpoint"],
        "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM",
        "hashes": [
            hash_object(
                source["sha256_observed"],
                f"observed PDF bytes for {source['key']}",
                "RAW_BYTES",
            )
        ],
        "retention": "DURABLE_EXTERNAL",
        "notes": source["statement"],
    }


def build_lfunction_spec(
    root: Path,
    config: dict[str, Any],
    curve_manifest: dict[str, Any],
    root_number_source: dict[str, Any],
) -> dict[str, Any]:
    _validate_root_number_source(root_number_source)
    record = _curve_record(curve_manifest)
    sources_by_key = {source["key"]: source for source in root_number_source["sources"]}
    source_identifiers = [
        "ATLAS:SOURCE:LMFDB_CURVES",
        "ATLAS:SOURCE:QUADRATIC_TWIST_ROOT_NUMBER:V1",
        "CONREY:FAMILIES:EQ19",
        "LMFDB:EC:11.a2",
        "LMFDB:LFUNCTION:11.a",
        "ROHRLICH:CM:1996:PROP10_COROLLARY",
    ]
    data_sources = [
        _publication_source(
            sources_by_key["ROHRLICH_1996"],
            identifier="ROHRLICH:CM:1996:PROP10_COROLLARY",
            year="1996",
        ),
        _publication_source(
            sources_by_key["CONREY_EQ19"],
            identifier="CONREY:FAMILIES:EQ19",
            year="2005",
        ),
        {
            "role": "root_number_source_manifest",
            "source_kind": "REPOSITORY",
            "identifier": "ATLAS:SOURCE:QUADRATIC_TWIST_ROOT_NUMBER:V1",
            "locator": ROOT_NUMBER_SOURCE,
            "version_or_retrieved_utc": config["run_timestamp_utc"],
            "coverage": "Pinned theorem statements, normalizations, negative-d convention, and 11.a2 specialization.",
            "rigor_level": "RIGOROUS_GIVEN_IMPORTED_THEOREM",
            "hashes": [
                hash_object(
                    sha256_hex(root_number_source),
                    "canonical JSON quadratic-twist root-number source manifest",
                    "CANONICAL_JSON_UTF8_NFC",
                )
            ],
            "retention": "CHECKED_IN",
            "notes": "The checked-in manifest is also content-bound by the evaluation.",
        },
        {
            "role": "curve_source_manifest",
            "source_kind": "REPOSITORY",
            "identifier": "ATLAS:SOURCE:LMFDB_CURVES",
            "locator": CURVE_SOURCE,
            "version_or_retrieved_utc": config["run_timestamp_utc"],
            "coverage": "Compact 11.a2 model, conductor, bad-prime, and imported base-sign metadata.",
            "rigor_level": "DISCOVERY_ONLY",
            "hashes": [
                hash_object(
                    sha256_hex(curve_manifest),
                    "canonical JSON compact LMFDB curve manifest",
                    "CANONICAL_JSON_UTF8_NFC",
                )
            ],
            "retention": "CHECKED_IN",
            "notes": "The compact manifest does not retain the complete LMFDB responses.",
        },
        {
            "role": "curve_metadata",
            "source_kind": "DATABASE",
            "identifier": "LMFDB:EC:11.a2",
            "locator": record["api_url"],
            "version_or_retrieved_utc": record["api_response_timestamp"],
            "coverage": "Weierstrass model, conductor, and bad-prime metadata for 11.a2.",
            "rigor_level": "DISCOVERY_ONLY",
            "hashes": [
                hash_object(
                    record["api_response_sha256"],
                    "observed unretained LMFDB API response bytes",
                    "RAW_BYTES",
                )
            ],
            "retention": "DYNAMIC_EXTERNAL",
            "notes": "The response hash is an observation lock, not an independently retained certificate.",
        },
        {
            "role": "base_root_number",
            "source_kind": "DATABASE",
            "identifier": "LMFDB:LFUNCTION:11.a",
            "locator": record["lfunction_url"],
            "version_or_retrieved_utc": record["api_response_timestamp"],
            "coverage": "Imported base functional-equation sign +1.",
            "rigor_level": "DISCOVERY_ONLY",
            "hashes": [],
            "retention": "DYNAMIC_EXTERNAL",
            "notes": "The dynamic LMFDB page is identified but not archived in this packet.",
        },
    ]
    spec = make_lfunction_spec(
        slug=FAMILY_SPEC_SLUG,
        title="Conductor-coprime quadratic twists of the 11.a2 weight-2 L-function",
        programme_numbers=[738, 741],
        source_identifiers=source_identifiers,
        construction=(
            "Family d -> L_f(s,chi_d) for fundamental discriminants d with gcd(d,11)=1, "
            "where f is the weight-2 newform identified by the imported 11.a2 metadata"
        ),
        classification={
            "domain": "NUMBER_FIELD",
            "degree": 2,
            "object_type": "QUADRATIC_TWIST_L",
            "family_id": "GL2.EC11A2.FUNDAMENTAL_DISCRIMINANT.COPRIME11",
            "automorphic_class": "GL2",
            "self_duality": "SELF_DUAL",
            "symmetry_type": "ORTHOGONAL_UNSPLIT",
            "motivic_weight": 1,
        },
        base_field={"label": "Q", "characteristic": 0},
        conductor={
            "kind": "INTEGER",
            "value": "11*d^2 for fundamental discriminants d with gcd(d,11)=1",
            "status": "IMPORTED_THEOREM",
        },
        completed_normalization={
            "normalization_id": "GL2.WEIGHT2.QUADRATIC_TWIST.UNITARY.COPRIME",
            "critical_center": "1/2",
            "exact_formula": (
                "xi_d(s)=(|d|*sqrt(11)/(2*pi))^s*Gamma(s+1/2)*L_f(s,chi_d)"
            ),
            "analytic_variable": "unitary s",
            "conductor_factor": "(|d|*sqrt(11))^s",
            "gamma_factors": [
                {
                    "kind": "EXPLICIT_OTHER",
                    "shift": "1/2",
                    "multiplicity": 1,
                    "scale": "(2*pi)^(-s)",
                    "notes": "Conrey equation (19) specialized to weight k=2 and level N=11.",
                }
            ],
            "notes": (
                "The corresponding classical variable is S=s+1/2, with center S=1 and "
                "completion (|d|*sqrt(11)/(2*pi))^S*Gamma(S)*L_classical(S)."
            ),
        },
        analytic_properties={
            "analytic_continuation": "IMPORTED_THEOREM",
            "functional_equation": "IMPORTED_THEOREM",
            "euler_product": "IMPORTED_THEOREM",
            "source_ref": ROOT_NUMBER_SOURCE,
        },
        functional_equation={
            "exact_formula": (
                "xi_d(s)=epsilon(11.a2)*chi_d(-11)*xi_d(1-s), with "
                "epsilon(11.a2)=+1 and chi_d(-11)=sign(d)*(d/11)"
            ),
            "root_number": "epsilon_d=sign(d)*(d/11)",
            "root_number_status": "IMPORTED_THEOREM",
            "source_ref": ROOT_NUMBER_SOURCE,
        },
        central_data={
            "assertion": "UNKNOWN",
            "value": None,
            "rigor_level": "DISCOVERY_ONLY",
            "source_ref": "NONE",
            "parity_forced": False,
            "notes": "No central order is computed or inferred from the functional-equation sign.",
        },
        euler_product={
            "good_factor_formula": (
                "For p not dividing 11*d, L_{p,d}(S)^(-1)=1-a_p*chi_d(p)*p^(-S)+p^(1-2*S)."
            ),
            "bad_factor_policy": (
                "The covariance omits the base bad prime 11; when p divides d, chi_d(p)=0 is "
                "retained in the coefficient row and no unramified degree-two factor is asserted."
            ),
            "reciprocal_coefficient_definition": (
                "At the emitted primes, the classical first coefficient is a_p*chi_d(p), and the "
                "unitary prime-sum coordinate is a_p*chi_d(p)/sqrt(p)."
            ),
            "coverage": (
                "Exact coefficient twists at the 13 declared primes through 43, conditional on the "
                "imported 11.a2 model; not a complete memberwise Euler-product archive."
            ),
            "source_refs": [CURVE_SOURCE, SHARED_COVARIANCE_ADAPTER, LOCAL_TRACE_ADAPTER],
            "rigor_level": "DISCOVERY_ONLY",
        },
        zero_data={
            "usage": "NOT_USED",
            "coverage_class": "NOT_APPLICABLE",
            "rigor_level": "DISCOVERY_ONLY",
            "source_refs": [],
            "window": None,
            "precision": None,
            "central_zero_policy": "NOT_APPLICABLE",
        },
        data_sources=data_sources,
        software=config["software"],
        assumptions=[
            {
                "code": "BASE_CURVE_METADATA_IMPORTED",
                "statement": (
                    "The LMFDB model, conductor 11, identification with the intended newform, and "
                    "base root number +1 are imported discovery metadata."
                ),
                "status": "IMPORTED",
            },
            {
                "code": "TWIST_SIGN_THEOREM_IMPORTED",
                "statement": (
                    "Rohrlich's corollary and Conrey equation (19) are imported on the enforced "
                    "fundamental-discriminant and conductor-coprime domain."
                ),
                "status": "IMPORTED",
            },
        ],
        notes=(
            "This DRAFT family spec records the sign split only. It imports no ranks, central orders, "
            "or zeros and makes no finite-to-asymptotic inference."
        ),
        twist_parameters=["fundamental_discriminant", "gcd(d,11)=1"],
    )
    spec["scope_boundary"] = (
        "All fundamental-discriminant quadratic twists coprime to conductor 11 as a defined family; "
        "the attached evaluation is finite through |d|<=2048 and p<=43, with no rank, zero, or "
        "asymptotic conclusion."
    )
    return spec


def build_detector(root: Path) -> dict[str, Any]:
    normalization = [
        "Use Conrey's unitary weight-2 completion with center 1/2 and twist level 11*d^2.",
        "Restrict to fundamental d coprime to 11 and set epsilon_d=sign(d)*(d/11).",
        "Keep ROOT_NUMBER_PLUS and ROOT_NUMBER_MINUS as separate uniform finite measures.",
        "Omit p=11 and reuse the exact rational/multiquadratic covariance summarizer at the 13 good primes p<=43.",
        "Derive Delta_X(p,r)=G_{X,+}(p,r)-G_{X,-}(p,r) only from aligned raw Gram entries for the 78 pairs p<r.",
        "Derive the 13 character-mean and local-density contrasts only from aligned character sums and raw Gram diagonals.",
    ]
    identity_kernel = {
        "version": 1,
        "slug": DETECTOR_SLUG,
        "mathematical_definition": DEFINITION,
        "kernel_convention": "CUSTOM",
        "central_zero_policy": "NOT_APPLICABLE",
        "normalization_requirements": normalization,
        "contract_revision": 3,
    }
    semantic_id, identity_sha256 = semantic_identity(
        "DETECTOR", DETECTOR_SLUG, identity_kernel
    )
    return {
        "schema_version": "riemann.atlas.detector_contract.v1",
        "record_type": "DETECTOR_CONTRACT",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact finite 11.a2 covariance split by quadratic-twist root number",
        "revision": 3,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": (
            "Fundamental discriminants coprime to 11 through 2048 and good primes through 43, "
            "conditional on the imported twist-sign theorem and base metadata; no rank, zero, or "
            "asymptotic conclusion."
        ),
        "supersedes": [],
        "detector_kind": "COEFFICIENT_DISPERSION",
        "mathematical_definition": DEFINITION,
        "kernel_convention": "CUSTOM",
        "central_zero_policy": "NOT_APPLICABLE",
        "required_inputs": [
            {
                "name": "lfunction_spec",
                "input_type": "LFUNCTION_SPEC",
                "required": True,
                "coverage_requirement": "COMPLETE",
            },
            {
                "name": "local_euler_factors",
                "input_type": "LOCAL_EULER_FACTORS",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "family_parameter",
                "input_type": "FAMILY_PARAMETER",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "root_number",
                "input_type": "ROOT_NUMBER",
                "required": True,
                "coverage_requirement": "FINITE_COMPLETE",
            },
            {
                "name": "root_number_theorem",
                "input_type": "RAW_ARTIFACT",
                "required": True,
                "coverage_requirement": "COMPLETE",
            },
        ],
        "parameters": [
            {
                "name": "discriminant_bounds",
                "value_type": "INTEGER_LIST",
                "required": True,
                "domain": "frozen nested positive bounds",
                "constraints": {
                    "nonempty": True,
                    "unique": True,
                    "strictly_increasing": True,
                    "element_minimum": 2,
                    "frozen_value": BOUNDS,
                },
            },
            {
                "name": "prime_bound",
                "value_type": "INTEGER",
                "required": True,
                "domain": "frozen value 43",
                "constraints": {"minimum": 2, "frozen_value": PRIME_BOUND},
            },
            {
                "name": "base_conductor",
                "value_type": "INTEGER",
                "required": True,
                "domain": "frozen value 11",
                "constraints": {"minimum": 1, "frozen_value": BASE_CONDUCTOR},
            },
            {
                "name": "partition_policy",
                "value_type": "ENUM",
                "required": True,
                "domain": "ROOT_NUMBER_PLUS_MINUS",
                "constraints": {"enum_values": ["ROOT_NUMBER_PLUS_MINUS"]},
            },
        ],
        "normalization_requirements": [
            {
                "field": "lfunction_spec_bindings",
                "requirement": normalization[0],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "result.artifact.theorem_import.formula",
                "requirement": normalization[1],
                "comparison_role": "IDENTITY",
            },
            {
                "field": "result.artifact.summaries.partition",
                "requirement": normalization[2],
                "comparison_role": "COVARIANCE",
            },
            {
                "field": "result.artifact.summaries.unitary_prime_sum",
                "requirement": normalization[3],
                "comparison_role": "SCALING",
            },
            {
                "field": "result.artifact.root_cohort_gram_contrast",
                "requirement": normalization[4],
                "comparison_role": "COVARIANCE",
            },
            {
                "field": "result.artifact.root_cohort_marginal_contrast",
                "requirement": normalization[5],
                "comparison_role": "COVARIANCE",
            },
        ],
        "invariances": [
            {
                "code": "ROOT_PARTITION_EXHAUSTIVE",
                "statement": (
                    "On the coprime domain, sign(d)*(d/11) is exactly +1 or -1, so the sign "
                    "cohorts are disjoint and exhaustive."
                ),
                "status": "CONDITIONAL",
            },
            {
                "code": "GRAM_POSITIVITY",
                "statement": "Each cohort raw matrix is an exact finite Gram matrix.",
                "status": "PROVED",
            },
            {
                "code": "CENTERED_COVARIANCE_POSITIVITY",
                "statement": "Each cohort centered matrix is an exact centered-scatter covariance.",
                "status": "PROVED",
            },
            {
                "code": "RADICAL_MOMENT_EXPANSION",
                "statement": (
                    "Each cohort moment has exact rational and squarefree-radical coordinates "
                    "reconstructible from the emitted aligned sufficient statistics."
                ),
                "status": "PROVED",
            },
            {
                "code": "ROOT_COHORT_GRAM_CONTRAST",
                "statement": (
                    "Each Delta_X entry, maximum absolute contrast, and 78-pair mean square is an "
                    "exact rational derived from the two aligned emitted Gram matrices."
                ),
                "status": "PROVED",
            },
            {
                "code": "ROOT_COHORT_MARGINAL_CONTRAST",
                "statement": (
                    "Every character-mean and local-density contrast, maximum, and 13-prime mean "
                    "square is an exact rational derived from aligned emitted sufficient statistics."
                ),
                "status": "PROVED",
            },
        ],
        "family_adapters": [
            {
                "family": "EC11A2_ROOT_NUMBER_SPLIT",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": IMPLEMENTATION,
                "correction": "Applies the sourced sign formula only after fundamental-discriminant and conductor-coprimality checks.",
            },
            {
                "family": "EXACT_TWIST_CHARACTER_COVARIANCE",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": SHARED_COVARIANCE_ADAPTER,
                "correction": "Reuses the unmodified exact finite summarizer separately inside each root-number cohort.",
            },
            {
                "family": "EC11A2_LOCAL_TRACES",
                "status": "REQUIRED_AVAILABLE",
                "adapter_path": LOCAL_TRACE_ADAPTER,
                "correction": "Point-counts the declared good-prime traces from the imported Weierstrass model.",
            },
        ],
        "theorem_links": [
            {
                "semantic_id": "ROHRLICH-1996-PROP10-COROLLARY",
                "status": "VERIFIED",
                "scope": "Quadratic elliptic-curve twist root number for coprime conductor ideals.",
            },
            {
                "semantic_id": "CONREY-EQ19",
                "status": "VERIFIED",
                "scope": "Primitive newform twist level, unitary completion, and sign w_f*chi_d(-N).",
            },
        ],
        "failure_modes": [
            {
                "code": "DISCRIMINANT_SIGN_AS_ROOT_NUMBER",
                "description": "The sign of d alone omits the factor (d/11).",
                "hostile_control": "Independent tests pair positive and negative d with both residue classes modulo 11.",
            },
            {
                "code": "OVERLAPPING_CONDUCTORS",
                "description": "When 11 divides d, chi_d(-11)=0 and the coprime sign formula does not apply.",
                "hostile_control": "The family enumerator and root-number adapter reject every such d.",
            },
            {
                "code": "SIGN_AS_CENTRAL_DATA",
                "description": "A functional-equation sign is not a computed central order or zero record.",
                "hostile_control": "Central data remain UNKNOWN, zero data are NOT_USED, and the result contains neither.",
            },
            {
                "code": "FINITE_AS_ASYMPTOTIC",
                "description": "Four finite covariance tables do not prove a limiting orthogonality law.",
                "hostile_control": (
                    "The Gram and marginal contrast RMS and sqrt(N_total)-scaled RMS values are "
                    "display-only; no fit, convergence rate, or finite-to-limit claim is emitted."
                ),
            },
            {
                "code": "IMPORTED_MODEL_AS_CERTIFICATE",
                "description": "The compact LMFDB metadata do not independently certify the base object.",
                "hostile_control": "The evaluation remains DISCOVERY_ONLY while downstream finite arithmetic is labeled exact conditional on imports.",
            },
        ],
        "output_contract": {
            "representations": ["HASHED_ARTIFACT"],
            "arithmetic_classes": ["MIXED"],
            "raw_schema_path": RAW_RESULT_SCHEMA,
            "global_claim_allowed": False,
        },
        "reference_implementation": {
            "path": IMPLEMENTATION,
            "entry_point": "build_result",
            "version": "1",
            "source_sha256": raw_sha256(root.parents[2] / IMPLEMENTATION),
        },
        "formalization_refs": [
            {
                "state": "DEFINITION_READY",
                "target": (
                    "Coprime quadratic-twist sign predicate, exhaustive two-sign partition, and "
                    "exact within-cohort Gram/covariance, cross-cohort Gram-contrast, and marginal-"
                    "contrast identities."
                ),
                "path": None,
            }
        ],
        "notes": (
            "This detector conditions the existing finite character covariance on a sourced root-number "
            "predicate and derives its Gram and marginal contrasts without another scan; it does not "
            "consume or infer ranks, central orders, or zeros."
        ),
    }


def build_evaluation(
    root: Path,
    config: dict[str, Any],
    spec: dict[str, Any],
    detector: dict[str, Any],
    result: dict[str, Any],
) -> dict[str, Any]:
    spec_binding = {
        "semantic_id": spec["semantic_id"],
        "record_sha256": sha256_hex(spec),
    }
    detector_binding = {
        "semantic_id": detector["semantic_id"],
        "record_sha256": sha256_hex(detector),
    }
    adapter_bindings = [
        artifact_binding(
            root,
            IMPLEMENTATION,
            "root_number_family_adapter",
            "FINITE_COMPLETE",
            None,
            "RAW_BYTES",
        ),
        artifact_binding(
            root,
            SHARED_COVARIANCE_ADAPTER,
            "exact_covariance_summarizer",
            "FINITE_COMPLETE",
            None,
            "RAW_BYTES",
        ),
        artifact_binding(
            root,
            LOCAL_TRACE_ADAPTER,
            "local_trace_arithmetic",
            "FINITE_COMPLETE",
            None,
            "RAW_BYTES",
        ),
    ]
    source_bindings = [
        artifact_binding(
            root,
            ROOT_NUMBER_SOURCE,
            "root_number_source_manifest",
            "COMPLETE",
            None,
        ),
        artifact_binding(
            root,
            CURVE_SOURCE,
            "base_curve_source_manifest",
            "PARTIAL",
            None,
        ),
    ]
    values = {
        "discriminant_bounds": BOUNDS,
        "prime_bound": PRIME_BOUND,
        "base_conductor": BASE_CONDUCTOR,
        "partition_policy": "ROOT_NUMBER_PLUS_MINUS",
    }
    fulfillments = [
        {
            "name": "lfunction_spec",
            "input_type": "LFUNCTION_SPEC",
            "coverage_class": "COMPLETE",
            "sources": [spec["semantic_id"]],
        },
        {
            "name": "local_euler_factors",
            "input_type": "LOCAL_EULER_FACTORS",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [CURVE_SOURCE, LOCAL_TRACE_ADAPTER],
        },
        {
            "name": "family_parameter",
            "input_type": "FAMILY_PARAMETER",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [IMPLEMENTATION, SHARED_COVARIANCE_ADAPTER],
        },
        {
            "name": "root_number",
            "input_type": "ROOT_NUMBER",
            "coverage_class": "FINITE_COMPLETE",
            "sources": [IMPLEMENTATION, ROOT_NUMBER_SOURCE],
        },
        {
            "name": "root_number_theorem",
            "input_type": "RAW_ARTIFACT",
            "coverage_class": "COMPLETE",
            "sources": [ROOT_NUMBER_SOURCE],
        },
    ]
    implementation_sha256 = raw_sha256(root.parents[2] / IMPLEMENTATION)
    identity_kernel = {
        "version": 1,
        "slug": EVALUATION_SLUG,
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapter_bindings,
        "configuration_sha256": sha256_hex(values),
        "input_sha256s": sorted(binding["sha256"] for binding in source_bindings),
        "input_fulfillments_sha256": sha256_hex(fulfillments),
        "implementation_commit": config["code_commit"],
        "implementation_sha256": implementation_sha256,
        "seed": None,
    }
    semantic_id, identity_sha256 = semantic_identity(
        "EVAL", EVALUATION_SLUG, identity_kernel
    )
    result_relative = f"research/l-families/atlas/results/{semantic_id}.json"
    result_binding = {
        "role": "detector_result",
        "path": result_relative,
        "sha256": sha256_hex(result),
        "hash_mode": "CANONICAL_JSON_UTF8_NFC",
        "coverage_class": "FINITE_COMPLETE",
        "media_type": "application/json",
        "schema_path": RAW_RESULT_SCHEMA,
        "notes": (
            "Exact integer sufficient statistics reconstruct the rational/radical moments "
            "conditional on the imported root-number theorem and base metadata; decimal fields "
            "are display-only."
        ),
    }
    count_text = "; ".join(
        f"X={bound}: + {EXPECTED_COUNTS[bound]['ROOT_NUMBER_PLUS']}, "
        f"- {EXPECTED_COUNTS[bound]['ROOT_NUMBER_MINUS']}"
        for bound in BOUNDS
    )
    return {
        "schema_version": "riemann.atlas.evaluation_record.v1",
        "record_type": "EVALUATION_RECORD",
        "semantic_id": semantic_id,
        "identity_sha256": identity_sha256,
        "identity_kernel": identity_kernel,
        "title": "Exact finite 11.a2 character covariance in the two quadratic-twist root-number cohorts",
        "revision": 3,
        "record_state": "DRAFT",
        "programme_refs": [programme_ref(738), programme_ref(741)],
        "scope_boundary": (
            "Every declared conductor-coprime fundamental discriminant through 2048 and every good "
            "prime through 43, split only by the sourced root-number formula; no rank, zero, or "
            "asymptotic conclusion."
        ),
        "supersedes": [],
        "subject": {
            "kind": "L_FUNCTION_SET",
            "description": "The two root-number cohorts of conductor-coprime 11.a2 quadratic twists",
        },
        "lfunction_spec_bindings": [spec_binding],
        "detector_contract_binding": detector_binding,
        "adapter_bindings": adapter_bindings,
        "configuration": {
            "values": values,
            "canonical_sha256": sha256_hex(values),
        },
        "evaluation_scope": "FAMILY_MOMENT",
        "input_bindings": source_bindings,
        "input_fulfillments": fulfillments,
        "arithmetic": {
            "class": "MIXED",
            "directed": False,
            "rounding_contract": (
                "Cohort membership, counts, correlations, and the sufficient statistics for exact "
                "radical coefficients are exact conditional on imported theorem/base data; decimal "
                "moment fields are display-only binary64 conversions, while Gram and marginal "
                "contrast square-root displays are rounded by exact integer comparisons from "
                "rational mean squares."
            ),
            "serialization_contract": (
                "Aligned integer vectors, common-denominator matrices, reconstruction formulas, "
                "and reduced rational triples in canonical UTF-8 NFC JSON."
            ),
        },
        "coverage": {
            "class": "FINITE_COMPLETE",
            "statement": (
                "Every fundamental discriminant 1<|d|<=2048 coprime to 11, nested at four bounds, "
                "in exactly one root-number cohort, and every good prime p<=43."
            ),
            "omissions": [
                "discriminants divisible by 11",
                "nonfundamental twist parameters",
                "primes above 43",
                "discriminants above 2048",
                "ranks and central orders",
                "zero ordinates",
                "asymptotic estimates",
            ],
        },
        "rigor_level": "DISCOVERY_ONLY",
        "software": config["software"],
        "run": {
            "timestamp_utc": config["run_timestamp_utc"],
            "command": f"python {IMPLEMENTATION} --check",
            "code_commit": config["code_commit"],
            "implementation_path": IMPLEMENTATION,
            "implementation_sha256": implementation_sha256,
        },
        "central_zero_policy_applied": "NOT_APPLICABLE",
        "result": {
            "representation": "HASHED_ARTIFACT",
            "predicate_outcome": "NOT_APPLICABLE",
            "artifact": result_binding,
            "summary": (
                "Exact within-sign character Gram/covariance, cross-sign raw-Gram and marginal "
                f"contrasts, and unitary-prime-sum moment coordinates at four bounds ({count_text})."
            ),
        },
        "result_hashes": [
            hash_object(
                result_binding["sha256"],
                "canonical JSON twist root-number covariance result",
                "CANONICAL_JSON_UTF8_NFC",
            )
        ],
        "interpretation": {
            "status": "EXACT_FINITE",
            "statement": (
                "Conditional on the imported coprime twist-sign theorem and 11.a2 base metadata, "
                "all emitted cohort membership, character counts, covariance entries, and "
                "sufficient statistics reconstructing the rational/radical coordinates are exact "
                "on the declared finite domain; the cross-cohort Gram and marginal maxima and mean "
                "squares are exact derived Fractions."
            ),
            "smallest_gap": (
                "Independently archive/certify the base 11.a2 metadata and prove any desired "
                "uniform root-number-conditioned covariance estimate; neither is supplied here."
            ),
            "theorem_claim_id": None,
        },
        "assumptions": spec["assumptions"],
        "firewalls": [
            {
                "code": "COPRIME_DOMAIN_ONLY",
                "statement": "No d divisible by 11 is classified by the coprime sign formula.",
            },
            {
                "code": "NO_CENTRAL_DATA_INFERENCE",
                "statement": "Root-number labels are not converted into ranks, central orders, or zero records.",
            },
            {
                "code": "FINITE_NOT_ASYMPTOTIC",
                "statement": (
                    "The four finite bounds, decreasing RMS displays, and sqrt(N_total)-scaled "
                    "displays do not establish a limiting law or rate."
                ),
            },
            {
                "code": "IMPORTED_BASE_METADATA",
                "statement": "The evaluation remains DISCOVERY_ONLY because the compact LMFDB base metadata are not independently certified here.",
            },
            {
                "code": "BAD_PRIME_OMITTED",
                "statement": "The base bad prime 11 is excluded; zeros chi_d(p)=0 at primes dividing d remain visible.",
            },
        ],
        "notes": (
            "The source manifest, curve manifest, dedicated family spec, new sign adapter, shared "
            "covariance summarizer, and local trace adapter are all content-bound; the Gram and "
            "marginal contrasts are derived only from already-emitted aligned sufficient statistics."
        ),
    }


def run(
    root: Path = ATLAS_ROOT,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    root = root.resolve()
    config = read_json(root / "config" / "pilot.json")
    curve_manifest = read_json(root.parents[2] / CURVE_SOURCE)
    root_number_source = read_json(root.parents[2] / ROOT_NUMBER_SOURCE)
    result = build_result(curve_manifest, root_number_source)
    spec = build_lfunction_spec(root, config, curve_manifest, root_number_source)
    detector = build_detector(root)
    evaluation = build_evaluation(root, config, spec, detector, result)
    return spec, detector, evaluation, result


def _records_with_slug(directory: Path, slug: str) -> list[Path]:
    paths: list[Path] = []
    for path in sorted(directory.glob("*.json")):
        try:
            record = read_json(path)
        except (OSError, ValueError):
            continue
        if record.get("identity_kernel", {}).get("slug") == slug:
            paths.append(path)
    return paths


def _artifact_paths(
    root: Path,
    spec: dict[str, Any],
    detector: dict[str, Any],
    evaluation: dict[str, Any],
) -> tuple[Path, Path, Path, Path]:
    return (
        root / "specs" / f"{spec['semantic_id']}.json",
        root / "detectors" / f"{detector['semantic_id']}.json",
        root / "evaluations" / f"{evaluation['semantic_id']}.json",
        root.parents[2] / evaluation["result"]["artifact"]["path"],
    )


def _stale_paths(
    root: Path,
    expected_paths: tuple[Path, Path, Path, Path],
) -> list[Path]:
    expected_spec, expected_detector, expected_evaluation, _expected_result = expected_paths
    stale_specs = [
        path
        for path in _records_with_slug(root / "specs", FAMILY_SPEC_SLUG)
        if path != expected_spec
    ]
    stale_detectors = [
        path
        for path in _records_with_slug(root / "detectors", DETECTOR_SLUG)
        if path != expected_detector
    ]
    stale_evaluations = [
        path
        for path in _records_with_slug(root / "evaluations", EVALUATION_SLUG)
        if path != expected_evaluation
    ]
    expected_result = root / "results" / expected_evaluation.name
    stale_results = [
        path
        for path in sorted(
            (root / "results").glob(f"ATLAS.EVAL.{EVALUATION_SLUG}.H*.json")
        )
        if path != expected_result
    ]
    return stale_specs + stale_detectors + stale_evaluations + stale_results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ATLAS_ROOT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="recompute, require dynamic IDs to be unique, and compare without writing",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    spec, detector, evaluation, result = run(root)
    paths = _artifact_paths(root, spec, detector, evaluation)
    expected = tuple(zip(paths, (spec, detector, evaluation, result), strict=True))
    stale = _stale_paths(root, paths)
    if args.check:
        mismatches = [
            str(path)
            for path, value in expected
            if not path.is_file() or read_json(path) != value
        ]
        if stale:
            mismatches.extend(f"stale:{path}" for path in stale)
        if mismatches:
            raise SystemExit(f"twist root-number covariance artifacts differ: {mismatches}")
        print("OK: exact twist root-number covariance artifacts match; stale=0")
        return

    for path in stale:
        path.unlink()
    for path, value in expected:
        write_json(path, value)
    counts = ",".join(
        f"{bound}:+{EXPECTED_COUNTS[bound]['ROOT_NUMBER_PLUS']}/-{EXPECTED_COUNTS[bound]['ROOT_NUMBER_MINUS']}"
        for bound in BOUNDS
    )
    print(
        "PASS_TWIST_ROOT_NUMBER_COVARIANCE "
        f"spec={spec['semantic_id']} detector={detector['semantic_id']} "
        f"evaluation={evaluation['semantic_id']} counts={counts} stale_removed={len(stale)}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact bounded certificates for the native restricted Mellin projection.

Positive irrational coefficients are represented by their rational squares.
No logarithm, irrational square root, spectral fit, or asymptotic search runs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "NATIVE_RESTRICTED_MELLIN_OBSERVABILITY.md"
LOCK = HERE / "native_restricted_mellin_observability.sources.json"
FIXTURE = HERE / "native_restricted_mellin_observability.json"
TEST = ROOT / "tests" / "test_native_restricted_mellin_observability.py"
PREDECESSOR = HERE / "live_fixed_conductor_multiplicity.py"
PREDECESSOR_SHA = "9547f4cdc2c8e27a36704029fd74470de844d401"
MAX_MODES = 16
MAX_SOURCE_BYTES = 131_072
MAX_RATIONAL_BITS = 1024

SOURCE_BLOBS = {
    (
        PREDECESSOR_SHA,
        "research/riemann-structures/LIVE_FIXED_CONDUCTOR_MULTIPLICITY.md",
    ): "c9c5f9e7e1ddab7e9a6aff629165a098fdf597a8",
    (
        PREDECESSOR_SHA,
        "research/riemann-structures/FIXED_CONDUCTOR_POWER_RANK_BARRIER.md",
    ): "3348165d3f9224b7a7348d6557d358bf3ef439f2",
    (
        PREDECESSOR_SHA,
        "research/riemann-structures/live_fixed_conductor_multiplicity.py",
    ): "04f8828301ef4096973829c7df8b1f5fa186fd83",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
    ): "388c7e166a0e6e534d7e908685f71a16de246575",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106191-source-dual-centered-double-incidence-correlation.md",
    ): "85c4ef92ead7d8b235f9c195c3c0acd16d16030f",
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ): "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
    ): "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rational(value: Fraction) -> Fraction:
    require(type(value) is Fraction, "exact Fraction required")
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length())
        <= MAX_RATIONAL_BITS,
        "rational input cap",
    )
    return value


def frozen_blob(commit: str, path: str, expected: str) -> bytes:
    ref = f"{commit}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    )
    require(0 < size <= MAX_SOURCE_BYTES, "primitive source size cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(len(raw) == size, "source byte count")
    blob = sha1(b"blob " + str(size).encode("ascii") + b"\0" + raw).hexdigest()
    require(blob == expected, "primitive source blob mismatch")
    return raw


def authenticate_sources() -> list[dict[str, object]]:
    raw = LOCK.read_bytes()
    require(len(raw) <= MAX_SOURCE_BYTES, "manifest size cap")
    data = json.loads(raw)
    require(
        data.get("schema") == "riemann.structures.native_restricted_mellin.sources.v1",
        "manifest schema",
    )
    rows = data.get("sources")
    require(type(rows) is list and len(rows) == len(SOURCE_BLOBS), "source count")
    seen = set()
    checked = []
    for row in rows:
        require(type(row) is dict, "source row type")
        key = (row.get("commit"), row.get("path"))
        require(key in SOURCE_BLOBS and key not in seen, "unknown or duplicate source")
        expected = SOURCE_BLOBS[key]
        require(row.get("git_blob") == expected, "manifest blob mismatch")
        source = frozen_blob(*key, expected)
        seen.add(key)
        checked.append(
            {
                "commit": key[0],
                "path": key[1],
                "git_blob": expected,
                "bytes": len(source),
            }
        )
    require(seen == set(SOURCE_BLOBS), "source coverage")
    return checked


def load_predecessor():
    key = (PREDECESSOR_SHA, PREDECESSOR.relative_to(ROOT).as_posix())
    frozen = frozen_blob(*key, SOURCE_BLOBS[key]).replace(b"\r\n", b"\n")
    current = PREDECESSOR.read_bytes()
    require(len(current) <= MAX_SOURCE_BYTES, "predecessor size cap")
    require(current.replace(b"\r\n", b"\n") == frozen, "unreviewed predecessor code")
    spec = importlib.util.spec_from_file_location(
        "reviewed_fcm_for_mellin", PREDECESSOR
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mode_certificate(
    ratios: tuple[Fraction, ...], coefficient_squares: tuple[Fraction, ...]
) -> dict[str, object]:
    require(
        type(ratios) is tuple and type(coefficient_squares) is tuple, "mode tuple type"
    )
    require(1 <= len(ratios) <= MAX_MODES, "mode count cap")
    require(len(ratios) == len(coefficient_squares), "mode coefficient count")
    require(all(rational(r) > 0 for r in ratios), "positive ratios required")
    require(
        all(rational(c) > 0 for c in coefficient_squares),
        "nonzero positive coefficient squares required",
    )
    require(len(set(ratios)) == len(ratios), "duplicate ratio")
    ordered = tuple(sorted(ratios))
    vandermonde = Fraction(1)
    for a, b in combinations(ordered, 2):
        require(b - a > 0, "strict ratio ordering")
        vandermonde *= b - a
    require(vandermonde > 0, "nonzero rational separation certificate")
    return {
        "exact_mode_count": len(ratios),
        "sorted_rational_ratios": list(map(str, ordered)),
        "coefficient_branch": "POSITIVE_SQUARE_ROOT_OF_RECORDED_RATIONAL",
        "rational_vandermonde_surrogate": str(vandermonde),
        "surrogate_is_native_derivative_hankel": False,
        "minimal_autonomous_dimension_by_NMO_2": len(ratios),
        "logarithms_or_square_roots_evaluated": False,
    }


def collapse_rational_control(
    terms: tuple[tuple[Fraction, Fraction], ...],
) -> dict[Fraction, Fraction]:
    """Diagnostic only: repeated-frequency cancellation with rational weights."""
    require(type(terms) is tuple and len(terms) <= MAX_MODES, "control count/type")
    result = {}
    for pair in terms:
        require(type(pair) is tuple and len(pair) == 2, "control pair type")
        ratio, coefficient = map(rational, pair)
        require(ratio > 0, "positive control ratio")
        result[ratio] = result.get(ratio, Fraction(0)) + coefficient
    return {r: c for r, c in result.items() if c}


def panel_record(module, spec: dict[str, object]) -> dict[str, object]:
    inherited = module.panel_record(spec)
    g = inherited["core"]["g"]
    y = inherited["horizon"]
    count = inherited["arithmetic_count"]
    require(count <= MAX_MODES, "mode count cap")
    ratios, squares, entries = [], [], []
    for pair in inherited["arithmetic_pairs"]:
        i, j = pair["index"]
        p, q = pair["P"], pair["Q"]
        n = inherited["left"]["physical_products"][i]
        m = inherited["right"]["physical_products"][j]
        ratio = Fraction(n, m)
        require(ratio == Fraction(25 * p, 49 * q), "Mellin orientation/scaling")
        require(Fraction(10, 11) < ratio < Fraction(11, 10), "Mellin ratio window")
        # The actual positive amplitude is (2/15)/sqrt(N), not a rational surrogate.
        left_square, right_square = Fraction(4, 225 * n), Fraction(4, 225 * m)
        coefficient_square = left_square * right_square
        require(
            coefficient_square == Fraction(16, 225**2 * 35**2 * g**4 * p * q),
            "native bilateral normalization",
        )
        dual_square = (35 * g) ** 2 * coefficient_square
        require(dual_square == Fraction(16, 225**2 * g**2 * p * q), "source-dual scale")
        require(
            dual_square == 16 * Fraction(pair["history_squared_source_dual_prefactor"]),
            "four equal histories sum before squaring",
        )
        require(coefficient_square < Fraction(4, 225 * y) ** 2, "upper amplitude bound")
        require(coefficient_square > Fraction(8, 495 * y) ** 2, "lower amplitude bound")
        ratios.append(ratio)
        squares.append(coefficient_square)
        entries.append(
            {
                "index": [i, j],
                "P": p,
                "Q": q,
                "N": n,
                "M": m,
                "cell": pair["cell"],
                "ratio_N_over_M": str(ratio),
                "left_amplitude_square": str(left_square),
                "right_amplitude_square": str(right_square),
                "native_coefficient_square": str(coefficient_square),
                "source_dual_coefficient_square": str(dual_square),
                "positive_coefficient_branch_from_histories": True,
                "literal_histories_per_mode": 4,
            }
        )
    certificate = mode_certificate(tuple(ratios), tuple(squares))
    upper = Fraction(4 * count, 225 * y)
    dual_upper = 35 * g * upper
    dual_diagonal = (
        sum(
            (Fraction(e["source_dual_coefficient_square"]) for e in entries),
            Fraction(0),
        )
        / 4
    )
    require(dual_diagonal <= dual_upper**2 / 4, "literal diagonal bound")
    return {
        "name": inherited["name"],
        "horizon": y,
        "common_core": g,
        "conductors": [5, 7],
        "one_sided_boolean_history_sum": 2,
        "one_sided_equal_pair_share": "1/15",
        "entries": entries,
        "mode_certificate": certificate,
        "literal_history_count": 4 * count,
        "sum_coefficients_strict_lower": str(Fraction(8 * count, 495 * y)),
        "sum_coefficients_strict_upper": str(upper),
        "source_dual_sum_strict_upper": str(dual_upper),
        "source_dual_literal_diagonal": str(dual_diagonal),
        "wick_absolute_pointwise_upper": str(Fraction(24, 35) * dual_upper**2),
        "mellin_integral_upper_multiplier": "||kappa||_2^2",
        "complete_weighted_source_assembly_replayed": False,
    }


def controls() -> list[dict[str, object]]:
    cancelled = collapse_rational_control(
        ((Fraction(7, 5), Fraction(1)), (Fraction(7, 5), Fraction(-1)))
    )
    require(cancelled == {}, "same-frequency signed cancellation control")
    repeated_positive = collapse_rational_control(
        ((Fraction(7, 5), Fraction(1)), (Fraction(7, 5), Fraction(1)))
    )
    require(
        repeated_positive == {Fraction(7, 5): Fraction(2)}, "same-frequency collapse"
    )
    single = mode_certificate((Fraction(1),), (Fraction(4, 9),))
    return [
        {"name": "same_frequency_signed_cancellation", "literal_terms": 2, "modes": 0},
        {"name": "same_frequency_positive_aggregation", "literal_terms": 2, "modes": 1},
        {"name": "single_constant_mode", "certificate": single},
    ]


def payload() -> dict[str, object]:
    sources = authenticate_sources()
    module = load_predecessor()
    inherited_sources = module.authenticate_sources()
    panels = [panel_record(module, spec) for spec in module.PANELS]
    owned = {}
    for path in (NOTE, Path(__file__), TEST, LOCK):
        raw = path.read_bytes()
        require(len(raw) <= MAX_SOURCE_BYTES, "owned file size cap")
        owned[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    return {
        "schema": "riemann.structures.native_restricted_mellin.v1",
        "status": "EXACT_RESTRICTED_SOURCE_PROJECTION_AND_SEPARATE_PROOF",
        "reviewed_predecessor": PREDECESSOR_SHA,
        "arithmetic": {
            "class": "EXACT_RATIONAL_AND_SYMBOLIC_POSITIVE_SQUARE_ROOT",
            "rounding": "NONE",
            "native_irrational_weights_replaced": False,
        },
        "coverage": {"fixed_panels": 2, "max_modes": MAX_MODES, "searches": 0},
        "sources": sources,
        "inherited_authenticated_sources": len(inherited_sources),
        "panels": panels,
        "controls": controls(),
        "proof_boundary": {
            "constant_generator_exact_realization_only": True,
            "full_source_projection_survival_proved": False,
            "single_integrated_observation_injective": False,
            "approximate_compression_lower_bound": False,
            "global_signed_current_estimated": False,
            "all_horizon_PNT_machine_reproved": False,
            "RH": "UNPROVED",
            "GRH": "UNPROVED",
        },
        "owned_file_sha256_lf": owned,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    encoded = json.dumps(payload(), indent=2, sort_keys=True) + "\n"
    if args.write:
        FIXTURE.write_text(encoded, encoding="utf-8", newline="\n")
    else:
        stored = FIXTURE.read_bytes()
        require(len(stored) <= 1_048_576, "fixture size cap")
        require(
            stored.replace(b"\r\n", b"\n").decode("utf-8") == encoded,
            "fixture replay mismatch",
        )
    print(
        f"PASS native restricted Mellin: panels=2 sources={len(SOURCE_BLOBS)} "
        f"proof_object={sha256(encoded.encode()).hexdigest()}"
    )


if __name__ == "__main__":
    main()

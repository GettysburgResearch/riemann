from __future__ import annotations

import hashlib
import importlib.util
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_six_place_connected_saturation.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("six_place_saturation", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load six-place producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_source_lock_and_formal_six_place_identity() -> None:
    module = _load_module()
    source = module.load_locked_source()
    _require(
        source["payload_sha256"] == module.SOURCE_PAYLOAD_SHA256,
        "source payload lock drifted",
    )
    _require(
        module._git_blob(module.SOURCE, module.SOURCE_COMMIT) == module.SOURCE_BLOB,
        "source git-blob lock drifted",
    )
    formal = module.formal_six_place_raw_sum()
    _require(formal == module.EXPECTED_RAW_SUM, "formal six-place sum drifted")
    for q, trace, middle in ((7, -3, 11), (9, 5, -8), (11, 0, 17)):
        _require(
            module.evaluate_expression(formal, q, trace, middle)
            == module.raw_six_place_sum(q, trace, middle),
            f"raw sparse evaluation drifted at q={q}",
        )


def test_exact_character_and_second_power_reformulations() -> None:
    module = _load_module()
    _require(
        module.six_place_character_expansion()
        == {
            (5, 1): 1,
            (1, 1): -21,
            (4, 2): 1,
            (2, 2): -6,
            (0, 0): -21,
        },
        "six-place USp(4) character expansion drifted",
    )
    for q, trace, second_trace in ((7, 5, 3), (9, -4, 2), (11, 3, -7)):
        middle = Fraction(trace**2 - second_trace, 2)
        _require(
            module.raw_six_place_sum_from_second_power(q, trace, second_trace)
            == (q**2 - 21) * trace + (q - 6) * middle - q**2 + 6 * q - 21,
            f"second-power reformulation drifted at q={q}",
        )


def test_bell_six_partition_channels_and_multiplicities() -> None:
    module = _load_module()
    partitions = module._set_partitions(tuple(range(6)))
    _require(len(partitions) == 203, "Bell(6) drifted")
    _require(
        module.partition_profile_rows()
        == [
            {
                "profile": [2, 2, 2],
                "partition_count": 15,
                "per_partition_cumulant_coefficient": 2,
                "aggregate_coefficient_if_moments_equal": 30,
            },
            {
                "profile": [2, 4],
                "partition_count": 15,
                "per_partition_cumulant_coefficient": -1,
                "aggregate_coefficient_if_moments_equal": -15,
            },
            {
                "profile": [3, 3],
                "partition_count": 10,
                "per_partition_cumulant_coefficient": -1,
                "aggregate_coefficient_if_moments_equal": -10,
            },
            {
                "profile": [6],
                "partition_count": 1,
                "per_partition_cumulant_coefficient": 1,
                "aggregate_coefficient_if_moments_equal": 1,
            },
        ],
        "centered partition profiles drifted",
    )
    channels = module.partition_channel_index()
    _require(channels["centered_partition_count"] == 41, "centered count drifted")
    _require(len(channels["four_plus_two"]) == 15, "4+2 multiplicity drifted")
    _require(
        len(channels["three_plus_three_unordered"]) == 10,
        "3+3 multiplicity drifted",
    )
    _require(len(channels["three_pairs"]) == 15, "2+2+2 multiplicity drifted")
    _require(
        {tuple(row["quadruple"]) for row in channels["four_plus_two"]}
        == set(combinations(range(6), 4)),
        "four-subset indexing drifted",
    )


def test_closed_cumulant_equals_direct_partition_replay() -> None:
    module = _load_module()
    triples = tuple(combinations(range(6), 3))
    quadruples = tuple(combinations(range(6), 4))
    for q, full_trace, full_middle in ((7, 5, -11), (9, -7, 13)):
        triple_traces = {
            subset: ((index * index + q) % 17) - 8
            for index, subset in enumerate(triples)
        }
        quadruple_traces = {
            subset: 9 - 2 * index for index, subset in enumerate(quadruples)
        }
        direct = module.partition_connected_cumulant(
            q,
            full_trace,
            full_middle,
            triple_traces,
            quadruple_traces,
        )
        closed = module.closed_connected_cumulant(
            q,
            full_trace,
            full_middle,
            triple_traces,
            quadruple_traces,
        )
        _require(direct == closed, f"closed cumulant drifted at q={q}")


def test_hasse_envelope_coefficients_use_sharp_character_bound() -> None:
    module = _load_module()
    for q in (7, 9, 11):
        rows = module.hasse_envelope_coefficients(q)
        family_size = q**4 * (q - 1)
        pair_sum = 2 * q - 3
        _require(rows["family_size"] == family_size, f"N drifted at q={q}")
        _require(rows["pair_sum"] == pair_sum, f"C drifted at q={q}")
        _require(
            rows["raw_omega_1_sqrt_q_coefficient"]
            == Fraction(4 * (q**2 - 21), family_size),
            f"omega1 envelope drifted at q={q}",
        )
        _require(
            rows["raw_omega_2_and_constant_bound"]
            == Fraction(5 * (q**2 - 6 * q) + 21, family_size),
            f"omega2 envelope drifted at q={q}",
        )
        _require(
            rows["four_plus_two_universal_bound"]
            == Fraction(15 * pair_sum * (q**2 - 10), family_size**2),
            f"4+2 universal envelope drifted at q={q}",
        )
        _require(
            rows["four_plus_two_elliptic_sqrt_q_coefficient"]
            == Fraction(30 * pair_sum * (4 * q - 10), family_size**2),
            f"4+2 elliptic envelope drifted at q={q}",
        )
        _require(
            rows["three_plus_three_bound"]
            == Fraction(360 * q * (q - 2) ** 2, family_size**2),
            f"3+3 envelope drifted at q={q}",
        )
        _require(
            rows["pair_cube"] == Fraction(30 * pair_sum**3, family_size**3),
            f"pair-cube envelope drifted at q={q}",
        )


def test_fixed_m_weight_ceiling_top_channel_and_genus_four_notch() -> None:
    module = _load_module()
    _require(
        module.inverse_root_coefficient_envelope(6, 5) == (1, Fraction(5, 2)),
        "inverse-root envelope drifted",
    )
    _require(
        {genus: module.symplectic_top_weight_channel(genus) for genus in range(2, 7)}
        == {
            2: {1: 1},
            3: {3: 1, 1: -1},
            4: {},
            5: {3: 1, 5: -1},
            6: {3: 1, 5: -1},
        },
        "top-weight channel classification drifted",
    )
    _require(
        module.degree_five_p_coefficient_polynomials(9)
        == {1: {0: 45, 1: -9}, 3: {0: 9, 1: -1}, 5: {0: 1}},
        "odd exact p-coefficient expansion drifted",
    )
    _require(
        module.degree_five_p_coefficient_polynomials(10)
        == {
            0: {0: -55, 1: 10},
            1: {0: 55, 1: -10},
            2: {0: -10, 1: 1},
            3: {0: 10, 1: -1},
            4: {0: -1},
            5: {0: 1},
        },
        "even exact p-coefficient expansion drifted",
    )
    _require(
        module.genus_four_character_expansion(9) == {(3, 3): -9, (1, 1): -45},
        "m=9 character notch drifted",
    )
    _require(
        module.genus_four_character_expansion(10)
        == {
            (4, 4): -1,
            (3, 3): -10,
            (2, 2): -10,
            (1, 1): -55,
            (0, 0): -55,
        },
        "m=10 character notch drifted",
    )
    _require(
        {m: module.proper_partition_correction_exponent(m) for m in range(5, 10)}
        == {
            5: Fraction(15, 2),
            6: Fraction(7),
            7: Fraction(13, 2),
            8: Fraction(6),
            9: Fraction(11, 2),
        },
        "proper-partition correction exponents drifted",
    )


def test_symbolic_replays_fail_closed_outside_declared_caps() -> None:
    module = _load_module()
    refusals = (
        (lambda: module.raw_six_place_sum(5, 0, 0), "q >= 7"),
        (lambda: module._set_partitions(tuple(range(7))), "six labels"),
        (lambda: module.proper_partition_correction_exponent(10), "5<=m<=9"),
        (lambda: module.inverse_root_coefficient_envelope(4, 1), "m>=5"),
    )
    for call, fragment in refusals:
        try:
            call()
        except ValueError as error:
            _require(fragment in str(error), f"wrong cap refusal for {fragment}")
        else:
            raise AssertionError(f"symbolic replay should refuse outside {fragment}")


def test_payload_is_canonical_self_hashed_and_file_locked() -> None:
    module = _load_module()
    payload = module.build_payload()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require(payload == stored, "stored payload drifted")
    unhashed = dict(stored)
    claimed = unhashed.pop("payload_sha256")
    _require(module._canonical_sha256(unhashed) == claimed, "self-hash failed")
    for label, path in {
        "note": module.NOTE,
        "producer": module.Path(module.__file__).resolve(),
        "test": module.TEST,
    }.items():
        digest = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        _require(
            digest == stored["packet_files_lf_sha256"][label],
            f"{label} hash drifted",
        )


def test_claim_resource_and_twist_firewalls() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require(
        "fixed_m" in stored["scope"] and "six_place" in stored["scope"],
        "two-theorem scope is not explicit",
    )
    raw = stored["raw_six_place_theorem"]
    _require("chi_(omega_2)" in raw["character_formula"], "middle character missing")
    fixed = stored["fixed_m_weight_ceiling_and_genus_four_notch"]
    _require(
        "nontrivial quadratic twist" in fixed["curve_and_twist_convention"]
        and "odd character channels" in fixed["curve_and_twist_convention"],
        "odd-m twist warning missing",
    )
    _require(
        "coarse fixed-m ceiling" in fixed["firewall"]
        and "not always the leading scale" in fixed["firewall"],
        "genus-four-notch firewall missing",
    )
    boundary = " ".join(stored["claim_boundary"])
    _require("RH" in boundary and "GRH" in boundary, "RH firewall missing")
    _require("external novelty" in boundary, "novelty firewall missing")
    resources = stored["resource_contract"]
    _require(resources["distinct_source_files_read"] == 1, "source-file ledger drifted")
    _require(resources["source_git_reads"] == 1, "source-read ledger drifted")
    _require(resources["source_bytes_read"] == 10_738, "source-byte ledger drifted")
    _require(resources["set_partitions_visited"] == 203, "partition ledger drifted")
    _require(resources["maximum_set_partitions"] == 203, "partition cap drifted")
    _require(resources["finite_field_enumeration"] is False, "field gate drifted")
    _require(
        resources["extension_field_enumeration"] is False,
        "extension-field gate drifted",
    )
    _require(resources["curve_enumeration"] is False, "curve gate drifted")
    _require(resources["sampling"] is False, "sampling gate drifted")
    _require(
        resources["floating_point_arithmetic"] is False,
        "floating-point gate drifted",
    )

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
    / "quadratic_family_multiplace_l_function_identity.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("multiplace_identity", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load multi-place producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_formal_degree_five_specializations() -> None:
    module = _load_module()
    actual = {m: module.formal_degree_five_coefficient(m) for m in range(1, 6)}
    _require(actual == module.EXPECTED_FORMULAS, "formal n=5 formulas drifted")
    _require(
        all(
            b_power == 0
            for expression in actual.values()
            for (_, _, b_power) in expression
        ),
        "the genus-two middle coefficient must cancel",
    )


def test_even_character_factor_and_coefficient_kernel() -> None:
    module = _load_module()
    _require(
        module._finite_dirichlet_l_coefficients(2) == [{(0, 0, 0): 1}, {(0, 0, 0): -1}],
        "m=2 must have L=1-u",
    )
    _require(
        module._finite_dirichlet_l_coefficients(4)
        == [
            {(0, 0, 0): 1},
            {(0, 1, 0): -1, (0, 0, 0): -1},
            {(1, 0, 0): 1, (0, 1, 0): 1},
            {(1, 0, 0): -1},
        ],
        "m=4 finite L-factor must be (1-u)*(1-t*u+q*u^2)",
    )
    for m in range(1, 6):
        _require(
            module._coefficient_kernel(m, 0) == {(0, 0, 0): 1},
            f"constant kernel coefficient failed at m={m}",
        )
        _require(
            module._coefficient_kernel(m, 1) == {(0, 0, 0): m, (1, 0, 0): -1},
            f"u^2 kernel coefficient failed at m={m}",
        )


def test_direct_f5_control_checks_twist_and_infinity_conventions() -> None:
    module = _load_module()
    control = module.direct_control()
    _require(control["candidate_polynomials"] == 3_125, "candidate count drifted")
    _require(control["squarefree_members"] == 2_500, "family size drifted")
    _require(
        control["actual_family_place_evaluations"] == 12_500,
        "actual place-evaluation count drifted",
    )
    expected = {
        "1": (0, 0, 1, 0),
        "2": (0, -1, 2, 7),
        "3": (-2, 2, 1, -18),
        "4": (-2, 1, 2, -5),
        "5": (0, 0, 1, 0),
    }
    for label, (trace, affine_sum, infinity_points, family_sum) in expected.items():
        row = control["rows"][label]
        _require(row["curve_trace"] == trace, f"trace drifted at m={label}")
        _require(
            row["affine_character_sum"] == affine_sum,
            f"affine character sum drifted at m={label}",
        )
        _require(
            row["rational_points_at_infinity"] == infinity_points,
            f"infinity convention drifted at m={label}",
        )
        _require(row["family_sum"] == family_sum, f"family sum drifted at m={label}")
        _require(
            row["predicted_sum"] == family_sum,
            f"predicted sum drifted at m={label}",
        )


def test_direct_control_fails_closed_outside_declared_budget() -> None:
    module = _load_module()
    try:
        module.direct_control(q=7, places=(0, 1, 2, 3, 4))
    except ValueError as error:
        _require("q=5" in str(error), "wrong field refusal")
    else:
        raise AssertionError("q=7 direct enumeration should be unavailable")
    try:
        module.direct_control(candidate_cap=3_124)
    except RuntimeError as error:
        _require("cap" in str(error), "wrong candidate-cap refusal")
    else:
        raise AssertionError("candidate cap should fail closed")


def test_connected_cumulant_partition_skeletons() -> None:
    module = _load_module()
    expected = {
        2: {(2,): 1},
        3: {(3,): 1},
        4: {(4,): 1, (2, 2): -3},
        5: {(5,): 1, (2, 3): -10},
    }
    actual = {order: module.cumulant_partition_skeleton(order) for order in range(2, 6)}
    _require(actual == expected, "centered cumulant skeletons drifted")
    _require(
        len(module._set_partitions(tuple(range(5)))) == 52,
        "fifth Bell-number cap drifted",
    )
    pair_triples = module.five_point_pair_triple_partitions()
    _require(len(pair_triples) == 10, "five-point 2+3 partition count drifted")
    _require(
        {triple for _, triple in pair_triples} == set(combinations(range(5), 3)),
        "three-subset indexing of 2+3 partitions drifted",
    )


def test_fifth_cumulant_keeps_ten_distinct_triple_traces() -> None:
    module = _load_module()
    triples = tuple(combinations(range(5), 3))
    quadruples = tuple(combinations(range(5), 4))
    traces = {subset: index for index, subset in enumerate(triples, start=1)}
    traces.update({subset: -index for index, subset in enumerate(quadruples, start=1)})
    traces[tuple(range(5))] = 17
    rows = module.connected_cumulant_values(5, traces)
    family_size = 2_500
    pair_sum = 7
    _require(rows["kappa_2"] == Fraction(pair_sum, family_size), "kappa_2 drifted")
    for subset in triples:
        _require(
            rows["kappa_3_by_triple"][subset]
            == Fraction(9 * traces[subset], family_size),
            f"kappa_3 drifted for {subset}",
        )
    for subset in quadruples:
        expected_fourth = (
            Fraction(15 + 10 * traces[subset], family_size)
            - 3 * Fraction(pair_sum, family_size) ** 2
        )
        _require(
            rows["kappa_4_by_quadruple"][subset] == expected_fourth,
            f"kappa_4 drifted for {subset}",
        )
    triple_trace_sum = sum(range(1, 11))
    expected_fifth = Fraction(10 * 17, family_size) - Fraction(
        3 * pair_sum * 3 * triple_trace_sum, family_size**2
    )
    collapsed_wrongly = Fraction(10 * 17, family_size) - Fraction(
        3 * pair_sum * 3 * 10 * 17, family_size**2
    )
    _require(rows["triple_trace_sum"] == triple_trace_sum, "trace sum drifted")
    _require(rows["kappa_5"] == expected_fifth, "kappa_5 drifted")
    _require(
        rows["kappa_5"] != collapsed_wrongly,
        "ten triple traces were incorrectly collapsed to the five-place trace",
    )


def test_hasse_envelope_coefficients_are_exact_and_enumeration_free() -> None:
    module = _load_module()
    for q in (5, 7, 9):
        rows = module.hasse_envelope_coefficients(q)
        family_size = q**4 * (q - 1)
        pair_sum = 2 * q - 3
        _require(rows["family_size"] == family_size, f"N drifted at q={q}")
        _require(rows["pair_sum"] == pair_sum, f"C drifted at q={q}")
        _require(
            rows["kappa_2"] == Fraction(pair_sum, family_size),
            f"kappa_2 drifted at q={q}",
        )
        _require(
            rows["kappa_2_remainder_after_2q^-4"] == Fraction(-1, q**4 * (q - 1)),
            f"kappa_2 remainder drifted at q={q}",
        )
        _require(
            rows["kappa_3_sqrt_q_coefficient"] == Fraction(6 * (q - 2), family_size),
            f"kappa_3 envelope drifted at q={q}",
        )
        _require(
            rows["kappa_4_universal_remainder_after_q^-3"]
            == Fraction(q - 10, family_size),
            f"kappa_4 leading remainder drifted at q={q}",
        )
        _require(
            rows["kappa_4_trace_sqrt_q_coefficient"]
            == Fraction(2 * (4 * q - 10), family_size),
            f"kappa_4 Hasse coefficient drifted at q={q}",
        )
        _require(
            rows["kappa_4_pair_correction"]
            == Fraction(3 * pair_sum**2, family_size**2),
            f"kappa_4 pair correction drifted at q={q}",
        )
        _require(
            rows["kappa_5_primary_sqrt_q_coefficient"]
            == Fraction(4 * (q**2 - 15), family_size),
            f"kappa_5 primary envelope drifted at q={q}",
        )
        _require(
            rows["kappa_5_complement_sqrt_q_coefficient"]
            == Fraction(60 * pair_sum * (q - 2), family_size**2),
            f"kappa_5 complement envelope drifted at q={q}",
        )


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


def test_claim_and_resource_firewalls() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require(
        stored["exact_identity"]["degree_five_coefficient"]
        == "S_5,m=(binom(m+1,2)-q*m)*l_1+(m-q)*l_3+l_5",
        "general degree-five coefficient formula drifted",
    )
    boundary = " ".join(stored["claim_boundary"])
    _require("not a claimed motive" in boundary, "motive firewall missing")
    _require("RH" in boundary and "GRH" in boundary, "RH firewall missing")
    _require("No external novelty claim" in boundary, "novelty firewall missing")
    cumulants = stored["connected_joint_cumulant_corollary"]
    _require(
        cumulants["orders"]["5"]["formula"]
        == "kappa_A=(q^2-15)*t_A/N-[3*C*(q-2)/N^2]*sum_(B subset A, |B|=3) t_B",
        "fifth connected formula drifted",
    )
    _require(
        "generally differ" in cumulants["triple_trace_warning"]
        and "do not collapse" in cumulants["triple_trace_warning"],
        "triple-trace noncollapse warning missing",
    )
    envelopes = cumulants["hasse_envelopes"]
    _require(
        envelopes["kappa_2"] == "kappa_2=2*q^-4-1/[q^4*(q-1)]=2*q^-4+O(q^-5)",
        "kappa_2 Hasse/asymptotic row drifted",
    )
    _require(
        "60*C*(q-2)*sqrt(q)/N^2" in envelopes["kappa_5_exact_bound"],
        "ten-triple Hasse coefficient drifted",
    )
    _require(
        "O(q^-15/2)" in envelopes["kappa_5_asymptotic"],
        "complement-correction scale missing",
    )
    resources = stored["resource_contract"]
    _require(resources["maximum_candidate_polynomials"] == 3_125, "cap drifted")
    _require(
        resources["extension_field_enumeration"] is False, "extension gate drifted"
    )

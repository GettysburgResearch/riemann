from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_three_place_elliptic_interference.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("three_place_interference", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load three-place producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_formal_u5_coefficient_is_elliptic_trace_channel() -> None:
    module = _load_module()
    _require(
        module.formal_triple_character_coefficient() == {(1, 1): 3, (0, 1): -6},
        "formal coefficient must be 3*(q-2)*t",
    )


def test_direct_controls_match_all_exact_channels() -> None:
    module = _load_module()
    expected = {
        3: {
            "squarefree_members": 162,
            "elliptic_trace": 0,
            "triple_product_sum": 0,
            "third_defect_numerator": 0,
        },
        5: {
            "squarefree_members": 2500,
            "elliptic_trace": -2,
            "triple_product_sum": -18,
            "third_defect_numerator": -66,
        },
    }
    remaining = module.MAX_CANDIDATE_POLYNOMIALS
    for q in (3, 5):
        row = module.direct_control(q, (0, 1, 2), remaining_candidates=remaining)
        remaining -= int(row["candidate_polynomials"])
        for key, value in expected[q].items():
            _require(row[key] == value, f"{key} failed at q={q}")
    _require(remaining == 728, "shared candidate budget drifted")


def test_direct_control_refuses_outside_declared_cap() -> None:
    module = _load_module()
    try:
        module.direct_control(7, (0, 1, 3))
    except ValueError as error:
        _require("q=3 or q=5" in str(error), "wrong q=7 refusal")
    else:
        raise AssertionError("q=7 direct enumeration should be unavailable")
    try:
        module.direct_control(5, (0, 1, 2), remaining_candidates=3_124)
    except RuntimeError as error:
        _require("cap" in str(error), "wrong atom-cap refusal")
    else:
        raise AssertionError("candidate cap should fail closed")


def test_source_blob_and_payload_are_locked() -> None:
    module = _load_module()
    source = module._load_source()
    _require(
        source["payload_sha256"] == module.SOURCE_PAYLOAD,
        "source payload lock drifted",
    )
    _require(
        module._git_blob(module.SOURCE, module.SOURCE_COMMIT) == module.SOURCE_BLOB,
        "source git blob drifted",
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


def test_claim_boundary_keeps_geometry_and_rh_separate() -> None:
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    boundary = " ".join(stored["claim_boundary"])
    _require("not a motive" in boundary, "motive firewall missing")
    _require("No RH" in boundary, "RH firewall missing")
    _require(
        stored["resource_contract"]["actual_candidate_polynomials"] == 3_368,
        "resource count drifted",
    )

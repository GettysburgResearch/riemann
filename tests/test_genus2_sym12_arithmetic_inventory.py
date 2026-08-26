from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym12_arithmetic_inventory.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("genus2_sym12_inventory", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load Sym12 arithmetic-inventory producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_exact_one_scalar_closure_and_ambient_cancellation() -> None:
    module = _load_module()
    payload = module.build_fixture()
    claimed = payload.pop("payload_sha256")
    _require(claimed == _canonical_sha256(payload), "payload hash drifted")
    _require(
        payload["status"] == "PROVED_EXACT_SOURCE_RELATIVE_ONE_SCALAR_CLOSURE",
        "claim status drifted",
    )

    dependency = payload["degree_twelve_dependency"]
    _require(
        dependency["marked_open_formula"]
        == "T_(12,0)=Hhat_12-2*q-9-4*Theta_Delta-Theta_(8,2)-Theta_(10,2)",
        "marked-open formula drifted",
    )
    _require(
        dependency["minimality_certificate"]["coefficient_of_Hhat_12"] == 1,
        "central scalar coefficient drifted",
    )
    _require(
        dependency["minimality_certificate"][
            "remaining_unknown_dimension_over_the_locked_input_ring"
        ]
        == 1,
        "unknown-module dimension drifted",
    )

    _require(
        payload["cubic_channel"]["full_G3_over_q_q_minus_1"] == [],
        "cubic cancellation drifted",
    )
    _require(
        payload["quartic_channel"]["full_G4_over_q_q_minus_1"]
        == [
            {
                "Hhat_12_power": 0,
                "Theta_(10,2)_power": 0,
                "Theta_(14,2)_power": 0,
                "Theta_(8,2)_power": 0,
                "Theta_Delta_power": 1,
                "coefficient": 1,
                "q_power": 0,
            }
        ],
        "quartic channel drifted",
    )
    _require(
        payload["ambient_inventory"]["formula"]
        == "Tr(F_q,e_c(A_2(w^1),V_(12,0)))=Hhat_12+2-5*q-q*Theta_(14,Gamma0(2))(q)",
        "ambient formula drifted",
    )
    _require(
        payload["ambient_boundary"]["dimension_sum"] == 455,
        "boundary dimension drifted",
    )
    _require(
        payload["ambient_inventory"]["channel_cancellations"]
        == {
            "Theta_Delta": "-4+4=0",
            "Theta_(8,2)": "-1+1=0",
            "Theta_(10,2)": "-1+1=0",
        },
        "ambient channel cancellation drifted",
    )


def test_source_locks_and_method_firewall() -> None:
    module = _load_module()
    payload = module.build_fixture()
    manifest = {row["name"]: row for row in payload["source_manifest"]}
    _require(
        set(manifest)
        == {
            "reciprocal_boundary",
            "r6_reconnaissance",
            "sym6",
            "sym8",
            "sym10",
            "genus1",
            "marked_tower",
            "ambient_ladder",
        },
        "source manifest drifted",
    )
    _require(
        manifest["reciprocal_boundary"]["commit"].startswith("476f1f5e"),
        "reciprocal-boundary source drifted",
    )
    _require(
        manifest["sym10"]["commit"].startswith("42910253"),
        "Sym10 source drifted",
    )
    _require(
        manifest["r6_reconnaissance"]["commit"].startswith("f83f8063"),
        "R6 source drifted",
    )
    _require(
        any("not a mathematical impossibility" in row for row in payload["firewalls"]),
        "method firewall drifted",
    )
    _require(
        "does not contain chi_(12,0)"
        in payload["r6_and_ladder_boundary"]["exact_character_level_statement"],
        "character-span firewall drifted",
    )


def test_cli_normal_optimized_and_committed_fixture(tmp_path: Path) -> None:
    normal = tmp_path / "normal.json"
    optimized = tmp_path / "optimized.json"
    subprocess.run(
        [sys.executable, str(SCRIPT), "--output", str(normal)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        [sys.executable, "-O", str(SCRIPT), "--output", str(optimized)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    _require(
        normal.read_bytes() == optimized.read_bytes() == FIXTURE.read_bytes(),
        "normal, optimized, and canonical fixtures differ",
    )
    subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

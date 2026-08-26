from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_general_cyclic_resonance_no_go.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
NOTE = SCRIPT.with_name("FFPS_GENERAL_CYCLIC_RESONANCE_NO_GO.md")


def load_module():
    spec = importlib.util.spec_from_file_location("general_cyclic_resonance", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def payload() -> dict[str, object]:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))["payload"]


def test_canonical_fixture_replays() -> None:
    subprocess.run([sys.executable, str(SCRIPT), "--check"], check=True, cwd=ROOT)


def test_payload_hash_and_resource_caps() -> None:
    module = load_module()
    envelope = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert (
        envelope["payload_sha256"]
        == module.hashlib.sha256(
            module.canonical_bytes(envelope["payload"])
        ).hexdigest()
    )
    ledger = envelope["payload"]["resource_ledger"]
    assert ledger["exact_operations"] <= ledger["max_exact_operations"]
    assert ledger["subsets"] <= ledger["max_subsets"]
    assert FIXTURE.stat().st_size <= ledger["max_output_bytes"]


def test_every_exact_collision_has_forced_selected_mass() -> None:
    for row in payload()["exhaustive_summaries"]:
        order = row["order"]
        size = row["retained_size"]
        assert Fraction(row["selected_mass"]) == Fraction(order, size) - 1
        assert Fraction(row["selected_mass"]) > 0
        assert row["minimum_mode_multiplicity"] >= row["uncertainty_lower_bound"]


def test_prime_orders_have_full_geometric_multiplicity() -> None:
    for row in payload()["exhaustive_summaries"]:
        if row["order"] in {2, 3, 5, 7}:
            assert row["minimum_mode_multiplicity"] == row["order"] - 1
            assert row["maximum_mode_multiplicity"] == row["order"] - 1


def test_subgroup_masks_attain_the_uncertainty_bound() -> None:
    for row in payload()["sharp_subgroup_controls"]:
        assert row["mode_multiplicity"] == row["sharp_bound"]
        assert (
            Fraction(row["selected_mass"])
            == Fraction(row["order"], row["retained_size"]) - 1
        )


def test_arithmetic_scalar_is_separate_from_geometric_constancy() -> None:
    controls = {row["name"]: row for row in payload()["named_collision_controls"]}
    ternary = controls["ternary_two_fibre"]["collision_components"][0]
    assert ternary["selected_kernel"] == "1/2"
    assert ternary["relative_kernel"] == "1"
    octic = controls["octic_sign_null"]["collision_components"]
    exact = next(row for row in octic if row["quotient_shift"] == 0)
    sign = next(row for row in octic if row["quotient_shift"] == 4)
    assert exact["selected_kernel"] == "1"
    assert sign["selected_kernel"] == "0"
    assert exact["relative_kernel"] == sign["relative_kernel"] == "1"


def test_note_preserves_relative_and_wick_firewalls() -> None:
    note = " ".join(NOTE.read_text(encoding="utf-8").split())
    assert "Wick normal ordering subtracts those coefficients only" in note
    assert (
        "Rotation averaging removes every selected mode at the **amplitude** level"
        in note
    )
    assert "scalar-extended formal class, not automatically the class" in note
    assert "common varying-place derived complex | **NOT CONSTRUCTED**" in note
    assert "No external novelty or priority claim is made." in note

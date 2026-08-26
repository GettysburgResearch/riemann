from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym12_outer_s6_convention_gate.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "genus2_sym12_outer_s6_convention_gate", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load outer-S6 convention replay")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_murnaghan_nakayama_table_is_orthonormal() -> None:
    module = _load_module()
    for left in module.S6_IRREPS:
        assert module.character(left, (1, 1, 1, 1, 1, 1)) == module.hook_dimension(left)
        for right in module.S6_IRREPS:
            inner_product = sum(
                module.class_size(cls)
                * module.character(left, cls)
                * module.character(right, cls)
                for cls in module.S6_CLASSES
            )
            assert inner_product == math.factorial(6) * int(left == right)


def test_outer_map_is_involutive_and_preserves_sign_and_class_size() -> None:
    module = _load_module()
    for cls, image in module.OUTER_CLASS.items():
        assert module.OUTER_CLASS[image] == cls
        assert module.class_size(image) == module.class_size(cls)
        assert module.permutation_sign(image) == module.permutation_sign(cls)

    outer_irreps = module.outer_irrep_map()
    assert all(
        outer_irreps[outer_irreps[partition]] == partition for partition in outer_irreps
    )
    assert outer_irreps[(5, 1)] == (2, 2, 2)
    assert outer_irreps[(2, 1, 1, 1, 1)] == (3, 3)


def test_four_exact_s5_selectors_and_frozen_row_fingerprints() -> None:
    module = _load_module()
    expected = {
        (False, False): (["[6]", "[5,1]"], 0),
        (True, False): (["[6]", "[2,2,2]"], 1),
        (False, True): (["[2,1,1,1,1]", "[1,1,1,1,1,1]"], 2),
        (True, True): (["[3,3]", "[1,1,1,1,1,1]"], 1),
    }
    for (outer, sign_twist), (selected, projected) in expected.items():
        assert module.selector(outer=outer, sign_twist=sign_twist) == selected
        assert (
            module.projection_on_official_rows(outer=outer, sign_twist=sign_twist)
            == projected
        )


def test_canonical_packet_and_convention_conclusion() -> None:
    module = _load_module()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert module.build_packet() == stored
    assert stored["official_general_rows"]["total_S6_dimension"] == 30
    assert stored["exact_conclusion"]["official_general_fixed_dimension"] == 0
    assert stored["exact_conclusion"]["outer_counterfactual_fixed_dimension"] == 1
    assert stored["exact_conclusion"]["corrected_natural_marked_valuation_nullity"] == 0
    assert "G=0" in stored["exact_conclusion"]["stable_adapter_status"]
    assert "already closed" in stored["exact_conclusion"]["remaining_gate"]
    assert "Eisenstein" in stored["exact_conclusion"]["remaining_gate"]
    reconciliation = stored["convention_reconciliation"]
    assert reconciliation["split_root_M2_type"] == "[2,2,2]"
    assert reconciliation["Bergstrom_Clery_2025_M2_type"] == "[2,2,2]"

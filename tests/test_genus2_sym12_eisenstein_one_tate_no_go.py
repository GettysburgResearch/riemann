from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_sym12_eisenstein_one_tate_no_go.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "genus2_sym12_eisenstein_one_tate_no_go", SCRIPT
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load Sym12 Eisenstein one-Tate replay")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_four_selector_projections() -> None:
    module = _load_module()
    projections = {
        name: module.project(module.SHMAKOV_TERMS, selector)
        for name, selector in module.SELECTORS.items()
    }
    assert projections == {
        "natural_trivial": {0: 2, 1: -4},
        "outer_trivial": {0: 1, 1: -3},
        "natural_sign": {},
        "outer_sign": {0: 1, 1: -1},
    }


def test_unique_fricke_positive_difference() -> None:
    module = _load_module()
    natural = module.SELECTORS["natural_trivial"]
    shmakov = module.project(module.SHMAKOV_TERMS, natural)
    bfg = module.project(module.BFG_EXPECTED_TERMS, natural)
    assert shmakov == {0: 2, 1: -4}
    assert bfg == {0: 2, 1: -5}
    assert module.subtract(shmakov, bfg) == {1: 1}

    shmakov_positive = frozenset((module.V321, module.V42))
    bfg_positive = frozenset(module.B_PRIME)
    assert bfg_positive - shmakov_positive == frozenset((module.V51,))
    assert module.V51 in natural
    assert module.V42 not in natural
    assert module.V321 not in natural


def test_rank_specialization_and_canonical_packet() -> None:
    module = _load_module()
    payload = module.build_packet()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert payload == stored
    assert payload["BFG_expected_marked_continuation"]["virtual_rank"] == -3
    assert (
        payload["shmakov_projection_by_selector"]["natural_trivial"]["virtual_rank"]
        == -2
    )
    assert payload["no_go"]["rank_difference_Shmakov_minus_BFG"] == 1
    assert not payload["no_go"]["epsilon_zero_compatible_with_displayed_Shmakov_terms"]
    assert not payload["no_go"]["outer_or_sign_selector_reaches_BFG_2_minus_5L"]

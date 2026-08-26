from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_two_place_cumulant_defect.py"
)
FIXTURE = SCRIPT.with_suffix(".json")


def _load_module():
    spec = importlib.util.spec_from_file_location("two_place_defect", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load two-place producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _expectation(counts, total: int, fn) -> Fraction:
    return Fraction(sum(count * fn(x, y) for (x, y), count in counts.items()), total)


def test_symbolic_degree_five_coefficients() -> None:
    module = _load_module()
    _require(
        module._symbolic_coefficients()
        == {
            "A": (0, 0, 0, 0, -1, 1),
            "V": (-1, 2, -2, 2, -2, 1),
            "W": (-6, 9, -7, 5, -3, 1),
            "one_character_degree_5": (0,),
            "C": (-3, 2),
        },
        "symbolic coefficients drifted",
    )


def test_joint_law_reconstructs_all_six_basis_moments() -> None:
    module = _load_module()
    for q in (3, 5, 7, 9):
        for s in (-1, 1):
            rows = module.scalar_rows(q, s)
            counts = module.joint_counts(q, s)
            total = sum(counts.values())
            _require(total == rows["A"], f"family size failed at q={q}, s={s}")
            _require(_expectation(counts, total, lambda x, y: x) == 0, "X mean failed")
            _require(_expectation(counts, total, lambda x, y: y) == 0, "Y mean failed")
            _require(
                _expectation(counts, total, lambda x, y: x * x) == rows["v"],
                "v failed",
            )
            _require(
                _expectation(counts, total, lambda x, y: x * y) == rows["c"],
                "c failed",
            )
            _require(
                _expectation(counts, total, lambda x, y: x * x * y) == s * rows["c"],
                "x2y failed",
            )
            _require(
                _expectation(counts, total, lambda x, y: x * y * y)
                == rows["epsilon"] * s * rows["c"],
                "xy2 failed",
            )
            _require(
                _expectation(counts, total, lambda x, y: x * x * y * y) == rows["w"],
                "w failed",
            )


def test_structural_and_direct_cumulants_agree() -> None:
    module = _load_module()
    for q in (3, 5, 7, 9):
        for s in (-1, 1):
            _require(
                module.cumulant_defects(q, s) == module.structural_defects(q, s),
                f"cumulant defect mismatch at q={q}, s={s}",
            )


def test_parity_and_covariance_channels() -> None:
    module = _load_module()
    for q in (3, 7):
        defects = module.structural_defects(q)
        _require(defects[2] > 0, "covariance defect must be positive")
        _require(defects[3] == 0 and defects[5] == 0, "q=3 mod 4 parity failed")
    defects = module.structural_defects(5)
    _require(defects[2] > 0 and defects[3] > 0, "q=5 oriented channel failed")


def test_payload_is_canonical_and_self_hashed() -> None:
    module = _load_module()
    payload = module.build_payload()
    stored = json.loads(FIXTURE.read_text(encoding="utf-8"))
    _require(payload == stored, "stored payload drifted")
    digest = stored.pop("payload_sha256")
    import hashlib

    encoded = json.dumps(stored, sort_keys=True, separators=(",", ":")).encode()
    _require(hashlib.sha256(encoded).hexdigest() == digest, "payload hash failed")

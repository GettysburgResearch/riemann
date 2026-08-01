#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x15613_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def load() -> tuple[dict, bytes]:
    path = ROOT / "certificates" / "synthetic.json"
    raw = path.read_bytes()
    return json.loads(raw), raw


def raw_for(data: dict) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()


class TestSoftSchurVerifier(unittest.TestCase):
    def test_baseline(self) -> None:
        data, raw = load()
        out = MOD.verify(data, raw)
        self.assertEqual(out["verdict"], "PASS_EXACT_L15632_SOFT_SCHUR_BOUND")

    def test_rejects_non_psd_line_centered_block(self) -> None:
        data, _ = load()
        data["line_centered"]["B"] = {"numerator": "1", "denominator": "200"}
        with self.assertRaises(ValueError):
            MOD.verify(data, raw_for(data))

    def test_rejects_oversized_perturbation(self) -> None:
        data, _ = load()
        data["perturbation"]["B"] = {"numerator": "-1", "denominator": "100"}
        with self.assertRaises(ValueError):
            MOD.verify(data, raw_for(data))

    def test_rejects_epsilon_touching_h(self) -> None:
        data, _ = load()
        data["epsilon"] = {"numerator": "1", "denominator": "1"}
        with self.assertRaises(ValueError):
            MOD.verify(data, raw_for(data))

    def test_rejects_wrong_declared_square_root(self) -> None:
        data, _ = load()
        data["sqrt_ell_over_h"] = {"numerator": "2", "denominator": "1"}
        with self.assertRaises(ValueError):
            MOD.verify(data, raw_for(data))

    def test_rejects_destroyed_actual_coercivity(self) -> None:
        data, _ = load()
        data["perturbation"]["C"] = {"numerator": "-1", "denominator": "1"}
        with self.assertRaises(ValueError):
            MOD.verify(data, raw_for(data))


if __name__ == "__main__":
    unittest.main()

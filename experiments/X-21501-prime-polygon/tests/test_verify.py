from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x21501_verify", HERE / "verify.py")
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class PrimePolygonVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads((HERE / "certificates" / "synthetic.json").read_text())

    def test_synthetic_violation(self) -> None:
        out = mod.verify(copy.deepcopy(self.base))
        self.assertEqual(out["verdict"], "SYNTHETIC_POSITIVE_TANGENT_WITNESS")
        self.assertGreater(mod.q(out["witness_interval"]["lower"], "lower"), 0)

    def test_large_B_removes_violation(self) -> None:
        data = copy.deepcopy(self.base)
        data["B_prefix"] = {"lower": "100", "upper": "100"}
        out = mod.verify(data)
        self.assertEqual(out["verdict"], "NO_VIOLATION_AT_THIS_TRIAL_TANGENT")

    def test_reversed_interval_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["log_r"] = {"lower": "1", "upper": "0"}
        with self.assertRaises(mod.CertificateError):
            mod.verify(data)

    def test_small_radius_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["trial_r"] = "7/5"
        with self.assertRaises(mod.CertificateError):
            mod.verify(data)

    def test_negative_series_count_rejected(self) -> None:
        data = copy.deepcopy(self.base)
        data["series_terms"] = -1
        with self.assertRaises(mod.CertificateError):
            mod.verify(data)

    def test_directed_requires_bindings(self) -> None:
        data = copy.deepcopy(self.base)
        data["classification"] = "RIEMANN_DIRECTED"
        with self.assertRaises(mod.CertificateError):
            mod.verify(data)

    def test_directed_accepts_typed_bindings(self) -> None:
        data = copy.deepcopy(self.base)
        data["classification"] = "RIEMANN_DIRECTED"
        data["prefix_binding"] = {
            "complete_through_prime_power": 16,
            "manifest_sha256": "1" * 64,
            "transcendental_producer_sha256": "2" * 64,
            "constant_source_sha256": "3" * 64
        }
        out = mod.verify(data)
        self.assertEqual(out["verdict"], "CERTIFIED_RH_FALSE_PRIME_POLYGON_TANGENT")


if __name__ == "__main__":
    unittest.main()

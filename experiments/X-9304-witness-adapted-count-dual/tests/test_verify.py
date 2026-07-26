from __future__ import annotations
import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x9304_verify", ROOT / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
CERT = ROOT / "certificates" / "synthetic.json"

class WitnessAdaptedDualTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text())

    def test_strict_synthetic_separation(self):
        result = MODULE.verify(self.load())
        statuses = {row["id"]: row["status"] for row in result["rows"]}
        self.assertEqual(result["verdict"], "SYNTHETIC_STRICT_SEPARATION")
        self.assertEqual(statuses["raw-log-monotonicity"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["coarse-count-deflation"], "CERTIFIED_NONNEGATIVE")
        self.assertEqual(statuses["witness-adapted-dual-deflation"], "CERTIFIED_NEGATIVE")
        self.assertEqual(result["dual_objective"], {"numerator": 17, "denominator": 6})

    def test_bad_dual_rejected(self):
        data = self.load()
        data["dual"]["lambdas"][0] = {"numerator": 1, "denominator": 3}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_bad_primal_rejected(self):
        data = self.load()
        data["primal"]["atom_counts"][0] = 0
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_unsafe_cell_cost_rejected(self):
        data = self.load()
        data["cell_cost_lower_bounds"][0] = {"numerator": 17, "denominator": 50}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_wrong_gate_rejected(self):
        data = self.load()
        data["count_windows"][0]["gate"] = "HARDY_SIGN_CHANGES_ONLY"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_count_rejected(self):
        data = self.load()
        data["count_windows"][0]["count"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_overlapping_atoms_rejected(self):
        data = self.load()
        data["atoms"][1]["lower_offset"] = {"numerator": -3, "denominator": 1}
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

if __name__ == "__main__":
    unittest.main()

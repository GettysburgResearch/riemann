from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("zero_deflation_verify", ROOT / "verify.py")
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)


class Tests(unittest.TestCase):
    def load(self, name):
        return json.loads((ROOT / "certificates" / name).read_text())

    def test_hidden_scalar(self):
        result = mod.verify(self.load("synthetic-hidden-offline-scalar.json"))
        self.assertEqual(result["status"], "CERTIFIED_NEGATIVE_DEFLATED_WITNESS")
        self.assertEqual(result["residual_interval"], {"lower": "-10/3", "upper": "-10/3"})

    def test_online_scalar(self):
        result = mod.verify(self.load("synthetic-online-scalar-control.json"))
        self.assertEqual(result["status"], "CERTIFIED_NONNEGATIVE_CONTROL")

    def test_hidden_pick(self):
        result = mod.verify(self.load("synthetic-hidden-offline-pick.json"))
        self.assertEqual(result["base_rayleigh_interval"], {"lower": "400/3", "upper": "400/3"})
        self.assertEqual(result["subtracted_lower"], "400")
        self.assertEqual(result["residual_interval"], {"lower": "-800/3", "upper": "-800/3"})

    def test_overlap_rejected(self):
        payload = self.load("synthetic-hidden-offline-scalar.json")
        payload["zero_bins"].append(
            {"id": "dup", "lower": "0", "upper": "1/10", "count": 1, "gate_id": "synthetic-zero-count"}
        )
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)

    def test_bad_count_rejected(self):
        payload = self.load("synthetic-hidden-offline-scalar.json")
        payload["zero_bins"][0]["count"] = 0
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)

    def test_blocking_gate_rejected(self):
        payload = self.load("synthetic-hidden-offline-scalar.json")
        payload["logical_gates"][0]["state"] = "PROPOSED"
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)

    def test_false_claim_rejected(self):
        payload = self.load("synthetic-hidden-offline-scalar.json")
        payload["claimed_interval"]["upper"] = "-3"
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)

    def test_vector_mutation_rejected_by_claim(self):
        payload = self.load("synthetic-hidden-offline-pick.json")
        payload["vector"][0]["re"] = "2"
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)

    def test_boolean_rejected(self):
        payload = self.load("synthetic-hidden-offline-scalar.json")
        payload["zero_bins"][0]["count"] = True
        with self.assertRaises(mod.CertificateError):
            mod.verify(payload)


if __name__ == "__main__":
    unittest.main()

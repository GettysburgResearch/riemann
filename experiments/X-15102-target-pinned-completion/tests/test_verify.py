from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("target_completion_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)

CERTIFICATE = ROOT / "certificates" / "synthetic-exact.json"


class TargetPinnedCompletionTests(unittest.TestCase):
    def payload(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_exact_completion(self):
        result = module.verify(self.payload())
        self.assertEqual(
            result["classification"], "EXACT_TARGET_PINNED_GRAPH_SOS"
        )
        self.assertEqual(result["diagonal_completion"], ["5", "3", "5"])
        self.assertEqual(
            result["completed_matrix"],
            [["3", "-1", "-1"], ["-1", "1", "-1"], ["-1", "-1", "3"]],
        )
        self.assertEqual(result["updated_beta"], ["1", "0", "-1"])
        self.assertEqual(result["positive_edge_count"], 3)

    def test_boundary_normalization_rejected(self):
        payload = self.payload()
        payload["target"][1] = "1/3"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_zero_target_coordinate_rejected(self):
        payload = self.payload()
        payload["target"][0] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_false_input_commutator_rejected(self):
        payload = self.payload()
        payload["beta"][0] = -2
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_negative_edge_rejected(self):
        payload = self.payload()
        payload["c"] = 0
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_disconnected_graph_rejected(self):
        payload = self.payload()
        payload["c"] = 1
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_parity_drift_rejected(self):
        payload = self.payload()
        payload["target"][2] = "1/5"
        payload["target"][1] = "11/20"
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_boolean_rejected(self):
        payload = self.payload()
        payload["frequencies"][0] = True
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_nonsymmetric_matrix_rejected(self):
        payload = self.payload()
        payload["weil_matrix"][0][1] = 2
        with self.assertRaises(module.CertificateError):
            module.verify(payload)

    def test_digest_deterministic(self):
        first = module.verify(self.payload())
        second = module.verify(copy.deepcopy(self.payload()))
        self.assertEqual(
            first["exact_proof_object_sha256"], second["exact_proof_object_sha256"]
        )


if __name__ == "__main__":
    unittest.main()

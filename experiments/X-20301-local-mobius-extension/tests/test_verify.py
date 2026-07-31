from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20301_verify", HERE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestLocalMobiusExtension(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads((HERE / "certificates" / "synthetic.json").read_text())

    def verify(self, data):
        return MODULE.verify(copy.deepcopy(data))

    def assert_rejected(self, data):
        with self.assertRaises(MODULE.VerificationError):
            self.verify(data)

    def test_baseline(self):
        result = self.verify(self.certificate)
        self.assertTrue(result["verified"])
        self.assertEqual(result["verdict"], "CERTIFIED_EXACT_LOCAL_MOBIUS_RADICAL_EXTENSION")
        self.assertEqual(result["source_integral"], {"numerator": 0, "denominator": 1})

    def test_cutoff_too_small(self):
        data = copy.deepcopy(self.certificate)
        data["N"] = 2
        self.assert_rejected(data)

    def test_psi_integral_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["psi_intervals"][0]["value"] = "3/2"
        self.assert_rejected(data)

    def test_tail_sample_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["tail_samples"][0]["expected_tail"] = "-3"
        self.assert_rejected(data)

    def test_visible_evaluation_singular(self):
        data = copy.deepcopy(self.certificate)
        data["graph_control"]["evaluation_W"] = "0"
        self.assert_rejected(data)

    def test_graph_kernel_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["graph_control"]["expected_kernel_vector"][1] = "-1/5"
        self.assert_rejected(data)

    def test_target_support_escape(self):
        data = copy.deepcopy(self.certificate)
        data["g_intervals"][0]["left"] = "3/2"
        self.assert_rejected(data)

    def test_boolean_rejected(self):
        data = copy.deepcopy(self.certificate)
        data["N"] = True
        self.assert_rejected(data)

    def test_formal_zero_sign_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["formal_zero_control"]["expected_tail_evaluation"] = "7/5"
        self.assert_rejected(data)


if __name__ == "__main__":
    unittest.main()

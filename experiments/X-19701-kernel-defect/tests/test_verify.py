#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_x19701", ROOT / "verify.py")
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)

GOOD = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class KernelDefectTests(unittest.TestCase):
    def check_bad(self, mutate):
        data = copy.deepcopy(GOOD)
        data.pop("proof_object_sha256", None)
        mutate(data)
        with self.assertRaises((V.VerificationError, KeyError)):
            V.verify(data)

    def test_good(self):
        out = V.verify(copy.deepcopy(GOOD))
        self.assertTrue(out["verified"])
        self.assertEqual(out["corrected_offline_rayleigh"], {"numerator": -17, "denominator": 16})
        self.assertEqual(out["line_only_schur_floor"], {"numerator": 31, "denominator": 16})

    def test_reject_nonpositive_complement(self):
        self.check_bad(lambda d: d.__setitem__("complement_block", [[{"numerator": 0, "denominator": 1}]]))

    def test_reject_wrong_signature_block(self):
        self.check_bad(lambda d: d["offline_kernel_block"][0].__setitem__(1, {"numerator": 2, "denominator": 1}))

    def test_reject_visible_offline_witness(self):
        self.check_bad(lambda d: d["selected_real_evaluation"][0].__setitem__(0, {"numerator": 1, "denominator": 1}))

    def test_reject_zero_witness(self):
        self.check_bad(lambda d: d.__setitem__("offline_witness", [0, 0]))

    def test_reject_nonpositive_line_control(self):
        self.check_bad(lambda d: d.__setitem__("line_only_kernel_block", [[0, 0], [0, 0]]))

    def test_reject_forged_corrected_value(self):
        self.check_bad(lambda d: d.__setitem__("expected_corrected_offline_quadratic", {"numerator": -2, "denominator": 1}))

    def test_reject_boolean_rational(self):
        self.check_bad(lambda d: d["kernel_metric"][0].__setitem__(0, True))

    def test_reject_cross_dimension_drift(self):
        self.check_bad(lambda d: d.__setitem__("kernel_complement_cross", [[0]]))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(verify)
BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class CardinalRadicalTests(unittest.TestCase):
    def test_exact_control_passes(self):
        out = verify.verify(copy.deepcopy(BASE))
        self.assertEqual(out["verdict"], "PASS")
        self.assertEqual(out["C_tilde"], [["1"], ["0"], ["1/8"], ["0"]])
        self.assertEqual(out["K"], [["0"], ["1"], ["19/160"], ["0"]])

    def test_rejects_false_cardinal_identity(self):
        x = copy.deepcopy(BASE)
        x["C"][0][0] = "2"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_nonradical_source(self):
        x = copy.deepcopy(BASE)
        x["R"][2][0] = "1/100"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_singular_evaluation_repair(self):
        x = copy.deepcopy(BASE)
        x["P"][0][0] = "0"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_false_kernel_repair_by_mutated_V(self):
        x = copy.deepcopy(BASE)
        x["V"][0][1] = "1"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_insufficient_floor(self):
        x = copy.deepcopy(BASE)
        x["claimed_schur_floor_loss"] = "1/63"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_nonpositive_complement(self):
        x = copy.deepcopy(BASE)
        x["Q"][3][3] = "-2"
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)

    def test_rejects_boolean_fraction(self):
        x = copy.deepcopy(BASE)
        x["Q"][0][0] = True
        with self.assertRaises(verify.VerificationError):
            verify.verify(x)


if __name__ == "__main__":
    unittest.main()

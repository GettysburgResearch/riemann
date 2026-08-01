#!/usr/bin/env python3
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)

CERT = json.loads((ROOT / "certificates/synthetic.json").read_text())


class TestVerifier(unittest.TestCase):
    def test_pass(self):
        out = verify.verify(copy.deepcopy(CERT))
        self.assertEqual(
            out["verdict"],
            "CERTIFIED_HARMONIC_TRIAL_ERASURE_AND_NEGATIVE_CHANNEL_UPDATE",
        )
        self.assertEqual(out["actual_source_schur_direct"], "-7394941/7329456")

    def test_bad_schema(self):
        cert = copy.deepcopy(CERT)
        cert["schema"] = "bad"
        with self.assertRaises(ValueError):
            verify.verify(cert)

    def test_trial_source_mutation(self):
        cert = copy.deepcopy(CERT)
        cert["trials"][1][0] = "2"
        with self.assertRaises(ValueError):
            verify.verify(cert)

    def test_singular_comparator(self):
        cert = copy.deepcopy(CERT)
        cert["C0"] = [["1", "1"], ["1", "1"]]
        with self.assertRaises(ValueError):
            verify.verify(cert)

    def test_nonpositive_actual_W(self):
        cert = copy.deepcopy(CERT)
        cert["negative_channel"]["W"] = ["2", "2"]
        with self.assertRaises(ValueError):
            verify.verify(cert)

    def test_negative_control_sign_mutation(self):
        cert = copy.deepcopy(CERT)
        cert["negative_channel"]["source"] = "2/5"
        with self.assertRaises(ValueError):
            verify.verify(cert)

    def test_trial_change_preserves_harmonic_vector(self):
        cert = copy.deepcopy(CERT)
        cert["trials"][1] = ["1", "100", "-77"]
        out = verify.verify(cert)
        self.assertEqual(
            out["harmonic_vectors_from_trials"][0],
            out["harmonic_vectors_from_trials"][1],
        )


if __name__ == "__main__":
    unittest.main()

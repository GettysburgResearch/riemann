from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x21501_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CERTIFICATE = ROOT / "certificates" / "synthetic.json"


class PrimePairEnergyTests(unittest.TestCase):
    def payload(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_exact_control(self):
        result = MODULE.verify(self.payload())
        self.assertEqual(result["direct_energy"], "29")
        self.assertEqual(result["pairwise_energy"], "29")
        self.assertEqual(result["diagonal_energy"], "28")
        self.assertEqual(result["off_diagonal_energy"], "1")
        self.assertEqual(
            result["exact_proof_object_sha256"],
            "75fb476e2abec4ea872e01069e6944781dc0e949d7f048c75dc17bc27dca6834",
        )

    def test_claim_mutation_rejected(self):
        payload = self.payload()
        payload["claimed"]["energy"] = "30"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_boolean_rejected(self):
        payload = self.payload()
        payload["atoms"][0]["weight"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_overlapping_segments_rejected(self):
        payload = self.payload()
        payload["window_segments"][1]["lower"] = "1/2"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_zero_atom_rejected(self):
        payload = self.payload()
        payload["atoms"][1]["weight"] = "0"
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(payload)

    def test_global_sign_flip_preserves_energy(self):
        payload = self.payload()
        for atom in payload["atoms"]:
            atom["weight"] = str(-MODULE.q(atom["weight"], "weight"))
        payload.pop("claimed")
        result = MODULE.verify(payload)
        self.assertEqual(result["pairwise_energy"], "29")
        self.assertEqual(result["off_diagonal_energy"], "1")

    def test_atom_permutation_preserves_energy(self):
        payload = self.payload()
        payload["atoms"] = list(reversed(payload["atoms"]))
        payload.pop("claimed")
        result = MODULE.verify(payload)
        self.assertEqual(result["pairwise_energy"], "29")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_target_remainder", ROOT / "verify_target_remainder.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

CERT = ROOT / "certificates" / "target-c1e11-m32768-r3.json"


class PhaseGridRemainderTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text(encoding="utf-8"))

    def test_committed_target_clears_gate(self):
        result = MODULE.verify(self.load())
        self.assertTrue(result["strictly_below_target_radius"])
        coarse = MODULE.rational(result["coarse_remainder_upper"], "coarse")
        target = MODULE.rational(result["target_radius"], "target")
        self.assertLess(coarse, target)

    def test_halving_grid_fails_gate(self):
        data = self.load()
        data["grid_size"] = 16384
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_lowering_taylor_order_fails_gate(self):
        data = self.load()
        data["taylor_order"] = 2
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_vector_mutation_fails(self):
        data = self.load()
        data["vector_sha256"] = "0" * 64
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)

    def test_boolean_integer_fails(self):
        data = self.load()
        data["grid_size"] = True
        with self.assertRaises(MODULE.CertificateError):
            MODULE.verify(data)


if __name__ == "__main__":
    unittest.main()

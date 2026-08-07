from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("rbc_verify", ROOT / "verify.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class RBCCertificateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = json.loads((ROOT / "certificates" / "synthetic.json").read_text())

    def test_central_fixture(self) -> None:
        out = mod.verify(copy.deepcopy(self.payload))
        self.assertEqual(out["charge_rate"], "3/4")
        self.assertEqual(out["reserve"], "1/2")
        self.assertEqual(len(out["non_top_rows"]), 6)

    def test_reject_weak_euler_order(self) -> None:
        p = copy.deepcopy(self.payload)
        p["euler_order"] = p["K"] ** 3 - 1
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_reject_uncancelled_internal_face(self) -> None:
        p = copy.deepcopy(self.payload)
        p["faces"].pop(1)
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_reject_zero_reserve(self) -> None:
        p = copy.deepcopy(self.payload)
        p["returned_target_fraction"] = {"num": 1, "den": 1}
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_reject_same_scale_self_route(self) -> None:
        p = copy.deepcopy(self.payload)
        p["same_scale_target_routes"] = 1
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_reject_false_lower_scale(self) -> None:
        p = copy.deepcopy(self.payload)
        p["lower_scale"] = {"num": 9, "den": 10}
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_reject_top_euler_claim(self) -> None:
        p = copy.deepcopy(self.payload)
        p["top_row_euler_closed"] = True
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)

    def test_digest_gate(self) -> None:
        p = copy.deepcopy(self.payload)
        p["claimed_sha256"] = "0" * 64
        with self.assertRaises(mod.VerificationError):
            mod.verify(p)


if __name__ == "__main__":
    unittest.main()

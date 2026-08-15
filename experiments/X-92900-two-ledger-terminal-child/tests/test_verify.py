#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import unittest

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class TestT92900(unittest.TestCase):
    def test_control(self):
        out = MOD.verify()
        self.assertEqual(
            out["verdict"],
            "PASS_TWO_LEDGER_TERMINAL_CHILD_FACTOR67_ALGEBRA",
        )
        self.assertEqual(len(out["mutations_caught"]), 7)

    def test_exact_constant(self):
        out = MOD.native_cost()
        self.assertEqual(out["combined_total"], "493951/8")
        self.assertFalse(out["benchmark_bridge_used"])

    def test_signed_type(self):
        out = MOD.two_ledger()
        self.assertFalse(out["signed_error_is_source_positive"])
        self.assertIn("-1", out["signed_error"])


if __name__ == "__main__":
    unittest.main()

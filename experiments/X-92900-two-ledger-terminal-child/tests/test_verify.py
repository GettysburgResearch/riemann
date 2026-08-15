import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

P = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("v92900", P)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class TestT92900(unittest.TestCase):
    def test_control(self):
        out = V.verify()
        self.assertEqual(
            out["verdict"],
            "PASS_TWO_LEDGER_TERMINAL_CHILD_FACTOR67_ALGEBRA",
        )
        self.assertFalse(out["two_ledger"]["signed_error_is_source_positive"])
        self.assertFalse(out["native_cost"]["portful_schur_demand_used"])

    def test_exact_constant(self):
        self.assertEqual(F(60989) + F(6039, 8), F(493951, 8))
        self.assertLess(F(493951, 8), F(61744))

    def test_mutations(self):
        for name, fn in V.MUTATIONS.items():
            with self.assertRaises(AssertionError, msg=name):
                fn(name)


if __name__ == "__main__":
    unittest.main()

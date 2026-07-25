from fractions import Fraction
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x2816_verify", ROOT / "verify_fast_budget.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class FastBudgetTests(unittest.TestCase):
    def test_total(self):
        result = VERIFY.verify()
        self.assertEqual(result["status"], "EXACT_GLOBAL_MOAT_VERIFIED")

    def test_term_bound(self):
        value = VERIFY.MAX_TERMS * VERIFY.TERM_ULPS * VERIFY.U80
        self.assertLess(value, Fraction(1, 1_070_000))

    def test_pairwise_bound(self):
        gamma = (
            VERIFY.PAIRWISE_DEPTH
            * VERIFY.U80
            / (1 - VERIFY.PAIRWISE_DEPTH * VERIFY.U80)
        )
        self.assertLess(
            gamma * VERIFY.WEIGHT_BOUND,
            Fraction(1, 25_000_000_000),
        )

    def test_deliberately_inflated_term_contract_fails_one_micro(self):
        value = VERIFY.MAX_TERMS * (2**15) * VERIFY.U80
        self.assertGreater(value, Fraction(1, 1_000_000))


if __name__ == "__main__":
    unittest.main()

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x2815_verify", ROOT / "verify_target_bounds.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class TargetBoundsTests(unittest.TestCase):
    def test_target(self):
        out = VERIFY.verify()
        self.assertEqual(out["status"], "EXACT_TARGET_BOUNDS_VERIFIED")

    def test_segment_geometry(self):
        zeta = Fraction(VERIFY.HALF, 2 * VERIFY.MID - VERIFY.HALF)
        beta = Fraction(VERIFY.HALF, VERIFY.MID)
        self.assertLess(zeta, Fraction(1, 8000))
        self.assertLess(beta, Fraction(1, 4000))

    def test_phase_claim_needs_four_odd_terms(self):
        zeta = Fraction(VERIFY.HALF, 2 * VERIFY.MID - VERIFY.HALF)
        self.assertLess(VERIFY.T * VERIFY.atanh_tail(zeta, 3), Fraction(1, 10**23))
        self.assertGreater(VERIFY.T * VERIFY.atanh_tail(zeta, 2), Fraction(1, 10**23))

    def test_sqrt_order(self):
        beta = Fraction(VERIFY.HALF, VERIFY.MID)
        tail5 = VERIFY.invsqrt_relative_tail(beta, 5)
        total5 = 10**11 * 18 * Fraction(1, 200_000) * tail5
        self.assertLess(total5, Fraction(1, 10**14))

    def test_gate_separation(self):
        out = VERIFY.verify()
        p = out["proved"]["total_acceleration_moat"]
        total = Fraction(int(p["numerator"]), int(p["denominator"]))
        self.assertLess(total, Fraction(1, 19_995_000_000))
        self.assertLess(total, Fraction(1, 4_000_000_000) / 4)

    def test_bad_domains_rejected(self):
        with self.assertRaises(ValueError):
            VERIFY.atanh_tail(Fraction(1), 3)
        with self.assertRaises(ValueError):
            VERIFY.invsqrt_relative_tail(Fraction(-1, 10), 5)


if __name__ == "__main__":
    unittest.main()

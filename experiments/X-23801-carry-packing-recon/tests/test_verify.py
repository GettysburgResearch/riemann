from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x23801_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class CarryPackingRegressionTests(unittest.TestCase):
    def test_beta_floor_identity(self):
        for n in range(2, 31):
            for q in range(2, n + 1):
                self.assertEqual(
                    module.beta_fraction(n, q),
                    module.beta_floor_fraction(n, q),
                )

    def test_exact_mobius_affine_regression(self):
        result = module.exact_regression(30)
        self.assertEqual(result["beta_floor_checks"], 435)
        self.assertEqual(result["mobius_affine_checks"], 435)

    def test_uniform_row_lower_bound(self):
        for n in range(2, 101):
            row = sum(
                module.beta_fraction(n, q) / q
                for q in range(2, n + 1)
            )
            self.assertGreaterEqual(row, Fraction(1, 16))

    def test_inverse_recon_control(self):
        result = module.inverse_recon(1000)
        self.assertEqual(result["negative_count_below_minus_1e_12"], 0)
        self.assertGreater(result["mass_ratio_to_8_sqrt_x"], 0.98)

    def test_row_potential_recon_control(self):
        result = module.row_potential_recon(200)
        self.assertLess(result["max_row_minus_n"], 0)


if __name__ == "__main__":
    unittest.main()

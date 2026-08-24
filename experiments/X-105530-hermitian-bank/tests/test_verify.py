import importlib.util
from pathlib import Path
import unittest

P = Path(__file__).resolve().parents[1] / "verify.py"
spec = importlib.util.spec_from_file_location("verify105530", P)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class TestT105530(unittest.TestCase):
    def test_scalar_no_go(self):
        self.assertEqual(mod.scalar_no_go()["unavoidable_z_zbar_coefficient"], "-1/4")

    def test_bank(self):
        x = mod.bank_checks()
        self.assertTrue(x["linear_and_quadratic_coefficients_zero"])
        self.assertEqual(x["epsilon_at_one_quarter"], "77/9216")

    def test_matrix_flux(self):
        x = mod.matrix_flux_checks()
        self.assertEqual(x["real_residue_checks"], 3)
        self.assertGreaterEqual(x["real_axis_lorentz_checks"], 4)

    def test_threshold(self):
        x = mod.threshold_checks()
        self.assertEqual(x["negative_trace_cut"], "9139/184320")

    def test_fail_closed(self):
        x = mod.build_payload()
        for key in (
            "bankreal105530_proved", "matrixlerc105531_proved",
            "stripneg105520_proved", "ninety_percent_established",
            "public_record_beaten", "rh_established"):
            self.assertFalse(x[key])

if __name__ == "__main__":
    unittest.main()

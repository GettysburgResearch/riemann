from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", HERE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class ResidueRigidityReplayTests(unittest.TestCase):
    def test_model_residue_is_negative_and_independent_of_cell(self):
        kappa = Fraction(5, 7)
        for m in range(3, 9):
            for j in range(-8, 9):
                self.assertEqual(VERIFY.model_residue(m, j, Fraction(5), Fraction(7)), -kappa)

    def test_coherence_identity(self):
        vals = [Fraction(9, 10), Fraction(1), Fraction(11, 10)]
        self.assertEqual(*VERIFY.coherence_identity(vals))

    def test_equal_residues_have_unit_coherence(self):
        self.assertEqual(VERIFY.coherence([Fraction(4, 9)] * 7), 1)

    def test_small_relative_spread_has_large_coherence(self):
        vals = [Fraction(99, 100), Fraction(1), Fraction(101, 100)]
        self.assertGreater(VERIFY.coherence(vals), Fraction(999, 1000))

    def test_integration_constant_firewall(self):
        self.assertEqual(
            VERIFY.firewall_residues(Fraction(0)),
            (Fraction(-1, 3), Fraction(-1, 3)),
        )
        plus, minus = VERIFY.firewall_residues(Fraction(1))
        self.assertGreater(plus, 0)
        self.assertLess(minus, 0)

    def test_natural_window_phase_drift_decreases(self):
        rows = VERIFY.natural_window_drift([10**3, 10**4, 10**5, 10**6])
        self.assertTrue(all(rows[i + 1] < rows[i] for i in range(len(rows) - 1)))

    def test_fail_closed_status(self):
        result = VERIFY.run()
        self.assertFalse(result["analytic_gaussian_saddle_replayed"])
        self.assertFalse(result["rh_established"])


if __name__ == "__main__":
    unittest.main()

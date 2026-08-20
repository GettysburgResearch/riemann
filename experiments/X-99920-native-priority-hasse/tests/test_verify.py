from __future__ import annotations

import importlib.util
import pathlib
import unittest
from fractions import Fraction as F

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t99920_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class PriorityHasseTests(unittest.TestCase):
    def test_conservation_with_duplicate_67(self):
        out = M.check_priority_conservation((67, 67, 71, 73))
        self.assertEqual(out["vertices"], 16)
        self.assertEqual(out["edges"], 15)

    def test_activation_surface(self):
        out = M.check_activation_truncation((67, 67, 71, 73), 400000)
        self.assertTrue(out["coarea_equal"])
        self.assertGreater(F(out["surface_flux"]), 0)

    def test_native_67_fibres(self):
        out = M.check_duplicate_67_native_source()
        self.assertEqual(out["native_67_coefficient"], "-2/67")
        self.assertTrue(out["normalization_firewall"])

    def test_poisson_tail(self):
        out = M.check_poisson_tail_identity()
        self.assertEqual(out["tau_checks"], 6)

    def test_negative_control(self):
        out = M.check_negative_control()
        self.assertEqual(out["sum_mu_over_n_through_13"], "-2323/30030")

    def test_mutations(self):
        out = M.check_mutations()
        self.assertTrue(all(out.values()))


if __name__ == "__main__":
    unittest.main()

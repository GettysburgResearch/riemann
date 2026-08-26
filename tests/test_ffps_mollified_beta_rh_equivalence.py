from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_mollified_beta_rh_equivalence.py"
)
SPEC = importlib.util.spec_from_file_location("mollified_equivalence", MODULE_PATH)
assert SPEC and SPEC.loader
mollified_equivalence = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mollified_equivalence)


class FfpsMollifiedBetaRhEquivalenceTest(unittest.TestCase):
    def test_beta_partial_sum_identity(self) -> None:
        self.assertEqual(
            mollified_equivalence.beta_partial_sum_identity(),
            "A_beta(x)=A_mu(x)-67^(-1/2)*A_mu(x/67)",
        )

    def test_bv_certificate(self) -> None:
        certificate = mollified_equivalence.bv_certificate(Fraction(1, 8))
        self.assertEqual(certificate["sup_norm_bound_in_units_of_TV_K_ext"], "8")
        self.assertEqual(certificate["variation_bound_in_units_of_TV_K_ext"], "16")
        self.assertEqual(
            certificate["summation_by_parts_factor_in_units_of_TV_K_ext"], "32"
        )
        with self.assertRaises(ValueError):
            mollified_equivalence.bv_certificate(Fraction(0))

    def test_box_multiplier(self) -> None:
        self.assertFalse(mollified_equivalence.box_multiplier_zero_free(Fraction(0)))
        self.assertTrue(
            mollified_equivalence.box_multiplier_zero_free(Fraction(1, 1000))
        )

    def test_equivalence_graph(self) -> None:
        graph = mollified_equivalence.implication_graph()
        self.assertEqual(len(graph), 3)
        self.assertIn("Landau", graph["negative_mass_to_RH"])
        result = mollified_equivalence.run()
        self.assertFalse(result["equivalence"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["source_atoms_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()

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
    / "ffps_extra_notched_mellin_landau_consumer.py"
)
SPEC = importlib.util.spec_from_file_location("extra_consumer", MODULE_PATH)
assert SPEC and SPEC.loader
extra_consumer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(extra_consumer)


class FfpsExtraNotchedMellinLandauConsumerTest(unittest.TestCase):
    def test_zero_locations_miss_open_strip(self) -> None:
        self.assertTrue(extra_consumer.open_strip_nonvanishing())
        self.assertEqual(
            extra_consumer.dyadic_zero_real_parts()["q(s)=1-sqrt(2)*2^(-s)"],
            Fraction(1, 2),
        )

    def test_exact_samples_and_guard(self) -> None:
        for s in (2, 3, 4, 6):
            self.assertNotEqual(
                extra_consumer.simplified_multiplier_at_integer(s),
                (Fraction(0), Fraction(0)),
            )
        with self.assertRaises(ValueError):
            extra_consumer.simplified_multiplier_at_integer(1)

    def test_positive_box_has_no_open_strip_zero(self) -> None:
        self.assertFalse(extra_consumer.smoothing_multiplier_nonzero(Fraction(0)))
        self.assertTrue(extra_consumer.smoothing_multiplier_nonzero(Fraction(1, 1000)))
        self.assertTrue(
            extra_consumer.smoothing_multiplier_nonzero(Fraction(499, 1000))
        )

    def test_measure_and_landau_certificates(self) -> None:
        measure = extra_consumer.finite_measure_certificate()
        self.assertEqual(measure["max_D_out_order"], 4)
        self.assertEqual(measure["convolution_identity"], "D^4(a*a)=a''*a''")
        landau = extra_consumer.landau_hypothesis_certificate()
        self.assertEqual(landau["positive_density_abscissa_upper_bound"], "1/2")
        self.assertIn("Re(s)>0", landau["division_gate"])

    def test_gate_and_caps(self) -> None:
        result = extra_consumer.run()
        self.assertEqual(result["source_adapter_gate"]["name"], "EXTSRC106150")
        self.assertEqual(
            result["conditional_consumer"]["conclusion"], "Riemann Hypothesis"
        )
        self.assertEqual(
            result["conditional_consumer"]["premise"],
            "nu_ext^-([1,Y]) = Y^o(1), in Jordan variation",
        )
        self.assertFalse(result["conditional_consumer"]["premise_viable"])
        self.assertIn("sqrt(Y)", result["conditional_consumer"]["atomic_lower_bound"])
        self.assertEqual(result["canonical_successor"]["strength"], "equivalent to RH")
        self.assertIn("K_bd", result["canonical_successor"]["boundary_field"])
        self.assertIn("|G(t)|", result["canonical_successor"]["shortest_criterion"])
        self.assertFalse(result["canonical_successor"]["criterion_proved"])
        self.assertFalse(result["canonical_successor"]["rh_proved"])
        self.assertEqual(result["resource_caps"]["source_atoms_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()

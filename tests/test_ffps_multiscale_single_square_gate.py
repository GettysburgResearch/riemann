from __future__ import annotations

import importlib.util
import math
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
    / "ffps_multiscale_single_square_gate.py"
)
SPEC = importlib.util.spec_from_file_location("multiscale_gate", MODULE_PATH)
assert SPEC and SPEC.loader
multiscale_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(multiscale_gate)


class MultiscaleSingleSquareGateTest(unittest.TestCase):
    def test_mode_census_and_mixed_fraction(self) -> None:
        for ranks in ((1, 1), (2, 1), (2, 2, 2), (1, 2, 2, 3)):
            row = multiscale_gate.mode_census(ranks)
            expected_pure = sum(2**rank - 1 for rank in ranks)
            self.assertEqual(row["selected_modes"], 2 ** sum(ranks) - 1)
            self.assertEqual(row["band_pure_modes"], expected_pure)
            self.assertEqual(
                row["cross_band_modes"], row["selected_modes"] - expected_pure
            )
            self.assertGreater(row["cross_band_modes"], 0)

    def test_mixed_witness_is_invisible_bandwise(self) -> None:
        for ranks in ((1, 1), (2, 2), (2, 1, 2)):
            row = multiscale_gate.walsh_witness(ranks)
            separate = Fraction(row["every_separate_band_interferometer"])
            joint = Fraction(row["joint_interferometer"])
            self.assertEqual(row["all_band_pure_transforms"], "0")
            self.assertLess(joint, separate)
            self.assertEqual(joint - separate, Fraction(row["joint_minus_separate"]))

    def test_conductor_closed_form(self) -> None:
        for degrees in ((2, 4), (2, 3, 8, 13), (2, 3, 5, 8, 13, 21)):
            row = multiscale_gate.conductor_budget(degrees)
            rank = len(degrees)
            direct = sum(
                sum(degrees[index] for index in range(rank) if mask & (1 << index)) - 2
                for mask in range(1, 2**rank)
            )
            self.assertEqual(row["total_modewise_hc1"], direct)
            average = Fraction(row["average_modewise_hc1"])
            self.assertGreaterEqual(average, Fraction(max(degrees), 2) - 2)

    def test_joint_gain_requires_one_square(self) -> None:
        panel = multiscale_gate.multiscale_panel((2, 2, 2), (2, 3, 5, 8, 13, 21))
        band_leverages = [Fraction(value) for value in panel["band_leverages"]]
        joint = Fraction(panel["joint_single_square_leverage"])
        self.assertTrue(panel["joint_equals_product_of_band_leverages"])
        self.assertEqual(joint, math.prod(band_leverages, start=Fraction(1)))
        self.assertTrue(all(Fraction(0) < value < 1 for value in band_leverages))
        self.assertTrue(all(joint < value for value in band_leverages))
        self.assertEqual(panel["separate_square_product_degree"], 6)

    def test_invalid_and_resource_caps(self) -> None:
        for ranks in ((), (0,), (True,), (3, 3, 3)):
            with self.assertRaises(ValueError):
                multiscale_gate.mode_census(ranks)
        for degrees in ((), (1,), (65,)):
            with self.assertRaises(ValueError):
                multiscale_gate.conductor_budget(degrees)
        with self.assertRaises(ValueError):
            multiscale_gate.walsh_witness((2,))
        caps = multiscale_gate.run()["resource_caps"]
        self.assertEqual(caps["maximum_quotient_points"], 256)
        self.assertEqual(caps["closed_places_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()

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
    / "function_field_frobenius_channel_filter_calculus.py"
)
SPEC = importlib.util.spec_from_file_location("frobenius_filter_calculus", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FrobeniusChannelFilterCalculusTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_exact_stable_factor_split(self) -> None:
        polys = subject.replay_polynomials()
        self.assertEqual(
            subject.uni_mul(polys["Q_factor"], polys["R_factor"]), polys["P"]
        )
        self.assertEqual(
            subject.uni_div_exact(polys["P"], polys["Q_factor"]),
            polys["R_factor"],
        )

    def test_reciprocal_series_is_inverse_to_cap(self) -> None:
        denominator = (Fraction(1), Fraction(-2), Fraction(3))
        reciprocal = subject.reciprocal_series(denominator)
        product = subject.uni_mul(denominator, reciprocal)
        self.assertEqual(product[0], 1)
        self.assertEqual(
            product[1 : subject.SERIES_CAP + 1],
            (Fraction(0),) * subject.SERIES_CAP,
        )

    def test_selector_and_deflation_replay(self) -> None:
        panel = subject.selector_replay()
        self.assertTrue(panel["stable_selector_verified"])
        self.assertTrue(panel["axis_deflation_verified"])
        self.assertTrue(panel["total_deflation_verified"])
        self.assertEqual(panel["curve_numerator_degree"], 4)
        self.assertEqual(panel["axis_filter_bidegree"], [4, 4])

    def test_minimal_degree_growth(self) -> None:
        panel = subject.minimal_degree_panel(8)
        for row in panel["rows"]:
            genus = row["genus"]
            self.assertEqual(row["generic_numerator_degree"], 2 * genus)
            self.assertEqual(row["two_axis_null_bidegree"], [2 * genus, 2 * genus])
            self.assertEqual(row["three_channel_depth_sum"], 6 * genus)

    def test_family_uniform_lcm_growth(self) -> None:
        panel = subject.family_uniform_panel()
        self.assertEqual(
            [row["universal_axis_depth"] for row in panel["rows"]], [4, 8, 12]
        )
        self.assertEqual(panel["generic_pairwise_coprime_depth"], "sum_i degree(P_i)")

    def test_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertTrue(result["scope"]["fixed_curve"])
        self.assertFalse(result["scope"]["growing_genus_fixed_depth_filter"])
        self.assertFalse(result["scope"]["incomplete_family_theorem"])
        self.assertFalse(result["scope"]["number_field_transfer"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertEqual(result["resource_caps"]["curves_enumerated"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.uni_div_exact((Fraction(1),), (Fraction(1), Fraction(1)))
        with self.assertRaises(ValueError):
            subject.reciprocal_series((Fraction(0), Fraction(1)))
        with self.assertRaises(ValueError):
            subject.monic((Fraction(0),))
        with self.assertRaises(ValueError):
            subject.lift_axis((Fraction(1),), 2)
        with self.assertRaises(ValueError):
            subject.minimal_degree_panel(0)


if __name__ == "__main__":
    unittest.main()

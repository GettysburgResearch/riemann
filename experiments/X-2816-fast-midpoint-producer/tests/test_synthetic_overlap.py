from fractions import Fraction
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "synthetic-overlap.json"


def frac(value):
    return Fraction(int(value["numerator"]), int(value["denominator"]))


class SyntheticOverlapTests(unittest.TestCase):
    def load(self):
        return json.loads(RESULT.read_text(encoding="utf-8"))

    def test_target_sized_midpoint_inside_directed_interval(self):
        data = self.load()["target_sized_control"]
        lower = frac(data["directed_algebraic_interval"]["lower"])
        upper = frac(data["directed_algebraic_interval"]["upper"])
        midpoint = frac(data["fast_midpoint"])
        self.assertLessEqual(lower, midpoint)
        self.assertLessEqual(midpoint, upper)
        self.assertTrue(data["fast_midpoint_inside_directed_interval"])

    def test_small_direct_interval_inside_fast_global_moat(self):
        data = self.load()["small_direct_control"]
        lower = frac(data["direct_mpfr_interval"]["lower"])
        upper = frac(data["direct_mpfr_interval"]["upper"])
        midpoint = frac(data["fast_midpoint"])
        moat = Fraction(1, 1_000_000)
        self.assertLessEqual(midpoint - moat, lower)
        self.assertLessEqual(upper, midpoint + moat)
        self.assertTrue(data["fast_midpoint_plus_minus_one_micro_contains_direct_interval"])

    def test_control_is_visibly_synthetic(self):
        data = self.load()
        self.assertEqual(data["status"], "SYNTHETIC_CONTROLS_ONLY")
        self.assertEqual(data["target_sized_control"]["cells"], 4)


if __name__ == "__main__":
    unittest.main()

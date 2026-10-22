"""Focused low-cost checks for the discovery-only USp(4) sign quadrature."""

from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import usp4_sign_probability as subject  # noqa: E402


class USp4SignProbabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_frozen_refinement_and_exact_moment_controls(self) -> None:
        self.assertEqual(
            [row["grid_size"] for row in self.fixture["grid_refinement"]],
            [128, 256, 512],
        )
        self.assertEqual(self.fixture["display_estimate"], "0.737849043834")
        self.assertTrue(
            all(
                phase["exact_moment_controls_pass"]
                for row in self.fixture["grid_refinement"]
                for phase in row["phase_estimates"]
            )
        )
        self.assertEqual(
            self.fixture["grid_refinement"][-1]["phase_spread_display"],
            "0.000070698736",
        )

    def test_finite_sign_proportions_are_exact_and_increase_toward_the_display(self) -> None:
        rows = self.fixture["finite_comparisons"]
        exact = [Fraction(*row["negative_proportion"]) for row in rows]
        self.assertEqual(exact, [Fraction(17, 27), Fraction(33, 50), Fraction(33, 49)])
        self.assertTrue(all(left < right for left, right in zip(exact, exact[1:])))
        display = float(self.fixture["display_estimate"])
        self.assertTrue(all(float(value) < display for value in exact))
        self.assertEqual(
            self.fixture["boundary_certificate"]["status"],
            "PROVED_HAAR_MEASURE_ZERO",
        )
        self.assertIn(
            "continuity set",
            self.fixture["boundary_certificate"]["weak_convergence_consequence"],
        )
        self.assertIn("do not prove convergence", self.fixture["interpretation"])
        self.assertIn("not an interval proof", self.fixture["firewall"])

    def test_resource_guards_fire_before_expansion(self) -> None:
        with self.assertRaisesRegex(ValueError, "wall limit"):
            subject.build_fixture(maximum_wall_seconds=5.1)

        class AdvancingClock:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self) -> float:
                self.calls += 1
                return 0.0 if self.calls == 1 else 6.0

        with self.assertRaisesRegex(TimeoutError, "monotonic wall deadline"):
            subject.build_fixture(clock=AdvancingClock())

    def test_checked_in_fixture_is_exact_replay(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "usp4_sign_probability.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, self.fixture)


if __name__ == "__main__":
    unittest.main()

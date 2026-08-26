from __future__ import annotations

import importlib.util
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_block_entropy_conductor_phase_diagram.py"
)
NOTE_PATH = MODULE_PATH.with_name(
    "FUNCTION_FIELD_BLOCK_ENTROPY_CONDUCTOR_PHASE_DIAGRAM.md"
)
SPEC = importlib.util.spec_from_file_location("entropy_conductor", MODULE_PATH)
assert SPEC and SPEC.loader
entropy_conductor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(entropy_conductor)


class FunctionFieldBlockEntropyConductorPhaseDiagramTest(unittest.TestCase):
    def test_display_math_delimiters_are_balanced(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)

    def test_orientation_density(self) -> None:
        self.assertEqual(entropy_conductor.eligible_density(5), 1.0)
        self.assertEqual(entropy_conductor.eligible_density(9), 1.0)
        self.assertEqual(entropy_conductor.eligible_density(3), 0.5)
        self.assertEqual(entropy_conductor.eligible_density(27), 0.5)
        with self.assertRaises(ValueError):
            entropy_conductor.eligible_density(15)

    def test_zero_loss_recovers_existing_balanced_points(self) -> None:
        panel_half = entropy_conductor.optimized_power_panel(0.5, 0.0)
        panel_one = entropy_conductor.optimized_power_panel(1.0, 0.0)
        self.assertAlmostEqual(float(panel_half["optimal_alpha"]), 0.274064461784)
        self.assertAlmostEqual(
            float(panel_half["optimal_net_exponent"]), 0.061155717291
        )
        self.assertAlmostEqual(float(panel_one["optimal_alpha"]), 0.548128923568)
        self.assertAlmostEqual(
            float(panel_one["optimal_net_exponent"]), 0.122311434583
        )

    def test_uniform_rich_core_balance_equation(self) -> None:
        for density in (0.5, 1.0):
            for theta in (0.0, 0.05 * density, 0.10 * density):
                fraction = entropy_conductor.uniform_balanced_fraction(
                    density, theta
                )
                alpha = density * fraction
                self.assertAlmostEqual(
                    entropy_conductor.richness_rate(density, alpha),
                    alpha * entropy_conductor.LOG_BLOCK_GAIN - theta,
                    places=12,
                )

    def test_typical_power_scale_is_not_the_uniform_exponent(self) -> None:
        density = 1.0
        theta = 0.10
        panel = entropy_conductor.optimized_power_panel(density, theta)
        alpha = float(panel["optimal_alpha"])
        typical = alpha * entropy_conductor.effective_rank_gain(density, theta)
        uniform = float(panel["uniform_trace_exponent_at_optimum"])
        self.assertGreater(typical, uniform)
        self.assertAlmostEqual(
            uniform,
            alpha * entropy_conductor.LOG_BLOCK_GAIN - theta,
            places=11,
        )

    def test_threshold_is_sharp_in_model(self) -> None:
        for density in (0.5, 1.0):
            threshold = density * math.log(5 / 4)
            self.assertGreater(
                entropy_conductor.effective_rank_gain(density, threshold - 1e-9),
                0,
            )
            with self.assertRaises(ValueError):
                entropy_conductor.uniform_balanced_fraction(
                    density, threshold + 1e-12
                )
            self.assertLess(
                entropy_conductor.effective_rank_gain(density, threshold + 1e-9),
                0,
            )

    def test_caps_and_guards(self) -> None:
        with self.assertRaises(ValueError):
            entropy_conductor.uniform_balanced_fraction(0.25, 0)
        with self.assertRaises(ValueError):
            entropy_conductor.sublog_panel(0.5, 0.0, 0.0)
        caps = entropy_conductor.run()["resource_caps"]
        self.assertEqual(caps["polynomials_enumerated"], 0)
        self.assertEqual(caps["curves_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()

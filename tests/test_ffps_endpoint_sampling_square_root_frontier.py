from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_endpoint_sampling_square_root_frontier.py"
)
SPEC = importlib.util.spec_from_file_location(
    "endpoint_sampling_square_root_frontier", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class EndpointSamplingSquareRootFrontierTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_exact_dyadic_hidden_excursion(self) -> None:
        unit = (Fraction(3, 5), Fraction(4, 5))
        coefficients, panel = subject.hidden_excursion(
            subject.TOY_LIMIT,
            subject.dyadic_endpoints(subject.TOY_LIMIT),
            unit,
        )
        self.assertEqual(len(coefficients), subject.TOY_LIMIT)
        self.assertTrue(panel["all_sampled_prefixes_zero"])
        self.assertEqual(panel["largest_gap"], 128)
        self.assertEqual(panel["half_excursion_length"], 64)
        self.assertEqual(Fraction(panel["maximum_square"]), 16)

    def test_square_root_grid(self) -> None:
        grid = subject.square_root_grid(subject.TOY_LIMIT, subject.TOY_SQRT_MESH)
        self.assertEqual(grid, (0, 4, 16, 36, 64, 100, 144, 196, 256))
        roots = [subject.isqrt(value) for value in grid]
        self.assertEqual(
            [right - left for left, right in pairwise(roots)],
            [subject.TOY_SQRT_MESH] * (len(roots) - 1),
        )

    def test_bridge_norm_comparison(self) -> None:
        panel = subject.bridge_norm_panel()
        endpoint = Fraction(panel["endpoint_max_square"])
        bridge = Fraction(panel["bridge_max_square"])
        full = Fraction(panel["full_max_square"])
        residual = max(endpoint, bridge)
        self.assertLessEqual(residual, 4 * full)
        self.assertLessEqual(full, 4 * residual)

    def test_dyadic_endpoints_are_logarithmic(self) -> None:
        endpoints = subject.dyadic_endpoints(subject.TOY_LIMIT)
        self.assertEqual(endpoints, (0, 1, 2, 4, 8, 16, 32, 64, 128, 256))

    def test_canonical_json_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertIn(
            "sqrt(X)/(2*(m+1))",
            result["source_blind_sampling"]["sharp_lower_bound"],
        )
        self.assertIn(
            "maximal beta bridge",
            result["literal_beta_bridge"]["canonical_residual_gate"],
        )
        scope = result["scope"]
        self.assertTrue(scope["literal_beta_square_root_sampler"])
        self.assertTrue(scope["arbitrary_coefficient_log_sampler_refuted"])
        self.assertTrue(scope["adaptive_sampler_refuted_source_blindly"])
        self.assertFalse(scope["literal_beta_dyadic_endpoints_alone"])
        self.assertFalse(scope["beta_bridge_estimate_proved"])
        self.assertFalse(scope["endpoint_only_logarithmic_rh_criterion_proved"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_resource_caps(self) -> None:
        result = subject.run(check_sources=False)
        self.assertEqual(result["resource_caps"]["toy_limit"], 256)
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        unit = (Fraction(3, 5), Fraction(4, 5))
        with self.assertRaises(ValueError):
            subject.gpower(unit, -1)
        with self.assertRaises(ValueError):
            subject.dyadic_endpoints(1)
        with self.assertRaises(ValueError):
            subject.square_root_grid(255, 2)
        with self.assertRaises(ValueError):
            subject.hidden_excursion(255, (0, 255), unit)
        with self.assertRaises(ValueError):
            subject.hidden_excursion(256, (0, 300), unit)


if __name__ == "__main__":
    unittest.main()

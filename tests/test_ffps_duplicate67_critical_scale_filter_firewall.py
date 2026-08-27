from __future__ import annotations

import importlib.util
import json
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
    / "ffps_duplicate67_critical_scale_filter_firewall.py"
)
SPEC = importlib.util.spec_from_file_location(
    "duplicate67_critical_scale_filter_firewall", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class Duplicate67CriticalScaleFilterFirewallTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_duplicate_prime_coefficient_identity(self) -> None:
        for prime in (subject.TOY_PRIME, subject.EXCEPTIONAL_PRIME):
            residue = 2
            expected = [
                coefficient * subject.mobius(residue) for coefficient in (1, -2, 1, 0)
            ]
            actual = [
                subject.beta((prime**exponent) * residue, prime)
                for exponent in range(4)
            ]
            self.assertEqual(actual, expected)

        exceptional = subject.coefficient_identity_panel(
            subject.EXCEPTIONAL_PRIME, subject.COEFFICIENT_CAP
        )
        toy = subject.coefficient_identity_panel(
            subject.TOY_PRIME, subject.COEFFICIENT_CAP
        )
        self.assertEqual(exceptional["prime"], subject.EXCEPTIONAL_PRIME)
        self.assertGreater(toy["layer_counts"]["2"], 0)

    def test_first_scale_filter_and_terminating_inverse(self) -> None:
        values = tuple(
            Fraction(((-1) ** index) * (index + 3), index + 1)
            for index in range(subject.SCALE_DEPTH_CAP)
        )
        filtered = subject.first_filter(values, subject.TOY_CONTRACTION)
        self.assertEqual(
            subject.inverse_first_filter(filtered, subject.TOY_CONTRACTION),
            values,
        )

    def test_squared_scale_filter_and_terminating_inverse(self) -> None:
        values = tuple(
            Fraction((index + 2) * (index + 5), 2 * index + 1)
            for index in range(subject.SCALE_DEPTH_CAP)
        )
        filtered = subject.second_filter(values, subject.TOY_CONTRACTION)
        self.assertEqual(
            subject.inverse_second_filter(filtered, subject.TOY_CONTRACTION),
            values,
        )

    def test_block_hilbert_bounds_and_sharp_modes(self) -> None:
        panel = subject.block_filter_panel()
        lower = Fraction(panel["lower_energy_constant"])
        upper = Fraction(panel["upper_energy_constant"])
        rows = panel["rows"]
        for row in rows:
            ratio = Fraction(row["energy_ratio"])
            self.assertGreaterEqual(ratio, lower)
            self.assertLessEqual(ratio, upper)

        aligned = [
            Fraction(row["energy_ratio"]) for row in rows if row["mode"] == "aligned"
        ]
        alternating = [
            Fraction(row["energy_ratio"])
            for row in rows
            if row["mode"] == "alternating"
        ]
        self.assertLess(abs(aligned[-1] - lower), abs(aligned[0] - lower))
        self.assertLess(abs(alternating[-1] - upper), abs(alternating[0] - upper))

    def test_perron_unit_bounds(self) -> None:
        panel = subject.perron_panel()
        self.assertEqual(panel["half_plane"], "Re(w)>=1/2")
        self.assertEqual(Fraction(panel["toy_lower"]), 1 - subject.TOY_CONTRACTION)
        self.assertEqual(Fraction(panel["toy_upper"]), 1 + subject.TOY_CONTRACTION)
        self.assertIn("sum_(k>=0)", panel["inverse"])

    def test_canonical_json_and_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertEqual(
            result["exact_scale_ladder"]["q67_explicit_layers_on_residue_2"],
            [-1, 2, -1, 0],
        )
        self.assertTrue(result["scope"]["exact_scale_identities_proved"])
        self.assertTrue(result["scope"]["weighted_maximal_isomorphism_proved"])
        self.assertTrue(result["scope"]["block_hilbert_isomorphism_proved"])
        self.assertFalse(result["scope"]["perron_numerator_zero_or_contraction"])
        self.assertFalse(result["scope"]["critical_window_estimate_proved"])
        self.assertFalse(result["scope"]["mobius_block_estimate_proved"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertEqual(
            result["smallest_live_estimate"]["status"],
            "OPEN SUFFICIENT TARGET; STRONGER THAN THE ASSEMBLED ENDPOINT",
        )
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.mobius(0)
        with self.assertRaises(ValueError):
            subject.beta(1, 0)
        with self.assertRaises(ValueError):
            subject.coefficient_identity_panel(subject.TOY_PRIME, 0)
        with self.assertRaises(ValueError):
            subject.first_filter((), subject.TOY_CONTRACTION)
        with self.assertRaises(ValueError):
            subject.inverse_second_filter((), subject.TOY_CONTRACTION)


if __name__ == "__main__":
    unittest.main()

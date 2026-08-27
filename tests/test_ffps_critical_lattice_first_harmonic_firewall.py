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
    / "ffps_critical_lattice_first_harmonic_firewall.py"
)
SPEC = importlib.util.spec_from_file_location(
    "critical_lattice_first_harmonic_firewall", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CriticalLatticeFirstHarmonicFirewallTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_literal_beta_magnitude_decomposition(self) -> None:
        for prime in (subject.TOY_PRIME, subject.EXCEPTIONAL_PRIME):
            panel = subject.magnitude_identity_panel(prime, subject.COEFFICIENT_CAP)
            self.assertEqual(
                panel["explicit_layers_on_residue_2"],
                [1, 2, 1, 0],
            )
            self.assertIn("zeta(s)/zeta(2s)", panel["dirichlet_series"])
            for value in (1, 2, prime, 2 * prime, prime * prime, 2 * prime * prime):
                self.assertEqual(
                    abs(subject.beta(value, prime)),
                    subject.beta_magnitude_decomposition(value, prime),
                )

    def test_coherent_four_cell_normalization(self) -> None:
        panel = subject.coherent_four_cell_panel()
        self.assertEqual(Fraction(panel["coordinate_square"]), 45)
        self.assertEqual(Fraction(panel["coefficient_l2_square"]), 85)
        self.assertEqual(
            Fraction(panel["single_row_rayleigh_lower_bound"]),
            Fraction(9, 17),
        )

    def test_growing_notch_frontier(self) -> None:
        panel = subject.growing_notch_frontier_panel()
        rows = {
            Fraction(row["r_over_logX_over_loglogX"]): Fraction(
                row["coherent_power_exponent"]
            )
            for row in panel["rows"]
        }
        self.assertEqual(rows[Fraction(0)], 1)
        self.assertEqual(rows[Fraction(1, 4)], Fraction(1, 2))
        self.assertEqual(rows[Fraction(1, 2)], 0)
        self.assertEqual(rows[Fraction(3, 4)], Fraction(-1, 2))
        self.assertEqual(panel["subpower_threshold"], "c>=1/2")

    def test_scope_firewalls(self) -> None:
        result = subject.run(check_sources=False)
        scope = result["scope"]
        self.assertTrue(scope["literal_beta_magnitudes_preserved"])
        self.assertFalse(scope["mobius_signs_preserved"])
        self.assertTrue(scope["countermodel_is_source_blind"])
        self.assertFalse(scope["actual_beta_witness_estimated"])
        self.assertFalse(scope["moving_notch_is_fixed_detector"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_fixture_and_resources(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        self.assertEqual(result["resource_caps"]["coefficient_identity_cap"], 625)
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.mobius(0)
        with self.assertRaises(ValueError):
            subject.beta(1, 0)
        with self.assertRaises(ValueError):
            subject.magnitude_identity_panel(5, 0)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_prefix_truncated_rough_rankin_frontier.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("truncated_rough_rankin", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load truncated rough Rankin producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class PrefixTruncatedRoughRankinFrontierTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_mobius_and_literal_beta(self) -> None:
        self.assertEqual(
            [subject.mobius(n) for n in range(1, 11)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
        )
        self.assertEqual(subject.beta(1), 1)
        self.assertEqual(subject.beta(67), -2)
        self.assertEqual(subject.beta(67 * 2), 2)
        with self.assertRaises(ValueError):
            subject.mobius(0)

    def test_smooth_and_rough_partitions(self) -> None:
        self.assertTrue(subject.is_y_smooth(2**4 * 3**2 * 5, 5))
        self.assertFalse(subject.is_y_smooth(7, 5))
        self.assertTrue(subject.is_y_rough(7 * 11, 5))
        self.assertFalse(subject.is_y_rough(7 * 11, 7))
        squarefree = subject.squarefree_smooth_divisors(100, 5)
        smooth = subject.smooth_numbers(100, 5)
        self.assertTrue(set(squarefree) <= set(smooth))
        self.assertIn(30, squarefree)
        self.assertNotIn(12, squarefree)
        self.assertIn(12, smooth)

    def test_all_four_prefix_identities(self) -> None:
        row = subject.source_prefixes(420, 13, 0.271)
        for key in (
            "forward_max_error",
            "inverse_max_error",
            "duplicate_max_error",
            "duplicate_inverse_max_error",
        ):
            self.assertLess(row[key], 2e-12)

    def test_truncated_masses_and_rankin_bounds(self) -> None:
        row = subject.coefficient_masses(840, 13, 0.11)
        self.assertLessEqual(
            row["squarefree_truncated_mass"], row["squarefree_rankin_bound"]
        )
        self.assertLessEqual(row["smooth_truncated_mass"], row["smooth_rankin_bound"])
        self.assertLess(
            row["squarefree_truncated_mass"], row["squarefree_complete_product"]
        )
        self.assertLess(row["smooth_truncated_mass"], row["smooth_complete_product"])
        self.assertLessEqual(
            row["squarefree_binomial_lower_bound"], row["squarefree_truncated_mass"]
        )
        with self.assertRaises(ValueError):
            subject.coefficient_masses(100, 5, 0.0)

    def test_polylog_parameter_tends_to_the_exponent_two_frontier(self) -> None:
        early = subject.polylog_phase_panel(10**6, (6.0,))[0]
        late = subject.polylog_phase_panel(10**100, (6.0,))[0]
        self.assertLess(late["rankin_sigma"], early["rankin_sigma"])
        self.assertLess(
            abs(late["log_y_over_loglog_x"] - 2), abs(early["log_y_over_loglog_x"] - 2)
        )
        self.assertLess(late["suppressed_prime_scale_over_log_x"], 1)

    def test_fixed_power_certificate(self) -> None:
        rows = subject.fixed_power_certificate(10**20, (3.0, 4.0, 6.0))
        self.assertAlmostEqual(rows[0]["certificate_power"], 1 / 6)
        self.assertAlmostEqual(rows[1]["certificate_power"], 1 / 4)
        self.assertAlmostEqual(rows[2]["certificate_power"], 1 / 3)
        self.assertTrue(
            all(row["suppressed_prime_scale_over_log_x"] < 1 for row in rows)
        )
        with self.assertRaises(ValueError):
            subject.fixed_power_certificate(math.e**3, (2.0,))

    def test_canonical_fixture_and_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertIn("if and only if", fixture["theorem"]["rankin_range"])
        self.assertEqual(fixture["proof_ledger"]["rough_source_estimate"], "OPEN")
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")
        self.assertEqual(fixture["resource_caps"]["integer_horizon"], 840)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_zero_free_beta_energy_ladder.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("zero_free_beta_energy", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load zero-free beta-energy producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsZeroFreeBetaEnergyLadderTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_order_one_is_normalized_frozen_universal_weight(self) -> None:
        mass_squared = 16.0 * math.sinh(0.5) ** 4
        for sample in subject.WEIGHT_SAMPLES:
            actual = subject.ladder_weight(1, float(sample))
            expected = subject.source.universal_weight(float(sample)) / mass_squared
            self.assertTrue(math.isclose(actual, expected, rel_tol=1e-13, abs_tol=0))

    def test_every_replayed_order_has_only_the_zero_notch(self) -> None:
        for order in range(1, subject.MAXIMUM_LADDER_ORDER + 1):
            self.assertEqual(subject.ladder_weight(order, 0.0), 0.0)
            for sample in subject.WEIGHT_SAMPLES:
                self.assertGreater(
                    subject.ladder_weight(order, float(sample)),
                    0.0,
                )

    def test_support_and_decay_ladders(self) -> None:
        self.assertEqual(
            [
                subject.support_endpoint(order)
                for order in range(1, subject.MAXIMUM_LADDER_ORDER + 1)
            ],
            [2, 2, 2, 2, 2, 2],
        )
        self.assertEqual(
            [
                subject.decay_exponent(order)
                for order in range(1, subject.MAXIMUM_LADDER_ORDER + 1)
            ],
            [-2, -6, -10, -14, -18, -22],
        )

    def test_high_frequency_power_is_finite_and_positive(self) -> None:
        for order in (1, 2, 4):
            scaled = [
                subject.ladder_weight(order, float(t))
                * float(t) ** (-subject.decay_exponent(order))
                for t in (Fraction(50), Fraction(100), Fraction(200))
            ]
            self.assertTrue(all(math.isfinite(value) and value > 0 for value in scaled))

    def test_control_rows_and_scope(self) -> None:
        result = subject.run()
        rows = result["kernel_ladder"]["rows"]
        self.assertEqual(len(rows), subject.MAXIMUM_LADDER_ORDER)
        self.assertTrue(all(row["weight_zero_order_at_zero"] == 2 for row in rows))
        self.assertEqual(
            result["proof_ledger"]["any_energy_or_off_diagonal_estimate"],
            "NOT PROVED",
        )
        self.assertEqual(result["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_fixture_is_canonical(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["rh_equivalent_prefix_energy"],
            "PROVED FROM FROZEN LANDAU ARGUMENT",
        )
        self.assertEqual(fixture["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        for bad in (True, 0, -1, subject.MAXIMUM_LADDER_ORDER + 1, 1.5):
            with self.assertRaises(ValueError):
                subject.validate_order(bad)
        with self.assertRaises(ValueError):
            subject.phi_fourier_weight(float("inf"))
        with self.assertRaises(ValueError):
            subject.ladder_weight(1, float("nan"))


if __name__ == "__main__":
    unittest.main()

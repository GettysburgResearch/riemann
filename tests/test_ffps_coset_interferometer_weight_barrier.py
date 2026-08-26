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
    / "ffps_coset_interferometer_weight_barrier.py"
)
SPEC = importlib.util.spec_from_file_location("weight_barrier", MODULE_PATH)
assert SPEC and SPEC.loader
weight_barrier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weight_barrier)


class CosetInterferometerWeightBarrierTest(unittest.TestCase):
    def test_prime_field_autocorrelations(self) -> None:
        for prime in (3, 5, 7, 11, 13, 17, 19):
            trivial = weight_barrier.additive_autocorrelation(prime, False)
            quadratic = weight_barrier.additive_autocorrelation(prime, True)
            self.assertEqual(trivial, [prime - 1] + [prime - 2] * (prime - 1))
            self.assertEqual(quadratic, [prime - 1] + [-1] * (prime - 1))
            self.assertEqual(weight_barrier.fourier_power_from_correlation(trivial), 1)
            self.assertEqual(
                weight_barrier.fourier_power_from_correlation(quadratic), prime
            )

    def test_barrier_formula_and_reconstruction(self) -> None:
        row = weight_barrier.barrier_row(5, 3)
        self.assertEqual(row["selected_total_energy"], 215)
        self.assertEqual(row["selected_average_energy"], str(Fraction(215, 7)))
        self.assertEqual(row["interferometer"], str(Fraction(-208, 7)))
        self.assertEqual(row["exact_reconstruction"], "1")
        self.assertFalse(row["interferometer_has_literal_atomic_diagonal"])

    def test_one_curve_obstruction(self) -> None:
        for prime in (3, 5, 13):
            row = weight_barrier.barrier_row(prime, 1)
            self.assertEqual(row["interferometer"], str(1 - prime))
            self.assertEqual(row["principal_energy"], 1)

    def test_resource_firewall_and_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            weight_barrier.additive_autocorrelation(31, False)
        with self.assertRaises(ValueError):
            weight_barrier.additive_autocorrelation(9, True)
        with self.assertRaises(ValueError):
            weight_barrier.barrier_row(5, True)
        with self.assertRaises(ValueError):
            weight_barrier.barrier_row(5, 6)

    def test_canonical_payload_caps(self) -> None:
        payload = weight_barrier.run()
        caps = payload["resource_caps"]
        self.assertEqual(caps["point_counts"], 0)
        self.assertEqual(caps["floating_point_operations"], 0)
        self.assertLessEqual(caps["largest_autocorrelation_cells"], 29**2)
        for row in payload["panels"]:
            self.assertEqual(row["exact_reconstruction"], "1")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_chebyshev_step_autocorrelation_normal_form.py"
)
SPEC = importlib.util.spec_from_file_location("chebyshev_step_corr", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Chebyshev-step autocorrelation producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ChebyshevStepAutocorrelationNormalFormTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_heights(self) -> None:
        self.assertEqual([subject.step_height(r) for r in range(4)], [1, 4, 32, 384])

    def test_cell_boundaries(self) -> None:
        self.assertEqual(subject.cell_boundaries(0), (0.0, 1.0))
        order_one = subject.cell_boundaries(1)
        self.assertAlmostEqual(order_one[1], 0.5)
        order_two = subject.cell_boundaries(2)
        self.assertAlmostEqual(order_two[1], 0.25)
        self.assertAlmostEqual(order_two[2], 0.75)

    def test_derivative_weights(self) -> None:
        self.assertEqual(subject.derivative_weights(0), (1, -1))
        self.assertEqual(subject.derivative_weights(1), (1, -2, 1))
        self.assertEqual(subject.derivative_weights(2), (1, -2, 2, -1))

    def test_minimum_cell_width(self) -> None:
        self.assertAlmostEqual(subject.minimum_cell_width(0), 1)
        self.assertAlmostEqual(subject.minimum_cell_width(1), 0.5)
        self.assertAlmostEqual(subject.minimum_cell_width(2), 0.25)

    def test_origin_curvature_mass(self) -> None:
        for order in range(20):
            self.assertEqual(subject.curvature_origin_mass(order), 2 * (2 * order + 1))

    def test_exact_small_lag_law(self) -> None:
        for order in range(9):
            delta = subject.minimum_cell_width(order)
            for fraction in (0.1, 0.5, 0.9):
                lag = fraction * delta
                expected = 1 - (2 * order + 1) * lag
                self.assertAlmostEqual(
                    subject.normalized_correlation(order, lag), expected, places=11
                )
                self.assertAlmostEqual(
                    subject.normalized_correlation(order, -lag), expected, places=11
                )

    def test_correlation_support_and_energy(self) -> None:
        for order in range(5):
            self.assertAlmostEqual(subject.normalized_correlation(order, 0), 1)
            self.assertAlmostEqual(subject.normalized_correlation(order, 1.1), 0)

    def test_curvature_symmetry_and_total_mass(self) -> None:
        for order in range(7):
            atoms = dict(subject.normalized_curvature_atoms(order))
            self.assertEqual(sum(atoms.values()), 0)
            for lag, weight in atoms.items():
                self.assertEqual(weight, atoms.get(round(-lag, 14)))
            self.assertEqual(atoms[0.0], 2 * (2 * order + 1))

    def test_local_zero_threshold(self) -> None:
        self.assertEqual(
            [subject.local_zero_inside_cusp(r) for r in range(9)],
            [True, True, True, True, False, False, False, False, False],
        )

    def test_resolution_asymptotic(self) -> None:
        for order in (100, 1000):
            scaled = (
                subject.minimum_cell_width(order) * 4 * (order + 1) ** 2 / math.pi**2
            )
            self.assertAlmostEqual(scaled, 1, delta=0.001)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["exact_small_lag_cusp"], "PROVED")
        self.assertEqual(
            ledger["local_cusp_locates_first_autocorrelation_zero_for_all_r"],
            "REFUTED FOR r>=4",
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_raw_curvature_pairs"], 100)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["quadratures"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.step_height(-1)
        with self.assertRaises(ValueError):
            subject.cell_boundaries(-1)
        with self.assertRaises(ValueError):
            subject.minimum_cell_width(-1)


if __name__ == "__main__":
    unittest.main()

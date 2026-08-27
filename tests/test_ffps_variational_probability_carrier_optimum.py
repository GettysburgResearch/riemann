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
    / "ffps_variational_probability_carrier_optimum.py"
)
SPEC = importlib.util.spec_from_file_location("variational_carrier", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load variational carrier producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class VariationalProbabilityCarrierOptimumTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_density_normalization_and_boundary(self) -> None:
        support = 2.5
        self.assertEqual(subject.optimal_density(support, 0.0), 0.0)
        self.assertEqual(subject.optimal_density(support, support), 0.0)
        mass = 6.0 / support**3 * (support**3 / 2.0 - support**3 / 3.0)
        self.assertAlmostEqual(mass, 1.0)

    def test_minimum_and_pythagorean_excess(self) -> None:
        support = 2.0
        self.assertAlmostEqual(subject.minimum_diagonal(support), 1.5)
        coefficient = 0.1
        self.assertGreater(subject.competitor_excess(support, coefficient), 0.0)
        self.assertEqual(subject.competitor_excess(support, 0.0), 0.0)

    def test_autocorrelation_formula(self) -> None:
        support = 2.0
        self.assertAlmostEqual(
            subject.autocorrelation(support, 0.0),
            subject.minimum_diagonal(support),
        )
        node = subject.annulus_node(support)
        self.assertAlmostEqual(subject.autocorrelation(support, node), 0.0)
        self.assertLess(subject.autocorrelation(support, 0.75 * support), 0.0)
        self.assertEqual(subject.autocorrelation(support, 1.1 * support), 0.0)

    def test_fourier_formula_has_correct_origin(self) -> None:
        for support in (1.0, 2.0, 4.0):
            self.assertEqual(subject.density_fourier(support, 0.0), 1.0 + 0.0j)
            small = subject.density_fourier(support, 1.0e-6)
            self.assertLessEqual(abs(small), 1.0 + 1.0e-12)

    def test_notch_roots(self) -> None:
        expected = (4.493409457909064, 7.725251836937707, 10.904121659428899)
        for index, target in enumerate(expected, 1):
            root = subject.notch_root(index)
            self.assertAlmostEqual(root, target, places=13)
            self.assertAlmostEqual(math.tan(root), root, places=10)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["unique_variational_minimizer"], "PROVED")
        self.assertEqual(ledger["beta_energy_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.minimum_diagonal(0.0)
        with self.assertRaises(ValueError):
            subject.notch_root(0)
        with self.assertRaises(ValueError):
            subject.density_fourier(2.0, math.inf)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import json
import math
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
    / "ffps_chebyshev_bv_kernel_extremizer.py"
)
SPEC = importlib.util.spec_from_file_location("chebyshev_bv", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Chebyshev-BV producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ChebyshevBVKernelExtremizerTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_minimax_errors(self) -> None:
        self.assertEqual(
            [subject.chebyshev_minimax_error(r) for r in range(4)],
            [Fraction(1, 2), Fraction(1, 8), Fraction(1, 32), Fraction(1, 128)],
        )

    def test_monic_residuals(self) -> None:
        self.assertEqual(
            subject.monic_minimax_residual(0),
            (Fraction(-1, 2), Fraction(1)),
        )
        self.assertEqual(
            subject.monic_minimax_residual(1),
            (Fraction(1, 8), Fraction(-1), Fraction(1)),
        )
        for order in range(7):
            self.assertEqual(subject.monic_minimax_residual(order)[-1], 1)

    def test_second_kind_l1_residuals(self) -> None:
        self.assertEqual(
            [subject.second_kind_l1_error(r) for r in range(4)],
            [Fraction(1), Fraction(1, 4), Fraction(1, 16), Fraction(1, 64)],
        )
        self.assertEqual(
            subject.monic_l1_residual(2),
            (Fraction(3, 16), Fraction(-1), Fraction(1)),
        )
        for order in range(7):
            self.assertEqual(subject.monic_l1_residual(order)[-1], 1)

    def test_sharp_variation(self) -> None:
        self.assertEqual(
            [subject.sharp_variation(r) for r in range(4)],
            [2, 16, 192, 3072],
        )

    def test_step_height_and_bv_size(self) -> None:
        self.assertEqual(
            [subject.extremal_step_height(r) for r in range(4)],
            [1, 4, 32, 384],
        )
        self.assertEqual(
            [subject.extremal_bv_size(r) for r in range(3)],
            [3, 20, 224],
        )
        for order in range(7):
            self.assertEqual(
                subject.extremal_step_height(order), subject.sharp_supremum(order)
            )

    def test_step_energy(self) -> None:
        self.assertEqual(
            [subject.extremal_step_energy(r) for r in range(4)],
            [1, 16, 1024, 147456],
        )

    def test_energy_gap_ratios(self) -> None:
        self.assertEqual(subject.energy_gap_ratio(0), 1)
        self.assertEqual(subject.energy_gap_ratio(1), Fraction(4, 3))
        self.assertEqual(subject.energy_gap_ratio(2), Fraction(64, 45))
        self.assertEqual(subject.energy_gap_ratio(3), Fraction(256, 175))
        self.assertAlmostEqual(
            float(subject.energy_gap_ratio(100)), math.pi / 2, places=2
        )

    def test_atom_moments(self) -> None:
        for order in range(7):
            atoms = subject.extremal_atoms(order)
            for lower in range(order + 1):
                self.assertAlmostEqual(
                    subject.numerical_atom_moment(atoms, lower), 0.0, places=7
                )
            self.assertAlmostEqual(
                subject.numerical_atom_moment(atoms, order + 1),
                (-1) ** (order + 1) * math.factorial(order + 1),
                places=6,
            )

    def test_first_atom_patterns(self) -> None:
        order_one = subject.extremal_atoms(1)
        self.assertEqual(
            [weight for _, weight in order_one],
            [Fraction(4), Fraction(-8), Fraction(4)],
        )
        order_zero = subject.extremal_atoms(0)
        self.assertEqual(
            [weight for _, weight in order_zero], [Fraction(-1), Fraction(1)]
        )

    def test_external_input(self) -> None:
        external = subject.run()["classical_external_input"]
        self.assertEqual(external["url"], "https://dlmf.nist.gov/18.38")

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["unique_alternating_step_extremizer"], "PROVED")
        self.assertEqual(
            ledger["BV_extremizer_also_minimizes_sup_plus_variation"],
            "PROVED",
        )
        self.assertEqual(
            ledger["new_beta_cancellation_or_unconditional_estimate"], "NOT PROVED"
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_information_order"], 6)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["root_searches"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.chebyshev_minimax_error(-1)
        with self.assertRaises(ValueError):
            subject.extremal_weight_scale(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.shifted_chebyshev_polynomial(-1)
        with self.assertRaises(ValueError):
            subject.extremal_atoms(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.numerical_atom_moment(subject.extremal_atoms(1), -1)


if __name__ == "__main__":
    unittest.main()

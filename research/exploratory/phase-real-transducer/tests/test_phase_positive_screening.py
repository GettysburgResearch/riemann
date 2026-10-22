from __future__ import annotations

import math
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from phase_positive_screening import (  # noqa: E402
    CriticalPoint,
    finite_hermite_source_resolvent,
    finite_partial_fraction_resolvent,
    mirrored_screening_field,
    partial_fraction_coefficients,
    rectangle_argument_ledger,
    screening_overlap_numeric,
    symmetric_resolvent_energy,
    symmetric_resolvent_response,
    two_point_toeplitz_eigenvalues,
)


class PhasePositiveScreeningTests(unittest.TestCase):
    def test_partial_fraction_coefficients(self) -> None:
        rate = 1.7
        for order in range(1, 6):
            coefficients = partial_fraction_coefficients(rate, order)
            for z in (0.2 + 0.7j, -0.4 + 1.1j):
                reconstructed = sum(
                    coefficients[k - 1]
                    * ((rate - z) ** (-k) + (rate + z) ** (-k))
                    for k in range(1, order + 1)
                )
                target = (rate * rate - z * z) ** (-order)
                self.assertLess(abs(reconstructed - target), 1e-12)

    def test_hermite_source_identity(self) -> None:
        zeros = (
            0.2 + 3.0j,
            0.2 - 3.0j,
            -0.2 + 3.0j,
            -0.2 - 3.0j,
        )
        z = 1.4 + 0.6j
        source = finite_hermite_source_resolvent(
            z,
            zeros,
            rate=1.2,
            order=2,
        )
        direct = finite_partial_fraction_resolvent(
            z,
            zeros,
            rate=1.2,
            order=2,
        )
        self.assertLess(abs(source - direct), 1e-11)

    def test_line_zero_model_is_two_point_positive(self) -> None:
        zeros = (3.0j, -3.0j, 5.0j, -5.0j)
        s0 = symmetric_resolvent_response(0.0, zeros, rate=1.0, order=2).real
        st = symmetric_resolvent_response(1.0, zeros, rate=1.0, order=2).real
        low, high = two_point_toeplitz_eigenvalues(s0, st)
        self.assertGreaterEqual(low, -1e-14)
        self.assertGreater(high, 0.0)

    def test_off_axis_quartet_has_two_point_witness(self) -> None:
        delta = 0.2
        gamma = 3.0
        zeros = (
            delta + 1j * gamma,
            delta - 1j * gamma,
            -delta + 1j * gamma,
            -delta - 1j * gamma,
        )
        s0 = symmetric_resolvent_response(0.0, zeros, rate=1.0, order=2).real
        st = symmetric_resolvent_response(0.98, zeros, rate=1.0, order=2).real
        low, _ = two_point_toeplitz_eigenvalues(s0, st)
        self.assertLess(low, 0.0)

    def test_energy_boundary_rejected(self) -> None:
        zeros = (0.2 + 3.0j, 0.2 - 3.0j, -0.2 + 3.0j, -0.2 - 3.0j)
        with self.assertRaises(ValueError):
            symmetric_resolvent_energy(0.2, zeros, rate=1.0, order=2)
        self.assertGreater(
            symmetric_resolvent_energy(0.3, zeros, rate=1.0, order=2),
            0.0,
        )

    def test_poisson_screening_identity(self) -> None:
        points = (
            CriticalPoint(-0.4, -1.0),
            CriticalPoint(-0.2, 1.5),
            CriticalPoint(0.3, -0.2),
        )
        positive, overlap, negative, n_left, n_right = screening_overlap_numeric(
            0.0,
            points,
            cutoff=500.0,
            panels=100_000,
        )
        self.assertEqual((n_left, n_right), (2, 1))
        self.assertLess(abs(positive - (math.pi * n_left - overlap)), 5e-3)
        self.assertLess(abs(negative - (math.pi * n_right - overlap)), 5e-3)

    def test_mirror_screening_firewall(self) -> None:
        for t in (-10.0, -1.0, 0.0, 2.5, 11.0):
            self.assertAlmostEqual(
                mirrored_screening_field(
                    t,
                    observation_sigma=0.0,
                    distance=0.4,
                    ordinate=1.2,
                ),
                0.0,
                places=14,
            )

    def test_rectangle_argument_ledger(self) -> None:
        zeros = (
            0.1 + 0.3j,
            0.3 + 1.2j,
            0.7 + 0.5j,
            -0.5 + 0.4j,
        )
        change, count = rectangle_argument_ledger(
            zeros,
            sigma_left=-0.2,
            sigma_right=0.5,
            t_bottom=-0.5,
            t_top=1.8,
            quadrature_steps=20_000,
        )
        self.assertEqual(count, 2)
        self.assertLess(abs(change - 2.0 * math.pi * count), 2e-7)


if __name__ == "__main__":
    unittest.main()

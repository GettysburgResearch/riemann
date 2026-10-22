from __future__ import annotations

import math
import pathlib
import sys
import unittest

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from phase_resolvent import (  # noqa: E402
    TAU,
    curvature_defect_zero_count_bound,
    finite_laplace_resolvent,
    finite_resolvent_energy,
    finite_taylor_remainder_resolvent,
    first_twenty_centered_zero_model,
    forced_lag_classes,
    gamma_resolvent_zero_sum,
    hardy_clockwise_convexity_numerator,
    minimum_absolute_curvature_for_span,
    open_petal_signed_turn,
    petal_is_forced_simple_from_span,
    simple_petal_total_turn,
    source_resolvent_truncation,
)


class FlowerTurningTests(unittest.TestCase):
    def test_open_turn_is_profile_independent_formula(self) -> None:
        span = 1.37 * math.pi
        self.assertAlmostEqual(open_petal_signed_turn(span), -span - math.pi)

    def test_simple_closed_turn_is_minus_two_pi(self) -> None:
        for span in (0.4 * math.pi, math.pi, 1.8 * math.pi, TAU):
            self.assertAlmostEqual(simple_petal_total_turn(span), -TAU)

    def test_self_intersection_threshold_and_lag_classes(self) -> None:
        self.assertTrue(petal_is_forced_simple_from_span(TAU))
        self.assertFalse(petal_is_forced_simple_from_span(TAU + 1e-9))
        self.assertEqual(forced_lag_classes(TAU), 0)
        self.assertEqual(forced_lag_classes(2.1 * math.pi), 1)
        self.assertEqual(forced_lag_classes(4.1 * math.pi), 2)

    def test_curvature_defect_bound(self) -> None:
        spans = (0.8 * math.pi, 1.2 * math.pi, 1.7 * math.pi)
        curvatures = [minimum_absolute_curvature_for_span(span) for span in spans]
        lower = curvature_defect_zero_count_bound(sum(spans), curvatures)
        self.assertLessEqual(lower, len(spans) + 1e-12)
        self.assertAlmostEqual(lower, 2.8)

    def test_real_convexity_numerator_matches_angular_formula(self) -> None:
        theta_p = 2.3
        theta_pp = -0.17
        z = 1.2
        z_p = -0.4
        z_pp = 0.9
        r_phi = z_p / theta_p
        r_phi_phi = z_pp / theta_p**2 - z_p * theta_pp / theta_p**3
        angular_numerator = z * r_phi_phi - z * z - 2.0 * r_phi**2
        real_numerator = hardy_clockwise_convexity_numerator(
            theta_p, theta_pp, z, z_p, z_pp
        )
        self.assertAlmostEqual(theta_p**2 * angular_numerator, -real_numerator)


class ResolventTests(unittest.TestCase):
    def test_safe_taylor_remainder_matches_zero_resolvent(self) -> None:
        zeros = (0.2 + 3j, 0.2 - 3j, -0.2 + 3j, -0.2 - 3j)
        for order in (1, 2, 3, 4):
            with self.subTest(order=order):
                probe = 1.3 + 0.7j
                direct = finite_laplace_resolvent(
                    probe, zeros, rate=2.0, order=order
                )
                remainder = finite_taylor_remainder_resolvent(
                    probe, zeros, rate=2.0, order=order
                )
                self.assertAlmostEqual(direct.real, remainder.real, places=13)
                self.assertAlmostEqual(direct.imag, remainder.imag, places=13)

    def test_finite_energy_matches_numerical_quadrature_fixture(self) -> None:
        zeros = (0.2 + 3j, 0.2 - 3j, -0.2 + 3j, -0.2 - 3j)
        energy = finite_resolvent_energy(
            0.7,
            zeros,
            rate=2.0,
            order=3,
        )
        mp.mp.dps = 35
        mp_zeros = tuple(mp.mpc(value.real, value.imag) for value in zeros)
        numerical = mp.quad(
            lambda t: mp.e ** (-mp.mpf("1.4") * t)
            * abs(
                sum(
                    mp.e ** (value * t) / (mp.mpf(2) - value) ** 3
                    for value in mp_zeros
                )
            )
            ** 2,
            [0, mp.inf],
        )
        self.assertAlmostEqual(energy, float(numerical), places=13)
        with self.assertRaises(ValueError):
            finite_resolvent_energy(0.2, zeros, rate=2.0, order=3)

    def test_actual_xi_source_zero_regression(self) -> None:
        # FLOATING_RECONNAISSANCE regression in ordinary doubles.
        # The prime truncation and twenty-zero truncation are intentionally
        # compared only at a broad tolerance; the analytic theorem does not
        # depend on this numerical fixture.
        rate = 2.0
        order = 3
        for t in (0.25, 0.5, 1.0, 1.5):
            with self.subTest(t=t):
                source = source_resolvent_truncation(
                    t,
                    rate=rate,
                    order=order,
                    prime_limit=1_000_000,
                )
                zero_side = gamma_resolvent_zero_sum(
                    t,
                    first_twenty_centered_zero_model(),
                    rate=rate,
                    order=order,
                ).real
                self.assertLess(abs(source - zero_side), 1.0e-5)


if __name__ == "__main__":
    unittest.main()

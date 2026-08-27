from __future__ import annotations

import importlib.util
import json
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
    / "ffps_beta_carrier_legendre_moment_tower.py"
)
SPEC = importlib.util.spec_from_file_location("beta_carrier_moment_tower", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta carrier moment-tower producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BetaCarrierLegendreMomentTowerTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_parabolic_carrier_moments(self) -> None:
        self.assertEqual(
            subject.parabolic_carrier_moments(3),
            (Fraction(1), Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)),
        )
        self.assertEqual(
            subject.parabolic_carrier_moments(2, Fraction(2)),
            (Fraction(1), Fraction(1), Fraction(6, 5)),
        )

    def test_field_moment_coefficients(self) -> None:
        q = subject.parabolic_carrier_moments(3)
        self.assertEqual(subject.field_moment_coefficients(1, q), (Fraction(-1),))
        self.assertEqual(
            subject.field_moment_coefficients(2, q),
            (Fraction(-1), Fraction(-2)),
        )
        self.assertEqual(
            subject.field_moment_coefficients(3, q),
            (Fraction(-9, 10), Fraction(-3), Fraction(-3)),
        )

    def test_triangular_recovery(self) -> None:
        q = subject.parabolic_carrier_moments(4)
        beta = (Fraction(2), Fraction(-3), Fraction(5), Fraction(7))
        field = [Fraction(0)]
        for order in range(1, 5):
            coefficients = subject.field_moment_coefficients(order, q)
            field.append(sum(c * b for c, b in zip(coefficients, beta)))
        self.assertEqual(subject.recover_beta_moments(tuple(field), q), beta)

    def test_shifted_legendre_coefficients(self) -> None:
        self.assertEqual(subject.shifted_legendre_coefficients(0), (1,))
        self.assertEqual(subject.shifted_legendre_coefficients(1), (-1, 2))
        self.assertEqual(subject.shifted_legendre_coefficients(2), (1, -6, 6))
        self.assertEqual(subject.shifted_legendre_coefficients(3), (-1, 12, -30, 20))

    def test_shifted_legendre_orthogonality(self) -> None:
        for left in range(7):
            for right in range(7):
                value = subject.polynomial_inner_product(
                    subject.shifted_legendre_coefficients(left),
                    subject.shifted_legendre_coefficients(right),
                )
                expected = Fraction(1, 2 * left + 1) if left == right else Fraction(0)
                self.assertEqual(value, expected)

    def test_legendre_delta_coefficients(self) -> None:
        length = Fraction(2)
        self.assertEqual(
            subject.legendre_delta_coefficients(1, length),
            (Fraction(-2), Fraction(2)),
        )
        self.assertEqual(
            subject.legendre_delta_coefficients(2, length),
            (Fraction(4), Fraction(-12), Fraction(6)),
        )

    def test_first_adjusted_beta_channels(self) -> None:
        q = subject.parabolic_carrier_moments(3)
        length = Fraction(2)
        self.assertEqual(
            subject.adjusted_beta_channel_coefficients(1, q, length),
            (Fraction(1),),
        )
        self.assertEqual(
            subject.adjusted_beta_channel_coefficients(2, q, length),
            (Fraction(-1, 2), Fraction(1)),
        )
        self.assertEqual(
            subject.adjusted_beta_channel_coefficients(3, q, length),
            (Fraction(1, 10), Fraction(-1), Fraction(1)),
        )

    def test_energy_constants(self) -> None:
        self.assertEqual(
            [subject.legendre_energy_constant(order) for order in range(1, 4)],
            [12, 720, 25200],
        )

    def test_uniform_forward_multiplier(self) -> None:
        self.assertEqual(
            subject.uniform_forward_multiplier(1, Fraction(7), Fraction(3, 2)),
            Fraction(3),
        )
        self.assertEqual(
            subject.uniform_forward_multiplier(3, Fraction(2), Fraction(1)),
            Fraction(24),
        )

    def test_autocorrelation_moments(self) -> None:
        moments = (Fraction(0), Fraction(2), Fraction(3), Fraction(5), Fraction(7))
        self.assertEqual(subject.autocorrelation_moment(moments, 1), 0)
        self.assertEqual(subject.autocorrelation_moment(moments, 2), -8)
        self.assertEqual(subject.autocorrelation_moment(moments, 3), 0)
        self.assertEqual(subject.autocorrelation_moment(moments, 4), -26)

    def test_autocorrelation_term_coefficients(self) -> None:
        self.assertEqual(
            subject.autocorrelation_term_coefficients(4),
            {"M_0*M_4": 2, "M_1*M_3": -8, "M_2*M_2": 6},
        )

    def test_spectral_derivative_sign(self) -> None:
        moments = (Fraction(0), Fraction(2), Fraction(3), Fraction(5), Fraction(7))
        self.assertEqual(subject.spectral_even_derivative(moments, 1), 8)
        self.assertEqual(subject.spectral_even_derivative(moments, 2), -26)

    def test_pole_order(self) -> None:
        self.assertEqual(subject.pole_order_after_moment(1, 1), 1)
        self.assertEqual(subject.pole_order_after_moment(3, 5), 7)

    def test_moving_carrier_cancels_second_field_moment(self) -> None:
        beta_0 = Fraction(2)
        beta_1 = Fraction(-3)
        q_1 = subject.moving_carrier_cancellation_first_moment(beta_0, beta_1)
        self.assertEqual(q_1, Fraction(3, 2))
        coefficients = subject.field_moment_coefficients(2, (Fraction(1), q_1))
        self.assertEqual(coefficients[0] * beta_0 + coefficients[1] * beta_1, 0)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["all_order_exponential_generating_identity"], "PROVED")
        self.assertEqual(
            ledger["fixed_polynomial_power_exponent_equivalence"], "PROVED"
        )
        self.assertEqual(ledger["RH_forward_growing_order_window"], "PROVED")
        self.assertEqual(ledger["moving_carrier_M_2_tuning_no_go"], "PROVED")
        self.assertEqual(ledger["growing_order_converse_or_equivalence"], "NOT PROVED")
        self.assertEqual(
            ledger["critical_line_zero_multiplicity_theorem"], "NOT PROVED"
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.parabolic_carrier_moments(-1)
        with self.assertRaises(ValueError):
            subject.parabolic_carrier_moments(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.field_moment_coefficients(0, (Fraction(1),))
        with self.assertRaises(ValueError):
            subject.recover_beta_moments((Fraction(1), Fraction(2)), (Fraction(1),))
        with self.assertRaises(ValueError):
            subject.shifted_legendre_coefficients(-1)
        with self.assertRaises(ValueError):
            subject.legendre_delta_coefficients(1, Fraction(0))
        with self.assertRaises(ValueError):
            subject.uniform_forward_multiplier(0, Fraction(1), Fraction(1))
        with self.assertRaises(ValueError):
            subject.uniform_forward_multiplier(1, Fraction(1), Fraction(-1))
        with self.assertRaises(ValueError):
            subject.autocorrelation_moment((Fraction(0),), 1)
        with self.assertRaises(ValueError):
            subject.spectral_even_derivative((Fraction(0),), -1)
        with self.assertRaises(ValueError):
            subject.pole_order_after_moment(0, 1)
        with self.assertRaises(ValueError):
            subject.moving_carrier_cancellation_first_moment(Fraction(0), Fraction(1))


if __name__ == "__main__":
    unittest.main()

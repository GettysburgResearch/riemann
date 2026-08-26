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
    / "ffps_primitive_rho_tilt_convolution_isomorphism.py"
)
SPEC = importlib.util.spec_from_file_location("primitive_rho_convolution", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class PrimitiveRhoTiltConvolutionIsomorphismTest(unittest.TestCase):
    def test_predecessor_blobs(self) -> None:
        subject.check_predecessor_blobs()
        subject.check_scope_markers()

    def test_exact_local_coefficients(self) -> None:
        self.assertEqual(subject.g_prime_power(2, 0), 1)
        self.assertEqual(subject.g_prime_power(2, 4), Fraction(1, 3))
        self.assertEqual(subject.h_prime_power(2, 4), Fraction(-8, 81))
        panel = subject.local_coefficient_panel(5, 7)
        self.assertEqual(panel["rho_p"], "5/6")
        self.assertEqual(len(panel["rows"]), 8)
        self.assertTrue(all(row["a"] == row["m_times_g"] for row in panel["rows"]))
        self.assertTrue(all(row["m"] == row["a_times_h"] for row in panel["rows"]))
        self.assertTrue(all(row["delta"] == row["g_times_h"] for row in panel["rows"]))

    def test_exact_global_convolutions(self) -> None:
        for n in range(1, 181):
            if n % subject.EXCEPTIONAL_PRIME == 0:
                continue
            with self.subTest(n=n):
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.m, subject.g, n),
                    subject.a(n),
                )
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.a, subject.h, n),
                    subject.m(n),
                )
                self.assertEqual(
                    subject.dirichlet_convolution_value(subject.g, subject.h, n),
                    subject.delta(n),
                )

    def test_multiplicative_values(self) -> None:
        self.assertEqual(subject.rho(30), Fraction(5, 12))
        self.assertEqual(subject.a(30), Fraction(-5, 12))
        self.assertEqual(subject.g(12), Fraction(1, 12))
        self.assertEqual(subject.h(12), Fraction(1, 18))

    def test_finite_operator_inverse(self) -> None:
        certificate = subject.finite_operator_certificate(32)
        self.assertEqual(certificate["dimension"], 32)
        self.assertTrue(certificate["inverse_both_orders"])
        self.assertTrue(certificate["unit_diagonal"])

    def test_exact_summatory_transfers(self) -> None:
        transfer = subject.summatory_transfer_panel(90)
        exceptional = subject.exceptional_prime_transfer_panel(150)
        self.assertEqual(transfer["checked_endpoints"], 90)
        self.assertEqual(exceptional["checked_endpoints"], 150)
        self.assertTrue(
            all(
                row["M_rho"] == row["M_rho_from_g"] and row["M_0"] == row["M_0_from_h"]
                for row in transfer["sample_rows"]
            )
        )
        self.assertTrue(
            all(
                row["M"] == row["M_from_M_0"] and row["M_0"] == row["M_0_from_M"]
                for row in exceptional["sample_rows"]
            )
        )

    def test_half_weighted_pair_coefficients(self) -> None:
        panel = subject.pair_coefficient_panel()
        for row in panel["rows_after_clearing_common_half_weight"]:
            self.assertEqual(
                row["rho_scaled_coefficient"],
                row["rho_via_g_scaled_coefficient"],
            )
            self.assertEqual(
                row["ordinary_scaled_coefficient"],
                row["ordinary_via_h_scaled_coefficient"],
            )

    def test_convergence_majorants_are_exactly_positive(self) -> None:
        rows = subject.convergence_majorant_panel()
        self.assertEqual([row["prime"] for row in rows], list(subject.REPLAY_PRIMES))
        self.assertTrue(
            all(row["g_bound_square_margin_9p_minus_16"] >= 0 for row in rows)
        )
        self.assertTrue(
            all(
                Fraction(row["h_bound_square_margin_p2_over_4_plus_1"]) > 0
                for row in rows
            )
        )

    def test_canonical_fixture_and_firewall(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertTrue(
            result["summatory_seminorm_transfer"]["mertens_exponents_coincide"]
        )
        scope = result["scope_firewall"]
        self.assertFalse(scope["sharp_finite_height_blocks_preserved"])
        self.assertFalse(scope["coprimality_preserved_by_dilation"])
        self.assertFalse(scope["ratio_kernel_preserved"])
        self.assertFalse(scope["dyadic_endpoint_structure_preserved"])
        self.assertFalse(scope["uniform_induced_dilation_estimate_proved"])
        self.assertFalse(scope["primcar_estimate_proved"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.rho(0)
        with self.assertRaises(ValueError):
            subject.g(67)
        with self.assertRaises(ValueError):
            subject.g_prime_power(67, 1)
        with self.assertRaises(ValueError):
            subject.h_prime_power(4, 1)
        with self.assertRaises(ValueError):
            subject.local_coefficient_panel(2, -1)
        with self.assertRaises(ValueError):
            subject.multiply_matrices(
                [[Fraction(1)]],
                [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]],
            )


if __name__ == "__main__":
    unittest.main()

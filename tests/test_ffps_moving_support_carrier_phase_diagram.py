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
    / "ffps_moving_support_carrier_phase_diagram.py"
)
SPEC = importlib.util.spec_from_file_location("moving_support_phase", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load moving-support phase producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class MovingSupportCarrierPhaseDiagramTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_parabolic_norms(self) -> None:
        norms = subject.parabolic_norms(2.0)
        self.assertAlmostEqual(norms["detector_L2_squared"], 1.5)
        self.assertAlmostEqual(norms["detector_supremum"], 1.5)
        self.assertAlmostEqual(norms["detector_total_variation"], 6.0)

    def test_centered_test_norm_and_extremizer(self) -> None:
        self.assertAlmostEqual(subject.centered_test_norm_squared(2.0), 2.0 / 3.0)
        extremal_energy = subject.parabolic_norms(2.0)["detector_L2_squared"]
        self.assertAlmostEqual(subject.sharp_prefix_bound(extremal_energy, 2.0), 1.0)

    def test_all_support_parabolic_forward_cost(self) -> None:
        log_x = 100.0
        upper = 900.0 * (1.0 + log_x) ** 4
        for support in (1.0, 100.0, 1.0e12):
            self.assertLessEqual(
                subject.parabolic_renormalized_forward_cost(log_x, support),
                upper,
            )

    def test_critical_renormalization_exponent(self) -> None:
        self.assertAlmostEqual(subject.trivial_dilution_schedule_exponent(0.0), 1 / 3)
        self.assertAlmostEqual(subject.trivial_dilution_schedule_exponent(1.0), 1 / 2)
        self.assertAlmostEqual(subject.trivial_dilution_schedule_exponent(2.0), 1.0)

    def test_projected_exponential_variance(self) -> None:
        for z in (1.0e-6, 0.01, 0.1, 1.0, 10.0):
            variance = subject.projected_exponential_variance(z)
            self.assertGreater(variance, 0.0)
            self.assertLessEqual(variance, z**2 / 12.0 + 1.0e-14)
            self.assertLessEqual(variance, 1.0 / (2.0 * z) + 1.0e-14)
        field_length = 2.0
        alpha = 1.0e-6
        self.assertAlmostEqual(
            subject.projected_laplace_cost(field_length, alpha),
            field_length**1.5 / math.sqrt(12.0),
            places=5,
        )

    def test_autocorrelation_second_moment(self) -> None:
        self.assertEqual(subject.autocorrelation_second_moment(3.0), -18.0)

    def test_pythagorean_energy(self) -> None:
        self.assertAlmostEqual(subject.pythagorean_energy(1.0, 2.0, 0.0), 1.5)
        self.assertAlmostEqual(subject.pythagorean_energy(1.0, 2.0, 0.25), 1.75)

    def test_reverse_choice_has_fixed_half_margin(self) -> None:
        for slope in (0.0, 1.0, 3.0, 20.0):
            row = subject.reverse_abscissa_choice(slope, 0.2)
            self.assertAlmostEqual(row["margin_to_target"], 0.1)
            self.assertLess(row["convergence_abscissa"], 0.2)

    def test_optimized_laplace_parameter(self) -> None:
        for support in (2.0, 10.0, 100.0):
            alpha = subject.optimized_laplace_parameter(support)
            self.assertAlmostEqual(alpha * support, 1.5)

    def test_zero_exclusion_wedge_meets_cubic_escape(self) -> None:
        self.assertAlmostEqual(subject.zero_exclusion_boundary(0.0), 0.5)
        self.assertAlmostEqual(subject.zero_exclusion_boundary(1.0 / 3.0), 1.0)

    def test_cubic_escape_flattens_trivial_bound(self) -> None:
        for log_x in subject.LOG_X_ROWS:
            log_bound = subject.trivial_log_energy_bound(log_x, log_x / 3.0)
            self.assertAlmostEqual(log_bound, math.log(192.0))

    def test_logarithmic_support_remains_power_sized_trivially(self) -> None:
        log_x = 1600.0
        log_bound = subject.trivial_log_energy_bound(log_x, math.log(log_x))
        self.assertGreater(log_bound / log_x, 0.9)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["sharp_centered_support_energy_inequality"], "PROVED")
        self.assertEqual(ledger["exact_signed_autocorrelation_second_moment"], "PROVED")
        self.assertEqual(
            ledger["exact_pythagorean_mertens_shape_decomposition"], "PROVED"
        )
        self.assertEqual(
            ledger["exact_projected_finite_alpha_carrier_inequality"], "PROVED"
        )
        self.assertEqual(
            ledger["comparable_weight_and_multiscale_abstract_no_improvement"],
            "PROVED",
        )
        self.assertEqual(
            ledger["parabolic_forward_gate_for_all_supports_at_least_one"],
            "PROVED",
        )
        self.assertEqual(
            ledger["all_support_parabolic_renormalized_RH_equivalence"],
            "PROVED",
        )
        self.assertEqual(
            ledger["subcubic_width_power_trivial_dilution_schedule"], "PROVED"
        )
        self.assertEqual(ledger["supercubic_all_support_forward_gate"], "NOT PROVED")
        self.assertEqual(ledger["subpower_support_reverse_RH_gate"], "PROVED")
        self.assertEqual(ledger["positive_power_support_full_RH_gate"], "NOT PROVED")
        self.assertEqual(
            ledger["arithmetic_improvement_over_centered_wedge"], "NOT PROVED"
        )
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.parabolic_norms(0.0)
        with self.assertRaises(ValueError):
            subject.centered_test_norm_squared(0.0)
        with self.assertRaises(ValueError):
            subject.sharp_prefix_bound(-1.0, 2.0)
        with self.assertRaises(ValueError):
            subject.parabolic_renormalized_forward_cost(1.0, 0.5)
        with self.assertRaises(ValueError):
            subject.trivial_dilution_schedule_exponent(3.0)
        with self.assertRaises(ValueError):
            subject.projected_exponential_variance(-1.0)
        with self.assertRaises(ValueError):
            subject.projected_laplace_cost(1.0, 0.0)
        with self.assertRaises(ValueError):
            subject.autocorrelation_second_moment(math.inf)
        with self.assertRaises(ValueError):
            subject.pythagorean_energy(1.0, 2.0, -1.0)
        with self.assertRaises(ValueError):
            subject.reverse_abscissa_choice(-1.0, 0.2)
        with self.assertRaises(ValueError):
            subject.trivial_log_energy_bound(0.0, 1.0)


if __name__ == "__main__":
    unittest.main()

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
    / "ffps_compact_kernel_finite_spectral_factor_surgery.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("compact_spectral_surgery", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load compact spectral-factor surgery producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsCompactKernelFiniteSpectralFactorSurgeryTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_reflection_is_an_involution(self) -> None:
        for point in (
            subject.RIGHT_REAL,
            subject.RIGHT_COMPLEX,
            subject.conjugate_zero(subject.RIGHT_COMPLEX),
        ):
            self.assertEqual(subject.reflect_zero(subject.reflect_zero(point)), point)
        self.assertEqual(
            subject.reflect_zero(subject.conjugate_zero(subject.RIGHT_COMPLEX)),
            subject.conjugate_zero(subject.reflect_zero(subject.RIGHT_COMPLEX)),
        )

    def test_exact_flow_composition_commutation_and_inverse(self) -> None:
        control = subject.divisor_flow_control()
        self.assertEqual(
            control["two_real_flips_sequential"], control["two_real_flips_direct"]
        )
        self.assertEqual(
            control["conjugate_pair_orbits_forward"],
            control["disjoint_orbit_reverse_order"],
        )
        self.assertEqual(
            control["inverse_flows_restore_initial"], control["initial_divisor"]
        )

    def test_elementary_factors_are_unitary_and_cancel_with_reflections(self) -> None:
        for real, imaginary in subject.ALLPASS_ZERO_SAMPLES:
            zero = complex(float(real), float(imaginary))
            reflected = -zero.conjugate()
            for frequency in subject.FREQUENCY_SAMPLES:
                spectral_point = complex(0.0, float(frequency))
                factor = subject.allpass_multiplier(zero, spectral_point)
                inverse = subject.allpass_multiplier(reflected, spectral_point)
                self.assertTrue(math.isclose(abs(factor), 1.0, rel_tol=1e-13))
                self.assertTrue(
                    math.isclose(
                        abs(factor * inverse - 1.0),
                        0.0,
                        rel_tol=0.0,
                        abs_tol=1e-12,
                    )
                )

    def test_conjugate_pair_factor_has_real_exact_coefficients(self) -> None:
        coefficients = subject.conjugate_pair_coefficients(subject.RIGHT_COMPLEX)
        self.assertEqual(
            coefficients["numerator"],
            (Fraction(5), Fraction(2), Fraction(1)),
        )
        self.assertEqual(
            coefficients["denominator"],
            (Fraction(5), Fraction(-2), Fraction(1)),
        )

    def test_mean_law_distinguishes_zero_and_nonzero_mean(self) -> None:
        self.assertEqual(subject.real_preserving_mean_sign(1), -1)
        self.assertEqual(subject.real_preserving_mean_sign(2), 1)
        self.assertEqual(subject.real_preserving_mean_sign(-3), -1)
        result = subject.run(check_sources=False)
        self.assertEqual(result["real_structure"]["zero_mean"], "preserved")
        self.assertIn("changes its sign", result["real_structure"]["nonzero_real_mean"])

    def test_explicit_jordan_l1_counterexample(self) -> None:
        self.assertEqual(sum(subject.JORDAN_WEIGHTS, Fraction(0)), Fraction(-1, 3))
        self.assertEqual(
            subject.jordan_root_polynomial(subject.JORDAN_EXPONENTIAL_ROOT), 0
        )
        control = subject.jordan_obstruction_control()
        self.assertGreater(
            control["flipped_positive_mass"], control["original_positive_mass"]
        )
        self.assertLess(
            control["flipped_negative_mass"], control["original_negative_mass"]
        )
        self.assertLess(control["flipped_l1_mass"], control["original_l1_mass"])
        self.assertLess(control["maximum_replayed_weight_error"], 1e-12)

    def test_scope_firewalls(self) -> None:
        result = subject.run(check_sources=False)
        ledger = result["proof_ledger"]
        self.assertEqual(ledger["arbitrary_infinite_allpass_product"], "NOT PROVED")
        self.assertEqual(
            ledger["global_minimum_phase_for_infinite_divisors"], "NOT PROVED"
        )
        self.assertEqual(ledger["any_beta_energy_estimate"], "NOT PROVED")
        self.assertEqual(ledger["rh_or_grh"], "NOT PROVED")
        self.assertTrue(
            any(
                "imaginary-axis zeros" in obstruction
                for obstruction in result["invariant_scope"]["fixed_obstructions"]
            )
        )

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
            fixture["proof_ledger"]["finite_rational_allpass_converse"],
            "PROVED EXACT",
        )
        self.assertEqual(fixture["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.apply_orbit_flow({subject.RIGHT_REAL: 0}, subject.RIGHT_REAL, 1)
        with self.assertRaises(ValueError):
            subject.apply_orbit_flow(
                {(Fraction(0), Fraction(1)): 1},
                (Fraction(0), Fraction(1)),
                1,
            )
        with self.assertRaises(ValueError):
            subject.conjugate_pair_coefficients((Fraction(1), Fraction(0)))
        with self.assertRaises(ValueError):
            subject.allpass_multiplier(1.0j, 1.0)
        with self.assertRaises(TypeError):
            subject.jordan_root_polynomial(0.75)


if __name__ == "__main__":
    unittest.main()

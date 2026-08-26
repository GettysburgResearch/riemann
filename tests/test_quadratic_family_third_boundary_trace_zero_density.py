"""Tests for the odd-notch minimum-degree-(h-2) boundary."""

from __future__ import annotations

import ast
import importlib.util
import itertools
import math
import subprocess
import sys
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
    / "quadratic_family_third_boundary_trace_zero_density.py"
)
NOTE_PATH = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_THIRD_BOUNDARY_TRACE_ZERO_DENSITY.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_third_boundary_trace_zero_density", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load third-boundary replay")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def independent_profiles(h_value: int) -> set[tuple[int, ...]]:
    """Tiny direct multiset check, independent of the replay recursion."""

    total = 4 * h_value + 1
    minimum = h_value - 2
    profiles: set[tuple[int, ...]] = set()
    degrees = range(minimum, total + 1)
    for factor_count in range(2, 5):
        for profile in itertools.combinations_with_replacement(degrees, factor_count):
            if profile[0] == minimum and sum(profile) == total:
                profiles.add(profile)
    return profiles


def direct_local_coefficients(
    q_value: int, sums: tuple[int, int, int, int, int]
) -> tuple[int, int]:
    """Multiply truncated formal Euler factors from aggregate sign sums."""

    coefficients = [1, 0, 0, 0, 0, 0]
    for degree, total in enumerate(sums, start=1):
        count = MODULE.irreducible_count(q_value, degree)
        if not MODULE.rademacher_attainable(count, total):
            raise ValueError("unattainable aggregate sign sum")
        signs = [1] * ((count + total) // 2) + [-1] * ((count - total) // 2)
        for sign in signs:
            updated = [0] * 6
            for old_degree, old_value in enumerate(coefficients):
                for exponent in range((5 - old_degree) // degree + 1):
                    updated[old_degree + exponent * degree] += (
                        old_value * sign**exponent
                    )
            coefficients = updated
    return coefficients[3] - q_value * coefficients[1], coefficients[5] - (
        q_value * coefficients[3]
    )


class QuadraticFamilyThirdBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_exact_residual_channels(self) -> None:
        h_value = 12
        examples = {
            (10, 39): ((1, 0, 0), "D5_zero"),
            (10, 10, 29): ((2, 0, 0), "D5_zero"),
            (10, 11, 28): ((1, 1, 0), "mixed_D5_D3"),
            (10, 12, 27): ((1, 0, 1), "nonzero_by_parity"),
            (10, 12, 12, 15): ((1, 0, 2), "fourth_order_D5_plus_2D1"),
        }
        for profile, (coefficients, branch) in examples.items():
            with self.subTest(profile=profile):
                self.assertEqual(
                    MODULE.notch_coefficients(profile, h_value), coefficients
                )
                self.assertEqual(
                    MODULE.classify_profile(h_value, profile)["branch"], branch
                )

    def test_independent_profile_and_parity_exhaustion(self) -> None:
        for h_value in (12, 15):
            profiles = set(MODULE.third_boundary_profiles(h_value))
            self.assertEqual(profiles, independent_profiles(h_value))
            parity_even = {
                profile for profile in profiles if profile.count(h_value) % 2 == 0
            }
            self.assertEqual(
                parity_even, set(MODULE.claimed_parity_even_profiles(h_value))
            )
            positive_even_h = {
                profile
                for profile in profiles
                if profile.count(h_value) > 0 and profile.count(h_value) % 2 == 0
            }
            self.assertEqual(
                positive_even_h,
                {(h_value - 2, h_value, h_value, h_value + 3)},
            )

    def test_harmonic_identity_and_exact_coefficients(self) -> None:
        for h_value in range(12, 61):
            self.assertEqual(
                MODULE.generic_direct_weight(h_value),
                MODULE.generic_harmonic_weight(h_value),
            )
        self.assertEqual(MODULE.H_MINUS_2, (Fraction(1, 3), Fraction(1, 3)))
        self.assertEqual(
            MODULE.H_MINUS_3_GENERIC,
            (Fraction(7, 12), Fraction(1, 3)),
        )
        self.assertEqual(MODULE.H_MINUS_3_REPEATED_MINIMUM, Fraction(1, 4))
        self.assertEqual(MODULE.H_MINUS_3_MIXED, Fraction(1, 2))
        self.assertEqual(
            MODULE.H_MINUS_3_D5_TOTAL,
            (Fraction(5, 6), Fraction(1, 3)),
        )

    def test_bounded_asymptotic_coefficients(self) -> None:
        h_value = 200
        c2 = (1 + math.log(2)) / 3
        generic_c3 = Fraction(7, 12) + math.log(2) / 3
        generic_estimate = h_value**3 * (
            float(MODULE.generic_harmonic_weight(h_value)) - c2 / h_value**2
        )
        self.assertLess(abs(generic_estimate - generic_c3), 0.02)
        self.assertLess(
            abs(h_value**3 * float(MODULE.repeated_minimum_weight(h_value)) - 0.25),
            0.02,
        )
        self.assertLess(
            abs(h_value**3 * float(MODULE.mixed_minimum_weight(h_value)) - 0.5),
            0.02,
        )

    def test_local_d3_d5_formulas(self) -> None:
        for sums in (
            (1, 1, 0, 0, 2),
            (-1, -1, 2, 0, -2),
            (3, 1, -2, 2, 0),
        ):
            with self.subTest(sums=sums):
                direct_d3, direct_d5 = direct_local_coefficients(3, sums)
                self.assertEqual(MODULE.local_d3(3, sums), direct_d3)
                self.assertEqual(MODULE.local_d5(3, sums), direct_d5)

    def test_exact_q3_local_probabilities(self) -> None:
        delta5, delta53 = MODULE.local_probabilities(3)
        self.assertEqual(
            delta5,
            Fraction(
                11000690707734068076805,
                151115727451828646838272,
            ),
        )
        self.assertEqual(
            delta53,
            Fraction(
                44252230658139381379541,
                604462909807314587353088,
            ),
        )
        self.assertGreater(delta5, 0)
        self.assertGreater(delta53, 0)

    def test_explicit_positivity_witnesses(self) -> None:
        for q_value in MODULE.WITNESS_Q_VALUES:
            witness = MODULE.positivity_witness(q_value)
            count = witness["N5"]
            for key in ("S5_for_D5_zero", "S5_for_D5_plus_D3_zero"):
                self.assertTrue(MODULE.rademacher_attainable(count, witness[key]))
            d5_sums = (
                witness["S1"],
                witness["S2"],
                witness["S3"],
                witness["S4"],
                witness["S5_for_D5_zero"],
            )
            d53_sums = (*d5_sums[:4], witness["S5_for_D5_plus_D3_zero"])
            self.assertEqual(MODULE.local_d5(q_value, d5_sums), 0)
            self.assertEqual(
                MODULE.local_d5(q_value, d53_sums) + MODULE.local_d3(q_value, d53_sums),
                0,
            )

    def test_source_locks_report_and_claim_boundary(self) -> None:
        MODULE.check_source_blobs()
        self.assertTrue(
            self.report["claim_boundary"]["raw_detector_zero_asymptotic_proved"]
        )
        self.assertFalse(self.report["claim_boundary"]["individual_L_function_zero"])
        self.assertEqual(self.report["resource_caps"]["zeros_enumerated"], 0)
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "S_{n,Q}=m_{h-2}D_5+m_{h-1}D_3+m_hD_1",
            "D_5+D_3=0",
            "D_5+2D_1=0",
            "excludes an `M^-1` term",
            "not a statement about a zero of an",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        for h_value in (True, 11, 201):
            with self.assertRaises(ValueError):
                MODULE.generic_direct_weight(h_value)
        with self.assertRaises(ValueError):
            MODULE.third_boundary_profiles(61)
        with self.assertRaises(ValueError):
            MODULE.classify_profile(12, (10, 38))
        with self.assertRaises(ValueError):
            MODULE.local_probabilities(5)
        with self.assertRaises(ValueError):
            MODULE.positivity_witness(4)

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("quadratic_third_boundary_zero.v1", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

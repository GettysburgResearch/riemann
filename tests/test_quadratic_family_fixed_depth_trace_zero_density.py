"""Tests for the all-fixed-depth odd-notch zero-density theorem."""

from __future__ import annotations

import ast
import importlib.util
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
MODULE_PATH = FUNCTION_FIELD / "quadratic_family_fixed_depth_trace_zero_density.py"
NOTE_PATH = FUNCTION_FIELD / "QUADRATIC_FAMILY_FIXED_DEPTH_TRACE_ZERO_DENSITY.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MODULE = load_module("quadratic_family_fixed_depth_trace_zero_density", MODULE_PATH)
SECOND = load_module(
    "quadratic_family_second_boundary_zero_density_third_order_for_fixed_depth",
    FUNCTION_FIELD / "quadratic_family_second_boundary_zero_density_third_order.py",
)
THIRD = load_module(
    "quadratic_family_third_boundary_trace_zero_density_for_fixed_depth",
    FUNCTION_FIELD / "quadratic_family_third_boundary_trace_zero_density.py",
)


def independent_profiles(depth: int, h_value: int) -> set[tuple[int, ...]]:
    """Direct two/three-factor loops plus the four-factor excess equation."""

    minimum = h_value - depth
    total = 4 * h_value + 1
    rows = {(minimum, total - minimum)}
    for second in range(minimum, total + 1):
        third = total - minimum - second
        if second <= third:
            rows.add((minimum, second, third))

    excess_total = 4 * depth + 1
    for first_excess in range(excess_total + 1):
        for second_excess in range(first_excess, excess_total + 1):
            third_excess = excess_total - first_excess - second_excess
            if second_excess <= third_excess:
                rows.add(
                    (
                        minimum,
                        minimum + first_excess,
                        minimum + second_excess,
                        minimum + third_excess,
                    )
                )
    return rows


class QuadraticFamilyFixedDepthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_exact_profile_exhaustion(self) -> None:
        for depth in (1, 2, 4, 8):
            for h_value in (MODULE.stable_h(depth), MODULE.stable_h(depth) + 3):
                profiles = set(MODULE.fixed_depth_profiles(depth, h_value))
                self.assertEqual(profiles, independent_profiles(depth, h_value))
                self.assertEqual(
                    {profile for profile in profiles if len(profile) <= 3},
                    set(MODULE.claimed_through_h_minus_3_profiles(depth, h_value)),
                )

    def test_residual_coefficient_collapse(self) -> None:
        for depth in range(1, 9):
            h_value = MODULE.stable_h(depth)
            minimum = h_value - depth
            for profile in MODULE.fixed_depth_profiles(depth, h_value):
                expected = tuple(
                    profile.count(minimum + shift) for shift in range(depth + 1)
                )
                self.assertEqual(
                    MODULE.notch_coefficients(profile, depth, h_value), expected
                )

    def test_exact_three_factor_channels(self) -> None:
        depth = 3
        h_value = MODULE.stable_h(depth)
        examples = {
            (14, 55): ("generic_D_top", "D_7=0"),
            (14, 14, 41): ("repeated_minimum_D_top", "D_7=0"),
            (14, 15, 40): ("near_h_joint", "D_7+D_5=0"),
            (14, 16, 39): ("near_h_joint", "D_7+D_3=0"),
            (14, 17, 38): ("parity_zero", "impossible: residual is odd"),
        }
        for profile, (branch, condition) in examples.items():
            with self.subTest(profile=profile):
                row = MODULE.classify_profile(depth, h_value, profile)
                self.assertEqual(row["branch"], branch)
                self.assertEqual(row["zero_condition"], condition)

    def test_terminal_channel_is_parity_zero(self) -> None:
        for depth in range(1, 9):
            self.assertTrue(MODULE.delta_forced_zero(depth, depth))
            for shift in range(depth):
                self.assertFalse(MODULE.delta_forced_zero(depth, shift))
            h_value = MODULE.stable_h(depth)
            minimum = h_value - depth
            terminal = (
                minimum,
                h_value,
                2 * h_value + depth + 1,
            )
            row = MODULE.classify_profile(depth, h_value, terminal)
            self.assertEqual(row["m_h"], 1)
            self.assertEqual(row["branch"], "parity_zero")

    def test_exact_generic_harmonic_identity(self) -> None:
        for depth in range(1, 9):
            for h_value in range(MODULE.stable_h(depth), MODULE.stable_h(depth) + 13):
                self.assertEqual(
                    MODULE.generic_direct_weight(depth, h_value),
                    MODULE.generic_harmonic_weight(depth, h_value),
                )

    def test_exact_affine_coefficients(self) -> None:
        for depth in range(1, 9):
            factor = 2 * depth - 1
            self.assertEqual(
                MODULE.generic_h_minus_3(depth),
                (Fraction(7 * factor, 36), Fraction(factor, 9)),
            )
            self.assertEqual(
                MODULE.delta0_h_minus_3(depth),
                (
                    Fraction(7 * factor + 9, 36),
                    Fraction(factor, 9),
                ),
            )
            self.assertEqual(
                MODULE.delta0_m_minus_3(depth),
                (
                    Fraction(32 * (7 * depth + 4), 9),
                    Fraction(32 * (4 * depth + 1), 9),
                ),
            )

    def test_profile_weight_limits(self) -> None:
        for depth in (1, 4, 8):
            h_value = 500
            generic_c2 = (1 + math.log(2)) / 3
            generic_c3 = (2 * depth - 1) * (7 + 4 * math.log(2)) / 36
            generic_estimate = h_value**3 * (
                float(MODULE.generic_harmonic_weight(depth, h_value))
                - generic_c2 / h_value**2
            )
            self.assertLess(abs(generic_estimate - generic_c3), 0.2)
            self.assertLess(
                abs(
                    h_value**3 * float(MODULE.repeated_minimum_weight(depth, h_value))
                    - 0.25
                ),
                0.03,
            )
            for shift in range(1, depth + 1):
                self.assertLess(
                    abs(
                        h_value**3 * float(MODULE.near_h_weight(depth, shift, h_value))
                        - 0.5
                    ),
                    0.04,
                )

    def test_j1_j2_recover_predecessors(self) -> None:
        self.assertEqual(MODULE.H_MINUS_2, SECOND.H_MINUS_2)
        self.assertEqual(MODULE.delta0_h_minus_3(1), SECOND.H_MINUS_3_TOTAL)
        self.assertEqual(MODULE.delta0_m_minus_3(1), SECOND.M_MINUS_3)
        self.assertEqual(MODULE.H_MINUS_2, THIRD.H_MINUS_2)
        self.assertEqual(MODULE.delta0_h_minus_3(2), THIRD.H_MINUS_3_D5_TOTAL)
        self.assertEqual(MODULE.delta0_m_minus_3(2), (Fraction(64), Fraction(32)))
        self.assertEqual(MODULE.NEAR_H_H_MINUS_3, THIRD.H_MINUS_3_MIXED)

    def test_source_locks_report_and_note_boundary(self) -> None:
        MODULE.check_source_blobs()
        self.assertFalse(self.report["fixed_q_asymptotic"]["positivity_claimed"])
        self.assertFalse(self.report["claim_boundary"]["uniform_growing_depth_theorem"])
        self.assertEqual(self.report["resource_caps"]["zeros_enumerated"], 0)
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "S_{n,Q}=\\sum_{s=0}^{j}m_{h-j+s}D_{2j+1-2s}",
            "\\delta_{j,j,q}=0",
            "(2j-1)(7+4\\log2)",
            "only a necessary condition",
            "No positivity is asserted",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        for depth in (True, 0, 9):
            with self.assertRaises(ValueError):
                MODULE.stable_h(depth)
        with self.assertRaises(ValueError):
            MODULE.fixed_depth_profiles(2, 11)
        with self.assertRaises(ValueError):
            MODULE.fixed_depth_profiles(8, 55)
        with self.assertRaises(ValueError):
            MODULE.classify_profile(3, 17, (14, 54))
        with self.assertRaises(ValueError):
            MODULE.near_h_weight(3, 0, 17)
        with self.assertRaises(ValueError):
            MODULE.delta_forced_zero(3, 4)

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("quadratic_fixed_depth_zero.v1", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

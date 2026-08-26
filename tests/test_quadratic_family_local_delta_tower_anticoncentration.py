"""Tests for local delta-tower anti-concentration."""

from __future__ import annotations

import ast
import importlib.util
import itertools
import subprocess
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_local_delta_tower_anticoncentration.py"
)
NOTE_PATH = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_LOCAL_DELTA_TOWER_ANTICONCENTRATION.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_local_delta_tower_anticoncentration", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load local delta-tower replay")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def brute_rademacher_max_atom(count: int) -> Fraction:
    distribution = Counter(
        sum(signs) for signs in itertools.product((-1, 1), repeat=count)
    )
    return Fraction(max(distribution.values()), 2**count)


def truncated_euler_coefficient(
    signs_by_degree: dict[int, tuple[int, ...]], target: int
) -> int:
    coefficients = [1] + [0] * target
    for degree, signs in signs_by_degree.items():
        for sign in signs:
            updated = [0] * (target + 1)
            for old_degree, old_value in enumerate(coefficients):
                for exponent in range((target - old_degree) // degree + 1):
                    updated[old_degree + exponent * degree] += (
                        old_value * sign**exponent
                    )
            coefficients = updated
    return coefficients[target]


class QuadraticFamilyDeltaTowerAnticoncentrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_exact_small_rademacher_atoms(self) -> None:
        for count in range(1, 13):
            self.assertEqual(
                MODULE.central_rademacher_atom(count),
                brute_rademacher_max_atom(count),
            )
            self.assertTrue(MODULE.central_atom_bound_holds(count))

    def test_central_binomial_bound_through_cap(self) -> None:
        for index in range(MODULE.MAX_CENTRAL_COUNT // 2 + 1):
            self.assertTrue(MODULE.wallis_induction_bound_holds(index))
        for count in range(1, MODULE.MAX_CENTRAL_COUNT + 1):
            atom = MODULE.central_rademacher_atom(count)
            self.assertLessEqual(count * atom * atom, 1)

    def test_top_degree_sum_has_coefficient_one(self) -> None:
        for target in (3, 5, 7):
            lower = {
                degree: ((1, -1) if degree % 2 else (1,)) for degree in range(1, target)
            }
            first = {**lower, target: (1, -1)}
            second = {**lower, target: (1, 1)}
            coefficient_difference = truncated_euler_coefficient(
                second, target
            ) - truncated_euler_coefficient(first, target)
            top_sum_difference = sum(second[target]) - sum(first[target])
            self.assertEqual(coefficient_difference, top_sum_difference)

    def test_channel_signatures_and_endpoint_parity(self) -> None:
        for depth in range(1, 13):
            top_degree = 2 * depth + 1
            zero = MODULE.channel_signature(depth, 0)
            self.assertEqual(zero["event"], f"D_{top_degree}=0")
            self.assertTrue(zero["s_zero_is_single_D"])
            self.assertEqual(zero["top_sign_coefficient"], 1)
            self.assertFalse(zero["parity_forced_zero"])

            terminal = MODULE.channel_signature(depth, depth)
            self.assertEqual(terminal["event"], f"D_{top_degree}+D_1=0")
            self.assertFalse(terminal["s_zero_is_single_D"])
            self.assertTrue(terminal["parity_forced_zero"])
            self.assertEqual(terminal["top_sign_coefficient"], 1)

    def test_irreducible_counts_and_lower_bound(self) -> None:
        self.assertEqual(MODULE.irreducible_count(3, 3), 8)
        self.assertEqual(MODULE.irreducible_count(3, 5), 48)
        self.assertEqual(MODULE.irreducible_count(3, 7), 312)
        for q_value in MODULE.REPLAY_Q_VALUES:
            for depth in range(1, MODULE.MAX_REPLAY_J + 1):
                degree = 2 * depth + 1
                count = MODULE.irreducible_count(q_value, degree)
                self.assertGreaterEqual(3 * degree * count, 2 * q_value**degree)
                self.assertTrue(MODULE.irreducible_lower_bound_holds(q_value, depth))

    def test_explicit_delta_majorant(self) -> None:
        for q_value in MODULE.REPLAY_Q_VALUES:
            for depth in range(1, MODULE.MAX_REPLAY_J + 1):
                degree = 2 * depth + 1
                expected = Fraction(3 * degree, 2 * q_value**degree)
                self.assertEqual(
                    MODULE.simple_delta_squared_majorant(q_value, depth),
                    expected,
                )
                count = MODULE.irreducible_count(q_value, degree)
                self.assertLessEqual(Fraction(1, count), expected)

    def test_report_and_source_locks(self) -> None:
        MODULE.check_source_blobs()
        self.assertTrue(self.report["coefficient_tower"]["absolute_summability"])
        self.assertFalse(self.report["claim_boundary"]["sums_full_conductor_layers"])
        self.assertEqual(self.report["resource_caps"]["zeros_enumerated"], 0)
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "single `D_r`, not `2D_r`",
            "\\delta_{j,j,q}=0",
            "{1\\over\\sqrt N}",
            "O_q(j^{3/2}q^{-j})",
            "does not prove that the total raw-zero",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        for count in (True, 0, MODULE.MAX_CENTRAL_COUNT + 1):
            with self.assertRaises(ValueError):
                MODULE.central_rademacher_atom(count)
        for q_value in (True, 2, 4):
            with self.assertRaises(ValueError):
                MODULE.irreducible_count(q_value, 3)
            with self.assertRaises(ValueError):
                MODULE.simple_delta_squared_majorant(q_value, 1)
        with self.assertRaises(ValueError):
            MODULE.irreducible_count(3, 0)
        with self.assertRaises(ValueError):
            MODULE.irreducible_lower_bound_holds(3, 13)
        with self.assertRaises(ValueError):
            MODULE.channel_signature(2, 3)

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("local_delta_tower_anticoncentration.v1", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

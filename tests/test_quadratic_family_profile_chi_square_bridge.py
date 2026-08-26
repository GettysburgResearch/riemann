"""Tests for the odd-notch profile chi-square bridge."""

from __future__ import annotations

import ast
import importlib.util
import itertools
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
    / "quadratic_family_profile_chi_square_bridge.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md")
PREDECESSOR_NOTE = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_LOGARITHMIC_DEPTH_ZERO_FIREWALL.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_profile_chi_square_bridge", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load profile chi-square replay")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def independent_profiles(
    total_degree: int, minimum_degree: int
) -> set[tuple[int, ...]]:
    profiles: set[tuple[int, ...]] = set()

    def extend(prefix: tuple[int, ...], remaining: int) -> None:
        if remaining == 0:
            if 2 <= len(prefix) <= 5:
                profiles.add(prefix)
            return
        if len(prefix) == 5:
            return
        lower = prefix[-1] if prefix else minimum_degree
        for degree in range(lower, remaining + 1):
            if degree < minimum_degree:
                continue
            extend((*prefix, degree), remaining - degree)

    extend((minimum_degree,), total_degree - minimum_degree)
    return profiles


def brute_elementary(values: tuple[int, ...], order: int) -> int:
    if order == 0:
        return 1
    return sum(math_product(choice) for choice in itertools.combinations(values, order))


def math_product(values: tuple[int, ...]) -> int:
    product = 1
    for value in values:
        product *= value
    return product


class QuadraticFamilyProfileChiSquareBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_profile_replay_matches_independent_recursion(self) -> None:
        for _q_value, h_value, depth in MODULE.PROFILE_INPUTS:
            total_degree = 4 * h_value + 1
            minimum_degree = h_value - depth
            expected = independent_profiles(total_degree, minimum_degree)
            actual = set(MODULE.degree_profiles(h_value, depth))
            self.assertEqual(actual, expected)
            self.assertTrue(all(len(profile) <= 5 for profile in actual))

    def test_uniform_profile_and_total_layer_lower_bounds(self) -> None:
        for q_value, h_value, depth in MODULE.PROFILE_INPUTS:
            total_degree = 4 * h_value + 1
            minimum_degree = h_value - depth
            profiles = MODULE.degree_profiles(h_value, depth)
            for profile in profiles:
                count = MODULE.profile_conductor_count(q_value, profile)
                self.assertGreaterEqual(
                    count * 122_880 * total_degree**5,
                    q_value**total_degree,
                )
                self.assertTrue(MODULE.profile_lower_bound_holds(q_value, profile))
            two_factor = (minimum_degree, total_degree - minimum_degree)
            two_factor_count = MODULE.profile_conductor_count(q_value, two_factor)
            self.assertGreaterEqual(
                two_factor_count * total_degree**2,
                q_value**total_degree,
            )

    def test_newton_recurrence_matches_elementary_symmetric_sum(self) -> None:
        values = (3, -2, 5, 1, -1)
        power_sums = tuple(
            sum(value**power for value in values) for power in range(1, 6)
        )
        for order in range(6):
            self.assertEqual(
                MODULE.newton_elementary(power_sums, order),
                brute_elementary(values, order),
            )

    def test_cycle_partitions_cover_repeated_degree_terms(self) -> None:
        expected_counts = (1, 2, 3, 5, 7)
        for multiplicity, expected_count in enumerate(expected_counts, start=1):
            partitions = MODULE.integer_partitions(multiplicity)
            self.assertEqual(len(partitions), expected_count)
            self.assertTrue(
                all(sum(partition) == multiplicity for partition in partitions)
            )
            for partition in partitions:
                for cycle_length in partition:
                    if cycle_length == 1:
                        self.assertEqual(cycle_length, 1)
                    else:
                        self.assertGreaterEqual(cycle_length, 2)

    def test_exact_finite_chi_square_gate(self) -> None:
        counts = ((3, 1, 0, 0), (0, 2, 1, 1))
        zero_sets = ((0, 1), (2, 3))
        panel = MODULE.chi_square_gate(counts, zero_sets, Fraction(1, 2))
        self.assertEqual(panel["T"], 8)
        self.assertEqual(panel["Z"], 6)
        self.assertEqual(panel["normalized_zero"], "3/4")
        self.assertEqual(panel["D_squared"], "1")
        self.assertTrue(panel["squared_gate_holds"])

    def test_near_wall_safe_condition_implies_discrepancy_gate(self) -> None:
        for q_value, h_value, depth in MODULE.BRIDGE_INPUTS:
            panel = MODULE.bridge_parameters(q_value, h_value, depth)
            self.assertTrue(panel["ell_at_most_M_over_2"])
            self.assertTrue(panel["near_wall_safe"])
            total_degree = panel["M"]
            top_degree = panel["r"]
            ell = panel["ell_r"]
            discrepancy_bound = Fraction(
                MODULE.DISCREPANCY_CONSTANT * total_degree**11 * (ell + 1) ** 10,
                q_value ** (total_degree - ell),
            )
            self.assertLessEqual(
                discrepancy_bound, Fraction(1, 2 * q_value**top_degree)
            )
            self.assertLessEqual(
                Fraction(1, 2 * q_value**top_degree),
                Fraction(top_degree, q_value**top_degree + top_degree),
            )

    def test_report_source_locks_claims_and_equation_balance(self) -> None:
        MODULE.check_source_blobs()
        self.assertEqual(
            self.report["discrepancy_bound"]["constant"],
            MODULE.DISCREPANCY_CONSTANT,
        )
        self.assertFalse(self.report["entropy_fence"]["breaks_logarithmic_depth"])
        self.assertFalse(self.report["claim_boundary"]["individual_L_function_zero"])
        self.assertFalse(self.report["claim_boundary"]["integer_rh_or_grh"])
        self.assertEqual(self.report["resource_caps"]["characters_enumerated"], 0)
        for note_path in (PREDECESSOR_NOTE, NOTE_PATH):
            note = note_path.read_text(encoding="utf-8")
            self.assertEqual(note.count("\\["), note.count("\\]"))
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "Z_{q,h,j}\\le T_j",
            "C_*=614400",
            "q^{M-\\ell_r-r}",
            "T_\\lambda",
            "Newton's permutation formula",
            "principal `chi^b` terms",
            "finite-residue entropy wall",
            "not an assumption about",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        self.assertEqual(MODULE.irreducible_count(9, 3), 240)
        for q_value in (True, 2, 4, 15, 45):
            with self.assertRaises(ValueError):
                MODULE.irreducible_count(q_value, 3)
        with self.assertRaises(ValueError):
            MODULE.degree_profiles(5, 2)
        with self.assertRaises(ValueError):
            MODULE.profile_multiplicities((3, 2))
        with self.assertRaises(ValueError):
            MODULE.integer_partitions(6)
        with self.assertRaises(ValueError):
            MODULE.newton_elementary((1,), 2)
        with self.assertRaises(ValueError):
            MODULE.chi_square_gate(((1, 0),), ((0, 1),), Fraction(1, 4))

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("profile_chi_square_bridge.v1", completed.stdout)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

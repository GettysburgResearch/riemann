"""Tests for the odd-notch second-boundary trace-zero reduction."""

from __future__ import annotations

import ast
import importlib.util
import itertools
import math
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_second_boundary_trace_zero_reduction.py"
)
NOTE_PATH = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_SECOND_BOUNDARY_TRACE_ZERO_REDUCTION.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_second_boundary_trace_zero_reduction", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load second-boundary module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def independent_profiles(h_value: int) -> set[tuple[int, ...]]:
    conductor_degree = 4 * h_value + 1
    minimum_degree = h_value - 1
    rows: set[tuple[int, ...]] = set()
    for factor_count in range(2, conductor_degree // minimum_degree + 1):
        for profile in itertools.combinations_with_replacement(
            range(minimum_degree, conductor_degree + 1), factor_count
        ):
            if profile[0] == minimum_degree and sum(profile) == conductor_degree:
                rows.add(profile)
    return rows


class QuadraticFamilySecondBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.build_report()

    def test_bounded_profile_replay(self) -> None:
        self.assertEqual(
            self.report["status"], "EXACT_SECOND_BOUNDARY_EXTERIOR_CUBIC_REDUCTION"
        )
        replay = self.report["profile_replay"]
        self.assertEqual((replay["h_min"], replay["h_max"]), (5, 80))
        self.assertGreater(replay["profiles_checked"], 100)
        self.assertEqual(replay["aggregate_branches"]["exceptional_mixed_trace"], 76)
        for row in replay["rows"]:
            self.assertEqual(row["exceptional_mixed_trace"], 1)

    def test_three_exact_branches(self) -> None:
        generic = MODULE.classify_profile(7, (6, 23))
        self.assertEqual(generic["branch"], "primitive_exterior_cubic")
        self.assertEqual(generic["zero_condition"], "D_3=0")

        parity = MODULE.classify_profile(7, (6, 7, 16))
        self.assertEqual(parity["branch"], "nonzero_by_parity")

        exceptional = MODULE.classify_profile(7, (6, 7, 7, 9))
        self.assertEqual(exceptional["branch"], "exceptional_mixed_trace")
        self.assertEqual(exceptional["zero_condition"], "D_3+2*D_1=0")

    def test_exact_residual_witnesses(self) -> None:
        self.assertEqual(MODULE.residual_value(7, (6, 23), 3, 0), 0)
        self.assertEqual(MODULE.residual_value(7, (6, 23), 3, 2), 2)
        self.assertEqual(MODULE.residual_value(7, (6, 7, 16), 3, -2), 1)
        self.assertEqual(MODULE.residual_value(7, (6, 7, 7, 9), 3, -6), 0)

    def test_independent_small_profile_generation(self) -> None:
        for h_value in range(5, 13):
            profiles = set(MODULE.second_boundary_profiles(h_value))
            self.assertEqual(profiles, independent_profiles(h_value))
            even_positive = {
                profile
                for profile in profiles
                if profile.count(h_value) > 0 and profile.count(h_value) % 2 == 0
            }
            self.assertEqual(
                even_positive,
                {(h_value - 1, h_value, h_value, h_value + 2)},
            )

    def test_exceptional_count_and_bound(self) -> None:
        row = MODULE.exceptional_profile_count(3, 5)
        i4 = (3**4 - 3**2) // 4
        i5 = (3**5 - 3) // 5
        i7 = (3**7 - 3) // 7
        self.assertEqual(row["exact_count"], i4 * math.comb(i5, 2) * i7)
        self.assertLessEqual(
            row["exact_count"] * row["upper_bound_denominator"], row["q_to_M"]
        )

    def test_invalid_inputs_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.second_boundary_profiles(4)
        with self.assertRaises(ValueError):
            MODULE.classify_profile(7, (6, 22))
        with self.assertRaises(ValueError):
            MODULE.residual_value(7, (6, 23), 2, 0)
        with self.assertRaises(ValueError):
            MODULE.exceptional_profile_count(4, 7)

    def test_source_locks_and_note_boundaries(self) -> None:
        MODULE.check_source_blobs()
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "complete dichotomy",
            "D_3=0",
            "D_3+2D_1=0",
            "O_q(M^-4)",
            "finite local residue statistic",
            "not zeros of an individual `L`-function",
        ):
            self.assertIn(marker, note)

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn(
            "EXACT_SECOND_BOUNDARY_EXTERIOR_CUBIC_REDUCTION", completed.stdout
        )

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

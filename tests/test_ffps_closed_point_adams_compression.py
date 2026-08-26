"""Tests for exact closed-point Adams compression."""

from __future__ import annotations

import ast
import importlib.util
import json
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
    / "ffps_closed_point_adams_compression.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md")
JSON_PATH = MODULE_PATH.with_name("ffps_closed_point_adams_compression.json")

SPEC = importlib.util.spec_from_file_location(
    "ffps_closed_point_adams_compression", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load closed-point Adams module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ClosedPointAdamsCompressionTests(unittest.TestCase):
    def test_canonical_json_matches(self) -> None:
        expected = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.run_checks(), expected)

    def test_mobius_and_divisors(self) -> None:
        self.assertEqual(MODULE.divisors(12), (1, 2, 3, 4, 6, 12))
        self.assertEqual(
            [MODULE.mobius(value) for value in range(1, 11)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1],
        )
        self.assertEqual(MODULE.mobius_support_count(12), 4)
        self.assertEqual(MODULE.mobius_support_count(30), 8)

    def test_one_place_identity_with_nontrivial_adams_power(self) -> None:
        for degree in range(1, 13):
            recovered = MODULE.one_place_inversion(degree, 2, 1, power=3)
            expected = degree * MODULE.synthetic_prime_trace(2, 1, degree, 3)
            self.assertEqual(recovered, expected)

    def test_two_place_identity_is_exact_rational(self) -> None:
        recovered = MODULE.two_place_inversion(8, 9, 2, 3)
        expected = 72 * MODULE.synthetic_pair_prime_trace(8, 9, 2, 3)
        self.assertIsInstance(recovered, Fraction)
        self.assertEqual(recovered, expected)

    def test_equal_degree_diagonal_extractor(self) -> None:
        for degree in (1, 4, 6, 12):
            recovered = MODULE.diagonal_inversion(degree, power=2)
            expected = degree * MODULE.synthetic_diagonal_prime_trace(degree, power=2)
            self.assertEqual(recovered, expected)

    def test_partial_adams_ranks_and_collisions(self) -> None:
        odd = MODULE.physical_adams_profile(1, 1)
        both_six = MODULE.physical_adams_profile(6, 6)
        left_six = MODULE.physical_adams_profile(6, 1)
        self.assertEqual(sum(odd.values()), 48)
        self.assertEqual(len(odd), 48)
        self.assertEqual(sum(both_six.values()), 48)
        self.assertEqual(len(both_six), 1)
        self.assertEqual(next(iter(both_six.values())), 48)
        self.assertEqual(sum(left_six.values()), 48)
        self.assertLess(len(left_six), 48)

    def test_selected_and_relative_profiles_add(self) -> None:
        for alignment in (-1, 1):
            selected = MODULE.physical_adams_profile(
                4, 9, alignment=alignment, modes=(1, 2)
            )
            relative = MODULE.physical_adams_profile(
                4, 9, alignment=alignment, modes=(0,)
            )
            regular = MODULE.physical_adams_profile(4, 9, alignment=alignment)
            self.assertEqual(sum(selected.values()), 32)
            self.assertEqual(sum(relative.values()), 16)
            self.assertEqual(regular, selected + relative)

    def test_divisor_cost_replaces_cycle_mass(self) -> None:
        panel = MODULE.complexity_panel(12, 12)
        self.assertEqual(panel["raw_divisor_pair_slots"], 36)
        self.assertEqual(panel["nonzero_mobius_pair_terms"], 16)
        self.assertEqual(panel["raw_distinct_diagonal_slots"], 6)
        self.assertEqual(panel["nonzero_mobius_diagonal_terms"], 4)
        self.assertEqual(panel["regular_character_line_evaluations"], 960)
        self.assertEqual(MODULE.selector_mass(12, 12), Fraction(262144, 9))

    def test_invalid_inputs_fail_closed(self) -> None:
        for value in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                MODULE.validate_positive_integer(value)
        with self.assertRaises(ValueError):
            MODULE.physical_adams_profile(1, 1, alignment=0)
        with self.assertRaises(ValueError):
            MODULE.physical_adams_profile(1, 1, modes=())

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_CLOSED_POINT_ADAMS_COMPRESSION", completed.stdout)

    def test_note_preserves_scope_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "extension-field recombination",
            "one diagonal Frobenius structure",
            "underlying ranks 32 and 16",
            "native owner/Boolean/Artin--Schreier separable adapter | **NOT CONSTRUCTED**",
            "RH, or GRH | **NOT PROVED**",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

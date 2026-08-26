"""Tests for the exact universal ternary norm-torsor normal form."""

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
    / "ffps_ternary_universal_norm_torsor.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md")
JSON_PATH = MODULE_PATH.with_name("ffps_ternary_universal_norm_torsor.json")

SPEC = importlib.util.spec_from_file_location(
    "ffps_ternary_universal_norm_torsor", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load universal ternary norm-torsor module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TernaryUniversalNormTorsorTests(unittest.TestCase):
    def test_exact_universal_ranks(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(report["universal_physical_ranks"]["regular_pushforward"], 48)
        self.assertEqual(report["universal_physical_ranks"]["selected_pushforward"], 32)
        self.assertEqual(report["universal_physical_ranks"]["relative_pushforward"], 16)

    def test_canonical_json_matches(self) -> None:
        expected = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.run_checks(), expected)

    def test_selector_mass_and_boundary_normal_form(self) -> None:
        self.assertEqual(MODULE.product_selector_rank_mass(3, 5), Fraction(64, 15))
        self.assertEqual(MODULE.toric_boundary_components(3, 5), 48)
        self.assertEqual(MODULE.regular_conductor_bound(3, 5), 2304)

    def test_generic_exponents_are_nontrivial(self) -> None:
        for alignment in (-1, 1):
            for mode in (1, 2):
                vector = MODULE.physical_exponent_vector(4, 3, mode, alignment)
                self.assertEqual(len(vector), 14)
                self.assertTrue(all(entry in {1, 2, 4, 5} for entry in vector))

    def test_invariant_descent_law(self) -> None:
        self.assertEqual(
            MODULE.descended_invariant_multiplicity(
                is_cube=False, is_sixth_power=False
            ),
            0,
        )
        self.assertEqual(
            MODULE.descended_invariant_multiplicity(is_cube=True, is_sixth_power=False),
            1,
        )
        self.assertEqual(
            MODULE.descended_invariant_multiplicity(is_cube=True, is_sixth_power=True),
            2,
        )
        with self.assertRaises(ValueError):
            MODULE.descended_invariant_multiplicity(is_cube=False, is_sixth_power=True)

    def test_prime_power_and_split_guards(self) -> None:
        for cardinality in (7, 13, 25, 49):
            MODULE.validate_base_cardinality(cardinality)
        for cardinality in (3, 9, 15, 35):
            with self.assertRaises(ValueError):
                MODULE.validate_base_cardinality(cardinality)

    def test_invalid_degree_mode_and_alignment_fail_closed(self) -> None:
        for degree in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                MODULE.validate_degree(degree)
        with self.assertRaises(ValueError):
            MODULE.physical_exponent_vector(2, 3, 0, 1)
        with self.assertRaises(ValueError):
            MODULE.physical_exponent_vector(2, 3, 1, 0)

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_VARYING_PLACE_NORM_TORSOR_NORMAL_FORM", completed.stdout)

    def test_note_preserves_scope_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "one varying-closed-place physical",
            "rank \\(48\\)",
            "linear toric",
            "full owner/Boolean/phase FFPS source adapter | **NOT CONSTRUCTED**",
            "RH, or GRH | **NOT PROVED**",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

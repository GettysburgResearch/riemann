"""Tests for the exact cyclic-torsor relative projector."""

from __future__ import annotations

import ast
import importlib.util
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
    / "ffps_cyclic_torsor_relative_projector.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_cyclic_torsor_projector", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load cyclic torsor projector module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CyclicTorsorRelativeProjectorTests(unittest.TestCase):
    def test_all_bounded_masks(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(report["resource_ledger"]["subsets"], 494)
        self.assertIn("C_S-S_S=Pi_0", report["exact_identities"])

    def test_ternary_matrix_identity(self) -> None:
        hard, selected, principal = MODULE.cyclic_operators(3, frozenset({0, 1}))
        self.assertEqual(MODULE.matrix_subtract(hard, selected), principal)
        self.assertTrue(all(sum(row) == 1 for row in hard))
        self.assertTrue(all(sum(row) == 0 for row in selected))

    def test_singleton_mask_is_identity_hard_operator(self) -> None:
        hard, selected, principal = MODULE.cyclic_operators(5, frozenset({2}))
        self.assertEqual(hard, MODULE.identity(5))
        self.assertEqual(MODULE.matrix_subtract(hard, selected), principal)

    def test_full_mask_has_no_selected_operator(self) -> None:
        hard, selected, principal = MODULE.cyclic_operators(4, frozenset(range(4)))
        zero = tuple(tuple(Fraction(0) for _ in range(4)) for _ in range(4))
        self.assertEqual(hard, principal)
        self.assertEqual(selected, zero)

    def test_arbitrary_trace_function_selector(self) -> None:
        weights = tuple(Fraction(value) for value in (2, -3, 0, 7, 5))
        selector = MODULE.trace_function_endomorphism(weights)
        for frobenius_class, expected in enumerate(weights):
            observed = MODULE.matrix_trace(
                MODULE.matrix_multiply(
                    selector, MODULE.shift_matrix(5, frobenius_class)
                )
            )
            self.assertEqual(observed, expected)

    def test_invalid_inputs_fail_closed(self) -> None:
        for args in ((1, frozenset({0})), (3, frozenset()), (3, frozenset({3}))):
            with self.assertRaises(ValueError):
                MODULE.cyclic_operators(*args)

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_ENDOMORPHISM_PROJECTOR_REPLAY", completed.stdout)

    def test_note_preserves_global_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "honest endomorphisms",
            "one varying-closed-place physical torsor",
            "uniform Betti/conductor control",
            "No external novelty or priority claim",
            "RH or GRH | **UNPROVED**",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()

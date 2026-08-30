"""Tests for the marked-place signed-descent Gate-0 packet."""

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
    / "ffps_marked_place_signed_descent_gate0.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_MARKED_PLACE_SIGNED_DESCENT_GATE0.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_marked_place_descent_gate0", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load marked-place descent module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MarkedPlaceSignedDescentGate0Tests(unittest.TestCase):
    def test_source_locks_resolve_exact_git_blobs(self) -> None:
        MODULE.check_source_blobs()
        MODULE.check_source_lock_manifest()
        self.assertEqual(len(MODULE.SOURCE_BLOBS), 13)

    def test_fixed_label_and_marked_partition_ranks(self) -> None:
        for q in MODULE.Q_CONTROLS:
            fixed_ranks = {
                MODULE.matrix_rank(MODULE.fixed_label_coefficient_slice(q, ell, rho))
                for ell, rho in MODULE.ordered_distinct_pairs(q)
            }
            self.assertEqual(fixed_ranks, {1})
            expected = q * (q - 1)
            self.assertEqual(
                MODULE.matrix_rank(MODULE.marked_cross_matrix(q)), expected
            )
            self.assertEqual(
                MODULE.matrix_rank(MODULE.wick_oriented_cross_matrix(q)),
                2 * expected,
            )
            self.assertEqual(
                MODULE.matrix_rank(MODULE.orientation_forgotten_cross_matrix(q)),
                expected,
            )

    def test_positive_and_source_blind_controls_are_rank_one(self) -> None:
        for q in MODULE.Q_CONTROLS:
            self.assertEqual(MODULE.matrix_rank(MODULE.separable_control_matrix(q)), 1)
            self.assertEqual(MODULE.matrix_rank(MODULE.source_blind_phase_matrix(q)), 1)

    def test_cleanup_coefficient_survives_only_off_atomic_distinct_chart(self) -> None:
        self.assertEqual(MODULE.pi0_invariant_coefficient(), Fraction(1))
        self.assertEqual(MODULE.linear_core_moebius_coprimality(0, 1), 1)
        self.assertEqual(MODULE.linear_core_moebius_coprimality(1, 1), 0)
        self.assertEqual(MODULE.wick_label_coefficient(0, 1), 1)
        self.assertEqual(MODULE.wick_label_coefficient(1, 1), 0)
        self.assertEqual(MODULE.post_cleanup_generic_coefficient(0, 1, 0, 1), 1)
        self.assertEqual(MODULE.post_cleanup_generic_coefficient(0, 0, 0, 1), 0)
        self.assertEqual(MODULE.post_cleanup_generic_coefficient(0, 1, 0, 0), 0)

    def test_partial_frobenius_moves_but_total_preserves_support(self) -> None:
        for q in MODULE.Q_CONTROLS:
            point = MODULE.clean_crossed_point(q)
            self.assertTrue(MODULE.crossed_support_holds(point))
            self.assertFalse(
                MODULE.crossed_support_holds(MODULE.left_partial_frobenius(point))
            )
            self.assertFalse(
                MODULE.crossed_support_holds(MODULE.right_partial_frobenius(point))
            )
            self.assertTrue(MODULE.crossed_support_holds(MODULE.total_frobenius(point)))

    def test_quadratic_extension_is_exact(self) -> None:
        for q in MODULE.Q_CONTROLS:
            theta = MODULE.Fq2(q, 2, 0, 1)
            one = MODULE.Fq2(q, 2, 1, 0)
            self.assertEqual(theta.square(), MODULE.Fq2(q, 2, 2, 0))
            self.assertEqual(theta**q, MODULE.Fq2(q, 2, 0, -1))
            self.assertEqual(theta**0, one)

    def test_report_scope_and_resource_ledger(self) -> None:
        report = MODULE.build_report()
        self.assertEqual(
            report["status"], "EXACT_SCOPED_NO_GO_AND_PARTITION_RECONCILIATION"
        )
        self.assertEqual(report["arithmetic_class"], "MIXED")
        self.assertEqual(
            report["arithmetic_components"],
            {
                "matrix_and_cleanup_coefficients": "EXACT_RATIONAL",
                "support_witnesses": "EXACT_FINITE_FIELD_EXTENSION_ARITHMETIC",
            },
        )
        self.assertIn(
            "noncancellation after the complete signed source pushforward",
            report["not_proved"],
        )
        resources = report["resource_ledger"]
        self.assertEqual(resources["maximum_matrix_dimension"], 40)
        self.assertEqual(resources["ordered_distinct_pairs_materialized"], 26)
        self.assertEqual(resources["quadratic_extension_point_transforms_checked"], 8)
        self.assertEqual(resources["floating_point_operations"], 0)

    def test_invalid_inputs_fail_closed(self) -> None:
        for q in (2, 4, 7, True):
            with self.assertRaises(ValueError):
                MODULE.ordered_distinct_pairs(q)
        with self.assertRaises(ValueError):
            MODULE.fixed_label_coefficient_slice(3, 0, 0)
        with self.assertRaises(ValueError):
            MODULE.principal_projector(1)
        with self.assertRaises(ValueError):
            MODULE.Fq2(3, 1, 0, 1)
        with self.assertRaises(ValueError):
            MODULE.Fq2(3, 2, 0, 1) ** -1
        with self.assertRaises(ValueError):
            MODULE.matrix_rank(((Fraction(1),), (Fraction(1), Fraction(2))))

    def test_note_preserves_partition_and_global_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "coefficient partition",
            "marked-place partition",
            "universal coefficient space",
            "base-field trace",
            "place at infinity is outside",
            "label-decorated copies of the same shared-coordinate graph",
            "does not introduce independent marked coordinates",
            "MPD-G0.3 — post-cleanup generic-support survival",
            "complete signed pushforward remains undecided",
            "ONEPLACEWEIL",
            "not a live-source occupancy theorem",
            "RH and GRH remain unproved",
        ):
            self.assertIn(marker, note)

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20.0,
        )
        self.assertIn(
            "EXACT_SCOPED_NO_GO_AND_PARTITION_RECONCILIATION", completed.stdout
        )


if __name__ == "__main__":
    unittest.main()

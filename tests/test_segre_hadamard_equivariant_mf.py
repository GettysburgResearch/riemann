"""Residual source action, equivariant syzygies, and hidden nonzero modules."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/equivariant_mf_replay.py"
)
SPEC = importlib.util.spec_from_file_location("segre_equivariant_mf", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class GaussianSourceAndEquivariantMaps(unittest.TestCase):
    def test_gaussian_arithmetic_keeps_the_finite_order_exact(self):
        self.assertEqual(M.power(M.I, 2), (-1, 0))
        self.assertEqual(M.power(M.I, 4), M.ONE)

    def test_source_weights_are_sym_cubic_weights_not_fitted_roots(self):
        row = M.source_weights(M.I, M.ONE)
        self.assertEqual(
            [row[key] for key in ("x", "z", "r", "s", "delta")],
            [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, 0)],
        )

    def test_all_D_columns_have_the_source_character_twist(self):
        rows = M.equivariant_columns(M.source_weights((2, 0), (3, 0)))
        self.assertEqual(rows[1]["generator_eigenvalues"], [(3888, 0), (8748, 0)])
        self.assertEqual(rows[2]["generator_eigenvalues"], [(1259712, 0), (2834352, 0)])

    def test_omitting_delta_would_break_even_the_first_column(self):
        source = M.source_weights((2, 0), (3, 0))
        self.assertNotEqual(M.times(source["r"], source["delta"]), source["r"])

    def test_negative_generator_trace_is_not_its_dimension(self):
        rows = M.equivariant_columns(M.source_weights(M.I, M.ONE))
        self.assertTrue(
            all(row["dimension"] == 2 and row["trace"] == M.ZERO for row in rows)
        )

    def test_two_step_periodicity_retains_delta_squared(self):
        source = M.source_weights((2, 0), (3, 0))
        rows = M.equivariant_columns(source)
        self.assertEqual(
            rows[2]["generator_eigenvalues"],
            [
                M.times(M.power(source["delta"], 2), value)
                for value in rows[0]["generator_eigenvalues"]
            ],
        )

    def test_source_diagonal_and_caps_reject_inexact_or_singular_inputs(self):
        for bad in ((0, 0), (True, 0), (1.0, 0), (8, 0)):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.source_weights(bad, M.ONE)
        with self.assertRaises(ValueError):
            M.equivariant_columns(M.source_weights(M.I, M.ONE), True)


class TraceCollapseAndOrdinaryDeterminant(unittest.TestCase):
    def test_first_residual_character_is_finite_free_looking_but_not_a_module_claim(
        self,
    ):
        row = M.character_control(M.I, M.ONE)
        self.assertEqual(
            row["actual_Chow_invariant_character"][:9],
            [M.ONE, (0, 2), M.ZERO, M.ZERO, M.ONE, (0, 2), M.ZERO, M.ZERO, M.ONE],
        )
        self.assertTrue(all(value == M.ZERO for value in row["odd_module_character"]))

    def test_independent_finite_order_control_has_different_nonzero_quotient_trace(
        self,
    ):
        row = M.character_control(M.ONE, M.I)
        self.assertEqual(
            row["actual_Chow_invariant_character"][:6],
            [M.ONE, (-2, 0), M.ZERO, M.ZERO, M.ONE, (-2, 0)],
        )

    def test_second_operator_power_recovers_every_visible_Tor_trace(self):
        row = M.character_control((-1, 0), M.ONE)
        self.assertTrue(all(part["trace"] == (2, 0) for part in row["Tor_weight_rows"]))
        self.assertEqual(row["odd_module_character"][1], (2, 0))

    def test_zero_first_trace_has_nontrivial_ordinary_determinant(self):
        row = M.finite_order_controls()
        self.assertEqual(
            row["degree_one_ordinary_determinant_low_to_high"], [M.ONE, M.ZERO, (-1, 0)]
        )
        self.assertEqual(row["second_power_degree_one_trace"], (2, 0))
        self.assertFalse(row["arithmetic_Frobenius_realization_asserted"])

    def test_generic_source_retains_nonzero_odd_module_and_infinite_Euler_rows(self):
        row = M.character_control((2, 0), (3, 0))
        self.assertEqual(row["odd_module_character"][1], (39, 0))
        self.assertTrue(all(part["trace"][0] > 0 for part in row["Tor_weight_rows"]))
        self.assertTrue(row["visible_resolution_Euler_rows_checked"])

    def test_identity_source_recovers_actual_dimensions(self):
        row = M.character_control(M.ONE, M.ONE)
        self.assertEqual(
            row["actual_Chow_invariant_character"][:5],
            [(1, 0), (4, 0), (14, 0), (32, 0), (63, 0)],
        )

    def test_character_cutoff_and_nonunit_denominator_are_rejected(self):
        with self.assertRaises(ValueError):
            M.character_control(M.I, M.ONE, 15)
        with self.assertRaises(ValueError):
            M.divide([M.ONE], [(2, 0)], 3)


class BoundSourceAndScope(unittest.TestCase):
    def test_frozen_source_authentication_refuses_revision_substitution(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaisesRegex(ValueError, "frozen Chow"),
        ):
            M.authenticate_source()

    def test_working_source_bytes_are_not_accepted_from_revision_alone(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=M.PINS[0][1]),
            patch.object(M, "canonical_bytes", return_value=b"wrong"),
            self.assertRaisesRegex(ValueError, "frozen Chow"),
        ):
            M.authenticate_source()

    def test_payload_rejects_module_vanishing_promoted_from_trace(self):
        row = M.build_payload()
        bad = copy.deepcopy(row)
        bad["finite_resolution_or_module_vanishing_inferred_from_trace"] = True
        with self.assertRaises(ValueError):
            M.check_payload(bad)

    def test_payload_rejects_bool_in_place_of_a_dimension(self):
        row = M.build_payload()
        bad = copy.deepcopy(row)
        bad["finite_order_trace_controls"]["primary"]["Tor_weight_rows"][0][
            "dimension"
        ] = True
        with self.assertRaises(ValueError):
            M.check_payload(bad)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("l105101_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load L-105101 verifier")
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class TestL105101(unittest.TestCase):
    def test_real_cubic_narrow_and_full_windows(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        narrow = V.local_ledger(
            "narrow",
            coefficients,
            [V.G(F(-1)), V.G(F(1))],
            [V.ZERO],
            F(1, 2),
            F(1),
        )
        self.assertEqual(narrow["real_m2"], "0")
        self.assertEqual(narrow["adjacent_derivative_debt"], "-1/18")
        self.assertEqual(narrow["boundary_residue_sum"], "-1/18")

        full = V.local_ledger(
            "full",
            coefficients,
            [V.G(F(-1)), V.G(F(1))],
            [V.ZERO],
            F(3, 2),
            F(1),
        )
        self.assertEqual(full["real_m2"], "5/18")
        self.assertEqual(full["adjacent_derivative_debt"], "-1/18")
        self.assertEqual(full["boundary_residue_sum"], "2/9")

    def test_asymmetric_partial_window(self) -> None:
        fixture = V.local_ledger(
            "asymmetric",
            [F(1), F(64), F(-32), F(-4, 3), F(1)],
            [V.G(F(-4)), V.G(F(1)), V.G(F(4))],
            [V.G(F(-2)), V.G(F(8, 3))],
            F(3),
            F(1),
        )
        self.assertEqual(fixture["inside_critical_roots"], ["1"])
        self.assertEqual(
            fixture["inside_second_critical_roots"], ["-2", "8/3"]
        )
        self.assertEqual(fixture["real_m2"], "2401/8100")
        self.assertEqual(
            fixture["adjacent_derivative_debt"], "-20987563/3110400"
        )
        self.assertEqual(fixture["boundary_residue_sum"], "-20065579/3110400")
        self.assertEqual(fixture["global_residue_sum"], "5437/3888")
        self.assertEqual(
            fixture["global_residue_sum"], fixture["root_v2_v4_ledger"]
        )
        self.assertTrue(fixture["global_exterior_split_verified"])
        self.assertTrue(fixture["independent_root_ledger_verified"])

    def test_nonreal_correction_enters_and_leaves_with_strip(self) -> None:
        coefficients = [F(1), F(3), F(0), F(1)]
        roots = [V.G(F(0), F(-1)), V.G(F(0), F(1))]
        narrow = V.local_ledger(
            "complex-narrow", coefficients, roots, [V.ZERO], F(1), F(1, 2)
        )
        wide = V.local_ledger(
            "complex-wide", coefficients, roots, [V.ZERO], F(1), F(2)
        )
        self.assertEqual(narrow["nonreal_correction"], "0")
        self.assertEqual(narrow["adjacent_derivative_debt"], "1/18")
        self.assertEqual(narrow["boundary_residue_sum"], "1/18")
        self.assertEqual(wide["nonreal_correction"], "1/6")
        self.assertEqual(wide["adjacent_derivative_debt"], "1/18")
        self.assertEqual(wide["boundary_residue_sum"], "2/9")
        self.assertEqual(wide["real_m2"], "0")
        firewall = V.algebraic_square_firewall()
        self.assertEqual(firewall["algebraic_squared_residue_sum"], "1/6")
        self.assertEqual(firewall["absolute_squared_residue_sum"], "5/18")

    def test_boundary_root_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            V.local_ledger(
                "boundary",
                [F(1), F(-3), F(0), F(1)],
                [V.G(F(-1)), V.G(F(1))],
                [V.ZERO],
                F(1),
                F(1),
            )

    def test_incomplete_and_duplicate_coverage_is_rejected(self) -> None:
        coefficients = [F(1), F(3), F(0), F(1)]
        with self.assertRaises(ValueError):
            V.residue_ladder(coefficients, [V.I], [V.ZERO])
        with self.assertRaises(ValueError):
            V.residue_ladder(coefficients, [V.I, V.I], [V.ZERO])
        with self.assertRaises(AssertionError):
            V.residue_ladder(coefficients, [V.I, V.ZERO], [V.ZERO])

    def test_second_critical_coverage_and_boundary_are_rejected(self) -> None:
        coefficients = [F(1), F(64), F(-32), F(-4, 3), F(1)]
        critical = [V.G(F(-4)), V.G(F(1)), V.G(F(4))]
        with self.assertRaises(ValueError):
            V.residue_ladder(coefficients, critical, [V.G(F(-2))])
        with self.assertRaises(ValueError):
            V.residue_ladder(
                coefficients, critical, [V.G(F(-2)), V.G(F(-2))]
            )
        with self.assertRaises((ValueError, AssertionError)):
            V.residue_ladder(
                coefficients, critical, [V.ZERO, V.G(F(8, 3))]
            )
        with self.assertRaises(ValueError):
            V.local_ledger(
                "psecond-boundary",
                coefficients,
                critical,
                [V.G(F(-2)), V.G(F(8, 3))],
                F(2),
                F(1),
            )

    def test_nonsimple_manifests_fail_closed(self) -> None:
        with self.assertRaises(ValueError):
            V.residue_ladder(
                [F(1), F(0), F(0), F(1)],
                [V.ZERO, V.ZERO],
                [V.ZERO],
            )
        with self.assertRaises(ValueError):
            V.residue_ladder(
                [F(0), F(1), F(0), F(0), F(1)],
                [V.ZERO, V.G(F(1)), V.G(F(2))],
                [V.ZERO, V.ZERO],
            )

    def test_boundary_segment_not_supporting_line(self) -> None:
        t, eta = F(2), F(1)
        self.assertTrue(V.on_rectangle_boundary(V.G(t, eta), t, eta))
        self.assertTrue(V.on_rectangle_boundary(V.G(t, F(1, 2)), t, eta))
        self.assertTrue(V.on_rectangle_boundary(V.G(F(1, 2), eta), t, eta))
        self.assertFalse(V.on_rectangle_boundary(V.G(t, F(2)), t, eta))
        self.assertFalse(V.inside_rectangle(V.G(t, F(0)), t, eta))
        with self.assertRaises(ValueError):
            V.local_ledger(
                "horizontal-boundary",
                [F(1), F(3), F(0), F(1)],
                [V.G(F(0), F(-1)), V.G(F(0), F(1))],
                [V.ZERO],
                F(1),
                F(1),
            )

    def test_removable_numerator_zeros_are_accounted_for(self) -> None:
        common = V.local_ledger(
            "common-removable",
            [F(1), F(-2), F(1)],
            [V.G(F(1))],
            [],
            F(2),
            F(1),
        )
        self.assertEqual(common["real_m2"], "0")
        self.assertEqual(common["boundary_residue_sum"], "0")
        zero_tau = V.local_ledger(
            "zero-tau",
            [F(0), F(3), F(0), F(1)],
            [V.G(F(0), F(-1)), V.G(F(0), F(1))],
            [V.ZERO],
            F(1),
            F(1, 2),
        )
        self.assertEqual(zero_tau["adjacent_derivative_debt"], "0")
        self.assertEqual(zero_tau["inside_second_critical_roots"], ["0"])

    def test_rectangle_orientation_and_parity(self) -> None:
        orientation = V.rectangle_orientation_checks()
        self.assertTrue(orientation["counterclockwise"])
        self.assertEqual(orientation["affine_contour_integral"], "0")
        self.assertEqual(
            F(orientation["reversed_signed_area"]),
            -F(orientation["signed_area"]),
        )
        edge = V.edge_formula_mutation_checks()
        self.assertEqual(edge["unit_square_1_over_z_ccw_winding"], "1")
        self.assertEqual(edge["unit_square_1_over_z_clockwise_winding"], "-1")
        self.assertTrue(edge["sign_mutations_rejected"])
        integrated = V.integrated_edge_formula_check()
        self.assertEqual(integrated["combined_a_over_pi_plus_b"], ["0", "1/4"])
        self.assertEqual(integrated["residue"], "1/4")
        self.assertTrue(integrated["both_sign_mutations_rejected"])
        parity = V.schwarz_parity_checks()
        self.assertTrue(parity["even"]["Q_is_odd"])
        self.assertTrue(parity["odd"]["Q_is_odd"])
        self.assertFalse(parity["generic_real"]["Q_is_odd"])

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact = json.loads(
            (ROOT / "results" / "verification.json").read_text(encoding="utf-8")
        )
        self.assertEqual(artifact, V.build_payload())
        self.assertEqual(set(artifact["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertFalse(scope["multiple_zero_confluent_ledger_proved"])
        self.assertFalse(scope["admissible_height_strip_sequence_controlled"])
        self.assertFalse(scope["uniform_height_flux_bound_proved"])
        self.assertFalse(scope["nonreal_correction_bound_proved"])
        self.assertFalse(scope["adjacent_derivative_debt_bound_proved"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()

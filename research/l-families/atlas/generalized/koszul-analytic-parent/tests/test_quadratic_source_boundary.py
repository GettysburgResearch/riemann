"""Actual diagonal inertia, partial-source refusals, and signed completion."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("quadratic_source_boundary",HERE/"quadratic_source_boundary_replay.py")
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class DiagonalInertiaTests(unittest.TestCase):
    def test_first_zero_trace_does_not_remove_infinity(self):
        result=M.infinity_control(7,1)
        self.assertEqual(result["first_two_traces"],[0,6])
        self.assertEqual(result["local_denominator"],[1,0,-3,0,3,0,-1])
        self.assertTrue(result["zero_first_trace_does_not_mean_zero_stalk"])

    def test_split_infinity_retains_same_dimension(self):
        result=M.infinity_control(5,1)
        self.assertEqual(result["first_two_traces"],[6,6])
        self.assertEqual(result["local_denominator"],[1,-6,15,-20,15,-6,1])

    def test_extension_degree_two_recovers_trace(self):
        self.assertEqual(M.infinity_trace(7,2,2),M.infinity_trace(49,2,1))
        self.assertEqual(M.infinity_trace(7,2,1),0)
        self.assertEqual(M.infinity_trace(49,2,1),28)

    def test_grade_zero_is_zero_cohomology_and_zero_infinity(self):
        row=M.source_rows(0)[0]
        self.assertEqual(row["h0_h1_h2"],[0,0,0])
        self.assertEqual(row["kappa"],0)
        self.assertEqual(M.infinity_polynomial(7,0),[1])

    def test_twisted_h1_uses_actual_four_primitive_ranks(self):
        rows=M.source_rows(2)
        self.assertEqual(rows[1]["h0_h1_h2"],[0,24,0])
        self.assertEqual(rows[2]["h0_h1_h2"],[0,128,0])

    def test_all_grade_conductor_and_parity_constraints(self):
        for row in M.source_rows(48):
            self.assertEqual(row["h0_h1_h2"][1]%2,0)
            self.assertEqual(row["infinity_dimension"]%2,0)
            self.assertEqual(row["zero_stalk_dimension"],0)

    def test_first_trace_counterfeit_is_caught_by_newton(self):
        actual=M.infinity_polynomial(7,1)
        self.assertNotEqual(actual,[1])
        self.assertEqual(M.S4.P.local_sums_from_polynomial(actual,2),[0,-6])

    def test_infinity_primitive_caps_are_enforced(self):
        for q in (True,7.0,9,343):
            with self.subTest(q=q),self.assertRaises((ValueError,TypeError)):
                M.infinity_trace(q,1,1)
        with self.assertRaises(ValueError):
            M.infinity_polynomial(7,7)


class ActualQuadraticSourceTests(unittest.TestCase):
    def test_p5_full_degree_ten_and_heldout_sixth(self):
        panel=M.native_panel(0)
        self.assertEqual(len(panel["twisted_polynomials"]["tw"]),11)
        self.assertEqual(panel["degree_ten_held_out_extensions"],[6])

    def test_p7_is_honestly_partial(self):
        for index in (1,2):
            panel=M.native_panel(index)
            self.assertIsNone(panel["twisted_polynomials"]["tw"])
            self.assertEqual(len(panel["tw_prefix_mod_T5"]),5)
            M.cohomology_powers(panel,4)
            with self.assertRaises(ValueError):
                M.cohomology_powers(panel,5)

    def test_partial_source_cannot_enter_completed_determinant(self):
        panel=M.native_panel(1)
        with self.assertRaises(ValueError):
            M.determinant_control(panel,Fraction(1,10),Fraction(1,2))
        with self.assertRaises(ValueError):
            M.finite_duality(panel,1)

    def test_recount_uses_only_small_frozen_fields(self):
        for index in range(3):
            rows=M.native_panel(index)["primitive_rows"]
            self.assertEqual([row["extension"] for row in rows],[1,2])
            self.assertLessEqual(max(row["field_order"] for row in rows),49)

    def test_primitive_genus49_regular_trace(self):
        for index in range(3):
            M.fibre_controls(M.native_panel(index))

    def test_zero_first_primitive_std_trace_but_dimension_two(self):
        rows=M.native_panel(1)["primitive_rows"]
        self.assertEqual(rows[0]["twisted_infinity_stalk_traces"]["std"],0)
        self.assertEqual(rows[0]["twisted_infinity_stalk_dimensions"]["std"],2)
        self.assertEqual(rows[1]["twisted_infinity_stalk_traces"]["std"],2)

    def test_p5_anti_regular_source_rank_sixty(self):
        panel=M.native_panel(0)
        rank=sum(d*(len(panel["twisted_polynomials"][name])-1)
                 for d,name in zip((1,2,3,3),("sign","two","std","tw")))
        self.assertEqual(rank,60)

    def test_trivial_inputs_cancel_despite_nonzero_regular_anti_source(self):
        row=M.native_panel(0)["primitive_rows"][0]
        self.assertNotEqual(row["signed_regular_source_sum"],0)
        self.assertEqual(row["twisted_stalk_sums"]["one"],0)

    def test_source_index_validation_precedes_cache(self):
        M.native_panel(1)
        for index in (True,1.0,-1,3):
            with self.subTest(index=index),self.assertRaises((ValueError,TypeError)):
                M.native_panel(index)


class SignedCompletionTests(unittest.TestCase):
    def test_ordinary_determinant_beyond_initial_euler_disk(self):
        result=M.determinant_control(M.native_panel(0),Fraction(1,10),Fraction(1,2))
        self.assertFalse(result["inside_initial_Euler_disk"])
        self.assertEqual(result["grade_zero_factor"],1)

    def test_independent_source_grade_and_power_bounds(self):
        result=M.determinant_control(M.native_panel(0),Fraction(1,4),Fraction(1,10))
        self.assertLess(Fraction(*result["proved_power_tail"]),Fraction(1,10**10))

    def test_finite_actual_twisted_functional_equations(self):
        for n in (0,1,2):
            result=M.finite_duality(M.native_panel(0),n)
            self.assertTrue(result["source_functional_equation"])

    def test_first_power_comes_from_full_primitive_fibres(self):
        panel=M.native_panel(0)
        z,T=Fraction(1,4),Fraction(1,100)
        self.assertEqual(M.power_log(panel,z,T,1),T*M.native_trace(panel["primitive_rows"][0],z))

    def test_partial_signed_constant_stays_within_known_prefix(self):
        panel=M.native_panel(1)
        result=M.signed_constant(panel,1,Fraction(1,14),4)
        self.assertFalse(result["full_rank_ten_source"])
        with self.assertRaises(ValueError):
            M.signed_constant(panel,1,Fraction(1,14),5)

    def test_analytic_domains_are_enforced(self):
        panel=M.native_panel(0)
        with self.assertRaises(ValueError):
            M.signed_constant(panel,1,Fraction(1,5))
        with self.assertRaises(ValueError):
            M.determinant_control(panel,Fraction(1,3),Fraction(1))

    def test_frozen_sources(self):
        M.authenticate_frozen()

    def test_forged_fixture_is_rejected(self):
        with self.assertRaises(ValueError):
            M.check_payload({"schema":"quadratic-signed-source-boundary-s4-v1","status":"PASS"})


if __name__=="__main__":
    unittest.main()

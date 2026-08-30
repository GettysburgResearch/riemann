"""Actual Lie arithmetic source, ramified correction and branch certificate."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("global_lie_cohomology",HERE/"global_lie_cohomology_replay.py")
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ActualLieSourceTests(unittest.TestCase):
    def test_first_grade_is_the_regular_S3_representation(self):
        row=M.lie_rows(1)[0]
        self.assertEqual(row["class_traces"],[6,0,0])
        self.assertEqual(row["multiplicities"],[1,1,2])
        self.assertEqual(row["h0_h1_h2"],[1,6,1])

    def test_second_grade_retains_relation_source_and_even_sign(self):
        row=M.lie_rows(2)[1]
        self.assertEqual(row["class_traces"],[3,1,0])
        self.assertEqual(row["multiplicities"],[1,0,1])
        self.assertEqual(row["parity_sign"],-1)
        self.assertEqual(row["h0_h1_h2"],[1,2,1])

    def test_all_bounded_source_multiplicities_and_inertia_spaces_are_honest(self):
        for row in M.lie_rows(64):
            a,b,c=row["multiplicities"]
            self.assertEqual(a+b+2*c,row["class_traces"][0])
            self.assertTrue(all(value>=0 for value in row["h0_h1_h2"]))
            self.assertEqual(row["C2_invariants"],a+c)
            self.assertEqual(row["C3_invariants"],a+b)

    def test_lie_grade_is_not_the_polynomial_segre_grade(self):
        self.assertEqual(M.lie_rows(2)[1]["class_traces"][0],3)
        self.assertEqual(M.segre_series("e",2)[2],18)

    def test_source_bounds_types_and_caps(self):
        for value in (True,1.0,0,97):
            with self.subTest(value=value),self.assertRaises((ValueError,TypeError)):
                M.lie_rows(value)


class RamifiedCorrectionTests(unittest.TestCase):
    def test_unramified_PBW_recovers_actual_character_series(self):
        for kind in ("e","s","c"):
            self.assertEqual(M.local_parent(kind,18),M.segre_series(kind,18))

    def test_C2_does_not_commute_invariants_with_PBW(self):
        self.assertEqual(M.local_parent("C2",2),[1,3,4])
        self.assertEqual(M.segre_series("C2",2),[1,3,10])

    def test_C3_identity_residual_action_has_its_own_defect(self):
        self.assertEqual(M.local_parent("C3",2),[1,2,2])
        self.assertEqual(M.segre_series("C3",2),[1,2,6])

    def test_nonsplit_infinity_needs_full_residual_action(self):
        self.assertEqual(M.local_parent("C3s",2),[1,0,0])
        self.assertEqual(M.segre_series("C3s",2),[1,0,2])
        self.assertNotEqual(M.local_parent("C3",12),M.local_parent("C3s",12))

    def test_all_three_Mahler_equations_from_finite_source_modules(self):
        result=M.local_controls(18)
        self.assertTrue(result["all_three_Mahler_identities"])
        self.assertEqual([row["degree_two_difference"] for row in result["ramified_defects"]],[-6,-4,-2])

    def test_reciprocal_sign_would_fail_first_source_coefficient(self):
        self.assertEqual(M.local_parent("e",1)[1],6)
        self.assertNotEqual(M.local_parent("e",1)[1],-6)

    def test_local_source_validation(self):
        with self.assertRaises(ValueError):
            M.local_parent("unknown",2)
        with self.assertRaises(ValueError):
            M.local_parent("C2",25)


class ArithmeticLieCohomologyTests(unittest.TestCase):
    def test_complete_primitive_fibres_match_finite_Lie_cohomology(self):
        for index in range(3):
            self.assertEqual(len(M.fibre_controls(index)),2)

    def test_first_grade_factor_is_actual_closure_zeta(self):
        source=M.native_source(0)
        u=Fraction(1,13)
        pd,pe=source["polynomials"]["D"],source["polynomials"]["E"]
        value=lambda poly:sum(coefficient*u**i for i,coefficient in enumerate(poly))
        expected=value(pd)*value(pe)**2/((1-u)*(1-source["parameters_p_A_B"][0]*u))
        self.assertEqual(M.finite_L(source,u,1),expected)

    def test_all_finite_signed_source_dualities(self):
        for index in range(3):
            for cut in (1,2,3,4):
                self.assertTrue(M.finite_duality(index,cut)["source_functional_equation"])
        self.assertEqual(M.finite_duality(0,3)["K"],3)
        self.assertEqual(M.finite_duality(0,3)["W"],5)

    def test_exact_ordinary_log_enclosures_and_infinite_grade_tail(self):
        for index in range(3):
            q=M.native_source(index)["parameters_p_A_B"][0]
            result=M.logarithm_control(index,Fraction(1,4*q))
            self.assertGreater(Fraction(*result["proved_infinite_grade_tail"]),0)
            self.assertLess(Fraction(*result["proved_infinite_grade_tail"]),Fraction(1,10**12))

    def test_original_euler_disk_and_finite_poles_are_enforced(self):
        with self.assertRaises(ValueError):
            M.logarithm_control(0,Fraction(1,5))
        with self.assertRaises(ValueError):
            M.finite_L(M.native_source(0),Fraction(1,5),1)

    def test_native_index_validation_precedes_frozen_cache(self):
        M.native_source(1)
        for value in (True,1.0,-1,3):
            with self.subTest(value=value),self.assertRaises((ValueError,TypeError)):
                M.native_source(value)


class ArithmeticBranchCertificateTests(unittest.TestCase):
    def test_actual_Q1mod3_sources_force_cubic_exponent(self):
        for index in (1,2):
            result=M.branch_gate(index)
            self.assertEqual(Fraction(*result["alpha"]).denominator,3)
            self.assertTrue(result["nonmeromorphic_cubic_branch"])

    def test_Q2mod3_integer_exponent_is_not_overpromoted(self):
        result=M.branch_gate(0)
        self.assertEqual(Fraction(*result["alpha"]).denominator,1)
        self.assertFalse(result["nonmeromorphic_cubic_branch"])
        self.assertTrue(result["integer_exponent_is_not_claimed_to_prove_a_branch"])

    def test_quadratic_extension_has_actual_infinity_and_cubic_exponent(self):
        row=M.fibre_controls(0)[1]
        self.assertEqual(row["field_order"],25)
        self.assertEqual(row["infinity_points"],2)
        self.assertEqual(Fraction(*row["first_boundary_exponent"]).denominator,3)

    def test_continuation_uses_nonzero_local_factors_not_no_poles_in_disk(self):
        result=M.branch_gate(1)
        self.assertTrue(all(Fraction(*value)!=0 for value in result["finite_factors_at_minus_half"]))
        r=Fraction(*result["continuation_radius"])
        self.assertGreater(r,Fraction(1,2))
        self.assertLess(2*r*r,1)
        self.assertLess(7*r**(result["removed_grade_cut"]+1),1)

    def test_frozen_sources_are_checked_before_replay(self):
        M.authenticate_frozen()

    def test_forged_summary_is_not_an_accepted_fixture(self):
        with self.assertRaises(ValueError):
            M.check_payload({"schema":"actual-global-koszul-lie-cohomology-v1","status":"PASS"})


class CompactSupportCorrectionTests(unittest.TestCase):
    def test_localization_has_actual_compact_support_dimensions(self):
        rows=M.compact_support_controls(0)[0]["compact_support_source_rows"]
        self.assertEqual(rows[0]["h0_h1_h2"],[0,19,1])
        self.assertEqual(rows[0]["full_geometric_boundary_dimension"],14)
        self.assertEqual(rows[1]["h0_h1_h2"],[0,10,1])

    def test_complete_source_split_branch_identity_and_integral_corrected_order(self):
        for index in range(3):
            for row in M.compact_support_controls(index):
                alpha=Fraction(*row["closed_Lie_exponent"])
                removed=Fraction(*row["bad_parent_exponent"])
                self.assertEqual(alpha-removed,row["unramified_split_rational_places"])
                self.assertEqual(row["corrected_Segre_exact_zero_order"],row["unramified_split_rational_places"])

    def test_actual_bad_source_values_do_not_hide_an_extra_zero(self):
        row=M.compact_support_controls(1)[0]
        self.assertEqual([Fraction(*value) for value in row["bad_Segre_values_at_minus_half"]],
                         [Fraction(8,9),Fraction(16,27),Fraction(16,9)])

    def test_cubic_Lie_obstruction_cannot_be_promoted_to_corrected_source(self):
        row=M.compact_support_controls(1)[0]
        self.assertEqual(Fraction(*row["closed_Lie_exponent"]).denominator,3)
        self.assertIsInstance(row["corrected_Segre_exact_zero_order"],int)
        self.assertGreaterEqual(row["corrected_Segre_exact_zero_order"],0)

    def test_compact_support_first_trace_is_actual_unramified_regular_source(self):
        row=M.compact_support_controls(2)[0]
        self.assertEqual(row["compact_support_source_rows"][0]["actual_unramified_trace"],
                         6*row["unramified_split_rational_places"])


if __name__=="__main__":
    unittest.main()

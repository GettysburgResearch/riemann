"""Source multiplication, parity, ramification and analytic assembly controls."""

from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("coherent_quadratic",HERE/"coherent_quadratic_replay.py")
M=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class MultiplicationAndRamificationTests(unittest.TestCase):
    def test_diagonal_colour_is_closed_under_actual_multiplication(self):
        for n in range(6):
            for m in range(6):
                self.assertEqual(M.colour_product(n,n%2,m,m%2),(n+m,(n+m)%2))

    def test_fixed_colour_module_is_not_a_subalgebra(self):
        self.assertEqual(M.colour_product(1,1,1,1),(2,0))
        self.assertNotEqual(M.colour_product(1,1,1,1),(2,1))

    def test_grade_zero_is_principal_not_fixed_module(self):
        row=M.source_rows(0)[0]
        self.assertEqual(row["h0_h1_h2"],[1,0,1])
        self.assertEqual(row["fixed_module_h0_h1_h2"],[0,0,0])
        self.assertEqual(row["kappa"],-1)

    def test_grade_one_agreement_does_not_determine_grade_two(self):
        rows=M.source_rows(2)
        self.assertEqual(rows[1]["h0_h1_h2"],rows[1]["fixed_module_h0_h1_h2"])
        self.assertNotEqual(rows[2]["h0_h1_h2"],rows[2]["fixed_module_h0_h1_h2"])
        self.assertGreater(rows[2]["h0_h1_h2"][0],0)

    def test_principal_poles_have_even_grade_parity(self):
        for row in M.source_rows(48):
            if row["grade"]%2:
                self.assertEqual(row["principal_pole_multiplicity"],0)
            else:
                self.assertGreater(row["principal_pole_multiplicity"],0)

    def test_odd_grade_diagonal_inertia_keeps_zero_trace_stalk(self):
        self.assertEqual(M.infinity_trace(7,1,1),0)
        self.assertEqual(M.infinity_trace(7,1,2),6)
        self.assertEqual(M.infinity_polynomial(7,1),[1,0,-3,0,3,0,-1])

    def test_even_grade_uses_old_inertia_including_grade_zero(self):
        self.assertEqual(M.infinity_polynomial(7,0),[1,-1])
        self.assertEqual(M.infinity_trace(7,2,1),8)
        self.assertEqual(M.infinity_trace(7,2,2),32)
        self.assertNotEqual(M.infinity_trace(7,2,2),M.Q.infinity_trace(7,2,2))

    def test_even_grade_infinity_full_polynomial_not_first_trace_fit(self):
        polynomial=M.infinity_polynomial(7,2)
        self.assertEqual(len(polynomial),33)
        self.assertEqual(M.F.S4.P.local_sums_from_polynomial(polynomial,2),[-8,-32])

    def test_colour_types_and_degree_caps(self):
        for value in (True,1.0,-1,49):
            with self.subTest(value=value),self.assertRaises((ValueError,TypeError)):
                M.colour_product(value,1,1,1)
        with self.assertRaises(ValueError):
            M.infinity_polynomial(7,3)


class ActualSourceAndScalarTests(unittest.TestCase):
    def test_full_fibre_even_odd_projection_matches_cohomology(self):
        for index in range(3):
            self.assertEqual(len(M.fibre_controls(index)),2)

    def test_constant_twist_exchanges_odd_extension_splittings(self):
        for index in range(3):
            data=M.power_data(index,2)
            self.assertEqual(data[0]["constant_twist_points"],2*data[0]["Z_points"]-data[0]["Ztilde_points"])
            self.assertEqual(data[1]["constant_twist_points"],data[1]["Ztilde_points"])

    def test_actual_joint_scalar_weights_are_both_nonnegative(self):
        for row in M.power_data(0,24):
            self.assertGreaterEqual(row["Ztilde_points"],0)
            self.assertGreaterEqual(row["opposite_scalar_points"],0)
            self.assertEqual(row["Ztilde_points"]+row["opposite_scalar_points"],2*row["Z_points"])

    def test_nonidentity_scalar_is_not_dropped_at_minus_one(self):
        result=M.boundary_constant(0,2,Fraction(1,10))
        self.assertGreater(Fraction(*result["omitted_by_identity_only"]),0)
        self.assertEqual(Fraction(*M.boundary_constant(0,1,Fraction(1,10))["omitted_by_identity_only"]),0)

    def test_grade_projection_precedes_even_frobenius_power(self):
        z=Fraction(1,4)
        proper_even,proper_odd=M.parity_sectors(z*z)
        wrong_even=M.F.sectors(z*z)
        self.assertNotEqual(proper_even,wrong_even)
        self.assertTrue(any(proper_odd))
        row=M.power_data(0,2)[1]
        proper=sum(a*b+c*d for a,b,c,d in zip(proper_even,row["untwisted_local"],proper_odd,row["fixed_local"]))
        wrong=sum(a*b for a,b in zip(wrong_even,row["untwisted_local"]))
        self.assertNotEqual(proper,wrong)

    def test_partial_p7_is_not_completed_by_parity_selection(self):
        M.power_data(1,4)
        with self.assertRaises(ValueError):
            M.power_data(1,5)
        with self.assertRaises(ValueError):
            M.determinant_control(1,Fraction(1,10),Fraction(1,2))
        with self.assertRaises(ValueError):
            M.finite_duality(1,1)

    def test_small_recount_fields_and_primitive_parameter_matching(self):
        for index in range(3):
            old,fixed=M.native_pair(index)
            self.assertEqual((old["p"],old["b"],old["c"]),(fixed["p"],fixed["b"],fixed["c"]))
            self.assertLessEqual(max(row["field_order"] for row in fixed["primitive_rows"]),49)

    def test_source_index_validation_precedes_cached_dependencies(self):
        M.native_pair(1)
        for value in (True,1.0,-1,3):
            with self.subTest(value=value),self.assertRaises((ValueError,TypeError)):
                M.native_pair(value)


class CoherentAnalyticTests(unittest.TestCase):
    def test_finite_source_duality_including_principal_grade_zero(self):
        for cut in (0,1,2):
            result=M.finite_duality(0,cut)
            self.assertTrue(result["source_functional_equation"])
        self.assertEqual(M.finite_duality(0,0)["K"],-1)

    def test_source_determinant_and_power_enclosures(self):
        result=M.determinant_control(0,Fraction(1,4),Fraction(1,10))
        self.assertTrue(result["inside_initial_Euler_disk"])
        self.assertEqual(Fraction(*result["separate_signed_grade_zero_factor"]),Fraction(20,9))

    def test_meromorphic_grade_zero_outside_initial_euler_disk(self):
        result=M.determinant_control(0,Fraction(1,10),Fraction(1,2))
        self.assertFalse(result["inside_initial_Euler_disk"])
        self.assertEqual(Fraction(*result["separate_signed_grade_zero_factor"]),Fraction(-4,3))

    def test_explicit_principal_pole_is_rejected_by_log_control(self):
        with self.assertRaises(ValueError):
            M.determinant_control(0,Fraction(1,10),Fraction(1,5))

    def test_actual_plus_and_minus_radial_source_bounds(self):
        for order in (1,2):
            self.assertTrue(M.radial_control(0,order,Fraction(999,1000),Fraction(1,10))["above_half_actual_constant"])

    def test_frozen_dependencies_and_forged_fixture(self):
        M.authenticate_frozen()
        with self.assertRaises(ValueError):
            M.check_payload({"schema":"coherent-quadratic-graded-source-v1","status":"PASS"})

    def test_boundary_domains(self):
        with self.assertRaises(ValueError):
            M.boundary_constant(0,1,Fraction(1,5))
        with self.assertRaises(ValueError):
            M.radial_control(0,1,Fraction(1),Fraction(1,10))


if __name__=="__main__":
    unittest.main()

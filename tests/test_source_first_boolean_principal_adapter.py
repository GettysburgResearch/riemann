"""Correct raw-quotient/completion order, native coefficients, and weighted diagonals."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "research" / "riemann-structures" / "source_first_boolean_principal_adapter.py"
SPEC = importlib.util.spec_from_file_location("source_first_adapter", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SourceFirstAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ea, gc = (M.EA,M.EA_PATH),(M.GC,M.GC_PATH)
        cls.algebra = M.load_primitive(ea,M.source_bytes(ea))
        cls.gauge = M.load_primitive(gc,M.source_bytes(gc))

    def test_actual_raw_squarefree_gauge_and_connection_are_trivial(self):
        result = M.gauge_quotient(self.gauge)
        self.assertEqual(result["raw_columns"],27)
        self.assertEqual(result["squarefree_rows"],8)
        self.assertEqual(result["exact_scalar_checks"],864)
        self.assertEqual(result["local_source"]["g_x_coefficients"][1],["0"])

    def test_source_first_full_derivative_is_nonzero_with_same_sign_pieces(self):
        result = M.completed_path(self.algebra,(3,5,17),(11,13),10)
        self.assertEqual(result["full_integral_times_sqrt_N"],"-1/5")
        self.assertEqual(result["owner_integral_times_sqrt_N"],"-2/25")
        self.assertEqual(result["core_integral_times_sqrt_N"],"-3/25")
        self.assertEqual(result["source_first_tau_polynomial_times_sqrt_N"],["0"]*5+["-1/5"])

    def test_raw_mixed_projection_and_completion_of_raw_squarefree_source_differ(self):
        result = M.completed_path(self.algebra,(3,5,17),(11,13),10)
        self.assertEqual(result["raw_mixed_monomial_full_integral"],"0")
        self.assertNotEqual(result["full_integral_times_sqrt_N"],"0")
        self.assertEqual(result["Boolean_multiplier"],"2")

    def test_exact_physical_coefficient_matches_native_mellin_normalization(self):
        result = M.completed_path(self.algebra,(3,5,17),(11,13),10)
        self.assertEqual(result["P"],143)
        self.assertEqual(result["a"],255)
        self.assertEqual(result["N"],143*255**2)
        self.assertEqual(Fraction(result["coefficient_square"]),Fraction(1,25*143*255**2))
        self.assertEqual(Fraction(result["raw_Euler_coefficient_square"]),Fraction(1,143*255))

    def test_completion_weight_cancels_common_core_exactly_and_bound_is_sharp(self):
        first = M.completion_ratio((3,),(5,))
        second = M.completion_ratio((3,7,11),(5,7,11))
        self.assertEqual(first["squared_completion_norm_ratio"],"3")
        self.assertEqual(second["squared_completion_norm_ratio"],"3")
        self.assertEqual(second["g"],77)
        self.assertEqual(Fraction(second["weight"]),77**2*45)

    def test_literal_boolean_histories_are_kept_and_their_diagonal_is_distinct(self):
        result = M.completed_path(self.algebra,(3,5,17),(11,13),10)
        self.assertEqual(len(result["rows"]["nonzero_balanced_histories"]),2)
        self.assertEqual(result["history_energy"],2)
        self.assertEqual(result["rows"]["balanced"]**2,4)
        self.assertLessEqual(result["history_energy"],9**3)

    def test_complete_equal_pair_column_is_contractively_split(self):
        for support in ((3,5,7,11,13),(3,5,7,11,13,17)):
            result = M.owner_column(self.algebra,support,10)
            self.assertEqual(Fraction(result["owner_only_column_energy"]),
                             Fraction(1,result["unordered_pairs"]))

    def test_closed_or_aliased_records_cannot_be_promoted_to_clean_phase_sector(self):
        for left,right in (((3,3),(5,)),((3,),(3,)),((True,3),(5,)),((2,),(5,)),((9,),(3,))):
            with self.subTest(left=left,right=right), self.assertRaises(ValueError):
                M.completion_ratio(left,right)
        with self.assertRaises(ValueError):
            M.completed_path(self.algebra,(3,5,67),(67,13),10)
        with self.assertRaises(ValueError):
            M.owner_column(self.algebra,(3,9,5,7),10)
        with self.assertRaises(ValueError):
            M.evaluate((Fraction(1),),0.5)

    def test_authentication_rejects_mutated_executable_or_primitive_source(self):
        with self.assertRaisesRegex(ValueError,"executable Git blob"):
            M.load_primitive((M.EA,M.EA_PATH),b"raise RuntimeError('not executed')")
        first = type("Size",(),{"stdout":"3"})()
        second = type("Bytes",(),{"stdout":b"bad"})()
        with (patch.object(M.subprocess,"run",side_effect=[first,second]),
              self.assertRaisesRegex(ValueError,"Git blob")):
            M.source_bytes(next(iter(M.SOURCES)))

    def test_numeric_json_types_are_part_of_acceptance(self):
        self.assertNotEqual(M.canonical({"n":1}),M.canonical({"n":True}))
        self.assertNotEqual(M.canonical({"n":1}),M.canonical({"n":1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n":float("nan")} )


if __name__ == "__main__":
    unittest.main()

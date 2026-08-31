"""Complete canonical cofactor cancellation and full positive-fibre boundaries."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "research" / "riemann-structures" / "complete_boolean_fibre_positivity_obstruction.py"
SPEC = importlib.util.spec_from_file_location("complete_boolean_fibres",PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CompleteBooleanFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.algebra = M.load_primitive((M.EA,M.EA_PATH),M.source_bytes((M.EA,M.EA_PATH)))

    def test_complete_all_rough_coefficients_have_exact_parity(self):
        values = [M.rough_parity(self.algebra,(257,263,269,271)[:k],256) for k in range(1,5)]
        self.assertEqual([r["balanced"] for r in values],[0,2,0,2])
        self.assertEqual(values[1]["canonical_coefficient"],"1/3")
        self.assertEqual(values[2]["canonical_coefficient"],"0")

    def test_four_rough_factors_are_excluded_by_actual_horizon(self):
        record = M.rough_parity(self.algebra,(257,263,269,271),256)
        self.assertTrue(record["depth_four_horizon_excluded"])
        self.assertGreater(6*M.prod(record["labels"])**2,16*256**6)

    def test_literal_kernel_transform_has_a_certified_simple_zero(self):
        record = M.kernel_transform_identity()
        self.assertEqual(record["C_polynomial"],[["-4","0"],["8","4"],["-4","-8"],["0","4"]])
        self.assertEqual(record["first_slope_divided_by_log2_squared"],["-8","8"])
        self.assertEqual(record["Fourier_zero_order_at_zero"],1)
        self.assertFalse(record["floating_evaluations"])

    def test_genuine_extra_cofactor_keeps_phase_and_physical_mask(self):
        record = M.zero_cofactor_chart(self.algebra)
        self.assertEqual(record["c"],263*269)
        self.assertEqual(record["ell"],263)
        self.assertLess(Fraction(record["N"],record["M"]),8)
        self.assertLessEqual(record["N"],16*record["Y"])
        self.assertFalse(record["cofactor_deleted_by_mask"])

    def test_zero_cofactor_uses_all_signed_histories_not_a_selected_row(self):
        record = M.zero_cofactor_chart(self.algebra)
        terms = [Fraction(v) for v in record["signed_bilateral_coefficients_before_physical_factor"]]
        self.assertEqual(len(terms),24)
        self.assertEqual(terms.count(Fraction(1,60)),12)
        self.assertEqual(terms.count(Fraction(-1,60)),12)
        self.assertEqual(sum(terms),0)
        self.assertGreater(Fraction(record["literal_history_diagonal"]),0)

    def test_nonrough_nonsquarefree_or_composite_support_is_refused(self):
        for labels in ((251,263),(257,257),(257,267),(True,263)):
            with self.subTest(labels=labels), self.assertRaises(ValueError):
                M.rough_parity(self.algebra,labels,256)

    def test_bounds_reject_numeric_aliases_and_excess_work(self):
        for cutoff in (True,256.0,1000000000):
            with self.subTest(cutoff=cutoff), self.assertRaises(ValueError):
                M.rough_parity(self.algebra,(257,263),cutoff)
        with self.assertRaises(ValueError):
            M.prime(1 << 200)

    def test_no_untrusted_primitive_execution_or_mutable_source_substitution(self):
        with self.assertRaises(ValueError):
            M.load_primitive((M.EA,M.EA_PATH),b"raise RuntimeError('untrusted')")
        key = (M.EA,M.EA_PATH)
        with patch.dict(M.SOURCES,{key:"0"*40}), self.assertRaises(ValueError):
            M.source_bytes(key)

    def test_full_build_replays_frozen_dense_candidate_without_native_promotion(self):
        result = M.build()
        self.assertEqual(result["inherited_dense_source_record"]["arithmetic_pairs"],16)
        self.assertTrue(result["all_selected_fibre_core_cofactors_classified"])
        self.assertFalse(result["complete_candidate_matching_upper_claimed"])
        self.assertFalse(result["full_native_moment_lower_bound_asserted"])
        self.assertFalse(result["cone_measure_numerically_estimated"])

    def test_typed_acceptance_rejects_equal_python_numeric_counterfeits(self):
        self.assertNotEqual(M.canonical({"x":1}),M.canonical({"x":True}))
        self.assertNotEqual(M.canonical({"x":1}),M.canonical({"x":1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"x":float("nan")})


if __name__ == "__main__":
    unittest.main()

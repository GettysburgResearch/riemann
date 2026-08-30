"""Post-Wick actual Boolean histories, full channels, and unchanged source weights."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "research" / "riemann-structures" / "native_off_atomic_conductor_cancellation.py"
SPEC = importlib.util.spec_from_file_location("off_atomic_conductors",PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class OffAtomicConductorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.algebra = M.load_algebra(M.source_bytes((M.EA,M.EA_PATH)))
        cls.record = M.record(cls.algebra)

    def test_fixed_owner_cofinal_windows_have_native_physical_shell(self):
        constants = M.window_constants()
        for key in ("N_lower","N_upper","M_lower","M_upper"):
            self.assertLess(Fraction(constants[key]),Fraction(11,10))
            self.assertGreater(Fraction(constants[key]),1)
        self.assertEqual(constants["PNT_count_constant_U5_over_log3"],"1/400000000")

    def test_complete_boolean_rows_have_only_two_positive_histories(self):
        for key in ("left_boolean","right_boolean"):
            rows = self.record[key]
            self.assertEqual(rows["complete_allocations"],9)
            self.assertEqual(rows["balanced"],2)
            self.assertEqual([h["coefficient"] for h in rows["nonzero_balanced_histories"]],[1,1])
        self.assertEqual(self.record["canonical_share"],"1/6")

    def test_literal_wick_leaves_twelve_equal_output_ordered_pairs(self):
        self.assertEqual(self.record["literal_histories"],4)
        self.assertEqual(self.record["off_atomic_ordered_pairs"],12)
        self.assertEqual(self.record["distinct_output_pairs_in_fibre"],0)
        n,m = self.record["N"],self.record["M"]
        self.assertEqual(Fraction(self.record["literal_off_atomic_without_weights"]),Fraction(1,108*n*m))

    def test_merging_histories_changes_the_subtracted_diagonal(self):
        old = Fraction(self.record["literal_diagonal_without_weights"])
        new = Fraction(self.record["merged_new_diagonal_without_weights"])
        self.assertEqual(new,4*old)
        self.assertEqual(new-old,Fraction(self.record["literal_off_atomic_without_weights"]))
        self.assertEqual(self.record["merged_new_wick_form_without_weights"],"0")

    def test_all_mixed_and_double_channels_recover_small_principal_difference(self):
        a,p,k,mixed,nn = (Fraction(self.record[key]) for key in
                         ("A_divided_by_Gamma0","P_divided_by_Gamma0","K_divided_by_Gamma0",
                          "mixed_divided_by_Gamma0","NN_divided_by_Gamma0"))
        self.assertEqual(a-k,p)
        self.assertEqual(k,mixed+nn)
        self.assertGreater(mixed,0)
        self.assertGreater(nn,0)
        self.assertLess(p/a,Fraction(1,1000000))

    def test_principal_energy_and_literal_diagonal_are_paid_separately(self):
        p = Fraction(self.record["P_divided_by_Gamma0"])
        self.assertEqual(Fraction(self.record["principal_literal_diagonal_divided_by_Gamma0"]),p/3)
        self.assertEqual(Fraction(self.record["principal_full_energy_divided_by_Gamma0"]),4*p/3)

    def test_actual_quadratic_classes_are_recorded_without_forcing_plus(self):
        _,ell,rho,sigma,tau = self.record["fibre"]
        self.assertEqual(pow(M.Q,(ell-1)//2,ell),1 if sigma==1 else ell-1)
        self.assertEqual(pow(M.P,(rho-1)//2,rho),1 if tau==1 else rho-1)

    def test_nonprime_out_of_window_and_wrong_cutoff_are_refused(self):
        for value in (True,2,9,10001):
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.prime(value)
        for kwargs in ({"cutoff":255},{"ell":3693},{"common":263}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                M.record(self.algebra,**kwargs)

    def test_tampered_executable_and_source_blob_are_refused(self):
        with self.assertRaises(ValueError):
            M.load_algebra(b"raise RuntimeError('untrusted')")
        key = (M.EA,M.EA_PATH)
        with patch.dict(M.SOURCES,{key:"0"*40}), self.assertRaises(ValueError):
            M.source_bytes(key)

    def test_typed_json_and_full_build_keep_the_scope(self):
        self.assertNotEqual(M.canonical({"x":1}),M.canonical({"x":True}))
        self.assertNotEqual(M.canonical({"x":1}),M.canonical({"x":1.0}))
        result = M.build()
        self.assertFalse(result["whole_source_moment_counterexample"])
        self.assertFalse(result["global_WCEQ_refuted"])
        self.assertEqual(result["prime_searches"],0)


if __name__ == "__main__":
    unittest.main()

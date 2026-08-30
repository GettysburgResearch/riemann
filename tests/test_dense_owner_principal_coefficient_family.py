"""Actual owner sharing, complete class partition, native Gram and literal diagonal."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "research" / "riemann-structures" / "dense_owner_principal_coefficient_family.py"
SPEC = importlib.util.spec_from_file_location("dense_owner_family",PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class DenseOwnerFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.algebra = M.load_primitive((M.EA,M.EA_PATH),M.source_bytes((M.EA,M.EA_PATH)))
        cls.data = json.loads(M.PRIMES.read_text(encoding="utf-8"))
        cls.record = M.record(cls.algebra,cls.data)

    def test_all_source_owner_pairs_and_literal_histories_are_retained(self):
        self.assertEqual(self.record["arithmetic_pairs"],16)
        self.assertEqual(self.record["literal_histories"],64)
        self.assertEqual(len({e["P"] for e in self.record["entries"]}),4)
        self.assertEqual(len({e["Q"] for e in self.record["entries"]}),4)

    def test_complete_native_quadratic_partition_is_not_replaced_by_one_class(self):
        counts = self.record["class_pair_counts"]
        self.assertEqual({tuple(row["class"]) for row in counts},set(M.product((-1,1),repeat=2)))
        self.assertEqual(sum(row["pairs"] for row in counts),16)
        self.assertEqual(sum(row["pairs"]**2 for row in counts),self.record["native_Gram_ratio_checks"])

    def test_distribution_free_class_lower_bound_handles_empty_and_balanced_classes(self):
        self.assertEqual(M.class_lower_bound((4,0),(4,0)),256)
        self.assertEqual(M.class_lower_bound((2,2),(2,2)),64)
        with self.assertRaises(ValueError):
            M.class_lower_bound((True,3),(2,2))

    def test_native_positive_irrational_coefficients_have_exact_four_history_square(self):
        for row in self.record["entries"]:
            square = Fraction(row["coefficient_square"])
            self.assertEqual(square,Fraction(1,81*row["N"]*row["M"]))
            self.assertEqual(square,16*Fraction(row["one_literal_square"]))
            self.assertIs(row["positive_branch"],True)

    def test_source_vector_diagonal_relative_lower_bound_and_paid_history_correction(self):
        self.assertGreaterEqual(Fraction(self.record["certified_energy_over_literal_diagonal_lower"]),16*M.LOWER)
        self.assertEqual(Fraction(self.record["equal_pair_principal_correction_divided_by_Gamma0"]),
                         3*Fraction(self.record["literal_principal_diagonal_divided_by_Gamma0"]))

    def test_all_prime_windows_and_independent_primality_are_enforced(self):
        for value in (1049625,True,1 << 40):
            data = copy.deepcopy(self.data)
            data["windows"]["p"]["primes"][0] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.validate_primes(data)

    def test_owner_reuse_within_one_side_is_legal_but_window_aliases_are_not(self):
        pvalues = {row["P"] for row in self.record["entries"]}
        self.assertTrue(any(M.gcd(p,q) > 1 for p,q in M.product(pvalues,repeat=2) if p != q))
        data = copy.deepcopy(self.data)
        data["windows"]["q"]["primes"][0] = data["windows"]["p"]["primes"][0]
        with self.assertRaises(ValueError):
            M.validate_primes(data)

    def test_cutoff_and_fixture_acquisition_caps_are_exact(self):
        for key,value in (("U",float(1 << 20)),("candidate_cap_per_window",201)):
            data = copy.deepcopy(self.data)
            data[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                M.validate_primes(data)

    def test_untrusted_primitive_or_wrong_blob_cannot_be_executed(self):
        with self.assertRaises(ValueError):
            M.load_primitive((M.EA,M.EA_PATH),b"raise RuntimeError('untrusted')")
        key = (M.EA,M.EA_PATH)
        with patch.dict(M.SOURCES,{key:"0"*40}), self.assertRaises(ValueError):
            M.source_bytes(key)

    def test_typed_json_build_preserves_full_source_boundary(self):
        self.assertNotEqual(M.canonical({"n":1}),M.canonical({"n":True}))
        self.assertNotEqual(M.canonical({"n":1}),M.canonical({"n":1.0}))
        result = M.build()
        self.assertFalse(result["full_native_principal_moment_refuted"])
        self.assertFalse(result["projection_proved_orthogonal_in_Mellin_norm"])
        self.assertEqual(result["prime_searches_during_replay"],0)


if __name__ == "__main__":
    unittest.main()

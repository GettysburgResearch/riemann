"""Source and hostile-acceptance controls for the actual Chow Tor Q action."""

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/q_action.py"
)
SPEC = importlib.util.spec_from_file_location("equivariant_pass_q_action", PATH)
Q = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(Q)


class SmallSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.k1 = Q.Complex(2, 1)
        cls.k2 = Q.Complex(2, 2)
        cls.k3 = Q.Complex(2, 3)
        cls.h01 = Q.Homology(cls.k1, 0)
        cls.h02 = Q.Homology(cls.k2, 0)
        cls.h12 = Q.Homology(cls.k2, 1)
        cls.h13 = Q.Homology(cls.k3, 1)
        cls.qb = Q.complementary_basis(2)
        cls.rows, cls.matrices = Q.action(cls.h12, cls.h13, cls.qb)

    def test_literal_chain_dimensions(self):
        self.assertEqual(list(map(len, self.k2.chains)), [36, 54, 15])
        self.assertEqual(list(map(len, self.k3.chains)), [100, 216, 135, 20])

    def test_calibration_homology_not_euler_coefficients(self):
        self.assertEqual(
            [len(h.cycles) for h in (self.h01, self.h02, self.h12, self.h13)],
            [3, 0, 3, 1],
        )

    def test_complement_has_zero_symmetrizer(self):
        for m, expected in ((2, 3), (3, 17)):
            basis = Q.complementary_basis(m)
            self.assertEqual(len(basis), expected)
            for _, terms in basis:
                self.assertEqual(sum(terms.values()), 0)
                self.assertTrue(any(a > 0 for a in terms.values()))

    def test_actual_boundary_identities(self):
        Q.verify_action_rows(self.h12, self.h13, self.qb, self.rows)
        self.assertEqual(len(self.rows), 9)

    def test_actual_W_wedge_homotopies(self):
        self.assertEqual(len(Q.w_homotopies(self.h12, self.h13)), 18)

    def test_factor_action_on_homology(self):
        record = Q.equivariance(self.h12, self.h13, self.qb, self.matrices, (1, 0))
        self.assertTrue(record["verified"])
        source = [Q.decode_vector(row, 3) for row in record["source_homology"]]
        target = [Q.decode_vector(row, 1) for row in record["target_homology"]]
        self.assertEqual(sum(source[i].get(i, 0) for i in range(3)), -3)
        self.assertEqual(target, [{0: Fraction(1)}])

    def test_action_column_omission_refused(self):
        with self.assertRaisesRegex(ValueError, "coverage"):
            Q.verify_action_rows(self.h12, self.h13, self.qb, self.rows[:-1])

    def test_action_address_bool_refused(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["q"] = False
        with self.assertRaisesRegex(ValueError, "address"):
            Q.verify_action_rows(self.h12, self.h13, self.qb, bad)

    def test_action_coefficient_corruption_refused(self):
        bad = copy.deepcopy(self.rows)
        bad[0]["image"] = [[0, 999, 1]]
        with self.assertRaisesRegex(ValueError, "original source identity"):
            Q.verify_action_rows(self.h12, self.h13, self.qb, bad)

    def test_boundary_witness_corruption_refused(self):
        bad = copy.deepcopy(self.rows)
        row = next(row for row in bad if row["boundary"])
        row["boundary"][0][1] += row["boundary"][0][2]
        with self.assertRaises(ValueError):
            Q.verify_action_rows(self.h12, self.h13, self.qb, bad)

    def test_changed_source_cycle_refused(self):
        original = self.h12.cycles[0]
        self.h12.cycles[0] = {0: Fraction(123)}
        try:
            with self.assertRaises(ValueError):
                Q.verify_action_rows(self.h12, self.h13, self.qb, self.rows)
        finally:
            self.h12.cycles[0] = original


class HostileEncoding(unittest.TestCase):
    def test_duplicate_keys_refused(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            Q.strict_json(b'{"x":1,"x":2}')

    def test_floating_and_nonfinite_numbers_refused(self):
        for raw in (b'{"x":[1.0]}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.assertRaises(ValueError):
                Q.strict_json(raw)

    def test_sparse_boolean_float_and_repeated_indices_refused(self):
        for rows in (
            [[False, 1, 1]],
            [[0, True, 1]],
            [[0, 1, 1.0]],
            [[0, 1, 1], [0, 2, 1]],
            [[0, 2, 2]],
        ):
            with self.assertRaises(ValueError):
                Q.decode_vector(rows, 3)

    def test_numeric_counterfeit_with_fresh_digest_refused(self):
        expected = {"count": 1}
        expected["proof_sha256"] = hashlib.sha256(
            Q.canonical(expected).encode()
        ).hexdigest()
        bad = {"count": True}
        bad["proof_sha256"] = hashlib.sha256(Q.canonical(bad).encode()).hexdigest()
        with self.assertRaisesRegex(ValueError, "typed"):
            Q.check_record(bad, expected)

    def test_bad_digest_refused(self):
        with self.assertRaisesRegex(ValueError, "digest"):
            Q.check_record({"proof_sha256": "0" * 64}, {})

    def test_bounds_before_large_allocation(self):
        for call in (
            lambda: Q.Complex(3, 4),
            lambda: Q.source_basis(4, 3),
            lambda: Q.complementary_basis(True),
            lambda: Q.rational(1 << 4096),
        ):
            with self.assertRaises(ValueError):
                call()

    def test_exact_span_witness_and_no_false_membership(self):
        span = Q.Span()
        span.insert({0: Fraction(2), 1: Fraction(3)}, {7: Fraction(1)})
        self.assertEqual(
            span.coordinates({0: Fraction(4), 1: Fraction(6)}), {7: Fraction(2)}
        )
        with self.assertRaisesRegex(ValueError, "outside"):
            span.coordinates({0: Fraction(4), 1: Fraction(5)})

    def test_gram_rank_annihilator_is_not_zero_action_assumption(self):
        self.assertEqual(
            Q.q_annihilator_dimension([[{0: Fraction(1)}], [{0: Fraction(2)}], [{}]]), 2
        )


if __name__ == "__main__":
    unittest.main()

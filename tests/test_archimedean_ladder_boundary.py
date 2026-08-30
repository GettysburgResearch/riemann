"""Bounded exact tests, not a numerical certificate for gamma continuation."""

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "research/riemann-structures/archimedean_ladder_boundary.py"
SPEC = importlib.util.spec_from_file_location("archimedean_ladder_boundary", MODULE)
ladder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ladder
SPEC.loader.exec_module(ladder)
Term = ladder.GammaTerm


class ArchimedeanLadderTests(unittest.TestCase):
    def test_empty_product(self):
        self.assertTrue(ladder.reduce_shifts(())["rational"])
        self.assertEqual(ladder.rational_value((), 5, 7), 1)

    def test_effective_product_not_rational(self):
        for terms in ((Term(0, 1),), (Term(0, 1), Term(1, 1)), (Term(-4, 2),)):
            self.assertFalse(ladder.reduce_shifts(terms)["rational"])

    def test_total_multiplicity_not_enough(self):
        data = ladder.reduce_shifts((Term(1, 1), Term(0, -1)))
        self.assertFalse(data["rational"])
        self.assertEqual(data["tail_multiplicities"], [["0", -1], ["1", 1]])

    def test_forward_and_backward_shift(self):
        self.assertEqual(ladder.rational_value((Term(2, 1), Term(0, -1)), 5, 7), Fraction(5, 7))
        self.assertEqual(ladder.rational_value((Term(-2, 1), Term(0, -1)), 5, 7), Fraction(7, 3))

    def test_fractional_shift_heldout(self):
        terms = (Term(Fraction(17, 3), 1), Term(Fraction(-1, 3), -1))
        value = ladder.rational_value(terms, 4, 7)
        self.assertEqual(value, Fraction(11 * 17 * 23, 27 * 343))

    def test_exact_repeated_cancellation(self):
        data = ladder.reduce_shifts((Term(4, 2), Term(4, -2)))
        self.assertTrue(data["rational"])
        self.assertEqual(data["two_pi_power"], 0)
        self.assertEqual(data["linear_factors"], [])

    def test_stable_divisor_tail(self):
        terms = (Term(Fraction(-7, 3), 2), Term(Fraction(5, 3), -1))
        rows = ladder.stable_tails(terms)
        self.assertEqual(rows[0]["orders"], [-1, -1, -1])
        self.assertEqual(ladder.divisor_order(terms, Fraction(-100)), 0)

    def test_unbalanced_value_rejected(self):
        with self.assertRaises(ValueError):
            ladder.rational_value((Term(1, 1),), 5, 7)

    def test_exact_input_contract(self):
        for value in (True, 0.5, "1/2"):
            with self.assertRaises(TypeError):
                Term(value, 1)
        for value in (True, 0.5):
            with self.assertRaises(TypeError):
                Term(0, value)
        for value in (-1, 2, True):
            with self.assertRaises(ValueError):
                ladder.tensor_data(value, 0)

    def test_all_tensor_intertwiners(self):
        for e, f in product((0, 1), repeat=2):
            row = ladder.pair_record(e, f)
            self.assertEqual(row["cokernel_dimension"], e * f)
            self.assertEqual(row["basis_checks"], 25)

    def test_all_triple_associativities(self):
        for values in product((0, 1), repeat=3):
            row = ladder.triple_record(*values)
            self.assertEqual(row["left_u_power"], row["right_u_power"])

    def test_dual_defect(self):
        self.assertTrue(ladder.dual_record(0)["perfect_over_A"])
        self.assertFalse(ladder.dual_record(1)["perfect_over_A"])

    def test_source_authentication(self):
        self.assertEqual(ladder.authenticate_sources()["frozen_programme_blob"], ladder.SOURCE_BLOB)

    def test_frozen_fixture(self):
        self.assertEqual(json.loads(ladder.FIXTURE.read_text(encoding="utf-8")), ladder.build_report())

    def test_distinct_tensor_products(self):
        report = ladder.build_report()
        self.assertEqual(report["ordinary_C_tensor_multiplicities"], list(range(1, 8)))
        self.assertEqual(report["balanced_A_tensor_multiplicity"], 1)
        self.assertEqual(report["spacing_one_split"], list(range(12)))


if __name__ == "__main__":
    unittest.main()

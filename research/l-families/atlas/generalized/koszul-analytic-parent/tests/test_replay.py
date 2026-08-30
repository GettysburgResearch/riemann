"""Independent exact controls and fail-closed cases for the source replay."""

from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("koszul23_replay", HERE / "replay.py")
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class KoszulSourceTests(unittest.TestCase):
    def test_source_fibres_partition_ordered_quadratics(self):
        fibres = R.quadratic_fibres()
        self.assertEqual(len(fibres), 18)
        words = [word for fibre in fibres for word in fibre]
        self.assertEqual(len(words), 36)
        self.assertEqual(len(set(words)), 36)
        for fibre in fibres:
            self.assertEqual(len({R.word_weight(word) for word in fibre}), 1)

    def test_source_quotient_and_lie_dimensions(self):
        self.assertEqual(
            [(R.source_grade(n)[0], len(R.source_grade(n)[2])) for n in (1, 2, 3)],
            [(6, 6), (18, 3), (40, 2)],
        )

    def test_native_degree_two_weights(self):
        self.assertEqual(
            set(R.source_grade(2)[2]),
            {(1, 1, 1, 1, 0), (1, 1, 1, 0, 1), (1, 1, 0, 1, 1)},
        )

    def test_native_degree_three_weights(self):
        self.assertEqual(set(R.source_grade(3)[2]), {(2, 1, 1, 1, 1), (1, 2, 1, 1, 1)})

    def test_odd_bracket_and_mixed_parity(self):
        self.assertEqual(R.bracket({(0,): 1}, {(1,): 1}, 1, 1), {(0, 1): 1, (1, 0): 1})
        self.assertEqual(
            R.bracket({(0,): 1}, {(1, 2): 1}, 1, 2), {(0, 1, 2): 1, (1, 2, 0): -1}
        )

    def test_no_tensor_expansion_beyond_cap(self):
        for value in (0, 4, 1000000, True, 2.0):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                R.source_grade(value)

    def test_echelon_rejects_invalid_column(self):
        with self.assertRaises(ValueError):
            R.Echelon(6).insert({6: 1})

    def test_native_resolution(self):
        self.assertTrue(R.polynomial_control()["composition_zero"])


class CharacterAndAnalyticTests(unittest.TestCase):
    def test_mobius_and_deviations(self):
        self.assertEqual(
            [R.mobius(n) for n in range(1, 9)], [1, -1, -1, 0, -1, 1, -1, 0]
        )
        self.assertEqual(
            [R.multiplicity(n) for n in range(1, 9)], [6, 3, 2, 3, 6, 11, 18, 30]
        )

    def test_formal_product_full_degree_24(self):
        self.assertEqual(R.signed_euler_series(24), R.hilbert(24))

    def test_even_sign_is_necessary(self):
        self.assertEqual(R.hilbert(2)[2], 21 - 3)
        self.assertNotEqual(R.hilbert(2)[2], 21 + 3)

    def test_repeated_inputs_are_allowed(self):
        result = R.equivariant_control((R.ONE, R.ONE), (R.ONE, R.ONE, R.ONE))
        self.assertEqual(
            result["numerator"],
            [
                R.gjson(R.ONE),
                R.gjson(R.ZERO),
                R.gjson((Fraction(-3), Fraction(0))),
                R.gjson((Fraction(2), Fraction(0))),
            ],
        )

    def test_held_out_torus_character(self):
        a = ((Fraction(5, 13), Fraction(12, 13)), R.I)
        b = (R.neg(R.ONE), R.I, R.I)
        R.equivariant_control(a, b, 16)

    def test_dual_action_is_detectably_wrong(self):
        trace = R.character(R.source_grade(1)[2], (R.ONE, R.I), (R.ONE, R.ONE, R.ONE))
        self.assertEqual(trace, (Fraction(3), Fraction(3)))
        self.assertNotEqual(trace, (trace[0], -trace[1]))

    def test_nonunitary_input_rejected(self):
        with self.assertRaises(ValueError):
            R.equivariant_control(((2, 0), R.ONE), (R.ONE, R.ONE, R.ONE))

    def test_rational_tail_enclosures(self):
        for t in (Fraction(1, 4), Fraction(-1, 4), Fraction(1, 3)):
            self.assertLess(Fraction(*R.enclosure(t, 8)["log_tail_bound"]), 1)

    def test_trace_boundary_not_silently_included(self):
        for radius in (Fraction(1, 2), Fraction(3, 4), -1):
            with self.subTest(radius=radius), self.assertRaises(ValueError):
                R.log_tail_bound(radius, 8)

    def test_too_coarse_enclosure_rejected(self):
        with self.assertRaises(ValueError):
            R.enclosure(Fraction(1, 3), 1)

    def test_numeric_types_and_caps(self):
        for value in (True, 0.25, "1/4"):
            with self.subTest(value=value), self.assertRaises(TypeError):
                R.rational(value)
        with self.assertRaises(ValueError):
            R.signed_euler_series(25)
        with self.assertRaises(ValueError):
            R.multiplicity(65)


class AuthenticationTests(unittest.TestCase):
    def test_frozen_source_authentication(self):
        self.assertEqual(R.authenticate()["precursor_commit"], R.FREEZE)

    def test_source_change_rejected(self):
        changed = json.loads(json.dumps(R.SOURCE))
        changed["ranks"] = [2, 4]
        with self.assertRaises(ValueError):
            R.authenticate_source(changed)

    def test_boolean_source_change_rejected(self):
        changed = json.loads(json.dumps(R.SOURCE))
        changed["generators_row_column"][0][0] = False
        with self.assertRaises(ValueError):
            R.authenticate_source(changed)

    def test_consistent_looking_forged_fixture_rejected(self):
        with self.assertRaises(ValueError):
            R.check_payload({"schema": "koszul23-exact-replay-v1", "claims": "PASS"})


if __name__ == "__main__":
    unittest.main()

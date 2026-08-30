"""Independent source and Frobenius-orbit controls for the descent extension."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "cubic_descent_replay", HERE / "descent_replay.py"
)
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)
P = D.P


class FieldExtensionTests(unittest.TestCase):
    def test_larger_moduli_have_no_possible_small_factor(self):
        for n in (5, 6):
            f = D.DescentField(5, n)
            # All monic divisors up to half the degree, independently of Rabin.
            for degree in range(1, n // 2 + 1):
                for code in range(5**degree):
                    divisor = list(P.digits(code, 5, degree)) + [1]
                    self.assertNotEqual(P.remainder(f.modulus, divisor, 5), [0])
            for a in range(1, 40):
                self.assertEqual(f.power(a, f.q), a)
                self.assertEqual(f.power(a, f.q - 1), 1)

    def test_new_model_agrees_with_frozen_model_where_domains_overlap(self):
        for n in (1, 2, 3, 4):
            old, new = P.Field(5, n), D.DescentField(5, n)
            self.assertEqual(old.modulus, new.modulus)
            for a, b in ((1, 2), (3, 4), (old.q - 1, old.q - 2), (old.q // 2, 2)):
                self.assertEqual(old.mul(a, b), new.mul(a, b))
                self.assertEqual(old.power(a, old.q), new.power(a, new.q))

    def test_caps_and_invalid_powers_fail_before_expansion(self):
        for p, n in ((7, 6), (5, 7), (True, 2), (5, True), (5, 6.0)):
            with self.assertRaises((TypeError, ValueError)):
                D.DescentField(p, n)
        f = D.DescentField(5, 1)
        for exponent in (-1, True, 2.0, D.FIELD_CAP + 1):
            with self.assertRaises((TypeError, ValueError)):
                f.power(2, exponent)


class DescentCharacterTests(unittest.TestCase):
    def test_character_frobenius_reverses_cubic_orientation(self):
        for n in (2, 4):
            field = D.DescentField(5, n)
            data = D.cube_character(field)
            for t in range(1, field.q):
                self.assertEqual(
                    data["exponents"][field.power(t, 5)], 2 * data["exponents"][t] % 3
                )

    def test_root_relabeling_preserves_the_special_rational_trace(self):
        field = D.DescentField(5, 2)
        data = D.cube_character(field)
        reverse = {
            "eta": field.mul(data["eta"], data["eta"]),
            "exponents": [None] + [2 * e % 3 for e in data["exponents"][1:]],
        }
        hist = D.power_histograms(field)
        for A, B in ((1, 1), (-1, 0)):
            left = D.count_curves(field, A, B, hist, data)
            right = D.count_curves(field, A, B, hist, reverse)
            self.assertEqual(
                left["geometric_character_sums"], right["geometric_character_sums"]
            )
            for value in left["geometric_character_sums"]:
                self.assertEqual(value[1], 0)

    def test_odd_extension_has_no_cubic_character_or_orbit_trace(self):
        for n in (1, 3, 5):
            field = D.DescentField(5, n)
            with self.assertRaises(ValueError):
                D.cube_character(field)
            row = D.count_curves(field, 1, 1, D.power_histograms(field))
            self.assertEqual(row["C_points"], row["E_points"])
            self.assertEqual(row["Eprime_points"], field.q + 1)
            self.assertEqual(row["descended_infinity_trace"], 0)

    def test_even_extension_requires_character_and_two_infinity_traces(self):
        field = D.DescentField(5, 2)
        hist = D.power_histograms(field)
        with self.assertRaises(ValueError):
            D.count_curves(field, 1, 1, hist)
        row = D.count_curves(field, 1, 1, hist, D.cube_character(field))
        self.assertEqual(row["descended_infinity_trace"], 2)
        self.assertEqual(row["Eprime_and_C_infinity_points"], 3)
        self.assertEqual(row["Eprime_points"], 36)


class CurveAndDeterminantTests(unittest.TestCase):
    def test_prime_counts_in_all_three_original_equations(self):
        field = D.DescentField(5, 1)
        hist = D.power_histograms(field)
        for A, B in ((1, 1), (-1, 0)):
            row = D.count_curves(field, A, B, hist)
            for power, key in ((2, "E_points"), (3, "Eprime_points"), (6, "C_points")):
                direct = 1 + sum(
                    (z**power - x**3 - A * x - B) % 5 == 0
                    for x in range(5)
                    for z in range(5)
                )
                self.assertEqual(row[key], direct)

    def test_cycle_substitution_from_independent_power_traces(self):
        # A two-block cycle with return eigenvalues 1,2,3 has zero odd traces
        # and twice the return trace at even powers, regardless of basis.
        return_polynomial = [1, -6, 11, -6]
        orbit = D.substitute_degree(return_polynomial, 2)
        sums = P.local_sums_from_polynomial(orbit, 6)
        expected = [0, -2 * (1 + 2 + 3), 0, -2 * (1 + 4 + 9), 0, -2 * (1 + 8 + 27)]
        self.assertEqual(sums, expected)
        self.assertNotEqual(
            P.local_sums_from_polynomial(return_polynomial, 6), expected
        )

    def test_forced_factor_sign_and_reciprocal_completion(self):
        for b in range(-10, 11):
            orbit = D.int_product([1, 0, 5], [1, 0, b, 0, 25])
            self.assertEqual(orbit, [1, 0, b + 5, 0, 5 * b + 25, 0, 125])
            self.assertNotEqual(orbit, D.int_product([1, 0, -5], [1, 0, b, 0, 25]))
        self.assertEqual(
            D.reciprocal_completion([1, 2, 3, 4, 5], 5, 4),
            [1, 2, 3, 4, 5, 20, 75, 250, 625],
        )

    def test_wrong_curve_and_numeric_source_refused(self):
        field = D.DescentField(5, 1)
        hist = D.power_histograms(field)
        for A, B in ((0, 1), (2, 2), (True, 1), (1, 1.0)):
            with self.assertRaises((TypeError, ValueError)):
                D.count_curves(field, A, B, hist)
        source = json.loads((HERE / "descent_source.json").read_text(encoding="utf-8"))
        self.assertEqual(P.digest(source), D.EXPECTED_SOURCE_HASH)
        forged = copy.deepcopy(source)
        forged["p"] = 5.0
        with self.assertRaises(ValueError):
            D.build(forged)
        with self.assertRaises(ValueError):
            P.require_same_json([1.0, 0, 5], [1, 0, 5], "counterfeit polynomial")


if __name__ == "__main__":
    unittest.main()

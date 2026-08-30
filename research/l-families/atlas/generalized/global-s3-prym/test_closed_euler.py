"""Independent closed-place coverage, ramification, and Euler-product controls."""

import copy
import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "closed_s3_euler", HERE / "closed_euler.py"
)
E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E)
P = E.P


class ClosedPlaceTests(unittest.TestCase):
    def test_degree_two_places_match_direct_monic_enumeration(self):
        for p in (5, 7):
            field = P.Field(p, 2)
            actual = {
                tuple(row["minimal_polynomial"]) for row in E.closed_places(field)
            }
            expected = set()
            for a in range(p):
                for b in range(p):
                    # A quadratic is irreducible exactly when it has no root.
                    if all((x * x + a * x + b) % p for x in range(p)):
                        expected.add((b, a, 1))
            self.assertEqual(actual, expected)

    def test_closed_place_count_and_exact_degree(self):
        for p in (5, 7):
            self.assertEqual(E.closed_point_count(p, 1), p)
            self.assertEqual(E.closed_point_count(p, 2), (p * p - p) // 2)
            self.assertEqual(E.closed_point_count(p, 3), (p**3 - p) // 3)
            self.assertEqual(E.closed_point_count(p, 4), (p**4 - p * p) // 4)
            for n in (1, 2, 3, 4):
                field = P.Field(p, n)
                rows = E.closed_places(field)
                self.assertEqual(len(rows), E.closed_point_count(p, n))
                self.assertEqual(
                    len({tuple(r["minimal_polynomial"]) for r in rows}), len(rows)
                )
                for row in rows:
                    self.assertEqual(len(row["minimal_polynomial"]), n + 1)

    def test_residue_field_character_is_not_constant_after_extension(self):
        local_factors = []
        for n in (1, 2):
            field = P.Field(7, n)
            histograms = E.histograms(field, 4, 4)
            local_factors.append(E.local_denominators(field, 4, 4, 3, *histograms))
        self.assertEqual(local_factors[0], ([1, -1], [1, 1]))
        self.assertEqual(local_factors[1], ([1, -1], [1, -1]))

    def test_zero_kummer_factor_and_cyclic_ramification(self):
        for p in (5, 7):
            field = P.Field(p, 1)
            histogram = E.histograms(field, 0, 1)
            self.assertEqual(E.local_denominators(field, 0, 1, 0, *histogram)[1], [1])
            for t in (1, p - 1):
                self.assertEqual(
                    E.local_denominators(field, 0, 1, t, *histogram), ([1], [1])
                )


class EulerProductTests(unittest.TestCase):
    def test_local_degree_substitution_and_inverse_sign(self):
        self.assertEqual(E.reciprocal_factor([1, -1], 1, 4), [1, 1, 1, 1, 1])
        self.assertEqual(E.reciprocal_factor([1, -1], 2, 4), [1, 0, 1, 0, 1])
        self.assertEqual(E.reciprocal_factor([1, 1], 2, 4), [1, 0, -1, 0, 1])
        self.assertEqual(E.reciprocal_factor([1, 1, 1], 1, 4), [1, -1, 0, 1, -1])

    def test_partial_or_malformed_coverage_fails(self):
        rows = [
            {
                "degree": 1,
                "factors": [{"standard": [1, -1], "twisted": [1, 1], "count": 1}],
            }
        ]
        with self.assertRaises(ValueError):
            E.multiply_censuses(rows, 2)
        for degree in (0, 5, True, 1.0):
            with self.assertRaises((TypeError, ValueError)):
                E.reciprocal_factor([1, -1], degree, 4)
        for denominator in ([True, -1], [1.0, -1], [1, -1.0], [0, 1]):
            with self.assertRaises((TypeError, ValueError)):
                E.reciprocal_factor(denominator, 1, 4)

    def test_omitting_or_misgrading_a_closed_factor_changes_product(self):
        field = P.Field(5, 1)
        census = E.field_census(field, 1, 1, E.closed_places(field))
        complete = E.multiply_censuses([census], 1)
        wrong = copy.deepcopy(census)
        for factor in wrong["factors"]:
            if factor["standard"] == [1, -2, 1]:
                factor["standard"] = [1]
                break
        else:
            # Any nonzero standard linear term is an effective omitted factor.
            for factor in wrong["factors"]:
                if len(factor["standard"]) > 1 and factor["standard"][1]:
                    factor["standard"] = [1]
                    break
        self.assertNotEqual(E.multiply_censuses([wrong], 1), complete)
        self.assertNotEqual(
            E.reciprocal_factor([1, -1], 1, 4), E.reciprocal_factor([1, -1], 2, 4)
        )

    def test_numeric_type_forgery_rejected(self):
        with self.assertRaises(ValueError):
            P.require_same_json(
                {"product": [1.0, 0, 5]}, {"product": [1, 0, 5]}, "numeric forgery"
            )


if __name__ == "__main__":
    unittest.main()

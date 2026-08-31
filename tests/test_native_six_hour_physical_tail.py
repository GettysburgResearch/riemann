"""Exact source, tail, matrix and acceptance controls for the fixed minor scout."""

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT / "research/riemann-structures/native-six-hour/native_physical_tail_scout.py"
)
SPEC = importlib.util.spec_from_file_location("native_physical_tail_scout", PATH)
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)
ZERO = (0, 0, 0)


def multiply(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            key = tuple(i + j for i, j in zip(a, b, strict=True))
            result[key] = result.get(key, F()) + x * y
    return {key: value for key, value in result.items() if value}


def derivative(poly, i):
    result = {}
    for key, value in poly.items():
        if key[i]:
            changed = list(key)
            changed[i] -= 1
            result[tuple(changed)] = value * key[i]
    return result


def literal_half(number):
    poly = {ZERO: F(1)}
    for i, degree in enumerate(S.exponents(number)):
        a, b = S.local_source(degree)
        key = tuple(int(j == i) for j in range(3))
        poly = multiply(poly, {ZERO: a, key: b})
    return poly


def direct_curvature(n, m):
    left, right = literal_half(n), literal_half(m)
    result = []
    for i, j, *powers in S.COORDINATES:
        first = multiply(derivative(left, i), derivative(right, j))
        second = multiply(derivative(left, j), derivative(right, i))
        result.append(
            2 * (first.get(tuple(powers), F()) - second.get(tuple(powers), F()))
        )
    return result


def local_unrestricted(k, alpha, beta):
    a, b = S.local_source(k + alpha)
    c, d = S.local_source(k + beta)
    return (a * c, a * d + b * c, b * d, b * c - a * d)


class PhysicalTailControls(unittest.TestCase):
    def test_literal_even_and_odd_source_coefficients(self):
        self.assertEqual(
            [S.coefficient(n) for n in range(5)],
            [F(1), F(-1, 2), F(-1, 8), F(-1, 16), F(-5, 128)],
        )
        self.assertEqual(S.local_source(2), (F(-1, 2), F(3, 8)))
        self.assertEqual(S.local_source(3), (F(), F(-1, 16)))

    def test_original_factor_two_and_reversal(self):
        values = [
            S.local(k, a, b)
            for k, a, b in zip((0, 0, 0), S.exponents(2), S.exponents(3), strict=True)
        ]
        coordinate = (0, 1, 0, 0, 0)
        self.assertEqual(S.source_coordinate(values, coordinate), F(1, 2))
        reverse = [
            S.local(k, b, a)
            for k, a, b in zip((0, 0, 0), S.exponents(2), S.exponents(3), strict=True)
        ]
        self.assertEqual(S.source_coordinate(reverse, coordinate), F(-1, 2))

    def test_actual_shared_prime_alias_coefficient_and_weight(self):
        values = [
            S.local(k, a, b)
            for k, a, b in zip(
                S.exponents(2), S.exponents(2), S.exponents(3), strict=True
            )
        ]
        value = S.source_coordinate(values, (0, 1, 1, 0, 0))
        self.assertEqual(value, F(3, 16))
        self.assertEqual(value / 2, F(3, 32))
        self.assertNotEqual(value, value / 2)

    def test_all36_coordinates_match_independent_polynomial_derivatives(self):
        for a, b in ((2, 3), (4, 5), (3, 4), (1, 6), (8, 15)):
            for g in (1, 2, 3, 5, 6):
                values = [
                    S.local(k, x, y)
                    for k, x, y in zip(
                        S.exponents(g), S.exponents(a), S.exponents(b), strict=True
                    )
                ]
                actual = [S.source_coordinate(values, c) for c in S.COORDINATES]
                self.assertEqual(actual, direct_curvature(g * a, g * b))
                for coordinate, value in zip(S.COORDINATES, actual, strict=True):
                    self.assertLessEqual(
                        abs(value), S.source_coordinate(values, coordinate, True)
                    )

    def test_doubly_differentiated_linear_power_is_exactly_zero(self):
        values = [S.local(2, 1, 0), S.local(3, 0, 1), S.local(1, 0, 0)]
        for power in range(3):
            self.assertEqual(S.source_coordinate(values, (0, 1, 1, 1, power)), 0)
            self.assertEqual(S.source_coordinate(values, (0, 1, 1, 1, power), True), 0)

    def test_local_geometric_remainders_cover_independent_later_terms(self):
        for prime in S.PRIMES:
            for alpha, beta in ((0, 1), (2, 0), (0, 0), (1, 3)):
                for kind in range(4):
                    table = S.local_sum(prime, alpha, beta, kind)
                    later = sum(
                        (
                            abs(local_unrestricted(k, alpha, beta)[kind]) / prime**k
                            for k in range(65, 72)
                        ),
                        F(),
                    )
                    self.assertLessEqual(later, table["remainder"])
                    self.assertEqual(
                        table["upper"], table["partial"] + table["remainder"]
                    )

    def test_identically_zero_determinant_has_zero_infinite_bound(self):
        for prime in S.PRIMES:
            table = S.local_sum(prime, 0, 0, 3)
            self.assertEqual(
                (table["partial"], table["remainder"], table["upper"]), (0, 0, 0)
            )

    def test_same_majorant_prefix_bounds_all_sampled_later_aliases(self):
        alpha, beta, coordinate = S.exponents(2), S.exponents(3), (0, 1, 1, 0, 0)
        tables = {}
        upper = S.total_majorant(alpha, beta, coordinate, tables)
        prefix, later = F(), F()
        for g in S.supported_aliases(100):
            values = [
                S.local(k, x, y)
                for k, x, y in zip(S.exponents(g), alpha, beta, strict=True)
            ]
            if g <= 30:
                prefix += S.source_coordinate(values, coordinate, True) / g
            else:
                later += abs(S.source_coordinate(values, coordinate)) / g
        self.assertGreaterEqual(upper - prefix, later)

    def test_exact_inverse_products_and_strict_contraction(self):
        matrix = [[F(2), F(1)], [F(1), F(1)]]
        inverse = S.inverse_exact(matrix)
        self.assertEqual(inverse["determinant"], 1)
        self.assertEqual(inverse["matrix"], [[1, -1], [-1, 2]])
        result = S.contraction(matrix, [[F(1, 10), F()], [F(), F(1, 10)]])
        self.assertEqual(result["theta"], F(3, 10))
        self.assertEqual(result["status"], "PASS")

    def test_unknown_outcomes_are_not_counterexamples_or_successes(self):
        result = S.contraction([[F(1)]], [[F(1)]])
        self.assertEqual(result["status"], "UNKNOWN_TAIL_NOT_CONTRACTIVE")
        self.assertFalse(result["all_future_horizons_certified"])
        result = S.contraction([[F(1), F(1)], [F(1), F(1)]], [[F(), F()], [F(), F()]])
        self.assertEqual(result["status"], "UNKNOWN_SINGULAR_MINOR")
        self.assertFalse(result["all_future_horizons_certified"])

    def test_inverse_product_verification_cannot_be_bypassed(self):
        with (
            patch.object(S, "matrix_product", return_value=[[F()]]),
            self.assertRaisesRegex(ValueError, "both actual inverse products"),
        ):
            S.inverse_exact([[F(1)]])

    def test_cached_numeric_aliases_and_arithmetic_caps_are_rejected(self):
        S.local(0, 0, 1)
        S.coefficient(1)
        S.local_sum(2, 0, 1, 3)
        for call in (
            lambda: S.local(False, 0, 1),
            lambda: S.local(0, 0.0, 1),
            lambda: S.coefficient(1.0),
            lambda: S.local_sum(2.0, 0, 1, 3),
            lambda: S.coefficient(81),
            lambda: S.exact(1 << 4096),
        ):
            with self.assertRaises(ValueError):
                call()

    def test_duplicate_float_and_numeric_alias_payloads_fail(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}'):
            with self.assertRaises(ValueError):
                S.read_json(raw)
        for bad in ({"rank": True}, {"rank": 1.0}):
            with self.assertRaises(ValueError):
                S.equal(bad, {"rank": 1})

    def test_heldout_gate_precedes_any_source_selection(self):
        with (
            patch.object(
                S, "calibration_gate", side_effect=S.Refusal("no frozen calibration")
            ),
            patch.object(S, "frozen_minor") as source,
        ):
            with self.assertRaisesRegex(ValueError, "no frozen calibration"):
                S.build("heldout", "PENDING")
            source.assert_not_called()

    def test_all_frozen_sources_are_authenticated_before_json_parsing(self):
        with (
            patch.object(S, "git_bytes", side_effect=S.Refusal("changed source")),
            patch.object(S, "read_json") as reader,
        ):
            with self.assertRaisesRegex(ValueError, "changed source"):
                S.frozen_minor()
            reader.assert_not_called()

    def test_sparse_coordinate_counterfeits_fail(self):
        for value in (
            [[0, "1"], [0, "2"]],
            [[False, "1"]],
            [[0.0, "1"]],
            [[0, "1.0"]],
            [[0, "0"]],
        ):
            with self.assertRaises(ValueError):
                S.decode_sparse(value)

    def test_alias_products_cover_every_supported_integer_through1024(self):
        expected = []
        for number in range(1, 1025):
            remainder = number
            for prime in (2, 3, 5):
                while remainder % prime == 0:
                    remainder //= prime
            if remainder == 1:
                expected.append(number)
        self.assertEqual(S.supported_aliases(1024), expected)
        with self.assertRaises(ValueError):
            S.supported_aliases(1025)

    def test_negative_tail_and_wrong_matrix_shapes_are_refusals(self):
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            S.contraction([[F(1)]], [[F(-1)]])
        with self.assertRaises(ValueError):
            S.inverse_exact([[F(1), F(2)]])


if __name__ == "__main__":
    unittest.main()

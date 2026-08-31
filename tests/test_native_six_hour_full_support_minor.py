import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_full_support_minor.py"
)
SPEC = importlib.util.spec_from_file_location("native_fixed_full_support", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FullSupportMinorTests(unittest.TestCase):
    def test_frozen_source_identity(self):
        records = MODULE.authenticate()
        self.assertEqual(len(records), 3)
        self.assertEqual(
            [row["blob"] for row in records], [pin[2] for pin in MODULE.PINS]
        )

    def test_literal_square_root_prefix(self):
        a, c = MODULE.coefficients(8)
        self.assertEqual(
            c[:6],
            [
                Fraction(1),
                Fraction(-1, 2),
                Fraction(-1, 8),
                Fraction(-1, 16),
                Fraction(-5, 128),
                Fraction(-7, 256),
            ],
        )
        self.assertEqual(a, [c[n // 2] if n % 2 == 0 else 0 for n in range(9)])
        for n in range(1, 9):
            self.assertEqual(
                sum(c[k] * c[n - k] for k in range(n + 1)), -1 if n == 1 else 0
            )

    def test_odd_shift_aa_is_zero(self):
        for prime in MODULE.PRIMES:
            matrix = MODULE.local_matrix(prime, cutoff=6)
            self.assertEqual(matrix[0][0], 0)
            self.assertEqual(matrix[2][0], 0)
            self.assertNotEqual(matrix[1][0], 0)

    def test_direct_laurent_orientation(self):
        q, beta, cutoff = Fraction(1, 3), 2, 6
        f = MODULE.coefficients(cutoff + beta)
        for i in range(2):
            for j in range(2):
                positive = sum(
                    q**k * f[i][k] * f[j][k + beta] for k in range(cutoff + 1)
                )
                direct = {}
                for left in range(cutoff + 1):
                    for right in range(cutoff + beta + 1):
                        power = right - left
                        direct[power] = (
                            direct.get(power, Fraction())
                            + q**left * f[i][left] * f[j][right]
                        )
                self.assertEqual(direct[beta], positive)
                negative = sum(
                    q ** (k + beta) * f[j][k + beta] * f[i][k]
                    for k in range(cutoff + 1)
                )
                self.assertEqual(negative, q**beta * positive)
                self.assertNotEqual(q**beta, 1)

    def test_geometric_tail(self):
        for prime in MODULE.PRIMES:
            q = Fraction(1, prime)
            tail = q**65 / (1 - q)
            self.assertEqual(sum(q**k for k in range(65, 81)) + q**81 / (1 - q), tail)
            self.assertGreater(tail, 0)

    def test_both_inverse_identities(self):
        matrix = [[Fraction(0), Fraction(2)], [Fraction(3), Fraction(5)]]
        inv = MODULE.inverse(matrix)
        self.assertEqual(
            inv, [[Fraction(-5, 6), Fraction(1, 3)], [Fraction(1, 2), Fraction(0)]]
        )
        self.assertEqual(MODULE.multiply(matrix, inv), MODULE.identity(2))
        self.assertEqual(MODULE.multiply(inv, matrix), MODULE.identity(2))

    def test_singular_unknown(self):
        record = MODULE.compare_tail(
            [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]], Fraction(0)
        )
        self.assertEqual(record["status"], "UNKNOWN_SINGULAR_PARTIAL")
        self.assertNotIn("infinite_inverse_upper", record)

    def test_noncontractive_unknown(self):
        record = MODULE.compare_tail(MODULE.identity(4), Fraction(1, 4))
        self.assertEqual(record["eta"], 1)
        self.assertEqual(record["status"], "UNKNOWN_TAIL_NOT_CONTRACTIVE")
        self.assertNotIn("infinite_inverse_upper", record)

    def test_certified_inverse_upper(self):
        record = MODULE.compare_tail(MODULE.identity(4), Fraction(1, 16))
        self.assertEqual(record["eta"], Fraction(1, 4))
        self.assertEqual(record["infinite_inverse_upper"], Fraction(4, 3))
        self.assertEqual(record["infinite_inverse_integer_upper"], 2)

    def test_strict_global_threshold(self):
        record = MODULE.threshold(Fraction(3, 7))
        h = record["all_integer_horizons_at_least"]
        square = record["strict_square_bound"]
        self.assertGreater(Fraction(h), square)
        self.assertLessEqual(Fraction(h - 1), square)
        self.assertEqual(record["global_tail_constant"], 235929600)
        self.assertEqual(record["largest_denominator"], 30**4)

    def test_fixed_panel_and_caps(self):
        rows = [
            (a, b, c)
            for a in MODULE.SHIFTS
            for b in MODULE.SHIFTS
            for c in MODULE.SHIFTS
        ]
        denominators = [2**a * 3**b * 5**c for a, b, c in rows]
        self.assertEqual(len(set(denominators)), 64)
        self.assertTrue(all(value % 30 == 0 for value in denominators))
        for bad in (True, 68.0, 81, -1):
            with self.assertRaises(ValueError):
                MODULE.coefficients(bad)
        with self.assertRaises(ValueError):
            MODULE.local_matrix(2, shifts=(2, 3, 4, 5))
        with self.assertRaises(ValueError):
            MODULE.local_matrix(2, shifts=(True, 2, 3, 4))
        with self.assertRaises(ValueError):
            MODULE.inverse(MODULE.identity(5))
        with self.assertRaises(ValueError):
            MODULE.bounded(1 << 4096)

    def test_strict_numeric_counterfeits(self):
        fresh = {"coefficient": [1, 2], "status": "CERTIFIED_LOCAL"}
        MODULE.validate_record(fresh, fresh)
        MODULE.validate_record(MODULE.strict_json(MODULE.canonical(fresh)), fresh)
        for counterfeit in (True, 1.0):
            bad = {"coefficient": [counterfeit, 2], "status": "CERTIFIED_LOCAL"}
            with self.assertRaises(ValueError):
                MODULE.validate_record(bad, fresh)
        with self.assertRaises(ValueError):
            MODULE.canonical({"bad": float("nan")})
        for raw in (
            '{"coefficient":[1,2],"coefficient":[1,2]}',
            '{"coefficient":[1.0,2]}',
            '{"coefficient":[1e0,2]}',
            '{"coefficient":[NaN,2]}',
            '{"coefficient":[Infinity,2]}',
            '{"coefficient":[-Infinity,2]}',
            '{"nested":{"value":1,"value":1}}',
        ):
            with self.assertRaises(ValueError):
                MODULE.strict_json(raw)


if __name__ == "__main__":
    unittest.main()

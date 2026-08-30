"""Independent finite controls and fail-closed checks; standard-library unittest."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "global_s3_prym_producer", HERE / "producer.py"
)
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


def prime_direct_counts(p, A, B):
    """Double loops in the original equations, independent of histograms."""
    e = 1 + sum(
        (y * y - x * x * x - A * x - B) % p == 0 for x in range(p) for y in range(p)
    )
    c = 1 + sum(
        (w**4 - x * x * x - A * x - B) % p == 0 for x in range(p) for w in range(p)
    )
    return e, c


def group_power_counts(field, A, B):
    """Count roots by cyclic multiplicative-group powers, without histograms."""
    e, c = 1, 1
    d4 = gcd(4, field.q - 1)
    for x in range(field.q):
        value = field.cubic(x, A, B)
        if value == 0:
            e += 1
            c += 1
        else:
            e += 2 * (field.power(value, (field.q - 1) // 2) == 1)
            c += d4 * (field.power(value, (field.q - 1) // d4) == 1)
    return e, c


class FieldTests(unittest.TestCase):
    def test_negative_or_inexact_powers_fail_closed(self):
        field = P.Field(5, 1)
        for exponent in (-1, True, 2.0, P.MAX_FIELD + 1):
            with self.assertRaises((TypeError, ValueError)):
                field.power(2, exponent)
            with self.assertRaises((TypeError, ValueError)):
                P.polynomial_power([0, 1], exponent, [2, 0, 1], 5)

    def test_irreducibility_against_exhaustive_small_divisors(self):
        # For degrees <=4, test divisibility by every monic degree 1 or 2
        # polynomial. This does not use the Frobenius/Rabin criterion.
        p = 5
        for n in (2, 3, 4):
            for code in range(45):
                candidate = list(P.digits(code, p, n)) + [1]
                reducible = False
                for d in range(1, n // 2 + 1):
                    for divisor_code in range(p**d):
                        divisor = list(P.digits(divisor_code, p, d)) + [1]
                        if P.remainder(candidate, divisor, p) == [0]:
                            reducible = True
                self.assertEqual(P.irreducible(candidate, p), not reducible)

    def test_field_arithmetic_and_frobenius(self):
        for p in (5, 7):
            for n in (1, 2, 3, 4):
                f = P.Field(p, n)
                for x in range(min(f.q, 80)):
                    self.assertEqual(f.power(x, f.q), x)
                    self.assertEqual(f.add(x, f.scale(x, -1)), 0)
                    if x:
                        self.assertEqual(f.power(x, f.q - 1), 1)
                for a, b, c in ((2, 3, 4), (f.q - 1, 2, 3), (f.q // 2, f.q - 1, 1)):
                    self.assertEqual(
                        f.mul(a, f.add(b, c)), f.add(f.mul(a, b), f.mul(a, c))
                    )
                    self.assertEqual(f.mul(f.mul(a, b), c), f.mul(a, f.mul(b, c)))

    def test_invalid_fields_fail_before_large_allocation(self):
        for p, n in (
            (2, 1),
            (3, 1),
            (9, 1),
            (True, 1),
            (5.0, 1),
            (5, True),
            (5, 5),
            (11, 4),
        ):
            with self.assertRaises((TypeError, ValueError)):
                P.Field(p, n)
        for modulus in ([0, 0, 1], [1, 1], [1, 0, True], (2, 0, 1)):
            with self.assertRaises((TypeError, ValueError)):
                P.Field(5, 2, modulus)

    def test_two_field_models_give_same_curve_counts(self):
        alternatives = []
        for a in range(5):
            for b in range(1, 5):
                poly = [b, a, 1]
                if P.irreducible(poly, 5):
                    alternatives.append(poly)
        left = P.count_source(P.Field(5, 2, alternatives[0]), 1, 1)
        right = P.count_source(P.Field(5, 2, alternatives[-1]), 1, 1)
        for key in (
            "elliptic_points",
            "quartic_cover_points",
            "W_local_sum",
            "W_twist_local_sum",
            "affine_fibre_types",
        ):
            self.assertEqual(left[key], right[key])


class SourceTests(unittest.TestCase):
    def test_prime_counts_from_original_equations(self):
        for p in (5, 7, 11, 13):
            for A, B in ((-1, 0), (1, 1), (0, 1)):
                data = P.count_source(P.Field(p, 1), A, B)
                self.assertEqual(
                    (data["elliptic_points"], data["quartic_cover_points"]),
                    prime_direct_counts(p, A, B),
                )

    def test_extension_counts_from_multiplicative_group(self):
        for p, n in ((5, 2), (5, 3), (7, 2)):
            field = P.Field(p, n)
            for A, B in ((-1, 0), (1, 1), (0, 1)):
                data = P.count_source(field, A, B)
                self.assertEqual(
                    (data["elliptic_points"], data["quartic_cover_points"]),
                    group_power_counts(field, A, B),
                )

    def test_singular_curves_and_inexact_parameters_rejected(self):
        field = P.Field(5, 1)
        for A, B in ((0, 0), (2, 2), (True, 1), (1, 1.0)):
            with self.assertRaises((TypeError, ValueError)):
                P.count_source(field, A, B)

    def test_ramified_stalk_and_character_normalizations(self):
        saw_negative_branch = False
        saw_positive_branch = False
        for p, n in ((5, 1), (5, 2), (7, 1), (7, 2)):
            field = P.Field(p, n)
            # The extra p7 case has prescribed t=3, double root r=1,
            # A=-3r^2=4, B=t^2+2r^3=4; chi_7(3)=-1.
            for A, B in ((-1, 0), (1, 1), (4, 4)):
                data = P.count_source(field, A, B)
                for row in data["old_branch_factors"]:
                    t = row["t"]
                    self.assertNotEqual(t, 0)
                    self.assertEqual(row["W_frobenius"], 1)
                    self.assertEqual(row["invariant_dimension"], 1)
                    sign = 1 if field.power(t, (field.q - 1) // 2) == 1 else -1
                    self.assertEqual(row["twist_frobenius"], sign)
                    saw_negative_branch |= sign == -1
                    saw_positive_branch |= sign == 1
                self.assertEqual(data["twist_zero_invariants"], 0)
                self.assertEqual(data["infinity"]["W_invariants"], 0)
        self.assertTrue(saw_negative_branch)
        self.assertTrue(saw_positive_branch)

    def test_cyclic_geometric_stalk_is_not_transposition_stalk(self):
        for p in (5, 7):
            data = P.count_source(P.Field(p, 1), 0, 1)
            self.assertEqual(data["affine_fibre_types"]["ramified_transposition"], 0)
            self.assertEqual(len(data["old_branch_factors"]), 2)
            for row in data["old_branch_factors"]:
                self.assertEqual(row["invariant_dimension"], 0)
                self.assertEqual(row["W_frobenius"], 0)

    def test_source_identity_and_coverage_are_frozen(self):
        source = json.loads((HERE / "source.json").read_text(encoding="utf-8"))
        self.assertEqual(P.digest(source), P.EXPECTED_SOURCE_HASH)
        P.validate_source(source)
        for key, value in (
            ("p", True),
            ("A", 1.0),
            ("extensions", [1, 2]),
            ("extensions", [True, 2, 3, 4]),
            ("p", 11),
        ):
            modified = copy.deepcopy(source)
            modified["panels"][0][key] = value
            with self.assertRaises((TypeError, ValueError)):
                P.validate_source(modified)
        modified = copy.deepcopy(source)
        modified["panels"].append(copy.deepcopy(modified["panels"][0]))
        with self.assertRaises(ValueError):
            P.validate_source(modified)


class CohomologyControls(unittest.TestCase):
    def test_forged_json_numeric_types_do_not_compare_equal(self):
        expected = {"coefficients": [1, 0, 5]}
        for forged_one in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                P.require_same_json(
                    {"coefficients": [forged_one, 0, 5]}, expected, "forged artifact"
                )
        P.require_same_json(expected, expected, "exact artifact")

    def test_newton_sign_and_held_out_recurrence(self):
        # Eigenvalues 1 and 2: det(1-TF)=1-3T+2T^2.
        local_sums = [-3, -5, -9, -17]
        self.assertEqual(P.newton_from_local_sums(local_sums), [1, -3, 2, 0, 0])
        self.assertEqual(P.local_sums_from_polynomial([1, -3, 2], 4), local_sums)
        with self.assertRaises(ArithmeticError):
            P.newton_from_local_sums([0, 1])

    def test_exact_quartic_weight_criterion_has_negative_controls(self):
        # Product of reciprocal quadratics with integral real traces.
        for q in (5, 7):
            for a in range(-7, 8):
                for b in range(-7, 8):
                    polynomial = [1, -(a + b), a * b + 2 * q, -q * (a + b), q * q]
                    self.assertEqual(
                        P.quartic_weil(polynomial, q), a * a <= 4 * q and b * b <= 4 * q
                    )
        self.assertFalse(P.quartic_weil([1, 0, 30, 0, 25], 5))
        self.assertFalse(P.quartic_weil([1, 0, 0, 1, 25], 5))

    def test_ramified_projector_uses_weighted_trace(self):
        # Inertia fixes (a,a,b). Generic trace is 2a+b, not a+b.
        p = [[Fraction(i == j) - Fraction(1, 3) for j in range(3)] for i in range(3)]
        vector = [Fraction(2), Fraction(2), Fraction(5)]
        projected = [sum(p[i][j] * vector[j] for j in range(3)) for i in range(3)]
        self.assertEqual(projected, [Fraction(-1), Fraction(-1), Fraction(2)])
        self.assertEqual(sum(projected), 0)
        self.assertNotEqual(
            2 * projected[0] + projected[2], projected[0] + projected[2]
        )

    def test_commutator_falsifier_preserves_augmentation(self):
        result = P.projector_control()
        self.assertTrue(result["S3_H_equals_three_halves_P"])
        self.assertTrue(result["C3_commutator_H_zero"])
        self.assertTrue(result["C3_augmentation_P_nonzero"])


if __name__ == "__main__":
    unittest.main()

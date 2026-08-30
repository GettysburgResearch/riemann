"""Hostile source, character, ramification and paired-duality controls."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "kummer_tower_replay", HERE / "kummer_replay.py"
)
K = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K)
P = K.P


class CyclotomicTests(unittest.TestCase):
    def test_integral_basis_roots_conjugation_and_norm(self):
        for m in (3, 4, 6):
            ring = K.Cyclotomic(m)
            self.assertEqual(ring.power((0, 1), m), K.ONE)
            self.assertEqual(len(set(ring.roots)), m)
            self.assertEqual(ring.sum(ring.roots), K.ZERO)
            for a in range(-3, 4):
                for b in range(-3, 4):
                    value = (a, b)
                    self.assertEqual(
                        ring.mul(value, ring.conjugate(value)),
                        (a * a + ring.s * a * b + b * b, 0),
                    )
                    self.assertEqual(ring.conjugate(ring.conjugate(value)), value)

    def test_invalid_rings_powers_and_nonintegral_newton(self):
        for m in (2, 5, True, 3.0):
            with self.assertRaises((TypeError, ValueError)):
                K.Cyclotomic(m)
        ring = K.Cyclotomic(3)
        for n in (-1, True, 2.0, P.MAX_FIELD + 1):
            with self.assertRaises((TypeError, ValueError)):
                ring.power((0, 1), n)
        with self.assertRaises(ArithmeticError):
            ring.divide_integer((1, 0), 2)

    def test_newton_from_independent_eigenvalue_powers(self):
        for m in (3, 4, 6):
            ring = K.Cyclotomic(m)
            eigenvalues = [(1, 1), (2, -1)]
            sums = [
                ring.scale(ring.sum(ring.power(a, n) for a in eigenvalues), -1)
                for n in range(1, 5)
            ]
            expected = K.polynomial_product(
                ring,
                [K.ONE, ring.scale(eigenvalues[0], -1)],
                [K.ONE, ring.scale(eigenvalues[1], -1)],
            )
            self.assertEqual(K.newton(ring, sums), expected + [K.ZERO, K.ZERO])
            self.assertEqual(K.local_sums(ring, expected, 4), sums)


class CharacterTests(unittest.TestCase):
    def test_character_orthogonality_matches_power_fibres(self):
        for p, m in ((5, 4), (7, 3), (7, 6)):
            ring = K.Cyclotomic(m)
            for n in (1, 2):
                field = P.Field(p, n)
                exponents = K.character_exponents(field, m)
                hist = [0] * field.q
                for w in range(field.q):
                    hist[field.power(w, m)] += 1
                for t in range(1, field.q):
                    self.assertEqual(
                        ring.sum(ring.roots[j * exponents[t] % m] for j in range(m)),
                        (hist[t], 0),
                    )

    def test_norm_restriction_and_multiplicativity(self):
        for p, m in ((5, 4), (7, 3), (7, 6)):
            base = K.character_exponents(P.Field(p, 1), m)
            for n in (2, 3, 4):
                field = P.Field(p, n)
                extension = K.character_exponents(field, m)
                for t in range(1, p):
                    self.assertEqual(extension[t], n * base[t] % m)
                for a in range(1, min(field.q, 12)):
                    for b in range(1, min(field.q, 12)):
                        self.assertEqual(
                            extension[field.mul(a, b)],
                            (extension[a] + extension[b]) % m,
                        )

    def test_missing_roots_of_unity_refused(self):
        with self.assertRaises(ValueError):
            K.character_exponents(P.Field(5, 1), 3)
        with self.assertRaises(ValueError):
            K.character_exponents(P.Field(7, 1), 4)


class GeometryTests(unittest.TestCase):
    def test_direct_prime_field_tower_equations(self):
        for p, m in ((5, 4), (7, 3), (7, 6)):
            ring = K.Cyclotomic(m)
            for A, B in ((1, 1), (-1, 0)):
                result = K.count_tower(P.Field(p, 1), ring, A, B)
                infinity = 3 if m % 3 == 0 else 1
                direct = infinity + sum(
                    (w ** (2 * m) - x**3 - A * x - B) % p == 0
                    for w in range(p)
                    for x in range(p)
                )
                self.assertEqual(result["tower_points"], direct)

    def test_order_three_infinity_is_a_missing_linear_factor(self):
        ring = K.Cyclotomic(3)
        counts = [K.count_tower(P.Field(7, n), ring, 1, 1) for n in (1, 2, 3, 4)]
        for j in (1, 2):
            complete = [tuple(c["complete_character_sums"][j]) for c in counts]
            affine = [tuple(c["affine_character_sums"][j]) for c in counts]
            for left, right in zip(complete, affine):
                self.assertEqual(ring.add(right, K.ONE), left)
            true_polynomial = K.newton(ring, complete[:3])
            self.assertEqual(K.local_sums(ring, true_polynomial, 4), complete)
            wrong_polynomial = K.newton(ring, affine)
            self.assertEqual(
                wrong_polynomial,
                K.polynomial_product(ring, true_polynomial, [K.ONE, (-1, 0)]),
            )
            self.assertNotEqual(wrong_polynomial[-1], K.ZERO)

    def test_nonreal_odd_degree_factors_are_paired_not_self_reciprocal(self):
        ring = K.Cyclotomic(3)
        counts = [K.count_tower(P.Field(7, n), ring, 1, 1) for n in (1, 2, 3)]
        factors = [
            K.newton(ring, [tuple(c["complete_character_sums"][j]) for c in counts])
            for j in (1, 2)
        ]
        self.assertTrue(K.paired_reciprocity(ring, factors[0], factors[1], 7))
        self.assertFalse(K.paired_reciprocity(ring, factors[0], factors[0], 7))
        self.assertEqual(ring.mul(factors[0][-1], factors[1][-1]), (7**3, 0))
        self.assertEqual([ring.conjugate(c) for c in factors[0]], factors[1])

    def test_resonance_dimension_list_and_genus(self):
        from math import gcd

        for m, expected in ((3, [2, 3, 3]), (4, [2, 4, 4, 4]), (6, [2, 4, 3, 4, 3, 4])):
            dimensions = [2] + [4 - int(m // gcd(m, j) == 3) for j in range(1, m)]
            self.assertEqual(dimensions, expected)
            self.assertEqual(sum(dimensions), 4 * m - 1 - gcd(m, 3))

    def test_wrong_curve_stratum_refused(self):
        for A, B in ((0, 1), (0, 0), (2, 2)):
            with self.assertRaises(ValueError):
                K.count_tower(P.Field(5, 1), K.Cyclotomic(4), A, B)

    def test_frozen_source_and_numeric_type_forgery(self):
        source = json.loads((HERE / "kummer_source.json").read_text(encoding="utf-8"))
        K.validate_source(source)
        for key, value in (("p", True), ("A", 1.0), ("m", 5)):
            forged = copy.deepcopy(source)
            forged["panels"][0][key] = value
            with self.assertRaises(ValueError):
                K.validate_source(forged)
        with self.assertRaises(ValueError):
            P.require_same_json(
                {"coefficient": [True, 0]},
                {"coefficient": [1, 0]},
                "forged cyclotomic coefficient",
            )


if __name__ == "__main__":
    unittest.main()

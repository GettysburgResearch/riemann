"""Independent polynomial, point-count, ramification and source controls."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "s3_closure_replay", HERE / "closure_replay.py"
)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
P = C.P


def poly_add(*terms):
    result = {}
    for term in terms:
        for powers, value in term.items():
            result[powers] = result.get(powers, 0) + value
    return {powers: value for powers, value in result.items() if value}


def poly_scale(poly, scalar):
    return {powers: scalar * value for powers, value in poly.items() if scalar * value}


def poly_mul(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            key = tuple(i + j for i, j in zip(a, b))
            result[key] = result.get(key, 0) + x * y
    return {powers: value for powers, value in result.items() if value}


def poly_power(poly, exponent):
    result = {(0, 0, 0): 1}
    for _ in range(exponent):
        result = poly_mul(result, poly)
    return result


class IntegralPolynomialTests(unittest.TestCase):
    def setUp(self):
        self.x, self.A, self.B = ({(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1})
        self.f = poly_add(poly_power(self.x, 3), poly_mul(self.A, self.x), self.B)
        self.g = poly_add(poly_scale(poly_power(self.x, 2), -3), poly_scale(self.A, -4))

    def test_vandermonde_and_second_map_identity_over_Z_A_B_x(self):
        derivative = poly_add(poly_scale(poly_power(self.x, 2), 3), self.A)
        left = poly_mul(self.g, poly_power(derivative, 2))
        right = poly_add(
            poly_scale(poly_power(self.A, 3), -4),
            poly_scale(poly_power(poly_add(self.B, poly_scale(self.f, -1)), 2), -27),
        )
        self.assertEqual(left, right)
        self.assertEqual(poly_mul(self.f, left), poly_mul(self.f, right))

    def test_first_map_identity_over_Z_A_B_x(self):
        numerator = poly_add(poly_power(self.x, 3), poly_scale(self.B, 4))
        correction = poly_add(
            poly_power(self.x, 3),
            poly_scale(poly_mul(self.A, self.x), 4),
            poly_scale(self.B, -8),
        )
        left = poly_mul(self.f, poly_power(correction, 2))
        right = poly_add(
            poly_power(numerator, 3),
            poly_mul(poly_mul(self.A, numerator), poly_power(self.g, 2)),
            poly_mul(self.B, poly_power(self.g, 3)),
        )
        self.assertEqual(left, right)
        wrong = poly_add(
            poly_power(self.x, 3),
            poly_scale(poly_mul(self.A, self.x), 4),
            poly_scale(self.B, -7),
        )
        self.assertNotEqual(poly_mul(self.f, poly_power(wrong, 2)), right)


class CompletePrimeFieldTests(unittest.TestCase):
    def test_direct_equation_counts_independent_of_square_histograms(self):
        for p, A, B in ((5, 1, 1), (5, -1, 0), (7, 1, 1), (7, -1, 0), (7, 4, 4)):
            with self.subTest(p=p, A=A, B=B):
                row = C.count_source(P.Field(p, 1), A, B)
                f = lambda x, A=A, B=B, p=p: (x**3 + A * x + B) % p
                g = lambda x, A=A, p=p: (-3 * x * x - 4 * A) % p
                d = lambda U, A=A, B=B, p=p: (-4 * A**3 - 27 * (B - U) ** 2) % p
                direct = {name: 0 for name in row["counts"]}
                for x in range(p):
                    for y in range(p):
                        direct["E"] += int(y * y % p == f(x))
                        direct["H"] += int(y * y % p == f(x) * g(x) % p)
                        direct["D"] += int(y * y % p == d(x * x))
                        direct["D2"] += int(y * y % p == x * d(x) % p)
                        direct["conic"] += int(y * y % p == g(x))
                        for v in range(p):
                            direct["Z"] += int(y * y % p == f(x) and v * v % p == g(x))
                for name, count in direct.items():
                    self.assertEqual(row["counts"][name], count + row["infinity"][name])

    def test_normalized_double_root_fibre_has_three_points(self):
        f = P.Field(7, 1)
        roots = C.square_roots(f)
        xs = [x for x in range(7) if f.cubic(x, 4, 4) == 2]
        self.assertEqual(xs, [1, 5])
        self.assertEqual([len(roots[C.g_value(f, x, 4)]) for x in xs], [2, 1])
        self.assertEqual(sum(len(roots[C.g_value(f, x, 4)]) for x in xs), 3)
        self.assertNotEqual(3, 6)

    def test_maps_have_projective_points_over_denominator_zero(self):
        f = P.Field(7, 1)
        row = C.count_source(f, 1, 1)
        self.assertEqual([x for x in range(7) if C.g_value(f, x, 1) == 0], [1, 6])
        self.assertEqual(row["first_map_affine_points_to_infinity"], 2)
        self.assertIsNone(C.elliptic_map(f, 1, 0, 1, 1))
        with self.assertRaises(ValueError):
            C.elliptic_map(f, 1, 1, 1, 1)


class ArithmeticExtensionTests(unittest.TestCase):
    def test_infinity_switches_under_constant_extension(self):
        for p, n, expected in ((5, 1, 0), (5, 2, 2), (7, 1, 2)):
            row = C.count_source(P.Field(p, n), 1, 1)
            self.assertEqual(row["infinity"]["Z"], expected)
            self.assertEqual(row["infinity"]["D"], expected)
            self.assertEqual(row["infinity"]["conic"], expected)
            self.assertEqual(row["infinity"]["E"], 1)
            self.assertEqual(row["infinity"]["H"], 1)
            self.assertEqual(row["infinity"]["D2"], 1)

    def test_complete_extension_coverage_and_two_factorizations(self):
        for p, n, A, B in ((5, 2, 1, 1), (7, 2, 4, 4), (5, 3, -1, 0)):
            row = C.count_source(P.Field(p, n), A, B)
            Q, counts = row["field_order"], row["counts"]
            self.assertEqual(row["complete_finite_fibre_count"], Q)
            self.assertEqual(row["affine_H_map_points_checked"], counts["H"] - 1)
            self.assertEqual(
                row["affine_deck_points_checked"], counts["Z"] - row["infinity"]["Z"]
            )
            self.assertEqual(counts["H"], counts["E"] + counts["D2"] - Q - 1)
            self.assertEqual(counts["D"], counts["D2"])

    def test_degree_two_quotient_has_no_geometric_fixed_point_control(self):
        f = P.Field(5, 2)
        roots = C.square_roots(f)
        for u in range(f.q):
            for s in roots[C.discriminant_value(f, f.mul(u, u), 1, 1)]:
                self.assertNotEqual((u, s), (f.scale(u, -1), f.scale(s, -1)))
        # At infinity the two leading ratios are exchanged by s -> -s.
        infinity = roots[(-27) % 5]
        self.assertEqual(len(infinity), 2)
        self.assertEqual({f.scale(s, -1) for s in infinity}, set(infinity))
        self.assertTrue(all(f.scale(s, -1) != s for s in infinity))

    def test_deck_relations_hold_without_cube_roots_in_base_field(self):
        f = P.Field(5, 1)
        self.assertEqual([x for x in range(5) if x**3 % 5 == 1], [1])
        row = C.count_source(f, 1, 1)
        self.assertGreater(row["affine_deck_points_checked"], 0)
        self.assertEqual(row["affine_deck_points_checked"] % 3, 0)


class ProvenanceAndBoundaryTests(unittest.TestCase):
    def test_singular_and_cyclic_specializations_are_rejected(self):
        field = P.Field(5, 1)
        for A, B in ((0, 1), (5, 1), (2, 2), (True, 1), (1, 1.0)):
            with self.assertRaises((ValueError, TypeError)):
                C.count_source(field, A, B)
        # The A=0 quintic actually has a repeated x factor; it is not genus two.
        f0 = [1, 0, 0, 1]
        g0 = [0, 0, 2]
        product = P.polynomial_product(f0, g0, 5)
        derivative = [(i * product[i]) % 5 for i in range(1, len(product))]
        self.assertNotEqual(P.polynomial_gcd(product, P.trim(derivative), 5), [1])

    def test_unchanged_resource_cap_and_incomplete_coverage(self):
        with self.assertRaises(ValueError):
            P.Field(7, 5)
        with self.assertRaises(ValueError):
            P.Field(11, 4)
        with self.assertRaises(ValueError):
            C.count_source(P.Field(5, 1), 1, 1, [[] for _ in range(5)])

    def test_primitive_source_and_types_cannot_be_self_forged(self):
        source = json.loads((HERE / "closure_source.json").read_text(encoding="utf-8"))
        self.assertEqual(P.digest(source), C.EXPECTED_SOURCE_HASH)
        for key, value in (("maximum_field_order", 2401.0), ("extensions", [1, 2])):
            altered = copy.deepcopy(source)
            altered[key] = value
            with self.assertRaises(ValueError):
                C.build(altered)
        with self.assertRaises(ValueError):
            P.require_same_json(
                {"count": True}, {"count": 1}, "wrong primitive integer"
            )


if __name__ == "__main__":
    unittest.main()

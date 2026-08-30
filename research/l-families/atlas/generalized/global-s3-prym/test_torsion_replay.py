"""Independent controls for source divisor pullbacks and the torsion graph."""

import copy
import importlib.util
import itertools
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "source_torsion_replay", HERE / "torsion_replay.py"
)
T = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(T)
P = T.P


def small_census(J):
    points = [J.zero]
    q = J.field.q
    if q != 5:
        raise ValueError("only the declared F5 full census is allowed")
    for degree in (1, 2):
        for coefficients in itertools.product(range(q), repeat=degree):
            u = coefficients + (1,)
            for v in itertools.product(range(q), repeat=degree):
                if J.r.mod(J.r.sub(J.h, J.r.mul(v, v)), u) == (0,):
                    points.append(J.reduced(u, v))
    return points


class PolynomialControls(unittest.TestCase):
    def setUp(self):
        self.r = T.Polynomials(P.Field(5, 2))

    def test_bezout_identity_with_shared_and_coprime_factors(self):
        r = self.r
        for a, b in (
            ((1, 2, 1), (1, 1)),
            ((1, 0, 1), (2, 1)),
            ((0, 0, 1), (0, 1)),
            ((1,), (0,)),
        ):
            d, s, t = r.xgcd(a, b)
            self.assertEqual(r.add(r.mul(s, a), r.mul(t, b)), d)
            self.assertEqual(r.mod(a, d), (0,))
            self.assertEqual(r.mod(b, d), (0,))

    def test_inverse_in_quotient_and_failed_denominator(self):
        r = self.r
        inverse = r.inverse_mod((0, 1), (1, 0, 1))
        self.assertEqual(r.mod(r.mul((0, 1), inverse), (1, 0, 1)), (1,))
        with self.assertRaises(ValueError):
            r.inverse_mod((0, 1), (0, 0, 1))
        with self.assertRaises(ArithmeticError):
            r.exact((1,), (0, 1))

    def test_degree_caps_and_warm_cache_type_checks(self):
        r = self.r
        r.inv(1)
        with self.assertRaises(TypeError):
            r.inv(True)
        with self.assertRaises((TypeError, ValueError)):
            r.checked((1.0,))
        with self.assertRaises(ValueError):
            r.checked((1,) * 14)
        with self.assertRaises(ValueError):
            r.mul((1,) * 8, (1,) * 8)
        with self.assertRaises(ValueError):
            r.inv(0)


class JacobianControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.J = T.Jacobian(P.Field(5, 1), 1, 1)
        cls.points = small_census(cls.J)

    def test_complete_F5_reduced_census_matches_frozen_curve_cardinality(self):
        artifact = json.loads(
            (HERE / "closure_artifact.json").read_text(encoding="utf-8")
        )
        curve = next(p for p in artifact["panels"] if p["source"]["id"] == "p5-generic")
        self.assertEqual(len(self.points), 54)
        self.assertEqual(len(set(self.points)), 54)
        self.assertEqual(len(self.points), sum(curve["polynomials"]["H"]))

    def test_complete_small_census_inverse_commutativity_and_closure(self):
        J, points = self.J, self.points
        allowed = set(points)
        for left in points:
            self.assertEqual(J.add(left, J.zero), left)
            self.assertEqual(J.add(left, J.neg(left)), J.zero)
            for right in points:
                total = J.add(left, right)
                self.assertIn(total, allowed)
                self.assertEqual(total, J.add(right, left))

    def test_associativity_against_three_geometric_point_classes(self):
        J = self.J
        generators = [
            J.reduced((0, 1), (1,)),
            J.reduced((0, 1), (4,)),
            J.reduced(J.g, (0,)),
        ]
        for a, b, c in itertools.product(
            self.points[::6], self.points[1::6], generators
        ):
            self.assertEqual(J.add(J.add(a, b), c), J.add(a, J.add(b, c)))

    def test_independent_tangent_doubling_at_x_zero(self):
        # h(0)=1,h'(0)=1, so the curve tangent is w=1+3x over F5.
        D = self.J.reduced((0, 1), (1,))
        self.assertEqual(self.J.add(D, D), ((0, 0, 1), (1, 3)))

    def test_invalid_divisor_and_scalar_caps(self):
        J = self.J
        with self.assertRaises(ValueError):
            J.reduced((0, 1), (0,))
        with self.assertRaises(ValueError):
            J.validate(((0, 2), (1,)))
        with self.assertRaises((TypeError, ValueError)):
            J.multiple(J.zero, True)
        with self.assertRaises(ValueError):
            J.multiple(J.zero, 28)


class EllipticAndMapControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.field = P.Field(5, 2)
        cls.E = T.Elliptic(cls.field, 1, 1)
        cls.D2 = T.second_short_model(cls.field, 1, 1)
        cls.J = T.Jacobian(cls.field, 1, 1)
        cls.points = cls.E.three_torsion()

    def test_division_polynomial_matches_all_primitive_curve_points(self):
        E, field = self.E, self.field
        roots = T.C.square_roots(field)
        direct = [None]
        for x in range(field.q):
            for y in roots[field.cubic(x, 1, 1)]:
                point = (x, y)
                if E.add(E.add(point, point), point) is None:
                    direct.append(point)
        self.assertEqual(set(direct), set(self.points))
        with self.assertRaises(ValueError):
            T.Elliptic(P.Field(5, 1), 1, 1).three_torsion()

    def test_short_second_model_is_exact_coordinate_change(self):
        f, D2 = self.field, self.D2
        roots = T.C.square_roots(f)
        for x in range(f.q):
            for y in roots[f.cubic(x, D2.a, D2.b)]:
                U, S = T.second_affine_coordinates(f, (x, y), 1)
                self.assertEqual(
                    f.mul(S, S), f.mul(U, T.C.discriminant_value(f, U, 1, 1))
                )

    def test_first_pullback_needs_the_nonzero_origin_correction(self):
        J = self.J
        correction = J.reduced(J.g, (0,))
        self.assertNotEqual(correction, J.zero)
        self.assertEqual(J.multiple(correction, 2), J.zero)
        image = J.first_pullback(self.points[1])
        raw_fibre = J.add(image, correction)
        self.assertEqual(J.multiple(image, 3), J.zero)
        self.assertEqual(J.multiple(raw_fibre, 3), correction)

    def test_pullback_helpers_reject_off_curve_and_coercible_points(self):
        for point in ((0, 0), (True, 1), (0, 1.0), [1]):
            with self.assertRaises((ValueError, TypeError)):
                self.J.first_pullback(point)
        for point in ((1, 0), (True, 1), (1, 1.0), [1]):
            with self.assertRaises((ValueError, TypeError)):
                self.J.second_pullback(point)
        with self.assertRaises(TypeError):
            T.Elliptic(self.field, True, 1)

    def test_complete_Weil_bilinearity_and_nontrivial_cube_root(self):
        E, f, points = self.E, self.field, self.points
        values = [[E.weil3(a, b) for b in points] for a in points]
        self.assertEqual({value for row in values for value in row}, {1, 7, 22})
        for i, j, k in itertools.product(range(9), repeat=3):
            index = points.index(E.add(points[i], points[j]))
            self.assertEqual(values[index][k], f.mul(values[i][k], values[j][k]))
        first = next(value for row in values for value in row if value != 1)
        self.assertNotEqual(f.power(f.scale(first, -1), 3), 1)

    def test_source_kernel_extraction_is_not_coordinate_index_matching(self):
        row = T.panel({"id": "test", "p": 5, "degree": 2, "A": 1, "B": 1})
        self.assertEqual(len(row["kernel_index_pairs"]), 9)
        self.assertNotEqual(row["kernel_index_pairs"], [(i, i) for i in range(9)])
        self.assertEqual(
            self.field.mul(row["basis_Weil_pairing"], row["image_basis_Weil_pairing"]),
            1,
        )


class SourceControls(unittest.TestCase):
    def test_primitive_forgery_and_geometry_refusal(self):
        source = json.loads((HERE / "torsion_source.json").read_text(encoding="utf-8"))
        self.assertEqual(T.P.digest(source), T.EXPECTED_SOURCE_HASH)
        bad = copy.deepcopy(source)
        bad["curves"][0]["degree"] = 2.0
        with self.assertRaises(ValueError):
            T.build(bad)
        with self.assertRaises(ValueError):
            T.Jacobian(P.Field(5, 1), 0, 1)
        with self.assertRaises(ValueError):
            T.Elliptic(P.Field(5, 1), 0, 0)
        with self.assertRaises(ValueError):
            T.P.require_same_json([1.0], [1], "typed torsion fixture")


if __name__ == "__main__":
    unittest.main()

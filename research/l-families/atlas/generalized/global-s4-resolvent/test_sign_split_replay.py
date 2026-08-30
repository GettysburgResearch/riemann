"""Independent small group, source map and complete two-torsion controls."""

import copy
import importlib.util
import itertools
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "s4_sign_split_tested", HERE / "sign_split_replay.py"
)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def elliptic_points(E):
    q = E.field.q
    if q != 5:
        raise ValueError("complete elementary group census is capped at F5")
    return [None] + [
        (x, y)
        for x, y in itertools.product(range(q), repeat=2)
        if y * y % q == E.rhs(x)
    ]


class GroupControls(unittest.TestCase):
    def test_complete_f5_group_closure_and_associativity(self):
        plus, minus, _ = R.elliptic_sources(R.P.Field(5, 1), 1, 1)
        for E in (plus, minus):
            points = elliptic_points(E)
            for left, right in itertools.product(points, repeat=2):
                self.assertIn(E.add(left, right), points)
                self.assertEqual(E.add(left, right), E.add(right, left))
            for a, b, c in itertools.product(points, repeat=3):
                self.assertEqual(E.add(E.add(a, b), c), E.add(a, E.add(b, c)))

    def test_identity_inverse_and_nonsplit_origin(self):
        plus, minus, _ = R.elliptic_sources(R.P.Field(5, 1), 1, 1)
        for E in (plus, minus):
            for point in elliptic_points(E):
                self.assertEqual(E.add(point, None), point)
                inverse = None if point is None else (point[0], (-point[1]) % 5)
                self.assertIsNone(E.add(point, inverse))
        # The second target's chosen (quartic) origin is Weierstrass infinity.
        row = R.count_maps(R.P.Field(7, 1), 1, 1)
        self.assertEqual(row["minus_origin_hits"], 0)
        self.assertEqual(row["infinity_images"], [])

    def test_reject_singular_coefficients_and_off_curve_points(self):
        field = R.P.Field(5, 1)
        with self.assertRaises(ValueError):
            R.Elliptic(field, 0, 0, 0)
        with self.assertRaises(TypeError):
            R.Elliptic(field, False, 0, 1)
        E = R.elliptic_sources(field, 1, 1)[0]
        for point in ((True, 1), (1.0, 0), [1, 0], (0, 0)):
            with self.assertRaises((TypeError, ValueError)):
                E.add(point, None)


class MapControls(unittest.TestCase):
    def test_both_weierstrass_transformations_by_direct_prime_field_algebra(self):
        for p, b, c in ((5, 1, 1), (7, 1, 1), (7, 3, 4)):
            delta = 256 * c**3 - 27 * b**4
            for r, s in itertools.product(range(p), repeat=2):
                h = 256 * (c - r) ** 3 - 27 * b**4
                if (s * s - h) % p == 0:
                    X, Y = 16 * (c - r), 4 * s
                    self.assertEqual((Y * Y - X**3 + 432 * b**4) % p, 0)
                if r and (s * s - r * h) % p == 0:
                    X, Y = delta * pow(r, -1, p), delta * s * pow(r, -2, p)
                    self.assertEqual(
                        (
                            Y * Y
                            - X**3
                            + 768 * c * c * X * X
                            - 768 * c * delta * X
                            + 256 * delta * delta
                        )
                        % p,
                        0,
                    )

    def test_affine_source_maps_and_origin_divisor(self):
        field = R.P.Field(5, 1)
        hits = []
        for u, s in itertools.product(range(5), repeat=2):
            if (s * s - (256 * (1 - u * u) ** 3 - 27)) % 5 == 0:
                first, second = R.quotient_maps(field, 1, 1, (u, s))
                if u == 0:
                    self.assertIsNone(second)
                    self.assertEqual(first, (1, (4 * s) % 5))
                    hits.append(s)
                else:
                    self.assertIsNotNone(second)
        self.assertEqual(hits, [2, 3])

    def test_projective_infinity_maps_counted_once(self):
        row = R.count_maps(R.P.Field(5, 1), 1, 1)
        self.assertEqual(len(row["infinity_images"]), 2)
        self.assertEqual(row["affine_map_checks"] + 2, row["counts"]["D"])
        for image in row["infinity_images"]:
            self.assertIsNone(image["plus"])
            self.assertEqual(image["minus"][0], 0)

    def test_source_map_rejects_coercible_and_off_curve_input(self):
        field = R.P.Field(5, 1)
        for point in ((0, 0), (False, 2), (0, 2.0), [0, 2]):
            with self.assertRaises((TypeError, ValueError)):
                R.quotient_maps(field, 1, 1, point)

    def test_cube_bijection_forces_trace_only_in_stated_residue_class(self):
        for n in (1, 3):
            row = R.count_maps(R.P.Field(5, n), 1, 1)
            self.assertEqual(row["counts"]["plus"], 5**n + 1)
        row = R.count_maps(R.P.Field(7, 1), 1, 1)
        self.assertNotEqual(row["counts"]["plus"], 8)


class TorsionControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graphs = [
            R.torsion_graph(R.P.Field(p, n), b, c)
            for p, n, b, c in ((5, 2, 1, 1), (7, 3, 1, 1), (7, 1, 3, 4))
        ]

    def test_all_three_common_root_graphs_and_source_divisors(self):
        for graph in self.graphs:
            self.assertEqual(graph["kernel_pairs"], [[i, i] for i in range(4)])
            self.assertEqual(len(graph["plus_points"]), 4)
            field = R.P.Field(graph["p"], graph["degree"])
            for root, polynomial in zip(
                graph["common_roots_r"], graph["common_source_divisor_polynomials_u"]
            ):
                self.assertEqual(polynomial, [field.scale(root, -1), 0, 1])
                self.assertEqual(R.source_h(field, root, graph["b"], graph["c"]), 0)

    def test_graph_law_is_klein_four_and_preserves_inverse_pairing(self):
        for graph in self.graphs:
            for i, j in itertools.product(range(4), repeat=2):
                total = graph["addition_table"][i][j]
                self.assertEqual(total == 0, i == j)
                self.assertEqual(graph["addition_table"][total][j], i)
                for points in (graph["plus_points"], graph["minus_points"]):
                    pairing = R.two_pairing(points[i], points[j], graph["p"])
                    self.assertEqual(
                        pairing, 1 if i == 0 or j == 0 or i == j else graph["p"] - 1
                    )

    def test_frobenius_permutation_distinguishes_three_splitting_patterns(self):
        fixed_counts = [
            sum(i == image for i, image in enumerate(g["frobenius_indices"]) if i)
            for g in self.graphs
        ]
        self.assertEqual(fixed_counts, [1, 0, 3])
        for graph in self.graphs:
            permutation = graph["frobenius_indices"]
            self.assertEqual(sorted(permutation), list(range(4)))
            for i, j in itertools.product(range(4), repeat=2):
                self.assertEqual(
                    permutation[graph["addition_table"][i][j]],
                    graph["addition_table"][permutation[i]][permutation[j]],
                )

    def test_unsplit_field_is_rejected_before_claiming_full_torsion(self):
        with self.assertRaises(ValueError):
            R.torsion_graph(R.P.Field(7, 1), 1, 1)


class ArtifactControls(unittest.TestCase):
    def test_source_identity_guards_allocation_and_scalar_types(self):
        source = json.loads((HERE / "sign_split_source.json").read_text())
        self.assertEqual(R.P.digest(source), R.SOURCE_HASH)
        for value in (True, 2401.0, 10**9):
            changed = copy.deepcopy(source)
            changed["maximum_field_order"] = value
            with self.assertRaises(ValueError):
                R.build(changed)

    def test_independent_elliptic_polynomials_refine_frozen_sign_factor(self):
        artifact = json.loads((HERE / "sign_split_artifact.json").read_text())
        frozen = json.loads((HERE / "artifact.json").read_text())
        for panel, old in zip(artifact["panels"], frozen["panels"]):
            plus, minus = panel["polynomials"]["plus"], panel["polynomials"]["minus"]
            self.assertEqual(R.C.product(plus, minus), old["polynomials"]["D"])
            self.assertEqual([x % 2 for x in plus], [x % 2 for x in minus])
            if panel["p"] % 3 == 2:
                self.assertEqual(plus, [1, 0, panel["p"]])


if __name__ == "__main__":
    unittest.main()

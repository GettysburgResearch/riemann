"""Independent and adversarial finite controls; no generic theorem inferred."""

import importlib.util
import itertools
import json
import tempfile
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cycle_response", ROOT / "cycle_response.py"
)
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class CycleResponseTests(unittest.TestCase):
    def test_declared_source_incidence(self):
        actual = c.source_lift({"a": [[2]], "b": [[3]], "c": [[5]]})
        self.assertEqual(actual, c.matrix([[5, 2], [3, 0]]))
        self.assertEqual(
            c.source_lift({"a": [[2]], "b": [[3]], "c": [[5]]}, True),
            c.transpose(actual),
        )

    def test_scalar_weight_identity_in_distinct_specializations(self):
        for x, y, z in ((2, 3, 5), (Q(2, 3), Q(-7, 5), 0), (0, 3, -2)):
            labels = {"a": [[x]], "b": [[y]], "c": [[z]]}
            a, b = c.source_lift(labels), c.source_lift(labels, True)
            expected = c.trim([Q(1), -Q(z), -Q(x) * Q(y)])
            self.assertEqual(c.det_poly_leibniz(a), expected)
            self.assertEqual(c.det_poly_leibniz(b), expected)

    def test_nonsemisimple_commuting_controls(self):
        labels = {"a": [[2, 1], [0, 2]], "b": [[3, -4], [0, 3]], "c": [[5, 7], [0, 5]]}
        a, b = c.source_lift(labels), c.source_lift(labels, True)
        self.assertEqual(c.det_poly_leibniz(a), c.det_poly_leibniz(b))

    def test_s3_first_difference_and_cover_counts(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        w = c.transpose(c.mul(u, v))
        a, b = c.lift(u, v, w), c.lift(u, v, w, True)
        self.assertEqual(c.traces(a, 3), [0, 0, 12])
        self.assertEqual(c.traces(b, 3), [0, 0, 3])
        self.assertEqual(c.walk_counts(a, 3), [0, 0, 12])
        self.assertEqual(c.walk_counts(b, 3), [0, 0, 3])
        self.assertEqual(c.det_poly_leibniz(a), [1, 0, 0, -4, 0, 0, -1])
        self.assertEqual(c.det_poly_leibniz(b), [1, 0, 0, -1, -3, -3, -1])

    def test_principal_factor_and_standard_factor(self):
        principal = [Q(1), Q(-1), Q(-1)]
        self.assertEqual(c.pmul(principal, [1, 1, 2, -1, 1]), [1, 0, 0, -4, 0, 0, -1])
        self.assertEqual(c.pmul(principal, [1, 1, 2, 2, 1]), [1, 0, 0, -1, -3, -3, -1])

    def test_all_small_cover_assignments(self):
        checked = 0
        for d in (1, 2):
            labels = [c.permutation(p) for p in itertools.permutations(range(d))]
            for u, v, w in itertools.product(labels, repeat=3):
                self.assertEqual(
                    c.det_poly_leibniz(c.lift(u, v, w)),
                    c.det_poly_leibniz(c.lift(u, v, w, True)),
                )
                checked += 1
        self.assertEqual(checked, 9)

    def test_direct_primitive_cycle_euler_product(self):
        a = c.matrix([[1, 1], [1, 0]])
        cycles = c.primitive_cycles(a, 6)
        self.assertEqual(cycles, [1, 1, 1, 1, 2, 2])
        self.assertEqual(c.euler_coefficients(cycles), [1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(
            c.euler_coefficients(cycles), c.inverse_series(c.det_poly_leibniz(a), 6)
        )

    def test_parallel_edges_are_distinct_cycle_words(self):
        a = c.matrix([[2]])
        self.assertEqual(c.primitive_cycles(a, 4), [2, 1, 2, 3])
        self.assertEqual(c.walk_counts(a, 4), [2, 4, 8, 16])
        self.assertEqual(
            c.euler_coefficients(c.primitive_cycles(a, 4)), [1, 2, 4, 8, 16]
        )

    def test_signed_orthogonal_dimension_two(self):
        u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
        self.assertEqual(c.commutator_energy(u, v), (12, 8))
        w = c.transpose(c.mul(u, v))
        self.assertEqual(c.det_poly_leibniz(c.lift(u, v, w)), [1, 0, 1, -2, 1])
        self.assertEqual(c.det_poly_leibniz(c.lift(u, v, w, True)), [1, 0, 1, 2, 1])

    def test_held_out_rational_orthogonal_pair(self):
        u = c.matrix([[Q(3, 5), Q(-4, 5)], [Q(4, 5), Q(3, 5)]])
        v = c.matrix([[1, 0], [0, -1]])
        gap, norm = c.commutator_energy(u, v)
        self.assertEqual(norm, Q(128, 25))
        self.assertEqual(gap, Q(192, 25))

    def test_held_out_s4_predictions(self):
        for p, q in c.SOURCE["held_out_s4_pairs"]:
            u, v = c.permutation(p), c.permutation(q)
            gap, _ = c.commutator_energy(u, v)
            k = c.mul(c.transpose(c.mul(u, v)), c.mul(v, u))
            moved = len(k) - sum(k[i][i] for i in range(len(k)))
            self.assertEqual(gap, 3 * moved)

    def test_transpose_duality(self):
        u = c.matrix([[1, 2], [0, 1]])
        v = c.matrix([[1, 0], [3, 1]])
        w = c.matrix([[2, 1], [0, -1]])
        original = c.lift(u, v, w)
        dual = c.lift(c.transpose(u), c.transpose(v), c.transpose(w), True)
        self.assertEqual(dual, c.transpose(original))
        self.assertEqual(c.det_poly_leibniz(original), c.det_poly_leibniz(dual))

    def test_alignment_is_not_automatic(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        wrong_w = c.eye(3)
        gap = (
            c.traces(c.lift(u, v, wrong_w), 3)[2]
            - c.traces(c.lift(u, v, wrong_w, True), 3)[2]
        )
        self.assertEqual(gap, 0)
        self.assertEqual(c.commutator_energy(u, v)[0], 9)

    def test_vertex_gauge_preserves_lift_but_not_fixed_label_response(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        w = c.transpose(c.mul(u, v))
        original = c.lift(u, v, w)
        gauged_u, gauged_v = c.eye(3), c.mul(u, v)
        gauged = c.lift(gauged_u, gauged_v, w)
        self.assertEqual(w, c.transpose(c.mul(gauged_u, gauged_v)))
        self.assertEqual(c.det_poly_leibniz(original), c.det_poly_leibniz(gauged))
        self.assertEqual(c.commutator_energy(u, v)[0], 9)
        self.assertEqual(c.commutator_energy(gauged_u, gauged_v)[0], 0)

    def test_nonunitary_energy_rejected(self):
        with self.assertRaises(ValueError):
            c.commutator_energy([[1, 1], [0, 1]], [[1, 0], [1, 1]])

    def test_determinant_methods_on_untrained_matrix(self):
        a = c.matrix([[2, -1, 0], [1, 3, 2], [0, -2, 1]])
        self.assertEqual(c.det_poly_leibniz(a), c.det_poly_newton(a))

    def test_exact_types_and_work_caps(self):
        for bad in ([[True]], [[1.0]], [[1 + 0j]], [[1, 2]], [[2**129]]):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                c.matrix(bad)
        with self.assertRaises(ValueError):
            c.permutation([0, 0])
        with self.assertRaises(ValueError):
            c.permutation([False, True])
        with self.assertRaises(ValueError):
            c.det_poly_leibniz(c.eye(7))
        with self.assertRaises(ValueError):
            c.primitive_cycles([[1]], 7)
        with self.assertRaises(ValueError):
            c.traces([[1]], 9)

    def test_primitive_source_mutation_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            mutated = dict(c.SOURCE)
            mutated["edges"] = [[0, 0, "a"]]
            (destination / "source.json").write_text(
                json.dumps(mutated), encoding="utf-8"
            )
            with (
                patch.object(c, "HERE", destination),
                self.assertRaisesRegex(ValueError, "source contract"),
            ):
                c.build_payload()


if __name__ == "__main__":
    unittest.main()

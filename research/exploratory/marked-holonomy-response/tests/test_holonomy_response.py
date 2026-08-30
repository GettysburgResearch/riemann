"""Independent transfer, gauge, cycle and refusal controls."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("holonomy", HERE / "holonomy_response.py")
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
c = h.c


class HolonomyTests(unittest.TestCase):
    def test_literal_lifted_graph_cycles(self):
        u, v = c.permutation([1, 0, 2]), c.permutation([0, 2, 1])
        self.assertEqual(h.literal_lift_cycles(u, v), [3, 3, 3])
        self.assertEqual(h.literal_lift_cycles(u, v, True), [9])
        with self.assertRaises(ValueError):
            h.literal_lift_cycles([[-1]], [[1]])

    def test_permutation_minimum_and_predicted_cycles(self):
        for d in (1, 2):
            for p, q in h.itertools.product(
                h.itertools.permutations(range(d)), repeat=2
            ):
                self.assertEqual(h.row(p, q)["trace_gap"], "0")
        result = h.row([1, 0, 2], [0, 2, 1])
        self.assertEqual(result["lifted_cycle_lengths"], [[3, 3, 3], [9]])
        self.assertEqual(result["trace_gap"], "9")
        self.assertEqual(result["determinants"][1], ["1"] + ["0"] * 8 + ["-1"])

    def test_full_orthogonal_transfer(self):
        u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
        self.assertEqual(h.word_operator(u, v, True), c.matrix([[-1, 0], [0, -1]]))
        for reverse, sign in ((False, -1), (True, 1)):
            a = h.transfer(u, v, reverse)
            expected = [1, 0, 0, 2 * sign, 0, 0, 1]
            self.assertEqual(c.det_poly_leibniz(a), expected)
            self.assertEqual(c.det_poly_newton(a), expected)
            self.assertEqual(c.traces(a, 6), [0, 0, -6 * sign, 0, 0, 6])

    def test_based_conjugation_and_independent_vertex_gauges(self):
        u, v = c.matrix([[0, 1], [1, 0]]), c.matrix([[1, 0], [0, -1]])
        q = c.matrix([[c.Q(3, 5), -c.Q(4, 5)], [c.Q(4, 5), c.Q(3, 5)]])
        conjugate = lambda a: c.mul(c.mul(c.transpose(q), a), q)
        for reverse in (False, True):
            self.assertEqual(
                h.word_operator(conjugate(u), conjugate(v), reverse),
                conjugate(h.word_operator(u, v, reverse)),
            )
        gauges = (q, u, v)
        diagonal = c.matrix(
            [
                [
                    gauges[i // 2][i % 2][j % 2] if i // 2 == j // 2 else 0
                    for j in range(6)
                ]
                for i in range(6)
            ]
        )
        for reverse in (False, True):
            original = h.transfer(u, v, reverse)
            changed = c.mul(c.mul(c.transpose(diagonal), original), diagonal)
            self.assertEqual(c.det_poly_leibniz(original), c.det_poly_leibniz(changed))
            self.assertEqual(c.traces(original, 6), c.traces(changed, 6))

    def test_held_out_cycle_product_independent(self):
        results = [h.row(p, q) for p, q in h.SOURCE["held_out_s4_pairs"]]
        self.assertEqual(len(results), 3)
        self.assertTrue(any(result["trace_gap"] != "0" for result in results))
        self.assertTrue(any(result["trace_gap"] == "0" for result in results))

    def test_nonunitary_dimension_and_type_refusal(self):
        for u in ([[2]], [[1.0]], [[True]], [[complex(1)]], c.eye(5)):
            with self.assertRaises(ValueError):
                h.word_operator(u, u)
        with self.assertRaises(ValueError):
            h.transfer(c.eye(3), c.eye(3))
        with self.assertRaises(ValueError):
            h.word_operator([[1]], [[1]], reverse=1)
        with self.assertRaises(ValueError):
            h.cycle_product([True])
        with self.assertRaises(ValueError):
            h.cycle_product([4, 4])
        with self.assertRaises(ValueError):
            h.permutation_cycle_lengths([[1, 0], [1, 0]])

    def test_primitive_source_corruption_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bad = dict(h.SOURCE)
            bad["words"] = [["a", "b", "c"], ["c", "b", "a"]]
            (root / "source.json").write_text(json.dumps(bad), encoding="utf-8")
            with (
                patch.object(h, "HERE", root),
                self.assertRaisesRegex(ValueError, "primitive"),
            ):
                h.payload()

    def test_frozen_library_corruption_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            bad = Path(directory) / "cycle_response.py"
            bad.write_bytes(b"altered matrix library")
            with patch.object(h, "LIBRARY", bad), self.assertRaises(ValueError):
                h.authenticate_library()

    def test_complete_fixture_matches_recomputed_payload(self):
        value = json.loads((HERE / "verification.json").read_text(encoding="utf-8"))
        self.assertEqual(
            value.pop("payload_sha256"),
            h.hashlib.sha256(h.canonical(value).encode()).hexdigest(),
        )
        self.assertEqual(value, h.payload())


if __name__ == "__main__":
    unittest.main()

"""Exact regression controls for the source-algebra adapter, not native gluing."""

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "source_algebra_diagonal_adams_adapter",
    ROOT / "research/riemann-structures/source_algebra_diagonal_adams_adapter.py",
)
adapter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = adapter
SPEC.loader.exec_module(adapter)
Source = adapter.Source


class SourceAlgebraAdapterTests(unittest.TestCase):
    def setUp(self):
        self.cycle = Source((1, 0), (1, 1))
        self.split = Source((0, 1), (1, -1))

    def test_cycle_and_split_have_identical_traces(self):
        for n in range(1, 13):
            self.assertEqual(adapter.pushed_trace(self.cycle, n), adapter.pushed_trace(self.split, n))

    def test_literal_diagonals_differ(self):
        dc = adapter.tensor_over_source(self.cycle, self.cycle)
        ds = adapter.tensor_over_source(self.split, self.split)
        self.assertEqual(adapter.pushed_trace(dc, 1), 0)
        self.assertEqual(adapter.pushed_trace(ds, 1), 2)

    def test_source_Adams_does_not_commute_with_pushforward(self):
        self.assertEqual(adapter.source_adams_trace(self.cycle, 1, 2), 0)
        self.assertEqual(adapter.pushed_adams_trace(self.cycle, 1, 2), 2)

    def test_degree_two_primitive_data_differ(self):
        self.assertEqual(adapter.primitive_trace(self.cycle, 2), 1)
        self.assertEqual(adapter.primitive_trace(self.split, 2), 0)

    def test_primitive_extractor_is_source_aware(self):
        self.assertEqual(adapter.extract_primitive(self.cycle, 2), 1)
        self.assertEqual(adapter.extract_primitive(self.cycle, 2, after_pushforward=True), 0)

    def test_total_but_not_partial_Frobenius(self):
        self.assertEqual(adapter.projector_commutator_size(self.cycle, partial=False), 0)
        self.assertGreater(adapter.projector_commutator_size(self.cycle, partial=True), 0)
        self.assertEqual(adapter.projector_commutator_size(self.split, partial=True), 0)

    def test_same_source_identification_required(self):
        with self.assertRaises(ValueError):
            adapter.tensor_over_source(self.cycle, self.split)

    def test_exact_input_and_invertibility(self):
        for weights in ((0, 1), (1 << 40, 1)):
            with self.assertRaises(ValueError):
                Source((1, 0), weights)
        for weights in ((1.0, 1), (True, 1)):
            with self.assertRaises(TypeError):
                Source((1, 0), weights)
        for sigma in ((True, 0), (1, 1), ()):
            with self.assertRaises(ValueError):
                Source(sigma, tuple(1 for _ in sigma))

    def test_runtime_caps(self):
        for value in (0, 73, True):
            with self.assertRaises(ValueError):
                adapter.pushed_trace(self.cycle, value)
        with self.assertRaises(ValueError):
            adapter.source_adams_trace(self.cycle, 9, 9)

    def test_nonintegral_heldout_five_cycle(self):
        source = Source((1, 2, 3, 4, 0), (1, 2, 3, -1, Fraction(1, 2)))
        self.assertEqual(adapter.primitive_trace(source, 5), -3)
        self.assertEqual(adapter.pushed_trace(source, 5), -15)
        self.assertEqual(adapter.extract_primitive(source, 5), -3)
        adapter.check_source(source)

    def test_mixed_orbit_source(self):
        source = Source((0, 2, 1), (2, 3, 5))
        self.assertEqual(adapter.pushed_trace(source, 1), 2)
        self.assertEqual(adapter.pushed_trace(source, 2), 34)
        self.assertEqual(adapter.primitive_trace(source, 2), 15)
        adapter.check_source(source)

    def test_bool_int_fixture_mutation_rejected(self):
        with self.assertRaises(ValueError):
            adapter.check_fixture({"count": True}, {"count": 1})

    def test_LF_hash_is_checkout_independent(self):
        self.assertEqual(adapter.digest(b"a\nb\n"), adapter.digest(b"a\r\nb\r\n"))

    def test_full_fixture(self):
        adapter.check_fixture(
            json.loads(adapter.FIXTURE.read_text(encoding="utf-8")), adapter.build_report()
        )

    def test_counterfeit_intertwiner_and_scope(self):
        result = adapter.counterfeit()
        self.assertEqual(result["intertwiner_determinant"], -2)
        self.assertEqual(result["cycle_P2"], "1")
        self.assertEqual(result["split_P2"], "0")


if __name__ == "__main__":
    unittest.main()

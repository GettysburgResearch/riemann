"""Independent source specialization and hostile-input checks for marked orbits."""

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "marked_kummer_orbit_obstruction.py"
)
SPEC = importlib.util.spec_from_file_location("marked_kummer_orbit", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class MarkedKummerOrbitTests(unittest.TestCase):
    def test_actual_source_witness_after_complete_owner_sum(self):
        p = M.source_polynomial()
        external = (1, -1, 1, -1, -1, 1, -1, -1)
        self.assertEqual(p.evaluate(19, external + (1,)), 4 * 176203654560)
        self.assertEqual(p.evaluate(19, external + (-1,)), 4 * 175867233696)
        self.assertEqual(
            (p.evaluate(19, external + (-1,)) - p.evaluate(19, external + (1,))) // 4,
            -336420864,
        )

    def test_character_parity_does_not_mean_discarding_odd_part(self):
        p = M.source_polynomial()
        odd = M.Poly(
            {key: value for key, value in p.terms.items() if key[1] & M.CROSSED}
        )
        self.assertTrue(odd.terms)
        a = M.Poly({(0, M.CROSSED): 1})
        self.assertEqual(a.square().terms, {(0, 0): 1})
        external = (1, -1, 1, -1, -1, 1, -1, -1)
        self.assertGreater(odd.evaluate(19, external + (1,)), 0)
        self.assertEqual(
            odd.evaluate(19, external + (-1,)), -odd.evaluate(19, external + (1,))
        )

    def test_partial_map_moves_the_divisor_but_total_is_odd_power(self):
        self.assertEqual(M.pullback(M.graph(0), "left"), M.graph(1))
        self.assertNotEqual(M.pullback(M.graph(0), "left"), M.graph(0))
        self.assertEqual(
            M.pullback(M.graph(-1), "left"), M.pullback(M.graph(0), "total")
        )
        self.assertEqual(
            M.pullback(M.graph(1), "right"), M.pullback(M.graph(0), "total")
        )

    def test_distinct_graphs_can_intersect_without_sharing_a_divisor(self):
        residual = M.restrict_to_graph(M.graph(1), 0)
        self.assertEqual(residual, {1: 1, 5: 4})
        self.assertNotEqual(residual, {})
        self.assertEqual(M.restrict_to_graph(M.graph(1), 1), {})

    def test_finite_orbit_products_do_not_close_under_translation(self):
        for support in ((0,), (-2, 0, 3), (-4, -3, -2, -1)):
            translates = [M.shifted_support(support, step) for step in range(10)]
            self.assertEqual(len(set(translates)), 10)
            self.assertTrue(all(len(x) == len(support) for x in translates))
        self.assertEqual(M.shifted_support((), 9), ())

    def test_graph_and_support_work_caps_fail_closed(self):
        for index in (True, 1.0, -9, 9):
            with self.subTest(index=index), self.assertRaises(ValueError):
                M.graph(index)
        for support in ((0, 0), (True,), tuple(range(33))):
            with self.subTest(support=support), self.assertRaises(ValueError):
                M.shifted_support(support, 1)
        with self.assertRaises(ValueError):
            M.pullback(M.graph(0), "unmarked")

    def test_polynomial_inputs_do_not_accept_bool_or_fractional_signs(self):
        for terms in ({(True, 0): 1}, {(0, 512): 1}, {(0, 0): True}, {(17, 0): 1}):
            with self.subTest(terms=terms), self.assertRaises(ValueError):
                M.Poly(terms)
        with self.assertRaises(ValueError):
            M.Poly.scalar(1).evaluate(19, (True,) * 9)
        with self.assertRaises(ValueError):
            M.Poly.scalar(1).evaluate(10001, (1,) * 9)

    def test_frozen_blob_is_authenticated_before_source_acceptance(self):
        class Response:
            stdout = "3"

        with (
            patch.object(
                M.subprocess,
                "run",
                side_effect=[Response(), type("Bytes", (), {"stdout": b"bad"})()],
            ),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))
        with self.assertRaises(ValueError):
            M.source_bytes("unlocked.md")

    def test_artifact_comparison_is_strict_about_numeric_types(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()

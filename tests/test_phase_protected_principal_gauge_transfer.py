"""Protected native gauge inverse, weighted bounds, and mask regressions."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "phase_protected_principal_gauge_transfer.py"
)
SPEC = importlib.util.spec_from_file_location("protected_gauge", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ProtectedGaugeTests(unittest.TestCase):
    def test_local_phase_geometry_reconstructs_canonical_selectors(self):
        self.assertEqual(M.allowed(3), (0, 3))
        self.assertEqual(M.allowed(7), (0, 1, 3))
        self.assertEqual(M.allowed(29), (0, 1, 2, 3))
        self.assertEqual(M.allowed(5), (1,))
        self.assertEqual(M.allowed(13), (2,))
        self.assertEqual(M.allowed(31), (0,))
        for state in M.alphabet(M.PRIMES):
            M.record(state)

    def test_true_inverse_is_not_compressed_original_inverse(self):
        tau = Fraction(1, 3)
        a, _ = M.parameter(tau)
        self.assertEqual(M.local_entry(3, 3, 0, tau, True)[0], -a * a / 3)
        self.assertNotEqual(M.local_entry(3, 3, 0, tau, True)[0], a * a / 3)
        self.assertEqual(M.local_entry(7, 3, 0, tau, True)[0], 0)
        self.assertEqual(M.local_entry(29, 3, 0, tau, True)[0], a * a / 29)

    def test_raw_square_gauge_and_native_weight_give_same_operator(self):
        states, forward, _, _, _ = M.matrices()
        i, j = states.index((0, 0, 1)), states.index((0, 0, 3))
        a, _ = M.parameter(Fraction(1, 3))
        self.assertEqual(forward[j][i], a)
        before, after = M.record(states[i]), M.record(states[j])
        self.assertEqual(Fraction(after["weight"]) / Fraction(before["weight"]), 29**2)

    def test_two_sided_inverse_and_derivative_identity(self):
        states, f, inv, df, dinv = M.matrices()
        self.assertEqual(M.multiply(f, inv), M.identity(len(states)))
        self.assertEqual(M.multiply(inv, f), M.identity(len(states)))
        self.assertEqual(
            M.add(M.multiply(df, inv), M.multiply(f, dinv)),
            [[Fraction(0)] * len(states) for _ in states],
        )

    def test_downward_horizon_preserves_inverse(self):
        states, f, inv, _, _ = M.matrices()
        indices = M.retained(states)
        self.assertLess(len(indices), len(states))
        self.assertEqual(
            M.multiply(M.restrict(f, indices), M.restrict(inv, indices)),
            M.identity(len(indices)),
        )

    def test_native_ratio_mask_deletes_required_inverse_paths(self):
        states, f, inv, _, _ = M.matrices()
        indices = M.retained(states, ratio_mask=True)
        initial, final = states.index((0, 0, 0)), states.index((0, 0, 3))
        self.assertIn(initial, indices)
        self.assertIn(final, indices)
        self.assertNotIn(states.index((0, 0, 1)), indices)
        self.assertNotIn(states.index((0, 0, 2)), indices)
        actual = M.multiply(M.restrict(f, indices), M.restrict(inv, indices))
        a, _ = M.parameter(Fraction(1, 3))
        self.assertEqual(
            actual[indices.index(final)][indices.index(initial)], 2 * a * a / 29
        )

    def test_endpoint_and_stationary_homotopy_controls(self):
        for tau in (Fraction(0), Fraction(1)):
            _, f, inv, _, _ = M.matrices(tau=tau)
            self.assertEqual(f, M.identity(len(f)))
            self.assertEqual(inv, f)
        _, _, _, df, dinv = M.matrices(tau=Fraction(1, 2))
        self.assertTrue(all(x == 0 for row in df + dinv for x in row))

    def test_uniform_majorant_survives_actual_entry_mask(self):
        states, f, inv, _, _ = M.matrices()
        indices = M.retained(states, ratio_mask=True)
        for matrix in (f, inv):
            masked = M.restrict(matrix, indices)
            self.assertLessEqual(
                max(M.absolute_sums(masked)), max(M.absolute_sums(matrix))
            )
        self.assertEqual(M.ABS_B, Fraction(33, 256))
        self.assertEqual(M.ABS_F, Fraction(289, 256))

    def test_hostile_types_and_work_caps_are_rejected(self):
        for tau in (0.5, True, Fraction(-1), Fraction(2)):
            with self.subTest(tau=tau), self.assertRaises(ValueError):
                M.parameter(tau)
        for primes in ((3, 3), (67,), (5,), (29, 41, 43)):
            with self.subTest(primes=primes), self.assertRaises(ValueError):
                M.alphabet(primes)
        with self.assertRaises(ValueError):
            M.allowed(True)
        with self.assertRaises(ValueError):
            M.record((True, 0, 0))
        with self.assertRaises(ValueError):
            M.identity(33)

    def test_primitive_mutation_and_numeric_json_substitution_fail(self):
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()

"""Exact native selector/weight and source-support regression tests."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "principal_selector_gauge_obstruction.py"
)
SPEC = importlib.util.spec_from_file_location("principal_selector_gauge", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class PrincipalSelectorGaugeTests(unittest.TestCase):
    def test_actual_least_prime_enters_common_core_and_reveals_large_phase(self):
        result = M.insertion((5, 1009, 1021), (3, 1201, 1223), 3, Fraction(1, 2))
        before, after = result["before"], result["after"]
        self.assertEqual((before["g"], before["ell"], before["rho"]), (1, 5, 3))
        self.assertEqual((after["g"], after["ell"], after["rho"]), (3, 5, 1201))
        self.assertEqual(result["gauge_physical_coefficient"], "-1/48")
        self.assertEqual(Fraction(before["weight"]), 45)
        self.assertEqual(
            Fraction(result["weighted_matrix_entry_squared"]),
            Fraction(1201, 1536) * Fraction(1202, 1200),
        )

    def test_each_interaction_is_native_but_no_common_width_eight_shell(self):
        result = M.insertion((5, 1009, 1021), (3, 1201, 1223), 3, Fraction(1, 2))
        for item in (result["before"], result["after"]):
            self.assertTrue(Fraction(1, 8) < Fraction(item["physical_ratio"]) < 8)
        self.assertEqual(result["after"]["N"], 9 * result["before"]["N"])
        self.assertGreater(Fraction(result["after"]["N"], result["before"]["N"]), 8)

    def test_nonleast_extraction_has_no_conductor_jump_algebraically(self):
        # This is an algebra control only; its large physical shift is not a live shell claim.
        result = M.insertion((5, 1009, 1021), (3, 1201, 1223), 1223, Fraction(1, 2))
        self.assertEqual(result["after"]["rho"], 3)
        self.assertEqual(
            Fraction(result["weighted_matrix_entry_squared"]), Fraction(1, 256)
        )

    def test_literal_gamma_denominator_transport_matches_square_shift(self):
        result = M.insertion((5, 1009, 1021), (3, 1201, 1223), 3, Fraction(1, 2))
        old = result["before"]["native_denominator_without_sqrt_PQ"]
        new = result["after"]["native_denominator_without_sqrt_PQ"]
        self.assertEqual(new, 3 * old)
        self.assertEqual(
            Fraction(result["gauge_physical_coefficient"]) * Fraction(new, old),
            Fraction(-1, 16),
        )

    def test_fixed_primes_and_symbolic_window_margins(self):
        for p in (1009, 1021, 1201, 1223):
            self.assertTrue(M.prime(p))
        self.assertFalse(M.prime(1203))
        bounds = M.symbolic_windows()
        self.assertGreater(Fraction(bounds["input_ratio_lower"]), Fraction(1, 2))
        self.assertLess(Fraction(bounds["input_ratio_upper"]), Fraction(2, 3))

    def test_cutoff_root_has_exact_inclusive_endpoints(self):
        for n in (1, 63, 64, 65, 40000 * 1000**4):
            root = M.sixth_root(n)
            self.assertLessEqual(root**6, n)
            self.assertGreater((root + 1) ** 6, n)

    def test_illegal_native_records_and_parameter_types_fail_closed(self):
        for args in (((5, 5), (3, 1201)), ((5, 67), (3, 1201)), ((5, 11), (3, 1201))):
            with self.subTest(args=args), self.assertRaises(ValueError):
                M.state(*args)
        with self.assertRaises(ValueError):
            M.insertion((5, 1009), (3, 1201), 3, 0.5)
        with self.assertRaises(ValueError):
            M.prime(True)
        with self.assertRaises(ValueError):
            M.prime(1000001)

    def test_no_unverified_executable_primitive_can_be_loaded(self):
        with self.assertRaisesRegex(ValueError, "executable source blob"):
            M.load_boolean_algebra(b"raise RuntimeError('must not run')")
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))

    def test_strict_canonical_artifact_comparison(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()

"""Independent endpoint, complete-row, and diagonal checks for Euler activation."""

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "euler_activation_source_adapter.py"
)
SPEC = importlib.util.spec_from_file_location("euler_activation_adapter", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class EulerActivationTests(unittest.TestCase):
    def test_owner_selection_does_not_descend_to_zero_endpoint(self):
        record = M.density_record(3)
        self.assertEqual(record["owner_coefficient_before_physical_weight"], "-1/10")
        self.assertEqual(record["core_coefficient_before_physical_weight"], "1/10")
        self.assertEqual(record["linear_total"], "0")
        self.assertEqual(M.raw_coefficients((1, 1, 2, 2, 2))["raw_hard_remainder"], 0)

    def test_empty_core_semiprime_is_not_deleted(self):
        values = M.raw_coefficients((1, 1))
        self.assertEqual(values["E"], 1)
        self.assertEqual(values["S"], 0)
        self.assertEqual(values["raw_hard_remainder"], 1)
        with self.assertRaises(ValueError):
            M.density_record(0)

    def test_three_diagonal_conventions_are_distinct(self):
        record = M.density_record(3)
        self.assertEqual(record["site_time_diagonal_times_N"], "4/315")
        self.assertEqual(record["integrated_site_diagonal_times_N"], "1/120")
        self.assertEqual(record["two_sector_diagonal_times_N"], "1/50")
        self.assertEqual(record["centered_site_time_form_times_N"], "-4/315")
        self.assertLess(
            Fraction(record["integrated_site_diagonal_times_N"]),
            Fraction(record["site_time_diagonal_times_N"]),
        )

    def test_full_vaughan_rows_recombine_before_source_adapter(self):
        # Small algebra witness only; the frozen large-window primes are replayed by build.
        rows = M.boolean_rows((11, 3, 5), 10)
        self.assertEqual(rows["complete_allocations"], 27)
        self.assertEqual(rows["truncated_double_convolution"], -1)
        self.assertEqual(
            (rows["type_I"], rows["balanced"], rows["full_mu"]), (1, -2, -1)
        )
        self.assertEqual(len(rows["nonzero_balanced_histories"]), 2)
        self.assertEqual(
            [x["coefficient"] for x in rows["nonzero_balanced_histories"]], [-1, -1]
        )

    def test_vaughan_cutoff_boundary_is_literal(self):
        # The product3*5 moves into the truncated Boolean slots exactly at15.
        below = M.boolean_rows((17, 3, 5), 14)
        at = M.boolean_rows((17, 3, 5), 15)
        self.assertEqual(below["full_mu"], at["full_mu"])
        self.assertNotEqual(
            below["truncated_double_convolution"], at["truncated_double_convolution"]
        )

    def test_two_labelled_67_copies_need_not_have_zero_physical_alias(self):
        # Four distinct labelled linear factors can realize physical p*q*67^2.
        self.assertEqual(M.raw_coefficients((1, 1, 1, 1))["E"], 1)
        # The individually squared label is a different source monomial.
        self.assertEqual(M.raw_coefficients((1, 1, 2, 0))["E"], 0)

    def test_derivative_and_integral_preserve_exact_rationals(self):
        poly = (Fraction(0), Fraction(0), Fraction(1), Fraction(-2), Fraction(1))
        self.assertEqual(M.integral(M.derivative(poly)), 0)
        self.assertEqual(M.integral(poly), Fraction(1, 30))
        self.assertEqual(
            M.multiply((Fraction(1), Fraction(-1)), (Fraction(1), Fraction(1))),
            (Fraction(1), Fraction(0), Fraction(-1)),
        )

    def test_caps_and_numeric_types_fail_closed(self):
        for depth in (True, 1.0, 0, 17):
            with self.subTest(depth=depth), self.assertRaises(ValueError):
                M.density_record(depth)
        for labels in ((3, 3), (True, 3), tuple(range(2, 9))):
            with self.subTest(labels=labels), self.assertRaises(ValueError):
                M.boolean_rows(labels, 10)
        with self.assertRaises(ValueError):
            M.raw_coefficients((1, True, 2))
        with self.assertRaises(ValueError):
            M.trim((1, 2))

    def test_source_git_blob_is_checked(self):
        first = type("Size", (), {"stdout": "3"})()
        second = type("Bytes", (), {"stdout": b"bad"})()
        with (
            patch.object(M.subprocess, "run", side_effect=[first, second]),
            self.assertRaisesRegex(ValueError, "Git blob"),
        ):
            M.source_bytes(next(iter(M.SOURCES)))
        with self.assertRaises(ValueError):
            M.source_bytes(("0" * 40, "unbound.md"))

    def test_canonical_acceptance_rejects_numeric_type_changes(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})


if __name__ == "__main__":
    unittest.main()

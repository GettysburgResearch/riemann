from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x15416_verify", ROOT / "verify.py")
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("unable to load verifier")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


class TerminalEulerGeometryTests(unittest.TestCase):
    def test_main_verdict(self) -> None:
        result = VERIFY.build_result()
        self.assertEqual(
            result["verdict"],
            "SYNTHETIC_TERMINAL_EULER_GEOMETRY_VERIFIED",
        )

    def test_noncoprime_true_step(self) -> None:
        row = VERIFY.solution_geometry_row(5, 5, 5, 50)
        self.assertEqual(row["true_step"], [1, 1])
        self.assertEqual(row["false_shift_residue_class_count"], 3)

    def test_coprime_control(self) -> None:
        row = VERIFY.solution_geometry_row(5, 6, 1, 80)
        self.assertEqual(row["true_step"], [5, 6])
        self.assertEqual(row["false_shift_residue_class_count"], 1)

    def test_second_noncoprime_control(self) -> None:
        row = VERIFY.solution_geometry_row(8, 12, 4, 80)
        self.assertEqual(row["true_step"], [2, 3])
        self.assertEqual(row["false_shift_residue_class_count"], 2)

    def test_no_solution_when_gcd_does_not_divide_r(self) -> None:
        with self.assertRaises(ValueError):
            VERIFY.solution_geometry_row(8, 12, 2, 20)

    def test_moment_rows(self) -> None:
        for order in range(1, 12):
            self.assertTrue(VERIFY.moment_row(order)["all_zero"])

    def test_reserve_is_strict(self) -> None:
        for delta in (
            Fraction(1, 5),
            Fraction(1, 3),
            Fraction(49, 100),
        ):
            self.assertTrue(VERIFY.exponent_row(delta)["contracting"])

    def test_boundary_reserve_rejected(self) -> None:
        self.assertFalse(VERIFY.exponent_row(Fraction(1, 2))["contracting"])


if __name__ == "__main__":
    unittest.main()

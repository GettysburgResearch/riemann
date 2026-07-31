from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x14307_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = V
SPEC.loader.exec_module(V)


class GrowingLowBlockTests(unittest.TestCase):
    def test_escaping_mode_keeps_negative_norm(self) -> None:
        result = V.verify_escaping(max_level=9, fixed_prefix=3)
        self.assertTrue(result["all_late_fixed_entries_zero"])
        self.assertTrue(result["all_operator_norms_one"])
        self.assertTrue(result["all_minimum_eigenvalues_minus_one"])

    def test_escaping_mode_rejects_short_ladder(self) -> None:
        with self.assertRaises(V.VerificationError):
            V.verify_escaping(max_level=3, fixed_prefix=3)

    def test_quantitative_tightness_packet(self) -> None:
        result = V.verify_tightness_bound()
        self.assertEqual(
            Fraction(
                int(result["L14312_total_norm_upper"]["numerator"]),
                int(result["L14312_total_norm_upper"]["denominator"]),
            ),
            Fraction(3, 125),
        )

    def test_radical_schur_packet(self) -> None:
        result = V.verify_radical_schur()
        self.assertEqual(
            Fraction(
                int(result["lower_floor_loss"]["numerator"]),
                int(result["lower_floor_loss"]["denominator"]),
            ),
            Fraction(1, 200),
        )

    def test_ldl_rejects_negative_direction(self) -> None:
        with self.assertRaises(V.VerificationError):
            V.ldl_nonnegative(
                [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]]
            )

    def test_full_result_is_stable(self) -> None:
        first = V.run()
        second = V.run()
        self.assertEqual(first, second)
        self.assertEqual(first["verdict"], "PASS_EXACT_FINITE_REGRESSIONS")
        self.assertEqual(
            first["proof_object_sha256"],
            "a97c525a0efc578ece75038764be27dc59cd040763aabfbfae233e716b03965d",
        )


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_beta_gram_sign_geometry.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("beta_gram_sign_geometry", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta Gram sign-geometry producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsBetaGramSignGeometryTest(unittest.TestCase):
    def test_frozen_source_quartet(self) -> None:
        subject.check_source_blobs()
        self.assertEqual(len(subject.SOURCE_BLOBS), 4)

    def test_closed_formula_matches_direct_branch_integration(self) -> None:
        for shift in subject.DIRECT_CHECK_SHIFTS:
            with self.subTest(shift=shift):
                closed = subject.raw_correlation_decimal(shift)
                direct = subject.direct_raw_correlation_decimal(shift)
                self.assertLessEqual(abs(closed - direct), Decimal("1e-75"))

    def test_exact_endpoint_values_and_evenness(self) -> None:
        with localcontext() as context:
            context.prec = subject.DECIMAL_PRECISION
            one = Decimal(1)
            two = Decimal(2)
            exp_one = one.exp()
            sinh_two = (two.exp() - (-two).exp()) / two
            self.assertLessEqual(
                abs(subject.raw_correlation_decimal(0) - (one + sinh_two / two)),
                Decimal("1e-75"),
            )
            self.assertLessEqual(
                abs(subject.raw_correlation_decimal(1) + exp_one / two),
                Decimal("1e-75"),
            )
        self.assertEqual(subject.raw_correlation_decimal(2), 0)
        self.assertEqual(subject.raw_correlation_decimal(3), 0)
        for shift in (Fraction(1, 7), Fraction(4, 5), Fraction(3, 2), 2):
            self.assertEqual(
                subject.correlation_decimal(shift),
                subject.correlation_decimal(-shift),
            )

    def test_unique_node_bracket_and_sign_geometry(self) -> None:
        lower, upper = subject.root_bracket()
        self.assertGreater(subject.raw_correlation_decimal(lower), 0)
        self.assertLess(subject.raw_correlation_decimal(upper), 0)
        with localcontext() as context:
            context.prec = subject.DECIMAL_PRECISION
            self.assertLess(upper - lower, Decimal("3e-39"))
        self.assertTrue(str(lower).startswith("0.63921327054652060848"))

        for index in range(subject.SIGN_GRID_CELLS + 1):
            radius = Fraction(index, subject.SIGN_GRID_CELLS)
            self.assertLess(subject.raw_inner_derivative_decimal(radius), 0)
        for radius in (0, Fraction(1, 4), Fraction(1, 2), Fraction(3, 5)):
            self.assertGreater(subject.correlation_decimal(radius), 0)
        for radius in (Fraction(2, 3), 1, Fraction(3, 2), Fraction(7, 4)):
            self.assertLess(subject.correlation_decimal(radius), 0)
        self.assertEqual(subject.correlation_decimal(2), 0)
        self.assertEqual(subject.correlation_decimal(Fraction(9, 4)), 0)

    def test_ratio_annuli_are_reciprocal(self) -> None:
        for radius, expected_sign in ((0.5, 1), (1.0, -1), (1.75, -1), (2.1, 0)):
            ratio = math.exp(radius)
            reciprocal = 1.0 / ratio
            forward = subject.correlation(math.log(ratio))
            backward = subject.correlation(math.log(reciprocal))
            self.assertTrue(math.isclose(forward, backward, rel_tol=0, abs_tol=2e-15))
            if expected_sign > 0:
                self.assertGreater(forward, 0)
            elif expected_sign < 0:
                self.assertLess(forward, 0)
            else:
                self.assertEqual(forward, 0)

    def test_integral_and_moment_identities(self) -> None:
        zeroth = subject.simpson_absolute_moment(0)
        absolute_first = subject.simpson_absolute_moment(1)
        second = subject.simpson_absolute_moment(2)
        expected_first = (2.0 - math.sinh(2.0)) / (16.0 * math.sinh(0.5) ** 4)
        self.assertAlmostEqual(zeroth, 0.0, delta=2e-13)
        self.assertAlmostEqual(absolute_first, expected_first, delta=4e-12)
        self.assertAlmostEqual(second, -2.0, delta=2e-13)

    def test_fixture_and_scope_are_canonical(self) -> None:
        for optimized in (False, True):
            command = ["python", "-B"]
            if optimized:
                command.append("-O")
            command.extend((str(SCRIPT), "--check"))
            completed = subprocess.run(
                command,
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=20,
            )
            self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["unique_interior_node_and_complete_sign_geometry"],
            "PROVED EXACT",
        )
        self.assertFalse(
            fixture["programme_boundary"]["physical_kernel_pointwise_nonnegative"]
        )
        self.assertFalse(fixture["programme_boundary"]["rh_or_grh_proved"])
        self.assertEqual(fixture["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        for bad in (float("nan"), float("inf"), "NaN"):
            with self.assertRaises(ValueError):
                subject.raw_correlation_decimal(bad)
        with self.assertRaises(TypeError):
            subject.raw_correlation_decimal(True)
        for bad in (-1, Fraction(3, 2)):
            with self.assertRaises(ValueError):
                subject.raw_inner_derivative_decimal(bad)
        for bad in (True, 0, 257):
            with self.assertRaises(ValueError):
                subject.root_bracket(bad)
        with self.assertRaises(TypeError):
            subject.correlation("0")
        for panels in (1, 3, subject.MAX_SIMPSON_PANELS_PER_PIECE + 2):
            with self.assertRaises(ValueError):
                subject.simpson_absolute_moment(1, panels)


if __name__ == "__main__":
    unittest.main()

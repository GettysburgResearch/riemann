from __future__ import annotations

import importlib.util
from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


builder = load_module(
    "positive_anchor_source_builder",
    ROOT / "build_positive_anchor_source.py",
)
verifier = load_module(
    "positive_anchor_pa1_verifier",
    ROOT / "verify_pa1.py",
)


class PositiveAnchorPA1Tests(unittest.TestCase):
    def test_source_patch_is_exact(self) -> None:
        source = (
            "prefix\n"
            "#define X_COUNT 3\n"
            "static const int X_BITS[X_COUNT] = {20, 10, 5};\n"
            "suffix\n"
        )
        patched, manifest = builder.patch(source)
        self.assertIn("static const int X_BITS[X_COUNT] = {0};", patched)
        self.assertEqual(manifest["x_coordinate"], {"numerator": 1, "denominator": 1})
        self.assertEqual(manifest["u_coordinate"], {"numerator": 1, "denominator": 1})
        self.assertEqual(manifest["emitted_point_count"], 1)

    def test_source_patch_rejects_multiple_grids(self) -> None:
        block = (
            "#define X_COUNT 2\n"
            "static const int X_BITS[X_COUNT] = {2, 1};\n"
        )
        with self.assertRaises(ValueError):
            builder.patch(block + block)

    def test_reduced_polynomial_identity(self) -> None:
        nodes = [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
        beta, reduced = verifier.reduced_coefficients(nodes)
        denominator = verifier.denominator_polynomial(nodes)
        self.assertEqual(beta, -1 / verifier.poly_evaluate(denominator, -1))
        # The returned old-node response polynomial has degree at most n-2,
        # hence at most one in this three-node control.
        self.assertTrue(all(value == 0 for value in reduced[2:]))

    def test_interval_intersection(self) -> None:
        left = verifier.RationalInterval(Fraction(0), Fraction(2))
        right = verifier.RationalInterval(Fraction(1), Fraction(3))
        self.assertEqual(
            verifier.interval_intersection(left, right),
            verifier.RationalInterval(Fraction(1), Fraction(2)),
        )

    def test_disjoint_intervals_are_rejected(self) -> None:
        left = verifier.RationalInterval(Fraction(0), Fraction(1))
        right = verifier.RationalInterval(Fraction(2), Fraction(3))
        with self.assertRaises(verifier.CertificateError):
            verifier.interval_intersection(left, right)

    def test_polynomial_division_rejects_remainder(self) -> None:
        with self.assertRaises(verifier.CertificateError):
            verifier.poly_divide_linear([Fraction(1), Fraction(0), Fraction(1)], Fraction(1))


if __name__ == "__main__":
    unittest.main()

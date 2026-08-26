from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_boundary_field_primitive_ray_localization.py"
)
SPEC = importlib.util.spec_from_file_location("boundary_primitive_rays", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BoundaryFieldPrimitiveRayLocalizationTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_beta_exceptional_local_factor(self) -> None:
        self.assertEqual(subject.beta(1), 1)
        self.assertEqual(subject.beta(67), -2)
        self.assertEqual(subject.beta(67**2), 1)
        self.assertEqual(subject.beta(67**3), 0)
        self.assertEqual(subject.beta(5 * 67), 2)
        self.assertEqual(subject.beta(5 * 67**2), -1)
        self.assertEqual(subject.beta(25 * 67), 0)

    def test_exact_ray_formula(self) -> None:
        for left, right, prefix in subject.RAY_SAMPLES:
            with self.subTest(left=left, right=right):
                self.assertEqual(
                    subject.scaled_ray_weight_direct(left, right, prefix),
                    subject.scaled_ray_weight_formula(left, right, prefix),
                )

    def test_exceptional_radial_sums(self) -> None:
        self.assertEqual(
            subject.exceptional_radial_sum(0, 0),
            Fraction(1) + Fraction(4, 67) + Fraction(1, 67**2),
        )
        self.assertEqual(
            subject.exceptional_radial_sum(1, 0), -Fraction(2) - Fraction(2, 67)
        )
        self.assertEqual(
            subject.exceptional_radial_sum(0, 1), -Fraction(2) - Fraction(2, 67)
        )
        self.assertEqual(subject.exceptional_radial_sum(2, 0), 1)
        self.assertEqual(subject.exceptional_radial_sum(0, 2), 1)

    def test_radial_projector_local_algebra(self) -> None:
        self.assertEqual(len(subject.ordinary_local_identity()), 4)
        self.assertEqual(len(subject.exceptional_local_identity()), 9)
        self.assertEqual(subject.exceptional_residue_ratio(), Fraction(2379, 2278))

    def test_squarefree_coprime_harmonic(self) -> None:
        expected = (
            Fraction(1)
            + Fraction(1, 2)
            + Fraction(1, 3)
            + Fraction(1, 5)
            + Fraction(1, 6)
        )
        self.assertEqual(subject.squarefree_coprime_harmonic(6, 67), expected)
        self.assertEqual(
            subject.squarefree_coprime_harmonic(66, 67),
            subject.squarefree_coprime_harmonic(66, 1),
        )

    def test_scope_and_guards(self) -> None:
        result = subject.run(check_sources=False)
        self.assertFalse(result["localization"]["residual_estimate_proved"])
        self.assertFalse(result["localization"]["rh_proved"])
        self.assertFalse(
            result["radial_projector"]["critical_line_convergence_claimed"]
        )
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        with self.assertRaises(ValueError):
            subject.beta(0)
        with self.assertRaises(ValueError):
            subject.ray_parts(67, 67)
        with self.assertRaises(ValueError):
            subject.ray_parts(67**3, 1)
        with self.assertRaises(ValueError):
            subject.squarefree_coprime_harmonic(-1, 1)
        with self.assertRaises(ValueError):
            subject.exceptional_radial_sum(1, 1)


if __name__ == "__main__":
    unittest.main()

"""Tests for the bounded Architecture-E algebra checker."""

from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "exploratory"
    / "xi_source_hermite_stieltjes_closure.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "xi_source_hermite_stieltjes_closure", MODULE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ArchitectureEClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_complete_exact_report(self) -> None:
        report = self.module.build_report()
        self.assertTrue(report["all_passed"])
        self.assertEqual(
            report["schema"], "xi-source-hermite-stieltjes-closure-v1"
        )
        checks = report["checks"]
        self.assertEqual(checks["companion_congruence_rows"], 2)
        self.assertEqual(checks["multiplier_defect_rows"], 20)
        self.assertEqual(checks["stieltjes_two_channel_rows"], 27)
        self.assertEqual(checks["source_factor_four"]["ratio"], "4")
        self.assertEqual(
            [
                row["CKE_lower_bound"]
                for row in checks[
                    "nonisometric_compression_counterexamples"
                ]
            ],
            [2, 3, 5, 10],
        )

    def test_gaussian_rational_field_operations(self) -> None:
        G = self.module.GaussianRational
        Q = self.module.Q
        z = G(Q(2, 3), Q(5, 7))
        w = G(Q(-4, 9), Q(1, 6))
        self.assertEqual((z / w) * w, z)
        self.assertEqual(z * z.conjugate(), G(z.squared_modulus()))

    def test_multiplier_is_pointwise_contracting(self) -> None:
        Q = self.module.Q
        for value in (Q(0), Q(1, 10), Q(1), Q(3), Q(100)):
            kappa = self.module.kappa(value)
            self.assertLessEqual(abs(kappa), 1)

    def test_compression_counterexample_is_strict(self) -> None:
        rows = self.module.check_nonisometric_compression_counterexample()
        for row in rows:
            self.assertEqual(row["K_norm"], 1)
            self.assertEqual(row["CE_norm"], 1)
            self.assertGreater(row["CKE_lower_bound"], 1)


if __name__ == "__main__":
    unittest.main()

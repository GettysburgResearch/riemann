"""Tests for the exact Architecture-E Loewner checker."""

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
    / "xi_architecture_e_loewner_checks.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "xi_architecture_e_loewner_checks", MODULE_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ArchitectureELoewnerChecksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_complete_report(self) -> None:
        report = self.module.build_report()
        self.assertTrue(report["all_passed"])
        self.assertEqual(
            report["schema"], "xi-architecture-e-loewner-checks-v1"
        )
        checks = report["checks"]
        self.assertEqual(checks["loewner_difference_rows"], 75)
        self.assertEqual(
            checks["stieltjes_loewner_grams"],
            {"cell_rows": 50, "square_rows": 8},
        )

    def test_loewner_difference_includes_diagonal(self) -> None:
        self.assertEqual(self.module.check_loewner_difference(), 75)

    def test_stieltjes_quadratic_forms_are_exact_squares(self) -> None:
        result = self.module.check_stieltjes_loewner_grams()
        self.assertEqual(result["square_rows"], 8)


if __name__ == "__main__":
    unittest.main()

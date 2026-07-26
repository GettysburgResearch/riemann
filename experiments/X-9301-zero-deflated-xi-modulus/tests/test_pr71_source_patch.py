from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_pr71_rs_source", ROOT / "build_pr71_rs_source.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PatcherTests(unittest.TestCase):
    def test_exact_three_occurrence_patch(self):
        source = (
            f"comment {MODULE.OLD}\n"
            f"const {MODULE.OLD}\n"
            f"json {MODULE.OLD}\n"
        )
        output, manifest = MODULE.patch_source(source)
        self.assertEqual(output.count(MODULE.NEW), 3)
        self.assertNotIn(MODULE.OLD, output)
        self.assertEqual(manifest["occurrences_replaced"], 3)

    def test_source_drift_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.patch_source(f"only {MODULE.OLD}\n")

    def test_positive_height_reflection_patch(self):
        source = f"prefix\n{MODULE.OLD_REFLECTION}suffix\n"
        output, manifest = MODULE.patch_positive_reflection(source)
        self.assertNotIn(MODULE.OLD_REFLECTION, output)
        self.assertIn(MODULE.NEW_REFLECTION, output)
        self.assertEqual(manifest["reflection_blocks_replaced"], 1)
        self.assertTrue(manifest["negative_height_rs_calls_removed"])

    def test_reflection_source_drift_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.patch_positive_reflection("no reflection block")


if __name__ == "__main__":
    unittest.main()

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
REVIEWED_SOURCE = ROOT.parent / "X-7501-xi-modulus" / "rs_modulus.c"


class PatcherTests(unittest.TestCase):
    def test_exact_three_occurrence_patch(self):
        source = REVIEWED_SOURCE.read_text(encoding="utf-8")
        output, manifest = MODULE.patch_source(source)
        self.assertEqual(output.count(MODULE.NEW), 3)
        self.assertNotIn(MODULE.OLD, output)
        self.assertEqual(manifest["occurrences_replaced"], 3)
        self.assertEqual(
            manifest["source_sha256"], MODULE.REVIEWED_SOURCE_SHA256
        )

    def test_source_drift_rejected(self):
        source = REVIEWED_SOURCE.read_text(encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "digest mismatch"):
            MODULE.patch_source(source + "\n")

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

    def test_exact_common_scale_patch(self):
        source = REVIEWED_SOURCE.read_text(encoding="utf-8")
        source, _ = MODULE.patch_source(source)
        source, _ = MODULE.patch_positive_reflection(source)
        output, manifest = MODULE.patch_common_xi_scale(source)
        self.assertIn(MODULE.SCALE_DECLARATION_REPLACEMENT, output)
        self.assertIn(MODULE.SCALE_VALUE_REPLACEMENT, output)
        self.assertIn(MODULE.SCALE_METADATA_REPLACEMENT, output)
        self.assertEqual(
            manifest["common_xi_scale_power_of_two"],
            MODULE.XI_COMMON_SCALE_POWER,
        )
        self.assertTrue(manifest["common_scale_is_exact"])

    def test_common_scale_source_drift_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.patch_common_xi_scale("no scale targets")


if __name__ == "__main__":
    unittest.main()

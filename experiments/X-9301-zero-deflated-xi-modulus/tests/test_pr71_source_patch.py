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

    def test_custom_ordinate_patch(self):
        custom = str(int(MODULE.NEW) + 1)
        source = (MODULE.OLD + "\n") * MODULE.EXPECTED_OCCURRENCES
        output, manifest = MODULE.patch_source(source, custom)
        self.assertEqual(output.count(custom), MODULE.EXPECTED_OCCURRENCES)
        self.assertEqual(manifest["new_ordinate_numerator"], custom)

    def test_original_ordinate_requires_no_replacement(self):
        source = (MODULE.OLD + "\n") * MODULE.EXPECTED_OCCURRENCES
        output, manifest = MODULE.patch_source(source, MODULE.OLD)
        self.assertEqual(output, source)
        self.assertEqual(manifest["occurrences_replaced"], 0)

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

    def test_common_scale_patch(self):
        source = (
            MODULE.SCALE_DECLARATION_NEEDLE
            + MODULE.SCALE_VALUE_NEEDLE
            + MODULE.SCALE_METADATA_NEEDLE
        )
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
            MODULE.patch_common_xi_scale("missing scale targets")

    def test_dense_x_grid_patch(self):
        bits = tuple(range(20, 4, -1))
        output, manifest = MODULE.patch_x_grid(MODULE.X_GRID_NEEDLE, bits)
        self.assertIn("#define X_COUNT 16", output)
        self.assertIn(", ".join(map(str, bits)), output)
        self.assertEqual(manifest["x_bits"], list(bits))

    def test_unsorted_x_grid_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "strictly decreasing"):
            MODULE.patch_x_grid(MODULE.X_GRID_NEEDLE, (20, 18, 19))


if __name__ == "__main__":
    unittest.main()

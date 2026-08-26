from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_boundary_field_finite_scout.py"
)
SPEC = importlib.util.spec_from_file_location("boundary_field_scout", MODULE_PATH)
assert SPEC and SPEC.loader
boundary_field_scout = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(boundary_field_scout)


class FfpsBoundaryFieldFiniteScoutTest(unittest.TestCase):
    def test_source_locks(self) -> None:
        boundary_field_scout.check_source_blobs()

    def test_boundary_kernel_is_compact(self) -> None:
        log_two = np.log(2.0)
        grid = np.array([-0.1, 0.1, 4.0 * log_two - 0.1, 4.0 * log_two + 0.1])
        values = boundary_field_scout.boundary_kernel(grid)
        self.assertEqual(float(values[0]), 0.0)
        self.assertNotEqual(float(values[1]), 0.0)
        self.assertNotEqual(float(values[2]), 0.0)
        self.assertEqual(float(values[3]), 0.0)

    def test_first_difference_matches_direct_mollification(self) -> None:
        control = boundary_field_scout.first_difference_control(10, 256)
        self.assertLess(control["maximum_relative_difference"], 1.0e-12)

    def test_jordan_identity_and_checkpoint(self) -> None:
        row = boundary_field_scout.run_panel(10, 256)["rows"][-1]
        self.assertAlmostEqual(row["jordan_residual"], row["signed_mass"], places=10)
        self.assertGreater(row["negative_mass"], 50.0)
        self.assertLess(row["negative_mass"], 70.0)

    def test_resolution_panels_are_close(self) -> None:
        coarse = boundary_field_scout.run_panel(10, 256)["rows"][-1]
        fine = boundary_field_scout.run_panel(10, 512)["rows"][-1]
        relative = (
            abs(coarse["negative_mass"] - fine["negative_mass"]) / fine["negative_mass"]
        )
        self.assertLess(relative, 0.003)

    def test_summary_scope_and_input_guards(self) -> None:
        summary = boundary_field_scout.rounded_summary()
        self.assertEqual(len(summary["checkpoints"]), 3)
        self.assertFalse("rh_proved" in summary)
        caps = summary["resource_caps"]
        self.assertEqual(caps["zero_searches"], 0)
        self.assertEqual(caps["source_construction_passes"], 3)
        self.assertEqual(caps["maximum_source_placement_visits"], 3 * (1 << 18))
        self.assertEqual(caps["maximum_source_grid_cells"], 9216)
        self.assertEqual(caps["maximum_validation_kernel_grid_cells"], 2304)
        self.assertEqual(caps["maximum_linear_convolution_cells"], 11519)
        self.assertEqual(caps["maximum_fft_length"], 16384)
        with self.assertRaises(ValueError):
            boundary_field_scout.rounded_summary(17)
        with self.assertRaises(ValueError):
            boundary_field_scout.run(10)
        with self.assertRaises(ValueError):
            boundary_field_scout.run_panel(True, 256)


if __name__ == "__main__":
    unittest.main()

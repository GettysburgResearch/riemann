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
    / "ffps_mollified_beta_finite_scout.py"
)
SPEC = importlib.util.spec_from_file_location("mollified_scout", MODULE_PATH)
assert SPEC and SPEC.loader
mollified_scout = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mollified_scout)


class FfpsMollifiedBetaFiniteScoutTest(unittest.TestCase):
    def test_beta_duplicate(self) -> None:
        beta = mollified_scout.beta_array(67 * 2)
        self.assertEqual(int(beta[1]), 1)
        self.assertEqual(int(beta[67]), -2)
        self.assertEqual(int(beta[134]), 2)

    def test_kernel_has_numerically_zero_mass(self) -> None:
        panel = mollified_scout.run_panel(8, 128)
        self.assertLess(abs(panel["kernel_integral_midpoint"]), 1.0e-10)

    def test_resolution_panels_are_close(self) -> None:
        coarse = mollified_scout.run_panel(10, 256)["rows"][-1]
        fine = mollified_scout.run_panel(10, 512)["rows"][-1]
        relative = (
            abs(coarse["negative_mass"] - fine["negative_mass"]) / fine["negative_mass"]
        )
        self.assertLess(relative, 0.005)

    def test_raw_lower_bound_overtakes_mollified_mass(self) -> None:
        row = mollified_scout.run_panel(12, 128)["rows"][-1]
        self.assertLess(row["mollified_to_raw_lower_ratio"], 0.3)

    def test_fft_matches_direct_convolution(self) -> None:
        left = np.array([1.0, -2.0, 3.0])
        right = np.array([4.0, 5.0])
        np.testing.assert_allclose(
            mollified_scout.fft_convolution(left, right),
            np.convolve(left, right),
            rtol=1.0e-12,
            atol=1.0e-12,
        )


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

import mpmath as mp


MODULE_PATH = Path(__file__).resolve().parents[1] / "prototype.py"
SPEC = importlib.util.spec_from_file_location("xi_passivity_prototype", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PassivityPrototypeTests(unittest.TestCase):
    def setUp(self) -> None:
        mp.mp.dps = 70

    def test_online_synthetic_scalar_positivity(self) -> None:
        zeros = [
            mp.mpc("0.5", "14"),
            mp.mpc("0.5", "-14"),
            mp.mpc("0.5", "21"),
            mp.mpc("0.5", "-21"),
        ]
        for point in [mp.mpc("0.51", "0"), mp.mpc("0.55", "14"), mp.mpc("0.9", "30")]:
            value = MODULE.logderivative_from_zeros(point, zeros)
            self.assertGreater(mp.re(value), 0)

    def test_online_synthetic_pick_kernel_is_positive(self) -> None:
        zeros = [
            mp.mpc("0.5", "14"),
            mp.mpc("0.5", "-14"),
            mp.mpc("0.5", "21"),
            mp.mpc("0.5", "-21"),
            mp.mpc("0.5", "25"),
            mp.mpc("0.5", "-25"),
        ]
        points = [mp.mpc("0.55", "10"), mp.mpc("0.60", "17"), mp.mpc("0.70", "24")]
        values = [MODULE.logderivative_from_zeros(s, zeros) for s in points]
        matrix = MODULE.pick_matrix(points, values)
        self.assertGreater(MODULE.smallest_hermitian_eigenvalue(matrix), mp.mpf("1e-8"))

    def test_offline_synthetic_orbit_triggers_scalar_and_matrix_violation(self) -> None:
        zeros = [
            mp.mpc("0.6", "20"),
            mp.mpc("0.6", "-20"),
            mp.mpc("0.4", "20"),
            mp.mpc("0.4", "-20"),
        ]
        points = [mp.mpc("0.55", "20"), mp.mpc("0.54", "19.9")]
        values = [MODULE.logderivative_from_zeros(s, zeros) for s in points]
        self.assertLess(mp.re(values[0]), -10)
        matrix = MODULE.pick_matrix(points, values)
        self.assertLess(MODULE.smallest_hermitian_eigenvalue(matrix), -100)

    def test_kernel_is_hermitian(self) -> None:
        points = [mp.mpc("0.6", "2"), mp.mpc("0.7", "3")]
        values = [mp.mpc("1", "2"), mp.mpc("3", "-1")]
        matrix = MODULE.pick_matrix(points, values)
        for j in range(matrix.rows):
            for k in range(matrix.cols):
                self.assertLess(abs(matrix[j, k] - mp.conj(matrix[k, j])), mp.mpf("1e-60"))

    def test_completed_logderivative_functional_equation(self) -> None:
        s = mp.mpc("0.73", "12.5")
        residual = MODULE.xi_logderivative(1 - s) + MODULE.xi_logderivative(s)
        self.assertLess(abs(residual), mp.mpf("1e-60"))

    def test_low_height_calibration_real_parts_are_positive(self) -> None:
        points = [mp.mpc("0.51", "0"), mp.mpc("0.51", "5"), mp.mpc("0.51", "10")]
        for point in points:
            self.assertGreater(mp.re(MODULE.xi_logderivative(point)), 0)

    def test_rejects_wrong_half_plane(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.pick_matrix([mp.mpc("0.5", "1")], [mp.mpc(1)])


if __name__ == "__main__":
    unittest.main()

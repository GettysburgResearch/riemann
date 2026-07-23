import unittest
import numpy as np
from scipy.linalg import toeplitz
from exact_vector import midpoint_rayleigh_from_lags


class ScalarizationTests(unittest.TestCase):
    def test_lag_scalarization(self):
        coefficients = np.array(
            [2 + 0j, 3 + 5j, -1 + 2j], dtype=np.complex128
        )
        row = np.array(
            [coefficients[0].real, 0.5 * coefficients[1], 0.5 * coefficients[2]],
            dtype=np.complex128,
        )
        matrix = toeplitz(np.conj(row), row)
        real = [2, -1, 3]
        imag = [1, 4, -2]
        bits = 3
        vector = np.array(
            [
                complex(a / (1 << bits), b / (1 << bits))
                for a, b in zip(real, imag)
            ]
        )
        direct = float(np.vdot(vector, matrix @ vector).real)
        scalar = midpoint_rayleigh_from_lags(
            coefficients, real, imag, bits
        )
        self.assertAlmostEqual(direct, scalar, places=14)


if __name__ == "__main__":
    unittest.main()

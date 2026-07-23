from pathlib import Path
import sys
import unittest

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from compact_corrections import (  # noqa: E402
    arch_compact_normalized,
    arch_triangular_cancellation_safe,
    autocorrelation_normalized,
    pole_compact_normalized,
    pole_finite_normalized,
)


class CompactCorrectionTests(unittest.TestCase):
    def test_autocorrelation_knots(self):
        v = [1 / mp.sqrt(2), 1j / mp.sqrt(2)]
        L = mp.log(17)
        self.assertAlmostEqual(float(mp.re(autocorrelation_normalized(0, v, L))), 1.0, places=14)
        self.assertLess(abs(autocorrelation_normalized(2 * L, v, L)), mp.mpf("1e-40"))

    def test_pole_compact_matches_finite_cell_transform(self):
        with mp.workdps(60):
            v = [mp.mpc("0.4", "0.1"), mp.mpc("-0.3", "0.2"), mp.mpc("0.5", "-0.4")]
            norm = mp.sqrt(mp.fsum(abs(x) ** 2 for x in v))
            v = [x / norm for x in v]
            L = mp.log(101)
            T = mp.mpf("13.25")
            compact = pole_compact_normalized(v, L, T, dps=60)
            finite = pole_finite_normalized(v, L, T, dps=60)
            self.assertLess(abs(compact - finite), mp.mpf("1e-48"))

    def test_archimedean_k1_matches_cancellation_safe_formula(self):
        with mp.workdps(60):
            L = mp.log(101)
            T = mp.mpf("17.75")
            compact = arch_compact_normalized([1], L, T, dps=60)
            scalar = arch_triangular_cancellation_safe(L, T, dps=60)
            self.assertLess(abs(compact - scalar), mp.mpf("1e-48"))


if __name__ == "__main__":
    unittest.main()

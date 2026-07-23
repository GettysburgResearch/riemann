import pathlib
import sys
import unittest

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from xi_jets import simultaneous_zeta_jet, stieltjes_moments, xi_logderivative_jet


class RiemannSiegelJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mp.mp.dps = 20
        cls.s = mp.mpf("0.61") + mp.j * mp.mpf("1000000")
        cls.zeta_jet = simultaneous_zeta_jet(cls.s, 4)

    def test_zeta_jet_against_independent_diff(self) -> None:
        for order, value in enumerate(self.zeta_jet):
            reference = mp.diff(lambda w: mp.zeta(w), self.s, order)
            relative = abs(value - reference) / max(1, abs(reference))
            self.assertLess(relative, mp.mpf("2e-12"))

    def test_localizer_scalar_identity(self) -> None:
        f_jet, _ = xi_logderivative_jet(self.s, 3)
        x = mp.re(self.s) - mp.mpf("0.5")
        moments = stieltjes_moments(f_jet, x, 3)
        b00 = moments[0] - x * x * moments[1]
        differential = mp.re(f_jet[1]) + mp.re(f_jet[0]) / x
        self.assertLess(abs(2 * b00 - differential), mp.mpf("1e-12"))


if __name__ == "__main__":
    unittest.main()

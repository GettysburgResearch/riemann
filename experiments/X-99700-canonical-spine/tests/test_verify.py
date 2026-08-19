from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x99700_verify", HERE / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class ExactReplayTests(unittest.TestCase):
    def test_inverse_convolution(self) -> None:
        self.assertEqual(MOD.conv_beta_g_limit(1000), 1000)

    def test_owner_identity(self) -> None:
        self.assertGreater(MOD.owner_identity_limit(1000), 0)

    def test_symmetric_homotopy(self) -> None:
        out = MOD.symmetric_homotopy_check([F(1, 3), F(1, 5), F(1, 7)])
        self.assertEqual(out["monomials"], 8)

    def test_alpha_firewall(self) -> None:
        out = MOD.alpha_firewall()
        self.assertEqual(out["contracted_net_shift"], "0")
        self.assertNotEqual(out["native_shift"], "0")

    def test_smoothing_factor(self) -> None:
        self.assertEqual(MOD.smoothing_local_factor_check()["coefficient_checks"], 44)


if __name__ == "__main__":
    unittest.main()

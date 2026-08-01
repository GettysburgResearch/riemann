from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x16202_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class FourGateReductionTests(unittest.TestCase):
    def test_repaired_packet(self):
        result = module.repaired_packet_control()
        self.assertTrue(result["raw_modes_have_poisson_power_corrections"])
        self.assertEqual(len(result["repaired_ldl_pivots"]), 2)

    def test_energy_angle(self):
        result = module.energy_angle_control()
        self.assertEqual(result["complete_gap_lower_bound"], "1")
        self.assertEqual(result["global_floor"], "0")

    def test_scalarization(self):
        result = module.scalarization_control()
        self.assertEqual(result["epsilon"], "1/10")
        self.assertGreater(module.F(result["complete_gap_lower_bound"]), 0)

    def test_complete(self):
        result = module.verify()
        self.assertEqual(result["schema"], module.SCHEMA)

    def test_bad_radical_basis_detected(self):
        q = [module.F(1)] * 4
        bad = [module.F(1), module.F(-2), module.F(0), module.F(0)]
        self.assertNotEqual(sum(q[i] * bad[i] for i in range(4)), 0)

    def test_bad_energy_angle_rejected(self):
        s0 = module.diagonal([module.F(1), module.F(4)])
        x = [[module.F(3)], [module.F(3)]]
        b = module.F(1)
        k = module.F(1, 2)
        margin = module.mat_sub(
            [[k * k * v for v in row] for row in s0],
            [[x[i][0] * x[j][0] / b for j in range(2)] for i in range(2)],
        )
        with self.assertRaises(module.CertificateError):
            module.require_pd(margin, "bad margin")

    def test_zero_touch_not_strict(self):
        with self.assertRaises(module.CertificateError):
            module.require_pd([[module.F(1), module.F(1)],
                               [module.F(1), module.F(1)]], "touching")

    def test_boolean_not_used_as_fraction(self):
        self.assertIsNot(True, module.F(1))


if __name__ == "__main__":
    unittest.main()

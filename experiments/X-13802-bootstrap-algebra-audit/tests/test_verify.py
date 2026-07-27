from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bootstrap_audit", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class BootstrapAuditTests(unittest.TestCase):
    def test_hermite_inertia(self):
        result = module.hermite_x2_plus_1()
        self.assertEqual(result["signature"], 0)
        self.assertEqual(result["refuted_formula_value"], -1)
        self.assertEqual(result["determinant"], -4)

    def test_targeted_li_first_coefficient_is_complex(self):
        result = module.targeted_li_first_coefficient()
        self.assertEqual(result["analytic_taylor_coefficient"]["imag"], "4")
        self.assertFalse(result["equal"])

    def test_classical_li_factor_two(self):
        result = module.classical_li_modulus_constant()
        self.assertNotEqual(
            result["correct_first_order_modulus_increment"],
            result["refuted_first_order_modulus_increment"],
        )

    def test_complete_verification(self):
        result = module.verify()
        self.assertEqual(result["schema"], module.SCHEMA)
        self.assertEqual(
            result["classification"], "EXACT_SYNTHETIC_ALGEBRA_AUDIT"
        )


if __name__ == "__main__":
    unittest.main()

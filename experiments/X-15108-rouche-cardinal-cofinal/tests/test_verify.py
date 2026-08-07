import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def base():
    return json.loads((ROOT / "certificates" / "synthetic-pass.json").read_text())


class RoucheCardinalFiniteGateTests(unittest.TestCase):
    def test_exact_pass(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_ROUCHE_CARDINAL_ARITHMETIC_COMPLETION")
        self.assertEqual(out["maximum_normalized_loss_upper"], {"numerator": 3, "denominator": 125})
        self.assertEqual(
            out["residue_margin_lower"],
            [
                {"numerator": 244, "denominator": 125},
                {"numerator": 2943, "denominator": 1000},
            ],
        )

    def test_rouche_touch_rejected(self):
        data = base()
        data["transform_boundary_error_upper"][0] = 1
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_zero_derivative_rejected(self):
        data = base()
        data["xi_derivative_lower"][0] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_mass_interval_rejected(self):
        data = base()
        data["phase_mass_upper"][0] = 1
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_large_residual_rejected(self):
        data = base()
        data["residual_residue_upper"][0] = 3
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_large_cardinal_derivative_rejected(self):
        data = base()
        data["cardinal_derivative_upper"][0][0] = 300
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["physical_node_spacing"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_dimension_mismatch_rejected(self):
        data = base()
        data["phase_mass_lower"] = [2]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()

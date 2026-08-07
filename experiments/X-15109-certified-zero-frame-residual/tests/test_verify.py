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


class CertifiedZeroFrameResidualTests(unittest.TestCase):
    def test_exact_pass(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_ZERO_FRAME_RESIDUAL_ARITHMETIC_COMPLETION")
        self.assertEqual(out["final_margin_scalar"], {"numerator": 59, "denominator": 4})
        self.assertEqual(out["selected_coordinate_ratios"], [0, 0, 0])

    def test_excessive_frame_floor_rejected(self):
        data = base()
        data["frame_floor"] = 16
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_selected_residual_rejected(self):
        data = base()
        data["selected_atoms"][0]["weight"] = {"numerator": 21, "denominator": 10}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_small_complete_residual_radius_rejected(self):
        data = base()
        data["complete_residual_radius"] = {"numerator": 1, "denominator": 5}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_failed_final_ratio_rejected(self):
        data = base()
        data["complete_residual_radius"] = 15
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_target_normalization_rejected(self):
        data = base()
        data["p"][0] = {"numerator": 1, "denominator": 2}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_nonpositive_selected_atom_rejected(self):
        data = base()
        data["selected_atoms"][0]["weight"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["frame_floor"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()

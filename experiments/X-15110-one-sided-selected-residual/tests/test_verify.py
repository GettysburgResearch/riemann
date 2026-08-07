import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def base():
    return json.loads((ROOT / "certificates" / "one-sided-pass.json").read_text())


class OneSidedResidualTests(unittest.TestCase):
    def test_pass(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_ONE_SIDED_RESIDUAL_COMPLETION")
        self.assertEqual(out["absolute_residual_radius_lower_witness"], 100)
        self.assertEqual(out["strict_margin"], 1)

    def test_old_absolute_gate_really_fails(self):
        out = VERIFY.verify(base())
        self.assertGreater(
            VERIFY.rat(out["absolute_residual_radius_lower_witness"]),
            VERIFY.rat(out["selected_floor"]),
        )

    def test_too_small_residual_radius_rejected(self):
        data = base()
        data["residual_negative_radius"] = {"numerator": 1, "denominator": 2}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_too_large_selected_floor_rejected(self):
        data = base()
        data["selected_floor"] = 4
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_no_strict_margin_rejected(self):
        data = base()
        data["residual_negative_radius"] = data["selected_floor"]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_kernel_drift_rejected(self):
        data = base()
        data["residual_pinned"][0][0] = 50
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["selected_floor"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_witness_rejected(self):
        data = base()
        data["absolute_witness"] = [1, 1, 1]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()

import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def base():
    return json.loads((ROOT / "certificates" / "selected-zero-pass.json").read_text())


class CertifiedZeroCardinalResidueTests(unittest.TestCase):
    def test_exact_pass(self):
        out = VERIFY.verify(base())
        self.assertEqual(out["status"], "CERTIFIED_SELECTED_ZERO_CARDINAL_RESIDUE_FLOOR")
        self.assertEqual(
            out["complete_residue_weights"],
            [
                {"numerator": 79, "denominator": 40},
                {"numerator": 119, "denominator": 40},
            ],
        )
        self.assertEqual(out["selected_residue_sums"], [2, 3])

    def test_pairing_swap_rejected_by_capture(self):
        data = base()
        data["selected_atoms"][0]["pair_root"] = 1
        data["selected_atoms"][1]["pair_root"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_large_residual_rejected(self):
        data = base()
        data["residual_atoms"][0]["weight"] = 100
        data["residual_atoms"][1]["weight"] = 100
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_negative_boundary_rejected(self):
        data = base()
        data["boundary_scalar"] = -100
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_repeated_root_rejected(self):
        data = base()
        data["roots"][1] = copy.deepcopy(data["roots"][0])
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_bad_normalization_rejected(self):
        data = base()
        data["p"][0] = {"numerator": 1, "denominator": 2}
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_rejected(self):
        data = base()
        data["selected_atoms"][0]["weight"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_duplicate_pair_rejected(self):
        data = base()
        data["selected_atoms"][1]["pair_root"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()

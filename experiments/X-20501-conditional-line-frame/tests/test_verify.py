from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x20501_verify", HERE / "verify.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class TestConditionalLineFrame(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = json.loads((HERE / "certificates" / "synthetic.json").read_text())
        cls.positive_residual = json.loads((HERE / "certificates" / "positive-residual.json").read_text())

    def verify(self, data):
        return MODULE.verify(copy.deepcopy(data))

    def assert_rejected(self, data):
        with self.assertRaises(MODULE.VerificationError):
            self.verify(data)

    def test_baseline(self):
        result = self.verify(self.certificate)
        self.assertTrue(result["verified"])
        self.assertEqual(result["verdict"], "CERTIFIED_CONDITIONAL_LINE_FRAME_KERNEL_FLOOR")
        self.assertEqual(result["corrected_floor"], {"numerator": 3191, "denominator": 3400})

    def test_large_positive_residual_is_harmless(self):
        result = self.verify(self.positive_residual)
        self.assertEqual(result["residual_negative_bound"], {"numerator": 0, "denominator": 1})
        self.assertEqual(result["corrected_floor"], {"numerator": 3551, "denominator": 3400})

    def test_singular_first_frame(self):
        data = copy.deepcopy(self.certificate)
        data["evaluation_Z"]["W"][0][0] = "0"
        self.assert_rejected(data)

    def test_conditional_schur_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["conditional_S"][0][0] = "2/3"
        self.assert_rejected(data)

    def test_frame_lower_too_large(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["frame_lower"] = "19/17"
        self.assert_rejected(data)

    def test_residual_bound_too_small(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["residual_negative_bound"] = "1/10"
        data["claimed"]["corrected_floor"] = str(
            MODULE.parse_fraction(data["claimed"]["frame_lower"])
            - MODULE.parse_fraction(data["claimed"]["residual_negative_bound"])
            - MODULE.parse_fraction(data["claimed"]["schur_cross_bound"])
        )
        self.assert_rejected(data)

    def test_cross_bound_too_small(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["schur_cross_bound"] = "1/100"
        data["claimed"]["corrected_floor"] = str(
            MODULE.parse_fraction(data["claimed"]["frame_lower"])
            - MODULE.parse_fraction(data["claimed"]["residual_negative_bound"])
            - MODULE.parse_fraction(data["claimed"]["schur_cross_bound"])
        )
        self.assert_rejected(data)

    def test_hardy_tail_floor_too_large(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["hardy_tail_floor"] = "7/17"
        self.assert_rejected(data)

    def test_metric_not_positive(self):
        data = copy.deepcopy(self.certificate)
        data["metric_W"][0][0] = "-1"
        self.assert_rejected(data)

    def test_full_determinant_mutation(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["full_evaluation_determinant"] = "-4/3"
        self.assert_rejected(data)

    def test_boolean_rejected(self):
        data = copy.deepcopy(self.certificate)
        data["claimed"]["frame_lower"] = True
        self.assert_rejected(data)


if __name__ == "__main__":
    unittest.main()

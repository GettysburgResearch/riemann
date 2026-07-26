import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "positive_node_verify", ROOT / "verify.py"
)
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)
CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class PositiveNodeTests(unittest.TestCase):
    def test_three_exact_cases(self):
        result = VERIFY.verify(copy.deepcopy(CERT))
        self.assertEqual(result["case_count"], 3)
        self.assertEqual(result["negative_case_count"], 2)
        self.assertEqual(
            result["cases"][0]["status"],
            "CERTIFIED_INSIDE_ONE_SCALAR_INTERVAL",
        )
        self.assertEqual(
            result["cases"][1]["status"],
            "CERTIFIED_NEGATIVE_LOWER_SQUARE_WITNESS",
        )
        self.assertEqual(
            result["cases"][2]["status"],
            "CERTIFIED_NEGATIVE_UPPER_Y_SQUARE_WITNESS",
        )

    def test_recurrence_identity(self):
        result = VERIFY.verify(copy.deepcopy(CERT))["cases"][0]
        old = [
            VERIFY.rat(value, "a")
            for value in CERT["cases"][0]["old_moments"]
        ]
        moments = [VERIFY.rat(value, "b") for value in result["new_moments"]]
        w = VERIFY.rat(CERT["cases"][0]["w"], "w")
        self.assertEqual(
            old,
            [moments[k + 1] + w * moments[k] for k in range(len(old))],
        )

    def test_lower_witness_is_exact(self):
        result = VERIFY.verify(copy.deepcopy(CERT))["cases"][1]
        value = VERIFY.rat(result["lower_witness_value"], "value")
        gap = VERIFY.rat(result["lower_gap"], "gap")
        self.assertEqual(value, gap)
        self.assertLess(value, 0)

    def test_upper_witness_is_exact(self):
        result = VERIFY.verify(copy.deepcopy(CERT))["cases"][2]
        value = VERIFY.rat(result["upper_witness_yq2_value"], "value")
        gap = VERIFY.rat(result["upper_gap"], "gap")
        w = VERIFY.rat(result["w"], "w")
        self.assertEqual(value, w * gap)
        self.assertLess(value, 0)

    def test_nonpositive_node_rejected(self):
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["w"] = {"numerator": 0, "denominator": 1}
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(mutated)

    def test_even_moment_count_rejected(self):
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["old_moments"].pop()
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(mutated)

    def test_false_expected_status_rejected(self):
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["expected_status"] = (
            "CERTIFIED_NEGATIVE_LOWER_SQUARE_WITNESS"
        )
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(mutated)

    def test_boolean_integer_rejected(self):
        mutated = copy.deepcopy(CERT)
        mutated["cases"][0]["new_b0"]["numerator"] = True
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(mutated)


if __name__ == "__main__":
    unittest.main()

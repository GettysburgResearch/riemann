from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def load(name: str):
    return json.loads((ROOT / "certificates" / name).read_text(encoding="utf-8"))


class CompletionTests(unittest.TestCase):
    def test_feasible_completion_with_empty_graph_interval(self):
        result = VERIFY.verify(load("feasible-graph-empty.json"))
        self.assertEqual(result["verdict"], "CERTIFIED_STRICT_TARGET_PINNED_COMPLETION")
        self.assertFalse(result["graph_separator"]["interval_nonempty"])
        self.assertFalse(result["graph_separator"]["all_weights_nonnegative_at_c"])
        self.assertEqual(
            [(item["numerator"], item["denominator"]) for item in result["complement_ldl_pivots"]],
            [(26, 1), (6075, 104), (48, 1)],
        )

    def test_null_obstruction(self):
        result = VERIFY.verify(load("infeasible-null.json"))
        self.assertEqual(
            result["verdict"], "CERTIFIED_NO_STRICT_COMPLETION_NULL_DIRECTION"
        )
        self.assertEqual(result["x_A_x"]["numerator"], 0)
        self.assertEqual(result["x_B_x"]["numerator"], 0)

    def test_pair_obstruction(self):
        result = VERIFY.verify(load("infeasible-pair.json"))
        self.assertEqual(
            result["verdict"], "CERTIFIED_NO_STRICT_COMPLETION_THRESHOLD_CONFLICT"
        )
        self.assertEqual(
            result["positive_direction"]["strict_lower_c"],
            result["negative_direction"]["strict_upper_c"],
        )

    def test_bad_scalar_rejected(self):
        data = load("feasible-graph-empty.json")
        data["c"] = 1000
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_normalization_drift_rejected(self):
        data = load("feasible-graph-empty.json")
        data["p"][0] = 2
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_boolean_rational_rejected(self):
        data = load("feasible-graph-empty.json")
        data["c"] = True
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_false_null_direction_rejected(self):
        data = load("infeasible-null.json")
        data["x"] = [1, -1, 0, 0]
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_wrong_pair_signs_rejected(self):
        data = load("infeasible-pair.json")
        data["x_minus"] = data["x_plus"]
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_asymmetry_rejected(self):
        data = load("feasible-graph-empty.json")
        data["Q"][0][1] += 1
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify(data)

    def test_slope_inertia(self):
        result = VERIFY.verify(load("feasible-graph-empty.json"))
        self.assertEqual(
            result["slope_inertia"],
            {
                "positive_on_full_space": 1,
                "negative_on_full_space": 2,
                "zero_on_full_space": 1,
                "positive_on_complement": 1,
                "negative_on_complement": 2,
            },
        )


if __name__ == "__main__":
    unittest.main()

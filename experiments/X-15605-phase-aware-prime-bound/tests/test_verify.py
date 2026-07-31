from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


def load() -> dict:
    return json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class TestPhaseAwarePrimeBound(unittest.TestCase):
    def test_synthetic_violation(self) -> None:
        result = verify.verify(load())
        self.assertEqual(result["verdict"], "CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_POSITIVE")
        self.assertEqual(result["total_budget"], {"numerator": "43", "denominator": "100"})

    def test_negative_violation(self) -> None:
        data = load()
        data["prime_interval"] = {
            "lower": {"numerator": -51, "denominator": 5},
            "upper": {"numerator": -101, "denominator": 10},
        }
        data["phase_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 0, "denominator": 1},
        }
        self.assertEqual(
            verify.verify(data)["verdict"],
            "CERTIFIED_OFFLINE_ZERO_BOUND_VIOLATION_NEGATIVE",
        )

    def test_inside_band(self) -> None:
        data = load()
        data["prime_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 1, "denominator": 10},
        }
        data["phase_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 0, "denominator": 1},
        }
        self.assertEqual(
            verify.verify(data)["verdict"], "FINITE_VALUE_CONSISTENT_WITH_RH_BOUND"
        )

    def test_boundary_overlap(self) -> None:
        data = load()
        data["prime_interval"] = {
            "lower": {"numerator": 2, "denominator": 5},
            "upper": {"numerator": 1, "denominator": 2},
        }
        data["phase_interval"] = {
            "lower": {"numerator": 0, "denominator": 1},
            "upper": {"numerator": 0, "denominator": 1},
        }
        self.assertEqual(verify.verify(data)["verdict"], "UNRESOLVED_BOUNDARY_OVERLAP")

    def test_selected_count_excess_rejected(self) -> None:
        data = load()
        data["shells"][0]["selected_multiplicity"] = 4
        with self.assertRaises(ValueError):
            verify.verify(data)

    def test_overlap_rejected(self) -> None:
        data = load()
        second = copy.deepcopy(data["shells"][0])
        second["left"] = {"numerator": 9, "denominator": 1}
        second["right"] = {"numerator": 11, "denominator": 1}
        data["shells"].append(second)
        with self.assertRaises(ValueError):
            verify.verify(data)

    def test_boolean_rejected(self) -> None:
        data = load()
        data["shells"][0]["selected_multiplicity"] = True
        with self.assertRaises(ValueError):
            verify.verify(data)

    def test_reversed_interval_rejected(self) -> None:
        data = load()
        data["prime_interval"]["lower"] = {"numerator": 20, "denominator": 1}
        with self.assertRaises(ValueError):
            verify.verify(data)


if __name__ == "__main__":
    unittest.main()

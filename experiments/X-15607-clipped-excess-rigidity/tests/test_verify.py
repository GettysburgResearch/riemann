from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify import verify  # noqa: E402


class ClippedExcessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base = {
            "schema": "riemann.clipped-excess-rigidity.v1",
            "G": "3",
            "alpha": "1",
            "theta": "1",
            "eta": "1/4",
            "D": ["2", "2", "6/5", "1/2"],
            "A": ["1", "1", "9/5", "5/2"],
            "packet_indices": [0, 1],
        }

    def test_exact_control_passes(self) -> None:
        result = verify(copy.deepcopy(self.base))
        self.assertEqual(result["excess"], "1/5")
        self.assertEqual(result["count_above_theta_plus_eta"], 2)
        self.assertEqual(result["certified_complement_floor"], "9/5")

    def test_zero_excess_flat_band(self) -> None:
        data = copy.deepcopy(self.base)
        data["D"] = ["2", "2", "1/2"]
        data["A"] = ["1", "1", "5/2"]
        result = verify(data)
        self.assertEqual(result["excess"], "0")
        self.assertTrue(result["flat_band"])

    def test_rejects_boolean(self) -> None:
        data = copy.deepcopy(self.base)
        data["G"] = True
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_duplicate_packet_index(self) -> None:
        data = copy.deepcopy(self.base)
        data["packet_indices"] = [0, 0]
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_packet_not_low(self) -> None:
        data = copy.deepcopy(self.base)
        data["A"][0] = "3/2"
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_false_lower_symbol(self) -> None:
        data = copy.deepcopy(self.base)
        data["A"][2] = "1"
        with self.assertRaises(ValueError):
            verify(data)

    def test_small_eta_detects_extra_mode(self) -> None:
        data = copy.deepcopy(self.base)
        data["eta"] = "1/10"
        result = verify(data)
        self.assertEqual(result["count_above_theta_plus_eta"], 3)
        self.assertEqual(result["excess"], "1/5")

    def test_rejects_invalid_theta(self) -> None:
        data = copy.deepcopy(self.base)
        data["theta"] = "2"
        with self.assertRaises(ValueError):
            verify(data)


if __name__ == "__main__":
    unittest.main()

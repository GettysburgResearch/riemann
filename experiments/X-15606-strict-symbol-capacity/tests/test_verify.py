from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify import verify

BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class StrictCapacityTests(unittest.TestCase):
    def test_exact_control_passes(self):
        self.assertEqual(verify(copy.deepcopy(BASE))["verdict"], "PASS")

    def test_rejects_boolean_rational(self):
        data = copy.deepcopy(BASE)
        data["Gamma"] = True
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_duplicate_packet_index(self):
        data = copy.deepcopy(BASE)
        data["packet_indices"] = [0, 0]
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_nonpositive_deficit(self):
        data = copy.deepcopy(BASE)
        data["D"][1][1] = "0"
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_packet_not_low(self):
        data = copy.deepcopy(BASE)
        data["A"][0][0] = "1"
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_false_trace_claim(self):
        data = copy.deepcopy(BASE)
        data["claimed_trace_D"] = "2"
        with self.assertRaises(ValueError):
            verify(data)

    def test_rejects_false_floor(self):
        data = copy.deepcopy(BASE)
        data["claimed_complement_floor"] = "7/4"
        with self.assertRaises(ValueError):
            verify(data)


if __name__ == "__main__":
    unittest.main()

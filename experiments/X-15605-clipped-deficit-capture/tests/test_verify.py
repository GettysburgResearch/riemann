import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify  # noqa: E402


CERT = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class ClippedDeficitTests(unittest.TestCase):
    def test_exact_control_passes(self):
        out = verify(copy.deepcopy(CERT))
        self.assertEqual(out["verdict"], "PASS")
        self.assertEqual(out["full_trace_gate"], "FAIL")
        self.assertEqual(out["clipped_gate"], "PASS")
        self.assertEqual(out["exact_complement_floor"], "7/5")

    def test_rejects_boolean_rational(self):
        bad = copy.deepcopy(CERT)
        bad["G"] = True
        with self.assertRaises(ValueError):
            verify(bad)

    def test_rejects_packet_not_low(self):
        bad = copy.deepcopy(CERT)
        bad["packet_indices"] = [0, 2]
        with self.assertRaises(ValueError):
            verify(bad)

    def test_rejects_insufficient_packet_capture(self):
        bad = copy.deepcopy(CERT)
        bad["deficit_eigenvalues"][1] = "3/2"
        with self.assertRaises(ValueError):
            verify(bad)

    def test_rejects_extra_deep_complement_mode(self):
        bad = copy.deepcopy(CERT)
        bad["deficit_eigenvalues"][2] = "3/2"
        with self.assertRaises(ValueError):
            verify(bad)

    def test_rejects_floor_above_actual_complement(self):
        bad = copy.deepcopy(CERT)
        bad["Gamma"] = "399/200"
        with self.assertRaises(ValueError):
            verify(bad)

    def test_rejects_duplicate_packet_index(self):
        bad = copy.deepcopy(CERT)
        bad["packet_indices"] = [0, 0]
        with self.assertRaises(ValueError):
            verify(bad)


if __name__ == "__main__":
    unittest.main()

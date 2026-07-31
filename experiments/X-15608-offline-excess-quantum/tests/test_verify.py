import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)
BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class ExcessQuantumTests(unittest.TestCase):
    def test_exact_control_passes(self):
        self.assertEqual(VERIFY.verify(copy.deepcopy(BASE))["clipped_excess"], "3/5")

    def test_rejects_boolean_rational(self):
        bad = copy.deepcopy(BASE)
        bad["G"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_duplicate_index(self):
        bad = copy.deepcopy(BASE)
        bad["extra_low_indices"] = [1]
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_packet_not_low(self):
        bad = copy.deepcopy(BASE)
        bad["D_diagonal"][0] = "1"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_extra_direction_at_threshold(self):
        bad = copy.deepcopy(BASE)
        bad["D_diagonal"][2] = "5/2"  # A=t, not strictly below t
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_empty_extra_block(self):
        bad = copy.deepcopy(BASE)
        bad["extra_low_indices"] = []
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)


if __name__ == "__main__":
    unittest.main()

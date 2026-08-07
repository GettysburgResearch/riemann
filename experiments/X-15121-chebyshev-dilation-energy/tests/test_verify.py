from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify  # noqa: E402

BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class TestVerifier(unittest.TestCase):
    def test_pass(self):
        out = verify(copy.deepcopy(BASE))
        self.assertEqual(
            out["verdict"], "CERTIFIED_EXACT_DILATION_GRAM_IDENTITY"
        )
        self.assertEqual(out["energy"], out["independent_cell_energy"])

    def test_boolean_rejected(self):
        bad = copy.deepcopy(BASE)
        bad["Y"] = True
        with self.assertRaises(ValueError):
            verify(bad)

    def test_bad_scale_rejected(self):
        bad = copy.deepcopy(BASE)
        bad["scale"] = "1"
        with self.assertRaises(ValueError):
            verify(bad)

    def test_duplicate_rejected(self):
        bad = copy.deepcopy(BASE)
        bad["weights"][1]["n"] = 2
        with self.assertRaises(ValueError):
            verify(bad)

    def test_negative_weight_rejected(self):
        bad = copy.deepcopy(BASE)
        bad["weights"][0]["weight"] = "-1"
        with self.assertRaises(ValueError):
            verify(bad)

    def test_node_outside_rejected(self):
        bad = copy.deepcopy(BASE)
        bad["weights"][0]["n"] = 100
        with self.assertRaises(ValueError):
            verify(bad)


if __name__ == "__main__":
    unittest.main()

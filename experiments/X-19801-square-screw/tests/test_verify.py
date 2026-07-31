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


class SquareScrewTests(unittest.TestCase):
    def test_exact_control_passes(self):
        out = VERIFY.verify(copy.deepcopy(BASE))
        self.assertEqual(out["total"], ["23/20", "51/40"])
        self.assertEqual(out["verdict"], "CERTIFIED_NONNEGATIVE_SQUARE_LEVEL")

    def test_rejects_boolean_rational(self):
        bad = copy.deepcopy(BASE)
        bad["prime_terms"][0]["lower"] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_duplicate_index(self):
        bad = copy.deepcopy(BASE)
        bad["prime_terms"][1]["n"] = 2
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_wrong_cutoff(self):
        bad = copy.deepcopy(BASE)
        bad["manifest"]["cutoff"] = 5
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_untyped_completeness(self):
        bad = copy.deepcopy(BASE)
        bad["manifest"]["completeness"] = "ASSUMED"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_rejects_false_total(self):
        bad = copy.deepcopy(BASE)
        bad["claimed_total"]["lower"] = "1"
        with self.assertRaises(ValueError):
            VERIFY.verify(bad)

    def test_negative_interval_is_violation(self):
        bad = copy.deepcopy(BASE)
        bad["prime_terms"][0]["lower"] = "2"
        bad["prime_terms"][0]["upper"] = "2"
        bad.pop("claimed_total")
        out = VERIFY.verify(bad)
        self.assertEqual(out["verdict"], "CERTIFIED_NEGATIVE_RH_VIOLATION")

    def test_straddling_interval_is_unresolved(self):
        bad = copy.deepcopy(BASE)
        bad["linear_term"] = {"lower": "-2", "upper": "0"}
        bad.pop("claimed_total")
        out = VERIFY.verify(bad)
        self.assertEqual(out["verdict"], "UNRESOLVED_SQUARE_LEVEL")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x94020_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class LiveSourceTest(unittest.TestCase):
    def test_retained_result(self) -> None:
        data = json.loads((ROOT / "results" / "verification.json").read_text())
        mutations = MOD.audit(data, ROOT / "results" / "certificates")
        self.assertTrue(all(mutations.values()))

    def test_gate_remains_open(self) -> None:
        data = json.loads((ROOT / "results" / "verification.json").read_text())
        self.assertTrue(data["joint_gate_status"].startswith("OPEN"))
        self.assertFalse(data["rh_established_by_replay"])

    def test_actual_child_separator(self) -> None:
        data = json.loads((ROOT / "results" / "verification.json").read_text())
        obstruction = data["q2_branchwise_child_obstruction"]
        self.assertEqual(obstruction["elementary_lower_bound"], "1/9")
        self.assertIn("impossible", obstruction["conclusion"])


if __name__ == "__main__":
    unittest.main()

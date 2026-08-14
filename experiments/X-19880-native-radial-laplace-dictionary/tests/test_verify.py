from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("x19880_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
BASE = json.loads((ROOT / "certificates" / "synthetic.json").read_text())


class NativeRadialDictionaryTests(unittest.TestCase):
    def verify(self, mutation=None):
        data = copy.deepcopy(BASE)
        if mutation is not None:
            mutation(data)
        return MOD.verify(data)

    def rejected(self, mutation):
        with self.assertRaises(MOD.CertificateError):
            self.verify(mutation)

    def test_exact_control_passes(self):
        out = self.verify()
        self.assertEqual(out["verdict"], "PASS_EXACT_NATIVE_RADIAL_DICTIONARY_ANALOGUE")
        self.assertEqual(out["mode_count"], 3)

    def test_rejects_owner_overallocation(self):
        self.rejected(
            lambda d: d["modes"][0].__setitem__("owner_fractions", ["2/3", "1/2"])
        )

    def test_rejects_negative_owner(self):
        self.rejected(
            lambda d: d["modes"][1].__setitem__("owner_fractions", ["-1/4", "1/2"])
        )

    def test_rejects_bad_geometric_parameter(self):
        self.rejected(lambda d: d.__setitem__("geometric_parameter", 1))

    def test_rejects_bad_interval_partition(self):
        self.rejected(lambda d: d.__setitem__("interval_weights", ["1/3", "1/3"]))

    def test_rejects_feature_dimension_change(self):
        self.rejected(lambda d: d["modes"][2].__setitem__("feature", [1, -1]))

    def test_rejects_false_claimed_slack(self):
        self.rejected(lambda d: d["claimed_slack_matrix"][0].__setitem__(0, "1/2"))

    def test_rejects_boolean_rational(self):
        self.rejected(lambda d: d.__setitem__("geometric_parameter", True))

    def test_radix_four_null_gauge(self):
        out = self.verify()
        records = {row["q"]: row for row in out["radix_four_columns"]}
        self.assertTrue(records[6]["prime_radial_null_gauge"])
        self.assertFalse(records[36]["prime_radial_null_gauge"])

    def test_rejects_false_radix_four_visibility(self):
        self.rejected(
            lambda d: d["radix_four_columns"][2].__setitem__("expected_y4_zero", True)
        )


if __name__ == "__main__":
    unittest.main()

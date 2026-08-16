from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x96300_verify", ROOT / "verify.py")
V = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(V)
BASE = json.loads((ROOT / "certificates" / "control.json").read_text())


class TwoFrontAssaultTests(unittest.TestCase):
    def test_control_passes(self):
        self.assertEqual(V.validate(copy.deepcopy(BASE))["verdict"], "PASS_T96300_RADICAL_TWO_FRONT_ASSAULT_ALGEBRA")

    def reject(self, mutate):
        bad = copy.deepcopy(BASE)
        mutate(bad)
        with self.assertRaises(ValueError):
            V.validate(bad)

    def test_schema(self):
        self.reject(lambda d: d.__setitem__("schema", "bad"))

    def test_annular_h(self):
        self.reject(lambda d: d["annular"].__setitem__("h", "0"))

    def test_positive_dictionary(self):
        self.reject(lambda d: d["single_row"]["q3"].__setitem__(2, "-5"))

    def test_numerator(self):
        self.reject(lambda d: d["single_row"]["numerator"].__setitem__(1, "8"))

    def test_affine_upper(self):
        self.reject(lambda d: d["affine"].__setitem__("U", "1"))

    def test_affine_lower(self):
        self.reject(lambda d: d["affine"].__setitem__("U", "1/10"))

    def test_profile_drift(self):
        self.reject(lambda d: d["volterra_profile"]["branches"][3].__setitem__(4, "-5"))

    def test_cutoff(self):
        self.reject(lambda d: d.__setitem__("formal_cutoff", 8))

    def test_actq_promotion(self):
        self.reject(lambda d: d["firewalls"].__setitem__("actq_proved", True))

    def test_sprp_promotion(self):
        self.reject(lambda d: d["firewalls"].__setitem__("sprp_proved", True))

    def test_frontier_chain_import(self):
        self.reject(lambda d: d["firewalls"].__setitem__("imports_pr537_frontier_chain_as_proof", True))

    def test_old_normalization(self):
        self.reject(lambda d: d["firewalls"].__setitem__("uses_old_J_equals_Y4_normalization", True))

    def test_genealogy(self):
        self.reject(lambda d: d["genealogy"].__setitem__("base_sha", "0" * 40))


if __name__ == "__main__":
    unittest.main()

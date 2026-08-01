from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VERIFY_SPEC = importlib.util.spec_from_file_location("x16209_verify", ROOT / "verify.py")
assert VERIFY_SPEC and VERIFY_SPEC.loader
mod = importlib.util.module_from_spec(VERIFY_SPEC)
sys.modules[VERIFY_SPEC.name] = mod
VERIFY_SPEC.loader.exec_module(mod)

MATERIALIZE_SPEC = importlib.util.spec_from_file_location(
    "x16209_materialize", ROOT / "materialize_source.py"
)
assert MATERIALIZE_SPEC and MATERIALIZE_SPEC.loader
materializer = importlib.util.module_from_spec(MATERIALIZE_SPEC)
sys.modules[MATERIALIZE_SPEC.name] = materializer
MATERIALIZE_SPEC.loader.exec_module(materializer)

CERT = json.loads((ROOT / "results/certificate-gamma32768.json").read_text())


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="x16209-source-")
        cls.source = Path(cls.tmp.name) / "source-gamma32768.json"
        digest = materializer.materialize(cls.source)
        assert digest == CERT["source_binding"]["source_file_sha256"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_production_block(self):
        out = mod.verify(copy.deepcopy(CERT), self.source)
        self.assertEqual(out["classification"], "SOURCE_BOUND_COFINAL_WRAPPER_BLOCK")
        self.assertEqual(out["gamma"], 32768)
        self.assertEqual(out["complete_alias"]["cross_upper"], "5019/23168")

    def test_source_digest_mutation_rejected(self):
        x = copy.deepcopy(CERT)
        x["source_binding"]["source_file_sha256"] = "0" * 64
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_alias_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["alias"]["cross_error_upper"] = "1/10"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_endpoint_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["endpoint"]["point_upper"] = "1/1000"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_source_energy_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["source_tails"]["derivative_l2_sum_upper"] = "1"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_good_measure_mutation_rejected(self):
        x = copy.deepcopy(CERT)
        x["cofinal_block"]["measure_lower"] = "1/100"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_epsilon_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["scalarization"]["claimed_epsilon_upper"] = "1/2"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_mode_ratio_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["tail_hierarchy"]["d4_over_d8_upper"] = "1/999999999999"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_ground_ratio_understatement_rejected(self):
        x = copy.deepcopy(CERT)
        x["tail_hierarchy"]["claimed_ground_ratio_upper"] = "1/1000000"
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)

    def test_next_scale_mutation_rejected(self):
        x = copy.deepcopy(CERT)
        x["next_gamma"] = 262145
        with self.assertRaises(mod.CertificateError):
            mod.verify(x, self.source)


if __name__ == "__main__":
    unittest.main()

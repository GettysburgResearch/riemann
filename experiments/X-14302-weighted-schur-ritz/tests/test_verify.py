from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("weighted_schur_verify", ROOT / "verify.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)
CertificateError = MOD.CertificateError


class WeightedSchurVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "certificates" / "synthetic-interval.json").read_text())

    def verify(self, mutate=None):
        data = copy.deepcopy(self.base)
        if mutate:
            mutate(data)
        return MOD.verify(data)

    def rejected(self, mutate):
        with self.assertRaises(CertificateError):
            self.verify(mutate)

    def test_passes_nontrivial_interval_certificate(self):
        out = self.verify()
        self.assertTrue(out["simple_even_ground_certified"])
        self.assertEqual(out["global_spectral_gap_lower"], "49/25")
        self.assertEqual(out["dual_residual_total_upper"], "21/100")
        self.assertEqual(out["weighted_target_line_distance_upper"], "37/70")

    def test_rejects_understated_rayleigh_upper(self):
        self.rejected(lambda d: d.__setitem__("rayleigh_upper", "0"))

    def test_rejects_false_weighted_coercivity(self):
        self.rejected(lambda d: d.__setitem__("weighted_coercivity", "1/2"))

    def test_rejects_false_odd_gap(self):
        self.rejected(lambda d: d.__setitem__("odd_gap", "3"))

    def test_rejects_understated_dual_residual(self):
        self.rejected(lambda d: d.__setitem__("dual_residual_midpoint_bound", "19/100"))

    def test_rejects_understated_operator_error_dual_budget(self):
        self.rejected(lambda d: d.__setitem__("dual_residual_error_bound", "9/1000"))

    def test_rejects_wrong_gram_order(self):
        def mutate(d):
            d["weighted_gram_upper"][0][0] = "3"
        self.rejected(mutate)

    def test_rejects_incomplete_even_basis(self):
        def mutate(d):
            d["even_complement_basis"] = [[row[0]] for row in d["even_complement_basis"]]
        self.rejected(mutate)

    def test_rejects_non_even_projection(self):
        def mutate(d):
            d["projection_vector"][3] = "1"
        self.rejected(mutate)

    def test_rejects_parity_breaking_midpoint(self):
        def mutate(d):
            d["matrix_midpoint"][0][3] = "1/1000"
            d["matrix_midpoint"][3][0] = "1/1000"
        self.rejected(mutate)

    def test_rejects_insufficient_lower_gram_floor(self):
        self.rejected(lambda d: d.__setitem__("weighted_lower_vs_ordinary", "5"))


if __name__ == "__main__":
    unittest.main()

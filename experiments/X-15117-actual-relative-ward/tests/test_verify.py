from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from verify import verify  # noqa: E402

CERT = ROOT / "certificates" / "noncommuting-ward-pass.json"


class WardVerifierTests(unittest.TestCase):
    def load(self):
        return json.loads(CERT.read_text())

    def test_valid(self):
        out = verify(self.load())
        self.assertEqual(out["status"], "CERTIFIED_ACTUAL_RELATIVE_WARD_PULLBACK")
        self.assertEqual(out["order_four_components"]["ward_order_four"], 19)
        self.assertEqual(out["corrected_scalar_coefficients"]["4"], 31)

    def test_wrong_schema(self):
        d = self.load(); d["schema"] = "bad"
        with self.assertRaises(ValueError): verify(d)

    def test_boolean_rejected(self):
        d = self.load(); d["raw_operator"][0][0] = True
        with self.assertRaises(ValueError): verify(d)

    def test_nonsymmetric_raw_rejected(self):
        d = self.load(); d["raw_operator"][0][1] = 3
        with self.assertRaises(ValueError): verify(d)

    def test_nonsymmetric_jet_rejected(self):
        d = self.load(); d["jet_operator"][1][0] = 2
        with self.assertRaises(ValueError): verify(d)

    def test_missing_order_rejected(self):
        d = self.load(); del d["nonlinear_counterterms"]["8"]
        with self.assertRaises(ValueError): verify(d)

    def test_bad_order_four_counterterm_rejected(self):
        d = self.load(); d["nonlinear_counterterms"]["4"] = 19
        with self.assertRaises(ValueError): verify(d)

    def test_bad_raw_defect_requires_recomputed_counterterm(self):
        d = self.load(); d["raw_diagonal_defects"]["4"] = 0
        with self.assertRaises(ValueError): verify(d)

    def test_invalid_radius_rejected(self):
        d = self.load(); d["series_radius"] = {"numerator": 1, "denominator": 4}
        with self.assertRaises(ValueError): verify(d)

    def test_undersized_hs_bound_rejected(self):
        d = self.load(); d["hilbert_schmidt_upper"] = 2
        with self.assertRaises(ValueError): verify(d)

    def test_dimension_mismatch_rejected(self):
        d = self.load(); d["jet_operator"] = [[0]]
        with self.assertRaises(ValueError): verify(d)


if __name__ == "__main__":
    unittest.main()

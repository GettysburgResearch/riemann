from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x4201_verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)
CERTIFICATE = ROOT / "certificates" / "c11-k1024.json"


class PiecewiseCorrectionBoundTests(unittest.TestCase):
    def load(self):
        return json.loads(CERTIFICATE.read_text(encoding="utf-8"))

    def test_committed_certificate(self):
        result = VERIFY.verify_certificate(self.load())
        self.assertEqual(
            result["status"],
            "RIGOROUS_CORRECTION_BOUND_EMPIRICAL_MARGIN_ONLY",
        )
        combined = Fraction(
            int(result["combined_operator_upper"]["numerator"]),
            int(result["combined_operator_upper"]["denominator"]),
        )
        self.assertLess(combined, Fraction(1, 4_000_000_000))
        self.assertEqual(result["minimum_scale_factor"], 1_000_000)

    def test_small_cell_bound_is_exact(self):
        result = VERIFY.verify_certificate(self.load())
        b_upper = Fraction(
            int(result["b_upper"]["numerator"]),
            int(result["b_upper"]["denominator"]),
        )
        self.assertEqual(b_upper, Fraction(319, 6400))
        self.assertLess(b_upper, Fraction(1, 20))

    def test_exponential_control_is_exact(self):
        result = VERIFY.verify_certificate(self.load())
        partial = result["log_c_bounds"]["exp_58_over_25_partial_degree_6"]
        value = Fraction(int(partial["numerator"]), int(partial["denominator"]))
        self.assertEqual(value, Fraction(110699859859, 10986328125))
        self.assertGreater(value, 10)

    def test_mutated_total_threshold_rejected(self):
        data = self.load()
        data["claimed"]["total_upper_threshold"] = {
            "numerator": "1",
            "denominator": "10000000000"
        }
        with self.assertRaisesRegex(
            VERIFY.CertificateError,
            "total correction threshold is not proved",
        ):
            VERIFY.verify_certificate(data)

    def test_empirical_margin_cannot_be_promoted(self):
        data = self.load()
        data["margin_classification"] = "CERTIFIED_INTERVAL_LOWER_BOUND"
        with self.assertRaisesRegex(
            VERIFY.CertificateError,
            "must remain explicitly empirical",
        ):
            VERIFY.verify_certificate(data)

    def test_parameter_mutation_rejected(self):
        data = self.load()
        data["K"] = 512
        with self.assertRaisesRegex(VERIFY.CertificateError, "supports K=1024"):
            VERIFY.verify_certificate(data)

    def test_claimed_scale_factor_cannot_be_inflated(self):
        data = self.load()
        data["claimed"]["minimum_scale_factor"] = "1000001"
        with self.assertRaisesRegex(
            VERIFY.CertificateError,
            "scale factor is not implied",
        ):
            VERIFY.verify_certificate(data)

    def test_harmonic_helper(self):
        self.assertEqual(VERIFY.harmonic(0), 0)
        self.assertEqual(VERIFY.harmonic(4), Fraction(25, 12))


if __name__ == "__main__":
    unittest.main()

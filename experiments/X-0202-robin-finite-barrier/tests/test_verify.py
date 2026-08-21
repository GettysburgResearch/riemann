from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from verify import build_certificate, divisor_sums, exact_abundancy_maximum


class ExactBarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sigma = divisor_sums(5582)

    def test_maximum_to_5040(self):
        maximum = exact_abundancy_maximum(self.sigma, 1, 5040)
        self.assertEqual(maximum.maximizers, [5040])
        self.assertEqual(Fraction(maximum.sigma, maximum.denominator_n), Fraction(403, 105))

    def test_exception_window(self):
        maximum = exact_abundancy_maximum(self.sigma, 5041, 5582)
        self.assertEqual(maximum.maximizers, [5460])
        self.assertEqual(Fraction(maximum.sigma, maximum.denominator_n), Fraction(224, 65))

    def test_transcendental_signs(self):
        certificate = build_certificate(precision=50, gamma_terms=10_000)
        self.assertTrue(certificate["comparison_at_5041"]["certified_strictly_positive"])
        self.assertTrue(certificate["comparison_at_5583"]["certified_strictly_positive"])

    def test_precision_stability(self):
        low = build_certificate(precision=45, gamma_terms=5_000)
        high = build_certificate(precision=70, gamma_terms=20_000)
        for key in ("comparison_at_5041", "comparison_at_5583"):
            self.assertTrue(low[key]["certified_strictly_positive"])
            self.assertTrue(high[key]["certified_strictly_positive"])


if __name__ == "__main__":
    unittest.main()

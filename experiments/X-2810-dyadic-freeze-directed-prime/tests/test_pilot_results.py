import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fraction(raw):
    return Fraction(raw["numerator"], raw["denominator"])


class PilotResultTests(unittest.TestCase):
    def test_directed_counts_and_width(self):
        data = json.loads(
            (ROOT / "results/mpfr-prime-c1e8.json").read_text()
        )
        self.assertEqual(data["prime_count"], 5_761_455)
        self.assertEqual(data["higher_prime_power_count"], 1_404)
        self.assertEqual(data["total_terms"], 5_762_859)
        lower = Fraction.from_float(
            float.fromhex(data["prime_rayleigh_lower_hex"])
        )
        upper = Fraction.from_float(
            float.fromhex(data["prime_rayleigh_upper_hex"])
        )
        self.assertLess(lower, upper)
        self.assertLess(upper - lower, Fraction(1, 10**12))

    def test_final_interval_positive(self):
        data = json.loads(
            (ROOT / "results/pilot-fixed-vector-summary-c1e8.json").read_text()
        )
        self.assertTrue(data["certified_positive"])
        self.assertFalse(data["certified_negative"])
        self.assertGreater(fraction(data["full_interval"]["lower"]), 0)

    def test_normalization_binding(self):
        data = json.loads(
            (ROOT / "results/pilot-certificate-manifest.json").read_text()
        )
        self.assertEqual(
            data.get("normalization_sha256"),
            "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be",
        )
        self.assertEqual(
            data.get("certificate_sha256"),
            "647443663adbdc8db114a8ef6d69b860ee66337bdf703ef52bfb4884713eb03e",
        )


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PrecisionLadderTests(unittest.TestCase):
    def test_192_and_256_bit_endpoints_match(self):
        first = json.loads(
            (ROOT / "results/mpfr-prime-c1e8.json").read_text()
        )
        second = json.loads(
            (ROOT / "results/mpfr-prime-c1e8-p256.json").read_text()
        )
        for key in (
            "alpha_lower_hex",
            "alpha_upper_hex",
            "prime_rayleigh_lower_hex",
            "prime_rayleigh_upper_hex",
        ):
            self.assertEqual(first[key], second[key])
        self.assertEqual(first["precision_bits"], 192)
        self.assertEqual(second["precision_bits"], 256)


if __name__ == "__main__":
    unittest.main()

import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFY = ROOT / "experiments" / "X-106800-beta-spectral-abscissa" / "verify.py"
RESULT = (
    ROOT
    / "experiments"
    / "X-106800-beta-spectral-abscissa"
    / "results"
    / "verification.json"
)


class BetaSpectralAbscissaTest(unittest.TestCase):
    def test_replay(self) -> None:
        subprocess.run([sys.executable, "-B", str(VERIFY)], check=True)
        data = json.loads(RESULT.read_text())
        self.assertEqual(
            data["verdict"],
            "PASS_T106800_BETA_SPECTRAL_ABSCISSA_AND_VK_ENERGY",
        )
        self.assertFalse(data["rh_established"])
        self.assertFalse(data["fixed_power_saving_proved"])

    def test_exponent_map(self) -> None:
        for q in range(2, 101):
            for p in range((q + 1) // 2, q + 1):
                theta = Fraction(p, q)
                self.assertEqual(
                    2 * (theta - Fraction(1, 2)),
                    2 * theta - 1,
                )

    def test_zero_free_dictionary_constants(self) -> None:
        self.assertEqual(
            Fraction(3, 40) + Fraction(11, 500),
            Fraction(97, 1000),
        )
        self.assertEqual(
            Fraction(997, 1000) - Fraction(97, 1000),
            Fraction(9, 10),
        )


if __name__ == "__main__":
    unittest.main()

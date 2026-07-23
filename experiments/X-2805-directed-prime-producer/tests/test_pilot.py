import json
import unittest
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


def interval(path: Path) -> tuple[Fraction, Fraction, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    raw = data["prime_rayleigh_interval"]
    lower = Fraction(
        raw["lower"]["numerator"], raw["lower"]["denominator"]
    )
    upper = Fraction(
        raw["upper"]["numerator"], raw["upper"]["denominator"]
    )
    return lower, upper, data


class DirectedPilotTests(unittest.TestCase):
    def test_counts_and_fingerprints(self):
        _, _, data = interval(HERE / "results" / "pilot-192.json")
        self.assertEqual(data["prime_count"], 9592)
        self.assertEqual(data["higher_prime_power_count"], 108)
        self.assertEqual(data["total_terms"], 9700)
        self.assertEqual(
            data["normalization_sha256"],
            "65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be",
        )

    def test_precision_nesting(self):
        lower_192, upper_192, _ = interval(HERE / "results" / "pilot-192.json")
        lower_256, upper_256, _ = interval(HERE / "results" / "pilot-256.json")
        self.assertLessEqual(lower_192, lower_256)
        self.assertLessEqual(lower_256, upper_256)
        self.assertLessEqual(upper_256, upper_192)
        self.assertLess(upper_256 - lower_256, upper_192 - lower_192)

    def test_independent_100_decimal_control_is_contained(self):
        getcontext().prec = 120
        control = Decimal(
            "-0.1133099482610300093554196495233908192581057802956499386971708073912527014079675612886902217966347712"
        )
        control_fraction = Fraction(control)
        for name in ("pilot-192.json", "pilot-256.json"):
            lower, upper, _ = interval(HERE / "results" / name)
            self.assertLessEqual(lower, control_fraction)
            self.assertLessEqual(control_fraction, upper)

    def test_widths_are_tiny(self):
        lower_192, upper_192, data_192 = interval(
            HERE / "results" / "pilot-192.json"
        )
        lower_256, upper_256, data_256 = interval(
            HERE / "results" / "pilot-256.json"
        )
        self.assertLess(upper_192 - lower_192, Fraction(1, 10**53))
        self.assertLess(upper_256 - lower_256, Fraction(1, 10**73))
        self.assertLess(
            data_256["maximum_phase_interval_width_upper"],
            data_192["maximum_phase_interval_width_upper"],
        )


if __name__ == "__main__":
    unittest.main()

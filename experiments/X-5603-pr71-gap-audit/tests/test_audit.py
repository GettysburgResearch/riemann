from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("audit", HERE.parent / "audit_exact_ordinate.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class ExactOrdinateAuditTests(unittest.TestCase):
    def test_exact_mismatch_and_ulp(self):
        data = MOD.build()
        self.assertEqual(data["exact_minus_binary64"]["fraction"], {
            "numerator": "174483",
            "denominator": "4294967296",
        })
        self.assertEqual(data["binary64_ulp_at_height"]["fraction"], {
            "numerator": "1",
            "denominator": "1024",
        })

    def test_reported_gap_is_509_over_512(self):
        data = MOD.build()
        self.assertEqual(data["reported_gap_from_serialized_endpoints"]["gap"], {
            "numerator": "509",
            "denominator": "512",
        })
        exact = Fraction(
            int(data["exact_ordinate"]["fraction"]["numerator"]),
            int(data["exact_ordinate"]["fraction"]["denominator"]),
        )
        rounded = Fraction(
            int(data["binary64_ordinate_used_by_strtod"]["fraction"]["numerator"]),
            int(data["binary64_ordinate_used_by_strtod"]["fraction"]["denominator"]),
        )
        self.assertGreater(exact, rounded)


if __name__ == "__main__":
    unittest.main()

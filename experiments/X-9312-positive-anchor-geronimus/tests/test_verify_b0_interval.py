from fractions import Fraction
import unittest

import positive_anchor as pa
import verify_b0_interval as vb


class VerifyB0Tests(unittest.TestCase):
    @staticmethod
    def basis_and_moments():
        old = [Fraction(3), Fraction(9), Fraction(35), Fraction(153), Fraction(707)]
        moments = [pa.Interval(value, value) for value in old]
        data = {
            "schema": pa.BASIS_SCHEMA,
            "primitive_sha256": "synthetic",
            "ordinate": {"numerator": 1, "denominator": 1},
            "primitive_shift": {"numerator": 0, "denominator": 1},
        }
        return data, moments, old

    @staticmethod
    def candidate(w, lower, upper):
        return {
            "schema": vb.SCHEMA,
            "anchor": pa.fraction_json(w),
            "b0_interval": {
                "lower": pa.fraction_json(lower),
                "upper": pa.fraction_json(upper),
            },
        }

    def test_lower_negative(self):
        data, moments, old = self.basis_and_moments()
        gate = pa.positive_anchor_gate(old, Fraction(2))
        b0 = gate["lower"] - Fraction(1, 100)
        result = vb.verify(data, moments, self.candidate(Fraction(2), b0, b0))
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_LOWER_SQUARE")

    def test_upper_negative(self):
        data, moments, old = self.basis_and_moments()
        gate = pa.positive_anchor_gate(old, Fraction(2))
        b0 = gate["upper"] + Fraction(1, 100)
        result = vb.verify(data, moments, self.candidate(Fraction(2), b0, b0))
        self.assertEqual(result["verdict"], "CERTIFIED_NEGATIVE_UPPER_Y_SQUARE")

    def test_inside_not_promoted(self):
        data, moments, old = self.basis_and_moments()
        gate = pa.positive_anchor_gate(old, Fraction(2))
        b0 = (gate["lower"] + gate["upper"]) / 2
        result = vb.verify(data, moments, self.candidate(Fraction(2), b0, b0))
        self.assertFalse(result["certified_negative"])

    def test_zero_touch_not_negative(self):
        data, moments, old = self.basis_and_moments()
        gate = pa.positive_anchor_gate(old, Fraction(2))
        result = vb.verify(
            data,
            moments,
            self.candidate(Fraction(2), gate["lower"], gate["lower"]),
        )
        self.assertFalse(result["certified_negative"])


if __name__ == "__main__":
    unittest.main()

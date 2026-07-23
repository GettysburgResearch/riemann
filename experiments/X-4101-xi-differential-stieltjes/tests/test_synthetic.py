from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import synthetic  # noqa: E402


CERTIFICATE = ROOT / "certificates" / "synthetic-offline-quartet.json"


class XiDifferentialStieltjesTests(unittest.TestCase):
    def load_certificate(self) -> dict:
        with CERTIFICATE.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def test_offline_quartet_has_positive_scalar_and_negative_differential(self) -> None:
        result = synthetic.verify_certificate(self.load_certificate())
        self.assertEqual(
            result["status"],
            "SYNTHETIC_RIGHT_SIDE_DIFFERENTIAL_NEGATIVE",
        )
        self.assertTrue(result["identity_b00_equals_half_differential"])
        self.assertGreater(
            synthetic.parse_fraction(result["re_f"], "re_f"),
            0,
        )
        self.assertLess(
            synthetic.parse_fraction(result["differential"], "differential"),
            0,
        )

    def test_mutated_claim_is_rejected(self) -> None:
        data = self.load_certificate()
        numerator = int(data["claimed"]["differential"]["numerator"])
        data["claimed"]["differential"]["numerator"] = str(numerator + 1)
        with self.assertRaises(synthetic.CertificateError):
            synthetic.verify_certificate(data)

    def test_on_line_moments_match_finite_jet_formula(self) -> None:
        ordinates = [
            Fraction(-7),
            Fraction(-3),
            Fraction(2),
            Fraction(5),
        ]
        zeros = [(Fraction(0), gamma) for gamma in ordinates]
        x = Fraction(2, 3)
        height = Fraction(1, 5)
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 7)
        from_jet = synthetic.moments_from_jet(jet, x, 7)
        direct = synthetic.direct_on_line_moments(
            ordinates, x, height, 7
        )
        self.assertEqual(from_jet, direct)

    def test_hankel_and_localizing_quadratics_match_positive_sums(self) -> None:
        ordinates = [
            Fraction(-7),
            Fraction(-3),
            Fraction(2),
            Fraction(5),
        ]
        zeros = [(Fraction(0), gamma) for gamma in ordinates]
        x = Fraction(2, 3)
        height = Fraction(1, 5)
        order = 3
        jet = synthetic.finite_logderivative_jet(
            zeros, x, height, 2 * order + 1
        )
        moments = synthetic.moments_from_jet(
            jet, x, 2 * order + 1
        )
        hankel = synthetic.hankel_matrix(moments, order)
        localizing = synthetic.localizing_matrix(
            moments, x * x, order
        )

        for raw_vector in product(range(-1, 2), repeat=order + 1):
            if not any(raw_vector):
                continue
            vector = [Fraction(value) for value in raw_vector]
            with self.subTest(vector=raw_vector, kind="hankel"):
                matrix_value = synthetic.quadratic_form(hankel, vector)
                direct_value = synthetic.direct_hankel_quadratic(
                    ordinates, x, height, vector
                )
                self.assertEqual(matrix_value, direct_value)
                self.assertGreaterEqual(matrix_value, 0)
            with self.subTest(vector=raw_vector, kind="localizing"):
                matrix_value = synthetic.quadratic_form(
                    localizing, vector
                )
                direct_value = synthetic.direct_localizing_quadratic(
                    ordinates, x, height, vector
                )
                self.assertEqual(matrix_value, direct_value)
                self.assertGreaterEqual(matrix_value, 0)

    def test_b00_is_exactly_half_the_differential(self) -> None:
        delta = Fraction(1, 10)
        gamma = Fraction(20)
        zeros = [
            (delta, gamma),
            (delta, -gamma),
            (-delta, gamma),
            (-delta, -gamma),
        ]
        x = Fraction(11, 100)
        height = Fraction(20)
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 1)
        moments = synthetic.moments_from_jet(jet, x, 1)
        b00 = moments[0] - x * x * moments[1]
        differential = synthetic.differential_from_jet(jet, x)
        self.assertEqual(b00, differential / 2)
        self.assertGreater(jet[0][0], 0)
        self.assertLess(b00, 0)

    def test_localizer_orientation_is_essential(self) -> None:
        ordinates = [Fraction(-2), Fraction(3)]
        zeros = [(Fraction(0), gamma) for gamma in ordinates]
        x = Fraction(3, 4)
        height = Fraction(1, 7)
        jet = synthetic.finite_logderivative_jet(zeros, x, height, 1)
        moments = synthetic.moments_from_jet(jet, x, 1)
        correct = moments[0] - x * x * moments[1]
        reversed_sign = x * x * moments[1] - moments[0]
        self.assertGreaterEqual(correct, 0)
        self.assertEqual(reversed_sign, -correct)
        self.assertLess(reversed_sign, 0)

    def test_right_side_divergence_strengthens_toward_the_pole(self) -> None:
        delta = Fraction(1, 10)
        gamma = Fraction(20)
        zeros = [
            (delta, gamma),
            (delta, -gamma),
            (-delta, gamma),
            (-delta, -gamma),
        ]
        height = Fraction(20)
        values = []
        for x in (Fraction(11, 100), Fraction(21, 200), Fraction(101, 1000)):
            jet = synthetic.finite_logderivative_jet(zeros, x, height, 1)
            values.append(
                (
                    jet[0][0],
                    synthetic.differential_from_jet(jet, x),
                )
            )
        self.assertTrue(all(re_f > 0 for re_f, _ in values))
        self.assertTrue(all(differential < 0 for _, differential in values))
        # x decreases from .11 to .105 to .101, approaching delta=.1.
        self.assertGreater(abs(values[1][1]), abs(values[0][1]))
        self.assertGreater(abs(values[2][1]), abs(values[1][1]))


if __name__ == "__main__":
    unittest.main()

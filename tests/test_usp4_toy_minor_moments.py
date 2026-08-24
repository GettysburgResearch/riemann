"""Exact tests for the lightweight USp(4) toy-minor comparator."""

from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import usp4_toy_minor_moments as usp4  # noqa: E402


class LaurentCertificateTests(unittest.TestCase):
    def test_character_identity_and_dimensions(self) -> None:
        self.assertEqual(usp4.character_identity_residual(), {})
        self.assertEqual(usp4.evaluate_at_identity(usp4.trace_character()), 4)
        self.assertEqual(usp4.evaluate_at_identity(usp4.fundamental_five_character()), 5)
        self.assertEqual(
            usp4.evaluate_at_identity(usp4.traceless_symmetric_square_character()), 14
        )
        self.assertEqual(usp4.evaluate_at_identity(usp4.statistic_character()), -20)

    def test_c2_weyl_normalization_and_haar_moments(self) -> None:
        self.assertEqual(usp4.constant_term(usp4.weyl_density()), 8)
        raw = [-1, 3, -11, 56, -374, 3117]
        self.assertEqual(usp4.haar_moments(), raw)
        self.assertEqual(usp4.centered_moments(raw), [0, 2, -4, 27, -178, 1533])
        self.assertEqual(usp4.cumulants(raw), [-1, 2, -4, 15, -98, 803])
        self.assertEqual(usp4.centered_moments([]), [])
        self.assertEqual(usp4.cumulants([]), [])

    def test_exact_range_witnesses_and_domain_guard(self) -> None:
        self.assertEqual(
            usp4.statistic_in_trace_coordinates(Fraction(2), Fraction(2)),
            usp4.HAAR_RANGE_MINIMUM,
        )
        self.assertEqual(
            usp4.statistic_in_trace_coordinates(Fraction(2), Fraction(-2, 3)),
            usp4.HAAR_RANGE_MAXIMUM,
        )
        with self.assertRaisesRegex(ValueError, "trace coordinates"):
            usp4.statistic_in_trace_coordinates(Fraction(3), Fraction(0))

    def test_laurent_arithmetic_hostile_controls(self) -> None:
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            usp4.power({(0, 0): 1}, -1)
        with self.assertRaisesRegex(ArithmeticError, "divisible"):
            usp4.divide_exact({(0, 0): 1}, 2)
        with self.assertRaisesRegex(ValueError, "max_moment"):
            usp4.haar_moments(7)

    def test_exact_degree_six_sign_majorant(self) -> None:
        coefficients = list(usp4.SIGN_MAJORANT_COEFFICIENTS)
        square = usp4.convolve_rational(coefficients, coefficients)
        self.assertEqual(len(square), 7)
        self.assertEqual(
            usp4.polynomial_moment(square, [-1, 3, -11, 56, -374, 3117]),
            Fraction(7663, 12023),
        )
        # The concave quadratic controlling R(x)-1 is positive at both
        # endpoints of the only interval where a nonnegative indicator matters.
        quadratic = lambda x: 5405 + 264 * x - 23 * x * x
        self.assertEqual(quadratic(Fraction(0)), 5405)
        self.assertEqual(quadratic(Fraction(4, 3)), Fraction(51445, 9))
        self.assertLess(-23, 0)
        for power in range(1, 4):
            moments = [1, -1, 3, -11, 56, -374, 3117]
            self.assertEqual(
                sum(coefficients[index] * moments[index + power] for index in range(4)),
                0,
            )
        with self.assertRaisesRegex(ValueError, "insufficient raw moments"):
            usp4.polynomial_moment(square, [-1, 3])


class FixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = usp4.build_fixture()

    def test_exact_finite_first_moments(self) -> None:
        expected = {
            3: Fraction(-104, 243),
            5: Fraction(-1994, 3125),
            7: Fraction(-12340, 16807),
        }
        for comparison in self.fixture["finite_comparisons"]:
            first = comparison["moments"][0]
            self.assertEqual(Fraction(*first["finite_exact"]), expected[comparison["q"]])
            self.assertEqual(first["usp4_haar_exact"], -1)
            self.assertEqual(
                Fraction(*first["finite_minus_haar"]),
                expected[comparison["q"]] + 1,
            )

    def test_all_six_moments_reconstruct_from_histograms(self) -> None:
        q_scan = json.loads(usp4.Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
        families = {family["q"]: family for family in q_scan["families"]}
        for comparison in self.fixture["finite_comparisons"]:
            actual = usp4.finite_moments(families[comparison["q"]], 6)
            stored = [Fraction(*entry["finite_exact"]) for entry in comparison["moments"]]
            self.assertEqual(stored, actual)
            q = comparison["q"]
            histogram = {int(key): value for key, value in families[q]["K_histogram"].items()}
            self.assertGreaterEqual(Fraction(min(histogram), q * q), usp4.HAAR_RANGE_MINIMUM)
            self.assertLessEqual(Fraction(max(histogram), q * q), usp4.HAAR_RANGE_MAXIMUM)

    def test_frozen_directional_pattern_is_exact_but_finite_only(self) -> None:
        pattern = self.fixture["frozen_moment_pattern"]
        self.assertEqual(pattern["status"], usp4.FROZEN_PATTERN_STATUS)
        self.assertTrue(pattern["not_a_theorem_beyond_frozen_fields"])
        self.assertEqual(pattern["q_values"], [3, 5, 7])
        self.assertEqual([row["order"] for row in pattern["per_order"]], list(range(1, 7)))
        for row in pattern["per_order"]:
            self.assertTrue(
                all(value is True for key, value in row.items() if key != "order")
            )

    def test_negative_sign_moment_certificate_is_exact(self) -> None:
        certificate = self.fixture["negative_sign_moment_certificate"]
        self.assertEqual(certificate["status"], usp4.SIGN_MAJORANT_STATUS)
        self.assertEqual(
            Fraction(*certificate["haar"]["moment_majorant_nonnegative_upper_bound"]),
            Fraction(7663, 12023),
        )
        self.assertEqual(
            Fraction(*certificate["haar"]["negative_probability_lower_bound"]),
            Fraction(4360, 12023),
        )
        expected = {
            3: (
                Fraction(316385345123392, 2074170795235803),
                Fraction(17, 27),
            ),
            5: (
                Fraction(1049258112998647044, 4411393096923828125),
                Fraction(33, 50),
            ),
            7: (
                Fraction(188194097859476923656, 686272022845319295847),
                Fraction(33, 49),
            ),
        }
        for row in certificate["finite_q_bounds"]:
            lower, observed = expected[row["q"]]
            self.assertEqual(Fraction(*row["negative_probability_lower_bound"]), lower)
            self.assertEqual(Fraction(*row["observed_negative_fraction"]), observed)
            self.assertLessEqual(lower, observed)
            self.assertTrue(row["verified_bound_holds"])
        conditional = certificate["conditional_consequence"]
        self.assertEqual(
            conditional["status"], "CONDITIONAL_ON_FIRST_SIX_MOMENT_CONVERGENCE"
        )
        self.assertTrue(conditional["not_an_equidistribution_proof"])

    def test_rigorous_parts_are_separate_from_limit_target(self) -> None:
        self.assertEqual(self.fixture["rigor_level"], usp4.HAAR_STATUS)
        self.assertEqual(
            self.fixture["character_identity"]["status"],
            "PROVED_EXACT_LAURENT_IDENTITY",
        )
        self.assertEqual(self.fixture["limit_target"]["status"], usp4.COMPARISON_STATUS)
        self.assertTrue(self.fixture["limit_target"]["not_a_theorem"])
        self.assertFalse(self.fixture["resource_contract"]["random_sampling"])
        self.assertFalse(self.fixture["resource_contract"]["numerical_integration"])

    def test_producer_source_is_content_locked(self) -> None:
        import hashlib

        source = Path(usp4.__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(
            self.fixture["producer"]["source_sha256_lf_normalized"],
            hashlib.sha256(source.encode("utf-8")).hexdigest(),
        )

    def test_histogram_count_mismatch_is_rejected(self) -> None:
        hostile = {"q": 3, "member_count": 2, "K_histogram": {"0": 1}}
        with self.assertRaisesRegex(ValueError, "histogram count mismatch"):
            usp4.finite_moments(hostile, 1)

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "usp4_toy_minor_moments.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, self.fixture)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rational_intervals import (  # noqa: E402
    DyadicInterval,
    euler_gamma_interval,
    exp_interval,
    log_fraction_interval,
    log_interval,
    parse_decimal_fraction,
)
from verify import (  # noqa: E402
    build_certificate,
    exact_abundancy_maximum,
    factorization_trial_division,
    sigma_from_factorization,
)


def divisor_sums_by_multiples(limit: int) -> list[int]:
    """Independent test oracle using divisor additions rather than factoring."""
    values = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            values[multiple] += divisor
    return values


class FactorizationTests(unittest.TestCase):
    def test_factorizations_and_sigma(self) -> None:
        self.assertEqual(factorization_trial_division(1), [])
        self.assertEqual(
            factorization_trial_division(5040),
            [(2, 4), (3, 2), (5, 1), (7, 1)],
        )
        self.assertEqual(sigma_from_factorization(1), 1)
        self.assertEqual(sigma_from_factorization(5040), 19344)
        self.assertEqual(sigma_from_factorization(5460), 18816)

    def test_factorization_sigma_agrees_with_divisor_addition(self) -> None:
        sieve = divisor_sums_by_multiples(5582)
        for n in range(1, 5583):
            self.assertEqual(sigma_from_factorization(n), sieve[n], msg=f"n={n}")

    def test_unique_exact_maxima(self) -> None:
        below = exact_abundancy_maximum(1, 5040)
        window = exact_abundancy_maximum(5041, 5582)
        self.assertEqual(below.maximizers, [5040])
        self.assertEqual(
            Fraction(below.reduced_numerator, below.reduced_denominator),
            Fraction(403, 105),
        )
        self.assertEqual(window.maximizers, [5460])
        self.assertEqual(
            Fraction(window.reduced_numerator, window.reduced_denominator),
            Fraction(224, 65),
        )


class IntervalTests(unittest.TestCase):
    BITS = 256
    TERMS = 80

    def test_decimal_parser_exact(self) -> None:
        self.assertEqual(parse_decimal_fraction("1.25E-2"), Fraction(1, 80))
        self.assertEqual(parse_decimal_fraction("-3.5"), Fraction(-7, 2))

    def test_log_one_and_log_two(self) -> None:
        zero = log_fraction_interval(Fraction(1), bits=self.BITS, terms=self.TERMS)
        self.assertEqual((zero.lower, zero.upper), (0, 0))
        log_two = log_fraction_interval(Fraction(2), bits=self.BITS, terms=self.TERMS)
        self.assertGreater(log_two.lower * 10000, 6931 * (1 << self.BITS))
        self.assertLess(log_two.upper * 10000, 6932 * (1 << self.BITS))

    def test_log_monotonic_interval(self) -> None:
        source = DyadicInterval.from_fraction(Fraction(3, 2), self.BITS)
        logged = log_interval(source, terms=self.TERMS)
        self.assertGreater(logged.lower, 0)
        self.assertLess(logged.width_numerator(), 1000)

    def test_gamma_coarse_sanity_and_width(self) -> None:
        gamma = euler_gamma_interval(
            harmonic_cutoff=100_000, bits=self.BITS, log_terms=self.TERMS
        )
        self.assertGreater(gamma.lower * 100000, 57721 * (1 << self.BITS))
        self.assertLess(gamma.upper * 100000, 57722 * (1 << self.BITS))
        # The two-sided harmonic remainder makes the interval O(n^-2).
        self.assertLess(gamma.width_numerator(), (1 << self.BITS) // 1_000_000_000)

    def test_exp_log_two_contains_two(self) -> None:
        log_two = log_fraction_interval(Fraction(2), bits=self.BITS, terms=self.TERMS)
        exp_log_two = exp_interval(log_two, terms=self.TERMS)
        self.assertTrue(exp_log_two.contains_fraction(Fraction(2)))


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = build_certificate(
            bits=256,
            log_terms=80,
            exp_terms=80,
            harmonic_cutoff=200_000,
            decimal_digits=55,
        )

    def test_strict_signs_and_sharp_crossing(self) -> None:
        self.assertTrue(
            self.certificate["comparison_at_5041"]["certified_strictly_positive"]
        )
        self.assertTrue(
            self.certificate["comparison_at_5582"]["certified_strictly_negative"]
        )
        self.assertTrue(
            self.certificate["comparison_at_5583"]["certified_strictly_positive"]
        )
        crossing = self.certificate["sharp_integer_crossing"]
        self.assertEqual(crossing["last_negative_integer"], 5582)
        self.assertEqual(crossing["first_positive_integer"], 5583)

    def test_independent_intervals_refine_x0202(self) -> None:
        for n in (5041, 5583):
            comparison = self.certificate[f"comparison_at_{n}"]
            self.assertTrue(comparison["contained_in_x0202_rhs_interval"])
            self.assertTrue(comparison["contained_in_x0202_difference_interval"])

    def test_no_x0202_reference_is_claimed_for_new_5582_check(self) -> None:
        comparison = self.certificate["comparison_at_5582"]
        self.assertFalse(comparison["x0202_reference_available"])
        self.assertIsNone(comparison["contained_in_x0202_rhs_interval"])
        self.assertIsNone(comparison["contained_in_x0202_difference_interval"])

    def test_boundary_labels(self) -> None:
        audit = self.certificate["boundary_audit"]
        self.assertEqual(set(audit), {"5040", "5041", "5582", "5583"})


if __name__ == "__main__":
    unittest.main()

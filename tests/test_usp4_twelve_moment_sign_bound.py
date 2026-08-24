"""Focused exact replay tests for the bounded USp(4) degree-twelve certificate."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import usp4_twelve_moment_sign_bound as subject  # noqa: E402


class ExactHaarReplayTests(unittest.TestCase):
    def test_twelve_c2_constant_term_moments_and_budget(self) -> None:
        moments, operations = subject.haar_moments()
        self.assertEqual(
            moments,
            [-1, 3, -11, 56, -374, 3117, -30321, 327688, -3815668, 46998100, -605231862, 8084025096],
        )
        self.assertEqual(operations, 238743)
        self.assertLessEqual(operations, subject.MAX_LAURENT_PAIR_PRODUCTS)

    def test_resource_guards_and_histogram_guard(self) -> None:
        with self.assertRaisesRegex(ValueError, "wall limit"):
            subject.haar_moments(maximum_wall_seconds=subject.MAX_WALL_SECONDS + 0.1)

        class AdvancingClock:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self) -> float:
                self.calls += 1
                return 0.0 if self.calls <= 2 else subject.MAX_WALL_SECONDS + 1.0

        with self.assertRaisesRegex(TimeoutError, "monotonic wall deadline"):
            subject.haar_moments(clock=AdvancingClock())
        with self.assertRaisesRegex(ValueError, "histogram count mismatch"):
            subject.finite_raw_moments({"q": 3, "member_count": 2, "K_histogram": {"0": 1}})


class MajorantCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.majorant_certificate()

    def test_exact_factorized_and_bernstein_certificates(self) -> None:
        polynomial = self.certificate["polynomial_t"]
        self.assertEqual(len(polynomial), 13)
        self.assertEqual(subject._poly_eval(polynomial, subject.POSITIVE_T_START), 1)
        self.assertEqual(subject._poly_eval(polynomial, subject.CONTACT), 1)
        self.assertEqual(subject._poly_eval(subject._poly_derivative(polynomial), subject.CONTACT), 0)
        self.assertGreater(self.certificate["quadratic_floor"], 0)
        self.assertEqual(tuple(self.certificate["bernstein"]), subject.EXPECTED_BERNSTEIN_QUOTIENT)
        self.assertTrue(all(value > 0 for value in self.certificate["bernstein"]))

    def test_exact_haar_bound_and_degree_six_improvement(self) -> None:
        raw, _ = subject.haar_moments()
        expectation = subject.polynomial_moment(self.certificate["polynomial_x"], raw)
        self.assertEqual(expectation, subject.EXPECTED_UPPER)
        self.assertLess(expectation, subject.SUPPORT_DEGREE_SIX_UPPER)
        self.assertEqual(
            subject.SUPPORT_DEGREE_SIX_UPPER - expectation,
            Fraction(
                1591512542290665885075183371275920634034566533880115933864168256509,
                17515010628514843235751823881636180941827271383724708897649705615360,
            ),
        )
        self.assertEqual(
            subject.t_moments(raw)[-1],
            Fraction(19820500355524589, 144115188075855872),
        )


class FixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_finite_histogram_bounds_and_scope_firewalls(self) -> None:
        expected_observed = {3: Fraction(17, 27), 5: Fraction(33, 50), 7: Fraction(33, 49)}
        for row in self.fixture["finite_q_bounds"]:
            lower = Fraction(*row["negative_probability_lower_bound"])
            self.assertLessEqual(lower, expected_observed[row["q"]])
            self.assertEqual(Fraction(*row["observed_negative_fraction"]), expected_observed[row["q"]])
            self.assertTrue(row["verified_bound_holds"])
        scope = self.fixture["scope"]
        self.assertTrue(scope["not_an_optimality_claim"])
        self.assertTrue(scope["not_an_equidistribution_theorem"])
        self.assertTrue(scope["not_a_number_field_transfer"])
        self.assertFalse(self.fixture["resource_contract"]["field_enumeration"])

    def test_checked_in_fixture_and_source_lock(self) -> None:
        stored = json.loads(subject.FROZEN_FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        source = Path(subject.__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(
            self.fixture["producer"]["source_sha256_lf_normalized"],
            hashlib.sha256(source.encode("utf-8")).hexdigest(),
        )
        q_scan = json.loads(
            (FUNCTION_FIELD / "genus2_q_scan.json").read_text(encoding="utf-8")
        )
        q_payload = dict(q_scan)
        payload_hash = q_payload.pop("payload_sha256")
        source_lock = self.fixture["producer"]["finite_histogram_source"]
        self.assertEqual(source_lock["payload_sha256"], payload_hash)
        self.assertEqual(
            source_lock["canonical_sha256"], subject._canonical_sha256(q_scan)
        )
        self.assertEqual(payload_hash, subject._canonical_sha256(q_payload))


if __name__ == "__main__":
    unittest.main()

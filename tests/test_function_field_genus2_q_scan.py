"""Focused exact and resource-guard tests for the genus-two q scan."""

from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_q_scan as scan  # noqa: E402
import pilot  # noqa: E402


class FieldAndCoefficientTests(unittest.TestCase):
    def test_extension_characters_have_exact_square_split(self) -> None:
        for q in scan.FROZEN_Q_VALUES:
            tables = scan.build_field_tables(q)
            self.assertEqual(
                pow(tables.nonsquare, (q - 1) // 2, q),
                q - 1,
            )
            counts = {
                value: sum(character == value for character in tables.extension_character.values())
                for value in (-1, 0, 1)
            }
            self.assertEqual(counts, {-1: (q * q - 1) // 2, 0: 1, 1: (q * q - 1) // 2})
            for value in tables.extension_elements:
                if value == (0, 0):
                    continue
                power = (1, 0)
                for _ in range(q * q - 1):
                    power = scan.fq2_multiply(
                        power, value, q, tables.nonsquare
                    )
                self.assertEqual(power, (1, 0))

    def test_character_sum_coefficients_match_direct_samples(self) -> None:
        samples = {
            3: ((0, 1, 0, 0, 0, 1), (1, 0, 0, 0, 0, 1)),
            5: ((0, 1, 0, 0, 0, 1), (0, 1, 0, 0, 1, 1)),
            7: ((0, 1, 0, 0, 0, 1), (0, 1, 0, 0, 1, 1)),
        }
        for q, conductors in samples.items():
            tables = scan.build_field_tables(q)
            for conductor in conductors:
                self.assertTrue(scan.is_squarefree_quintic(conductor, q))
                a, b = scan.coefficients_from_character_sums(conductor, tables)
                self.assertEqual(
                    pilot.l_coefficients(conductor, q),
                    (1, a, b, q * a, q * q),
                )


class FrozenScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = scan.build_fixture()
        cls.by_q = {family["q"]: family for family in cls.fixture["families"]}

    def test_exact_counts_moments_and_signs(self) -> None:
        expected = {
            3: {
                "members": 162,
                "a2_sum": 384,
                "a4_sum": 2112,
                "a2b_sum": 1584,
                "b_sum": 372,
                "b2_sum": 1776,
                "K_sum": -624,
                "K_mean": [-104, 27],
                "normalized_mean": [-104, 243],
                "signs": {"negative": 102, "zero": 12, "positive": 48},
            },
            5: {
                "members": 2500,
                "a2_sum": 10560,
                "a4_sum": 116880,
                "a2b_sum": 84240,
                "b_sum": 10480,
                "b2_sum": 92680,
                "K_sum": -39880,
                "K_mean": [-1994, 125],
                "normalized_mean": [-1994, 3125],
                "signs": {"negative": 1650, "zero": 50, "positive": 800},
            },
            7: {
                "members": 14406,
                "a2_sum": 88704,
                "a4_sum": 1503936,
                "a2b_sum": 1059744,
                "b_sum": 88452,
                "b2_sum": 1139208,
                "K_sum": -518280,
                "K_mean": [-12340, 343],
                "normalized_mean": [-12340, 16807],
                "signs": {"negative": 9702, "zero": 336, "positive": 4368},
            },
        }
        for q, control in expected.items():
            family = self.by_q[q]
            self.assertEqual(family["candidate_count"], q**5)
            self.assertEqual(family["member_count"], control["members"])
            self.assertEqual(family["member_count"], q**5 - q**4)
            self.assertEqual(family["moments"]["a_squared"]["sum"], control["a2_sum"])
            self.assertEqual(family["moments"]["a_fourth"]["sum"], control["a4_sum"])
            self.assertEqual(
                family["moments"]["a_squared_b"]["sum"], control["a2b_sum"]
            )
            self.assertEqual(family["moments"]["b"]["sum"], control["b_sum"])
            self.assertEqual(family["moments"]["b_squared"]["sum"], control["b2_sum"])
            self.assertEqual(family["moments"]["K"]["sum"], control["K_sum"])
            self.assertEqual(family["moments"]["K"]["mean"], control["K_mean"])
            self.assertEqual(
                family["moments"]["normalized_K"]["mean"], control["normalized_mean"]
            )
            self.assertEqual(family["sign_counts"], control["signs"])
            self.assertEqual(sum(family["K_histogram"].values()), control["members"])
            self.assertEqual(
                {
                    name: Fraction(*value)
                    for name, value in family["low_weight_character_means"].items()
                },
                scan.candidate_low_weight_character_means(q),
            )

    def test_witnesses_cover_all_signs_and_are_exact(self) -> None:
        for q, family in self.by_q.items():
            for sign, predicate in (
                ("negative", lambda value: value < 0),
                ("zero", lambda value: value == 0),
                ("positive", lambda value: value > 0),
            ):
                witness = family["witnesses"][sign]
                self.assertTrue(predicate(witness["K"]))
                self.assertEqual(witness["K"], q * witness["a"] ** 2 - witness["b"] ** 2)
                self.assertEqual(
                    Fraction(*witness["normalized_K"]),
                    Fraction(witness["K"], q * q),
                )

    def test_q3_scan_matches_existing_exact_fixture(self) -> None:
        control = self.fixture["q3_existing_fixture_control"]
        self.assertTrue(all(control["comparisons"].values()))
        existing = json.loads(
            (FUNCTION_FIELD / "genus2_f3_quintics.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            self.by_q[3]["K_histogram"],
            existing["family_statistics"]["toy_minor_numerator_histogram"],
        )

    def test_closed_form_and_first_moment_limit_are_proof_bound(self) -> None:
        self.assertEqual(self.fixture["closed_formula_target"]["status"], scan.FORMULA_STATUS)
        self.assertFalse(self.fixture["closed_formula_target"]["not_a_theorem"])
        self.assertEqual(
            self.fixture["usp4_limit_target"]["status"], scan.MEAN_LIMIT_STATUS
        )
        self.assertFalse(self.fixture["usp4_limit_target"]["not_a_theorem"])
        profile = self.fixture["closed_formula_target"]["low_weight_character_profile"]
        self.assertEqual(profile["status"], "PROVED_FROM_EXACT_COEFFICIENT_MOMENTS")
        self.assertEqual(profile["mean_chi_(0,1)"], "-1/q+1/q^2-1/q^4")
        self.assertEqual(profile["mean_chi_(2,0)"], "1/q^3-1/q^4")
        self.assertEqual(profile["mean_chi_(0,2)"], "-1/q-1/q^5")
        self.assertEqual(profile["mean_chi_(2,1)"], "2/q^3-1/q^4-2/q^5")
        self.assertEqual(profile["mean_chi_(4,0)"], "-3/q^5")
        proof = self.fixture["closed_formula_target"]["proof"]
        self.assertEqual(proof["symbolic_operations"], scan.moment_identity.build_certificate().operations_used)
        self.assertLess(proof["symbolic_operations"], proof["operation_cap"])
        self.assertTrue(
            all(all(checks.values()) for checks in proof["scan_regression_controls"].values())
        )
        for family in self.fixture["families"]:
            self.assertTrue(
                all(entry["matches"] for entry in family["formula_comparison"].values())
            )
            q = family["q"]
            self.assertEqual(
                Fraction(*family["moments"]["a_fourth"]["mean"]),
                scan.candidate_mean_a_fourth(q),
            )
            self.assertEqual(
                Fraction(*family["moments"]["a_squared_b"]["mean"]),
                scan.candidate_mean_a_squared_b(q),
            )
            self.assertEqual(
                Fraction(*family["moments"]["b"]["mean"]),
                scan.candidate_mean_b(q),
            )

    def test_negative_sign_density_corollary_is_exact_and_scope_limited(self) -> None:
        corollary = self.fixture["negative_proportion_corollary"]
        self.assertEqual(
            corollary["status"], "PROVED_FROM_EXACT_MEAN_AND_USP4_RANGE"
        )
        self.assertEqual(corollary["scope"], "every odd prime power q")
        self.assertEqual(corollary["range_lower_bound"], -20)
        self.assertEqual(
            corollary["certified_moment_bridge"],
            "-sum_D K_D=q*(q-1)*P(q)",
        )
        self.assertEqual(
            corollary["frozen_lower_bound_regressions"],
            {"3": [26, 1215], "5": [997, 31250], "7": [617, 16807]},
        )
        self.assertEqual(corollary["liminf_lower_bound"], [1, 20])
        self.assertIn("does not determine the sign law", corollary["scope_boundary"])

    def test_family_algorithm_has_no_runtime_or_numeric_root_payload(self) -> None:
        encoded = json.dumps(self.fixture, sort_keys=True).lower()
        self.assertNotIn("runtime_seconds", encoded)
        self.assertNotIn("elapsed_seconds", encoded)
        self.assertIn("numerical root finding", encoded)
        self.assertIn("per-member euler coefficient enumeration", encoded)
        self.assertTrue(self.fixture["resource_contract"]["runtime_not_in_identity"])

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "genus2_q_scan.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, self.fixture)


class ResourceGuardTests(unittest.TestCase):
    def test_larger_q_and_candidate_overflow_are_refused_before_scan(self) -> None:
        with self.assertRaisesRegex(ValueError, "frozen exact scan"):
            scan.scan_q(11)
        with self.assertRaisesRegex(ValueError, "above candidate cap"):
            scan.scan_q(7, candidate_cap=10_000)
        with self.assertRaisesRegex(ValueError, "wall limit"):
            scan.scan_q(3, wall_limit_seconds=8.1)

    def test_monotonic_wall_guard_aborts(self) -> None:
        class AdvancingClock:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self) -> float:
                self.calls += 1
                return 0.0 if self.calls == 1 else 8.0

        with self.assertRaisesRegex(TimeoutError, "monotonic wall deadline"):
            scan.scan_q(
                3,
                wall_limit_seconds=8.0,
                guard_interval=1,
                clock=AdvancingClock(),
            )


if __name__ == "__main__":
    unittest.main()

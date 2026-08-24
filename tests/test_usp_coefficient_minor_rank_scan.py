"""Regression tests for the exact low-rank coefficient-minor audit."""

from __future__ import annotations

import json
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import usp_coefficient_minor_rank_scan as scan  # noqa: E402


class UspCoefficientMinorRankScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = scan.build_fixture()

    def test_dual_jacobi_trudi_laurent_identity(self) -> None:
        guard = scan.ResourceGuard()
        for rank in scan.FROZEN_RANKS:
            minor = scan.reciprocal_centre_minor(rank, guard)
            rectangle = scan.dual_jacobi_trudi_rectangle(rank, guard)
            self.assertEqual(minor, scan.scale(rectangle, -1))

    def test_rank_decompositions(self) -> None:
        expected = {
            1: [([2], 1, 3)],
            2: [([0, 0], 1, 1), ([0, 1], 1, 5), ([0, 2], 1, 14)],
            3: [([2, 0, 0], 1, 21), ([1, 0, 1], 1, 70), ([0, 0, 2], 1, 84)],
        }
        for row in self.fixture["rank_audits"]:
            actual = [
                (
                    item["highest_weight_fundamental_basis"],
                    item["multiplicity"],
                    item["dimension"],
                )
                for item in row["restricted_character_decomposition"]
            ]
            self.assertCountEqual(actual, expected[row["rank"]])

    def test_centre_minor_moments(self) -> None:
        expected = {
            1: [0, 1, -1, 3],
            2: [-1, 3, -11, 56],
            3: [0, 3, -15, 377],
        }
        for row in self.fixture["rank_audits"]:
            self.assertEqual(
                row["hankel_minor_haar_moments_1_through_4"],
                expected[row["rank"]],
            )
            self.assertTrue(row["alternating_weak_sign_verified"])
            self.assertTrue(row["even_moments_strictly_positive"])

    def test_fixed_depth_rank_boundary_and_moments(self) -> None:
        rows = {
            row["rank"]: row
            for row in self.fixture["fixed_depth_two_probe"]["rank_audits"]
        }
        self.assertEqual(rows[1]["honest_orientation"], "e_1^2-e_2^2")
        self.assertEqual(rows[1]["original_probe_moments_1_through_4"], [0, 1, 1, 3])
        self.assertEqual(rows[2]["original_probe_moments_1_through_4"], [-1, 3, -11, 56])
        self.assertEqual(rows[3]["original_probe_moments_1_through_4"], [-1, 7, -87, 2051])
        for rank in (2, 3):
            self.assertEqual(rows[rank]["honest_character_decomposition"][0]["notation"], "trivial")

    def test_balanced_virtual_all_order_formula_frozen_rungs(self) -> None:
        record = self.fixture["usp4_balanced_virtual_probe"]
        self.assertEqual(record["frozen_moments_1_through_6"], [0, 2, 0, 12, 0, 100])
        for order, moment in enumerate(record["frozen_moments_1_through_6"], start=1):
            expected = (
                0
                if order % 2
                else math.comb(order, order // 2) ** 2 // (order // 2 + 1)
            )
            self.assertEqual(moment, expected)
        law = record["compact_law_factorization"]
        self.assertEqual(law["support"], [-4, 4])
        self.assertEqual(
            law["sign_probabilities"],
            {"negative": [1, 2], "zero": [0, 1], "positive": [1, 2]},
        )
        for r in range(21):
            arcsine_moment = math.comb(2 * r, r)
            semicircle_moment = arcsine_moment // (r + 1)
            self.assertEqual(
                arcsine_moment * semicircle_moment,
                math.comb(2 * r, r) ** 2 // (r + 1),
            )

    def test_balanced_virtual_character_identity(self) -> None:
        guard = scan.ResourceGuard()
        first = scan.elementary_character(2, 1)
        second = scan.elementary_character(2, 2)
        balanced = scan.add_scaled(
            scan.scale(scan.multiply(first, first, guard), 2),
            scan.multiply(second, second, guard),
            -1,
            guard,
        )
        engine = scan.CnCharacterEngine(2, guard)
        virtual = scan.add_scaled(
            engine.character((2, 0)), engine.character((2, 2)), -1, guard
        )
        self.assertEqual(balanced, virtual)

    def test_balanced_finite_family_mean_bridge(self) -> None:
        bridge = self.fixture["usp4_balanced_virtual_probe"][
            "finite_genus_two_family_bridge"
        ]
        self.assertEqual(
            bridge["frozen_specializations"],
            [
                {"q": 3, "exact_mean": [88, 243]},
                {"q": 5, "exact_mean": [646, 3125]},
                {"q": 7, "exact_mean": [2444, 16807]},
            ],
        )
        q_scan = json.loads(
            (FUNCTION_FIELD / "genus2_q_scan.json").read_text(encoding="utf-8")
        )
        for family, specialization in zip(
            q_scan["families"], bridge["frozen_specializations"]
        ):
            channels = family["low_weight_character_means"]
            reconstructed = Fraction(*channels["chi_(2,0)"]) - Fraction(
                *channels["chi_(0,2)"]
            )
            self.assertEqual(
                reconstructed, Fraction(*specialization["exact_mean"])
            )

    def test_balanced_moment_formula_from_independent_sparse_density(self) -> None:
        # This deliberately does not use the producer's Laurent multiplication.
        def local_multiply(left: dict[tuple[int, int], int], right: dict[tuple[int, int], int]):
            result: dict[tuple[int, int], int] = {}
            for (a, b), left_coefficient in left.items():
                for (c, d), right_coefficient in right.items():
                    key = (a + c, b + d)
                    result[key] = result.get(key, 0) + left_coefficient * right_coefficient
            return {key: value for key, value in result.items() if value}

        density = {(0, 0): 1}
        for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
            density = local_multiply(
                density,
                {
                    (0, 0): 2,
                    root: -1,
                    (-root[0], -root[1]): -1,
                },
            )
        self.assertEqual(density[(0, 0)], 8)
        self.assertFalse(
            any(density.get((a, b), 0) for a in (-2, 2) for b in (-2, 2))
        )
        relevant_even = {
            exponent: coefficient
            for exponent, coefficient in density.items()
            if all(value % 4 == 0 for value in exponent)
        }
        self.assertEqual(
            relevant_even,
            {(-4, 0): -2, (0, -4): -2, (0, 0): 8, (0, 4): -2, (4, 0): -2},
        )

        def one_variable_coefficient(power: int, exponent: int) -> int:
            # Coefficient of x^exponent in (x^2+x^-2)^power.
            numerator = power - exponent // 2
            if exponent % 2 or numerator % 2:
                return 0
            index = numerator // 2
            return math.comb(power, index) if 0 <= index <= power else 0

        for power in range(1, 41):
            numerator = sum(
                coefficient
                * one_variable_coefficient(power, -exponent[0])
                * one_variable_coefficient(power, -exponent[1])
                for exponent, coefficient in density.items()
            )
            self.assertEqual(numerator % 8, 0)
            moment = ((-1) ** power) * numerator // 8
            expected = (
                0
                if power % 2
                else math.comb(power, power // 2) ** 2 // (power // 2 + 1)
            )
            self.assertEqual(moment, expected)

    def test_checked_in_fixture_replays_exactly(self) -> None:
        expected = json.loads(
            (FUNCTION_FIELD / "usp_coefficient_minor_rank_scan.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(self.fixture, expected)

    def test_source_and_dependency_locks(self) -> None:
        producer = self.fixture["producer"]
        self.assertEqual(producer["source_sha256_lf_normalized"], scan._source_sha256())
        self.assertEqual(
            producer["note_sha256_lf_normalized"],
            scan._lf_normalized_file_sha256(scan.NOTE_PATH),
        )
        self.assertEqual(
            producer["checker_sha256_lf_normalized"],
            scan._lf_normalized_file_sha256(scan.CHECKER_PATH),
        )
        for lock in self.fixture["dependency_locks"].values():
            path = FUNCTION_FIELD / lock["path"]
            self.assertEqual(
                lock["sha256_lf_normalized"], scan._lf_normalized_file_sha256(path)
            )

    def test_resource_contract_remains_light(self) -> None:
        observed = self.fixture["resource_contract"]["observed_counts"]
        caps = self.fixture["resource_contract"]["hard_caps"]
        self.assertTrue(all(observed[key] < caps[key] for key in caps))
        self.assertFalse(self.fixture["resource_contract"]["numerical_integration"])
        self.assertFalse(self.fixture["resource_contract"]["finite_field_enumeration"])

    def test_resource_caps_fail_closed(self) -> None:
        guard = scan.ResourceGuard()
        guard.limits["laurent_pair_products"] = 0
        with self.assertRaisesRegex(RuntimeError, "resource cap exceeded"):
            scan.multiply({(0,): 1}, {(0,): 1}, guard)


if __name__ == "__main__":
    unittest.main()

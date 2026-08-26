"""Exact replay tests for the genus-two B3 primitive trace theorem."""

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

import genus2_b3_primitive_trace_average as subject


def _poly_add(left: list[list[int]], right: list[list[int]]) -> list[Fraction]:
    size = max(len(left), len(right))
    result = []
    for index in range(size):
        left_value = Fraction(*left[index]) if index < len(left) else Fraction(0)
        right_value = Fraction(*right[index]) if index < len(right) else Fraction(0)
        result.append(left_value + right_value)
    while len(result) > 1 and not result[-1]:
        result.pop()
    return result


class Genus2B3PrimitiveTraceAverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_all_field_theorem_is_closed(self) -> None:
        self.assertEqual(self.fixture["status"], "PROVED_EXACT_ALL_ODD_PRIME_POWERS")
        self.assertEqual(
            self.fixture["b3_total_low_to_high"],
            [
                [0, 1],
                [1, 1],
                [8, 1],
                [3, 1],
                [-20, 1],
                [1, 1],
                [16, 1],
                [-13, 1],
                [4, 1],
            ],
        )
        theorem = self.fixture["theorem"]
        self.assertEqual(theorem["chi_(0,3)_mean"], "(q^4-2*q-1)/q^6")
        self.assertEqual(theorem["marked_stack_trace"], "T_(0,3)(q)=q^4-2*q-1")

    def test_theorem_matches_frozen_exhaustive_controls(self) -> None:
        source = json.loads(
            subject.HIGH_WEIGHT_FIXTURE_PATH.read_text(encoding="utf-8")
        )
        controls = source["finite_aggregate_controls"]
        expected_sums = {3: 8_256, 5: 788_080, 7: 14_205_744}
        expected_traces = {3: 74, 5: 614, 7: 2_386}
        coefficients = [
            Fraction(*pair) for pair in self.fixture["b3_total_low_to_high"]
        ]
        self.assertEqual({row["q"] for row in controls}, set(expected_sums))
        for row in controls:
            q = row["q"]
            evaluated = sum(
                coefficient * q**degree
                for degree, coefficient in enumerate(coefficients)
            )
            self.assertEqual(evaluated, expected_sums[q])
            self.assertEqual(row["frozen_new_raw_sums"]["b_cubed"], expected_sums[q])
            self.assertEqual(
                row["channel_means"]["chi_(0,3)"], [expected_traces[q], q**6]
            )

    def test_four_radical_degree_blocks_sum_coefficientwise(self) -> None:
        expected = {
            "0": [[value, 1] for value in subject.EXPECTED_DEGREE_BLOCKS[0]],
            "2": [[value, 1] for value in subject.EXPECTED_DEGREE_BLOCKS[2]],
            "4": [[value, 1] for value in subject.EXPECTED_DEGREE_BLOCKS[4]],
            "6": [[value, 1] for value in subject.EXPECTED_DEGREE_BLOCKS[6]],
        }
        self.assertEqual(self.fixture["radical_degree_blocks"], expected)
        total: list[list[int]] = [[0, 1]]
        for degree in ("0", "2", "4", "6"):
            values = _poly_add(total, expected[degree])
            total = [[value.numerator, value.denominator] for value in values]
        self.assertEqual(total, self.fixture["b3_total_low_to_high"])

    def test_signature_ledger_is_complete_and_reconstructs_blocks(self) -> None:
        rows = self.fixture["signature_ledger"]
        self.assertEqual(len(rows), 23)
        self.assertEqual(len({row["signature"] for row in rows}), 23)
        counts = {
            degree: sum(row["radical_degree"] == degree for row in rows)
            for degree in (0, 2, 4, 6)
        }
        self.assertEqual(counts, {0: 4, 2: 10, 4: 5, 6: 4})
        audit = self.fixture["ordered_triple_signature_audit"]
        self.assertEqual(
            audit["radical_degree_census"], {"0": 4, "2": 10, "4": 5, "6": 4}
        )
        self.assertEqual(
            audit["weighted_type_count_low_to_high"],
            [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [1, 1]],
        )
        for degree in (0, 2, 4, 6):
            aggregate: list[list[int]] = [[0, 1]]
            for row in rows:
                if row["radical_degree"] == degree:
                    values = _poly_add(
                        aggregate, row["weighted_contribution_low_to_high"]
                    )
                    aggregate = [
                        [value.numerator, value.denominator] for value in values
                    ]
            self.assertEqual(
                aggregate, self.fixture["radical_degree_blocks"][str(degree)]
            )

    def test_primitive_p1_p2_bridge_is_coefficientwise_exact(self) -> None:
        rows = self.fixture["primitive_type_aggregates"]
        self.assertEqual(len(rows), 7)
        self.assertEqual(
            {(row["linear_prime_count"], row["quadratic_prime_count"]) for row in rows},
            {(4, 0), (2, 1), (0, 2), (6, 0), (4, 1), (2, 2), (0, 3)},
        )
        for row in rows:
            count_plus_s1 = _poly_add(
                row["count_low_to_high"], row["sum_s1_low_to_high"]
            )
            self.assertEqual(
                [[value.numerator, value.denominator] for value in count_plus_s1],
                row["sum_p1_low_to_high"],
            )
            twice_p2_minus_p1 = []
            size = max(len(row["sum_p2_low_to_high"]), len(row["sum_p1_low_to_high"]))
            for index in range(size):
                p2 = (
                    Fraction(*row["sum_p2_low_to_high"][index])
                    if index < len(row["sum_p2_low_to_high"])
                    else Fraction(0)
                )
                p1 = (
                    Fraction(*row["sum_p1_low_to_high"][index])
                    if index < len(row["sum_p1_low_to_high"])
                    else Fraction(0)
                )
                twice_p2_minus_p1.append(2 * (p2 - p1))
            moment_sum = _poly_add(
                row["sum_s1_squared_low_to_high"], row["sum_s2_low_to_high"]
            )
            while len(twice_p2_minus_p1) > 1 and not twice_p2_minus_p1[-1]:
                twice_p2_minus_p1.pop()
            self.assertEqual(twice_p2_minus_p1, moment_sum)

    def test_lower_moment_bridge_closes_chi03(self) -> None:
        self.assertEqual(
            self.fixture["cleared_chi_sum_low_to_high"],
            [[0, 1], [1, 1], [1, 1], [-2, 1], [0, 1], [-1, 1], [1, 1]],
        )

    def test_no_enumeration_and_caps_are_literal(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["family_members_consumed"], 0)
        self.assertEqual(scope["numeric_approximations"], 0)
        contract = self.fixture["resource_contract"]
        self.assertEqual(contract["actual_signatures"], 23)
        self.assertEqual(contract["actual_primitive_types"], 7)
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertEqual(contract["maximum_symbolic_operations_and_input_atoms"], 4096)

    def test_fixture_payload_and_sources_are_locked(self) -> None:
        frozen = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.fixture)
        payload = dict(frozen)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        for record in frozen["source_manifest"]:
            path = ROOT / record["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                record["sha256_lf_normalized"], hashlib.sha256(normalized).hexdigest()
            )

    def test_invalid_symbolic_domains_are_rejected(self) -> None:
        guard = subject.AlgebraGuard(subject.time.monotonic() + 1)
        with self.assertRaises(ValueError):
            subject._elementary_sign_sum(9, subject.ONE, subject.ONE, guard)
        with self.assertRaises(ValueError):
            subject._parse_signature("not-a-B3-signature")


if __name__ == "__main__":
    unittest.main()

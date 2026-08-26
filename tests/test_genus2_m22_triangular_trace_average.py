"""Exact replay tests for the genus-two M22 triangular trace theorem."""

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

import genus2_m22_triangular_trace_average as subject


def _add_pairs(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = max(len(left), len(right))
    values = []
    for index in range(size):
        left_value = Fraction(*left[index]) if index < len(left) else Fraction(0)
        right_value = Fraction(*right[index]) if index < len(right) else Fraction(0)
        values.append(left_value + right_value)
    while len(values) > 1 and not values[-1]:
        values.pop()
    return [[value.numerator, value.denominator] for value in values]


class Genus2M22TriangularTraceAverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_all_field_m22_theorem_is_closed(self) -> None:
        self.assertEqual(self.fixture["status"], "PROVED_EXACT_ALL_ODD_PRIME_POWERS")
        self.assertEqual(
            self.fixture["M22_total_low_to_high"],
            [
                [0, 1],
                [3, 1],
                [21, 1],
                [2, 1],
                [-50, 1],
                [14, 1],
                [24, 1],
                [-19, 1],
                [5, 1],
            ],
        )
        theorem = self.fixture["theorem"]
        self.assertEqual(theorem["chi_(2,2)_mean"], "(2*q^3-q^2-2*q-2)/q^6")
        self.assertEqual(theorem["marked_stack_trace_chi_(2,2)"], "2*q^3-q^2-2*q-2")

    def test_theorem_matches_frozen_exhaustive_controls(self) -> None:
        source = json.loads(
            subject.b3.HIGH_WEIGHT_FIXTURE_PATH.read_text(encoding="utf-8")
        )
        payload = dict(source)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject.b3._canonical_sha256(payload))
        self.assertEqual(claimed, subject.b3.EXPECTED_HIGH_WEIGHT_PAYLOAD_SHA256)
        expected_sums = {3: 8_352, 5: 857_040, 7: 16_117_248}
        expected_traces = {3: 37, 5: 213, 7: 621}
        coefficients = [
            Fraction(*pair) for pair in self.fixture["M22_total_low_to_high"]
        ]
        controls = source["finite_aggregate_controls"]
        self.assertEqual({row["q"] for row in controls}, set(expected_sums))
        for row in controls:
            q = row["q"]
            evaluated = sum(
                coefficient * q**degree
                for degree, coefficient in enumerate(coefficients)
            )
            self.assertEqual(evaluated, expected_sums[q])
            self.assertEqual(
                row["frozen_new_raw_sums"]["a_squared_b_squared"], expected_sums[q]
            )
            self.assertEqual(
                row["channel_means"]["chi_(2,2)"], [expected_traces[q], q**6]
            )

    def test_twenty_signatures_exhaust_q6(self) -> None:
        audit = self.fixture["ordered_tuple_signature_audit"]
        self.assertEqual(audit["signature_count"], 20)
        self.assertEqual(
            audit["radical_degree_census"], {"0": 4, "2": 8, "4": 5, "6": 3}
        )
        self.assertEqual(
            audit["weighted_type_count_low_to_high"],
            [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [1, 1]],
        )

    def test_radical_blocks_sum_to_theorem(self) -> None:
        blocks = self.fixture["radical_degree_blocks"]
        expected = {
            str(degree): [[value, 1] for value in coefficients]
            for degree, coefficients in subject.EXPECTED_DEGREE_BLOCKS.items()
        }
        self.assertEqual(blocks, expected)
        total = [[0, 1]]
        for degree in ("0", "2", "4", "6"):
            total = _add_pairs(total, blocks[degree])
        self.assertEqual(total, self.fixture["M22_total_low_to_high"])

    def test_row_ledger_reconstructs_each_radical_block(self) -> None:
        rows = self.fixture["signature_ledger"]
        self.assertEqual(len(rows), 20)
        self.assertEqual(len({row["signature"] for row in rows}), 20)
        for degree in (0, 2, 4, 6):
            aggregate = [[0, 1]]
            for row in rows:
                if row["radical_degree"] == degree:
                    aggregate = _add_pairs(
                        aggregate, row["weighted_contribution_low_to_high"]
                    )
            self.assertEqual(
                aggregate, self.fixture["radical_degree_blocks"][str(degree)]
            )

    def test_triangular_character_subtraction_is_exact(self) -> None:
        bridge = self.fixture["triangular_character_bridge"]
        self.assertEqual(
            bridge["cleared_R22_sum_low_to_high"],
            [[0, 1], [3, 1], [1, 1], [-3, 1], [-3, 1], [1, 1], [1, 1]],
        )
        self.assertEqual(
            bridge["cleared_chi_(0,3)_sum_low_to_high"],
            [[0, 1], [1, 1], [1, 1], [-2, 1], [0, 1], [-1, 1], [1, 1]],
        )
        self.assertEqual(
            bridge["cleared_chi_(2,2)_sum_low_to_high"],
            [[0, 1], [2, 1], [0, 1], [-1, 1], [-3, 1], [2, 1]],
        )

    def test_no_enumeration_sampling_or_cap_overrun(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["family_members_consumed"], 0)
        self.assertEqual(scope["sampled_q_values_used"], 0)
        contract = self.fixture["resource_contract"]
        self.assertEqual(contract["actual_signatures"], 20)
        self.assertEqual(contract["actual_primitive_types"], 7)
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertEqual(contract["maximum_symbolic_operations_and_input_atoms"], 4096)

    def test_source_locked_b3_dependency_is_current(self) -> None:
        source = self.fixture["reused_primitive_aggregate_lemma"]
        self.assertEqual(
            source["source_payload_sha256"],
            subject.EXPECTED_PAYLOAD_SHA256["B3_fixture"],
        )
        self.assertFalse(source["new_fitted_or_sampled_primitive_average"])

    def test_fixture_payload_and_source_manifest(self) -> None:
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

    def test_malformed_source_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            subject._normalize_m22_rows({})


if __name__ == "__main__":
    unittest.main()

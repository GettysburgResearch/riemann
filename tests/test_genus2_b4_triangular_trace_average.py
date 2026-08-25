"""Exact replay tests for the genus-two B4 triangular trace theorem."""

from __future__ import annotations

import hashlib
import json
import sys
import time
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_b4_triangular_trace_average as subject


def _evaluate(pairs: list[list[int]], q: int) -> Fraction:
    return sum(
        (Fraction(*pair) * q**degree for degree, pair in enumerate(pairs)),
        Fraction(0),
    )


class Genus2B4TriangularTraceAverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_all_field_b4_and_chi04_theorems_are_closed(self) -> None:
        self.assertEqual(self.fixture["status"], "PROVED_EXACT_ALL_ODD_PRIME_POWERS")
        theorem = self.fixture["theorem"]
        self.assertEqual(
            theorem["B4_total"],
            "sum_D b_D^4=q*(q-1)*(10*q^7-29*q^6+21*q^5+44*q^4-47*q^3-56*q^2-10*q-1)",
        )
        self.assertEqual(theorem["chi_(0,4)_mean"], "-(2*q^2+1)/q^7")
        self.assertEqual(theorem["marked_stack_trace_chi_(0,4)"], "-(2*q^2+1)")

    def test_theorem_matches_all_frozen_and_held_out_controls(self) -> None:
        expected = {
            3: 45_552,
            5: 8_278_480,
            7: 221_057_088,
            11: 16_219_859_920,
            13: 77_445_995_952,
        }
        coefficients = self.fixture["B4_total_low_to_high"]
        for q, total in expected.items():
            self.assertEqual(_evaluate(coefficients, q), total)
        held_out = self.fixture["held_out_falsification_controls"]
        self.assertEqual({row["q"] for row in held_out}, {11, 13})
        for row in held_out:
            self.assertEqual(row["difference"], 0)
            self.assertFalse(row["theorem_input"])
            self.assertEqual(row["observed_sum_b_fourth"], expected[row["q"]])

    def test_fifty_four_signatures_exhaust_q8(self) -> None:
        audit = self.fixture["ordered_tuple_signature_audit"]
        self.assertEqual(audit["signature_count"], 54)
        self.assertEqual(
            audit["radical_degree_census"],
            {"0": 9, "2": 16, "4": 17, "6": 7, "8": 5},
        )
        self.assertEqual(
            audit["weighted_type_count_low_to_high"],
            [[0, 1]] * 8 + [[1, 1]],
        )
        rows = self.fixture["signature_ledger"]
        self.assertEqual(len(rows), 54)
        self.assertEqual(len({row["signature"] for row in rows}), 54)

    def test_level_two_descent_keeps_only_the_marked_root_channel(self) -> None:
        certificate = self.fixture["level2_descent_certificate"]
        coefficients = certificate["weighted_total_coefficients"]
        self.assertEqual(coefficients["M_111_2"], [[8274, 1], [-3096, 1], [252, 1]])
        self.assertEqual(coefficients["M_12_2"], [[2286, 1], [-960, 1], [84, 1]])
        self.assertEqual(coefficients["M_111_4"], [[234, 1], [-27, 1]])
        self.assertEqual(coefficients["M_12_4"], [[78, 1], [-9, 1]])
        for key in ("M_111_6", "M_111_8", "M_12_6", "M_12_8"):
            self.assertEqual(coefficients[key], [[0, 1]])
        for q in (3, 5, 17):
            self.assertEqual(
                _evaluate(coefficients["M_111_4"], q),
                3 * _evaluate(coefficients["M_12_4"], q),
            )

    def test_marked_root_lemma_is_serialized_exactly(self) -> None:
        lemma = self.fixture["marked_root_cubic_lemma"]
        expected = {
            "Legendre_second_moment": lambda q: (q - 3) * (q + 1),
            "M_111_2": lambda q: q * (q - 1) * (q - 3) * (q + 1) // 6,
            "M_12_2": lambda q: q * (q - 1) ** 2 * (q + 1) // 2,
            "three_M_111_4_plus_M_12_4": (
                lambda q: 2 * q * (q - 1) * (q + 1) * (q**2 - 2 * q - 1)
            ),
        }
        for q in (3, 5, 7, 11):
            for key, formula in expected.items():
                self.assertEqual(_evaluate(lemma[key], q), formula(q))
        partition_sum = [[0, 1]]
        guard = subject.b3.AlgebraGuard(time.monotonic() + 1)
        aggregate = subject.b3.ZERO
        for pairs in lemma["four_point_collision_partitions"].values():
            aggregate = subject.b3._add(
                aggregate, subject._parse_polynomial(pairs), guard
            )
        partition_sum = subject.b3._polynomial_pairs(aggregate)
        self.assertEqual(partition_sum, lemma["unrestricted_translated_fourth_moment"])

    def test_triangular_character_bridge_is_denominator_free(self) -> None:
        bridge = self.fixture["triangular_character_bridge"]
        cleared = bridge["cleared_chi_(0,4)_sum_low_to_high"]
        for q in (3, 5, 7, 11):
            self.assertEqual(_evaluate(cleared, q), -q * (q - 1) * (2 * q**2 + 1))

    def test_source_locked_packet_a_is_current(self) -> None:
        frozen = json.loads(subject.THIRD_FIXTURE_PATH.read_text(encoding="utf-8"))
        payload = dict(frozen)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        self.assertEqual(claimed, subject.EXPECTED_THIRD_PAYLOAD_SHA256)
        locked_sources = {
            "fixture": subject.THIRD_FIXTURE_PATH,
            "producer": subject.THIRD_PRODUCER_PATH,
            "note": subject.THIRD_NOTE_PATH,
            "test": subject.THIRD_TEST_PATH,
        }
        for key, path in locked_sources.items():
            self.assertEqual(
                subject._lf_normalized_sha256(path),
                subject.EXPECTED_THIRD_LF_SHA256[key],
            )

    def test_no_enumeration_sampling_or_cap_overrun(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated_by_theorem_replay"], 0)
        self.assertEqual(scope["family_members_consumed_by_theorem_replay"], 0)
        self.assertEqual(scope["sampled_q_values_used_as_theorem_input"], 0)
        contract = self.fixture["resource_contract"]
        self.assertEqual(contract["actual_signatures"], 54)
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertEqual(contract["maximum_symbolic_operations_and_input_atoms"], 4096)

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

    def test_malformed_sources_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            subject._normalize_b4_rows({})
        with self.assertRaises(ValueError):
            subject._parse_signature("not-a-B4-signature")


if __name__ == "__main__":
    unittest.main()

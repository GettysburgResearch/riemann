"""Focused checks for the bounded genus-two second-moment roadmap."""

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

import genus2_second_moment_reduction as subject  # noqa: E402


class GenusTwoSecondMomentReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_signature_counts_weights_and_tuple_totals(self) -> None:
        blocks = self.fixture["signature_blocks"]
        self.assertEqual(blocks["M22"]["signature_count"], 20)
        self.assertEqual(blocks["B4"]["signature_count"], 54)
        self.assertEqual(
            blocks["M22"]["weighted_tuple_count_coefficients_low_to_high"],
            [[0, 1]] * 6 + [[1, 1]],
        )
        self.assertEqual(
            blocks["B4"]["weighted_tuple_count_coefficients_low_to_high"],
            [[0, 1]] * 8 + [[1, 1]],
        )
        self.assertTrue(
            all(
                row["tuple_weight"] > 0
                for block in blocks.values()
                for row in block["signatures"]
            )
        )

        m22 = {row["signature"]: row for row in blocks["M22"]["signatures"]}
        b4 = {row["signature"]: row for row in blocks["B4"]["signatures"]}
        self.assertEqual(m22["L[6].Q[-]"]["tuple_weight"], 1)
        self.assertEqual(m22["L[1,1].Q[2]"]["tuple_weight"], 2)
        self.assertEqual(b4["L[-].Q[4]"]["tuple_weight"], 1)
        self.assertEqual(b4["L[-].Q[1,1,1,1]"]["tuple_weight"], 24)
        self.assertEqual(
            b4["L[1,1,1,1,1,1,1,1].Q[-]"]["tuple_weight"], 2520
        )

    def test_type_count_polynomials_have_exact_integer_specializations(self) -> None:
        for block in self.fixture["signature_blocks"].values():
            for row in block["signatures"]:
                coefficients = [
                    Fraction(*pair)
                    for pair in row["type_count"]["coefficients_low_to_high"]
                ]
                for q_text, expected in row["type_count"]["specializations"].items():
                    q = int(q_text)
                    value = Fraction(0)
                    for coefficient in reversed(coefficients):
                        value = value * q + coefficient
                    self.assertEqual(value, expected)
                    self.assertGreaterEqual(expected, 0)

    def test_master_reduction_and_frozen_histogram_checks(self) -> None:
        self.assertEqual(
            self.fixture["master_reduction"]["formula"],
            "sum_D K_D^2=q^2*A4(q)-2*q*M22(q)+B4(q)",
        )
        expected = {
            3: (14448, [2408, 2187], 2112, -4560, [-760, 2187], [-16, 27], [536, 2187]),
            5: (2630080, [131504, 78125], 116880, -291920, [-14596, 78125], [-174, 625], [7154, 78125]),
            7: (69108480, [1645440, 823543], 1503936, -4584384, [-109152, 823543], [-428, 2401], [37652, 823543]),
        }
        for row in self.fixture["finite_histogram_checks"]:
            q = row["q"]
            self.assertEqual(
                (
                    row["sum_K_squared"],
                    row["normalized_second_moment_Z"],
                    row["sum_a_fourth"],
                    row["unresolved_B4_minus_2qM22"],
                    row["normalized_virtual_character_obstruction"],
                    row["exact_low_weight_character_correction"],
                    row["normalized_honest_high_weight_packet"],
                ),
                expected[q],
            )

    def test_weyl_alternant_decompositions_and_single_obstruction(self) -> None:
        certificate = self.fixture["character_certificate"]
        self.assertIn("Weyl-alternant", certificate["method"])
        self.assertEqual(
            certificate["trace_fourth"]["formula"],
            "(Tr U)^4=3*chi_00+5*chi_01+6*chi_20+2*chi_02+3*chi_21+chi_40",
        )
        self.assertEqual(certificate["trace_fourth"]["dimension_checksum"], 256)
        mixed = certificate["mixed_trace_middle"]
        self.assertEqual(
            mixed["formula"],
            "(Tr U)^2*e_2(U)=2*chi_00+3*chi_01+3*chi_20+chi_02+chi_21",
        )
        self.assertEqual(mixed["dimension_checksum"], 96)
        self.assertEqual(
            mixed["arithmetic_normalization"],
            "a_D^2*b_D/q^2=(Tr U)^2*e_2(U)",
        )
        self.assertEqual(
            certificate["statistic_squared"]["haar_second_moment_target"], 3
        )
        self.assertEqual(
            certificate["statistic_squared"]["dimension_checksum"], 400
        )
        obstruction = certificate["single_virtual_character_obstruction"]
        self.assertEqual(obstruction["dimension_checksum"], 144)
        self.assertEqual(
            obstruction["status"],
            "EXACT_REDUCTION_UNRESOLVED_FOR_GENERAL_Q",
        )
        self.assertEqual(
            sum(
                row["multiplicity"]
                for row in obstruction["decomposition"]
                if row["highest_weight_a_b"] == [0, 0]
            ),
            0,
        )
        refined = certificate["refined_honest_high_weight_obstruction"]
        self.assertEqual(
            refined["status"],
            "EXACT_REDUCTION_USING_PROVED_LOW_WEIGHT_MEANS",
        )
        self.assertEqual(refined["formula"], "H=chi_04+chi_22+2*chi_03")
        self.assertEqual(refined["dimension_checksum"], 196)
        self.assertEqual(
            refined["exact_low_weight_average"],
            "mean(L)=-1/q-1/q^2-6/q^3+6/q^4",
        )

    def test_payload_source_locks_and_checked_in_replay(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "genus2_second_moment_reduction.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.fixture)
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(subject._canonical_sha256(payload), claimed)
        for source in self.fixture["source_locks"].values():
            if "sha256_lf_normalized" not in source:
                continue
            path = ROOT / source["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(normalized).hexdigest(), source["sha256_lf_normalized"]
            )

    def test_resource_guards_and_scope_firewalls(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["actual_signatures"], 74)
        self.assertLess(resources["exact_operations_used"], subject.MAX_OPERATIONS)
        self.assertEqual(resources["field_enumeration"], "FORBIDDEN_AND_NOT_IMPORTED")
        self.assertTrue(any("not an all-q" in value for value in self.fixture["firewalls"]))
        self.assertTrue(any("not interpolation" in value for value in self.fixture["firewalls"]))

        with self.assertRaisesRegex(ValueError, "operation limit"):
            subject.build_fixture(operation_limit=subject.MAX_OPERATIONS + 1)
        with self.assertRaises(subject.ResourceLimitError):
            subject.build_fixture(operation_limit=100)

        class AdvancingClock:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self) -> float:
                self.calls += 1
                return 0.0 if self.calls == 1 else subject.MAX_WALL_SECONDS + 1.0

        with self.assertRaisesRegex(TimeoutError, "monotonic wall deadline"):
            subject.build_fixture(clock=AdvancingClock())

        source = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertNotIn("import genus2_q_scan", source)
        self.assertNotIn("build_field_tables", source)
        self.assertNotIn("is_squarefree_quintic", source)


if __name__ == "__main__":
    unittest.main()

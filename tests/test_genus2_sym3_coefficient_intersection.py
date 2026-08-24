"""Independent exact tests for the genus-two/Sym^3 intersection packet."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_sym3_coefficient_intersection as subject  # noqa: E402


def direct_residual(a: int, b: int, q: int) -> int:
    return -q * a**4 + q * a * a * b + q * q * a * a + b**3 - 2 * q * b * b


class Genus2Sym3CoefficientIntersectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.families = {
            row["q"]: row
            for row in cls.fixture["frozen_atom_transform"]["families"]
        }

    def test_scaled_equation_parameterization_and_sign_bridge(self) -> None:
        # Independently substitute every integral induced shape on a bounded grid.
        for q in range(1, 18):
            for t in range(-12, 13):
                a = Fraction(2 * q * t - t**3, q)
                b = Fraction(t**4 - 3 * q * t * t + 2 * q * q, q)
                both_integral = a.denominator == 1 and b.denominator == 1
                self.assertEqual(both_integral, t**3 % q == 0)
                self.assertEqual(subject.shape_from_trace(t, q), (a, b))
                if both_integral:
                    self.assertEqual(direct_residual(a.numerator, b.numerator, q), 0)
                    self.assertEqual(
                        subject.scaled_curve_residual(a.numerator, b.numerator, q),
                        0,
                    )

        # Source convention: t=3,q=3 maps to a=-3, not +3.
        self.assertEqual(subject.shape_from_trace(3, 3), (Fraction(-3), Fraction(6)))
        self.assertEqual(subject.shape_from_trace(-3, 3), (Fraction(3), Fraction(6)))

    def test_generic_inverse_and_cross_multiplied_certificates(self) -> None:
        for q in (3, 5, 7, 9):
            for a in range(-8, 9):
                for b in range(-4, 22):
                    d = a * a - b
                    n = a * (q - b)
                    G = direct_residual(a, b, q)
                    left1 = n**3 - 2 * q * n * d**2 + q * a * d**3
                    right1 = a * (q - a * a) * G
                    self.assertEqual(left1, right1)
                    multiplier2 = (
                        a**4 * b
                        - 2 * q * a**4
                        + q * a * a * b
                        + q * q * a * a
                        - q * b * b
                    )
                    left2 = n**4 - 3 * q * n * n * d**2 + (2 * q * q - q * b) * d**4
                    self.assertEqual(left2, multiplier2 * G)

        for q, a, b, t in ((3, -3, 6, 3), (3, 3, 6, -3), (5, 0, 10, 0), (7, 0, 14, 0)):
            self.assertEqual(subject.generic_trace_parameter(a, b, q), t)
            self.assertEqual(subject.shape_from_trace(t, q), (a, b))

    def test_exceptional_divisor_and_all_three_ghost_nodes(self) -> None:
        for q in range(1, 15):
            for a in range(-8, 9):
                b = a * a
                self.assertEqual(
                    subject.scaled_curve_residual(a, b, q),
                    a * a * (a * a - q) ** 2,
                )

        for q in (3, 5, 7, 9, 15):
            zero = subject.classify_atom(0, 0, q, {})
            self.assertEqual(zero["classification"], "compact_curve_ghost_node_(0,0)")
            self.assertFalse(zero["source_witnessed_arithmetic_sym3_origin"])

        for a in (-3, 3):
            side = subject.classify_atom(a, 9, 9, {})
            self.assertEqual(side["classification"], "compact_curve_ghost_side_node")
            self.assertIn(side["normalized_node"], [[-1, 1], [1, 1]])

        with self.assertRaisesRegex(ValueError, "undefined"):
            subject.generic_trace_parameter(0, 0, 5)

    def test_odd_prime_candidate_classification(self) -> None:
        for p, expected in ((3, (-3, 0, 3)), (5, (0,)), (7, (0,)), (11, (0,)), (13, (0,))):
            independent = tuple(
                t
                for t in range(-2 * p, 2 * p + 1)
                if t**3 % p == 0 and t * t <= 4 * p
            )
            self.assertEqual(independent, expected)
            self.assertEqual(subject.odd_prime_integral_shape_trace_candidates(p), expected)

        with self.assertRaisesRegex(ValueError, "odd prime"):
            subject.odd_prime_integral_shape_trace_candidates(2)
        with self.assertRaisesRegex(ValueError, "odd prime"):
            subject.odd_prime_integral_shape_trace_candidates(9)

    def test_all_251_atoms_are_preserved_and_independently_reclassified(self) -> None:
        balanced = json.loads(subject.BALANCED_FIXTURE.read_text(encoding="utf-8"))
        source_families = {
            row["q"]: row
            for row in balanced["frozen_enumeration_facts"]["families"]
        }
        self.assertEqual(sum(row["source_atom_count"] for row in self.families.values()), 251)

        for q, transformed_family in self.families.items():
            source_atoms = source_families[q]["joint_a_D_b_D_law"]["atoms"]
            transformed = transformed_family["transformed_atoms"]
            self.assertEqual(len(source_atoms), len(transformed))
            for source, row in zip(source_atoms, transformed):
                self.assertEqual(
                    (source["a_D"], source["b_D"], source["member_count"], source["member_fraction"]),
                    (row["a_D"], row["b_D"], row["member_count"], row["member_fraction"]),
                )
                residual = direct_residual(row["a_D"], row["b_D"], q)
                self.assertEqual(row["scaled_curve_residual"], residual)
                self.assertEqual(row["on_compact_sym3_curve"], residual == 0)

    def test_exact_frozen_intersections_and_member_counts(self) -> None:
        expected = {
            3: {
                "summary": (32, 162, 3, 18, 2, 6, 1, 12),
                "hits": [
                    (-3, 6, 3, 3, 1),
                    (0, 0, 12, None, None),
                    (3, 6, 3, -3, 1),
                ],
                "fractions": ([1, 9], [1, 27], [2, 27]),
                "candidate_presence": [(-3, (3, 6), 3), (0, (0, 6), 0), (3, (-3, 6), 3)],
            },
            5: {
                "summary": (81, 2500, 2, 55, 1, 5, 1, 50),
                "hits": [(0, 0, 50, None, None), (0, 10, 5, 0, 20)],
                "fractions": ([11, 500], [1, 500], [1, 50]),
                "candidate_presence": [(0, (0, 10), 5)],
            },
            7: {
                "summary": (138, 14406, 2, 378, 1, 42, 1, 336),
                "hits": [(0, 0, 336, None, None), (0, 14, 42, 0, 42)],
                "fractions": ([9, 343], [1, 343], [8, 343]),
                "candidate_presence": [(0, (0, 14), 42)],
            },
        }
        for q, control in expected.items():
            family = self.families[q]
            summary = family["classification_summary"]
            self.assertEqual(
                (
                    family["source_atom_count"],
                    family["source_member_count"],
                    summary["on_curve_atom_count"],
                    summary["on_curve_member_count"],
                    summary["source_witnessed_atom_count"],
                    summary["source_witnessed_member_count"],
                    summary["ghost_atom_count"],
                    summary["ghost_member_count"],
                ),
                control["summary"],
            )
            self.assertEqual(
                (
                    summary["on_curve_member_fraction"],
                    summary["source_witnessed_member_fraction"],
                    summary["ghost_member_fraction"],
                ),
                control["fractions"],
            )
            hits = []
            for row in family["on_curve_atoms"]:
                t = row.get("generic_trace_parameter_t")
                hits.append(
                    (
                        row["a_D"],
                        row["b_D"],
                        row["member_count"],
                        None if t is None else Fraction(*t).numerator,
                        row.get("elliptic_source_trace_witness_member_count"),
                    )
                )
            self.assertEqual(hits, control["hits"])
            candidates = [
                (
                    row["elliptic_trace_t"],
                    tuple(row["coefficient_shape_a_b"]),
                    row["locked_member_count"],
                )
                for row in family["odd_prime_arithmetic_shape_candidates"]
            ]
            self.assertEqual(candidates, control["candidate_presence"])

        totals = self.fixture["frozen_atom_transform"]["aggregate_audit_totals"]
        self.assertEqual(totals["source_atom_count"], 251)
        self.assertEqual(totals["source_member_count"], 17068)
        self.assertEqual(
            totals["atom_counts_by_classification"],
            {
                "compact_curve_ghost_node_(0,0)": 3,
                "off_compact_sym3_coefficient_curve": 244,
                "source_witnessed_arithmetic_sym3_coefficient_shape": 4,
            },
        )
        self.assertEqual(
            totals["member_counts_by_classification"],
            {
                "compact_curve_ghost_node_(0,0)": 398,
                "off_compact_sym3_coefficient_curve": 16617,
                "source_witnessed_arithmetic_sym3_coefficient_shape": 53,
            },
        )

    def test_source_locks_negative_controls_and_scope_firewall(self) -> None:
        locks = self.fixture["source_locks"]
        for name, path, expected_payload in (
            ("balanced_control_fixture", subject.BALANCED_FIXTURE, subject.EXPECTED_BALANCED_PAYLOAD_SHA256),
            ("elliptic_sym3_fixture", subject.SYM3_FIXTURE, subject.EXPECTED_SYM3_PAYLOAD_SHA256),
        ):
            text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
            self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), locks[name]["file_sha256_lf_normalized"])
            source = json.loads(text)
            self.assertEqual(source["payload_sha256"], expected_payload)
            unhashed = dict(source)
            claimed = unhashed.pop("payload_sha256")
            self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        negative = self.fixture["negative_controls"]
        self.assertEqual(negative["generic_usp4_boundary_point"]["scaled_curve_residual"], "-16q^3")
        for q in (3, 5, 7, 11):
            self.assertEqual(subject.scaled_curve_residual(0, -2 * q, q), -16 * q**3)
        self.assertEqual(len(negative["locked_off_curve_witnesses"]), 3)
        self.assertEqual(self.fixture["scope_firewall"]["conjectural"], [])
        self.assertIn("no RH or GRH implication", self.fixture["scope_firewall"]["nonclaims"])

    def test_stored_fixture_payload_producer_hashes_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (Path(subject.__file__), "script_sha256_lf_normalized"),
            (subject.NOTE_PATH, "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
            self.assertEqual(hashlib.sha256(text.encode()).hexdigest(), producer[field])

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(self.fixture)
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_curve_or_field_enumerations"], 0)
        self.assertEqual(resources["source_atoms_transformed"], 251)
        self.assertLessEqual(resources["source_atoms_transformed"], resources["source_atom_cap"])
        self.assertLessEqual(resources["source_members_represented"], resources["source_member_cap"])


if __name__ == "__main__":
    unittest.main()

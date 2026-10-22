"""Independent exact tests for tensor/symmetric-power subtorus rigidity."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_tensor_symmetric_power_subtorus_rigidity as subject  # noqa: E402


def independent_weights(r: int, a: int, b: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            epsilon * a + b * (r - 2 * j)
            for epsilon in (-1, 1)
            for j in range(r + 1)
        )
    )


def independent_target(r: int, c: int = 1) -> tuple[int, ...]:
    return tuple(sorted(c * value for value in range(-(2 * r + 1), 2 * r + 2, 2)))


def independent_solutions(r: int, c: int = 1) -> set[tuple[int, int]]:
    scale = abs(c)
    return {
        *((sign_a * scale * (r + 1), sign_b * scale) for sign_a in (-1, 1) for sign_b in (-1, 1)),
        *((sign_a * scale, sign_b * 2 * scale) for sign_a in (-1, 1) for sign_b in (-1, 1)),
    }


class EllipticTensorSymmetricPowerSubtorusRigidityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_canonical_weight_decompositions_beyond_frozen_range(self) -> None:
        for r in range(1, 97):
            target = independent_target(r)
            for a, b in independent_solutions(r):
                with self.subTest(r=r, a=a, b=b):
                    self.assertEqual(independent_weights(r, a, b), target)
                    self.assertTrue(subject.is_scaled_spectral_solution(r, a, b))
            self.assertEqual(
                set(subject.predicted_scaled_solutions(r)), independent_solutions(r)
            )

    def test_independent_complete_search_in_small_proof_forced_boxes(self) -> None:
        for r in range(1, 13):
            bound = 2 * r + 1
            target = independent_target(r)
            found = {
                (a, b)
                for a in range(-bound, bound + 1)
                for b in range(-bound, bound + 1)
                if independent_weights(r, a, b) == target
            }
            self.assertEqual(found, independent_solutions(r))

    def test_scaled_target_classification_and_divisibility(self) -> None:
        for r in range(1, 25):
            for c in (-5, -2, -1, 1, 3, 4):
                target = independent_target(r, c)
                predicted = set(subject.predicted_scaled_solutions(r, c))
                self.assertEqual(predicted, independent_solutions(r, c))
                for a, b in predicted:
                    self.assertEqual(independent_weights(r, a, b), target)
                    self.assertEqual(a % abs(c), 0)
                    self.assertEqual(b % abs(c), 0)

    def test_zero_and_overlap_multiplicity_corners(self) -> None:
        for r in range(1, 17):
            for nonzero in (1, 2, r + 1):
                weights_a_zero = independent_weights(r, 0, nonzero)
                weights_b_zero = independent_weights(r, nonzero, 0)
                self.assertLess(len(set(weights_a_zero)), len(weights_a_zero))
                self.assertLess(len(set(weights_b_zero)), len(weights_b_zero))

            for a in range(1, 2 * r + 2):
                for b in range(1, 2 * r + 2):
                    plus = {a + b * (r - 2 * j) for j in range(r + 1)}
                    minus = {-a + b * (r - 2 * j) for j in range(r + 1)}
                    direct = bool(plus & minus)
                    predicted = a % b == 0 and a // b <= r
                    self.assertEqual(direct, predicted)
                    self.assertEqual(subject.cross_branch_overlap(r, a, b), predicted)

        zero_target = independent_target(5, 0)
        self.assertEqual(independent_weights(5, 0, 0), zero_target)
        for a, b in ((1, 0), (0, 1), (1, 1), (-2, 3)):
            self.assertNotEqual(independent_weights(5, a, b), zero_target)

    def test_independent_weyl_signs_and_r1_swap_orbit(self) -> None:
        for r, a, b in ((1, 2, 1), (2, 3, 1), (7, 1, 2), (19, 20, 1)):
            base = subject.tensor_weight_multiset(r, a, b)
            self.assertEqual(base, subject.tensor_weight_multiset(r, -a, b))
            self.assertEqual(base, subject.tensor_weight_multiset(r, a, -b))
            self.assertEqual(base, subject.tensor_weight_multiset(r, -a, -b))

        for a in range(-5, 6):
            for b in range(-5, 6):
                self.assertEqual(independent_weights(1, a, b), independent_weights(1, b, a))
        for r in range(2, 20):
            self.assertNotEqual(independent_weights(r, 1, r + 1), independent_target(r))
            self.assertNotEqual(independent_weights(r, 2, 1), independent_target(r))

    def test_dickson_recurrence_and_graph_equations(self) -> None:
        expected = {
            0: (2,),
            1: (0, 1),
            2: (-2, 0, 1),
            3: (0, -3, 0, 1),
            4: (2, 0, -4, 0, 1),
            5: (0, 5, 0, -5, 0, 1),
        }
        for degree, coefficients in expected.items():
            self.assertEqual(subject.dickson_trace_coefficients(degree), coefficients)

        for degree in range(0, 25):
            coefficients = subject.dickson_trace_coefficients(degree)
            for z in (-5, -2, 0, 1, 4):
                direct = sum(value * z**power for power, value in enumerate(coefficients))
                self.assertEqual(subject.dickson_trace_value(degree, z), direct)

        graph = self.fixture["dickson_chebyshev_graph_equations"]
        self.assertIn("x=D_(r+1)(z)", graph["first_graph"])
        self.assertIn("y=D_2(z)=z^2-2", graph["second_graph"])
        self.assertIn("delta_u+r*delta_v=0 mod 2", graph["central_sign_note"])

    def test_frozen_regression_counts_and_exact_rows(self) -> None:
        replay = self.fixture["bounded_exact_regression"]
        self.assertEqual(replay["maximum_r"], 16)
        self.assertEqual(len(replay["rows"]), 16)
        self.assertEqual(
            sum(row["signed_candidate_pairs_checked"] for row in replay["rows"]),
            27_344,
        )
        self.assertEqual(
            sum(row["weight_atoms_emitted"] for row in replay["rows"]),
            720_816,
        )
        for row in replay["rows"]:
            r = row["r"]
            self.assertEqual(row["proof_forced_coordinate_bound"], 2 * r + 1)
            self.assertEqual(row["solution_count"], 8)
            self.assertEqual(
                {tuple(pair) for pair in row["solutions_a_b"]},
                independent_solutions(r),
            )

        large = self.fixture["large_r_direct_canonical_checks"]["rows"]
        self.assertEqual([row["r"] for row in large], [32, 64])
        for row in large:
            self.assertFalse(row["candidate_box_enumerated"])
            self.assertEqual(row["canonical_signed_solutions_checked"], 8)
            self.assertEqual(row["weight_count_per_solution"], 2 * row["r"] + 2)
            self.assertEqual(
                {tuple(pair) for pair in row["solutions_a_b"]},
                independent_solutions(row["r"]),
            )

    def test_predecessor_payload_and_all_file_locks(self) -> None:
        lock = self.fixture["predecessor_source_lock"]
        predecessor_fixture_path = ROOT / lock["fixture_path"]
        predecessor_producer_path = ROOT / lock["producer_path"]
        fixture_bytes = predecessor_fixture_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        producer_bytes = predecessor_producer_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        self.assertEqual(hashlib.sha256(fixture_bytes).hexdigest(), lock["fixture_sha256_lf_normalized"])
        self.assertEqual(hashlib.sha256(producer_bytes).hexdigest(), lock["producer_sha256_lf_normalized"])
        predecessor = json.loads(predecessor_fixture_path.read_text(encoding="utf-8"))
        self.assertEqual(predecessor["schema"], lock["fixture_schema"])
        self.assertEqual(predecessor["payload_sha256"], lock["fixture_payload_sha256"])

        for owned in self.fixture["source_and_owned_file_locks"]["owned_file_locks"].values():
            path = ROOT / owned["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), owned["sha256_lf_normalized"])

    def test_payload_resources_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))
        resources = stored["resource_contract"]
        ledger = resources["accounted_work_unit_ledger"]
        self.assertEqual(ledger["bounded_signed_candidate_pairs"], 27_344)
        self.assertEqual(ledger["large_r_direct_canonical_solution_checks"], 16)
        self.assertLess(
            ledger["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["bounded_weight_atoms_emitted"], 720_816)
        self.assertLessEqual(
            resources["bounded_weight_atoms_emitted"],
            resources["bounded_weight_atom_cap_inclusive"],
        )
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["runtime_symbolic_packages"], 0)

        def reject_floats(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_floats(item)
            elif isinstance(value, list):
                for item in value:
                    reject_floats(item)

        reject_floats(stored)

    def test_note_scope_integrity_and_source_has_no_asserts(self) -> None:
        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        self.assertEqual(text.count(r"\["), text.count(r"\]"))
        self.assertEqual(text.count("```"), 2)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))
        for anchor in (
            "W_r(a,b)=O_r",
            "Nonprimitive target exponent",
            "D_{n+1}(z)=zD_n(z)-D_{n-1}(z)",
            "q^{r/2}T",
            "720{,}816",
            "root of unity",
            "full rational coefficient intersection",
            "RH, or GRH",
        ):
            self.assertIn(anchor, text)
        source = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(?m)^\s*assert\b", source))

    def test_strict_refusals_survive_optimized_python(self) -> None:
        for malformed in (True, Fraction(1), "1", 1.0, None):
            with self.subTest(value=malformed):
                with self.assertRaises(TypeError):
                    subject.tensor_weight_multiset(malformed, 1, 1)
        for invalid_r in (0, -1, subject.EXPLICIT_WEIGHT_MAX_R + 1):
            with self.assertRaises(ValueError):
                subject.tensor_weight_multiset(invalid_r, 1, 1)
        with self.assertRaises(ValueError):
            subject.target_weight_multiset(2, 0)
        with self.assertRaises(ValueError):
            subject.predicted_scaled_solutions(2, 0)
        with self.assertRaises(ValueError):
            subject.cross_branch_overlap(2, 0, 1)
        with self.assertRaises(ValueError):
            subject.cross_branch_overlap(2, 1, 0)
        with self.assertRaises(ValueError):
            subject.dickson_trace_coefficients(subject.DICKSON_MAX_DEGREE + 1)
        with self.assertRaises(ValueError):
            subject.build_fixture(31)
        with self.assertRaises(TypeError):
            subject.build_fixture(True)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard(5).charge("deliberate_refusal", 5)


if __name__ == "__main__":
    unittest.main()

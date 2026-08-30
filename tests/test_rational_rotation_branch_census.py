from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "rational_rotation_branch_census.py"
SPEC = importlib.util.spec_from_file_location(
    "rational_rotation_branch_census", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load rational-rotation branch census")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError(f"unexpected float {value!r}")
    if isinstance(value, dict):
        for child in value.values():
            reject_float(child)
    elif isinstance(value, list):
        for child in value:
            reject_float(child)


class RationalRotationBranchCensusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_integer_orbit_skeleton_exhaustively(self) -> None:
        for b in range(2, 18):
            for a in range(1, b):
                if math.gcd(a, b) != 1:
                    continue
                row = subject.orbit_skeleton(a, b)
                states = row["sine_signs_for_n_1_through_2b"]
                self.assertEqual(len(states), 2 * b)
                self.assertEqual(row["zero_n_indices"], [b, 2 * b])
                self.assertIn(1, states)
                self.assertIn(-1, states)
                multiplier = -1 if a % 2 else 1
                self.assertEqual(
                    states[b:], [multiplier * state for state in states[:b]]
                )
                self.assertEqual(row["absolute_minimal_period"], b)
        self.assertEqual(subject.sine_state(1, 2, 1), 1)
        self.assertEqual(subject.sine_state(1, 2, 2), 0)
        self.assertEqual(subject.sine_state(1, 2, 3), -1)
        self.assertEqual(subject.sine_state(2, 3, 1), 1)
        self.assertEqual(subject.sine_state(2, 3, 2), -1)

    def test_branch_period_decision(self) -> None:
        self.assertEqual(subject.branch_minimal_period(2, 3, True), 3)
        self.assertEqual(subject.branch_minimal_period(2, 3, False), 3)
        self.assertEqual(subject.branch_minimal_period(1, 3, True), 3)
        self.assertEqual(subject.branch_minimal_period(1, 3, False), 6)
        table = subject.branch_period_decision_table()
        self.assertEqual(len(table), 4)
        self.assertEqual(
            [row["period_multiplier_times_b"] for row in table], [1, 1, 1, 2]
        )
        with self.assertRaisesRegex(TypeError, "boolean"):
            subject.branch_minimal_period(1, 3, 1)

    def test_zero_exponent_fourier_spectrum(self) -> None:
        for b in range(2, 20):
            constant = subject.zero_exponent_fourier_spectrum(b, 1)
            self.assertEqual(constant["minimal_recurrence_order"], 1)
            self.assertEqual(constant["reduced_denominator"], "1-T")
            self.assertEqual(
                [
                    row["root_exponent_mod_b"]
                    for row in constant["nonzero_fourier_modes"]
                ],
                [0],
            )

            missing_mean = subject.zero_exponent_fourier_spectrum(b, 1 - b)
            self.assertEqual(missing_mean["minimal_recurrence_order"], b - 1)
            self.assertEqual(
                [
                    row["root_exponent_mod_b"]
                    for row in missing_mean["nonzero_fourier_modes"]
                ],
                list(range(1, b)),
            )

            support = subject.zero_exponent_fourier_spectrum(b, 0)
            self.assertEqual(support["minimal_recurrence_order"], b)
            self.assertEqual(support["block"], [1] * (b - 1) + [0])
            self.assertEqual(support["reduced_denominator"], "1-T^b")

    def test_grouped_binomial_coefficients_and_hostile_cancellation(self) -> None:
        self.assertEqual(
            subject.grouped_binomial_coefficients(2, 5), {0: 1, 1: -2, 2: 1, 3: 0, 4: 0}
        )
        self.assertEqual(
            subject.grouped_binomial_coefficients(3, 3), {0: 0, 1: -3, 2: 3}
        )
        self.assertEqual(
            subject.grouped_binomial_coefficients(5, 5),
            {0: 0, 1: -5, 2: 10, 3: -10, 4: 5},
        )
        for b in range(2, 13):
            for k in range(1, 20):
                grouped = subject.grouped_binomial_coefficients(k, b)
                self.assertEqual(sum(grouped.values()), 0)

    def test_grouped_spectrum_equals_direct_group_ring(self) -> None:
        for b in range(2, 11):
            for a in range(1, b):
                if math.gcd(a, b) != 1:
                    continue
                for k in range(1, 12):
                    spectrum = subject.integer_power_spectrum(a, b, k)
                    roots = [
                        row["root_exponent_mod_2b"]
                        for row in spectrum["retained_modes"]
                    ]
                    self.assertEqual(len(roots), len(set(roots)))
                    self.assertEqual(spectrum["minimal_recurrence_order"], len(roots))
                    for r in range(2 * b + 1):
                        self.assertEqual(
                            subject.direct_scaled_integer_power_modes(a, b, k, r),
                            subject.grouped_scaled_integer_power_modes(a, b, k, r),
                        )
        hostile = subject.integer_power_spectrum(1, 3, 3)
        self.assertEqual(hostile["all_grouped_binomial_amplitudes"], [0, -3, 3])
        self.assertEqual(hostile["minimal_recurrence_order"], 2)

    def test_sources_manifest_and_exact_git_objects(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCES_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 4)
        self.assertEqual(
            {row["path"]: row["git_blob"] for row in source["verified_sources"]},
            subject.EXPECTED_SOURCE_OBJECTS,
        )
        references = source["external_references"]
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0]["authors"], "Oliver Knill and John Lesieutre")
        self.assertEqual(references[1]["authors"], "William Kahan")
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT,
                "research/l-families/atlas/generalized/definitely_missing",
            )

    def test_claims_parent_and_survival_firewalls(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.RATIONAL_ROTATION_ZERO_PERIOD",
                "GLO764.FIXED_BRANCH_POWER_PERIOD",
                "GLO764.ZERO_EXPONENT_CONVENTION_SPECTRUM",
                "GLO764.INTEGER_POWER_COLLISION_SPECTRUM",
            },
        )
        parent = self.fixture["non_scalar_parent"]
        self.assertIn("Sym^k", parent["integer_parent"])
        self.assertTrue(
            parent["scalar_denominator_can_merge_and_cancel_parent_weights"]
        )
        self.assertTrue(
            parent["not_identified_with_standard_symmetric_power_local_factor"]
        )
        census = self.fixture["integer_power_collision_spectrum"]
        self.assertNotIn("rows", census)
        self.assertEqual(
            census["exhaustive_row_count"],
            self.fixture["orbit_skeleton"]["reduced_rotation_count"]
            * census["maximum_k"],
        )
        self.assertGreaterEqual(len(census["representative_rows"]), 4)
        self.assertGreater(census["hostile_cancellation_row_count"], 0)
        ladder = self.fixture["survival_ladder"]["rows"]
        self.assertEqual(ladder[1]["first_failure_level"], "L1")
        self.assertEqual(ladder[3]["first_failure_level"], "L0")
        firewall = self.fixture["scope_firewall"]
        for field in (
            "one_unramified_determinant_one_local_recurrence",
            "tempered_rational_rotations_only",
            "fixed_branch_index_is_data_for_noninteger_signed_powers",
            "termwise_varying_branch_indices_excluded",
            "no_uniform_local_degree_over_unbounded_b",
            "no_global_Euler_product_completion_or_functional_equation",
            "no_automorphy_motivic_or_categorical_no_go",
            "no_RH_GRH_or_zero_distribution_consequence",
            "external_novelty_unreviewed",
        ):
            self.assertTrue(firewall[field])

    def test_resource_refusals_and_no_floats(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["arithmetic_class"], "EXACT_RATIONAL")
        self.assertEqual(resources["float_operations"], 0)
        self.assertFalse(resources["external_symbolic_engine"])
        self.assertLess(
            resources["declared_work_units"], resources["work_unit_cap_exclusive"]
        )
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=1)
        with self.assertRaisesRegex(ValueError, "max_b"):
            subject.build_fixture(max_b=21)
        with self.assertRaisesRegex(ValueError, "max_k"):
            subject.build_fixture(max_k=31)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_b=True)
        with self.assertRaisesRegex(ValueError, "lowest terms"):
            subject.orbit_skeleton(2, 4)
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.sine_state(1, 3, 0)
        with self.assertRaisesRegex(ValueError, "k > 0"):
            subject.integer_power_spectrum(1, 3, 0)

    def test_note_integrity_and_proof_gates(self) -> None:
        raw = (PACKET_ROOT / "RATIONAL_ROTATION_BRANCH_CENSUS.md").read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        for command in (r"\binom", r"\theta", r"\mathbb", r"\operatorname"):
            self.assertIn(command, note)
        self.assertFalse(
            [
                line_number
                for line_number, line in enumerate(note.splitlines(), start=1)
                if line.rstrip(" \t") != line
            ]
        )
        self.assertEqual(note.count(r"\("), note.count(r"\)"))
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 25)
        for required in (
            "analytic germ",
            "minimal period",
            "zero-exponent convention",
            "branch values agree",
            "pairwise distinct",
            "weighted observable",
            "must not be silently",
            "no claim of priority",
        ):
            self.assertIn(required, note)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = PACKET_ROOT / "rational_rotation_branch_census.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT / "RATIONAL_ROTATION_BRANCH_CENSUS.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()

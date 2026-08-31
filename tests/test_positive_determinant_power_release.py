from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "positive_determinant_power_release.py"
SPEC = importlib.util.spec_from_file_location(
    "positive_determinant_power_release", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load positive-determinant release packet")
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


class PositiveDeterminantPowerReleaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_binet_formula_matches_recurrence(self) -> None:
        pairs = (
            (Fraction(3), Fraction(2)),
            (Fraction(4), Fraction(1)),
            (Fraction(9), Fraction(4)),
            (Fraction(2), Fraction(1, 2)),
        )
        for alpha, beta in pairs:
            recurrence = subject.recurrence_sequence(
                30, alpha=alpha, beta=beta
            )
            binet = subject.binet_sequence(30, alpha=alpha, beta=beta)
            self.assertEqual(recurrence, binet, (alpha, beta))
            self.assertEqual(recurrence[:2], (Fraction(1), alpha + beta))
            self.assertTrue(all(value > 0 for value in recurrence))
            for index in range(28):
                self.assertEqual(
                    recurrence[index + 2],
                    (alpha + beta) * recurrence[index + 1]
                    - alpha * beta * recurrence[index],
                )

    def test_determinant_one_normalization_and_integer_transport(self) -> None:
        controls = (
            (Fraction(4), Fraction(1), Fraction(2)),
            (Fraction(9), Fraction(4), Fraction(6)),
            (Fraction(2), Fraction(1, 2), Fraction(1)),
        )
        for alpha, beta, scale in controls:
            original, normalized = subject.normalized_sequences(
                18,
                alpha=alpha,
                beta=beta,
                positive_sqrt_delta=scale,
            )
            for index in range(18):
                self.assertEqual(original[index], scale**index * normalized[index])
                for exponent in (-2, -1, 0, 1, 2, 3):
                    self.assertEqual(
                        original[index] ** exponent,
                        (scale**exponent) ** index * normalized[index] ** exponent,
                    )

    def test_integer_power_terms_are_exact_parent_shadow(self) -> None:
        pairs = (
            (Fraction(3), Fraction(2)),
            (Fraction(4), Fraction(1)),
            (Fraction(9), Fraction(4)),
            (Fraction(2), Fraction(1, 2)),
        )
        for alpha, beta in pairs:
            base = subject.recurrence_sequence(40, alpha=alpha, beta=beta)
            for power in range(9):
                terms = subject.integer_power_terms(
                    power, alpha=alpha, beta=beta
                )
                weights = tuple(term[1] for term in terms)
                coefficients = tuple(term[0] for term in terms)
                self.assertEqual(len(terms), power + 1)
                self.assertEqual(len(set(weights)), power + 1)
                self.assertTrue(all(weight > 0 for weight in weights))
                self.assertTrue(all(coefficient for coefficient in coefficients))
                parent = subject.power_parent_sequence(
                    power, 40, alpha=alpha, beta=beta
                )
                self.assertEqual(parent, tuple(value**power for value in base))

    def test_integer_minimal_denominator_and_tail_annihilation(self) -> None:
        for alpha, beta in (
            (Fraction(3), Fraction(2)),
            (Fraction(4), Fraction(1)),
            (Fraction(2), Fraction(1, 2)),
        ):
            base = subject.recurrence_sequence(50, alpha=alpha, beta=beta)
            for power in range(9):
                terms = subject.integer_power_terms(
                    power, alpha=alpha, beta=beta
                )
                weights = tuple(term[1] for term in terms)
                denominator = subject.denominator_from_weights(weights)
                self.assertEqual(len(denominator) - 1, power + 1)
                shadow = tuple(value**power for value in base)
                for index in range(power + 1, len(shadow)):
                    self.assertEqual(
                        subject.convolution_at(denominator, shadow, index),
                        0,
                        (alpha, beta, power, index),
                    )

    def test_fixture_corpus_and_sharp_degree(self) -> None:
        corpus = self.fixture["root_pair_corpus"]
        self.assertEqual(len(corpus), 4)
        for root_row in corpus:
            self.assertEqual(len(root_row["integer_power_rows"]), 9)
            for power, row in enumerate(root_row["integer_power_rows"]):
                self.assertEqual(row["k"], power)
                self.assertEqual(row["minimal_denominator_degree"], power + 1)
                self.assertEqual(len(row["terms"]), power + 1)
                self.assertTrue(row["all_coefficients_nonzero"])
                self.assertTrue(row["all_weights_positive_and_pairwise_distinct"])
        normalizations = self.fixture["determinant_normalization_controls"]
        self.assertEqual(len(normalizations), 3)
        self.assertTrue(
            all(
                row["all_complex_lambda_transport"]
                == "PROVED_BY_POSITIVE_LOG_ADDITIVITY_IN_NOTE"
                for row in normalizations
            )
        )

    def test_source_manifest_authenticates_exact_base_objects(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCE_MANIFEST_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 6)
        blobs = {
            row["path"]: row["git_blob"] for row in source["verified_sources"]
        }
        self.assertEqual(blobs, subject.EXPECTED_SOURCE_OBJECTS)
        self.assertFalse(source["corollary_audit"]["new_nonrationality_mechanism"])
        self.assertTrue(source["corollary_audit"]["source_theorem_is_logically_sufficient"])
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT,
                "research/l-families/atlas/definitely_missing",
            )

    def test_claims_audit_survival_and_scope_firewalls(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.POSITIVE_DETERMINANT_POWER_RATIONALITY",
                "GLO764.POSITIVE_DETERMINANT_INTEGER_MINIMAL_DENOMINATOR",
                "GLO764.POSITIVE_DETERMINANT_BRANCH_GATE",
            },
        )
        self.assertFalse(
            self.fixture["audit_verdict"]["independent_nonrationality_theorem"]
        )
        self.assertIn(
            "sqrt(delta)^lambda",
            self.fixture["audit_verdict"]["exact_relation_to_source"],
        )
        ladder = self.fixture["survival_ladder"]["rows"]
        self.assertEqual(ladder[0]["first_unresolved_level"], "L4")
        self.assertEqual(ladder[2]["first_failure_level"], "L0")
        for key in (
            "positive_distinct_real_roots_only",
            "positive_delta_and_t_strictly_above_two_sqrt_delta_only",
            "positive_real_logarithm_only",
            "positive_square_root_normalization_only",
            "coalesced_nonpositive_and_complex_determinants_excluded",
            "no_tempered_or_sign_changing_classification",
            "no_global_euler_product_or_ramified_factors",
            "no_completion_functional_equation_or_automorphy",
            "no_motive_explicit_formula_or_zero_theorem",
            "no_RH_GRH_or_zero_distribution_consequence",
        ):
            self.assertTrue(self.fixture["scope_firewall"][key])

    def test_rejects_out_of_scope_and_inexact_parameters(self) -> None:
        for alpha, beta in ((1, 1), (1, 2), (1, 0), (1, -1)):
            with self.assertRaisesRegex(ValueError, "alpha > beta > 0"):
                subject.positive_root_pair(alpha, beta)
        with self.assertRaisesRegex(TypeError, "exact integer or fraction"):
            subject.positive_root_pair(2.0, 1)
        with self.assertRaisesRegex(TypeError, "exact integer or fraction"):
            subject.positive_root_pair(True, 1)
        with self.assertRaisesRegex(ValueError, r"square to alpha\*beta"):
            subject.normalized_sequences(
                5, alpha=4, beta=1, positive_sqrt_delta=3
            )
        with self.assertRaisesRegex(ValueError, r"square to alpha\*beta"):
            subject.normalized_sequences(
                5, alpha=4, beta=1, positive_sqrt_delta=-2
            )
        with self.assertRaisesRegex(ValueError, "at least one"):
            subject.denominator_from_weights(())

    def test_resource_refusals_and_exact_arithmetic(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertEqual(resource["arithmetic_class"], "EXACT_RATIONAL")
        self.assertEqual(resource["float_operations"], 0)
        self.assertFalse(resource["external_symbolic_engine"])
        self.assertLess(
            resource["declared_work_units"], resource["work_unit_cap_exclusive"]
        )
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=resource["declared_work_units"])
        with self.assertRaisesRegex(ValueError, "through four"):
            subject.build_fixture(max_power=3)
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            subject.build_fixture(max_power=15)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_power=True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(resource_cap=True)

    def test_note_integrity_and_required_proof_gates(self) -> None:
        note_path = PACKET_ROOT / "POSITIVE_DETERMINANT_POWER_RELEASE.md"
        raw = note_path.read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        self.assertFalse(
            [
                line_number
                for line_number, line in enumerate(note.splitlines(), start=1)
                if line.rstrip(" \t") != line
            ]
        )
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        for required in (
            "independent nonrationality theorem",
            "unique positive square roots",
            "GLO764.POSITIVE_DETERMINANT_POWER_RATIONALITY",
            "GLO764.POSITIVE_DETERMINANT_INTEGER_MINIMAL_DENOMINATOR",
            "GLO764.POSITIVE_DETERMINANT_BRANCH_GATE",
            "G_{\\lambda;t,\\delta}(T)",
            "lambda\\in\\mathbb Z_{\\geq0}",
            "minimal eventual constant-coefficient recurrence order",
            "No classification in those chambers",
            "priority or external novelty is claimed",
            "no RH or GRH consequence",
        ):
            self.assertIn(required, note)
        self.assertNotIn("proves RH", note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 15)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = PACKET_ROOT / "positive_determinant_power_release.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT / "POSITIVE_DETERMINANT_POWER_RELEASE.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()

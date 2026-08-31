from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "transfer_matrix_symmetric_parent.py"
SPEC = importlib.util.spec_from_file_location(
    "transfer_matrix_symmetric_parent", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load transfer-matrix symmetric-parent packet")
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


class TransferMatrixSymmetricParentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_polynomial_product_and_denominator(self) -> None:
        self.assertEqual(
            subject.multiply_polynomials(
                (Fraction(1), Fraction(-2)),
                (Fraction(1), Fraction(-3)),
            ),
            (Fraction(1), Fraction(-5), Fraction(6)),
        )
        self.assertEqual(
            subject.denominator_from_weights((2, 3)),
            (Fraction(1), Fraction(-5), Fraction(6)),
        )
        with self.assertRaisesRegex(ValueError, "at least one"):
            subject.multiply_polynomials((), (Fraction(1),))

    def test_symmetric_parent_identity_on_exact_grid(self) -> None:
        parameters = (
            (Fraction(3), Fraction(2), Fraction(3), Fraction(-2)),
            (Fraction(2), Fraction(1, 2), Fraction(5, 3), Fraction(-7, 4)),
            (Fraction(-2), Fraction(3), Fraction(1), Fraction(4)),
        )
        for alpha, beta, c_alpha, c_beta in parameters:
            for power in range(9):
                shadow = subject.power_shadow_sequence(
                    power,
                    25,
                    alpha=alpha,
                    beta=beta,
                    c_alpha=c_alpha,
                    c_beta=c_beta,
                )
                parent = subject.parent_matrix_coefficient_sequence(
                    power,
                    25,
                    alpha=alpha,
                    beta=beta,
                    c_alpha=c_alpha,
                    c_beta=c_beta,
                )
                self.assertEqual(shadow, parent, (parameters, power))

    def test_nonunit_determinant_recurrence_and_power_denominators(self) -> None:
        base = subject.scalar_sequence(
            30,
            alpha=Fraction(3),
            beta=Fraction(2),
            c_alpha=Fraction(3),
            c_beta=Fraction(-2),
        )
        self.assertEqual(base[:2], (Fraction(1), Fraction(5)))
        for index in range(28):
            self.assertEqual(base[index + 2], 5 * base[index + 1] - 6 * base[index])

        for power in range(9):
            terms = subject.symmetric_power_terms(
                power,
                alpha=Fraction(3),
                beta=Fraction(2),
                c_alpha=Fraction(3),
                c_beta=Fraction(-2),
            )
            weights = tuple(term[1] for term in terms)
            self.assertEqual(len(weights), power + 1)
            self.assertEqual(len(set(weights)), power + 1)
            self.assertTrue(all(term[0] for term in terms))
            denominator = subject.denominator_from_weights(weights)
            sequence = tuple(value**power for value in base)
            for index in range(power + 1, len(sequence)):
                self.assertEqual(
                    subject.convolution_at(denominator, sequence, index),
                    0,
                    (power, index),
                )

    def test_zero_eigenvalue_is_excluded_from_minimal_order_theorem(self) -> None:
        terms = subject.symmetric_power_terms(
            1,
            alpha=Fraction(0),
            beta=Fraction(1),
            c_alpha=Fraction(1),
            c_beta=Fraction(1),
        )
        weights = tuple(term[1] for term in terms)
        self.assertEqual(weights, (Fraction(0), Fraction(1)))
        self.assertEqual(len(set(weights)), 2)

        sequence = subject.power_shadow_sequence(
            1,
            6,
            alpha=Fraction(0),
            beta=Fraction(1),
            c_alpha=Fraction(1),
            c_beta=Fraction(1),
        )
        denominator = subject.denominator_from_weights(weights)
        self.assertEqual(sequence, (2, 1, 1, 1, 1, 1))
        self.assertEqual(denominator, (Fraction(1), Fraction(-1)))
        self.assertEqual(len(denominator) - 1, 1)
        self.assertNotEqual(len(denominator) - 1, 2)
        for index in range(2, len(sequence)):
            self.assertEqual(subject.convolution_at(denominator, sequence, index), 0)

        control = self.fixture["hostile_controls"]["zero_eigenvalue_transient"]
        self.assertTrue(control["weights_pairwise_distinct"])
        self.assertFalse(control["all_weights_nonzero"])
        self.assertEqual(control["generating_function"], "(2-T)/(1-T)")
        self.assertEqual(control["reduced_denominator_degree"], 1)
        self.assertEqual(control["excluded_k_plus_1_conclusion"], 2)

    def test_exponent_triangle_and_parent_dimension(self) -> None:
        for degree in range(15):
            pairs = subject.exponent_triangle(degree)
            expected = math.comb(degree + 2, 2)
            self.assertEqual(len(pairs), expected)
            self.assertEqual(len(set(pairs)), expected)
            self.assertTrue(all(left >= 0 and right >= 0 for left, right in pairs))
            self.assertTrue(all(left + right <= degree for left, right in pairs))
            self.assertEqual(
                subject.filtered_parent_dimension(range(degree + 1)), expected
            )

    def test_determinant_one_projection_is_exact_interval(self) -> None:
        for degree in range(15):
            projected = subject.determinant_one_exponents(
                subject.exponent_triangle(degree)
            )
            self.assertEqual(projected, tuple(range(-degree, degree + 1)))
            weights = subject.numerical_weights(
                subject.exponent_triangle(degree),
                alpha=Fraction(2),
                beta=Fraction(1, 2),
            )
            self.assertEqual(len(set(weights)), 2 * degree + 1)

    def test_generic_and_dependent_weight_controls(self) -> None:
        for degree in range(2, 15):
            pairs = subject.exponent_triangle(degree)
            generic = subject.numerical_weights(
                pairs, alpha=Fraction(2), beta=Fraction(3)
            )
            dependent = subject.numerical_weights(
                pairs, alpha=Fraction(2), beta=Fraction(4)
            )
            self.assertEqual(len(set(generic)), math.comb(degree + 2, 2))
            self.assertLess(len(set(dependent)), len(set(generic)))
            self.assertEqual(len(set(dependent)), 2 * degree + 1)

    def test_sparse_filtered_parent(self) -> None:
        self.assertEqual(
            subject.filtered_exponent_pairs((4, 0, 2, 4)),
            (
                (0, 0),
                (0, 2),
                (1, 1),
                (2, 0),
                (0, 4),
                (1, 3),
                (2, 2),
                (3, 1),
                (4, 0),
            ),
        )
        self.assertEqual(subject.filtered_parent_dimension((4, 0, 2, 4)), 9)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.filtered_exponent_pairs((0, -1))
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.exponent_triangle(True)

    def test_higher_rank_exponent_simplex(self) -> None:
        for rank in range(1, 7):
            for degree in range(11):
                exponents = subject.exponent_simplex(rank, degree)
                self.assertEqual(len(exponents), math.comb(rank + degree, rank))
                self.assertEqual(len(exponents), len(set(exponents)))
                self.assertTrue(all(len(row) == rank for row in exponents))
                self.assertTrue(
                    all(
                        all(coordinate >= 0 for coordinate in row)
                        and sum(row) <= degree
                        for row in exponents
                    )
                )
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.exponent_simplex(0, 3)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.exponent_simplex(True, 3)

    def test_higher_rank_determinant_quotient_formula(self) -> None:
        for rank in range(1, 7):
            for degree in range(11):
                classes = subject.determinant_one_character_classes(rank, degree)
                positive = math.comb(degree, rank) if degree >= rank else 0
                expected = math.comb(rank + degree, rank) - positive
                self.assertEqual(len(classes), expected, (rank, degree))
                self.assertTrue(all(min(row) == 0 for row in classes))

        seed = (5, 2, 7, 3)
        expected = (3, 0, 5, 1)
        self.assertEqual(subject.determinant_one_canonical_exponent(seed), expected)
        self.assertEqual(
            subject.determinant_one_canonical_exponent(
                tuple(coordinate + 11 for coordinate in seed)
            ),
            expected,
        )
        with self.assertRaisesRegex(ValueError, "nonempty"):
            subject.determinant_one_canonical_exponent(())
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.determinant_one_canonical_exponent((0, -1))

    def test_fixture_power_rows_and_spectral_prediction(self) -> None:
        power_rows = self.fixture["nonunit_determinant_power_parent"]["rows"]
        self.assertEqual(len(power_rows), 9)
        for power, row in enumerate(power_rows):
            self.assertEqual(row["k"], power)
            self.assertEqual(row["parent_dimension"], power + 1)
            self.assertEqual(row["minimal_denominator_degree"], power + 1)
            self.assertEqual(len(row["terms"]), power + 1)

        spectrum_rows = self.fixture["filtered_parent_spectrum"]["rows"]
        for degree, row in enumerate(spectrum_rows):
            triangular = math.comb(degree + 2, 2)
            self.assertEqual(row["filtered_parent_dimension"], triangular)
            self.assertEqual(
                row["generic_two_torus"]["distinct_weight_count"], triangular
            )
            self.assertEqual(
                row["determinant_one"]["distinct_weight_count"], 2 * degree + 1
            )
        self.assertIn(
            "freeing determinant",
            self.fixture["filtered_parent_spectrum"]["held_out_prediction"],
        )
        higher = self.fixture["higher_rank_determinant_quotient"]
        self.assertEqual(higher["maximum_rank"], 5)
        self.assertEqual(higher["maximum_degree"], 8)
        self.assertEqual(len(higher["rows"]), 4 * 9)
        for row in higher["rows"]:
            rank = row["rank"]
            degree = row["d"]
            positive = math.comb(degree, rank) if degree >= rank else 0
            self.assertEqual(
                row["determinant_one_character_count"],
                math.comb(rank + degree, rank) - positive,
            )

    def test_source_manifest_authenticates_inherited_packets(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCE_MANIFEST_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 5)
        self.assertEqual(
            source["verified_sources"][0]["payload_sha256"],
            "d809d5bed68618ff8dc9fd657b6c63c9cd0c8eca9ea83ffedda0b6d84a4ce7c3",
        )
        self.assertTrue(
            source["scope_firewall"]["local_finite_rank_linear_algebra_only"]
        )
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT,
                "research/l-families/atlas/definitely_missing",
            )

    def test_claims_survival_ladder_and_firewalls(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.TENSOR_PARENT_IDENTITY",
                "GLO764.GENERIC_POWER_MINIMAL_DENOMINATOR",
                "GLO764.DETERMINANT_ONE_SPECTRAL_COMPRESSION",
                "GLO764.HIGHER_RANK_DETERMINANT_QUOTIENT",
                "GLO764.FINITE_PARENT_INTERPOLATION_OBSTRUCTION",
            },
        )
        obstruction = self.fixture["finite_parent_interpolation_obstruction"]
        self.assertIn("iff", obstruction["classification"])
        self.assertIn(
            "Deligne or other complex-rank tensor categories",
            obstruction["not_excluded"],
        )
        rows = self.fixture["survival_ladder"]["rows"]
        self.assertEqual(rows[0]["first_unresolved_level"], "L4")
        self.assertEqual(rows[1]["first_failure_level"], "L1")
        self.assertTrue(
            self.fixture["literature_firewall"][
                "integer_power_recurrence_generating_functions_are_classical"
            ]
        )
        for key in (
            "local_finite_rank_linear_algebra_only",
            "integer_symmetric_powers_only",
            "matrix_coefficient_shadow_is_not_promoted_to_a_determinant_l_factor",
            "does_not_construct_a_global_Euler_product",
            "does_not_supply_ramified_factors_completion_or_functional_equation",
            "does_not_prove_automorphy_motivic_origin_or_a_zero_theorem",
            "no_RH_GRH_or_zero_distribution_consequence",
            "external_novelty_unreviewed",
        ):
            self.assertTrue(self.fixture["scope_firewall"][key])

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
            subject.build_fixture(max_degree=3)
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            subject.build_fixture(max_degree=15)
        with self.assertRaisesRegex(ValueError, "rank two"):
            subject.build_fixture(max_rank=1)
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            subject.build_fixture(max_rank=8)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_degree=True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_rank=True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(resource_cap=True)

    def test_note_integrity_and_required_proof_gates(self) -> None:
        raw = (PACKET_ROOT / "TRANSFER_MATRIX_SYMMETRIC_PARENT.md").read_bytes()
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
        self.assertGreaterEqual(note.count(r"\["), 15)
        for required in (
            "honest non-scalar object",
            "functorial in `A`",
            "not the determinant inverse itself",
            "symmetric quotient",
            "presentation with denominator",
            "alpha*beta != 0",
            "does **not**",
            "pairwise distinct",
            "determinant-one spectral compression",
            "HIGHER_RANK_DETERMINANT_QUOTIENT",
            "unique representative with minimum",
            "coordinate zero",
            "FINITE_PARENT_INTERPOLATION_OBSTRUCTION",
            "if and only if `lambda` is a nonnegative integer",
            "does not rule out nuclear operators",
            "held-out prediction",
            "multiplicatively independent",
            "external novelty not claimed",
            "no RH or GRH consequence",
        ):
            self.assertIn(required, note)
        self.assertNotIn("proves RH", note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 15)

    def test_stored_fixture_and_producer_hashes(self) -> None:
        stored_path = PACKET_ROOT / "transfer_matrix_symmetric_parent.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT / "TRANSFER_MATRIX_SYMMETRIC_PARENT.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()

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
MODULE_PATH = PACKET_ROOT / "irrational_rotation_principal_complex_power_rationality.py"
SPEC = importlib.util.spec_from_file_location(
    "irrational_rotation_principal_complex_power_rationality", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load principal complex-power packet")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def evaluate_laurent(value: subject.Laurent, alpha: Fraction) -> Fraction:
    return sum(
        Fraction(coefficient) * alpha**exponent
        for exponent, coefficient in value.items()
    )


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError(f"unexpected float {value!r}")
    if isinstance(value, dict):
        for child in value.values():
            reject_float(child)
    elif isinstance(value, list):
        for child in value:
            reject_float(child)


class IrrationalRotationPrincipalComplexPowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_scaled_integer_fourier_coefficients(self) -> None:
        self.assertEqual(subject.scaled_integer_fourier_coefficients(0), {0: 1})
        self.assertEqual(subject.scaled_integer_fourier_coefficients(1), {1: 1, -1: -1})
        self.assertEqual(
            subject.scaled_integer_fourier_coefficients(2), {2: 1, 0: -2, -2: 1}
        )
        self.assertEqual(
            subject.scaled_integer_fourier_coefficients(3),
            {3: 1, 1: -3, -1: 3, -3: -1},
        )
        for k in range(13):
            coefficients = subject.scaled_integer_fourier_coefficients(k)
            self.assertEqual(tuple(coefficients), tuple(range(k, -k - 1, -2)))
            self.assertTrue(all(coefficients.values()))
            expected_zero = 1 if k == 0 else 0
            self.assertEqual(sum(coefficients.values()), expected_zero)

    def test_symbolic_denominator_and_tail_annihilation(self) -> None:
        for k in range(11):
            denominator = subject.alpha_denominator(k)
            self.assertEqual(len(denominator), k + 2)
            self.assertEqual(denominator[0], {0: 1})
            numerator = subject.scaled_integer_power_numerator(k)
            self.assertLessEqual(len(numerator), k + 1)
            for index in range(4 * (k + 1)):
                coefficient: subject.Laurent = {}
                for degree in range(min(index, len(denominator) - 1) + 1):
                    coefficient = subject.laurent_add(
                        coefficient,
                        subject.laurent_multiply(
                            denominator[degree],
                            subject.scaled_integer_power_sequence_laurent(
                                k, index - degree
                            ),
                        ),
                    )
                expected = numerator[index] if index < len(numerator) else {}
                self.assertEqual(coefficient, expected, (k, index))

    def test_exact_rational_specialization(self) -> None:
        alpha = Fraction(2)
        for k in range(9):
            denominator = [
                evaluate_laurent(coefficient, alpha)
                for coefficient in subject.alpha_denominator(k)
            ]
            direct = [Fraction(1)]
            for frequency in range(k, -k - 1, -2):
                root = alpha**frequency
                updated = [Fraction(0)] * (len(direct) + 1)
                for degree, coefficient in enumerate(direct):
                    updated[degree] += coefficient
                    updated[degree + 1] -= coefficient * root
                direct = updated
            self.assertEqual(denominator, direct)

    def test_complex_rational_cusp_controls(self) -> None:
        zero = subject.cusp_control(Fraction(0))
        self.assertTrue(zero["smooth"])
        self.assertEqual(zero["classification"], "SEPARATE_ZERO_EXPONENT")
        for integer in range(1, 7):
            row = subject.cusp_control(Fraction(integer))
            self.assertTrue(row["smooth"])
            self.assertEqual(row["classification"], "POSITIVE_INTEGER")
        controls = {
            (Fraction(1, 2), Fraction(0)): 1,
            (Fraction(3, 2), Fraction(0)): 2,
            (Fraction(1), Fraction(1, 2)): 2,
            (Fraction(2), Fraction(-1, 3)): 3,
            (Fraction(7, 3), Fraction(5, 4)): 3,
        }
        for (real, imaginary), derivative_order in controls.items():
            row = subject.cusp_control(real, imaginary)
            self.assertFalse(row["smooth"])
            self.assertEqual(
                row["first_forced_divergent_derivative_order"], derivative_order
            )
            self.assertLess(Fraction(row["magnitude_power_at_zero"]), 0)
            self.assertNotEqual(
                (
                    row["falling_factorial"]["real"],
                    row["falling_factorial"]["imaginary"],
                ),
                ("0", "0"),
            )
        with self.assertRaisesRegex(ValueError, "domain"):
            subject.cusp_control(Fraction(0), Fraction(1))
        with self.assertRaisesRegex(ValueError, "domain"):
            subject.cusp_control(Fraction(-1, 2))

    def test_branch_controls_and_integer_minimal_orders(self) -> None:
        for value in (0, 1, 2, 7):
            row = subject.branch_control(Fraction(value))
            self.assertTrue(row["coefficient_sequence_branch_independent"])
            self.assertEqual(row["integer_multiplier_value"], "1")
        for real, imaginary in (
            (Fraction(1, 2), Fraction(0)),
            (Fraction(2, 3), Fraction(0)),
            (Fraction(1), Fraction(1, 2)),
        ):
            row = subject.branch_control(real, imaginary)
            self.assertFalse(row["coefficient_sequence_branch_independent"])
            self.assertTrue(row["all_fixed_branches_have_same_rationality_verdict"])
        rows = self.fixture["integer_power_replay"]["rows"]
        for k, row in enumerate(rows):
            self.assertEqual(row["k"], k)
            self.assertEqual(row["minimal_recurrence_order"], k + 1)
            self.assertEqual(
                row["characteristic_root_alpha_exponents"],
                list(range(k, -k - 1, -2)),
            )
            self.assertNotIn("record", row["minimal_denominator_certificate"])
        representatives = self.fixture["integer_power_replay"][
            "representative_polynomials"
        ]
        self.assertEqual([row["k"] for row in representatives], [0, 1, 2, 3, 6, 10])

    def test_sources_manifest_and_git_objects(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCES_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 6)
        self.assertEqual(
            {row["path"]: row["git_blob"] for row in source["verified_sources"]},
            subject.EXPECTED_SOURCE_OBJECTS,
        )
        references = source["external_references"]
        self.assertEqual(references[0]["authors"], "Oliver Knill and John Lesieutre")
        self.assertEqual(references[1]["authors"], "William Kahan")
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT,
                "research/l-families/atlas/generalized/definitely_missing",
            )

    def test_claims_parent_survival_and_scope(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.IRRATIONAL_FIXED_BRANCH_COMPLEX_POWER_RATIONALITY",
                "GLO764.IRRATIONAL_PRINCIPAL_POWER_MINIMAL_DENOMINATOR",
                "GLO764.NONINTEGER_POWER_FINITE_STATE_NO_GO",
            },
        )
        parent = self.fixture["non_scalar_parent"]
        self.assertIn("Sym^k", parent["parent"])
        self.assertTrue(parent["not_equal_to_standard_determinant_inverse"])
        self.assertTrue(
            parent[
                "infinite_dimensional_categorical_and_nonlinear_parents_not_ruled_out"
            ]
        )
        rows = self.fixture["survival_ladder"]["rows"]
        self.assertEqual(rows[0]["first_failure_level"], "L0")
        self.assertEqual(rows[2]["first_unresolved_level"], "L4")
        firewall = self.fixture["scope_firewall"]
        for field in (
            "one_unramified_determinant_one_local_recurrence",
            "tempered_irrational_rotation_only",
            "fixed_real_axis_branch_required_for_nonintegers",
            "lambda_zero_or_strictly_positive_real_part_only",
            "no_verdict_for_nonzero_lambda_with_nonpositive_real_part",
            "finite_dimensional_constant_state_space_no_go_only",
            "no_global_Euler_product_completion_or_functional_equation",
            "no_automorphy_motivic_or_infinite_dimensional_no_go",
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
        with self.assertRaisesRegex(ValueError, "max_k"):
            subject.build_fixture(max_k=19)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_k=True)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.alpha_denominator(-1)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.scaled_integer_power_sequence_laurent(2, -1)
        with self.assertRaisesRegex(TypeError, "Fraction"):
            subject.cusp_control(Fraction(1), 0)

    def test_note_integrity_and_proof_gates(self) -> None:
        raw = (
            PACKET_ROOT / "IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md"
        ).read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        for command in (r"\binom", r"\theta", r"\mathbb", r"\widehat"):
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
        self.assertGreaterEqual(len(displays), 30)
        for required in (
            "analytic germ",
            "single real-axis logarithm branch",
            "tail is dense modulo",
            "pairwise distinct",
            "Fejér's theorem",
            "unbounded as",
            "Cayley--Hamilton",
            "constant finite-dimensional linear state-space",
            "No theorem is asserted",
            "makes no novelty claim",
        ):
            self.assertIn(required, note)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = (
            PACKET_ROOT / "irrational_rotation_principal_complex_power_rationality.json"
        )
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT
                / "IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()

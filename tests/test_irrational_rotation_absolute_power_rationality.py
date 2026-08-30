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
MODULE_PATH = PACKET_ROOT / "irrational_rotation_absolute_power_rationality.py"
SPEC = importlib.util.spec_from_file_location(
    "irrational_rotation_absolute_power_rationality", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load irrational-rotation absolute-power packet")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def evaluate_laurent(value: subject.Laurent, q: Fraction) -> Fraction:
    return sum(
        Fraction(coefficient) * q**exponent for exponent, coefficient in value.items()
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


class IrrationalRotationAbsolutePowerRationalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_even_fourier_coefficients(self) -> None:
        self.assertEqual(subject.scaled_even_fourier_coefficients(0), {0: 1})
        self.assertEqual(
            subject.scaled_even_fourier_coefficients(1),
            {-1: -1, 0: 2, 1: -1},
        )
        self.assertEqual(
            subject.scaled_even_fourier_coefficients(2),
            {-2: 1, -1: -4, 0: 6, 1: -4, 2: 1},
        )
        for m in range(9):
            coefficients = subject.scaled_even_fourier_coefficients(m)
            self.assertEqual(tuple(coefficients), tuple(range(-m, m + 1)))
            self.assertTrue(all(coefficients.values()))
            self.assertEqual(
                coefficients,
                {frequency: coefficients[-frequency] for frequency in coefficients},
            )
            expected_at_zero = 1 if m == 0 else 0
            self.assertEqual(sum(coefficients.values()), expected_at_zero)
            self.assertEqual(
                sum(
                    coefficient * (-1 if frequency % 2 else 1)
                    for frequency, coefficient in coefficients.items()
                ),
                2 ** (2 * m),
            )

    def test_q_denominator_matches_inherited_weight_product(self) -> None:
        for m in range(9):
            denominator = subject.q_denominator(m)
            inherited = [
                subject.alpha_even_laurent_to_q(coefficient)
                for coefficient in subject.PARENT.denominator_laurent(2 * m)
            ]
            self.assertEqual(denominator, inherited)
            self.assertEqual(len(denominator), 2 * m + 2)
            self.assertEqual(denominator[0], {0: 1})
            self.assertEqual(
                denominator[-1],
                {0: -1 if (2 * m + 1) % 2 else 1},
            )
            for coefficient in denominator:
                self.assertEqual(
                    coefficient,
                    {exponent: coefficient[-exponent] for exponent in coefficient},
                )

    def test_exact_tail_annihilation(self) -> None:
        for m in range(8):
            denominator = subject.q_denominator(m)
            numerator = subject.scaled_sine_power_numerator(m)
            order = 2 * m + 1
            self.assertLessEqual(len(numerator), order)
            for index in range(4 * order):
                coefficient: subject.Laurent = {}
                for degree in range(min(index, len(denominator) - 1) + 1):
                    coefficient = subject.laurent_add(
                        coefficient,
                        subject.laurent_multiply(
                            denominator[degree],
                            subject.scaled_sine_power_sequence_laurent(
                                m, index - degree
                            ),
                        ),
                    )
                expected = numerator[index] if index < len(numerator) else {}
                self.assertEqual(coefficient, expected, (m, index))

    def test_exact_numeric_specialization(self) -> None:
        q = Fraction(2)
        for m in range(7):
            denominator = [
                evaluate_laurent(coefficient, q)
                for coefficient in subject.q_denominator(m)
            ]
            direct = [Fraction(1)]
            for frequency in range(-m, m + 1):
                root = q**frequency
                updated = [Fraction(0)] * (len(direct) + 1)
                for degree, coefficient in enumerate(direct):
                    updated[degree] += coefficient
                    updated[degree + 1] -= coefficient * root
                direct = updated
            self.assertEqual(denominator, direct)

            values = [
                evaluate_laurent(
                    subject.scaled_sine_power_sequence_laurent(m, index), q
                )
                for index in range(4 * (2 * m + 1))
            ]
            numerator = [
                evaluate_laurent(coefficient, q)
                for coefficient in subject.scaled_sine_power_numerator(m)
            ]
            for index in range(len(values)):
                convolution = sum(
                    denominator[degree] * values[index - degree]
                    for degree in range(min(index, len(denominator) - 1) + 1)
                )
                expected = numerator[index] if index < len(numerator) else 0
                self.assertEqual(convolution, expected, (m, index))

    def test_minimal_order_rows_include_lambda_zero(self) -> None:
        rows = self.fixture["even_power_replay"]["rows"]
        for m, row in enumerate(rows):
            self.assertEqual(row["m"], m)
            self.assertEqual(row["lambda"], 2 * m)
            self.assertEqual(row["minimal_recurrence_order"], 2 * m + 1)
            self.assertEqual(
                row["characteristic_root_exponents_k"],
                list(range(-m, m + 1)),
            )
            self.assertTrue(row["all_fourier_coefficients_nonzero"])
            self.assertTrue(row["roots_distinct_under_theta_over_pi_irrational"])
            denominator_record = subject.t_laurent_polynomial_record(
                subject.q_denominator(m)
            )
            self.assertEqual(
                row["minimal_denominator_certificate"]["canonical_payload_sha256"],
                subject._canonical_sha256(denominator_record),
            )
            numerator = subject.scaled_sine_power_numerator(m)
            numerator_record = subject.t_laurent_polynomial_record(numerator)
            self.assertEqual(
                row["scaled_sine_power_numerator_certificate"][
                    "canonical_payload_sha256"
                ],
                subject._canonical_sha256(numerator_record),
            )
        zero = self.fixture["even_power_replay"]["lambda_zero_handled_separately"]
        self.assertEqual(zero["generating_function"], "1/(1-T)")
        self.assertEqual(zero["minimal_order"], 1)

    def test_cusp_smoothness_controls(self) -> None:
        expected = {
            Fraction(0): (True, None),
            Fraction(1, 2): (False, 1),
            Fraction(1): (False, 1),
            Fraction(3, 2): (False, 2),
            Fraction(2): (True, None),
            Fraction(5, 2): (False, 3),
            Fraction(3): (False, 3),
            Fraction(4): (True, None),
        }
        for value, verdict in expected.items():
            row = subject.cusp_smoothness_control(value)
            self.assertEqual(
                (row["smooth"], row["first_failed_derivative_order"]), verdict
            )
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.cusp_smoothness_control(Fraction(-1, 2))

    def test_rational_rotation_hostile_counterexample(self) -> None:
        row = subject.rational_rotation_counterexample()
        self.assertEqual(row["theta_over_pi"], "1/2")
        self.assertEqual(row["lambda"], "1/2")
        self.assertEqual(row["u_prefix"], [1, 0, -1, 0, 1, 0, -1, 0])
        self.assertEqual(row["absolute_power_pattern"], ["1", "0", "1", "0"])
        self.assertEqual(row["generating_function"], "1/(1-T^2)")
        self.assertIn("DESPITE_NON_EVEN", row["verdict"])

    def test_sources_manifest_and_nearby_prior_art(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCES_SHA256_LF,
        )
        self.assertEqual(
            source["imported_parent_state_commit"],
            subject.EXPECTED_IMPORTED_PARENT_COMMIT,
        )
        self.assertEqual(len(source["verified_sources"]), 4)
        fixture_source = source["verified_sources"][0]
        self.assertEqual(
            fixture_source["payload_sha256"],
            "4acc9097a55ef6eee6377f5cbc63018b361acc04ca2f3aa5767fd94f585c9e9d",
        )
        references = source["external_references"]
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0]["authors"], "Oliver Knill and John Lesieutre")
        self.assertIn("almost periodic coefficients", references[0]["title"])
        self.assertTrue(source["scope_firewall"]["rational_rotations_excluded"])

    def test_claims_survival_and_scope_firewalls(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY",
                "GLO764.IRRATIONAL_ROTATION_EVEN_POWER_MINIMAL_DENOMINATOR",
                "GLO764.DENSE_ORBIT_FINITE_SPECTRUM",
            },
        )
        gate = self.fixture["dense_orbit_fourier_gate"]
        self.assertTrue(gate["eventual_recurrence_to_translate_identity"])
        self.assertTrue(gate["tail_orbit_dense_modulo_pi"])
        self.assertTrue(gate["finite_fourier_support_implies_trigonometric_polynomial"])
        rows = self.fixture["survival_ladder"]["rows"]
        self.assertEqual(rows[0]["first_unresolved_level"], "L4")
        self.assertEqual(rows[1]["first_failure_level"], "L3")
        firewall = self.fixture["scope_firewall"]
        for field in (
            "one_unramified_determinant_one_local_recurrence",
            "tempered_irrational_rotation_only",
            "rational_rotations_excluded_and_can_be_counterexamples",
            "absolute_powers_erase_phase_and_are_not_complex_powers",
            "does_not_give_a_uniform_statement_over_primes",
            "does_not_construct_a_global_Euler_product",
            "does_not_supply_ramified_factors_completion_or_functional_equation",
            "does_not_prove_automorphy_motivic_origin_or_categorical_no_go",
            "no_RH_GRH_or_zero_distribution_consequence",
            "external_novelty_unreviewed",
        ):
            self.assertTrue(firewall[field])

    def test_resource_refusals_and_no_floats(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["arithmetic_class"], "EXACT_RATIONAL")
        self.assertIn("Fourier", resources["exact_method"])
        self.assertLess(
            resources["declared_work_units"], resources["work_unit_cap_exclusive"]
        )
        self.assertEqual(resources["float_operations"], 0)
        self.assertFalse(resources["external_symbolic_engine"])
        self.assertEqual(
            resources["prime_curve_field_zero_or_conductor_enumerations"], 0
        )
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=resources["declared_work_units"])
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            subject.build_fixture(max_m=11)
        with self.assertRaisesRegex(ValueError, "include m=0"):
            subject.build_fixture(max_m=3)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_m=True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.q_denominator(False)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.scaled_even_fourier_coefficients(-1)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.scaled_sine_power_sequence_laurent(1, -1)
        with self.assertRaisesRegex(ArithmeticError, "even alpha"):
            subject.alpha_even_laurent_to_q({1: 1})

    def test_note_integrity_and_proof_gates(self) -> None:
        raw = (
            PACKET_ROOT / "IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md"
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
        self.assertGreaterEqual(note.count(r"\["), 20)
        for required in (
            "analytic germ",
            "eventual recurrence",
            "tail of an irrational rotation orbit is dense",
            "pairwise distinct",
            "only finitely many",
            "Fejér's theorem",
            "minimal constant-coefficient recurrence order",
            "irrationality hypothesis cannot simply be dropped",
            "Oliver Knill and John Lesieutre",
            "natural-boundary",
            "no novelty claim",
        ):
            self.assertIn(required, note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 20)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = (
            PACKET_ROOT / "irrational_rotation_absolute_power_rationality.json"
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
                PACKET_ROOT / "IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()

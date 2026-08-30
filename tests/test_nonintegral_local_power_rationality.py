from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import re
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "nonintegral_local_power_rationality.py"
SPEC = importlib.util.spec_from_file_location(
    "nonintegral_local_power_rationality", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load nonintegral local-power packet")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def evaluate_x_polynomial(coefficients: tuple[int, ...], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError(f"unexpected float {value!r}")
    if isinstance(value, dict):
        for child in value.values():
            reject_float(child)
    elif isinstance(value, list):
        for child in value:
            reject_float(child)


class NonintegralLocalPowerRationalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_hecke_laurent_binet_and_recurrence(self) -> None:
        x_laurent = {1: 1, -1: 1}
        self.assertEqual(subject.hecke_laurent(0), {0: 1})
        self.assertEqual(subject.hecke_laurent(1), x_laurent)
        for index in range(20):
            expected = {index - 2 * j: 1 for j in range(index + 1)}
            self.assertEqual(subject.hecke_laurent(index), expected)
            recurrence = subject.laurent_add(
                subject.laurent_multiply(x_laurent, subject.hecke_laurent(index + 1)),
                subject.laurent_scale(subject.hecke_laurent(index), -1),
            )
            self.assertEqual(recurrence, subject.hecke_laurent(index + 2))

        alpha = Fraction(2)
        x = alpha + 1 / alpha
        previous, current = Fraction(1), x
        for index in range(12):
            binet = (alpha ** (index + 1) - alpha ** (-(index + 1))) / (
                alpha - 1 / alpha
            )
            recurrence_value = previous if index == 0 else current
            self.assertEqual(binet, recurrence_value)
            if index:
                previous, current = current, x * current - previous

    def test_symbolic_denominator_and_numerator_annihilation(self) -> None:
        for power in range(9):
            denominator = subject.denominator_laurent(power)
            numerator = subject.numerator_laurent(power)
            self.assertEqual(len(denominator), power + 2)
            self.assertLessEqual(len(numerator), power + 1)
            self.assertEqual(denominator[0], {0: 1})
            for coefficient in denominator + numerator:
                self.assertEqual(
                    coefficient,
                    {exponent: coefficient[-exponent] for exponent in coefficient},
                )
            for index in range(4 * (power + 1)):
                coefficient: subject.Laurent = {}
                for degree in range(min(index, len(denominator) - 1) + 1):
                    coefficient = subject.laurent_add(
                        coefficient,
                        subject.laurent_multiply(
                            denominator[degree],
                            subject.laurent_power(
                                subject.hecke_laurent(index - degree), power
                            ),
                        ),
                    )
                expected = numerator[index] if index < len(numerator) else {}
                self.assertEqual(coefficient, expected, (power, index))

    def test_required_numerator_defects(self) -> None:
        self.assertEqual(subject.numerator_in_x(0), [(1,)])
        self.assertEqual(subject.numerator_in_x(1), [(1,)])
        self.assertEqual(subject.numerator_in_x(2), [(1,), (1,)])
        self.assertEqual(subject.numerator_in_x(3), [(1,), (0, 2), (1,)])
        self.assertEqual(
            subject.numerator_in_x(4),
            [(1,), (-1, 0, 3), (-1, 0, 3), (1,)],
        )
        row = self.fixture["integer_power_replay"]
        self.assertEqual(row["required_numerator_defects"]["k2"], "1+T")
        self.assertEqual(row["required_numerator_defects"]["k3"], "1+2*x*T+T^2")

    def test_exact_numeric_specialization_and_minimal_root_rows(self) -> None:
        alpha = Fraction(2)
        x = alpha + 1 / alpha
        for power in range(9):
            denominator = [
                evaluate_x_polynomial(polynomial, x)
                for polynomial in subject.denominator_in_x(power)
            ]
            numerator = [
                evaluate_x_polynomial(polynomial, x)
                for polynomial in subject.numerator_in_x(power)
            ]
            weights = list(range(power, -power - 1, -2))
            self.assertEqual(len(weights), len(set(weights)))
            direct_denominator = [Fraction(1)]
            for weight in weights:
                root = alpha**weight
                updated = [Fraction(0)] * (len(direct_denominator) + 1)
                for degree, coefficient in enumerate(direct_denominator):
                    updated[degree] += coefficient
                    updated[degree + 1] -= coefficient * root
                direct_denominator = updated
            self.assertEqual(denominator, direct_denominator)

            values = []
            for index in range(4 * (power + 1)):
                u_value = (alpha ** (index + 1) - alpha ** (-(index + 1))) / (
                    alpha - 1 / alpha
                )
                values.append(u_value**power)
            for index in range(len(values)):
                convolution = sum(
                    denominator[degree] * values[index - degree]
                    for degree in range(min(index, len(denominator) - 1) + 1)
                )
                expected = numerator[index] if index < len(numerator) else 0
                self.assertEqual(convolution, expected, (power, index))

            fixture_row = self.fixture["integer_power_replay"]["rows"][power]
            self.assertEqual(
                fixture_row["minimal_denominator_degree_for_x_gt_2"], power + 1
            )
            self.assertTrue(fixture_row["weights_pairwise_distinct"])
            self.assertTrue(
                all(
                    term["nonzero"]
                    for term in fixture_row[
                        "partial_fraction_coefficients_without_common_factor"
                    ]
                )
            )

    def test_generalized_binomial_termination_and_hostile_prefixes(self) -> None:
        for power in range(10):
            coefficients = [
                subject.generalized_binomial(Fraction(power), index)
                for index in range(power + 5)
            ]
            self.assertTrue(all(coefficients[: power + 1]))
            self.assertFalse(any(coefficients[power + 1 :]))
        for value in (Fraction(-1), Fraction(1, 2), Fraction(3, 2), Fraction(-3, 2)):
            coefficients = [
                subject.generalized_binomial(value, index) for index in range(40)
            ]
            self.assertTrue(all(coefficients))

        controls = self.fixture["noninteger_hostile_controls"]
        for row in controls["binomial_pole_prefixes"]:
            self.assertTrue(row["all_displayed_coefficients_nonzero"])
            self.assertTrue(row["displayed_poles_pairwise_distinct"])
            self.assertTrue(row["finite_prefix_is_not_the_nonrationality_proof"])
        hankel = controls["negative_one_exact_hankel"]
        self.assertTrue(hankel["all_displayed_nonzero"])
        self.assertTrue(hankel["finite_hankel_prefix_is_not_an_infinite_rank_proof"])

    def test_polynomial_root_bound_handles_mixed_parity(self) -> None:
        self.assertEqual(subject.polynomial_root_exponents((0,)), (0,))
        for degree in range(13):
            all_roots = subject.polynomial_root_exponents(range(degree + 1))
            self.assertEqual(all_roots, tuple(range(-degree, degree + 1)))
            self.assertEqual(len(all_roots), 2 * degree + 1)
            parity_roots = subject.polynomial_root_exponents(
                range(degree % 2, degree + 1, 2)
            )
            self.assertEqual(
                parity_roots,
                tuple(range(-degree, degree + 1, 2)),
            )

    def test_formal_polynomial_multiplicativity_classification(self) -> None:
        values = (-1, 0, 1)
        for length in range(1, 6):
            for coefficients in itertools.product(values, repeat=length):
                identity = subject.multiplicativity_identity(coefficients)
                support = [index for index, value in enumerate(coefficients) if value]
                predicted = not support or (
                    len(support) == 1 and coefficients[support[0]] == 1
                )
                self.assertEqual(identity, predicted, coefficients)
                exponent = subject.normalized_multiplicative_monomial(coefficients)
                normalized_predicted = (
                    support[0]
                    if len(support) == 1 and coefficients[support[0]] == 1
                    else None
                )
                self.assertEqual(exponent, normalized_predicted, coefficients)

        self.assertTrue(subject.multiplicativity_identity((0, 0, 0)))
        self.assertIsNone(subject.normalized_multiplicative_monomial((0, 0, 0)))
        self.assertFalse(
            subject.multiplicativity_identity((Fraction(1, 2), Fraction(1, 2)))
        )

    def test_source_manifest_authenticates_primitive_files(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCE_MANIFEST_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 5)
        self.assertTrue(source["path"].endswith(".sources.json"))
        fixture_lock = source["verified_sources"][0]
        self.assertEqual(
            fixture_lock["payload_sha256"],
            "046f76f43a2af3ac296f5c18c258e61f138e122bee38ec618af489e7e3a9e50e",
        )
        self.assertTrue(source["scope_firewall"]["local_only"])
        self.assertTrue(source["scope_firewall"]["hyperbolic_non_tempered_chamber"])
        self.assertTrue(
            source["scope_firewall"]["tempered_GL2_trace_chamber_not_treated"]
        )
        self.assertTrue(source["scope_firewall"]["external_novelty_unreviewed"])

    def test_survival_and_scope_firewalls(self) -> None:
        claims = self.fixture["claims"]
        self.assertEqual(
            set(claims),
            {
                "GLO764.LOCAL_POWER_RATIONALITY",
                "GLO764.INTEGER_MINIMAL_DENOMINATOR",
                "GLO764.POLYNOMIAL_RECURRENCE_BOUND",
                "GLO764.POLYNOMIAL_MULTIPLICATIVITY_RIGIDITY",
            },
        )
        self.assertEqual(
            claims["GLO764.POLYNOMIAL_RECURRENCE_BOUND"]["scope"],
            "nonzero Phi in C[z]",
        )
        rows = self.fixture["survival_ladder"]["rows"]
        noninteger = next(row for row in rows if row["object"].startswith("noninteger"))
        self.assertEqual(noninteger["first_failure_level"], "L3")
        self.assertIn("INFINITELY_MANY", noninteger["statuses"]["L3"])
        firewall = self.fixture["scope_firewall"]
        for field in (
            "does_not_classify_arbitrary_holomorphic_Phi",
            "does_not_construct_a_global_Euler_product",
            "does_not_supply_ramified_factors_gamma_factors_or_a_functional_equation",
            "does_not_prove_automorphy_motivic_origin_or_a_zero_theorem",
            "no_RH_GRH_or_zero_distribution_consequence",
            "external_novelty_unreviewed",
            "x_gt_2_is_hyperbolic_non_tempered",
            "tempered_GL2_trace_chamber_not_treated",
            "not_an_automorphic_nonintegral_symmetric_power_no_go",
        ):
            self.assertTrue(firewall[field])
        literature = self.fixture["literature_firewall"]
        self.assertTrue(literature["integer_power_formula_is_classical"])
        self.assertTrue(literature["external_specialist_novelty_review_required"])

    def test_resource_refusals_and_arithmetic_class(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["arithmetic_class"], "EXACT_RATIONAL")
        self.assertIn("Laurent-polynomial", resources["exact_method"])
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
            subject.build_fixture(max_k=13)
        with self.assertRaisesRegex(ValueError, "include the k=2,3,4"):
            subject.build_fixture(max_k=3)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_k=True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.denominator_laurent(False)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.hecke_laurent(-1)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.polynomial_root_exponents((0, -1))

    def test_note_integrity_and_required_proof_gates(self) -> None:
        raw = (PACKET_ROOT / "NONINTEGRAL_LOCAL_POWER_RATIONALITY.md").read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        for command in (r"\binom", r"\rho", r"\mathbb"):
            self.assertIn(command, note)
        self.assertFalse(
            [
                line_number
                for line_number, line in enumerate(note.splitlines(), start=1)
                if line.rstrip(" \t") != line
            ]
        )
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        self.assertGreaterEqual(note.count(r"\["), 20)
        for required in (
            "analytic germ at",
            "Absolute convergence permits the interchange",
            "tail therefore converges locally uniformly",
            "which is nonzero",
            "all other terms are analytic there",
            "Mixed even and odd degrees matter",
            "external novelty unreviewed",
            "Scientific firewall",
            "hyperbolic,",
            "non-tempered",
            "does **not** prove an automorphic",
            "no novelty claim",
        ):
            self.assertIn(required, note)
        self.assertNotIn("proves RH", note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 20)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = PACKET_ROOT / "nonintegral_local_power_rationality.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT / "NONINTEGRAL_LOCAL_POWER_RATIONALITY.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                producer[field],
                hashlib.sha256(normalized).hexdigest(),
            )


if __name__ == "__main__":
    unittest.main()

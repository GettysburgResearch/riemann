from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import re
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
MODULE_PATH = (
    FUNCTION_FIELD / "elliptic_symmetric_power_full_factor_sign_aliases.py"
)
SPEC = importlib.util.spec_from_file_location(
    "elliptic_symmetric_power_full_factor_sign_aliases", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load symmetric-power full-factor collision packet")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def multiply(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    product = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_degree, left_coefficient in enumerate(left):
        for right_degree, right_coefficient in enumerate(right):
            product[left_degree + right_degree] += (
                left_coefficient * right_coefficient
            )
    return tuple(product)


def explicit_factor(m: int, alpha: Fraction, beta: Fraction) -> tuple[Fraction, ...]:
    factor = (Fraction(1),)
    for index in range(m + 1):
        eigenvalue = alpha ** (m - index) * beta**index
        factor = multiply(factor, (Fraction(1), -eigenvalue))
    return factor


def independent_phi(value: int) -> int:
    return sum(math.gcd(value, candidate) == 1 for candidate in range(1, value + 1))


class EllipticSymmetricPowerFullFactorCollisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_newton_factor_matches_explicit_weight_products(self) -> None:
        root_pairs = (
            (Fraction(2), Fraction(3)),
            (Fraction(-2), Fraction(3)),
            (Fraction(2), Fraction(2)),
            (Fraction(2), Fraction(-2)),
            (Fraction(1, 2), Fraction(3, 5)),
        )
        for m in range(0, 9):
            for alpha, beta in root_pairs:
                q = alpha * beta
                self.assertNotEqual(q, 0)
                self.assertEqual(
                    subject.sym_power_local_factor(m, alpha + beta, q),
                    explicit_factor(m, alpha, beta),
                )

    def test_coefficient_sign_law_and_even_termwise_invariance(self) -> None:
        for m in range(0, 13):
            for t, q in (
                (Fraction(-3), Fraction(5)),
                (Fraction(0), Fraction(3)),
                (Fraction(2), Fraction(2)),
                (Fraction(3), Fraction(3)),
                (Fraction(2, 3), Fraction(-5, 7)),
            ):
                left = subject.sym_power_local_factor(m, t, q)
                right = subject.sym_power_local_factor(m, -t, q)
                self.assertEqual(len(left), m + 2)
                for degree, coefficient in enumerate(left):
                    self.assertEqual(
                        right[degree],
                        ((-1) ** (m * degree)) * coefficient,
                    )
                if m % 2 == 0:
                    self.assertEqual(left, right)

    def test_consecutive_residue_lemma_including_repeated_torsion(self) -> None:
        for length in range(1, 97):
            for even_order in range(2, 65, 2):
                certificate = subject.consecutive_residue_shift_certificate(
                    length, even_order
                )
                counts = Counter(index % even_order for index in range(length))
                brute = tuple(counts[index] for index in range(even_order))
                shifted = tuple(
                    brute[(index - even_order // 2) % even_order]
                    for index in range(even_order)
                )
                actual = brute == shifted
                self.assertEqual(certificate["counts"], list(brute))
                self.assertEqual(certificate["half_shifted_counts"], list(shifted))
                self.assertEqual(actual, length % even_order == 0)
                self.assertEqual(certificate["invariant"], actual)
                witness = certificate["contradiction_witness"]
                if length % even_order:
                    self.assertIsInstance(witness, dict)
                    inside = witness["inside_residue"]
                    outside = witness["half_shifted_outside_residue"]
                    self.assertEqual(
                        (inside + even_order // 2) % even_order,
                        outside,
                    )
                    self.assertGreater(brute[inside], brute[outside])
                else:
                    self.assertIsNone(witness)

    def test_dependency_free_cyclotomic_certificate(self) -> None:
        polynomials = subject.cyclotomic_polynomials(36)
        for order in range(1, 37):
            self.assertEqual(len(polynomials[order]) - 1, independent_phi(order))
            product = (Fraction(1),)
            for divisor in range(1, order + 1):
                if order % divisor == 0:
                    product = multiply(
                        product,
                        tuple(Fraction(value) for value in polynomials[divisor]),
                    )
            expected = (Fraction(-1),) + (Fraction(0),) * (order - 1) + (
                Fraction(1),
            )
            self.assertEqual(product, expected)
        self.assertEqual(
            [order for order in range(1, 37) if independent_phi(order) <= 2],
            [1, 2, 3, 4, 6],
        )
        self.assertEqual(polynomials[2], (1, 1))
        self.assertEqual(polynomials[4], (1, 0, 1))
        self.assertEqual(polynomials[6], (1, -1, 1))

    def test_rational_sign_classification_and_closed_alias_factors(self) -> None:
        cases = (
            ("order2", Fraction(0), Fraction(3), 2),
            ("order4", Fraction(2), Fraction(2), 4),
            ("order6", Fraction(3), Fraction(3), 6),
            ("order3", Fraction(3), Fraction(9), 3),
            ("order1", Fraction(6), Fraction(9), 1),
            ("generic", Fraction(1), Fraction(3), None),
        )
        for m in range(1, 25):
            for label, t, q, order in cases:
                with self.subTest(m=m, label=label):
                    self.assertEqual(subject.rational_root_ratio_order(t, q), order)
                    left = subject.sym_power_local_factor(m, t, q)
                    right = subject.sym_power_local_factor(m, -t, q)
                    predicted = (
                        True
                        if m % 2 == 0
                        else order in (2, 4, 6) and (m + 1) % int(order) == 0
                    )
                    self.assertEqual(left == right, predicted)
                    self.assertEqual(
                        subject.rational_sign_alias_prediction(m, t, q),
                        predicted,
                    )
                    if m % 2 and predicted:
                        self.assertEqual(
                            left,
                            subject.complete_cycle_alias_factor(m, q, int(order)),
                        )

    def test_complete_fixed_q_Q_collision_classification(self) -> None:
        traces = sorted(
            {
                Fraction(numerator, denominator)
                for denominator in (1, 2)
                for numerator in range(-4, 5)
            }
        )
        for m in range(1, 11):
            for q in (Fraction(-3), Fraction(1), Fraction(2), Fraction(3)):
                factors = {
                    trace: subject.sym_power_local_factor(m, trace, q)
                    for trace in traces
                }
                for x, y in itertools.combinations_with_replacement(traces, 2):
                    actual = factors[x] == factors[y]
                    predicted = subject.rational_full_factor_collision_prediction(
                        m, x, y, q
                    )
                    self.assertEqual(actual, predicted, (m, q, x, y))
                    if actual:
                        self.assertEqual(x * x, y * y)

        with self.assertRaisesRegex(ValueError, "m>=1"):
            subject.rational_full_factor_collision_prediction(0, 1, 2, 3)
        self.assertEqual(
            subject.sym_power_local_factor(0, 1, 3),
            subject.sym_power_local_factor(0, 2, 3),
        )

    def test_nonrational_trace_hypothesis_counterexample(self) -> None:
        row = self.fixture["nonrational_trace_counterexample"]
        self.assertEqual(row["first_spectrum_exponents_mod_5"], [1, 2, 3, 4])
        self.assertEqual(row["second_spectrum_exponents_mod_5"], [1, 2, 3, 4])
        self.assertEqual(row["common_factor"], [1, 1, 1, 1, 1])
        # The two traces are the distinct roots of X^2+X-1.  They cannot
        # be negatives because their sum is -1, and neither is zero.
        self.assertEqual(row["x_and_y_minimal_polynomial"], "X^2+X-1")
        self.assertTrue(row["x_not_equal_plus_or_minus_y"])

    def test_odd_prime_power_integral_corollary(self) -> None:
        prime_powers = (3, 5, 7, 9, 11, 25, 27, 49, 81, 125, 243)
        for q in prime_powers:
            hasse_limit = math.isqrt(4 * q)
            traces = set(range(1, min(hasse_limit, 10) + 1))
            square_root_3q = math.isqrt(3 * q)
            if square_root_3q * square_root_3q == 3 * q:
                traces.add(square_root_3q)
            for t in sorted(traces):
                for m in range(1, 12, 2):
                    actual = (
                        subject.sym_power_local_factor(m, t, q)
                        == subject.sym_power_local_factor(m, -t, q)
                    )
                    predicted = (m + 1) % 6 == 0 and t * t == 3 * q
                    self.assertEqual(actual, predicted, (m, q, t))
        for exponent in range(1, 10):
            q = 3**exponent
            square = 3 * q
            root = math.isqrt(square)
            self.assertEqual(root * root == square, exponent % 2 == 1)
        for q in range(1, 200, 2):
            self.assertNotEqual(math.isqrt(2 * q) ** 2, 2 * q)

    def test_locked_sources_are_replayed_by_all_three_hashes(self) -> None:
        locks = {
            Path(row["path"]).name: row for row in self.fixture["source_locks"]
        }
        expectations = (
            (
                subject.TRACE_SOURCE_PATH,
                subject.EXPECTED_TRACE_SOURCE_SCHEMA,
                subject.EXPECTED_TRACE_SOURCE_PAYLOAD_SHA256,
                subject.EXPECTED_TRACE_SOURCE_FILE_SHA256_LF,
            ),
            (
                subject.SYM5_SOURCE_PATH,
                subject.EXPECTED_SYM5_SOURCE_SCHEMA,
                subject.EXPECTED_SYM5_SOURCE_PAYLOAD_SHA256,
                subject.EXPECTED_SYM5_SOURCE_FILE_SHA256_LF,
            ),
        )
        for path, schema, payload, lf_hash in expectations:
            source = json.loads(path.read_text(encoding="utf-8"))
            lock = locks[path.name]
            self.assertEqual(source["schema"], schema)
            self.assertEqual(source["payload_sha256"], payload)
            unhashed = dict(source)
            self.assertEqual(unhashed.pop("payload_sha256"), subject._canonical_sha256(unhashed))
            self.assertEqual(subject._lf_sha256(path), lf_hash)
            self.assertEqual(lock["schema"], schema)
            self.assertEqual(lock["payload_sha256"], payload)
            self.assertEqual(lock["file_sha256_lf_normalized"], lf_hash)

        replay = self.fixture["source_replay"]
        self.assertEqual(
            replay["sym5_packet_full_factor_aliases"],
            [
                {"q": 3, "x": -3, "y": 3},
                {"q": 27, "x": -9, "y": 9},
                {"q": 243, "x": -27, "y": 27},
            ],
        )
        self.assertEqual(replay["new_curve_field_or_trace_range_enumerations"], 0)

    def test_resource_contract_firewalls_and_refusals(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertLess(
            resources["accounted_work_units"],
            resources["accounted_work_unit_cap_exclusive"],
        )
        self.assertLessEqual(resources["accounted_work_unit_cap_exclusive"], 5_000)
        self.assertEqual(resources["maximum_regression_m"], 36)
        self.assertEqual(resources["new_curve_field_or_trace_range_enumerations"], 0)
        self.assertFalse(resources["symbolic_engine_dependency"])

        firewall = self.fixture["scope_firewall"]
        self.assertTrue(firewall["complete_fixed_q_rational_full_factor_classification"])
        self.assertTrue(firewall["does_not_classify_arbitrary_scalar_trace_collisions"])
        self.assertTrue(
            firewall["does_not_extend_complete_classification_to_nonrational_traces"]
        )
        self.assertTrue(firewall["no_RH_GRH_or_zero_distribution_consequence_claim"])

        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(
                resource_cap=resources["accounted_work_units"]
            )
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            subject.build_fixture(max_m=37)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_m=True)
        with self.assertRaisesRegex(ValueError, "nonzero"):
            subject.sym_power_local_factor(3, 1, 0)
        with self.assertRaisesRegex(TypeError, "integer or Fraction"):
            subject.sym_power_local_factor(3, 1.0, 3)
        with self.assertRaisesRegex(ValueError, "positive even"):
            subject.consecutive_residue_shift_certificate(4, 3)
        with self.assertRaisesRegex(ValueError, "divide"):
            subject.complete_cycle_alias_factor(5, 3, 4)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for child in value.values():
                    reject_float(child)
            elif isinstance(value, list):
                for child in value:
                    reject_float(child)

        reject_float(self.fixture)

    def test_note_integrity_and_scientific_boundaries(self) -> None:
        note_path = (
            FUNCTION_FIELD
            / "ELLIPTIC_SYMMETRIC_POWER_FULL_FACTOR_SIGN_ALIASES.md"
        )
        raw = note_path.read_bytes()
        self.assertFalse(
            [byte for byte in raw if byte < 32 and byte not in (9, 10, 13)]
        )
        note = raw.decode("utf-8")
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
            "intrinsic quotient group",
            "Consecutive-residue multiplicity lemma",
            "rational-trace hypothesis is sharp",
            "Scientific firewall",
            "classification of collisions of the scalar character alone",
        ):
            self.assertIn(required, note)
        self.assertNotIn(",quad", note)
        self.assertNotIn(",qquad", note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        for display in displays:
            for control_word in (
                "alpha",
                "begin",
                "beta",
                "cdot",
                "det",
                "end",
                "frac",
                "ge",
                "in",
                "langle",
                "mathbb",
                "mid",
                "ne",
                "operatorname",
                "pm",
                "prod",
                "qquad",
                "rangle",
                "text",
            ):
                self.assertIsNone(
                    re.search(rf"(?<!\\)\b{control_word}\b", display),
                    (control_word, display),
                )

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = (
            FUNCTION_FIELD
            / "elliptic_symmetric_power_full_factor_sign_aliases.json"
        )
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                FUNCTION_FIELD
                / "ELLIPTIC_SYMMETRIC_POWER_FULL_FACTOR_SIGN_ALIASES.md",
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

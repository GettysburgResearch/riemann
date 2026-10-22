from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import re
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
MODULE_PATH = FUNCTION_FIELD / "elliptic_sym5_coefficient_recovery.py"
SPEC = importlib.util.spec_from_file_location(
    "elliptic_sym5_coefficient_recovery", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load elliptic_sym5_coefficient_recovery")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def independent_e(order: int, t: Fraction, q: Fraction) -> Fraction:
    if order == 0:
        return Fraction(1)
    previous_previous, previous = Fraction(1), t
    for _ in range(2, order + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def independent_power_sum(order: int, t: Fraction, q: Fraction) -> Fraction:
    if order == 0:
        return Fraction(2)
    previous_previous, previous = Fraction(2), t
    for _ in range(2, order + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def independent_sym5_factor(
    t_value: int | Fraction, q_value: int | Fraction
) -> tuple[Fraction, ...]:
    t, q = Fraction(t_value), Fraction(q_value)
    power_sums = [Fraction(0)] + [
        independent_e(5, independent_power_sum(order, t, q), q**order)
        for order in range(1, 7)
    ]
    coefficients = [Fraction(1)]
    for degree in range(1, 7):
        coefficients.append(
            -sum(
                coefficients[degree - order] * power_sums[order]
                for order in range(1, degree + 1)
            )
            / degree
        )
    return tuple(coefficients)


def independent_e5(t: int | Fraction, q: int | Fraction) -> Fraction:
    t_fraction, q_fraction = Fraction(t), Fraction(q)
    return (
        t_fraction**5
        - 4 * q_fraction * t_fraction**3
        + 3 * q_fraction**2 * t_fraction
    )


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def independent_numeric_resultant(x: int, y: int) -> int:
    h_value = x * x + x * y + y * y
    k_value = x**4 + x**3 * y + x * x * y * y + x * y**3 + y**4
    s_value = x * x + y * y
    u_value = x**4 + x * x * y * y + y**4
    v_value = x**6 + x**4 * y * y + x * x * y**4 + y**6
    q_coefficients = (3, -4 * h_value, k_value)
    r_coefficients = (-13, 16 * s_value, -7 * u_value, v_value)
    matrix: list[list[int]] = []
    for shift in range(3):
        row = [0] * 5
        row[shift : shift + 3] = q_coefficients
        matrix.append(row)
    for shift in range(2):
        row = [0] * 5
        row[shift : shift + 4] = r_coefficients
        matrix.append(row)
    determinant = 0
    for permutation in itertools.permutations(range(5)):
        term = permutation_sign(permutation)
        for row_index, column_index in enumerate(permutation):
            term *= matrix[row_index][column_index]
        determinant += term
    return determinant


def independent_factor_product(x: int, y: int) -> int:
    return (
        (x * x - 3 * y * y)
        * (3 * x * x - y * y)
        * (x * x + 3 * x * y + y * y)
        * (x**3 - 3 * x * x * y - 4 * x * y * y - y**3)
        * (x**3 + 4 * x * x * y + 3 * x * y * y - y**3)
    )


class EllipticSym5CoefficientRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_closed_coefficients_match_independent_newton_reconstruction(self) -> None:
        inputs = (
            (-7, 31),
            (3, 9),
            (-3, 3),
            (Fraction(3, 2), Fraction(5, 3)),
            (Fraction(-2, 3), Fraction(-7, 5)),
        )
        for t, q in inputs:
            expected = independent_sym5_factor(t, q)
            self.assertEqual(subject.sym5_local_factor(t, q), expected)
            self.assertEqual(subject.e5_trace(t, q), independent_e5(t, q))
            self.assertEqual(subject.sym5_second_coefficient(t, q), expected[2])
            self.assertEqual(subject.sym5_third_coefficient(t, q), expected[3])

    def test_difference_factorizations_and_euclidean_reduction(self) -> None:
        values = (Fraction(-3), Fraction(-1, 2), Fraction(0), Fraction(2, 3), Fraction(4))
        q_values = (Fraction(-5, 2), Fraction(-1), Fraction(1, 3), Fraction(3), Fraction(11, 2))
        for x in values:
            for y in values:
                for q in q_values:
                    scalar_difference = subject.e5_trace(x, q) - subject.e5_trace(y, q)
                    self.assertEqual(
                        scalar_difference,
                        (x - y) * subject.collision_quotient(x, y, q),
                    )
                    c2_difference = subject.sym5_second_coefficient(
                        x, q
                    ) - subject.sym5_second_coefficient(y, q)
                    self.assertEqual(
                        c2_difference,
                        q
                        * (x * x - y * y)
                        * subject.second_coefficient_quotient(x, y, q),
                    )

                    h_value = x * x + x * y + y * y
                    k_value = x**4 + x**3 * y + x * x * y * y + x * y**3 + y**4
                    s_value = x * x + y * y
                    a_value = (
                        -40 * x**4
                        - 185 * x**3 * y
                        - 264 * x * x * y * y
                        - 185 * x * y**3
                        - 40 * y**4
                    )
                    b_value = (
                        13 * x**6
                        + 56 * x**5 * y
                        + 69 * x**4 * y * y
                        + 60 * x**3 * y**3
                        + 69 * x * x * y**4
                        + 56 * x * y**5
                        + 13 * y**6
                    )
                    self.assertEqual(
                        9 * subject.second_coefficient_quotient(x, y, q),
                        (-39 * q + 48 * s_value - 52 * h_value)
                        * subject.collision_quotient(x, y, q)
                        + a_value * q
                        + b_value,
                    )
                    self.assertEqual(
                        k_value * a_value * a_value
                        + 4 * h_value * a_value * b_value
                        + 3 * b_value * b_value,
                        9 * independent_factor_product(x, y),
                    )

    def test_resultant_is_exact_with_no_dropped_factor(self) -> None:
        expected_coefficients = [
            3,
            12,
            -37,
            -235,
            -228,
            467,
            1_016,
            467,
            -228,
            -235,
            -37,
            12,
            3,
        ]
        certificate = self.fixture["resultant_certificate"]
        self.assertEqual(
            certificate["exact_resultant_coefficient_vector_x12_to_y12"],
            expected_coefficients,
        )
        self.assertEqual(certificate["factor_multiplicities"], [1, 1, 1, 1, 1])
        self.assertEqual(certificate["dropped_scalar_or_variable_factors"], [])
        for x in range(-6, 7):
            determinant = independent_numeric_resultant(x, 1)
            product = independent_factor_product(x, 1)
            polynomial_value = sum(
                coefficient * x ** (12 - index)
                for index, coefficient in enumerate(expected_coefficients)
            )
            self.assertEqual(determinant, product)
            self.assertEqual(determinant, polynomial_value)
        self.assertEqual(independent_numeric_resultant(1, 0), 3)
        self.assertEqual(independent_factor_product(1, 0), 3)

    def test_each_resultant_factor_has_no_nonzero_rational_projective_zero(self) -> None:
        # The quadratic arguments reduce to nonsquareness of 3 and 5.
        for prime in (3, 5):
            for denominator in range(1, 40):
                for numerator in range(-80, 81):
                    self.assertNotEqual(numerator * numerator, prime * denominator * denominator)

        first_cubic = lambda r: r**3 - 3 * r**2 - 4 * r - 1
        second_cubic = lambda r: r**3 + 4 * r**2 + 3 * r - 1
        self.assertEqual([first_cubic(r) for r in (-1, 1)], [-1, -7])
        self.assertEqual([second_cubic(r) for r in (-1, 1)], [-1, 7])
        self.assertEqual(
            self.fixture["resultant_certificate"]["conclusion"],
            "the resultant has no nonzero rational projective zero",
        )

    def test_all_Q_recovery_classification_on_an_independent_rational_grid(self) -> None:
        values = [Fraction(numerator, denominator) for denominator in range(1, 5) for numerator in range(-8, 9)]
        values = sorted(set(values))
        q_values = [
            Fraction(-7, 3),
            Fraction(-1),
            Fraction(1, 3),
            Fraction(3, 4),
            Fraction(1),
            Fraction(3),
            Fraction(9),
        ]
        for q in q_values:
            for x in values:
                for y in values:
                    flags = subject.recovery_flags(x, y, q)
                    self.assertEqual(flags["pair_equal"], flags["predicted_pair_equal"])
                    self.assertEqual(
                        flags["triple_equal"], flags["predicted_triple_equal"]
                    )
                    self.assertEqual(flags["full_equal"], flags["predicted_full_equal"])
                    self.assertEqual(flags["triple_equal"], flags["full_equal"])

    def test_sign_and_zero_cases_are_complete(self) -> None:
        pair_only = subject.recovery_flags(-3, 3, 9)
        self.assertTrue(pair_only["pair_equal"])
        self.assertFalse(pair_only["triple_equal"])
        self.assertEqual(subject.sym5_third_coefficient(3, 9), 2 * 9**7 * 3)
        full_alias = subject.recovery_flags(-3, 3, 3)
        self.assertTrue(full_alias["pair_equal"])
        self.assertTrue(full_alias["triple_equal"])
        self.assertTrue(full_alias["full_equal"])
        self.assertEqual(subject.sym5_local_factor(3, 3), (1, 0, 0, 0, 0, 0, 3**15))

        for q, nonzero in ((9, 3), (3, 3)):
            flags = subject.recovery_flags(0, nonzero, q)
            self.assertTrue(flags["scalar_equal"])
            self.assertFalse(flags["c2_equal"])
            self.assertEqual(subject.sym5_second_coefficient(0, q), 3 * q**5)

    def test_plethystic_identities_and_weight_multisets(self) -> None:
        certificate = self.fixture["plethystic_certificate"]
        wedge2 = Counter()
        for left in range(6):
            for right in range(left + 1, 6):
                wedge2[(10 - left - right, left + right)] += 1
        wedge2_rhs = Counter(
            [(9 - index, index + 1) for index in range(9)]
            + [(7 - index, index + 3) for index in range(5)]
            + [(5, 5)]
        )
        self.assertEqual(wedge2, wedge2_rhs)
        self.assertEqual(sum(wedge2.values()), 15)

        wedge3 = Counter()
        for indices in itertools.combinations(range(6), 3):
            beta_power = sum(indices)
            wedge3[(15 - beta_power, beta_power)] += 1
        wedge3_rhs = Counter(
            [(12 - index, index + 3) for index in range(10)]
            + [(10 - index, index + 5) for index in range(6)]
            + [(9 - index, index + 6) for index in range(4)]
        )
        self.assertEqual(wedge3, wedge3_rhs)
        self.assertEqual(sum(wedge3.values()), 20)
        self.assertEqual(certificate["lambda2_sym5"]["dimension"], 15)
        self.assertEqual(certificate["lambda3_sym5"]["dimension"], 20)

        for denominator in range(1, 5):
            for numerator in range(-5, 6):
                t = Fraction(numerator, denominator)
                for q in (Fraction(-3, 2), Fraction(1, 3), Fraction(5)):
                    self.assertEqual(
                        subject.sym5_second_coefficient(t, q),
                        q * independent_e(8, t, q)
                        + q**3 * independent_e(4, t, q)
                        + q**5,
                    )
                    self.assertEqual(
                        subject.sym5_third_coefficient(t, q),
                        -(
                            q**3 * independent_e(9, t, q)
                            + q**5 * independent_e(5, t, q)
                            + q**6 * independent_e(3, t, q)
                        ),
                    )

    def test_all_61_locked_collisions_are_replayed_not_reenumerated(self) -> None:
        source = json.loads(subject.SOURCE_PATH.read_text(encoding="utf-8"))
        outcome_counts: Counter[str] = Counter()
        class_outcomes: Counter[tuple[str, str]] = Counter()
        replay_projection: list[dict[str, object]] = []
        for q_row in source["finite_census"]["rows"]:
            q = int(q_row["q"])
            for pair in q_row["pairs"]:
                x, y = int(pair["x"]), int(pair["y"])
                left = independent_sym5_factor(x, q)
                right = independent_sym5_factor(y, q)
                self.assertEqual(left[1], right[1])
                if left[2] != right[2]:
                    outcome = "T2"
                elif left[3] != right[3]:
                    outcome = "T3"
                elif left == right:
                    outcome = "full_factor_alias"
                else:
                    self.fail("independent full-factor replay was inconsistent")
                outcome_counts[outcome] += 1
                collision_class = str(pair["collision_class"])
                class_outcomes[(collision_class, outcome)] += 1
                replay_projection.append(
                    {"q": q, "x": x, "y": y, "class": collision_class, "outcome": outcome}
                )

        replay = self.fixture["locked_collision_replay"]
        self.assertEqual(len(replay_projection), 61)
        self.assertEqual(
            outcome_counts,
            Counter({"T2": 42, "T3": 16, "full_factor_alias": 3}),
        )
        self.assertEqual(
            class_outcomes,
            Counter(
                {
                    ("general", "T2"): 4,
                    ("zero_nonzero", "T2"): 38,
                    ("sign_pair", "T3"): 16,
                    ("sign_pair", "full_factor_alias"): 3,
                }
            ),
        )
        self.assertEqual(replay["rows_replayed"], 61)
        self.assertEqual(
            replay["row_projection_sha256"], subject._canonical_sha256(replay_projection)
        )
        self.assertEqual(replay["new_curve_field_or_trace_range_enumerations"], 0)

    def test_source_locks_resources_and_scientific_firewall(self) -> None:
        source = json.loads(subject.SOURCE_PATH.read_text(encoding="utf-8"))
        source_lock = self.fixture["source_lock"]
        self.assertEqual(source["schema"], subject.EXPECTED_SOURCE_SCHEMA)
        self.assertEqual(
            source["payload_sha256"], subject.EXPECTED_SOURCE_PAYLOAD_SHA256
        )
        unhashed = dict(source)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        self.assertEqual(subject._lf_sha256(subject.SOURCE_PATH), source_lock["file_sha256_lf_normalized"])

        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["accounted_work_units"], 226)
        self.assertEqual(resources["accounted_work_unit_cap_exclusive"], 25_000)
        self.assertLess(resources["accounted_work_units"], resources["accounted_work_unit_cap_exclusive"])
        self.assertEqual(resources["new_curve_field_or_trace_range_enumerations"], 0)
        self.assertFalse(resources["symbolic_engine_dependency"])

        firewall = self.fixture["scope_firewall"]
        for key, value in firewall.items():
            if key == "finite_replay_is_not_evidence_for_the_all_Q_proof":
                self.assertIn("exact difference/resultant", value)
            else:
                self.assertTrue(value, key)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for child in value.values():
                    reject_float(child)
            elif isinstance(value, list):
                for child in value:
                    reject_float(child)

        reject_float(self.fixture)

    def test_note_math_delimiters_controls_and_bytes_are_clean(self) -> None:
        note_path = FUNCTION_FIELD / "ELLIPTIC_SYM5_COEFFICIENT_RECOVERY.md"
        raw = note_path.read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10, 13)])
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
                "Lambda",
                "mathbin",
                "ne",
                "operatorname",
                "oplus",
                "qquad",
                "simeq",
                "text",
            ):
                self.assertIsNone(
                    re.search(rf"(?<!\\)\b{control_word}\b", display),
                    (control_word, display),
                )

    def test_stored_fixture_hashes_and_refusals_are_optimized_safe(self) -> None:
        stored_path = FUNCTION_FIELD / "elliptic_sym5_coefficient_recovery.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                FUNCTION_FIELD / "ELLIPTIC_SYM5_COEFFICIENT_RECOVERY.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())

        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=226)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(resource_cap=True)
        with self.assertRaisesRegex(TypeError, "integer or Fraction"):
            subject.e5_trace(1.0, 3)
        with self.assertRaisesRegex(ValueError, "nonzero"):
            subject.e5_trace(1, 0)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.e_trace(-1, 1, 3)
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.ResourceGuard(0)


if __name__ == "__main__":
    unittest.main()

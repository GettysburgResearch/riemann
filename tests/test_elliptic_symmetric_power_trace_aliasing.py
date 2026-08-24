"""Independent replay tests for symmetric-power scalar-trace aliasing."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_symmetric_power_trace_aliasing as subject  # noqa: E402


def independent_tau(m: int, t: int, q: int) -> int:
    coefficients = [1]
    if m == 0:
        return 1
    coefficients.append(t)
    for degree in range(2, m + 1):
        coefficients.append(t * coefficients[-1] - q * coefficients[-2])
    return coefficients[m]


def multiply_by_linear(coefficients: tuple[int, ...], root: int) -> tuple[int, ...]:
    output = [0] * (len(coefficients) + 1)
    for degree, coefficient in enumerate(coefficients):
        output[degree] += coefficient
        output[degree + 1] -= root * coefficient
    return tuple(output)


def direct_factor_from_integral_roots(
    m: int, alpha: int, beta: int
) -> tuple[int, ...]:
    coefficients = (1,)
    for index in range(m + 1):
        coefficients = multiply_by_linear(
            coefficients, alpha ** (m - index) * beta**index
        )
    return coefficients


def quartic_discriminant(a: int, b: int, c: int, d: int, e: int) -> int:
    """Standard quartic discriminant, independent of the producer."""

    return (
        256 * a**3 * e**3
        - 192 * a * a * b * d * e * e
        - 128 * a * a * c * c * e * e
        + 144 * a * a * c * d * d * e
        - 27 * a * a * d**4
        + 144 * a * b * b * c * e * e
        - 6 * a * b * b * d * d * e
        - 80 * a * b * c * c * d * e
        + 18 * a * b * c * d**3
        + 16 * a * c**4 * e
        - 4 * a * c**3 * d * d
        - 27 * b**4 * e * e
        + 18 * b**3 * c * d * e
        - 4 * b**3 * d**3
        - 4 * b * b * c**3 * e
        + b * b * c * c * d * d
    )


class EllipticSymmetricPowerTraceAliasingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.frozen = {
            int(row["q"]): row for row in cls.fixture["frozen_histogram_transforms"]
        }

    def test_recurrence_closed_form_and_character_meaning(self) -> None:
        for q in (-9, -5, -1, 1, 3, 5, 9, 13):
            for t in range(-7, 8):
                for m in range(31):
                    with self.subTest(q=q, t=t, m=m):
                        expected = independent_tau(m, t, q)
                        self.assertEqual(subject.tau(m, t, q), expected)
                        self.assertEqual(subject.tau_closed(m, t, q), expected)

        for alpha, beta in ((1, 3), (-1, -3), (1, 5), (3, 5)):
            q = alpha * beta
            t = alpha + beta
            for m in range(13):
                direct = sum(alpha ** (m - i) * beta**i for i in range(m + 1))
                self.assertEqual(subject.tau(m, t, q), direct)

    def test_collision_quotient_polynomial_identities(self) -> None:
        for q in (-5, -1, 1, 3, 7):
            for x in range(-5, 6):
                for y in range(-5, 6):
                    for m in range(1, 20, 2):
                        quotient = subject.odd_collision_quotient(m, x, y, q)
                        if x != y:
                            self.assertEqual(
                                subject.tau(m, x, q) - subject.tau(m, y, q),
                                (x - y) * quotient,
                            )
                    for m in range(2, 20, 2):
                        quotient = subject.even_collision_quotient(m, x, y, q)
                        if x * x != y * y:
                            self.assertEqual(
                                subject.tau(m, x, q) - subject.tau(m, y, q),
                                (x * x - y * y) * quotient,
                            )

        for x in range(-6, 7):
            for y in range(-6, 7):
                for q in (-3, -1, 1, 3, 5):
                    self.assertEqual(
                        subject.odd_collision_quotient(5, x, y, q),
                        subject.m5_collision_quotient_closed(x, y, q),
                    )

    def test_twelve_residue_parity_recurrence_table(self) -> None:
        table = subject.quotient_parity_table()
        odd_bits = [
            "1111", "0111", "1000", "0111", "1111", "0000",
            "1111", "0111", "1000", "0111", "1111", "0000",
        ]
        even_bits = [
            "0000", "1111", "1001", "0001", "0111", "1000",
            "1000", "0111", "0001", "1001", "1111", "0000",
        ]
        self.assertEqual(len(table), 12)
        for residue, row in enumerate(table):
            self.assertEqual(row["r_mod_12"], residue)
            self.assertEqual(
                "".join(map(str, row["odd_m_2r_plus_1_mod_2_values_at_00_01_10_11"])),
                odd_bits[residue],
            )
            self.assertEqual(
                "".join(map(str, row["even_m_2r_mod_2_values_at_00_01_10_11"])),
                even_bits[residue],
            )
            if row["odd_target_m_mod_6_in_1_3"]:
                self.assertTrue(
                    all(pair == [0, 0] for pair in row["odd_zero_parity_pairs"])
                )
            if row["even_target_m_mod_6_eq_2"]:
                self.assertTrue(
                    all(pair == [0, 0] for pair in row["even_zero_parity_pairs"])
                )

        # Pin the indexing warning: m=2 and m=14 differ in the even table,
        # even though they are the same residue modulo 12.
        row_m2 = tuple(
            subject.even_collision_quotient(2, x, y, 1) % 2
            for x, y in subject.PARITY_PAIRS
        )
        row_m14 = tuple(
            subject.even_collision_quotient(14, x, y, 1) % 2
            for x, y in subject.PARITY_PAIRS
        )
        self.assertEqual(row_m2, (1, 1, 1, 1))
        self.assertEqual(row_m14, (0, 1, 1, 1))

    def test_all_m_two_adic_valuation_lemma(self) -> None:
        for r in range(1, 101):
            for s in range(1, r + 1):
                for q in (-9, -3, -1, 1, 3, 9):
                    actual = subject.odd_higher_coefficient_valuation_margin(r, s, q)
                    formula = subject.odd_interval_margin_formula(r, s)
                    self.assertEqual(actual, formula)
                    self.assertGreaterEqual(actual, 1)
                self.assertGreaterEqual((2 * s + 1).bit_count(), 2)

        for r in range(2, 101):
            for s in range(1, r):
                for q in (-9, -3, -1, 1, 3, 9):
                    actual = subject.even_higher_coefficient_valuation_margin(r, s, q)
                    formula = subject.even_interval_margin_formula(r, s)
                    self.assertEqual(actual, formula)
                    self.assertGreaterEqual(actual, 1)
                if (2 * s + 2).bit_count() == 1:
                    remaining = [
                        value
                        for value in range(r - s, r + s + 2)
                        if value not in (r, r + 1)
                    ]
                    self.assertTrue(any(value % 2 == 0 for value in remaining))

    def test_integer_collision_theorem_adversarial_ranges(self) -> None:
        for q in range(-19, 20, 2):
            for m in range(1, 43):
                if m % 6 in (1, 3):
                    seen: dict[int, int] = {}
                    for t in range(-30, 31):
                        image = subject.tau(m, t, q)
                        self.assertNotIn(image, seen, (q, m, seen.get(image), t))
                        seen[image] = t
                if m % 6 == 2:
                    seen_sign_classes: dict[int, int] = {}
                    for t in range(31):
                        image = subject.tau(m, t, q)
                        self.assertNotIn(
                            image, seen_sign_classes, (q, m, seen_sign_classes.get(image), t)
                        )
                        seen_sign_classes[image] = t
                        self.assertEqual(image, subject.tau(m, -t, q))

    def test_sharp_complement_and_locked_q3_realization(self) -> None:
        for k in range(9):
            q = 3 ** (2 * k + 1)
            t = 3 ** (k + 1)
            self.assertEqual(t * t, 3 * q)
            self.assertLessEqual(t * t, 4 * q)
            initial = [subject.tau(m, t, q) for m in range(6)]
            self.assertEqual(initial, [1, t, 2 * q, q * t, q * q, 0])
            for m in range(61):
                self.assertEqual(
                    subject.tau(m + 6, t, q), -q**3 * subject.tau(m, t, q)
                )
                if m > 0 and m % 6 in (0, 4, 5):
                    self.assertEqual(subject.tau(m, 0, q), subject.tau(m, t, q))

        source = json.loads(subject.SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
        row3 = next(row for row in source["finite_regressions"] if row["q"] == 3)
        histogram = {int(t): int(count) for t, count in row3["model_trace_histogram"].items()}
        self.assertEqual({t: histogram[t] for t in (-3, 0, 3)}, {-3: 1, 0: 4, 3: 1})

    def test_full_factor_newton_diagnostics_and_scope(self) -> None:
        for alpha, beta in ((1, 3), (-1, -3), (1, 5), (3, 5)):
            q = alpha * beta
            t = alpha + beta
            for m in range(8):
                self.assertEqual(
                    subject.sym_power_local_factor(m, t, q),
                    direct_factor_from_integral_roots(m, alpha, beta),
                )

        for m in range(1, 19):
            positive = subject.sym_power_local_factor(m, 3, 3)
            negative = subject.sym_power_local_factor(m, -3, 3)
            if m % 2 == 0:
                self.assertEqual(positive, negative)
            elif m % 6 == 5:
                self.assertEqual(positive, negative)
            if m % 6 in (0, 4, 5):
                zero = subject.sym_power_local_factor(m, 0, 3)
                self.assertNotEqual(zero, positive)
                self.assertEqual(subject.tau(m, 0, 3), subject.tau(m, 3, 3))

        # The second root power sum separates the constructed zero/nonzero
        # scalar alias for every positive complementary residue, not merely
        # in the frozen m<=18 range.
        unit_character = (1, 1, 0, -1, -1, 0)
        for k in range(5):
            q = 3 ** (2 * k + 1)
            t = 3 ** (k + 1)
            for m in range(1, 61):
                if m % 6 not in (0, 4, 5):
                    continue
                zero_r2 = subject.sym_power_root_power_sum(m, 2, 0, q)
                nonzero_r2 = subject.sym_power_root_power_sum(m, 2, t, q)
                self.assertEqual(zero_r2, (-1) ** m * (m + 1) * q**m)
                self.assertEqual(nonzero_r2, unit_character[m % 6] * q**m)
                self.assertNotEqual(zero_r2, nonzero_r2)

        m4_zero = (1, -9, -162, 1458, 6561, -59049)
        m4_three = (1, -9, 81, -729, 6561, -59049)
        self.assertEqual(subject.sym4_local_factor_closed(0, 3), m4_zero)
        self.assertEqual(subject.sym4_local_factor_closed(3, 3), m4_three)
        self.assertEqual(subject.sym_power_local_factor(4, 0, 3), m4_zero)
        self.assertEqual(subject.sym_power_local_factor(4, 3, 3), m4_three)

        m5_sign = (1, 0, 0, 0, 0, 0, 3**15)
        m5_zero = (1, 0, 3**6, 0, 3**11, 0, 3**15)
        self.assertEqual(subject.sym_power_local_factor(5, 3, 3), m5_sign)
        self.assertEqual(subject.sym_power_local_factor(5, -3, 3), m5_sign)
        self.assertEqual(subject.sym_power_local_factor(5, 0, 3), m5_zero)

        expected_minus_seven = (
            1, -5544, 29339640, -142543380980, 839968983845640,
            -4544019223021560744, 23465261991844685929951,
        )
        expected_three = (
            1, -5544, 11744040, -81567162180, 336221894510040,
            -4544019223021560744, 23465261991844685929951,
        )
        self.assertEqual(subject.tau(5, -7, 31), 5544)
        self.assertEqual(subject.tau(5, 3, 31), 5544)
        self.assertEqual(subject.sym_power_local_factor(5, -7, 31), expected_minus_seven)
        self.assertEqual(subject.sym_power_local_factor(5, 3, 31), expected_three)
        self.assertNotEqual(expected_minus_seven, expected_three)
        self.assertFalse(
            self.fixture["full_factor_diagnostics"][
                "q_31_m_5_ordinary_looking_scalar_witness"
            ]["curve_realization_claimed"]
        )

    def test_m5_binary_quartic_elimination_and_nonsingularity(self) -> None:
        self.assertEqual(quartic_discriminant(1, 5, 9, 5, 1), 189)
        for x in range(-8, 9):
            for y in range(-8, 9):
                for q in (-5, -1, 1, 3, 5, 31):
                    square, quartic = subject.m5_elimination_square(x, y, q)
                    quotient = subject.m5_collision_quotient_closed(x, y, q)
                    self.assertEqual(square - quartic, 3 * quotient)
        self.assertEqual(subject.m5_collision_quotient_closed(-7, 3, 31), 0)
        self.assertEqual(subject.m5_collision_quartic(-7, 3), 361)
        self.assertEqual(subject.m5_elimination_square(-7, 3, 31), (361, 361))
        target = self.fixture["m_5_collision_curve_target"]
        self.assertEqual(target["dehomogenized_quartic_discriminant"], 189)
        self.assertIn("not solved", target["scope"])

    def test_complete_frozen_histogram_transforms_and_extra_fibers(self) -> None:
        source = json.loads(subject.SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
        source_by_q = {int(row["q"]): row for row in source["finite_regressions"]}
        self.assertEqual(set(self.frozen), {3, 5, 7, 11, 13})
        self.assertEqual(
            sum(row["source_histogram_atom_count"] for row in self.frozen.values()), 55
        )
        self.assertEqual(
            sum(row["source_member_count"] for row in self.frozen.values()), 3650
        )

        signature = []
        for q, q_row in self.frozen.items():
            source_histogram = {
                int(t): int(count)
                for t, count in source_by_q[q]["model_trace_histogram"].items()
            }
            self.assertEqual(len(q_row["transforms"]), 18)
            for transform in q_row["transforms"]:
                m = int(transform["m"])
                direct: Counter[int] = Counter()
                class_fibers: dict[int, set[int]] = {}
                for t, count in source_histogram.items():
                    scalar = independent_tau(m, t, q)
                    direct[scalar] += count
                    representative = t if m % 2 else abs(t)
                    class_fibers.setdefault(scalar, set()).add(representative)
                self.assertEqual(
                    transform["transformed_scalar_trace_histogram"],
                    {str(value): direct[value] for value in sorted(direct)},
                )
                self.assertEqual(sum(direct.values()), q_row["source_member_count"])
                expected_extras = {
                    scalar: tuple(sorted(classes))
                    for scalar, classes in class_fibers.items()
                    if len(classes) > 1
                }
                actual_extras = {
                    int(fiber["scalar_trace"]): tuple(
                        int(item["class_representative"])
                        for item in fiber["expected_domain_classes"]
                    )
                    for fiber in transform[
                        "extra_collision_fibers_after_expected_domain_quotient"
                    ]
                }
                self.assertEqual(actual_extras, expected_extras)
                for scalar, classes in sorted(expected_extras.items()):
                    signature.append((q, m, scalar, classes))

        expected_signature = (
            (3, 4, 9, (0, 3)),
            (3, 5, 0, (-3, 0, 3)),
            (3, 6, -27, (0, 3)),
            (3, 6, 13, (1, 2)),
            (3, 10, -243, (0, 3)),
            (3, 11, 0, (-3, 0, 3)),
            (3, 12, 729, (0, 3)),
            (3, 16, 6561, (0, 3)),
            (3, 17, 0, (-3, 0, 3)),
            (3, 18, -19683, (0, 3)),
        )
        self.assertEqual(tuple(signature), expected_signature)

    def test_source_locks_caps_firewall_and_literature_boundary(self) -> None:
        self.assertEqual(
            subject._lf_sha256(subject.SOURCE_FIXTURE_PATH),
            subject.EXPECTED_SOURCE_FIXTURE_SHA256_LF,
        )
        self.assertEqual(
            subject._lf_sha256(subject.SOURCE_PRODUCER_PATH),
            subject.EXPECTED_SOURCE_PRODUCER_SHA256_LF,
        )
        source = json.loads(subject.SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
        unhashed = dict(source)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject.EXPECTED_SOURCE_PAYLOAD_SHA256)
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        self.assertEqual(source["normalization"], subject.EXPECTED_SOURCE_NORMALIZATION)

        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_curve_or_field_enumerations"], 0)
        self.assertEqual(resources["source_histogram_atoms"], 55)
        self.assertEqual(resources["source_members_represented"], 3650)
        self.assertLess(
            resources["accounted_work_units"],
            resources["accounted_work_unit_cap_exclusive"],
        )
        firewall = self.fixture["scope_firewall"]
        self.assertTrue(firewall["scalar_trace_aliasing_is_not_a_full_local_factor_classification"])
        self.assertTrue(firewall["odd_m_5_mod_6_sign_pair_can_still_share_a_full_factor"])
        self.assertTrue(firewall["q_31_witness_is_not_claimed_to_be_realized_by_curves"])
        self.assertTrue(firewall["no_literature_priority_claim"])

        references = self.fixture["literature_boundary"]["references"]
        self.assertEqual(
            [reference["url"] for reference in references],
            [
                "https://doi.org/10.4153/CJM-1994-009-8",
                "https://doi.org/10.1137/130942589",
                "https://arxiv.org/abs/math/0604095",
            ],
        )

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(self.fixture)

    def test_stored_fixture_hashes_refusals_and_optimized_safe_contract(self) -> None:
        stored_path = FUNCTION_FIELD / "elliptic_symmetric_power_trace_aliasing.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (Path(subject.__file__), "script_sha256_lf_normalized"),
            (FUNCTION_FIELD / "ELLIPTIC_SYMMETRIC_POWER_TRACE_ALIASING.md", "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())

        with self.assertRaisesRegex(ValueError, "at least one"):
            subject.build_fixture(())
        with self.assertRaisesRegex(ValueError, "distinct"):
            subject.build_fixture((3, 3))
        with self.assertRaisesRegex(ValueError, "absent"):
            subject.build_fixture((17,))
        with self.assertRaisesRegex(ValueError, "1..18"):
            subject.build_fixture((3,), 19)
        with self.assertRaisesRegex(ValueError, "odd"):
            subject.tau(3, 1, 2)
        with self.assertRaisesRegex(ValueError, "positive odd"):
            subject.odd_collision_quotient(4, 1, 2, 3)
        with self.assertRaisesRegex(ValueError, "positive even"):
            subject.even_collision_quotient(3, 1, 2, 3)
        with self.assertRaisesRegex(ValueError, r"v2\(0\)"):
            subject.v2(0)


if __name__ == "__main__":
    unittest.main()

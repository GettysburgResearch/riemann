"""Independent checks for exact genus-two repeated-factor tomography."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(FUNCTION_FIELD) not in sys.path:
    sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_repeated_factor_tomography as subject


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def rational(pair: list[int]) -> Fraction:
    return Fraction(pair[0], pair[1])


def assert_no_float(testcase: unittest.TestCase, value: object) -> None:
    testcase.assertNotIsInstance(value, float)
    if isinstance(value, dict):
        for item in value.values():
            assert_no_float(testcase, item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            assert_no_float(testcase, item)


def multiply_low(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return tuple(result)


def compose_affine(
    coefficients_low: tuple[int, ...], constant: Fraction, linear: Fraction
) -> tuple[Fraction, ...]:
    """Independently form p(constant+linear*y), low coefficient first."""

    result = [Fraction(0)] * len(coefficients_low)
    power = [Fraction(1)]
    for coefficient in coefficients_low:
        for index, value in enumerate(power):
            result[index] += coefficient * value
        next_power = [Fraction(0)] * (len(power) + 1)
        for index, value in enumerate(power):
            next_power[index] += constant * value
            next_power[index + 1] += linear * value
        power = next_power
    return tuple(result)


class SourceAndLocalTheoremTests(unittest.TestCase):
    def test_all_dependency_hashes_are_authenticated(self) -> None:
        subject._verify_primitive_hashes()
        paths = {
            "histogram_fixture": subject.INPUT_PATH,
            "histogram_producer": subject.INPUT_PRODUCER_PATH,
            "coefficient_arithmetic": subject.COEFFICIENT_ARITHMETIC_PATH,
            "affine_action": subject.AFFINE_ACTION_PATH,
            "zero_fixture": subject.ZERO_FIXTURE_PATH,
            "zero_producer": subject.ZERO_PRODUCER_PATH,
            "zero_note": subject.ZERO_NOTE_PATH,
            "selector_producer": subject.SELECTOR_PRODUCER_PATH,
            "selector_note": subject.SELECTOR_NOTE_PATH,
            "split_fixture": subject.SPLIT_FIXTURE_PATH,
            "split_producer": subject.SPLIT_PRODUCER_PATH,
            "split_note": subject.SPLIT_NOTE_PATH,
            "note": subject.NOTE_PATH,
            "test": subject.TEST_PATH,
        }
        for name, path in paths.items():
            self.assertEqual(subject._lf_sha256(path), subject.EXPECTED_LF_SHA256[name])

    def test_source_and_adapter_substitution_fail_closed(self) -> None:
        changed = dict(subject.EXPECTED_LF_SHA256)
        changed["selector_producer"] = "0" * 64
        with (
            mock.patch.object(subject, "EXPECTED_LF_SHA256", changed),
            self.assertRaisesRegex(ValueError, "digest mismatch"),
        ):
            subject._validated_sources()
        with (
            mock.patch.object(subject, "EXPECTED_ZERO_PAYLOAD_SHA256", "0" * 64),
            self.assertRaisesRegex(ValueError, "payload/source pin mismatch"),
        ):
            subject._validated_sources()

    def test_guard_refuses_above_inclusive_4096_cap(self) -> None:
        guard = subject.SourceAtomGuard()
        guard.preflight(4_096)
        with self.assertRaisesRegex(RuntimeError, "exceeds inclusive cap"):
            guard.preflight(4_097)
        guard.charge("atoms", 4_096)
        with self.assertRaisesRegex(RuntimeError, "would exceed"):
            guard.charge("one_more")

    def test_G_zero_iff_integral_reciprocal_quadratic_square(self) -> None:
        for q in (2, 3, 5, 7, 9, 11):
            for trace in range(-6, 7):
                a = -2 * trace
                b = trace * trace + 2 * q
                factor = subject.repeated_factor(q, a, b)
                self.assertIsNotNone(factor)
                assert factor is not None
                quadratic = (1, -trace, q)
                quartic = (1, a, b, q * a, q * q)
                self.assertEqual(factor.trace, trace)
                self.assertEqual(multiply_low(quadratic, quadratic), quartic)
                self.assertEqual(a * a - 4 * b + 8 * q, 0)
                self.assertEqual(a % 2, 0)

        self.assertIsNone(subject.repeated_factor(5, -8, 25))
        with self.assertRaisesRegex(ValueError, "q must be positive"):
            subject.repeated_factor(0, 0, 0)

    def test_parity_is_forced_not_assumed(self) -> None:
        for q in range(1, 13):
            for a in range(-25, 26):
                numerator = a * a + 8 * q
                if numerator % 4:
                    continue
                b = numerator // 4
                factor = subject.repeated_factor(q, a, b)
                self.assertIsNotNone(factor)
                self.assertEqual(a % 2, 0)

    def test_compact_coordinate_matches_arithmetic_normalization(self) -> None:
        for q, a, b in ((5, -4, 14), (5, 0, 10), (7, 4, 18), (5, -8, 26)):
            factor = subject.repeated_factor(q, a, b)
            self.assertIsNotNone(factor)
            assert factor is not None
            z = factor.compact_z
            self.assertEqual(Fraction(a * a, q), 16 * z)
            self.assertEqual(Fraction(b, q), 2 + 4 * z)
            self.assertEqual(Fraction(a * a - 4 * b + 8 * q, q), 0)


class SelectorLineTests(unittest.TestCase):
    def test_factorized_selector_restrictions_expand_exactly(self) -> None:
        certificate = subject.selector_line_certificate()
        self.assertEqual(
            certificate["expanded_coefficients_low_to_high"],
            {
                "P": [0, 96, -608, 1_024, -512],
                "D": [16, -120, 384, -768, 512],
                "S": [24, -688, 3_968, -9_472, 10_240, -4_096],
            },
        )
        selector_module = subject._load_module(
            subject.SELECTOR_PRODUCER_PATH, "_independent_repeated_selector_test"
        )
        for z in (
            Fraction(0),
            Fraction(1, 25),
            Fraction(1, 7),
            Fraction(1, 5),
            Fraction(1, 4),
            Fraction(1, 2),
            Fraction(3, 4),
            Fraction(4, 5),
            Fraction(1),
        ):
            raw = selector_module.selector_values_from_squared_first_elementary(
                16 * z, 2 + 4 * z
            )
            expected = subject.selector_values_on_repeated_line(z)
            self.assertEqual(Fraction(raw["product_selector"]), expected["P"])
            self.assertEqual(Fraction(raw["doubled_selector"]), expected["D"])
            self.assertEqual(Fraction(raw["sym3_selector"]), expected["S"])

    def test_P_and_D_exact_sign_chambers(self) -> None:
        p_samples = {
            Fraction(0): 0,
            Fraction(1, 8): 1,
            Fraction(1, 4): 0,
            Fraction(1, 2): -1,
            Fraction(3, 4): 0,
            Fraction(7, 8): 1,
            Fraction(1): 0,
        }
        for z, sign in p_samples.items():
            value = subject.selector_values_on_repeated_line(z)["P"]
            self.assertEqual((value > 0) - (value < 0), sign)

        h = lambda z: 16 * z**3 - 20 * z**2 + 7 * z - 2
        self.assertEqual(h(Fraction(11, 12)), Fraction(-7, 108))
        self.assertEqual(h(Fraction(12, 13)), Fraction(10, 2_197))
        # Cubic discriminant, computed independently from (a,b,c,d).
        a, b, c, d = 16, -20, 7, -2
        discriminant = (
            b * b * c * c
            - 4 * a * c**3
            - 4 * b**3 * d
            - 27 * a * a * d * d
            + 18 * a * b * c * d
        )
        self.assertEqual(discriminant, -13_360)
        d_samples = {
            Fraction(0): 1,
            Fraction(1, 4): 0,
            Fraction(1, 2): -1,
            Fraction(4, 5): -1,
            Fraction(19, 20): 1,
            Fraction(1): 1,
        }
        for z, sign in d_samples.items():
            value = subject.selector_values_on_repeated_line(z)["D"]
            self.assertEqual((value > 0) - (value < 0), sign)

    def test_S_root_reduction_and_sign_chambers_are_exact(self) -> None:
        k_coefficients = (3, -80, 336, -512, 256)
        self.assertEqual(
            compose_affine(k_coefficients, Fraction(1, 2), Fraction(1, 2)),
            (Fraction(-1), Fraction(0), Fraction(-12), Fraction(0), Fraction(16)),
        )
        k = lambda z: 256 * z**4 - 512 * z**3 + 336 * z**2 - 80 * z + 3
        self.assertEqual(k(Fraction(1, 25)), Fraction(119_331, 390_625))
        self.assertEqual(k(Fraction(1, 20)), Fraction(-139, 625))
        self.assertEqual(k(Fraction(19, 20)), Fraction(-139, 625))
        self.assertEqual(k(Fraction(24, 25)), Fraction(119_331, 390_625))
        s_samples = {
            Fraction(0): 1,
            Fraction(1, 25): 1,
            Fraction(1, 20): -1,
            Fraction(1, 4): -1,
            Fraction(1, 2): 0,
            Fraction(3, 4): 1,
            Fraction(19, 20): 1,
            Fraction(24, 25): -1,
            Fraction(1): -1,
        }
        for z, sign in s_samples.items():
            value = subject.selector_values_on_repeated_line(z)["S"]
            self.assertEqual((value > 0) - (value < 0), sign)


class FrozenTomographyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["finite_histogram_tomography"]["families"]
        }

    def test_payload_resource_accounting_and_no_floats(self) -> None:
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(payload))
        self.assertEqual(tuple(self.by_q), subject.FROZEN_Q_VALUES)
        self.assertEqual(
            self.fixture["resource_contract"]["source_atom_preflight_count"], 251
        )
        self.assertEqual(
            self.fixture["resource_contract"]["guarded_source_atom_visits"]["total"],
            251,
        )
        assert_no_float(self, self.fixture)

    def test_complete_repeated_census_and_cross_packet_agreement(self) -> None:
        expected = {
            3: (0, 0, Fraction(0), []),
            5: (
                3,
                15,
                Fraction(3, 500),
                [(Fraction(0), 5), (Fraction(1, 5), 10)],
            ),
            7: (
                3,
                84,
                Fraction(2, 343),
                [(Fraction(0), 42), (Fraction(1, 7), 42)],
            ),
        }
        for q, row in self.by_q.items():
            atoms, members, fraction, z_law = expected[q]
            self.assertEqual(row["repeated_signed_atom_count"], atoms)
            self.assertEqual(row["repeated_member_count"], members)
            self.assertEqual(
                rational(row["repeated_member_fraction_of_full_family"]), fraction
            )
            self.assertEqual(
                [
                    (rational(atom["z"]), atom["member_count"])
                    for atom in row["compact_z_member_law"]
                ],
                z_law,
            )
            self.assertEqual(
                row["cross_checks"]["zero_geometry_G_zero_member_count"], members
            )
            self.assertEqual(
                row["cross_checks"]["split_locus_repeated_member_count"], members
            )

    def test_every_repeated_atom_reconstructs_and_lies_on_classifier_diagonal(
        self,
    ) -> None:
        split_module = subject._load_module(
            subject.SPLIT_PRODUCER_PATH, "_independent_repeated_split_test"
        )
        for row in self.by_q.values():
            q = int(row["q"])
            for atom in row["complete_repeated_signed_atoms"]:
                a, b = int(atom["a_D"]), int(atom["b_D"])
                trace = int(atom["repeated_trace_r"])
                quadratic = tuple(atom["quadratic_coefficients_low_to_high"])
                quartic = tuple(atom["quartic_coefficients_low_to_high"])
                self.assertEqual(quadratic, (1, -trace, q))
                self.assertEqual(multiply_low(quadratic, quadratic), quartic)
                self.assertEqual(quartic, (1, a, b, q * a, q * q))
                classification = split_module.classify_factorization(q, a, b)
                self.assertEqual(classification.kind, "split_repeated")
                self.assertEqual(classification.elliptic_traces, (trace, trace))

    def test_observed_D_positivity_is_exactly_a_support_chamber_fact(self) -> None:
        for q in (5, 7):
            row = self.by_q[q]
            self.assertEqual(
                row["selector_sign_member_counts"]["D"],
                {"negative": 0, "zero": 0, "positive": row["repeated_member_count"]},
            )
            for atom in row["complete_repeated_signed_atoms"]:
                z = rational(atom["compact_z"])
                self.assertLess(z, Fraction(1, 4))
                self.assertGreater(rational(atom["selectors"]["D"]), 0)

    def test_integral_hasse_admissible_counterexample_refutes_universal_D_sign(
        self,
    ) -> None:
        packet = self.fixture["universal_D_positivity_no_go"]
        self.assertEqual(
            (packet["q"], packet["trace_r"], packet["a"], packet["b"]), (5, 4, -8, 26)
        )
        self.assertTrue(packet["hasse_admissible_trace"])
        self.assertEqual(rational(packet["G"]), 0)
        self.assertEqual(rational(packet["compact_z"]), Fraction(4, 5))
        self.assertEqual(rational(packet["selectors"]["D"]), Fraction(-11_088, 625))
        self.assertLess(rational(packet["selectors"]["D"]), 0)
        quadratic = tuple(packet["quadratic_coefficients_low_to_high"])
        quartic = tuple(packet["quartic_coefficients_low_to_high"])
        self.assertEqual(quadratic, (1, -4, 5))
        self.assertEqual(multiply_low(quadratic, quadratic), quartic)

    def test_committed_fixture_is_exact_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(subject.Path(subject.__file__)), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("check: ok", completed.stdout)


if __name__ == "__main__":
    unittest.main()

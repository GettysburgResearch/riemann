"""Independent checks for the genus-two interferometry pushforward."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(FUNCTION_FIELD) not in sys.path:
    sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_interferometry_arithmetic_pushforward as subject  # noqa: E402


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def quadratic_add(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def quadratic_scale(
    scalar: Fraction | int, value: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return Fraction(scalar) * value[0], Fraction(scalar) * value[1]


def quadratic_multiply(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
    first_square: Fraction,
) -> tuple[Fraction, Fraction]:
    return (
        left[0] * right[0] + left[1] * right[1] * first_square,
        left[0] * right[1] + left[1] * right[0],
    )


def independent_selector_adapter(
    first_square: Fraction, second: Fraction
) -> dict[str, Fraction]:
    """Newton recurrence in Q[e1]/(e1^2-A), not the exported polynomial."""

    zero = (Fraction(0), Fraction(0))
    e1 = (Fraction(0), Fraction(1))
    e2 = (second, Fraction(0))
    values = [(Fraction(4), Fraction(0)), e1]
    values.append(
        quadratic_add(
            quadratic_multiply(e1, e1, first_square),
            quadratic_scale(-2, e2),
        )
    )
    e1_cubed = quadratic_multiply(
        quadratic_multiply(e1, e1, first_square), e1, first_square
    )
    values.append(
        quadratic_add(
            quadratic_add(
                e1_cubed,
                quadratic_scale(
                    -3, quadratic_multiply(e1, e2, first_square)
                ),
            ),
            quadratic_scale(3, e1),
        )
    )
    for frequency in range(4, 11):
        value = zero
        terms = (
            quadratic_multiply(e1, values[frequency - 1], first_square),
            quadratic_scale(
                -1,
                quadratic_multiply(e2, values[frequency - 2], first_square),
            ),
            quadratic_multiply(e1, values[frequency - 3], first_square),
            quadratic_scale(-1, values[frequency - 4]),
        )
        for term in terms:
            value = quadratic_add(value, term)
        values.append(value)

    def interferometer(left: int, right: int) -> tuple[Fraction, Fraction]:
        return quadratic_add(
            quadratic_multiply(values[left], values[right], first_square),
            quadratic_scale(-1, values[left + right]),
        )

    i22 = interferometer(2, 2)
    i44 = interferometer(4, 4)
    i11 = interferometer(1, 1)
    i15 = interferometer(1, 5)
    i28 = interferometer(2, 8)
    result = {
        "P": quadratic_add(i22, quadratic_scale(-1, i44)),
        "D": quadratic_add(
            quadratic_add(quadratic_scale(-1, i11), quadratic_scale(2, i15)),
            i44,
        ),
        "S": quadratic_scale(-2, i28),
    }
    for name, value in result.items():
        if value[1] != 0:
            raise AssertionError(f"selector {name} retained an odd e1 part")
    return {name: value[0] for name, value in result.items()}


class SourceLockAndAdapterTests(unittest.TestCase):
    def test_every_primitive_hash_is_the_frozen_expected_digest(self) -> None:
        subject._verify_primitive_hashes()
        paths = {
            "histogram_fixture": subject.INPUT_PATH,
            "histogram_producer": subject.INPUT_PRODUCER_PATH,
            "coefficient_arithmetic": subject.COEFFICIENT_ARITHMETIC_PATH,
            "affine_action": subject.AFFINE_ACTION_PATH,
            "selector_producer": subject.SELECTOR_PRODUCER_PATH,
            "selector_note": subject.SELECTOR_NOTE_PATH,
        }
        for name, path in paths.items():
            self.assertEqual(
                subject._lf_normalized_sha256(path),
                subject.EXPECTED_LF_SHA256[name],
            )

    def test_source_and_selector_pins_fail_closed(self) -> None:
        with mock.patch.object(subject, "EXPECTED_INPUT_PAYLOAD_SHA256", "0" * 64):
            with self.assertRaisesRegex(ValueError, "payload/source pin mismatch"):
                subject._validated_input()
        changed = dict(subject.EXPECTED_LF_SHA256)
        changed["selector_producer"] = "0" * 64
        with mock.patch.object(subject, "EXPECTED_LF_SHA256", changed):
            with self.assertRaisesRegex(ValueError, "digest mismatch"):
                subject._load_selector_module()

    def test_guard_refuses_before_processing_more_than_4096_atoms(self) -> None:
        guard = subject.SourceAtomGuard()
        guard.preflight(4_096)
        with self.assertRaisesRegex(RuntimeError, "exceeds inclusive cap"):
            guard.preflight(4_097)
        guard.charge("atoms", 4_096)
        with self.assertRaisesRegex(RuntimeError, "would exceed"):
            guard.charge("one_more")

    def test_independent_quadratic_recurrence_matches_all_251_atoms(self) -> None:
        _, families = subject._validated_input()
        module = subject._load_selector_module()
        visits = 0
        for family in families:
            q = int(family["q"])
            for atom in family["joint_a_D_b_D_law"]["atoms"]:
                a, b = int(atom["a_D"]), int(atom["b_D"])
                expected = independent_selector_adapter(
                    Fraction(a * a, q), Fraction(b, q)
                )
                actual = subject.selector_values_from_arithmetic_coefficients(
                    q, a, b, module
                )
                self.assertEqual(actual, expected)
                visits += 1
        self.assertEqual(visits, 251)


class FrozenPushforwardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["exact_frozen_member_weight_laws"]["families"]
        }

    def test_fixture_payload_and_complete_joint_masses(self) -> None:
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(payload))
        self.assertEqual(tuple(self.by_q), subject.FROZEN_Q_VALUES)
        for q, row in self.by_q.items():
            atoms = row["joint_selector_law"]["atoms"]
            self.assertEqual(sum(atom[-1] for atom in atoms), row["member_count"])
            self.assertEqual(
                row["input_signed_source_atom_count"],
                subject.EXPECTED_ATOM_COUNTS[q],
            )

    def test_marginals_reconstruct_joint_law_and_summary(self) -> None:
        for row in self.by_q.values():
            reconstructed = {name: Counter() for name in subject.SELECTOR_ORDER}
            for atom in row["joint_selector_law"]["atoms"]:
                values = {
                    "P": Fraction(atom[0], atom[1]),
                    "D": Fraction(atom[2], atom[3]),
                    "S": Fraction(atom[4], atom[5]),
                }
                for name in subject.SELECTOR_ORDER:
                    reconstructed[name][values[name]] += atom[-1]
            for name in subject.SELECTOR_ORDER:
                packet = row["marginal_selector_laws"][name]
                serialized = Counter(
                    {
                        Fraction(numerator, denominator): count
                        for numerator, denominator, count in packet["atoms"]
                    }
                )
                self.assertEqual(serialized, reconstructed[name])
                mass = sum(serialized.values())
                mean = sum(value * count for value, count in serialized.items()) / mass
                self.assertEqual(Fraction(*packet["mean"]), mean)
                signs = Counter({"negative": 0, "zero": 0, "positive": 0})
                for value, count in serialized.items():
                    signs[subject._sign(value)] += count
                self.assertEqual(dict(signs), packet["sign_member_counts"])

    def test_covariance_is_exact_symmetric_and_psd_on_rational_vectors(self) -> None:
        probes = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (2, -3, 5))
        for row in self.by_q.values():
            covariance = [
                [Fraction(*entry) for entry in matrix_row]
                for matrix_row in row["covariance_matrix_P_D_S"]
            ]
            self.assertEqual(covariance, [list(column) for column in zip(*covariance)])
            for vector in probes:
                quadratic = sum(
                    vector[i] * covariance[i][j] * vector[j]
                    for i in range(3)
                    for j in range(3)
                )
                self.assertGreaterEqual(quadratic, 0)

    def test_outer_one_percent_tail_has_exact_tie_semantics(self) -> None:
        for row in self.by_q.values():
            for name in subject.SELECTOR_ORDER:
                packet = row["marginal_selector_laws"][name]
                histogram = {
                    Fraction(numerator, denominator): count
                    for numerator, denominator, count in packet["atoms"]
                }
                tail = packet["outer_one_percent_absolute_tail"]
                threshold = Fraction(*tail["absolute_threshold"])
                count = sum(
                    weight for value, weight in histogram.items() if abs(value) >= threshold
                )
                self.assertEqual(count, tail["member_count_including_ties"])
                self.assertGreaterEqual(count, tail["target_member_count_ceiling"])
                larger_count = sum(
                    weight for value, weight in histogram.items() if abs(value) > threshold
                )
                self.assertLess(larger_count, tail["target_member_count_ceiling"])

    def test_exceptional_strata_are_nonempty_exact_conditionals(self) -> None:
        for q, row in self.by_q.items():
            member_count = row["member_count"]
            strata = row["exceptional_coefficient_strata"]
            for name, packet in strata.items():
                if q == 3 and name == "repeated_plus_q_split":
                    self.assertEqual(packet["status"], "EMPTY_IN_FROZEN_FAMILY")
                    self.assertEqual(packet["member_count"], 0)
                    self.assertIsNone(packet["conditional_mean"])
                    continue
                self.assertEqual(packet["status"], "NONEMPTY_EXACT_CONDITIONAL")
                self.assertGreater(packet["member_count"], 0)
                self.assertLess(packet["member_count"], member_count)
                self.assertEqual(
                    Fraction(*packet["member_fraction"]),
                    Fraction(packet["member_count"], member_count),
                )

    def test_exact_frozen_means_signs_and_tails(self) -> None:
        expected_means = {
            3: (Fraction(-2584, 2187), Fraction(232, 2187), Fraction(8, 6561)),
            5: (Fraction(-57468, 78125), Fraction(16148, 78125), Fraction(7152, 390625)),
            7: (Fraction(-441712, 823543), Fraction(156896, 823543), Fraction(-2952, 5764801)),
        }
        expected_signs = {
            3: ((96, 6, 60), (102, 0, 60), (45, 36, 81)),
            5: ((1410, 30, 1060), (1464, 0, 1036), (1211, 250, 1039)),
            7: ((8484, 42, 5880), (8820, 0, 5586), (6552, 1092, 6762)),
        }
        expected_tails = {
            3: ((Fraction(728, 81), 6), (Fraction(1376, 81), 9), (Fraction(4112, 243), 6)),
            5: ((Fraction(5872, 625), 40), (Fraction(10532, 625), 40), (Fraction(48696, 3125), 106)),
            7: ((Fraction(23368, 2401), 252), (Fraction(40468, 2401), 168), (Fraction(284040, 16807), 462)),
        }
        sign_order = ("negative", "zero", "positive")
        for q, row in self.by_q.items():
            self.assertEqual(
                tuple(Fraction(*pair) for pair in row["mean_vector_P_D_S"]),
                expected_means[q],
            )
            for index, name in enumerate(subject.SELECTOR_ORDER):
                packet = row["marginal_selector_laws"][name]
                self.assertEqual(
                    tuple(packet["sign_member_counts"][sign] for sign in sign_order),
                    expected_signs[q][index],
                )
                tail = packet["outer_one_percent_absolute_tail"]
                self.assertEqual(
                    (
                        Fraction(*tail["absolute_threshold"]),
                        tail["member_count_including_ties"],
                    ),
                    expected_tails[q][index],
                )

    def test_exceptional_stratum_counts_and_orbit_ambiguity_are_frozen(self) -> None:
        expected_strata = {
            3: (27, 0, 18, 12, 6),
            5: (705, 15, 55, 50, 5),
            7: (3570, 84, 378, 336, 42),
        }
        stratum_order = (
            "integral_plus_q_split",
            "repeated_plus_q_split",
            "sym3_coefficient_curve",
            "sym3_nodal_ghost",
            "sym3_generic_integer_trace_candidate",
        )
        expected_orbit_ambiguity = {3: (3, 66), 5: (10, 966), 7: (17, 7896)}
        for q, row in self.by_q.items():
            strata = row["exceptional_coefficient_strata"]
            self.assertEqual(
                tuple(strata[name]["member_count"] for name in stratum_order),
                expected_strata[q],
            )
            orbit = row["uniform_affine_orbit_weighting"]
            self.assertEqual(
                (
                    orbit["ambiguous_B_bucket_count"],
                    orbit["member_count_in_ambiguous_B_buckets"],
                ),
                expected_orbit_ambiguity[q],
            )

    def test_matched_stratum_conditionals_and_tail_overlaps(self) -> None:
        expected_matched_means = {
            3: (Fraction(128, 81), None, Fraction(0)),
            5: (Fraction(10112, 29375), Fraction(12544, 1875), Fraction(24)),
            7: (Fraction(45376, 40817), Fraction(24812, 2401), Fraction(24)),
        }
        expected_s_tail_overlaps = {
            3: (0, 0, 0, 0, 0),
            5: (105, 15, 5, 0, 5),
            7: (336, 84, 42, 0, 42),
        }
        stratum_order = (
            "integral_plus_q_split",
            "repeated_plus_q_split",
            "sym3_coefficient_curve",
            "sym3_nodal_ghost",
            "sym3_generic_integer_trace_candidate",
        )
        for q, row in self.by_q.items():
            strata = row["exceptional_coefficient_strata"]
            p_split, d_repeated, s_generic = expected_matched_means[q]
            self.assertEqual(
                Fraction(*strata["integral_plus_q_split"]["conditional_mean"]["P"]),
                p_split,
            )
            if d_repeated is None:
                self.assertIsNone(strata["repeated_plus_q_split"]["conditional_mean"])
            else:
                self.assertEqual(
                    Fraction(*strata["repeated_plus_q_split"]["conditional_mean"]["D"]),
                    d_repeated,
                )
            self.assertEqual(
                Fraction(*strata["sym3_generic_integer_trace_candidate"]["conditional_mean"]["S"]),
                s_generic,
            )
            self.assertEqual(
                tuple(
                    strata[name]["member_count_in_each_selector_outer_one_percent_tail"]["S"]
                    for name in stratum_order
                ),
                expected_s_tail_overlaps[q],
            )
            for name in stratum_order:
                overlaps = strata[name][
                    "member_count_in_each_selector_outer_one_percent_tail"
                ]
                self.assertEqual((overlaps["P"], overlaps["D"]), (0, 0))

    def test_orbit_law_is_refused_exactly_when_B_buckets_are_ambiguous(self) -> None:
        for row in self.by_q.values():
            packet = row["uniform_affine_orbit_weighting"]
            self.assertGreater(packet["ambiguous_B_bucket_count"], 0)
            self.assertEqual(
                packet["status"],
                "NOT_IDENTIFIABLE_FROM_B_AGGREGATED_ORBIT_SOURCE",
            )
            self.assertIsNone(packet["exact_uniform_orbit_selector_law"])
            self.assertIsNotNone(packet["refusal_reason"])


if __name__ == "__main__":
    unittest.main()

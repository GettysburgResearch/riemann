"""Independent focused checks for the frozen genus-two integral split locus."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(FUNCTION_FIELD) not in sys.path:
    sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_endoscopic_split_locus as subject  # noqa: E402

NO_Q_ELLIPTIC_FORM_FACTORIZATION = (
    "no_integral_q_elliptic_form_factorization"
)


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    return hashlib.sha256(encoded).hexdigest()


def lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


class ExactClassificationTests(unittest.TestCase):
    def test_complement_label_does_not_claim_absolute_irreducibility(self) -> None:
        result = subject.classify_factorization(5, 0, -10)
        self.assertEqual(result.kind, NO_Q_ELLIPTIC_FORM_FACTORIZATION)
        self.assertEqual(
            subject.multiply_low((1, 0, -5), (1, 0, -5)),
            [1, 0, -10, 0, 25],
        )
        self.assertIsNone(subject.factorization_residual(5, 0, -10))

    def test_square_discriminant_criterion_and_factorization_on_grid(self) -> None:
        saw_repeated = False
        saw_distinct = False
        saw_complement = False
        for q in range(2, 14):
            for a in range(-10, 11):
                for b in range(-2 * q, 6 * q + 1):
                    result = subject.classify_factorization(q, a, b)
                    delta = a * a - 4 * b + 8 * q
                    self.assertEqual(result.delta, delta)
                    square = delta >= 0 and isqrt(delta) ** 2 == delta
                    parity = square and (isqrt(delta) - a) % 2 == 0
                    self.assertEqual(result.in_integral_split_locus, parity)
                    if result.in_integral_split_locus:
                        traces = result.elliptic_traces
                        self.assertIsNotNone(traces)
                        left, right = traces or (0, 0)
                        self.assertEqual(left + right, -a)
                        self.assertEqual(left * right, b - 2 * q)
                        self.assertEqual((left - right) ** 2, delta)
                        self.assertEqual(
                            subject.factorization_residual(q, a, b),
                            [0, 0, 0, 0, 0],
                        )
                        saw_repeated |= result.kind == "split_repeated"
                        saw_distinct |= result.kind == "split_distinct"
                    else:
                        self.assertIsNone(result.elliptic_traces)
                        saw_complement = True
        self.assertTrue(saw_repeated and saw_distinct and saw_complement)

    def test_newton_second_power_and_echo_recurrence(self) -> None:
        for a, b, q in ((0, 0, 3), (4, 14, 5), (-7, 24, 7), (5, 15, 5)):
            self.assertEqual(
                subject.frobenius_power_coefficients(a, b, q, 2),
                (2 * b - a * a, b * b - 2 * q * a * a + 2 * q * q),
            )
            direct = []
            for power in range(1, subject.MAX_ECHO_POWER + 1):
                coefficients = subject.frobenius_power_coefficients(a, b, q, power)
                direct.append(subject.balanced_echo_value(*coefficients, q, power))
            self.assertEqual(
                subject.echo_recurrence_profile(
                    direct[0], direct[1], subject.MAX_ECHO_POWER
                )[1:],
                direct,
            )


class FrozenHistogramReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["frozen_histogram_results"]["families"]
        }
        cls.input_data = json.loads(subject.INPUT_PATH.read_text(encoding="utf-8"))

    def test_independent_complete_histogram_classification(self) -> None:
        expected = {
            3: {
                "counts": ((0, 0), (9, 27), (23, 135)),
                "split_fraction": Fraction(1, 6),
                "delta": {4: (2, 6), 9: (4, 12), 16: (1, 3), 25: (2, 6)},
            },
            5: {
                "counts": ((3, 15), (20, 690), (58, 1795)),
                "split_fraction": Fraction(141, 500),
                "delta": {
                    0: (3, 15), 4: (2, 40), 9: (6, 160), 16: (3, 120),
                    25: (4, 120), 36: (2, 180), 49: (2, 40), 64: (1, 30),
                },
            },
            7: {
                "counts": ((3, 84), (30, 3486), (105, 10836)),
                "split_fraction": Fraction(85, 343),
                "delta": {
                    0: (3, 84), 4: (4, 168), 9: (8, 630), 16: (3, 504),
                    25: (6, 672), 36: (2, 756), 49: (4, 336), 64: (1, 252),
                    81: (2, 168),
                },
            },
        }
        families = self.input_data["frozen_enumeration_facts"]["families"]
        for family in families:
            q = family["q"]
            counts = {kind: Counter() for kind in subject.CLASS_ORDER}
            delta_histogram: dict[int, Counter[str]] = {}
            for atom in family["joint_a_D_b_D_law"]["atoms"]:
                a, b, weight = atom["a_D"], atom["b_D"], atom["member_count"]
                delta = a * a - 4 * b + 8 * q
                root = isqrt(delta)
                if delta == 0:
                    kind = "split_repeated"
                elif root * root == delta and (root - a) % 2 == 0:
                    kind = "split_distinct"
                else:
                    kind = NO_Q_ELLIPTIC_FORM_FACTORIZATION
                counts[kind]["atoms"] += 1
                counts[kind]["members"] += weight
                if kind in subject.SPLIT_CLASSES:
                    delta_histogram.setdefault(delta, Counter())["atoms"] += 1
                    delta_histogram[delta]["members"] += weight

            observed = tuple(
                (counts[kind]["atoms"], counts[kind]["members"])
                for kind in subject.CLASS_ORDER
            )
            self.assertEqual(observed, expected[q]["counts"])
            self.assertEqual(
                {
                    delta: (row["atoms"], row["members"])
                    for delta, row in delta_histogram.items()
                },
                expected[q]["delta"],
            )
            split = self.by_q[q]["factorization_classification"]["integral_split_locus"]
            self.assertEqual(
                Fraction(*split["member_fraction"]), expected[q]["split_fraction"]
            )
            self.assertEqual(split["member_count"], sum(pair[1] for pair in observed[:2]))

    def test_every_serialized_split_atom_reconstructs_the_source_polynomial(self) -> None:
        for q, family in self.by_q.items():
            split = family["factorization_classification"]
            atoms = split["split_signed_coefficient_atoms"]
            self.assertEqual(len(atoms), split["integral_split_locus"]["signed_coefficient_atom_count"])
            for atom in atoms:
                traces = atom["elliptic_traces_sorted"]
                self.assertEqual(sum(traces), -atom["a_D"])
                self.assertEqual(traces[0] * traces[1], atom["b_D"] - 2 * q)
                self.assertLessEqual(traces[0] ** 2, 4 * q)
                self.assertLessEqual(traces[1] ** 2, 4 * q)
                self.assertEqual(
                    subject.factorization_residual(q, atom["a_D"], atom["b_D"]),
                    [0, 0, 0, 0, 0],
                )

    def test_detector_fibers_do_not_identify_the_split_locus(self) -> None:
        expected = {
            3: {"B": (14, 1, 12), "F": (12, 1, 24), "echo": (17, 1, 12)},
            5: {"B": (33, 3, 246), "F": (24, 6, 700), "echo": (39, 1, 6)},
            7: {"B": (55, 5, 2898), "F": (53, 5, 2856), "echo": (67, 2, 924)},
        }
        for q, family in self.by_q.items():
            correlations = family["detector_correlations"]
            packets = {
                "B": correlations["B"]["fiber_purity"],
                "F": correlations["F"]["fiber_purity"],
                "echo": correlations["complete_frobenius_echo"]["fiber_purity"],
            }
            for name, packet in packets.items():
                self.assertEqual(
                    (
                        packet["fiber_count"],
                        packet["mixed_factorization_fiber_count"],
                        packet["member_count_in_mixed_fibers"],
                    ),
                    expected[q][name],
                )
                self.assertGreater(packet["mixed_factorization_fiber_count"], 0)
                for mixed in packet["mixed_factorization_fibers"]:
                    self.assertGreaterEqual(len(mixed["factorization_types"]), 2)
                    self.assertTrue(
                        any(
                            kind in subject.SPLIT_CLASSES
                            for kind in mixed["factorization_types"]
                        )
                    )
                    self.assertTrue(
                        any(
                            kind not in subject.SPLIT_CLASSES
                            for kind in mixed["factorization_types"]
                        )
                    )
            self.assertEqual(
                packets["B"]["multi_factorization_label_fiber_count"],
                packets["B"]["mixed_factorization_fiber_count"]
                + packets["B"]["same_split_status_multi_label_fiber_count"],
            )
        self.assertEqual(
            self.by_q[5]["detector_correlations"]["B"]["fiber_purity"][
                "same_split_status_multi_label_fiber_count"
            ],
            1,
        )
        self.assertEqual(
            self.by_q[5]["detector_correlations"]["complete_frobenius_echo"][
                "fiber_purity"
            ]["same_split_status_multi_label_fiber_count"],
            1,
        )

    def test_exact_cyclotomic_certificates_cross_the_split_boundary(self) -> None:
        expected = {
            3: {
                (0, 0, NO_Q_ELLIPTIC_FORM_FACTORIZATION, 12, 8),
                (9, 6, "split_distinct", 6, 12),
            },
            5: {
                (0, -10, NO_Q_ELLIPTIC_FORM_FACTORIZATION, 1, 2),
                (0, 0, NO_Q_ELLIPTIC_FORM_FACTORIZATION, 50, 8),
                (0, 10, "split_repeated", 5, 4),
                (25, 15, NO_Q_ELLIPTIC_FORM_FACTORIZATION, 24, 10),
            },
            7: {
                (0, 0, NO_Q_ELLIPTIC_FORM_FACTORIZATION, 336, 8),
                (0, 14, "split_repeated", 42, 4),
            },
        }
        for q, family in self.by_q.items():
            packet = family["detector_correlations"]["cyclotomic_normalized_spectrum"]
            observed = {
                (
                    row["a_D_squared"], row["b_D"], row["factorization_type"],
                    row["member_count"], row["minimum_even_power_to_identity"],
                )
                for row in packet["certified_states"]
            }
            self.assertEqual(observed, expected[q])
            self.assertTrue(any(row[2] in subject.SPLIT_CLASSES for row in observed))
            self.assertTrue(
                any(
                    row[2] == NO_Q_ELLIPTIC_FORM_FACTORIZATION
                    for row in observed
                )
            )

    def test_tail_extrema_keep_three_distinct_frobenius_shapes(self) -> None:
        expected_f_minimum = {
            3: (Fraction(-8, 3), {"split_distinct": 6}),
            5: (Fraction(-116, 25), {"split_repeated": 10}),
            7: (
                Fraction(-282, 49),
                {NO_Q_ELLIPTIC_FORM_FACTORIZATION: 42},
            ),
        }
        for q, family in self.by_q.items():
            minimum = family["tail_and_extreme_shares"]["F"]["minimum"]
            expected_value, expected_nonzero = expected_f_minimum[q]
            self.assertEqual(Fraction(*minimum["values"][0]), expected_value)
            observed_nonzero = {
                kind: count
                for kind, count in minimum["member_counts_by_factorization_type"].items()
                if count
            }
            self.assertEqual(observed_nonzero, expected_nonzero)
        self.assertEqual(
            self.by_q[3]["tail_and_extreme_shares"]["F"]["far_negative_F_below_minus_4"]["member_count"],
            0,
        )
        self.assertGreater(
            self.by_q[5]["tail_and_extreme_shares"]["F"]["far_negative_F_below_minus_4"]["member_count"],
            0,
        )
        self.assertGreater(
            self.by_q[7]["tail_and_extreme_shares"]["F"]["far_negative_F_below_minus_4"]["member_count"],
            0,
        )

    def test_orbit_counts_are_bounded_not_invented(self) -> None:
        expected = {
            3: ("EXACTLY_IDENTIFIED_FROM_AGGREGATED_SOURCE_AND_ORBIT_SIZE_BOUNDS", 5, 5),
            5: ("EXACTLY_IDENTIFIED_FROM_AGGREGATED_SOURCE_AND_ORBIT_SIZE_BOUNDS", 38, 38),
            7: ("BOUNDED_NOT_IDENTIFIABLE_FROM_AGGREGATED_SOURCE", 86, 88),
        }
        for q, family in self.by_q.items():
            orbit = family["affine_orbit_weighting"]
            lower, upper = orbit["integral_split_locus_affine_orbit_count_bounds"]
            status, expected_lower, expected_upper = expected[q]
            self.assertEqual((orbit["status"], lower, upper), (status, expected_lower, expected_upper))
            self.assertEqual(
                orbit["integral_split_locus_affine_orbit_count"],
                lower if lower == upper else None,
            )
            self.assertGreater(len(orbit["mixed_B_buckets"]), 0)
            self.assertLessEqual(upper, orbit["source_total_affine_orbit_count"])
            for row in orbit["mixed_B_buckets"]:
                self.assertGreater(row["split_member_count"], 0)
                self.assertGreater(
                    row["no_q_elliptic_form_factorization_member_count"], 0
                )

    def test_q7_ambiguity_survives_retained_orbit_sizes_and_state_totals(self) -> None:
        source = next(
            family
            for family in self.input_data["frozen_enumeration_facts"]["families"]
            if family["q"] == 7
        )
        self.assertEqual(
            source["affine_orbit_analysis"]["orbit_size_histogram"],
            {"21": 12, "42": 337},
        )
        support = source["balanced_support"]["atoms"]
        self.assertEqual(
            sum(
                2 * atom["affine_orbit_count"] - atom["member_count"] // 21
                for atom in support
            ),
            12,
        )

        family = self.by_q[7]
        orbit_rows = {
            row["B_numerator_J"]: row
            for row in family["affine_orbit_weighting"]["mixed_B_buckets"]
        }
        fiber_rows = {}
        for row in family["detector_correlations"]["B"]["fiber_purity"][
            "mixed_factorization_fibers"
        ]:
            j_value = int(Fraction(*row["detector_value"]) * 49)
            fiber_rows[j_value] = row

        possible_by_bucket = {}
        for j_value, orbit_row in orbit_rows.items():
            states = fiber_rows[j_value]["states"]
            possibilities = {(0, 0, 0)}
            for state in states:
                units = state["member_count"] // 21
                self.assertEqual(21 * units, state["member_count"])
                state_options = []
                for small_orbits in range(units + 1):
                    if (units - small_orbits) % 2:
                        continue
                    large_orbits = (units - small_orbits) // 2
                    orbit_count = small_orbits + large_orbits
                    split_count = (
                        orbit_count
                        if state["factorization_type"] in subject.SPLIT_CLASSES
                        else 0
                    )
                    state_options.append((orbit_count, small_orbits, split_count))
                possibilities = {
                    (o1 + o2, s1 + s2, p1 + p2)
                    for o1, s1, p1 in possibilities
                    for o2, s2, p2 in state_options
                }

            source_orbit_count = orbit_row["source_affine_orbit_count"]
            total_members = (
                orbit_row["split_member_count"]
                + orbit_row["no_q_elliptic_form_factorization_member_count"]
            )
            required_small = 2 * source_orbit_count - total_members // 21
            possible_by_bucket[j_value] = {
                split_count
                for orbit_count, small_count, split_count in possibilities
                if orbit_count == source_orbit_count and small_count == required_small
            }

        self.assertEqual(possible_by_bucket[-100], {7, 8})
        self.assertEqual(possible_by_bucket[-4], {6, 7})
        self.assertTrue(
            all(
                len(counts) == 1
                for j_value, counts in possible_by_bucket.items()
                if j_value not in {-100, -4}
            )
        )
        totals = {
            family["affine_orbit_weighting"][
                "exact_split_orbits_from_homogeneous_B_buckets"
            ]
        }
        for j_value in sorted(possible_by_bucket):
            totals = {
                partial + contribution
                for partial in totals
                for contribution in possible_by_bucket[j_value]
            }
        self.assertEqual(totals, {86, 87, 88})


class ProvenanceScopeAndResourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_committed_fixture_payload_and_all_file_locks(self) -> None:
        committed = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(committed, self.fixture)
        unhashed = dict(committed)
        digest = unhashed.pop("payload_sha256")
        self.assertEqual(digest, canonical_sha256(unhashed))
        self.assertEqual(
            committed["producer_and_source_locks"]["input_payload_sha256_required"],
            subject.EXPECTED_INPUT_PAYLOAD_SHA256,
        )
        locks = committed["producer_and_source_locks"]["locks"]
        expected_paths = {
            "input_fixture": subject.INPUT_PATH,
            "input_producer": subject.INPUT_PRODUCER_PATH,
            "producer": Path(subject.__file__),
            "note": subject.NOTE_PATH,
            "test": subject.TEST_PATH,
        }
        self.assertEqual(set(locks), set(expected_paths))
        for name, path in expected_paths.items():
            self.assertEqual(locks[name]["sha256_lf_normalized"], lf_sha256(path))
        self.assertEqual(
            locks["input_fixture"]["payload_sha256"],
            subject.EXPECTED_INPUT_PAYLOAD_SHA256,
        )

    def test_resource_cap_and_no_enumerator_or_float_dependency(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertFalse(resource["finite_field_enumeration"])
        self.assertFalse(resource["curve_or_family_member_enumeration"])
        self.assertFalse(resource["random_sampling"])
        self.assertFalse(resource["floating_point_arithmetic"])
        self.assertLess(
            resource["guarded_transform_work_units"]["total"],
            resource["transform_work_unit_cap_exclusive"],
        )
        self.assertEqual(resource["transform_work_unit_cap_exclusive"], 20_000)
        source = Path(subject.__file__).read_text(encoding="utf-8")
        for forbidden in (
            "import genus2_q_scan",
            "import balanced_control_family_scan",
            "itertools.product",
            "import random",
            "float(",
        ):
            self.assertNotIn(forbidden, source)
        guard = subject.HistogramGuard()
        guard.charge("test", subject.TRANSFORM_WORK_UNIT_CAP_EXCLUSIVE - 1)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            guard.charge("test")

    def test_interpretation_and_three_field_firewalls_are_explicit(self) -> None:
        firewall = self.fixture["interpretation_firewall"]
        self.assertIn("Honda-Tate/Tate", firewall["imported_theorem_target_not_used"])
        self.assertIn("principal", firewall["polarization_warning"])
        self.assertIn("does not prove geometric simplicity", firewall["geometric_warning"])
        quarantine = self.fixture["quarantined_patterns_and_targets"]
        self.assertEqual(quarantine["status"], "NO_ALL_Q_FREQUENCY_FORMULA_CLAIMED")
        self.assertIn("three-field census", quarantine["warning"])


if __name__ == "__main__":
    unittest.main()

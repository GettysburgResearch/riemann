"""Focused exact tests for the tensor/endoscopic rank-drop bridge."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import tensor_endoscopic_rank_drop_bridge as subject  # noqa: E402


def lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


class TensorEndoscopicRankDropBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            row["q"]: row
            for row in cls.fixture["frozen_product_model_incidence"]
        }

    def test_master_sum_of_squares_from_independent_coefficient_formulas(self) -> None:
        for q in (3, 5, 7):
            for A in range(-3, 4):
                for a in range(-3, 4):
                    for b in range(-2, 2 * q + 3):
                        v = Fraction(
                            A * A * b + q * a * a - 2 * q * b,
                            q * q,
                        )
                        h = Fraction(
                            A**4
                            + A * A * a * a
                            - 4 * q * A * A
                            - 2 * q * a * a
                            + b * b
                            + 2 * q * q,
                            q * q,
                        )
                        L = h + 2 * v + 2
                        numerator = subject.transverse_detector_numerator(
                            A, a, b, q
                        )
                        self.assertEqual(L, Fraction(numerator, q * q))
                        self.assertGreaterEqual(numerator, 0)
                        self.assertEqual(
                            numerator == 0,
                            bool(subject.rank_branch_labels(A, a, b, q)),
                        )

    def test_scheme_primary_decomposition_and_multiplicity_boundary(self) -> None:
        geometry = self.fixture["symbolic_bridge"]
        scheme = geometry["rank_line_pullback"]
        generators = scheme["computed_monomial_generators_A_a_R"]
        self.assertEqual(generators["I_rank"], [[0, 0, 2], [1, 1, 0]])
        self.assertEqual(generators["intersection"], generators["I_rank"])
        self.assertEqual(
            subject._monomial_ideal_intersection(
                ((1, 0, 0), (0, 0, 2)),
                ((0, 1, 0), (0, 0, 2)),
            ),
            ((0, 0, 2), (1, 1, 0)),
        )
        # R is not in I_rank but R^2 is: the doubled transverse direction is
        # genuine and must not be silently replaced by the radical.
        rank_generators = ((0, 0, 2), (1, 1, 0))
        self.assertFalse(any(subject._divides(generator, (0, 0, 1)) for generator in rank_generators))
        self.assertTrue(any(subject._divides(generator, (0, 0, 2)) for generator in rank_generators))

        for A in range(-4, 5):
            for a in range(-4, 5):
                for R in range(-3, 4):
                    delta = a * a + 4 * A * A - 4 * R
                    self.assertEqual(delta - (a + 2 * A) ** 2, -4 * (R + A * a))
                    if A * a == 0 and R == 0:
                        self.assertEqual(delta, (a + 2 * A) ** 2)
                        self.assertEqual(delta, (a - 2 * A) ** 2)

    def test_both_rank_branches_factor_and_are_integral_split(self) -> None:
        for q in (3, 5, 7, 9):
            for a in range(-6, 7):
                classification = subject.classify_integral_q_split(q, a, 2 * q)
                self.assertTrue(classification.split)
                self.assertEqual(
                    classification.traces, tuple(sorted((0, -a)))
                )
                self.assertEqual(
                    subject.factorization_residual(q, a, 2 * q),
                    (0, 0, 0, 0, 0),
                )
                self.assertIn(
                    "E_trace_zero_zero_factor_branch",
                    subject.rank_branch_labels(0, a, 2 * q, q),
                )

            for A in range(-6, 7):
                b = 2 * q - A * A
                classification = subject.classify_integral_q_split(q, 0, b)
                self.assertTrue(classification.split)
                self.assertEqual(
                    classification.traces, tuple(sorted((-A, A)))
                )
                self.assertEqual(
                    subject.factorization_residual(q, 0, b),
                    (0, 0, 0, 0, 0),
                )
                self.assertIn(
                    "C_trace_zero_matching_antidiagonal_branch",
                    subject.rank_branch_labels(A, 0, b, q),
                )

    def test_exact_converses_on_both_singular_components(self) -> None:
        saw_split_non_rank_e = False
        saw_split_non_rank_c = False
        for q in (3, 5, 7):
            for A in range(-5, 6):
                for a in range(-5, 6):
                    for b in range(-2 * q, 4 * q + 1):
                        classification = subject.classify_integral_q_split(q, a, b)
                        rank = subject.reduced_rank_drop(A, a, b, q)
                        self.assertEqual(
                            rank,
                            subject.transverse_detector_numerator(A, a, b, q) == 0,
                        )
                        if rank:
                            self.assertTrue(classification.split)
                            self.assertEqual(
                                classification.kind == "split_repeated",
                                A == 0 and a == 0 and b == 2 * q,
                            )
                        if classification.split and A == 0:
                            traces = classification.traces or ()
                            self.assertEqual(rank, 0 in traces)
                            saw_split_non_rank_e |= not rank
                        if classification.split and a == 0:
                            traces = classification.traces or ()
                            self.assertEqual(rank, tuple(sorted((-A, A))) == traces)
                            saw_split_non_rank_c |= not rank
                        if A != 0 and a != 0:
                            self.assertFalse(rank)
        self.assertTrue(saw_split_non_rank_e)
        self.assertTrue(saw_split_non_rank_c)

    def test_complete_frozen_incidence_counts_and_fractions(self) -> None:
        expected = {
            3: {
                "counts": (2916, 486, 0, 486, 1068, 66, 150, 84, 336, 0, 66),
                "fractions": (
                    Fraction(11, 486),
                    Fraction(11, 81),
                    Fraction(25, 178),
                    Fraction(11, 25),
                    Fraction(11, 178),
                ),
                "rank_atoms": 6,
            },
            5: {
                "counts": (
                    250000,
                    70500,
                    1500,
                    69000,
                    82480,
                    5000,
                    21700,
                    16700,
                    48800,
                    100,
                    4900,
                ),
                "fractions": (
                    Fraction(1, 50),
                    Fraction(10, 141),
                    Fraction(1085, 4124),
                    Fraction(50, 217),
                    Fraction(125, 2062),
                ),
                "rank_atoms": 11,
            },
            7: {
                "counts": (
                    4235364,
                    1049580,
                    24696,
                    1024884,
                    1155420,
                    72324,
                    287532,
                    215208,
                    762048,
                    1764,
                    70560,
                ),
                "fractions": (
                    Fraction(41, 2401),
                    Fraction(41, 595),
                    Fraction(163, 655),
                    Fraction(41, 163),
                    Fraction(41, 655),
                ),
                "rank_atoms": 13,
            },
        }
        count_names = (
            "all_product_pairs",
            "integral_split",
            "split_repeated",
            "split_distinct",
            "tensor_singular",
            "rank_drop",
            "split_and_tensor_singular",
            "split_singular_not_rank",
            "split_outside_tensor_singular",
            "rank_split_repeated",
            "rank_split_distinct",
        )
        fraction_names = (
            "rank_drop_of_all_product_pairs",
            "rank_drop_of_integral_split_pairs",
            "split_singular_of_tensor_singular",
            "rank_drop_of_split_singular",
            "rank_drop_of_tensor_singular",
        )
        for q, row in self.by_q.items():
            self.assertEqual(
                tuple(
                    row["incidence_counts"][name]["product_pair_count"]
                    for name in count_names
                ),
                expected[q]["counts"],
            )
            self.assertEqual(
                tuple(
                    Fraction(*row["incidence_fractions"][name])
                    for name in fraction_names
                ),
                expected[q]["fractions"],
            )
            self.assertEqual(
                len(row["rank_drop_product_atoms"]), expected[q]["rank_atoms"]
            )

    def test_inclusive_branch_converse_census(self) -> None:
        expected = {
            3: ((648, 108, 48, 60), (540, 54, 18, 36), 0),
            5: ((50000, 14100, 2900, 11200), (40600, 9500, 2200, 7300), 100),
            7: (
                (605052, 149940, 37044, 112896),
                (642096, 160524, 37044, 123480),
                1764,
            ),
        }
        for q, row in self.by_q.items():
            census = row["inclusive_branch_converse_census"]
            e = census["E_trace_zero_component"]
            c = census["C_trace_zero_component"]
            self.assertEqual(
                (
                    e["all_component_pairs"],
                    e["integral_split_pairs"],
                    e["rank_pairs_zero_factor"],
                    e["split_but_nonzero_factor_pairs"],
                ),
                expected[q][0],
            )
            self.assertEqual(
                (
                    c["all_component_pairs"],
                    c["integral_split_pairs"],
                    c["rank_pairs_trace_match"],
                    c["split_but_trace_mismatch_pairs"],
                ),
                expected[q][1],
            )
            self.assertEqual(census["rank_branch_intersection_pairs"], expected[q][2])

    def test_detector_recognition_and_locked_genus2_failures(self) -> None:
        expected_contingency = {
            3: (66, 420, 0, 2430),
            5: (5000, 65500, 0, 179500),
            7: (72324, 977256, 0, 3185784),
        }
        expected_failures = {
            3: {"B": (14, 1, 12), "F": (12, 1, 24), "complete_balanced_echo": (17, 1, 12)},
            5: {"B": (33, 3, 246), "F": (24, 6, 700), "complete_balanced_echo": (39, 1, 6)},
            7: {"B": (55, 5, 2898), "F": (53, 5, 2856), "complete_balanced_echo": (67, 2, 924)},
        }
        for q, row in self.by_q.items():
            detector = row["detector_recognition"]
            contingency = detector["L_zero_contingency"]
            self.assertEqual(
                tuple(contingency.values()), expected_contingency[q]
            )
            self.assertEqual(
                detector["rank_as_split_detector"]["precision_P_split_given_L_zero"],
                [1, 1],
            )
            for name, expected in expected_failures[q].items():
                packet = detector["locked_genus2_detector_failures"][name]
                self.assertEqual(
                    (
                        packet["fiber_count"],
                        packet["mixed_split_status_fiber_count"],
                        packet["genus2_member_count_in_mixed_fibers"],
                    ),
                    expected,
                )

    def test_rank_rows_reconstruct_branches_and_split_factors(self) -> None:
        for q, row in self.by_q.items():
            total = 0
            for atom in row["rank_drop_product_atoms"]:
                A = atom["tensor_polynomial_coefficient_A"]
                a = atom["genus2_a"]
                b = atom["genus2_b"]
                self.assertEqual(atom["source_geometric_trace_t_E"], -A)
                self.assertEqual(atom["R"], 0)
                self.assertEqual(atom["q_squared_L_numerator"], 0)
                self.assertTrue(atom["branches"])
                classification = subject.classify_integral_q_split(q, a, b)
                self.assertTrue(classification.split)
                self.assertEqual(
                    atom["integral_factor_traces_sorted"],
                    list(classification.traces or ()),
                )
                self.assertEqual(
                    subject.factorization_residual(q, a, b),
                    (0, 0, 0, 0, 0),
                )
                total += atom["product_pair_count"]
            self.assertEqual(
                total, row["incidence_counts"]["rank_drop"]["product_pair_count"]
            )
            self.assertEqual(
                len(row["complete_product_atom_classification_ledger_sha256"]), 64
            )

    def test_payload_source_locks_resource_cap_and_firewalls(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        locks = stored["producer_and_source_locks"]["locks"]
        expected_names = {
            "tensor_fixture",
            "endoscopic_fixture",
            "genus1_fixture",
            "balanced_fixture",
            "tensor_producer",
            "endoscopic_producer",
            "genus1_producer",
            "balanced_producer",
            "producer",
            "note",
            "test",
        }
        self.assertEqual(set(locks), expected_names)
        for lock in locks.values():
            path = ROOT / lock["path"]
            self.assertEqual(lock["sha256_lf_normalized"], lf_sha256(path))
            if "payload_sha256" in lock:
                self.assertEqual(
                    lock["payload_sha256"],
                    json.loads(path.read_text(encoding="utf-8"))["payload_sha256"],
                )

        resources = stored["resource_contract"]
        self.assertEqual(resources["guarded_work_units"]["total"], 2471)
        self.assertLess(
            resources["guarded_work_units"]["total"],
            resources["strict_histogram_work_cap_exclusive"],
        )
        self.assertTrue(resources["strict_cap_satisfied"])
        self.assertEqual(resources["field_curve_variety_or_member_enumerations"], 0)
        self.assertEqual(resources["floating_point_values"], 0)

        firewall = " ".join(stored["scope_firewall"].values()).lower()
        self.assertIn("nilpotent", firewall)
        self.assertIn("honda-tate", firewall)
        self.assertIn("principal polarization", firewall)
        self.assertIn("complex", firewall)
        self.assertIn("not a coarse moduli", firewall)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(stored)

        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5))
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.transverse_detector_numerator(1, 2, 3, 0)
        guard = subject.WorkGuard()
        guard.charge("near_cap", subject.HISTOGRAM_WORK_CAP_EXCLUSIVE - 1)
        with self.assertRaisesRegex(RuntimeError, "strict"):
            guard.charge("over_cap")


if __name__ == "__main__":
    unittest.main()

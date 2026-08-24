"""Focused replay tests for the tensor trace-zero singular-stratum packet."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import tensor_trace_zero_singular_strata as subject  # noqa: E402


class TensorTraceZeroSingularStrataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            row["q"]: row for row in cls.fixture["frozen_histogram_census"]
        }

    def test_exact_partials_full_reduced_singular_locus_and_transverse_rank(self) -> None:
        geometry = subject.symbolic_geometry_certificate()
        self.assertEqual(
            geometry["exact_partial_derivatives"],
            {
                "dF_du": "2*u*h-4*u^3+4*u*v+2*u-2*w",
                "dF_dv": "2*u^2",
                "dF_dw": "-2*u-2*w",
                "dF_dh": "u^2",
            },
        )
        adapted = geometry["adapted_coordinates"]
        self.assertEqual(adapted["identity"], "F=L*u^2-u^4-r^2")
        self.assertEqual(adapted["pinch_coordinate"], "lambda=L-u^2")
        self.assertEqual(adapted["pinch_point_identity"], "r^2=u^2*lambda")
        self.assertEqual(adapted["total_rank_drop_germ"], "pinch point times the free v-line")
        self.assertEqual(
            adapted["jacobian_ideal_in_characteristic_not_2"], "(r,u^2,u*L)"
        )
        self.assertEqual(adapted["reduced_jacobian_ideal"], "rad(r,u^2,u*L)=(u,r)=(u,w)")
        self.assertEqual(
            geometry["full_reduced_affine_singular_locus"],
            "u=w=0, with v and h free",
        )

        for v, h in ((0, 0), (3, -8), (Fraction(-7, 5), Fraction(4, 9))):
            self.assertEqual(subject.hypersurface_value(0, v, 0, h), 0)
            self.assertEqual(
                subject.hypersurface_gradient(0, v, 0, h),
                (Fraction(0),) * 4,
            )
        transverse = geometry["transverse_quadratic_cone"]
        self.assertEqual(transverse["matrix_determinant"], "-(h+2*v+2)=-L")
        self.assertEqual(transverse["rank_on_line"], 1)
        self.assertEqual(transverse["rank_off_line"], 2)
        self.assertIn(
            "slice-dependent A3",
            transverse["fixed_original_v_h_slice_on_rank_drop_line_over_C"],
        )
        self.assertIn("only the real point", transverse["real_fixed_slice"])

    def test_pullback_factorization_and_both_square_restrictions(self) -> None:
        pullback = self.fixture["symbolic_geometry"]["coefficient_map_pullback"]
        self.assertEqual(pullback["adapted_relations"]["L=h+2*v+2"], "t^2+x*y=t^2+u^2")
        self.assertEqual(
            pullback["reduced_rank_drop_preimage"],
            "(x=0,z=2) union (y=0,z=2-x)",
        )
        self.assertIn("over Q", pullback["base_ring_scope"])
        scheme = pullback["scheme_pullback_after_clearing_q"]
        self.assertEqual(scheme["R"], "A^2+b-2*q")
        self.assertEqual(scheme["singular_plane_ideal"], "(A*a)")
        self.assertEqual(scheme["rank_drop_line_ideal"], "(A*a,R^2)")
        self.assertIn("(A,b-2*q) intersect", scheme["reduced_rank_drop_ideal"])

        # Independent set-theoretic check of the radical decomposition on a grid.
        for A in range(-3, 4):
            for a in range(-3, 4):
                for b in range(-2, 13):
                    R = A * A + b - 10
                    left = A * a == 0 and R * R == 0
                    right = (A == 0 and b == 10) or (a == 0 and R == 0)
                    self.assertEqual(left, right)

        q = 5
        # E trace zero: b=2q, and q(v+4)=a^2.
        u, v, w, h = subject.coefficient_image(0, 3, 2 * q, q)
        self.assertEqual((u, v, w, h), (0, Fraction(-11, 5), 0, Fraction(12, 5)))
        self.assertEqual(subject.transverse_detector_numerator(0, 3, 2 * q, q), 0)
        self.assertEqual(q * (v + 4), 3**2)
        self.assertEqual(h, -2 * v - 2)
        left = [1, 0, q]
        right = [1, 3, q]
        self.assertEqual(
            [
                sum(
                    left[i] * right[k - i]
                    for i in range(len(left))
                    if 0 <= k - i < len(right)
                )
                for k in range(len(left) + len(right) - 1)
            ],
            [1, 3, 2 * q, 3 * q, q * q],
        )

        # C trace zero: the sign is b=2q-A^2, so v=-(b/q)^2.
        A = 2
        b = 2 * q - A * A
        u, v, w, h = subject.coefficient_image(A, 0, b, q)
        self.assertEqual((u, v, w), (0, -Fraction(b * b, q * q), 0))
        self.assertEqual(h, 2 * Fraction(b * b, q * q) - 2)
        self.assertEqual(subject.transverse_detector_numerator(A, 0, b, q), 0)
        self.assertEqual(2 * q - b, A * A)
        left = [1, A, q]
        right = [1, -A, q]
        self.assertEqual(
            [
                sum(
                    left[i] * right[k - i]
                    for i in range(len(left))
                    if 0 <= k - i < len(right)
                )
                for k in range(len(left) + len(right) - 1)
            ],
            [1, 0, 2 * q - A * A, 0, q * q],
        )

        self.assertEqual(subject.coefficient_image(0, 0, 2 * q, q), (0, -4, 0, 6))

    def test_frozen_counts_are_an_independent_locked_histogram_partition(self) -> None:
        genus1 = json.loads(subject.GENUS1_FIXTURE_PATH.read_text(encoding="utf-8"))
        balanced = json.loads(subject.BALANCED_FIXTURE_PATH.read_text(encoding="utf-8"))
        genus1_by_q = {row["q"]: row for row in genus1["finite_regressions"]}
        balanced_by_q = {
            row["q"]: row
            for row in balanced["frozen_enumeration_facts"]["families"]
        }
        operations = 0
        expected_counts = {
            3: {
                "E_trace_zero_only": 528,
                "C_trace_zero_only": 420,
                "both_trace_zero": 120,
                "neither_trace_zero": 1848,
                "singular_trace_zero_total": 1068,
                "transverse_degenerate_union": 66,
            },
            5: {
                "E_trace_zero_only": 41880,
                "C_trace_zero_only": 32480,
                "both_trace_zero": 8120,
                "neither_trace_zero": 167520,
                "singular_trace_zero_total": 82480,
                "transverse_degenerate_union": 5000,
            },
            7: {
                "E_trace_zero_only": 513324,
                "C_trace_zero_only": 550368,
                "both_trace_zero": 91728,
                "neither_trace_zero": 3079944,
                "singular_trace_zero_total": 1155420,
                "transverse_degenerate_union": 72324,
            },
        }
        expected_component_counts = {
            3: (648, 540, 120, 48, 18, 0),
            5: (50000, 40600, 8120, 2900, 2200, 100),
            7: (605052, 642096, 91728, 37044, 37044, 1764),
        }
        for q in subject.FROZEN_Q_VALUES:
            counts = {
                "E_trace_zero_only": 0,
                "C_trace_zero_only": 0,
                "both_trace_zero": 0,
                "neither_trace_zero": 0,
                "transverse_degenerate_union": 0,
            }
            for trace_text, elliptic_count in genus1_by_q[q]["model_trace_histogram"].items():
                A = -int(trace_text)
                for atom in balanced_by_q[q]["joint_a_D_b_D_law"]["atoms"]:
                    operations += 1
                    a = int(atom["a_D"])
                    b = int(atom["b_D"])
                    weight = int(elliptic_count) * int(atom["member_count"])
                    if A == 0 and a == 0:
                        counts["both_trace_zero"] += weight
                    elif A == 0:
                        counts["E_trace_zero_only"] += weight
                    elif a == 0:
                        counts["C_trace_zero_only"] += weight
                    else:
                        counts["neither_trace_zero"] += weight
                    if (A == 0 or a == 0) and (A * A + b == 2 * q):
                        counts["transverse_degenerate_union"] += weight
            stored = self.by_q[q]["trace_zero_partition_counts"]
            for name, count in counts.items():
                self.assertEqual(stored[name], count)
            self.assertEqual(
                stored["singular_trace_zero_total"],
                counts["E_trace_zero_only"]
                + counts["C_trace_zero_only"]
                + counts["both_trace_zero"],
            )
            self.assertEqual(stored, expected_counts[q])
            components = self.by_q[q]["component_incidence_census"]
            self.assertEqual(
                tuple(
                    components[name]["pair_count"]
                    for name in (
                        "E_trace_zero_component",
                        "C_trace_zero_component",
                        "component_intersection",
                        "E_component_rank_drop",
                        "C_component_rank_drop",
                        "rank_drop_intersection",
                    )
                ),
                expected_component_counts[q],
            )
        self.assertEqual(operations, 2471)

    def test_v_h_detector_summaries_moment_shares_and_rank_drop_law(self) -> None:
        expected_first_moments = {
            3: {
                "E_trace_zero_only": (Fraction(-28, 33), Fraction(142, 99), Fraction(172, 99)),
                "C_trace_zero_only": (Fraction(-4, 35), Fraction(2, 35), Fraction(64, 35)),
                "both_trace_zero": (Fraction(-4, 15), Fraction(38, 15), Fraction(4)),
                "singular_trace_zero_total": (
                    Fraction(-44, 89),
                    Fraction(814, 801),
                    Fraction(1624, 801),
                ),
                "transverse_degenerate_union": (Fraction(-16, 11), Fraction(10, 11), Fraction(0)),
            },
            5: {
                "E_trace_zero_only": (
                    Fraction(-956, 1047),
                    Fraction(8546, 5235),
                    Fraction(3152, 1745),
                ),
                "C_trace_zero_only": (
                    Fraction(-24, 145),
                    Fraction(1651, 10150),
                    Fraction(18591, 10150),
                ),
                "both_trace_zero": (Fraction(-12, 29), Fraction(2662, 1015), Fraction(3852, 1015)),
                "singular_trace_zero_total": (
                    Fraction(-2936, 5155),
                    Fraction(29671, 25775),
                    Fraction(51861, 25775),
                ),
                "transverse_degenerate_union": (
                    Fraction(-1088, 625),
                    Fraction(926, 625),
                    Fraction(0),
                ),
            },
            7: {
                "E_trace_zero_only": (
                    Fraction(-1868, 2037),
                    Fraction(23762, 14259),
                    Fraction(26128, 14259),
                ),
                "C_trace_zero_only": (
                    Fraction(-174, 637),
                    Fraction(1136, 1911),
                    Fraction(3914, 1911),
                ),
                "both_trace_zero": (Fraction(-58, 91), Fraction(1852, 637), Fraction(178, 49)),
                "singular_trace_zero_total": (
                    Fraction(-18876, 32095),
                    Fraction(40258, 32095),
                    Fraction(9528, 4585),
                ),
                "transverse_degenerate_union": (
                    Fraction(-488, 287),
                    Fraction(402, 287),
                    Fraction(0),
                ),
            },
        }
        for q, row in self.by_q.items():
            all_pairs = row["product_model_pair_count"]
            for name, stratum in row["strata"].items():
                total = stratum["pair_count"]
                laws = stratum["coordinate_distribution_summaries_and_moment_shares"]
                for law in laws.values():
                    mass = Fraction(*law["moments_0_through_2"][0]["all_product_pair_moment_share"])
                    self.assertEqual(mass, Fraction(total, all_pairs))
                self.assertEqual(
                    tuple(
                        Fraction(*laws[coordinate]["moments_0_through_2"][1]["conditional_mean"])
                        for coordinate in ("v", "h", "transverse_rank_drop_detector_L")
                    ),
                    expected_first_moments[q][name],
                )
                self.assertEqual(
                    laws["transverse_rank_drop_detector_L"]["numerator_name"],
                    "L_num",
                )
            degenerate = row["strata"]["transverse_degenerate_union"]
            joint = degenerate["complete_joint_v_h_transverse_detector_law"]
            self.assertEqual(
                sum(atom["pair_count"] for atom in joint["atoms"]),
                degenerate["pair_count"],
            )
            for atom in joint["atoms"]:
                V, H, L_num = atom["numerators_v_h_L_over_q_squared"]
                self.assertEqual(L_num, H + 2 * V + 2 * q * q)
                self.assertEqual(L_num, 0)
                self.assertEqual(math.isqrt(L_num) ** 2, L_num)

    def test_payload_note_test_and_dependency_hashes(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))
        locks = stored["producer_and_source_locks"]["locks"]
        self.assertIn("note", locks)
        self.assertIn("test", locks)
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                lock["sha256_lf_normalized"], hashlib.sha256(normalized).hexdigest()
            )
        self.assertEqual(
            locks["genus1_fixture"]["payload_sha256"],
            json.loads(subject.GENUS1_FIXTURE_PATH.read_text(encoding="utf-8"))["payload_sha256"],
        )
        self.assertEqual(
            locks["balanced_fixture"]["payload_sha256"],
            json.loads(subject.BALANCED_FIXTURE_PATH.read_text(encoding="utf-8"))["payload_sha256"],
        )
        self.assertEqual(
            locks["product_tensor_fixture"]["payload_sha256"],
            json.loads(subject.PRODUCT_FIXTURE_PATH.read_text(encoding="utf-8"))["payload_sha256"],
        )

    def test_resource_contract_scope_firewall_and_refusals(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["histogram_pair_operations"], 2471)
        self.assertLess(
            resources["histogram_pair_operations"], resources["strict_histogram_pair_cap"]
        )
        self.assertTrue(resources["strict_cap_satisfied"])
        self.assertEqual(resources["field_or_curve_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_arithmetic_or_results"], 0)
        firewall = " ".join(self.fixture["scope_firewall"].values()).lower()
        self.assertIn("coefficient", firewall)
        self.assertIn("not evidence", firewall)
        self.assertIn("singular variety", firewall)
        self.assertIn("honda-tate", firewall)
        self.assertIn("no jacobian splitting", firewall)

        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5))
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.coefficient_image(1, 2, 3, 0)
        guard = subject.HistogramPairGuard(subject.MAX_HISTOGRAM_PAIR_OPERATIONS - 2)
        guard.charge()
        with self.assertRaisesRegex(RuntimeError, "strict histogram-pair cap"):
            guard.charge()


if __name__ == "__main__":
    unittest.main()

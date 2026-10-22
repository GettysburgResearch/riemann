"""Replay tests for the elliptic Sym^4 thin-SO(5)-slice packet."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_symmetric_fourth_so5_slice as subject  # noqa: E402
import genus1_cubic_family_laws as genus1  # noqa: E402


def independent_multiply(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def independent_su2_sym4_moments(maximum: int) -> list[int]:
    """Weyl-character extraction, independent of Clebsch--Gordan code.

    A symmetric SU(2) character is sum_m c_m*chi_m.  Its Laurent coefficients
    satisfy c_0=[z^0]-[z^2].  Apply this to chi_4^n.
    """

    chi4 = {4: 1, 2: 1, 0: 1, -2: 1, -4: 1}
    power = {0: 1}
    moments: list[int] = []
    for order in range(maximum + 1):
        moments.append(power.get(0, 0) - power.get(2, 0))
        if order == maximum:
            continue
        output: Counter[int] = Counter()
        for left_exponent, left_value in power.items():
            for right_exponent, right_value in chi4.items():
                output[left_exponent + right_exponent] += left_value * right_value
        power = dict(output)
    return moments


def explicit_all_q_laws(
    q: int, theta12: int | None = None
) -> dict[str, Fraction]:
    if theta12 is None:
        theta12 = genus1.delta_frobenius_trace(q)
    return {
        "mean_y": -Fraction(1, q**3),
        "mean_d": -Fraction(1, q**2) - Fraction(1, q**4),
        "mean_y_squared": Fraction(1)
        - Fraction(1, q**2)
        - Fraction(1, q**3)
        - Fraction(1, q**4)
        - Fraction(1, q**5),
        "mean_y_times_d": -Fraction(2, q**2)
        - Fraction(2, q**3)
        - Fraction(2, q**4)
        - Fraction(1, q**5)
        - Fraction(1 + theta12, q**6),
        "mean_d_squared": Fraction(2)
        - Fraction(2, q**2)
        - Fraction(4, q**3)
        - Fraction(3, q**4)
        - Fraction(3, q**5)
        - Fraction(1 + theta12, q**6)
        - Fraction(1, q**7),
        "mean_y_cubed": Fraction(1)
        - Fraction(3, q**2)
        - Fraction(5, q**3)
        - Fraction(4, q**4)
        - Fraction(3, q**5)
        - Fraction(2 * (1 + theta12), q**6)
        - Fraction(1, q**7),
    }


class EllipticSymmetricFourthSO5SliceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["frozen_histogram_pushforwards"]
        }

    def test_two_local_factor_derivations_and_exact_middle_division(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            for a in (-8, -3, -1, 0, 2, 5, 9):
                with self.subTest(q=q, a=a):
                    closed = subject.sym4_local_coefficients_closed(a, q)
                    newton = subject.sym4_local_coefficients_via_newton(a, q)
                    paired = subject.sym4_local_coefficients_via_paired_roots(a, q)
                    self.assertEqual(closed, newton)
                    self.assertEqual(newton, paired)

                    u = a * a - 2 * q
                    independent = independent_multiply(
                        (1, -(q**2)),
                        independent_multiply(
                            (1, -(u * u - 2 * q * q), q**4),
                            (1, -q * u, q**4),
                        ),
                    )
                    self.assertEqual(closed, independent)
                    quotient = subject.pointwise_central_quotient(a, q)
                    self.assertEqual(
                        closed, independent_multiply((1, -(q**2)), quotient)
                    )
                    self.assertEqual(closed[3], -(q**2) * closed[2])
                    self.assertEqual(closed[4], -(q**6) * closed[1])
                    self.assertEqual(closed[5], -(q**10))

    def test_normalized_shape_parameterization_and_elimination(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25):
            for a in range(-8, 9):
                y, d = subject.normalized_so5_coordinates(a, q)
                w, parameter_y, parameter_d = subject.normalized_parameterization(a, q)
                self.assertEqual((y, d), (parameter_y, parameter_d))
                self.assertEqual(w, Fraction(a * a, q) - 2)
                self.assertEqual(subject.rank_one_curve_residual(y, d), 0)
                coefficients = subject.sym4_local_coefficients_closed(a, q)
                normalized = tuple(
                    Fraction(coefficient, q ** (2 * degree))
                    for degree, coefficient in enumerate(coefficients)
                )
                self.assertEqual(normalized, (1, -y, d, -d, y, -1))

        # The eliminated equation has a singular point at the collapsed pair.
        y = d = Fraction(0)
        self.assertEqual(2 * d + y, 0)
        self.assertEqual(d - 2 * y - 3 * y * y, 0)
        self.assertNotEqual(math.isqrt(5) ** 2, 5)
        for q in (3, 5, 7, 9, 11, 13, 25):
            for a in range(-20, 21):
                self.assertNotEqual(subject.normalized_so5_coordinates(a, q), (0, 0))
        geometry = self.fixture["rank_one_SO5_slice"]
        self.assertIn("no rational root", geometry["arithmetic_node_exclusion"])
        target = next(
            row
            for row in self.fixture["next_targets"]
            if row["name"] == "rank_one_curve_singular_point_exclusion"
        )
        self.assertIn("no arithmetic input hits", target["known"])
        self.assertNotIn("which finite fields", target["open"])

    def test_su2_character_decompositions_and_all_q_stack_laws(self) -> None:
        self.assertEqual(subject.Y_CHARACTER, {4: 1})
        self.assertEqual(subject.D_CHARACTER, {2: 1, 6: 1})
        self.assertEqual(
            subject.su2_tensor(subject.Y_CHARACTER, subject.Y_CHARACTER),
            {0: 1, 2: 1, 4: 1, 6: 1, 8: 1},
        )
        self.assertEqual(
            subject.su2_tensor(subject.Y_CHARACTER, subject.D_CHARACTER),
            {2: 2, 4: 2, 6: 2, 8: 1, 10: 1},
        )
        self.assertEqual(
            subject.su2_tensor(subject.D_CHARACTER, subject.D_CHARACTER),
            {0: 2, 2: 2, 4: 4, 6: 3, 8: 3, 10: 1, 12: 1},
        )
        self.assertEqual(
            subject.su2_character_power(subject.Y_CHARACTER, 3),
            {0: 1, 2: 3, 4: 5, 6: 4, 8: 3, 10: 2, 12: 1},
        )
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            with self.subTest(q=q):
                self.assertEqual(
                    subject.bounded_exact_coordinate_laws(q),
                    explicit_all_q_laws(q),
                )

        self.assertEqual(
            subject.symbolic_all_q_coordinate_laws(),
            subject.SYMBOLIC_ALL_Q_COORDINATE_LAWS,
        )
        with self.assertRaisesRegex(ValueError, "characteristic<=1000"):
            subject.bounded_exact_coordinate_laws(1009)
        supplied_theta12 = 123_456_789
        self.assertEqual(
            subject.exact_coordinate_laws_with_theta12(1009, supplied_theta12),
            explicit_all_q_laws(1009, supplied_theta12),
        )
        for invalid_theta12 in (True, False, Fraction(1, 2), 1.0, "17", None):
            with self.subTest(invalid_theta12=invalid_theta12):
                with self.assertRaisesRegex(TypeError, "integer exact"):
                    subject.exact_coordinate_laws_with_theta12(
                        1009, invalid_theta12  # type: ignore[arg-type]
                    )
        contract = self.fixture["all_q_stack_laws"]["numeric_evaluator_contract"]
        self.assertEqual(contract["automatic_characteristic_cap_inclusive"], 1000)
        self.assertIn("refuses explicitly", contract["q_1009_boundary"])
        self.assertIn("without coercion", contract["supplied_trace_type_contract"])
        self.assertEqual(
            self.fixture["all_q_stack_laws"]["symbolic_formulas"],
            subject.symbolic_all_q_coordinate_laws(),
        )

    def test_compact_haar_moments_expose_the_thin_slice(self) -> None:
        expected_su2 = [1, 0, 1, 1, 5, 16, 65, 260, 1085]
        expected_so5 = [1, 0, 1, 0, 3, 1, 15, 15, 105]
        self.assertEqual(subject.su2_sym4_haar_trace_moments(), expected_su2)
        self.assertEqual(independent_su2_sym4_moments(8), expected_su2)
        self.assertEqual(subject.so5_standard_haar_trace_moments(), expected_so5)
        comparison = self.fixture["compact_group_comparison"]
        self.assertEqual(comparison["SU2_Sym4_trace_moments"], expected_su2)
        self.assertEqual(comparison["SO5_standard_trace_moments"], expected_so5)
        self.assertEqual(
            comparison["first_separation"],
            {
                "order": 3,
                "SU2_Sym4": 1,
                "SO5_standard": 0,
                "reason": "the principal SO(3) slice has a cubic invariant in Sym^4, whereas the SO(5) standard representation has none",
            },
        )

    def test_complete_locked_histogram_pushforward_independently(self) -> None:
        source = json.loads(subject.GENUS1_FIXTURE_PATH.read_text(encoding="utf-8"))
        source_by_q = {int(row["q"]): row for row in source["finite_regressions"]}
        expected_sizes = {3: (18, 4), 5: (100, 5), 7: (294, 6), 11: (1210, 7), 13: (2028, 8)}
        for q, row in self.by_q.items():
            histogram = {
                int(a): int(count)
                for a, count in source_by_q[q]["model_trace_histogram"].items()
            }
            direct: Counter[tuple[Fraction, Fraction]] = Counter()
            for a, count in histogram.items():
                r = Fraction(a * a, q)
                y = r * r - 3 * r + 1
                d = (r - 2) * y
                direct[(y, d)] += count
                self.assertEqual(
                    subject.sym4_local_coefficients_via_newton(a, q),
                    subject.sym4_local_coefficients_via_paired_roots(a, q),
                )
            members, support = expected_sizes[q]
            self.assertEqual(sum(direct.values()), members)
            self.assertEqual(len(direct), support)
            self.assertEqual(row["member_count"], members)
            self.assertEqual(row["complete_rank_one_pushforward"]["support_size"], support)

            names_and_powers = {
                "mean_y": (1, 0),
                "mean_d": (0, 1),
                "mean_y_squared": (2, 0),
                "mean_y_times_d": (1, 1),
                "mean_d_squared": (0, 2),
                "mean_y_cubed": (3, 0),
            }
            for name, (y_power, d_power) in names_and_powers.items():
                actual = Fraction(
                    sum(
                        count * y**y_power * d**d_power
                        for (y, d), count in direct.items()
                    ),
                    members,
                )
                self.assertEqual(
                    actual,
                    Fraction(*row["selected_exact_coordinate_laws"][name]),
                )
                self.assertEqual(actual, explicit_all_q_laws(q)[name])
            negative = row["negative_control_wrong_weight_factor"]
            self.assertTrue(negative["nonzero"])
            self.assertNotEqual(Fraction(*negative["P_at_T_equals_1_over_q"]), 0)

    def test_fiber_family_and_genus2_comparison_firewalls(self) -> None:
        levels = self.fixture[
            "pointwise_q_squared_eigenline_without_forced_common_line"
        ]
        self.assertIn("irreducible", levels["ambient_representation_level"])
        self.assertIn("not proved", levels["actual_family_level"])
        self.assertIn("procyclic", levels["individual_finite_field_fiber_level"])
        self.assertIn("not preserved", levels["why_the_axis_varies"])
        self.assertIn("not asserted", levels["pointwise_quotient_status"])

        comparison = self.fixture["genus2_primitive_exterior_comparator"]
        self.assertIn("1-u*z+v*z^2-v*z^3+u*z^4-z^5", comparison["shared_universal_shape"])
        self.assertIn("d^2+y*d-y^2-y^3=0", comparison["rank_contrast"])
        self.assertIn("not make", comparison["not_an_identification"])
        self.assertIn("no pre-existing common line", comparison["central_eigenvalue_parallel"])
        self.assertIn("does not prove any common line", comparison["central_eigenvalue_parallel"])
        self.assertEqual(
            comparison["locked_comparator_payload_sha256"],
            subject.EXPECTED_PRIMITIVE_PAYLOAD_SHA256,
        )
        firewall = self.fixture["scope_firewall"]
        self.assertIn("compared with", firewall["no_family_identification"])
        self.assertIn("does not provide", firewall["no_pointwise_to_global_line"])
        self.assertIn("RH", firewall["no_analytic_or_RH_claim"])

    def test_fixture_hashes_source_locks_and_resource_cap(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        locks = stored["producer_and_source_locks"]["locks"]
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(
                b"\r", b"\n"
            )
            self.assertEqual(
                lock["sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )
        self.assertEqual(
            locks["genus1_fixture"]["payload_sha256"],
            subject.EXPECTED_GENUS1_PAYLOAD_SHA256,
        )
        self.assertEqual(
            locks["primitive_exterior_fixture"]["payload_sha256"],
            subject.EXPECTED_PRIMITIVE_PAYLOAD_SHA256,
        )
        resources = stored["resource_contract"]
        total = resources["accounted_work_unit_ledger"][
            "total_accounted_work_units"
        ]
        self.assertLess(total, resources["exclusive_accounted_work_unit_cap"])
        self.assertEqual(resources["field_or_curve_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertEqual(resources["automatic_theta12_characteristic_cap_inclusive"], 1000)
        self.assertIn("not literal", resources["unit_definition"])

        literature = stored["literature_boundary"]
        self.assertIn("classical", literature["classical_context"])
        self.assertIn("10.1090/S0894-0347-02-00410-1", literature["primary_reference"])
        self.assertIn("thin-curve", literature["project_specific_contribution"])

    def test_refusals(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5, 7))
        for q in (2, 4, 8, 15, 21):
            with self.subTest(q=q):
                with self.assertRaisesRegex(ValueError, "odd|prime power"):
                    subject.sym4_local_coefficients_closed(1, q)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.su2_sym4_haar_trace_moments(9)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.so5_standard_haar_trace_moments(9)
        with self.assertRaisesRegex(ValueError, "nonnegative even"):
            subject.normalized_stack_character_mean(3, 5)
        guard = subject.ResourceGuard()
        with self.assertRaisesRegex(RuntimeError, "cap 5000"):
            guard.charge("deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE)


if __name__ == "__main__":
    unittest.main()

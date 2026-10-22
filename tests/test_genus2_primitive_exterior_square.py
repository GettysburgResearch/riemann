"""Replay tests for the primitive exterior-square L-family packet."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_primitive_exterior_square as subject  # noqa: E402


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def independent_so5_weyl_moments(maximum: int) -> list[int]:
    """A deliberately separate tiny Laurent-polynomial B2 constant term."""

    def product(
        left: dict[tuple[int, int], int],
        right: dict[tuple[int, int], int],
    ) -> dict[tuple[int, int], int]:
        output: Counter[tuple[int, int]] = Counter()
        for (left_x, left_y), left_value in left.items():
            for (right_x, right_y), right_value in right.items():
                output[(left_x + right_x, left_y + right_y)] += (
                    left_value * right_value
                )
        return {key: value for key, value in output.items() if value}

    denominator = {(0, 0): 1}
    for root in ((1, -1), (0, 1), (1, 0), (1, 1)):
        denominator = product(
            denominator,
            {(0, 0): 2, root: -1, (-root[0], -root[1]): -1},
        )
    character = {(0, 0): 1, (1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1}
    power = {(0, 0): 1}
    moments = []
    for order in range(maximum + 1):
        numerator = sum(
            coefficient
            * denominator.get((-exponent[0], -exponent[1]), 0)
            for exponent, coefficient in power.items()
        )
        moments.append(numerator // 8)
        if order != maximum:
            power = product(power, character)
    return moments


class Genus2PrimitiveExteriorSquareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["frozen_histogram_transforms"]
        }

    def test_two_derivations_and_both_exact_divisions_on_every_source_atom(self) -> None:
        balanced = json.loads(subject.BALANCED_FIXTURE_PATH.read_text(encoding="utf-8"))
        operations = 0
        for family in balanced["frozen_enumeration_facts"]["families"]:
            q = int(family["q"])
            for atom in family["joint_a_D_b_D_law"]["atoms"]:
                a = int(atom["a_D"])
                b = int(atom["b_D"])
                full_closed = subject.exterior_square_coefficients_closed(a, b, q)
                full_newton = subject.exterior_square_coefficients_via_newton(a, b, q)
                primitive_closed = subject.primitive_exterior_square_coefficients_closed(
                    a, b, q
                )
                primitive_newton = subject.primitive_exterior_square_coefficients_via_newton(
                    a, b, q
                )
                local_quartic = subject.moving_local_eigenline_quotient_closed(a, b, q)
                self.assertEqual(full_closed, full_newton)
                self.assertEqual(primitive_closed, primitive_newton)
                self.assertEqual(full_closed, multiply((1, -q), primitive_closed))
                self.assertEqual(primitive_closed, multiply((1, -q), local_quartic))
                self.assertEqual(
                    local_quartic,
                    subject.moving_local_eigenline_quotient(a, b, q),
                )

                # Normalized character form R(z/q)=1-sz+kz^2-kz^3+sz^4-z^5.
                s_numerator = b - q
                k_numerator = a * a - b
                self.assertEqual(primitive_closed[1], -s_numerator)
                self.assertEqual(primitive_closed[2], q * k_numerator)
                self.assertEqual(primitive_closed[3], -q**2 * k_numerator)
                self.assertEqual(primitive_closed[4], q**3 * s_numerator)
                self.assertEqual(primitive_closed[5], -q**5)
                operations += 1
        self.assertEqual(operations, 251)

    def test_closed_form_is_algebraic_beyond_the_frozen_weil_atoms(self) -> None:
        for q in (3, 5, 7, 9, 11, 25):
            for a, b in ((0, 0), (1, -2), (-3, 4), (5, 13)):
                with self.subTest(q=q, a=a, b=b):
                    full = subject.exterior_square_coefficients_closed(a, b, q)
                    self.assertEqual(
                        full,
                        subject.exterior_square_coefficients_via_newton(a, b, q),
                    )
                    primitive = subject.primitive_exterior_square_coefficients_closed(
                        a, b, q
                    )
                    quartic = subject.moving_local_eigenline_quotient_closed(a, b, q)
                    self.assertEqual(full, multiply((1, -q, ), primitive))
                    self.assertEqual(primitive, multiply((1, -q), quartic))

    def test_exact_all_q_character_moment_formulas(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            actual = subject.all_q_primitive_character_moments(q)
            expected = {
                "mean_s": -Fraction(1, q) + Fraction(1, q**2) - Fraction(1, q**4),
                "mean_s_squared": Fraction(1)
                - Fraction(1, q)
                + Fraction(1, q**3)
                - Fraction(1, q**4)
                - Fraction(1, q**5),
                "mean_k": Fraction(1, q**3) - Fraction(1, q**4),
                "mean_k_squared": Fraction(1)
                - Fraction(2, q)
                + Fraction(1, q**2)
                + Fraction(3, q**3)
                - Fraction(3, q**4)
                - Fraction(6, q**5),
                "mean_s_times_k": -Fraction(1, q)
                + Fraction(1, q**2)
                + Fraction(3, q**3)
                - Fraction(3, q**4)
                - Fraction(2, q**5),
            }
            self.assertEqual(actual, expected)

            # Re-derive from the five unnormalized source moments rather than
            # trusting the simplified displayed formulas.
            inputs = subject.all_q_input_moments(q)
            self.assertEqual(actual["mean_s"], inputs["b"] / q - 1)
            self.assertEqual(
                actual["mean_s_squared"],
                inputs["b2"] / q**2 - 2 * inputs["b"] / q + 1,
            )
            self.assertEqual(
                actual["mean_k"], (inputs["a2"] - inputs["b"]) / q
            )
            self.assertEqual(
                actual["mean_k_squared"],
                (inputs["a4"] - 2 * inputs["a2b"] + inputs["b2"]) / q**2,
            )
            self.assertEqual(
                actual["mean_s_times_k"],
                (inputs["a2b"] - inputs["b2"]) / q**2
                - (inputs["a2"] - inputs["b"]) / q,
            )

    def test_so5_weyl_baseline_and_orientation_moment(self) -> None:
        expected = [1, 0, 1, 0, 3, 1, 15]
        self.assertEqual(subject.so5_standard_haar_trace_moments(), expected)
        self.assertEqual(independent_so5_weyl_moments(6), expected)
        baseline = self.fixture["compact_SO5_baseline"]
        self.assertEqual(baseline["standard_trace_moments"], expected)
        self.assertEqual(
            baseline["orientation_fingerprint"],
            {
                "order": 5,
                "SO5_moment": 1,
                "O5_moment": 0,
                "reason": "the SO(5) volume tensor is the first odd invariant; adjoining a reflection kills odd trace moments",
            },
        )
        sign_reversal = baseline["frozen_fifth_moment_sign_reversal"]
        expected_frozen = {
            3: Fraction(-8059, 6561),
            5: Fraction(-541001, 390625),
            7: Fraction(-5982775, 5764801),
        }
        self.assertEqual(
            {
                row["q"]: Fraction(*row["family_mean_s_fifth"])
                for row in sign_reversal["rows"]
            },
            expected_frozen,
        )
        self.assertTrue(all(value < 0 for value in expected_frozen.values()))
        self.assertIn("no all-q", sign_reversal["status"])

    def test_frozen_pushforwards_are_complete_and_match_all_q_moments(self) -> None:
        expected_source = {3: (32, 162), 5: (81, 2500), 7: (138, 14406)}
        for q, row in self.by_q.items():
            source_atoms, members = expected_source[q]
            self.assertEqual(row["source_joint_atom_count"], source_atoms)
            self.assertEqual(row["member_count"], members)
            law = row["complete_primitive_coefficient_law"]
            self.assertEqual(
                sum(atom["member_count"] for atom in law["atoms"]), members
            )
            trace_law = row["normalized_trace_law"]
            self.assertEqual(
                sum(atom["member_count"] for atom in trace_law["atoms"]), members
            )
            moments = trace_law["moments_0_through_8"]
            self.assertEqual(len(moments), 9)
            exact = subject.all_q_primitive_character_moments(q)
            self.assertEqual(Fraction(*moments[1]["family_mean_s_power"]), exact["mean_s"])
            self.assertEqual(
                Fraction(*moments[2]["family_mean_s_power"]),
                exact["mean_s_squared"],
            )
            self.assertTrue(all(moments[index]["all_q_formula_checked"] for index in range(3)))
            regression = row["all_q_character_moment_regression"]
            for name, value in exact.items():
                self.assertEqual(Fraction(*regression[name]), value)

    def test_center_kernel_and_local_global_firewall(self) -> None:
        for row in self.by_q.values():
            check = row["twist_kernel_check"]
            self.assertTrue(check["signed_histogram_invariant_under_a_to_minus_a"])
            self.assertTrue(check["primitive_polynomial_depends_only_on_a_squared_and_b"])
            self.assertLessEqual(
                check["twist_quotient_support_size"], check["source_signed_support_size"]
            )
            for witness in row["newton_and_division_witnesses"]:
                a, b = witness["input_a_b"]
                q = int(row["q"])
                self.assertEqual(
                    subject.primitive_exterior_square_coefficients_closed(a, b, q),
                    subject.primitive_exterior_square_coefficients_closed(-a, b, q),
                )
        gap = self.fixture["pointwise_local_eigenline_without_forced_common_line"]
        self.assertIn("irreducible", gap["ambient_representation_level"])
        self.assertIn("not determined", gap["actual_family_level"])
        self.assertIn("procyclic", gap["individual_finite_field_fiber_level"])
        self.assertIn("anti-diagonal", gap["endoscopic_specialization"])
        self.assertIn(
            "varies",
            gap["why_not_a_forced_common_Tate_subrepresentation"],
        )
        self.assertIn("do not define", gap["noncanonical_tensor_warning"])
        self.assertIn("remains formal", gap["formal_Euler_product_warning"])
        firewall = self.fixture["scope_firewall"]
        self.assertIn(
            "actual family monodromy",
            firewall["no_forced_second_common_Tate_line"],
        )
        self.assertIn("does not prove", firewall["no_full_monodromy_claim"])
        self.assertIn("RH", firewall["no_analytic_or_RH_claim"])
        literature = self.fixture["literature_boundary"]
        self.assertIn("classical", literature["classical_context"])
        self.assertIn("1201.2783", literature["primary_reference"])
        self.assertIn("exact pushforward", literature["project_specific_contribution"])

    def test_fixture_hashes_sources_and_resource_contract(self) -> None:
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
            locks["balanced_fixture"]["payload_sha256"],
            subject.EXPECTED_BALANCED_PAYLOAD_SHA256,
        )
        self.assertEqual(
            locks["genus2_formula_fixture"]["payload_sha256"],
            subject.EXPECTED_GENUS2_FORMULA_PAYLOAD_SHA256,
        )
        resources = stored["resource_contract"]
        self.assertLess(
            resources["accounted_work_unit_ledger"][
                "total_accounted_work_units"
            ],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertIn("not literal", resources["unit_definition"])
        self.assertEqual(resources["field_or_curve_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)

    def test_refusals(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5))
        for q in (2, 4, 8, 15, 21):
            with self.subTest(q=q):
                with self.assertRaisesRegex(ValueError, "odd prime power"):
                    subject.exterior_square_coefficients_closed(1, 2, q)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.so5_standard_haar_trace_moments(7)
        guard = subject.ResourceGuard()
        with self.assertRaisesRegex(RuntimeError, "cap 10000"):
            guard.charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()

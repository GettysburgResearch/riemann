"""Independent lightweight checks for the frozen genus-two tail geometry."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_tail_geometry as subject  # noqa: E402


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def multiply_low(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    product = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            product[i + j] += left_value * right_value
    return product


def remainder_mod_2(dividend_low: list[int], divisor_low: list[int]) -> list[int]:
    remainder = [value % 2 for value in dividend_low]
    while len(remainder) >= len(divisor_low):
        if remainder[-1]:
            shift = len(remainder) - len(divisor_low)
            for index, value in enumerate(divisor_low):
                remainder[index + shift] ^= value % 2
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return remainder


class AllQAlgebraTests(unittest.TestCase):
    def test_discriminant_edge_and_endpoint_identities_on_independent_grid(self) -> None:
        for q in range(1, 12):
            for a in range(-10, 11):
                for b in range(-2 * q, 6 * q + 1):
                    delta = a * a - 4 * b + 8 * q
                    gamma = (b + 2 * q) ** 2 - 4 * q * a * a
                    k_value = q * a * a - b * b
                    self.assertEqual(
                        subject.quartic_discriminant(a, b, q),
                        q * q * delta * delta * gamma,
                    )
                    self.assertEqual(gamma, (6 * q - b) ** 2 - 4 * q * delta)
                    self.assertEqual(
                        20 * q * q + k_value,
                        q * delta + (6 * q - b) * (2 * q + b),
                    )

    def test_square_defect_and_integral_repeated_angle_ladder(self) -> None:
        for q in range(1, 12):
            for a in range(-8, 9):
                for b in range(-2 * q, 6 * q + 1):
                    delta = a * a - 4 * b + 8 * q
                    square = multiply_low(
                        [Fraction(q), Fraction(a, 2), Fraction(1)],
                        [Fraction(q), Fraction(a, 2), Fraction(1)],
                    )
                    square[2] -= Fraction(delta, 4)
                    self.assertEqual(
                        square,
                        [Fraction(q * q), Fraction(q * a), Fraction(b), Fraction(a), Fraction(1)],
                    )
                    if delta == 0:
                        self.assertEqual(a % 2, 0)
                        r = a // 2
                        self.assertEqual(b, 2 * q + r * r)
                        self.assertEqual(q * a * a - b * b, -4 * q * q - r**4)

    def test_admissible_range_and_far_negative_concentration(self) -> None:
        equality_witnesses: list[tuple[int, int, int]] = []
        for q in range(1, 24):
            for abs_a in range(isqrt(16 * q) + 1):
                for b in range(-2 * q, 6 * q + 1):
                    if not subject.is_usp4_trace_admissible(q, abs_a, b):
                        continue
                    row = subject.tail_invariants(q, abs_a, b)
                    self.assertGreaterEqual(row["K"], -20 * q * q)
                    if row["K"] == -20 * q * q:
                        equality_witnesses.append((q, abs_a, b))
                        self.assertEqual(row["Delta"], 0)
                        self.assertEqual(b, 6 * q)
                        self.assertEqual(abs_a * abs_a, 16 * q)
                    if row["K"] < -4 * q * q:
                        self.assertGreater(b, 2 * q)
                        edge = row["haar_edge_defect_E"]
                        self.assertLessEqual(q * row["Delta"], edge)
                        self.assertLessEqual(4 * q * (6 * q - b), edge)
        self.assertTrue(equality_witnesses)


class FrozenReconstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(subject.FIXTURE.read_text(encoding="utf-8"))
        cls.by_q = {row["q"]: row for row in cls.fixture["families"]}

    def test_exact_fixture_replay_payload_and_source_locks(self) -> None:
        self.assertEqual(subject.build_fixture(), self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, canonical_sha256(unhashed))
        producer = self.fixture["producer"]
        self.assertEqual(
            producer["source_sha256_lf_normalized"],
            lf_sha256(FUNCTION_FIELD / "genus2_tail_geometry.py"),
        )
        q_scan = json.loads(subject.Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
        affine = json.loads(subject.AFFINE_FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(producer["q_scan_fixture_canonical_sha256"], canonical_sha256(q_scan))
        self.assertEqual(producer["affine_fixture_canonical_sha256"], canonical_sha256(affine))

    def test_minimum_pairs_orbits_and_shape_trichotomy(self) -> None:
        expected = {
            3: (-24, 2, 6, 4, 1, 6, "SPLIT_NONISOTYPIC"),
            5: (-116, 4, 14, 0, 2, 10, "SPLIT_ISOTYPIC"),
            7: (-282, 7, 25, 5, 1, 42, "FQ_SIMPLE"),
        }
        for q, row in self.by_q.items():
            tail = row["minimum_tail_atom"]
            pair = tail["unique_admissible_pair_up_to_a_sign"]
            orbit = tail["orbit_certificate"]
            k_value, abs_a, b, delta, stabilizer, size, shape = expected[q]
            self.assertEqual(
                (tail["K"], pair["abs_a"], pair["b"], pair["Delta"]),
                (k_value, abs_a, b, delta),
            )
            self.assertEqual((orbit["orbit_count"], orbit["stabilizer_order"], orbit["orbit_size"]), (1, stabilizer, size))
            self.assertEqual(tail["frobenius_geometry"]["shape"], shape)
        self.assertEqual(
            self.by_q[3]["minimum_tail_atom"]["frobenius_geometry"]["elliptic_trace_factors"],
            [0, 2],
        )
        self.assertEqual(
            self.by_q[5]["minimum_tail_atom"]["frobenius_geometry"]["elliptic_trace_factors"],
            [2, 2],
        )
        q7_geometry = self.by_q[7]["minimum_tail_atom"]["frobenius_geometry"]
        self.assertEqual(q7_geometry["real_trace_field"], "Q(sqrt(5))")
        self.assertEqual(q7_geometry["mod_2_irreducibility_certificate"]["remainder_mod_T2_plus_T_plus_1"], "T+1")
        phi_5_low = [1, 1, 1, 1, 1]
        self.assertEqual(sum(phi_5_low) % 2, 1)
        self.assertEqual(remainder_mod_2(phi_5_low, [1, 1, 1]), [1, 1])

    def test_lattice_exclusions_and_repeated_angle_support(self) -> None:
        expected_lattice = {
            3: (38, -117, 6, 15),
            5: (75, -356, 8, 26),
            7: (118, -821, 10, 39),
        }
        expected_positive_rungs = {3: [], 5: [(2, -116, 10)], 7: [(2, -212, 42)]}
        for q, row in self.by_q.items():
            lattice = row["usp4_admissible_integer_coefficient_lattice"]
            count, k_value, abs_a, b = expected_lattice[q]
            self.assertEqual(lattice["abs_a_sign_quotiented_pair_count"], count)
            self.assertEqual(lattice["minimum_K"], k_value)
            self.assertEqual(
                (lattice["minimum_pair"]["abs_a"], lattice["minimum_pair"]["b"], lattice["minimum_pair"]["Delta"]),
                (abs_a, b, 0),
            )
            self.assertTrue(lattice["absent_from_frozen_family_support"])
            realized = [
                (item["r"], item["K"], item["member_count_at_K"])
                for item in row["realized_positive_repeated_angle_rungs"]
            ]
            self.assertEqual(realized, expected_positive_rungs[q])

    def test_extreme_atom_first_dominates_at_order_ten(self) -> None:
        expected_twelfth = {
            3: Fraction(4565043429507072, 7816952346147025),
            5: Fraction(371001690114457905135616, 598826630780182957326013),
            7: Fraction(585471222280559325572506368, 797570369691811117670825621),
        }
        for q, row in self.by_q.items():
            tail = row["minimum_tail_atom"]
            self.assertEqual(
                tail["first_even_moment_order_with_more_than_half_of_absolute_moment"],
                10,
            )
            shares = tail["absolute_moment_shares"]
            self.assertLess(Fraction(shares["8"]["numerator"], shares["8"]["denominator"]), Fraction(1, 2))
            self.assertGreater(Fraction(shares["10"]["numerator"], shares["10"]["denominator"]), Fraction(1, 2))
            twelfth = Fraction(shares["12"]["numerator"], shares["12"]["denominator"])
            self.assertEqual(twelfth, expected_twelfth[q])
        q7_repeated = self.by_q[7]["realized_positive_repeated_angle_rungs"][0]
        repeated_share = q7_repeated["absolute_moment_12_share"]
        self.assertEqual(
            Fraction(repeated_share["numerator"], repeated_share["denominator"]),
            Fraction(515122296789900884328841216, 21534399981678900177112291767),
        )
        self.assertLess(Fraction(repeated_share["numerator"], repeated_share["denominator"]), Fraction(1, 40))

    def test_minimum_orbit_measure_distortion_is_the_only_coarse_claim(self) -> None:
        expected_ratios = {3: Fraction(27, 29), 5: Fraction(125, 66), 7: Fraction(343, 349)}
        for q, row in self.by_q.items():
            ratio = row["minimum_tail_atom"]["coarse_to_member_mass_ratio"]
            self.assertEqual(Fraction(ratio["numerator"], ratio["denominator"]), expected_ratios[q])
        ledger = self.fixture["non_identifiability_ledger"]
        self.assertIn("not recoverable", ledger["uniform_orbit_K_or_H_mean"])
        self.assertIn("do not rerun", ledger["action_taken"])


class Q5QuotientGeometryTests(unittest.TestCase):
    def test_both_elliptic_quotient_identities_are_symbolically_zero(self) -> None:
        self.assertEqual(subject.q5_quotient_identity_residual(1), {})
        self.assertEqual(subject.q5_quotient_identity_residual(-1), {})
        with self.assertRaisesRegex(ValueError, "sign"):
            subject.q5_quotient_identity_residual(0)

    def test_special_curve_and_marked_stack_firewall(self) -> None:
        fixture = json.loads(subject.FIXTURE.read_text(encoding="utf-8"))
        geometry = fixture["q5_special_curve_geometry"]
        self.assertEqual(geometry["curve"], "y^2=x^5+x^3+x over F_5")
        self.assertEqual(geometry["odd_affine_symmetry"]["order"], 4)
        self.assertEqual(geometry["reciprocal_involution"]["order"], 2)
        self.assertIn("not in AGL", geometry["reciprocal_involution"]["scope_note"])
        self.assertIn("not the full", geometry["measure_warning"])
        self.assertEqual(len({1 % 5, -1 % 5, -2 % 5}), 3)
        self.assertEqual(len({1 % 5, -1 % 5, 2 % 5}), 3)


class ResourceAndScopeTests(unittest.TestCase):
    def test_frozen_inputs_caps_and_no_field_enumerator_dependency(self) -> None:
        self.assertEqual(subject.FROZEN_Q_VALUES, (3, 5, 7))
        self.assertLessEqual(subject.MAX_LATTICE_CANDIDATES_PER_Q, 1_000)
        with self.assertRaisesRegex(ValueError, "frozen"):
            subject.admissible_coefficient_lattice(11)
        source = (FUNCTION_FIELD / "genus2_tail_geometry.py").read_text(encoding="utf-8")
        self.assertNotIn("import genus2_q_scan", source)
        self.assertNotIn("build_field_tables", source)
        self.assertNotIn("coefficients_from_character_sums", source)
        self.assertNotIn("itertools.product", source)

    def test_scope_firewalls_distinguish_all_q_algebra_from_three_field_facts(self) -> None:
        fixture = json.loads(subject.FIXTURE.read_text(encoding="utf-8"))
        self.assertIn("EVERY_POSITIVE_INTEGER_Q", fixture["exact_symbolic_identities"]["status"])
        self.assertEqual(fixture["minimum_shape_trichotomy"]["status"], "EXACT_FOR_Q_3_5_7_ONLY")
        firewall = fixture["firewall"]
        for phrase in (
            "three-field fact only",
            "need not be realized",
            "No asymptotic tail law",
            "number-field transfer",
        ):
            self.assertIn(phrase, firewall)


if __name__ == "__main__":
    unittest.main()

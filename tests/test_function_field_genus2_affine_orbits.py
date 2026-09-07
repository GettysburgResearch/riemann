"""Focused independent checks for the exact genus-two affine-orbit packet."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_affine_orbits as subject  # noqa: E402
import genus2_q_scan as q_scan  # noqa: E402


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def lf_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class AffineActionTests(unittest.TestCase):
    def test_right_action_law_identity_and_inverses(self) -> None:
        conductor = (0, 1, 0, 0, 1, 1)
        for q in subject.FROZEN_Q_VALUES:
            elements = subject.affine_elements(q)
            self.assertEqual(len(elements), q * (q - 1))
            self.assertEqual(
                subject.affine_transform(conductor, q, 1, 0), conductor
            )
            for element in elements:
                inverse = subject.inverse_affine(element, q)
                self.assertEqual(subject.compose_affine(element, inverse, q), (1, 0))
                self.assertEqual(subject.compose_affine(inverse, element, q), (1, 0))
            for left in elements:
                once = subject.affine_transform(conductor, q, *left)
                for right in elements:
                    twice = subject.affine_transform(once, q, *right)
                    composed = subject.compose_affine(left, right, q)
                    self.assertEqual(
                        twice,
                        subject.affine_transform(conductor, q, *composed),
                    )

    def test_character_sum_transformation_law_directly(self) -> None:
        conductor = (0, 1, 0, 0, 1, 1)
        for q in subject.FROZEN_Q_VALUES:
            tables = q_scan.build_field_tables(q)
            self.assertTrue(q_scan.is_squarefree_quintic(conductor, q))
            a_d, b_d = q_scan.coefficients_from_character_sums(conductor, tables)
            self.assertNotEqual(a_d, 0)
            k_d = q * a_d * a_d - b_d * b_d
            for alpha, beta in subject.affine_elements(q):
                transformed = subject.affine_transform(
                    conductor, q, alpha, beta
                )
                self.assertEqual(transformed[-1], 1)
                self.assertTrue(q_scan.is_squarefree_quintic(transformed, q))
                transformed_a, transformed_b = q_scan.coefficients_from_character_sums(
                    transformed, tables
                )
                self.assertEqual(
                    transformed_a,
                    tables.base_character[alpha] * a_d,
                )
                self.assertEqual(transformed_b, b_d)
                self.assertEqual(
                    q * transformed_a * transformed_a - transformed_b * transformed_b,
                    k_d,
                )
            nonsquare = tables.nonsquare
            nonsquare_transform = subject.affine_transform(
                conductor, q, nonsquare, 0
            )
            transformed_a, _transformed_b = q_scan.coefficients_from_character_sums(
                nonsquare_transform, tables
            )
            self.assertEqual(transformed_a, -a_d)

    def test_hostile_action_inputs_are_refused(self) -> None:
        conductor = (0, 1, 0, 0, 1, 1)
        with self.assertRaisesRegex(ValueError, "monic quintic"):
            subject.affine_transform(conductor[:-1], 3, 1, 0)
        with self.assertRaisesRegex(ValueError, "alpha must be nonzero"):
            subject.affine_transform(conductor, 3, 0, 0)
        with self.assertRaisesRegex(ValueError, "residue"):
            subject.affine_transform(conductor, 3, 1, 3)


class FrozenOrbitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {row["q"]: row for row in cls.fixture["families"]}

    def test_exact_orbit_and_stabilizer_histograms(self) -> None:
        expected = {
            3: {
                "members": 162,
                "edges": 972,
                "orbits": 29,
                "orbit_sizes": {"3": 4, "6": 25},
                "stabilizers": {"1": 25, "2": 4},
                "a_zero": {"members": 30, "orbits": 7},
            },
            5: {
                "members": 2500,
                "edges": 50000,
                "orbits": 132,
                "orbit_sizes": {"1": 1, "4": 1, "5": 3, "10": 6, "20": 121},
                "stabilizers": {"1": 121, "2": 6, "4": 3, "5": 1, "20": 1},
                "a_zero": {"members": 406, "orbits": 24},
            },
            7: {
                "members": 14406,
                "edges": 605052,
                "orbits": 349,
                "orbit_sizes": {"21": 12, "42": 337},
                "stabilizers": {"1": 337, "2": 12},
                "a_zero": {"members": 2184, "orbits": 58},
            },
        }
        for q, control in expected.items():
            family = self.by_q[q]
            partition = family["orbit_partition"]
            self.assertEqual(family["member_count"], control["members"])
            self.assertEqual(family["group"]["order"], q * (q - 1))
            self.assertEqual(
                family["action_checks"]["member_action_pairs_checked"],
                control["edges"],
            )
            self.assertEqual(
                family["action_checks"]["expected_member_action_pairs"],
                control["edges"],
            )
            self.assertEqual(partition["orbit_count"], control["orbits"])
            self.assertEqual(partition["orbit_size_histogram"], control["orbit_sizes"])
            self.assertEqual(
                partition["stabilizer_order_histogram"], control["stabilizers"]
            )
            self.assertEqual(
                sum(int(size) * count for size, count in control["orbit_sizes"].items()),
                control["members"],
            )
            self.assertEqual(
                family["a_D_zero_partition"]["zero_member_count"],
                control["a_zero"]["members"],
            )
            self.assertEqual(
                family["a_D_zero_partition"]["zero_orbit_count"],
                control["a_zero"]["orbits"],
            )

    def test_exact_sign_summaries_are_orbit_invariant(self) -> None:
        expected = {
            3: {
                "negative": (19, 102, {"3": 4, "6": 15}),
                "zero": (2, 12, {"6": 2}),
                "positive": (8, 48, {"6": 8}),
            },
            5: {
                "negative": (86, 1650, {"1": 1, "4": 1, "5": 1, "10": 2, "20": 81}),
                "zero": (4, 50, {"5": 2, "20": 2}),
                "positive": (42, 800, {"10": 4, "20": 38}),
            },
            7: {
                "negative": (237, 9702, {"21": 12, "42": 225}),
                "zero": (8, 336, {"42": 8}),
                "positive": (104, 4368, {"42": 104}),
            },
        }
        for q, controls in expected.items():
            family = self.by_q[q]
            for sign, (orbit_count, member_count, size_histogram) in controls.items():
                row = family["sign_summaries"][sign]
                self.assertEqual(row["orbit_count"], orbit_count)
                self.assertEqual(row["member_count"], member_count)
                self.assertEqual(row["orbit_size_histogram"], size_histogram)
            self.assertEqual(
                family["member_sign_counts"],
                {sign: values[1] for sign, values in controls.items()},
            )
            self.assertEqual(
                sum(row["orbit_count"] for row in family["sign_summaries"].values()),
                family["orbit_partition"]["orbit_count"],
            )

    def test_characteristic_five_full_stabilizer_is_exact(self) -> None:
        family = self.by_q[5]
        witness = family["nontrivial_stabilizer_witnesses"]["20"]
        conductor = tuple(witness["representative_coefficients_low_to_high"])
        self.assertEqual(conductor, (0, 4, 0, 0, 0, 1))
        self.assertEqual(witness["orbit_size"], 1)
        self.assertEqual(witness["stabilizer_order"], 20)
        self.assertEqual(witness["K_D"], -100)
        self.assertEqual(
            [tuple(element) for element in witness["stabilizer_elements_alpha_beta"]],
            list(subject.affine_elements(5)),
        )
        for element in subject.affine_elements(5):
            self.assertEqual(
                subject.affine_transform(conductor, 5, *element),
                conductor,
            )

    def test_most_negative_tail_is_one_exact_affine_orbit(self) -> None:
        q_scan_fixture = json.loads(subject.Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
        families = {row["q"]: row for row in q_scan_fixture["families"]}
        controls = {
            3: ((0, 1, 1, 1, 1, 1), (-2, 6), -24, 6, 1, (4, 3)),
            5: ((0, 1, 0, 1, 0, 1), (-4, 14), -116, 10, 2, (0, 5)),
            7: ((3, 0, 3, 6, 4, 1), (-7, 25), -282, 42, 1, (5, 7)),
        }
        for q, control in controls.items():
            conductor, coefficients, minimum_k, orbit_size, stabilizer, discriminant = control
            tables = q_scan.build_field_tables(q)
            self.assertEqual(
                q_scan.coefficients_from_character_sums(conductor, tables),
                coefficients,
            )
            self.assertEqual(q * coefficients[0] ** 2 - coefficients[1] ** 2, minimum_k)
            self.assertEqual(
                (coefficients[0] ** 2 - 4 * coefficients[1] + 8 * q, q),
                discriminant,
            )
            orbit = {
                subject.affine_transform(conductor, q, *element)
                for element in subject.affine_elements(q)
            }
            self.assertEqual(len(orbit), orbit_size)
            self.assertEqual(q * (q - 1) // len(orbit), stabilizer)
            histogram = families[q]["K_histogram"]
            self.assertEqual(min(map(int, histogram)), minimum_k)
            self.assertEqual(histogram[str(minimum_k)], orbit_size)

    def test_q_scan_moments_histograms_and_signs_are_replayed(self) -> None:
        self.assertTrue(
            all(
                all(checks.values())
                for checks in self.fixture["q_scan_regression_controls"].values()
            )
        )
        q_scan_fixture = json.loads(subject.Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            self.fixture["producer"]["shared_q_scan_fixture_canonical_sha256"],
            canonical_sha256(q_scan_fixture),
        )
        expected_by_q = {row["q"]: row for row in q_scan_fixture["families"]}
        for q, family in self.by_q.items():
            expected = expected_by_q[q]
            self.assertEqual(family["member_sign_counts"], expected["sign_counts"])
            self.assertEqual(
                family["moment_sums"],
                {
                    "a_D_squared": expected["moments"]["a_squared"]["sum"],
                    "b_D_squared": expected["moments"]["b_squared"]["sum"],
                    "K_D": expected["moments"]["K"]["sum"],
                },
            )

    def test_source_locks_payload_hash_and_scope_firewall(self) -> None:
        producer = self.fixture["producer"]
        self.assertEqual(
            producer["source_sha256_lf_normalized"],
            lf_sha256(FUNCTION_FIELD / "genus2_affine_orbits.py"),
        )
        self.assertEqual(
            producer["shared_q_scan_source_sha256_lf_normalized"],
            lf_sha256(FUNCTION_FIELD / "genus2_q_scan.py"),
        )
        without_hash = copy.deepcopy(self.fixture)
        payload_hash = without_hash.pop("payload_sha256")
        self.assertEqual(payload_hash, canonical_sha256(without_hash))
        self.assertIn("not a Pick/Loewner", self.fixture["firewall"])
        encoded = json.dumps(self.fixture, sort_keys=True).lower()
        self.assertNotIn("runtime_seconds", encoded)
        self.assertNotIn("elapsed_seconds", encoded)
        self.assertIn("numerical root finding", encoded)
        self.assertIn("per-member euler coefficient enumeration", encoded)

    def test_all_odd_trace_cancellation_corollary_is_explicit(self) -> None:
        corollary = self.fixture["odd_trace_cancellation_corollary"]
        self.assertEqual(
            corollary["status"], "PROVED_FOR_EVERY_ODD_PRIME_POWER"
        )
        self.assertIn("a_D^(2r+1)", corollary["statement"])
        self.assertIn("(a,b)->(-a,b)", corollary["special_cases"][1])
        self.assertIn("nonsquare alpha", corollary["proof"])
        self.assertIn("no equidistribution rate", corollary["scope_boundary"])

    def test_checked_in_fixture_is_exact_generator_output(self) -> None:
        stored = json.loads(subject.FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)


class ResourceGuardTests(unittest.TestCase):
    def test_other_fields_candidate_overflow_and_bad_fixture_scope_are_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "frozen affine-orbit certificate"):
            subject.analyze_q(11)
        with self.assertRaisesRegex(ValueError, "frozen affine-orbit certificate"):
            subject.analyze_q(2)
        with self.assertRaisesRegex(ValueError, "above candidate cap"):
            subject.analyze_q(7, candidate_cap=10_000)
        with self.assertRaisesRegex(ValueError, "wall limit"):
            subject.analyze_q(3, wall_limit_seconds=8.1)
        with self.assertRaisesRegex(ValueError, "requires exactly"):
            subject.build_fixture(q_values=(3, 5))

    def test_monotonic_global_wall_guard_aborts(self) -> None:
        class AdvancingClock:
            def __init__(self) -> None:
                self.calls = 0

            def __call__(self) -> float:
                self.calls += 1
                return 0.0 if self.calls == 1 else 8.0

        with self.assertRaisesRegex(TimeoutError, "monotonic wall deadline"):
            subject.analyze_q(
                3,
                wall_limit_seconds=8.0,
                guard_interval=1,
                clock=AdvancingClock(),
            )


if __name__ == "__main__":
    unittest.main()

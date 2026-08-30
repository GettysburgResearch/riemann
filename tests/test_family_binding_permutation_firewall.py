"""Hostile exact controls for the label-forgetting structural firewall."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "research/riemann-structures/family_binding_permutation_firewall.py"
SPEC = importlib.util.spec_from_file_location(
    "family_binding_permutation_firewall", SCRIPT
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load the family-binding producer")
packet = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packet)


class FamilyBindingFirewallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = packet.build_report()

    def test_fixture_is_exact_rebuild(self):
        self.assertEqual(
            json.loads(packet.FIXTURE.read_text(encoding="utf-8")), self.report
        )

    def test_general_scope_is_not_the_compute_cap(self):
        scope = self.report["theorem_scope"]
        self.assertIn("every integer N>=1", scope["family_size"])
        self.assertIn("first average alone", scope["mean_only_tax"])
        self.assertIn("higher moments", scope["stronger_data_escape"])
        self.assertIn("P=A-K=C-S", scope["signed_source_escape"])
        self.assertFalse(scope["actual_arithmetic_family_or_RH_estimate"])

    def test_opposite_principal_and_every_checked_moment(self):
        magnitude = Fraction(7, 3)
        for size in range(2, packet.MAX_N + 1):
            left = (magnitude, -magnitude) + (0,) * (size - 2)
            right = packet.counterfeit(left, 0)
            self.assertIsNotNone(right)
            self.assertEqual(right[0], -magnitude)
            self.assertEqual(sorted(left), sorted(right))
            for order in range(packet.MAX_ORDER + 1):
                expected = (
                    Fraction(1)
                    if order == 0
                    else (
                        2 * magnitude**order / size if order % 2 == 0 else Fraction(0)
                    )
                )
                self.assertEqual(packet.moment(left, order), expected)
                self.assertEqual(packet.moment(right, order), expected)

    def test_singleton_and_all_equal_are_identifiable(self):
        for values in ((-2,), (Fraction(5, 3),), (0, 0, 0), (2, 2, 2)):
            for index in range(len(values)):
                self.assertIsNone(packet.counterfeit(values, index))
        self.assertEqual(packet.moment((0,), 0), 1)
        self.assertEqual(packet.moment((-2,), 1), -2)

    def test_repeated_but_nonconstant_does_not_restore_recovery(self):
        values = (2, 2, -1, 2)
        for index in range(len(values)):
            other = packet.counterfeit(values, index)
            self.assertIsNotNone(other)
            self.assertNotEqual(other[index], values[index])
            self.assertEqual(sorted(other), sorted(values))

    def test_nonnegative_spike_sharp_for_every_size_including_one(self):
        magnitude = Fraction(13, 7)
        for size in range(1, packet.MAX_N + 1):
            values = (magnitude,) + (0,) * (size - 1)
            self.assertEqual(packet.nonnegative_bound(values, 0), magnitude)
            self.assertEqual(values[0] / packet.moment(values, 1), size)
            if size >= 2:
                self.assertEqual(packet.counterfeit(values, 0)[0], 0)

    def test_zero_mean_nonnegative_and_other_principal_labels(self):
        self.assertEqual(packet.nonnegative_bound((0, 0, 0), 1), 0)
        values = (1, 3, 2, 0)
        for index in range(len(values)):
            self.assertLessEqual(values[index], packet.nonnegative_bound(values, index))

    def test_signed_average_is_not_a_positive_envelope(self):
        values = (5, -5, 0)
        self.assertEqual(packet.moment(values, 1), 0)
        self.assertGreater(values[0], 0)
        with self.assertRaises(ValueError):
            packet.nonnegative_bound(values, 0)
        absolute_values = tuple(abs(value) for value in values)
        self.assertLessEqual(
            abs(values[0]), packet.nonnegative_bound(absolute_values, 0)
        )

    def test_stronger_moments_do_not_inherit_the_first_mean_tax(self):
        values = (3, 0, 0, 0)
        for order in range(1, packet.MAX_ORDER + 1):
            self.assertEqual(len(values) * packet.moment(values, order), 3**order)
        values = (Fraction(2, 3), 0, 1, 2)
        for order in range(1, packet.MAX_ORDER + 1):
            total = len(values) * packet.moment(values, order)
            self.assertLessEqual(max(values) ** order, total)
            self.assertLessEqual(total, len(values) * max(values) ** order)

    def test_exhaustive_census_counts(self):
        census = self.report["exhaustive_census"]
        self.assertEqual(census["tuple_count"], 120)
        self.assertEqual(census["marked_tuple_count"], 426)
        self.assertEqual(census["identifiable_marked_cases"], 30)
        self.assertEqual(census["nonnegative_marked_cases"], 98)
        self.assertTrue(census["all_distinct_permutations_enumerated"])

    def test_invalid_family_types_and_compute_caps(self):
        for values in (
            (),
            (0,) * 9,
            [1, 2],
            (True,),
            (1.0,),
            ("1",),
            (1 << 32,),
            (Fraction(1, 1 << 32),),
        ):
            with self.subTest(values=values), self.assertRaises(ValueError):
                packet.family(values)

    def test_invalid_principal_labels(self):
        for index in (-1, 2, True, 0.0):
            with self.subTest(index=index), self.assertRaises(ValueError):
                packet.counterfeit((1, 2), index)

    def test_invalid_permutations(self):
        for permutation in ((0, 0), (0,), (0, 2), (0, 1, 2), (False, 1), [0, 1]):
            with self.subTest(permutation=permutation), self.assertRaises(ValueError):
                packet.relabel((1, 2), permutation)
        self.assertEqual(packet.relabel((1, 2), (1, 0)), (2, 1))

    def test_invalid_moment_orders(self):
        for order in (-1, 13, True, 1.0):
            with self.subTest(order=order), self.assertRaises(ValueError):
                packet.moment((1, 2), order)

    def test_mutated_result_or_scope_is_rejected(self):
        changed = copy.deepcopy(self.report)
        changed["signed_opposite_pairs"][0]["selected_values"][1] = "3/2"
        with self.assertRaises(ValueError):
            packet.validate_report(changed)
        changed = copy.deepcopy(self.report)
        changed["theorem_scope"]["actual_arithmetic_family_or_RH_estimate"] = True
        with self.assertRaises(ValueError):
            packet.validate_report(changed)
        changed = copy.deepcopy(self.report)
        changed["theorem_scope"]["actual_arithmetic_family_or_RH_estimate"] = 0
        with self.assertRaises(ValueError):
            packet.validate_report(changed)

    def test_missing_or_mutated_source_contract_is_rejected(self):
        with (
            mock.patch.object(packet, "expected_manifest", return_value={}),
            self.assertRaises(ValueError),
        ):
            packet.authenticate_sources()
        with (
            mock.patch.object(packet, "git_bytes", return_value=b"wrong blob\n"),
            self.assertRaisesRegex(ValueError, "Git blob mismatch"),
        ):
            packet.authenticate_sources()
        source = packet.SOURCES[0]
        with (
            mock.patch.object(
                packet,
                "git_bytes",
                side_effect=[source["git_blob"].encode() + b"\n", b"wrong content"],
            ),
            self.assertRaisesRegex(ValueError, "content hash mismatch"),
        ):
            packet.authenticate_sources()

    def test_checks_survive_optimization(self):
        packet.check_packet_contract()


if __name__ == "__main__":
    unittest.main()

"""Strict exact controls; global mathematics is reviewed from the note."""

from __future__ import annotations

import copy
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "research" / "exploratory")
)
import xi_four_node_far_zero_reserve as p


class FarReserveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = p.build()

    def reseal(self, value):
        value["payload_sha256"] = p.sha(
            p.canonical({k: v for k, v in value.items() if k != "payload_sha256"})
        )
        return value

    def test_01_frozen_fixture_fresh(self):
        self.assertTrue(p.validate(p.load(p.FIXTURE)))

    def test_02_complete_dispersion_coverage(self):
        self.assertEqual(
            len(self.value["dispersion"]), len(p.POLE_MODELS) * len(p.TS) * 2
        )

    def test_03_all_dispersion_real(self):
        for row in self.value["dispersion"]:
            self.assertIsInstance(p.unpack(row["value"]), Q)

    def test_04_atom_coverage(self):
        self.assertEqual(
            len(self.value["atom_controls"]), len(p.ATOM_MODELS) * len(p.QUADS)
        )

    def test_05_atom_strict_signs(self):
        for row in self.value["atom_controls"]:
            self.assertLess(p.unpack(row["A"]), 0)
            self.assertLess(p.unpack(row["C"]), 0)
            self.assertGreater(p.unpack(row["det"]), 0)

    def test_06_negative_pair_failure_retained(self):
        self.assertEqual(
            [row["q"] for row in self.value["negative_without_reserve"]], [0, 1]
        )
        self.assertTrue(
            all(
                p.unpack(row["value"]) < 0
                for row in self.value["negative_without_reserve"]
            )
        )

    def test_07_negative_constant_cap(self):
        self.assertTrue(
            all(
                p.unpack(self.value["constants"]["negative_coefficients"][str(q)])
                < 2**28
                for q in p.QS
            )
        )

    def test_08_positive_constant_floor(self):
        self.assertTrue(
            all(
                p.unpack(self.value["constants"]["positive_coefficients"][str(q)])
                > Q(1, 2**12)
                for q in p.QS
            )
        )

    def test_09_height_integer_margin(self):
        self.assertLess(p.H + 3, 2**64)
        self.assertGreater(p.H * p.H, 2**46)

    def test_10_phase_constants(self):
        self.assertLess(p.unpack(self.value["constants"]["phase"]["total_lt"]), Q(3, 2))

    def test_11_shared_anchor_edges_distinct(self):
        edges = self.value["allocation"]["shared_anchor_distinct"]
        self.assertEqual(len({tuple(sorted(x)) for x in edges}), len(edges))

    def test_12_reverse_allocation_rejected(self):
        edges = self.value["allocation"]["reverse_collision"]
        self.assertNotEqual(len({tuple(sorted(x)) for x in edges}), len(edges))

    def test_13_multiplicity_retained(self):
        self.assertEqual(self.value["allocation"]["multiplicity_weights"], [2, 4, 8])

    def test_14_source_manifest_fresh(self):
        self.assertEqual(p.load(p.MANIFEST), p.source_manifest())

    def test_15_artifact_seals(self):
        self.assertEqual(self.value["artifacts"], p.artifact_seals())

    def test_16_payload_seal(self):
        payload = {k: v for k, v in self.value.items() if k != "payload_sha256"}
        self.assertEqual(self.value["payload_sha256"], p.sha(p.canonical(payload)))

    def test_17_duplicate_key_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":1,"a":2}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_18_nonfinite_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":NaN}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_19_noncanonical_rational_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([2, 2])

    def test_20_zero_denominator_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([1, 0])

    def test_21_schema_cap_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["extra"] = 1
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_22_contract_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["contract"]["finite_scope"] = "expanded"
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_23_dispersion_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["dispersion"][0]["value"] = [0, 1]
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_24_atom_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["atom_controls"][0]["det"] = [1, 1]
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_25_allocation_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["allocation"]["shared_anchor_distinct"][1] = [10, 25]
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_26_manifest_reseal_rejected(self):
        bad = copy.deepcopy(p.load(p.MANIFEST))
        bad["external_primary"][0]["sha256"] = "0" * 64
        with (
            mock.patch.object(p, "load", return_value=bad),
            self.assertRaises(ValueError),
        ):
            p.validate(self.value)

    def test_27_exact_determinant_singular(self):
        self.assertEqual(p.determinant([[Q(1), Q(1)], [Q(2), Q(2)]]), 0)

    def test_28_exact_determinant_swap(self):
        self.assertEqual(p.determinant([[Q(0), Q(1)], [Q(1), Q(0)]]), -1)

    def test_29_boolean_integer_alias_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["constants"]["margin"]["H_plus_3_lt_2_pow_64"] = 1
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))


if __name__ == "__main__":
    unittest.main()

"""Exact finite controls; the infinite H2 domain theorem is reviewed in prose."""

from __future__ import annotations

import copy
import itertools
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "research" / "exploratory")
)
import xi_zero_feature_form_domain_obstruction as p


class ZeroFeatureDomainTests(unittest.TestCase):
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

    def test_02_panel_coverage(self):
        self.assertEqual(len(self.value["panels"]), len(p.MODELS) * len(p.PANELS))

    def test_03_every_principal_subpacket(self):
        expected = [
            list(c) for n in range(1, 6) for c in itertools.combinations(range(5), n)
        ]
        for row in self.value["panels"]:
            self.assertEqual([cell["indices"] for cell in row["minors"]], expected)

    def test_04_minors_nonnegative(self):
        for row in self.value["panels"]:
            self.assertTrue(all(p.unpack(cell["det"]) >= 0 for cell in row["minors"]))

    def test_05_rank_caps(self):
        for row in self.value["panels"]:
            if len(row["x"]) > row["rank_cap"]:
                self.assertEqual(p.unpack(row["minors"][-1]["det"]), 0)

    def test_06_finite_minimality(self):
        self.assertNotEqual(
            p.unpack(self.value["minimality"]["feature_determinant"]), 0
        )

    def test_07_residue_pair_invertible(self):
        self.assertEqual(
            self.value["residues"]["stacked_determinant_modulus_squared"], 4
        )

    def test_08_same_height_aggregated(self):
        self.assertIs(
            self.value["residues"]["same_height_multiplicity_aggregated"], True
        )

    def test_09_missing_sine_fails(self):
        self.assertNotEqual(
            p.unpack(self.value["hostile"]["correct"]),
            p.unpack(self.value["hostile"]["missing_sine"]),
        )

    def test_10_wrong_pole_fails(self):
        self.assertNotEqual(
            p.unpack(self.value["hostile"]["correct"]),
            p.unpack(self.value["hostile"]["wrong_pole_sign"]),
        )

    def test_11_operator_identity_forbidden(self):
        self.assertIs(self.value["hostile"]["operator_identity_allowed"], False)

    def test_12_source_manifest_fresh(self):
        self.assertEqual(p.load(p.MANIFEST), p.source_manifest())

    def test_13_artifact_seals(self):
        self.assertEqual(self.value["artifacts"], p.artifact_seals())

    def test_14_payload_seal(self):
        payload = {k: v for k, v in self.value.items() if k != "payload_sha256"}
        self.assertEqual(self.value["payload_sha256"], p.sha(p.canonical(payload)))

    def test_15_duplicate_key_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":1,"a":2}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_16_nonfinite_rejected(self):
        with (
            mock.patch.object(p.Path, "read_bytes", return_value=b'{"a":Infinity}'),
            self.assertRaises(ValueError),
        ):
            p.load(p.FIXTURE)

    def test_17_rational_noncanonical_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([2, 2])

    def test_18_rational_zero_denominator_rejected(self):
        with self.assertRaises(ValueError):
            p.unpack([1, 0])

    def test_19_contract_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["contract"]["domain_result"] = "closable"
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_20_panel_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["panels"][0]["minors"][0]["det"] = [0, 1]
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_21_operator_reseal_rejected(self):
        bad = copy.deepcopy(self.value)
        bad["hostile"]["operator_identity_allowed"] = True
        with self.assertRaises(ValueError):
            p.validate(self.reseal(bad))

    def test_22_source_reseal_rejected(self):
        bad = copy.deepcopy(p.load(p.MANIFEST))
        bad["sources"][0]["commit"] = "0" * 40
        with (
            mock.patch.object(p, "load", return_value=bad),
            self.assertRaises(ValueError),
        ):
            p.validate(self.value)

    def test_23_determinant_routes_independent(self):
        matrix = [[Q(1), Q(2), Q(3)], [Q(2), Q(5), Q(7)], [Q(3), Q(7), Q(11)]]
        self.assertEqual(p.det_elimination(matrix), p.det_permutation(matrix))

    def test_24_singular_determinant(self):
        matrix = [[Q(1), Q(2)], [Q(2), Q(4)]]
        self.assertEqual(p.det_elimination(matrix), 0)
        self.assertEqual(p.det_permutation(matrix), 0)


if __name__ == "__main__":
    unittest.main()

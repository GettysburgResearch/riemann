"""Exact held-out formulas, coverage and primitive source/report attacks."""

import copy
import itertools
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research/exploratory"))
import xi_occupancy_carleson_capture as M


class OccupancyCarlesonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_source_authentication(self):
        self.assertEqual(M.authenticate(), 4)
        self.assertEqual(len(M.BINDINGS), 4)

    def test_02_primitive_fixture_replay(self):
        self.assertEqual(
            M.canonical(self.report), M.canonical(M.load_json(M.FIXTURE.read_bytes()))
        )

    def test_03_complete_coverage(self):
        self.assertEqual(
            self.report["coverage"],
            {
                "cell_families": 32,
                "independent_subset_controls": 17,
                "normalized_boxes": 600,
                "rayleigh": 16,
                "sparse_prefixes": 32,
            },
        )
        self.assertEqual(
            [(x["N"], x["family"]) for x in self.report["families"]],
            [(n, k) for n in range(1, 17) for k in ("dispersed", "crowded")],
        )
        self.assertEqual(len(self.report["normalized_boxes"]), 600)

    def test_04_all_preregistered_family_values(self):
        for row in self.report["families"]:
            self.assertEqual(
                Q(row["carleson_cost"]), 1 if row["family"] == "dispersed" else row["N"]
            )

    def test_05_independent_subset_oracle(self):
        for n in range(1, 9):
            for kind in ("dispersed", "crowded"):
                self.assertEqual(
                    M.box_norm(M.family(kind, n))[0], M.subset_norm(M.family(kind, n))
                )
        self.assertEqual(M.box_norm(M.MIXED)[0], M.subset_norm(M.MIXED))

    def test_06_heldout_all_pairs_and_triples(self):
        # Not the author's family parametrization: full finite held-out grid.
        grid = tuple(
            itertools.product((Q(0), Q(1, 3), Q(2, 3)), (Q(1, 9), Q(1, 3), Q(2, 3)))
        )
        for n in (2, 3):
            for subset in itertools.combinations(grid, n):
                self.assertEqual(M.box_norm(subset)[0], M.subset_norm(subset))

    def test_07_single_repeated_and_mixed_atoms(self):
        self.assertEqual(M.box_norm(((Q(1, 2), Q(1, 7)),))[0], 1)
        self.assertEqual(M.box_norm(((Q(1, 2), Q(1, 7)),) * 3)[0], 3)
        self.assertEqual(M.box_norm(((Q(0), Q(1, 8)), (Q(1, 8), Q(1, 4))))[0], Q(3, 2))

    def test_08_report_witnesses(self):
        for row in self.report["families"] + [self.report["mixed"]]:
            left, length, mass = map(Q, row["witness_left_length_mass"])
            pts = [tuple(map(Q, b)) for b in row["nodes"]]
            actual = sum(
                (y for x, y in pts if left <= x <= left + length and y <= length), Q(0)
            )
            self.assertEqual(actual, mass)
            self.assertEqual(mass / length, Q(row["carleson_cost"]))

    def test_09_small_and_large_interval_proof_constants(self):
        for r in (Q(1, 100), Q(1, 3), Q(9, 10)):
            self.assertLessEqual(2 * r, 3 * r)
        for r in (Q(1), Q(3, 2), Q(10)):
            self.assertLessEqual(r + 2, 3 * r)

    def test_10_union_boxes_and_endpoint_convention(self):
        union = M.normalized_union()
        for row in self.report["normalized_boxes"]:
            left, length, mass = map(Q, (row["left"], row["length"], row["mass"]))
            self.assertEqual(M.box_mass(union, left, length), mass)
            self.assertLessEqual(mass, 3 * length)
        self.assertEqual(
            M.box_mass(((Q(0), Q(1), Q(1)), (Q(1), Q(1), Q(1))), Q(0), Q(1)), 2
        )

    def test_11_reflection_and_local_jensen_geometry(self):
        for height in (Q(1, 4), Q(1), Q(3), Q(6)):
            self.assertGreater((height + 3) ** 2, 1 + (height + 2) ** 2)
        self.assertEqual((-1j) ** 5, -1j)
        self.assertEqual((-1j) ** 6, -1)

    def test_12_crowded_rayleigh_and_weight(self):
        for row in self.report["rayleigh"]:
            n = row["N"]
            self.assertGreaterEqual(Q(row["unweighted_rayleigh"]), Q(16 * n, 17))
            self.assertEqual(
                Q(row["weighted_rayleigh"]), Q(row["unweighted_rayleigh"]) / n
            )
            self.assertLessEqual(Q(row["weighted_rayleigh"]), 1)

    def test_13_sparse_prefix_tail_identity(self):
        for row in self.report["sparse_prefixes"]:
            j = row["last_scale"]
            self.assertEqual(Q(row["exact_remaining_tail"]), Q(j + 2, 2**j))
            self.assertEqual(
                Q(row["sum_j_over_2_power_j"]) + Q(row["exact_remaining_tail"]), 2
            )

    def test_14_numeric_and_resource_guards(self):
        for bad in (True, 1.0, float("nan"), "1", None):
            with self.assertRaises(ValueError):
                M.family("dispersed", bad)
        for n in (0, -1, 17, 1000000):
            with self.assertRaises(ValueError):
                M.family("crowded", n)
        for bad in (
            (),
            ((0, 0),),
            ((0, 2),),
            ((1, Q(1, 2)),),
            ((False, Q(1, 2)),),
            ((0, 0.1),),
        ):
            with self.assertRaises(ValueError):
                M.box_norm(bad)
        with self.assertRaises(ValueError):
            M.subset_norm(M.family("dispersed", 9))
        with self.assertRaises(ValueError):
            M.exact(Q(1, 2**257))

    def test_15_json_guards(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b"[" * 18 + b"0" + b"]" * 18,
            b" " * 1000001,
        ):
            with self.assertRaises((ValueError, RecursionError)):
                M.load_json(raw)

    def test_16_fully_resealed_hostile_reports(self):
        mutations = (
            lambda r: r["families"][0]["nodes"][0].__setitem__(0, "1/3"),
            lambda r: r["families"][1].__setitem__("carleson_cost", "9"),
            lambda r: r["families"][0].__setitem__("subset_oracle_complete", False),
            lambda r: r["normalized_boxes"][0].__setitem__("bound", "0"),
            lambda r: r["sparse_prefixes"][0].__setitem__("exact_remaining_tail", "0"),
            lambda r: r["coverage"].__setitem__("normalized_boxes", 599),
            lambda r: r["contract"].__setitem__(
                "physical_metric", "coefficient Euclidean norm"
            ),
            lambda r: r["sources"][0].__setitem__("sha256_lf", "0" * 64),
        )
        for change in mutations:
            value = copy.deepcopy(self.report)
            value.pop("payload_sha256")
            change(value)
            with self.assertRaises(ValueError):
                M.check_report(M.seal(value))

    def test_17_true_source_mutation(self):
        forged = copy.deepcopy(M.BINDINGS)
        forged[0]["git_blob"] = "0" * 40
        with mock.patch.object(M, "BINDINGS", forged), self.assertRaises(ValueError):
            M.authenticate()

    def test_18_no_analytic_claim_from_finite_controls(self):
        self.assertTrue(self.report["contract"]["no_xi_computation"])
        self.assertIn("innerness", self.report["contract"]["open"])
        self.assertIn("cofinal", self.report["contract"]["open"])
        self.assertNotEqual(
            self.report["contract"]["arithmetic_class"], "DIRECTED_BALL"
        )


if __name__ == "__main__":
    unittest.main()

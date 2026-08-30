"""Independent controls and hostile contracts for the Segre Koszul--Lie packet."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/l-families/atlas/generalized/segre_koszul_lie_parent.py"
SPEC = importlib.util.spec_from_file_location("segre_koszul_lie_parent", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SegreKoszulLieTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def bar(self, ranks, degree):
        return next(
            row
            for row in self.report["bar_controls"]
            if row["ranks"] == list(ranks) and row["internal_degree"] == degree
        )

    def lie(self, ranks):
        return next(
            row
            for row in self.report["actual_lie_quotients"]
            if row["ranks"] == list(ranks)
        )

    def test_fixture_canonical_replay(self):
        M.same_json(M.strict_json(M.bounded_bytes(M.FIXTURE)), self.report)

    def test_complete_bar_coverage(self):
        self.assertEqual(len(self.report["bar_controls"]), 16)
        observed = {
            (tuple(row["ranks"]), row["internal_degree"])
            for row in self.report["bar_controls"]
        }
        self.assertEqual(
            observed,
            {(ranks, degree) for ranks in M.BAR_PANELS for degree in range(1, 5)},
        )
        for row in self.report["bar_controls"]:
            self.assertEqual(
                row["homology_H1_through_Hj"][:-1],
                [0] * (row["internal_degree"] - 1),
            )
            self.assertEqual(
                sum(row["chain_dimensions"]), row["allocation"]["total_basis_slots"]
            )

    def test_direct_bar_diagonal_dimensions(self):
        expected = {
            (2,): [2, 1, 0, 0],
            (2, 2): [4, 7, 8, 8],
            (2, 3): [6, 18, 40, 81],
            (2, 2, 2): [8, 37, 144, 540],
        }
        for ranks, values in expected.items():
            self.assertEqual(
                [
                    self.bar(ranks, degree)["homology_H1_through_Hj"][-1]
                    for degree in range(1, 5)
                ],
                values,
            )

    def test_unequal_rank_fourth_tor_is_not_ring_piece(self):
        row = self.bar((2, 3), 4)
        self.assertEqual(row["chain_dimensions"], [75, 804, 1944, 1296])
        self.assertEqual(row["differential_ranks_d1_through_dj"], [0, 75, 729, 1215])
        self.assertEqual(row["homology_H1_through_Hj"], [0, 0, 0, 81])
        self.assertEqual(row["square_zero_columns"], 1944 + 1296)
        self.assertNotEqual(
            row["homology_H1_through_Hj"][-1], row["chain_dimensions"][0]
        )

    def test_three_factor_full_complex(self):
        row = self.bar((2, 2, 2), 4)
        self.assertEqual(row["chain_dimensions"], [125, 1753, 5184, 4096])
        self.assertEqual(row["differential_ranks_d1_through_dj"], [0, 125, 1628, 3556])
        self.assertEqual(row["homology_H1_through_Hj"], [0, 0, 0, 540])

    def test_actual_cubic_lie_quotients(self):
        expected = {
            (2,): (3, 0, 0, 0),
            (2, 2): (9, 1, 8, 0),
            (2, 3): (18, 3, 40, 2),
            (3, 3): (36, 9, 181, 16),
            (2, 2, 2): (27, 9, 144, 16),
        }
        for ranks, values in expected.items():
            row = self.lie(ranks)
            self.assertEqual(
                tuple(
                    row[key]
                    for key in ("quadratic_dual_relations", "g2", "U_g_degree3", "g3")
                ),
                values,
            )
            self.assertEqual(
                row["ideal_degree3_rank"] + row["U_g_degree3"], row["tensor_degree3"]
            )
            self.assertEqual(
                sum(item["multiplicity"] for item in row["g3_dual_positive_weights"]),
                row["g3"],
            )

    def test_unequal_rank_whole_character(self):
        self.assertEqual(
            self.lie((2, 3))["g3_dual_positive_weights"],
            [
                {"weight": [[0, 0, 1], [0, 1, 2]], "multiplicity": 1},
                {"weight": [[0, 1, 1], [0, 1, 2]], "multiplicity": 1},
            ],
        )

    def test_cubic_dual_multidegrees(self):
        for row in self.report["actual_lie_quotients"]:
            for item in row["g3_dual_positive_weights"]:
                self.assertEqual(len(item["weight"]), len(row["ranks"]))
                self.assertGreater(item["multiplicity"], 0)
                for rank, block in zip(row["ranks"], item["weight"]):
                    self.assertEqual(len(block), 3)
                    self.assertEqual(sorted(block), block)
                    self.assertTrue(all(0 <= value < rank for value in block))

    def test_native_minors_and_linear_syzygies(self):
        self.assertEqual(
            self.report["linear_syzygy_control"],
            {
                "ranks": [2, 3],
                "ambient_degree3": 56,
                "variable_times_minor_columns": 18,
                "rank": 16,
                "linear_syzygies": 2,
                "native_identities": ["zero", "zero"],
            },
        )

    def test_additional_polynomial_controls(self):
        for ranks in ((1,), (1, 1, 1), (1, 3)):
            row = M.bar_control(ranks, 4)
            self.assertEqual(row["homology_H1_through_Hj"], [0, 0, 0, 0])
            self.assertEqual(M.lie3_control(ranks)["g3"], 0)

    def test_factor_permutation_character_control(self):
        swapped = M.lie3_control((3, 2))
        original = self.lie((2, 3))
        transformed = sorted(
            (tuple(map(tuple, reversed(item["weight"]))), item["multiplicity"])
            for item in original["g3_dual_positive_weights"]
        )
        observed = sorted(
            (tuple(map(tuple, item["weight"])), item["multiplicity"])
            for item in swapped["g3_dual_positive_weights"]
        )
        self.assertEqual(observed, transformed)

    def test_reject_noninteger_ranks(self):
        class IntSubclass(int):
            pass

        for ranks in (
            None,
            "23",
            (),
            [],
            [0],
            [4],
            [True],
            [2.0],
            [Fraction(2)],
            [IntSubclass(2)],
            [1] * 4,
        ):
            with self.subTest(ranks=ranks), self.assertRaises(ValueError):
                M.bar_control(ranks, 2)
            with self.subTest(lie_ranks=ranks), self.assertRaises(ValueError):
                M.lie3_control(ranks)

    def test_reject_bad_degrees_and_caps(self):
        for degree in (True, 0, -1, 5, 2.0, Fraction(2), "2", None):
            with self.subTest(degree=degree), self.assertRaises(ValueError):
                M.bar_control((2, 3), degree)
        for cap in (True, 0, M.MAX_TOTAL_BASIS + 1, 100.0, None):
            with self.subTest(cap=cap), self.assertRaises(ValueError):
                M.bar_control((2, 3), 2, cap)

    def test_exclusive_bar_cap_before_allocation(self):
        plan = M.bar_preflight((2, 3), 4)
        total = plan["total_basis_slots"]
        with patch.object(
            M, "_ring_basis", side_effect=RuntimeError("allocated early")
        ):
            with self.assertRaises(ValueError):
                M.bar_control((2, 3), 4, total)
            with self.assertRaises(ValueError):
                M.bar_control((3, 3), 4)
            with self.assertRaises(ValueError):
                M.bar_control((3, 3, 3), 4)
        self.assertEqual(M.bar_preflight((2, 3), 4, total + 1), plan)

    def test_lie_cap_before_word_allocation(self):
        with (
            patch.object(M, "product", side_effect=RuntimeError("allocated early")),
            self.assertRaises(ValueError),
        ):
            M.lie3_control((2, 2, 3))
        self.assertEqual(M.lie_preflight((3, 3))["tensor_degree3"], 729)

    def test_exact_sparse_rank_controls(self):
        self.assertEqual(M._sparse_rank([]), 0)
        self.assertEqual(M._sparse_rank([{}, {0: 0}]), 0)
        self.assertEqual(M._sparse_rank([{0: 1, 1: 2}, {0: 2, 1: 4}]), 1)
        self.assertEqual(
            M._sparse_rank([{0: Fraction(1, 3), 1: 1}, {0: 1, 1: Fraction(2)}]),
            2,
        )

    def test_strict_json_and_typed_replay(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":{"b":0,"b":1}}',
            b"NaN",
            b"Infinity",
            b"-Infinity",
        ):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                M.strict_json(raw)
        for raw in ("{}", bytearray(b"{}"), b" " * (M.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                M.strict_json(raw)
        for altered in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                M.same_json(altered, 1)

    def test_payload_hash_is_recomputed(self):
        report = copy.deepcopy(self.report)
        expected = report.pop("payload_sha256")
        self.assertEqual(M.hashlib.sha256(M.canonical(report)).hexdigest(), expected)
        report["bar_controls"][0]["homology_H1_through_Hj"][0] += 1
        self.assertNotEqual(M.hashlib.sha256(M.canonical(report)).hexdigest(), expected)

    def test_source_manifest_tamper_rejected(self):
        malformed = copy.deepcopy(M.EXPECTED_MANIFEST)
        malformed["parents"][0]["git_blob"] = "0" * 40
        with (
            patch.object(M, "bounded_bytes", return_value=M.canonical(malformed)),
            self.assertRaises(ValueError),
        ):
            M.source_locks()

    def test_source_blob_mismatch_rejected(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=["0" * 40, b"bad"]),
            self.assertRaisesRegex(ValueError, "blob mismatch"),
        ):
            M.source_locks()

    def test_source_frozen_bytes_mismatch_rejected(self):
        blob = M.EXPECTED_MANIFEST["parents"][0]["git_blob"]
        with (
            patch.object(M.subprocess, "check_output", side_effect=[blob, b"bad"]),
            self.assertRaisesRegex(ValueError, "digest mismatch"),
        ):
            M.source_locks()

    def test_source_current_bytes_mismatch_rejected(self):
        original = M.bounded_bytes
        parent = M.ROOT / M.EXPECTED_MANIFEST["parents"][0]["path"]

        def altered(path):
            return b"bad" if path == parent else original(path)

        with (
            patch.object(M, "bounded_bytes", side_effect=altered),
            self.assertRaisesRegex(ValueError, "current parent"),
        ):
            M.source_locks()

    def test_source_missing_git_object_rejected(self):
        failure = M.subprocess.CalledProcessError(1, ["git", "show"])
        with (
            patch.object(M.subprocess, "check_output", side_effect=failure),
            self.assertRaisesRegex(ValueError, "unavailable"),
        ):
            M.source_locks()

    def test_artifact_source_hashes_and_firewalls(self):
        for path, expected in self.report["artifact_sha256_lf"].items():
            self.assertEqual(M.digest(M.bounded_bytes(ROOT / path)), expected)
        self.assertEqual(self.report["coverage"]["fitted_Hilbert_series_ranks"], 0)
        self.assertEqual(self.report["coverage"]["prime_samples"], 0)
        self.assertEqual(
            self.report["verdict"], "EXACT_BOUNDED_ALGEBRA_PASS_NO_ANALYTIC_COMPLETION"
        )
        note = M.NOTE.read_text(encoding="utf-8")
        for phrase in (
            "Gorbounov--Schechtman",
            "strict alternating",
            "natural boundary",
            "RH and GRH remain open",
        ):
            self.assertIn(phrase, note)

    def test_fixture_missing_row_and_float_counterfeit_rejected(self):
        expected = M.strict_json(M.bounded_bytes(M.FIXTURE))
        for change in ("missing", "float", "unknown"):
            altered = copy.deepcopy(expected)
            if change == "missing":
                altered["bar_controls"].pop()
            elif change == "float":
                altered["bar_controls"][0]["internal_degree"] = 1.0
            else:
                altered["unexpected"] = 1
            with self.subTest(change=change), self.assertRaises(ValueError):
                M.same_json(altered, self.report)


if __name__ == "__main__":
    unittest.main()

"""Exact coefficient/wall coverage and hostile source-contract controls."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/l-families/atlas/generalized/segre_higher_power_unitary_chambers.py"
)
SPEC = importlib.util.spec_from_file_location("segre_higher", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class HigherPowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_fixture(self):
        M.same_json(M.strict_json(M.bounded_bytes(M.FIXTURE)), self.report)

    def test_arithmetic_contract(self):
        self.assertEqual(
            self.report["arithmetic"],
            {
                "class": "MIXED",
                "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
                "rounding": "none",
            },
        )

    def test_all_three_full_characters(self):
        self.assertEqual(
            [r["word_total"] for r in self.report["characters"]],
            [2520, 113400, 7484400],
        )
        for row in self.report["characters"]:
            m = row["power"]
            self.assertEqual(row["denominator_degree"], 2 * m + 1)
            self.assertEqual(row["numerator_degree"], 2 * m - 2)
            self.assertTrue(all(v > 0 for _, _, v in row["full_character"]))
            self.assertLessEqual(row["peak_DP_states"], M.MAX_STATES)

    def test_character_not_only_dimension(self):
        p = M.native_polynomials(4)[1]
        wrong = p + M.T * M.X
        self.assertNotEqual(M.laurent_character(wrong), M.multiset_character(4)[0])

    def test_small_classical_character(self):
        char, _, _ = M.multiset_character(2)
        self.assertEqual(
            dict(char), {(0, 0): 1, (1, -1): 1, (1, 0): 2, (1, 1): 1, (2, 0): 1}
        )

    def test_all_component_counts(self):
        self.assertEqual(
            [
                len(t["pure_closed_components_wall_indices"])
                for t in self.report["chambers"]
            ],
            [3, 4, 6],
        )

    def test_complete_wall_counts(self):
        self.assertEqual(
            [len(t["walls"]) for t in self.report["chambers"]], [9, 21, 36]
        )
        for table in self.report["chambers"]:
            self.assertEqual(len(table["cells"]), len(table["walls"]) + 1)
            self.assertEqual(
                sum(f["real_roots_in_minus2_plus2"] for f in table["wall_factors"]),
                len(table["walls"]),
            )

    def test_wall_factor_degrees(self):
        self.assertEqual(
            [
                max(len(f["coefficients_descending"]) - 1 for f in t["wall_factors"])
                for t in self.report["chambers"]
            ],
            [14, 32, 62],
        )

    def test_no_float_wall_brackets(self):
        for table in self.report["chambers"]:
            for row in table["walls"]:
                left, right = (Fraction(*p) for p in row["bracket"])
                self.assertLessEqual(left, right)
                self.assertLessEqual(right - left, Fraction(1, 10**8))

    def test_every_cell_has_Sturm_certificate(self):
        for table in self.report["chambers"]:
            for cell in table["cells"]:
                a, b = cell["sturm_variations"]
                self.assertEqual(a - b, cell["roots_in_open_interval"])
                self.assertEqual(cell["pure"], a - b == table["power"] - 1)

    def test_heldout_failures_preserved(self):
        self.assertEqual(
            [r["prediction_passed"] for r in self.report["heldout_power6"]],
            [True, True, True, True, False],
        )
        self.assertEqual(self.report["preregistered_component_count"], 5)
        self.assertEqual(self.report["observed_power6_component_count"], 6)

    def test_two_way_nonnesting(self):
        rows = self.report["nonnesting"]
        self.assertEqual([r["power5"]["pure"] for r in rows], [False, True])
        self.assertEqual([r["power6"]["pure"] for r in rows], [True, False])
        self.assertEqual(rows[0]["x"], [-407, 250])

    def test_sixth_torsion_predictions(self):
        rows = {r["x"]: r for r in self.report["torsion"] if r["power"] == 6}
        z = M.Z
        for x, target in [
            (-1, (z - 2) ** 2 * (z + 1) ** 3),
            (0, z**2 * (z - 2) * (z + 2) ** 2),
            (1, (z - 2) * (z - 1) * (z + 1) * (z + 2) * (z + 63)),
        ]:
            self.assertEqual(
                rows[x]["M_coefficients_descending"],
                [int(c) for c in sp.Poly(target, z).all_coeffs()],
            )

    def test_cubic_distinct_roots_and_characters(self):
        row = self.report["open_SU3_control"]
        self.assertEqual(row["simple_unit_roots"], 7)
        self.assertEqual(row["separation_values"], [[13, 8], [27, 8]])
        self.assertEqual(len(row["distinct_restricted_characters"]), 10)
        self.assertFalse(row["effective_neighborhood_radius_claimed"])

    def test_source_contract(self):
        self.assertEqual(len(self.report["sources"]["parents"]), 7)
        self.assertEqual(
            sum(r["current_copy_required"] for r in self.report["sources"]["parents"]),
            5,
        )
        self.assertEqual(
            self.report["sources"]["parents"][5]["commit"],
            "e21e44d84077b7703c6795a81c91fc305b3fe344",
        )

    def test_artifact_hashes(self):
        for path, sha in self.report["artifact_sha256_lf"].items():
            self.assertEqual(M.digest(M.bounded_bytes(ROOT / path)), sha)
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)

    def test_payload_seal(self):
        clone = copy.deepcopy(self.report)
        sha = clone.pop("payload_sha256")
        self.assertEqual(hashlib.sha256(M.canonical(clone)).hexdigest(), sha)

    def test_typed_bool_int_not_equal(self):
        with self.assertRaises(ValueError):
            M.same_json({"n": 1}, {"n": True})

    def test_resealed_wrong_result_rejected(self):
        clone = copy.deepcopy(self.report)
        clone["heldout_power6"][-1]["pure"] = True
        clone.pop("payload_sha256")
        clone["payload_sha256"] = hashlib.sha256(M.canonical(clone)).hexdigest()
        with self.assertRaises(ValueError):
            M.same_json(clone, self.report)

    def test_duplicate_JSON_key(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            M.strict_json(b'{"a":1,"a":2}')

    def test_noninteger_JSON_numbers(self):
        for raw in (b"1.5", b"NaN", b"Infinity", b"-Infinity", b"1e2"):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                M.strict_json(raw)

    def test_JSON_depth_and_bytes(self):
        for raw in (b"[" * 33 + b"0" + b"]" * 33, b" " * (M.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                M.strict_json(raw)

    def test_JSON_integer_cap(self):
        with self.assertRaisesRegex(ValueError, "digit cap"):
            M.strict_json(b"1" * 2001)

    def test_LF_hash_normalization(self):
        self.assertEqual(M.digest(b"a\nb\n"), M.digest(b"a\r\nb\r\n"))

    def test_power_type_and_resource_guards(self):
        for n in (True, False, 0, 7, -1, 4.0, "4"):
            with self.subTest(n=n), self.assertRaises(ValueError):
                M.native_polynomials(n)

    def test_rational_type_and_bits(self):
        for x in (True, 0.5, "0", 1 << 1025):
            with self.subTest(x=x), self.assertRaises(ValueError):
                M.membership(4, x)

    def test_unitary_domain_guard(self):
        for x in (-3, 3):
            with self.assertRaises(ValueError):
                M.membership(4, x)

    def test_torsion_not_regular_membership(self):
        with self.assertRaises(ValueError):
            M.membership(6, -1)

    def test_DP_cap(self):
        with (
            patch.object(M, "MAX_STATES", 5),
            self.assertRaisesRegex(ValueError, "state cap"),
        ):
            M.multiset_character(4)

    def test_polynomial_caps(self):
        with self.assertRaisesRegex(ValueError, "degree cap"):
            M.bounded_poly(M.X**81, M.X)

    def test_wrong_manifest_fails_closed(self):
        forged = copy.deepcopy(M.EXPECTED_MANIFEST)
        forged["parents"][0]["sha256_lf"] = "0" * 64
        original = M.bounded_bytes

        def changed(path):
            return M.canonical(forged) if path == M.MANIFEST else original(path)

        with (
            patch.object(M, "bounded_bytes", side_effect=changed),
            self.assertRaises(ValueError),
        ):
            M.source_locks()

    def test_current_parent_tamper_fails(self):
        original = M.bounded_bytes
        target = ROOT / M.EXPECTED_MANIFEST["parents"][0]["path"]

        def changed(path):
            return original(path) + b" " if path == target else original(path)

        with (
            patch.object(M, "bounded_bytes", side_effect=changed),
            self.assertRaisesRegex(ValueError, "current source"),
        ):
            M.source_locks()

    def test_frozen_git_blob_tamper_fails(self):
        with (
            patch.object(M.subprocess, "check_output", return_value="0" * 40),
            self.assertRaisesRegex(ValueError, "source blob"),
        ):
            M.source_locks()

    def test_no_global_claim(self):
        self.assertFalse(self.report["global_or_automorphic_conclusion"])

    def test_primitive_Sturm_negative_leading_and_repeated_roots(self):
        z = M.Z
        for p in [
            (z + 3) * (z + 1) * (z - 1),
            -(z + 3) * (z + 1) * (z - 1),
            (z + 1) ** 2 * (z - 1),
            z**5 - 3 * z**3 + z,
            -(z**5) + 3 * z**3 - z,
        ]:
            count, _ = M.sturm_count(p, z)
            self.assertEqual(count, int(sp.Poly(p, z).count_roots(-2, 2)))

    def test_wall_Sturm_certificates(self):
        for table in self.report["chambers"]:
            for factor in table["wall_factors"]:
                a, b = factor["sturm_outer_variations"]
                self.assertEqual(a - b, factor["real_roots_in_minus2_plus2"])
            for wall in table["walls"]:
                if wall["sturm_bracket_variations"] is not None:
                    a, b = wall["sturm_bracket_variations"]
                    self.assertEqual(a - b, 1)

    def test_theorem_component_endpoints(self):
        expected = [
            [
                (("R", 1), ("beta", 1)),
                (("sqrt2", 1), ("R", 2)),
                (("R", 3), ("zero", 1)),
            ],
            [
                (("R", 2), ("R", 3)),
                (("sqrt2", 1), ("gamma", 1)),
                (("E", 2), ("R", 5)),
                (("R", 8), ("zero", 1)),
            ],
            [
                (("R", 2), ("R", 3)),
                (("sqrt2", 1), ("R", 7)),
                (("R", 8), ("gamma", 1)),
                (("R", 10), ("R", 11)),
                (("R", 14), ("R", 15)),
                (("R", 16), ("zero", 1)),
            ],
        ]
        known = {
            (1, 7, 8): "beta",
            (1, 0, -2): "sqrt2",
            (1, -1, -1): "gamma",
            (1, 0): "zero",
            (1, 14, 48, 57, 20): "E",
        }
        for table, target in zip(self.report["chambers"], expected):
            factors = {
                row["id"]: tuple(row["coefficients_descending"])
                for row in table["wall_factors"]
            }

            def label(index, table=table, factors=factors):
                row = table["walls"][index]
                coefficients = factors[row["factor"]]
                name = "R" if len(coefficients) > 10 else known[coefficients]
                return name, row["root_index_in_minus2_plus2"]

            observed = [
                (label(a), label(b))
                for a, b in table["pure_closed_components_wall_indices"]
            ]
            self.assertEqual(observed, target)

    def test_negative_Laurent_coefficient_not_silently_dropped(self):
        with self.assertRaisesRegex(ValueError, "nonnegative Laurent"):
            M.laurent_character(1 - M.T)

    def test_wall_count_cap(self):
        with (
            patch.object(M, "MAX_WALLS", 1),
            self.assertRaisesRegex(ValueError, "wall number cap"),
        ):
            M.chamber_table(4)


if __name__ == "__main__":
    unittest.main()

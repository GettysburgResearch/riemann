"""Hostile exact controls; no numerical sine-power interpolation."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT / "research/l-families/atlas/generalized/"
    "rational_rotation_real_power_exact_degree.py"
)
SPEC = importlib.util.spec_from_file_location("exact_real_degree", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("unable to import exact-degree producer")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ExactRealDegreeTests(unittest.TestCase):
    def test_small_cyclotomic_polynomials(self):
        known = {
            1: (-1, 1),
            2: (1, 1),
            3: (1, 1, 1),
            4: (1, 0, 1),
            6: (1, -1, 1),
            8: (1, 0, 0, 0, 1),
            12: (1, 0, -1, 0, 1),
        }
        for n, expected in known.items():
            self.assertEqual(M.cyclotomic(n), expected)

    def test_cyclotomic_product_identity(self):
        for n in range(1, 4 * M.MAX_B + 1):
            product = (1,)
            for d in range(1, n + 1):
                if n % d:
                    continue
                factor = M.cyclotomic(d)
                result = [0] * (len(product) + len(factor) - 1)
                for i, left in enumerate(product):
                    for j, right in enumerate(factor):
                        result[i + j] += left * right
                product = tuple(result)
            self.assertEqual(product, tuple([-1] + [0] * (n - 1) + [1]))

    def test_exact_integer_degree_rectangle(self):
        for b in range(2, 13):
            for k in range(1, 9):
                got = M.integer_spectrum(b, k)
                self.assertEqual(got["reduced_degree"], b if k % 2 else min(b, k + 1))

    def test_held_out_prime_denominators(self):
        for b in (17, 23):
            for k in (1, 2, 5, 8, 11, 12):
                row = M.integer_spectrum(b, k)
                self.assertEqual(row["reduced_degree"], b if k % 2 else min(b, k + 1))

    def test_units_permute_modes(self):
        for b in range(2, 11):
            for k in (1, 2, 4):
                base = M.integer_spectrum(b, k)["support"]
                for a in range(1, b):
                    if math.gcd(a, b) == 1:
                        expected = sorted((a * j) % b for j in base)
                        self.assertEqual(
                            M.integer_spectrum(b, k, a=a)["support"], expected
                        )

    def test_exact_even_mode_alias_independent(self):
        for b in range(2, M.MAX_B + 1):
            for m in range(1, 7):
                grouped = {}
                for h in range(2 * m + 1):
                    residue = (m - h) % b
                    grouped[residue] = grouped.get(residue, 0) + (-1) ** h * math.comb(
                        2 * m, h
                    )
                expected = sorted(j for j, c in grouped.items() if c)
                self.assertEqual(M.integer_spectrum(b, 2 * m)["support"], expected)

    def test_sign_variations_and_leading_sign(self):
        rows = [
            M.sign_variation_row(b, j)
            for b in range(2, M.MAX_SIGN_B + 1)
            for j in range(1, b // 2 + 1)
        ]
        self.assertEqual(len(rows), 1024)
        for row in rows:
            self.assertLessEqual(row["variations"], row["j"])
            self.assertEqual(row["eventual_sign"], (-1) ** row["j"])

    def test_quadrant_zeros_are_removed(self):
        self.assertEqual(
            M.sign_variation_row(4, 1)["signs_in_increasing_base_order"], [0, -1]
        )
        self.assertEqual(
            M.sign_variation_row(4, 2)["signs_in_increasing_base_order"], [-1, 1]
        )

    def test_continuation_at_zero_not_zero_to_zero(self):
        for b in range(2, M.MAX_B + 1):
            for j in range(1, b):
                self.assertEqual(M.positive_zero_continuation_remainder(b, j), (-1,))

    def test_complex_counterexample_rational_block(self):
        # Twice the sample block has integer entries (0,1,2,1).
        # Evaluate its DFT in Q(i), retaining exact integer polynomials.
        remainders = []
        for j in range(4):
            raw = [0] * 4
            for l, value in enumerate((0, 1, 2, 1)):
                raw[(-j * l) % 4] += value
            remainders.append(M.divide_monic(raw, M.cyclotomic(4))[1])
        self.assertEqual(remainders, [(4,), (-2,), (), (-2,)])

    def test_types_and_hard_bounds(self):
        bad_calls = [
            lambda: M.cyclotomic(True),
            lambda: M.cyclotomic(97),
            lambda: M.integer_spectrum(1, 2),
            lambda: M.integer_spectrum(25, 2),
            lambda: M.integer_spectrum(3, 13),
            lambda: M.integer_spectrum(4, 2, a=2),
            lambda: M.integer_spectrum(4.0, 2),
            lambda: M.sign_variation_row(65, 1),
            lambda: M.build_fixture(max_b=True),
            lambda: M.build_fixture(resource_cap=True),
        ]
        for call in bad_calls:
            with self.assertRaises((TypeError, ValueError)):
                call()

    def test_exclusive_resource_cap(self):
        work = M.work_bound(2, 1, 2)["total"]
        with self.assertRaises(RuntimeError):
            M.build_fixture(max_b=2, max_k=1, sign_b=2, resource_cap=work)
        self.assertLess(
            M.work_bound(M.MAX_B, M.MAX_K, M.MAX_SIGN_B)["total"], M.WORK_CAP_EXCLUSIVE
        )

    def test_source_authentication_and_mutation_refusal(self):
        authenticated = M.verify_sources()
        self.assertTrue(authenticated["frozen_blobs_and_worktree_bytes_authenticated"])
        with (
            patch.object(M, "EXPECTED_MANIFEST_SHA256_LF", "0" * 64),
            self.assertRaises(RuntimeError),
        ):
            M.verify_sources()
        original = json.loads(M.SOURCES_PATH.read_text(encoding="utf-8"))
        malformed = copy.deepcopy(original)
        malformed["sources"][0]["sha256_lf"] = "0" * 64
        with (
            patch.object(M.json, "loads", return_value=malformed),
            self.assertRaises(RuntimeError),
        ):
            M.verify_sources()
        malformed = copy.deepcopy(original)
        malformed["sources"] = [17]
        with (
            patch.object(M.json, "loads", return_value=malformed),
            self.assertRaises(TypeError),
        ):
            M.verify_sources()
        with (
            patch.object(M.subprocess, "check_output", return_value=b"0" * 40),
            self.assertRaises(RuntimeError),
        ):
            M.verify_sources()

    def test_exact_stored_fixture_and_artifact_hashes(self):
        got = M.build_fixture()
        stored = json.loads(M.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(got, stored)
        digest = stored.pop("payload_sha256")
        self.assertEqual(digest, M.canonical_sha(stored))
        self.assertEqual(got["integer_power_census"]["row_count"], 120)
        self.assertEqual(got["resource_contract"]["float_operations"], 0)
        self.assertTrue(
            got["proof_boundary"][
                "noninteger_real_theorem_is_analytic_not_computational"
            ]
        )


if __name__ == "__main__":
    unittest.main()

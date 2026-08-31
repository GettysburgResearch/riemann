"""Source and acceptance controls for the separate fixed-minor extension."""

from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as F
from math import comb
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-six-hour/native_physical_tail_extension.py"
)
SPEC = importlib.util.spec_from_file_location("native_physical_tail_extension", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class PhysicalTailExtensionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = M.build("calibration")
        cls.helper, cls.minor, cls.old_cal, cls.old_later, *_ = M.source()

    def test_complete_calibration(self):
        M.equal(self.payload["result"], M.compact_prior(self.old_later["result"]))
        self.assertEqual(self.payload["result"]["horizon"], 2**20)
        self.assertEqual(self.payload["execution_status"], "PASS")
        self.assertEqual(
            self.payload["result"]["contraction"]["status"],
            "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        )

    def test_all_authentication_precedes_compile_and_parse(self):
        with (
            patch.object(M, "authenticate", side_effect=M.Refusal("bad frozen pin")),
            patch("builtins.compile") as compile_mock,
            patch.object(M, "read_json") as parse_mock,
            self.assertRaises(M.Refusal),
        ):
            M.source()
        compile_mock.assert_not_called()
        parse_mock.assert_not_called()

    def test_fixed_selection_and_old_unknowns(self):
        M.equal(self.payload["selection"], self.old_cal["selection"])
        M.equal(self.payload["selection"], self.old_later["selection"])
        self.assertEqual(
            self.payload["scope"]["old_900_status"], "UNKNOWN_TAIL_NOT_CONTRACTIVE"
        )
        self.assertEqual(
            self.payload["scope"]["old_2pow20_status"], "UNKNOWN_TAIL_NOT_CONTRACTIVE"
        )
        altered = copy.deepcopy(self.payload["selection"])
        altered["coordinate_indices"][0], altered["coordinate_indices"][1] = (
            altered["coordinate_indices"][1],
            altered["coordinate_indices"][0],
        )
        with self.assertRaises(M.Refusal):
            M.equal(altered, self.payload["selection"])

    def test_independent_small_alias_census(self):
        for maximum in (1, 2, 30, 100, 1024):
            literal = []
            for number in range(1, maximum + 1):
                rest = number
                for p in (2, 3, 5):
                    while rest % p == 0:
                        rest //= p
                if rest == 1:
                    literal.append(number)
            self.assertEqual(M.supported_aliases(maximum), literal)

    def test_complete_larger_exponent_box(self):
        values = M.supported_aliases(2**24)
        self.assertLessEqual(len(values), 25 * 16 * 11)
        self.assertEqual(values[-1], 2**24)
        present = set(values)
        self.assertIn(1, present)
        for number in values:
            for p in (2, 3, 5):
                if number * p <= 2**24:
                    self.assertIn(number * p, present)
        self.assertEqual(M.exponents(2**24), (24, 0, 0))
        self.assertEqual(M.exponents(3**15), (0, 15, 0))
        self.assertEqual(M.exponents(5**10), (0, 0, 10))

    def test_integer_type_support_and_cap_refusals(self):
        for value in (True, 1.0, "2", 0, 2**24 + 1):
            with self.assertRaises(M.Refusal):
                M.supported_aliases(value)
        with self.assertRaises(M.Refusal):
            M.exponents(7)
        with self.assertRaises(M.Refusal):
            M.validate_aliases([1, 2, 2], 2)
        with self.assertRaises(M.Refusal):
            M.validate_aliases([2, 1], 2)

    def test_stream_records_include_source_majorant_and_order(self):
        row = self.old_later["result"]["rows"][0]
        records = row["complete_aliases"]
        digest = M.stream_start(row["ratio"])
        for record in records:
            M.stream_record(digest, record)
        self.assertEqual(
            digest.hexdigest(),
            self.payload["result"]["rows"][0]["source_majorant_sha256"],
        )
        changed = copy.deepcopy(records)
        changed[0]["majorant_coordinates"][0] = "999"
        other = M.stream_start(row["ratio"])
        for record in changed:
            M.stream_record(other, record)
        self.assertNotEqual(digest.hexdigest(), other.hexdigest())
        reordered = M.stream_start(row["ratio"])
        for record in reversed(records):
            M.stream_record(reordered, record)
        self.assertNotEqual(digest.hexdigest(), reordered.hexdigest())

    def test_omitted_alias_and_false_prefix_cannot_match_calibration(self):
        altered = copy.deepcopy(self.old_later["result"])
        altered["rows"][0]["complete_aliases"].pop()
        with self.assertRaises(M.Refusal):
            M.equal(M.compact_prior(altered), self.payload["result"])
        altered = copy.deepcopy(self.old_later["result"])
        altered["rows"][0]["positive_prefix"][0] = "999"
        with self.assertRaises(M.Refusal):
            M.equal(M.compact_prior(altered), self.payload["result"])

    def test_literal_factor_two_and_original_alias_weight(self):
        # lambda2=-u/2, lambda3=-v/2 give curvature(1/2)du wedge dv.
        # lambda4=-1/2+3u/8, lambda6=uv/4 give(3u/16)du wedge dv.
        coordinates = list(self.helper.COORDINATES)
        constant = coordinates.index((0, 1, 0, 0, 0))
        u = coordinates.index((0, 1, 1, 0, 0))
        rows = []
        for g in (1, 2):
            values = [
                self.helper.local(k, a, b)
                for k, a, b in zip(
                    M.exponents(g), M.exponents(2), M.exponents(3), strict=True
                )
            ]
            rows.append([self.helper.source_coordinate(values, c) for c in coordinates])
        self.assertEqual(rows[0][constant], F(1, 2))
        self.assertEqual(rows[1][u], F(3, 16))
        self.assertEqual(rows[0][u] + rows[1][u] / 2, F(3, 32))
        self.assertNotEqual(rows[0][u] + rows[1][u], F(3, 32))

    def test_same_majorant_subtraction_and_both_inverse_products(self):
        result = self.payload["result"]
        for row in result["rows"]:
            self.assertEqual(
                [
                    M.rational(a) - M.rational(b)
                    for a, b in zip(
                        row["infinite_majorant_upper"],
                        row["positive_prefix"],
                        strict=True,
                    )
                ],
                [M.rational(x) for x in row["tail"]],
            )
            self.assertTrue(all(M.rational(x) >= 0 for x in row["tail"]))
        matrix = [[M.rational(x) for x in row] for row in result["matrix"]]
        inverse = [
            [M.rational(x) for x in row]
            for row in result["contraction"]["inverse"]["matrix"]
        ]
        identity = [[F(int(i == j)) for j in range(20)] for i in range(20)]
        self.assertEqual(self.helper.matrix_product(matrix, inverse), identity)
        self.assertEqual(self.helper.matrix_product(inverse, matrix), identity)

    def test_local_helpers_and_arithmetic_caps_unchanged(self):
        self.assertEqual(self.helper.LOCAL_CUTOFF, 64)

        def half(n):
            return F(1) if n == 0 else -F(comb(2 * n, n), 4**n * (2 * n - 1))

        b33, a24, b24 = half(33), half(12), half(24) - half(12)
        self.assertEqual(
            self.helper.local(24, 9, 0), (F(0), b33 * a24, b33 * b24, b33 * a24)
        )
        with self.assertRaises(ValueError):
            self.helper.local(65, 0, 0)
        with self.assertRaises(ValueError):
            self.helper.local_source(81)
        with self.assertRaises(ValueError):
            self.helper.exact(2**4096)
        with self.assertRaises(M.Refusal):
            M.rational(str(2**4096))

    def test_strict_contraction_boundary_and_singular_status(self):
        self.assertEqual(
            self.helper.contraction([[F(1)]], [[F(1)]])["status"],
            "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        )
        self.assertEqual(
            self.helper.contraction([[F(1)]], [[F(1, 2)]])["status"], "PASS"
        )
        self.assertEqual(
            self.helper.contraction([[F(0)]], [[F(1)]])["status"],
            "UNKNOWN_SINGULAR_MINOR",
        )

    def test_scope_does_not_promote_unknown_or_bridge_gap(self):
        scope = self.payload["scope"]
        self.assertTrue(scope["current_minor_rank20_certified"])
        self.assertFalse(scope["all_integer_horizons_at_or_above_target_certified"])
        self.assertIsNone(scope["effective_sufficient_threshold"])
        for key in (
            "first_faithful_horizon_claimed",
            "gap_901_to_extension_minus1_bridged",
            "all_integer_horizons_rank20_claimed",
            "new_energy_minimum_claimed",
            "native_gamma_decoder_claimed",
            "all_prime_completion_claimed",
        ):
            self.assertFalse(scope[key])
        forged = copy.deepcopy(self.payload["result"])
        forged["contraction"]["status"] = "PASS"
        forged["contraction"]["all_future_horizons_certified"] = True
        forged["contraction"]["theta"] = "1"
        with self.assertRaises(M.Refusal):
            M.scope(forged)

    def test_new_phase_requires_its_own_freeze_before_source(self):
        with patch.object(M, "source") as load:
            for phase, commit in (
                ("extension", None),
                ("calibration", "0" * 40),
                ("heldout", "0" * 40),
            ):
                with self.assertRaises(M.Refusal):
                    M.build(phase, commit)
        load.assert_not_called()

    def test_owned_code_change_blocks_new_calibration_gate(self):
        def fake_git(commit, path, expected=None, compare_current=True):
            if path == M.OWNED[0].relative_to(ROOT).as_posix():
                raise M.Refusal("changed new algorithm")
            return b"not parsed", {"commit": commit, "path": path, "blob": expected}

        with (
            patch.object(M, "git_bytes", side_effect=fake_git),
            patch("builtins.compile") as compile_mock,
            patch.object(M, "read_json") as parse_mock,
            self.assertRaises(M.Refusal),
        ):
            M.source("0" * 40)
        compile_mock.assert_not_called()
        parse_mock.assert_not_called()

    def test_typed_json_duplicates_and_rational_spellings(self):
        for raw in (b'{"n":1.0}', b'{"n":NaN}', b'{"n":1,"n":2}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        with self.assertRaises(M.Refusal):
            M.equal({"n": True}, {"n": 1})
        for value in (True, 1, "1.0", "2/2", "01"):
            with self.assertRaises(ValueError):
                M.rational(value)

    def test_body_digest_and_complete_canonical_record(self):
        M.body_check(self.payload)
        altered = copy.deepcopy(self.payload)
        altered["result"]["rows"][0]["source_majorant_sha256"] = "0" * 64
        with self.assertRaises(M.Refusal):
            M.body_check(altered)
        with self.assertRaises(M.Refusal):
            M.equal(altered, self.payload)

    def test_framed_stream_has_ratio_and_domain_identity(self):
        record = {
            "g": 1,
            "source_curvature": [[0, "1/2"]],
            "majorant_coordinates": ["1/2"] * 20,
        }
        left, right = M.stream_start([2, 3]), M.stream_start([3, 2])
        M.stream_record(left, record)
        M.stream_record(right, record)
        self.assertNotEqual(left.hexdigest(), right.hexdigest())
        raw = M.canonical(record).encode()
        self.assertEqual(json.loads(raw)["g"], 1)
        self.assertIn(b"\n", M.DOMAIN)


if __name__ == "__main__":
    unittest.main()

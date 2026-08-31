"""Separate original-row certification, actual maps and acceptance tests."""

import copy
import importlib.util
import unittest
from collections import Counter
from functools import lru_cache
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/row_restricted_resolution.py"
)
SPEC = importlib.util.spec_from_file_location("ternary_row_restricted_resolution", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


@lru_cache(maxsize=1)
def context():
    return R.verified_source()


def compose_polynomial_column(matrix, column):
    result = Counter()
    for outer in column["terms"]:
        for inner in matrix[outer["generator"]]["terms"]:
            exponent = tuple(
                a + b
                for a, b in zip(outer["S_exponent"], inner["S_exponent"], strict=True)
            )
            result[(inner["generator"], exponent)] += (
                outer["coefficient"] * inner["coefficient"]
            )
    return {key: value for key, value in result.items() if value}


class RowRestrictedActualMaps(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = context()
        cls.helper, cls.upstream = cls.source.helper, cls.source.upstream
        cls.payload = R.read_json(R.FIXTURE.read_bytes())
        cls.maps = cls.payload["result"]

    def test_frozen_presentation_and_acquired_degree_four_maps_preserved(self):
        self.assertEqual(
            self.maps["F0_generators"], self.source.presentation["generators"]
        )
        self.assertEqual(
            self.maps["D1_columns"], self.source.presentation["D1_columns"]
        )
        low = [c for c in self.maps["D2_columns"] if c["degree"] == 4]
        self.assertEqual(len(low), 65)
        self.assertEqual(
            R.digest(low), self.source.acquisition["D2_degree_four_columns_sha256"]
        )

    def test_complete_stage_five_cache_records_are_preserved(self):
        self.assertEqual(self.maps["stages"][:3], self.source.maps["stages"])
        self.assertEqual(self.maps["D2_columns"], self.source.maps["D2_columns"])
        self.assertEqual(self.maps["D3_columns"][:11], self.source.maps["D3_columns"])

    def test_exact_full_minimal_shift_lists(self):
        self.assertEqual(
            Counter(c["degree"] for c in self.maps["D2_columns"]), {4: 65, 5: 20}
        )
        self.assertEqual(
            Counter(c["degree"] for c in self.maps["D3_columns"]), {5: 11, 6: 17, 7: 1}
        )

    def test_every_D1_D2_polynomial_composition_independently(self):
        for column in self.maps["D2_columns"]:
            self.assertFalse(compose_polynomial_column(self.maps["D1_columns"], column))

    def test_every_D2_D3_polynomial_composition_independently(self):
        for column in self.maps["D3_columns"]:
            self.assertFalse(compose_polynomial_column(self.maps["D2_columns"], column))

    def test_changed_D2_coefficient_breaks_actual_composition(self):
        column = copy.deepcopy(self.maps["D2_columns"][0])
        column["terms"][0]["coefficient"] += 1
        self.assertTrue(compose_polynomial_column(self.maps["D1_columns"], column))

    def test_changed_D3_coefficient_breaks_actual_composition(self):
        column = copy.deepcopy(self.maps["D3_columns"][-1])
        column["terms"][0]["coefficient"] += 1
        self.assertTrue(compose_polynomial_column(self.maps["D2_columns"], column))

    def test_all_entries_are_minimal_and_weight_homogeneous(self):
        for source, target in (
            (self.maps["D2_columns"], self.maps["D1_columns"]),
            (self.maps["D3_columns"], self.maps["D2_columns"]),
        ):
            for column in source:
                for term in column["terms"]:
                    generator = target[term["generator"]]
                    exponent = term["S_exponent"]
                    self.assertGreater(sum(exponent), 0)
                    self.assertEqual(
                        sum(exponent) + generator["degree"], column["degree"]
                    )
                    self.assertEqual(
                        self.helper.add(
                            self.helper.polynomial_weight(exponent), generator["weight"]
                        ),
                        tuple(column["weight"]),
                    )

    def test_complete_dual_weight_tables(self):
        for grade in (4, 5):
            current = [c for c in self.maps["D2_columns"] if c["degree"] == grade]
            self.assertTrue(
                self.upstream.weight_check(current, self.maps["D1_columns"], 7 - grade)[
                    "complete_match"
                ]
            )
        for grade in (5, 6, 7):
            current = [c for c in self.maps["D3_columns"] if c["degree"] == grade]
            self.assertTrue(
                self.upstream.weight_check(
                    current, self.maps["F0_generators"], 7 - grade
                )["complete_match"]
            )

    def test_degree_five_D3_does_not_use_degree_five_D2_targets(self):
        for column in self.maps["D3_columns"][:11]:
            self.assertTrue(
                all(
                    self.maps["D2_columns"][term["generator"]]["degree"] == 4
                    for term in column["terms"]
                )
            )

    def test_actual_old_rank_639_not_assigned_column_count_650(self):
        row = self.maps["stages"][1]
        quotient = row["minimal_quotient"]
        self.assertEqual(len(quotient["actual_old_columns_in_current_domain"]), 650)
        self.assertEqual(
            (quotient["actual_old_rank"], quotient["new_quotient_dimension"]), (639, 20)
        )
        self.assertEqual(row["evaluation"]["nullity"], 659)

    def test_later_old_quotients_retain_every_monomial_multiple(self):
        for row, count, new in zip(
            self.maps["stages"][3:], (110, 775), (17, 1), strict=True
        ):
            quotient = row["minimal_quotient"]
            self.assertEqual(len(quotient["old_multiple_domain_basis"]), count)
            self.assertEqual(
                len(quotient["actual_old_columns_in_current_domain"]), count
            )
            self.assertEqual(
                (quotient["actual_old_rank"], quotient["new_quotient_dimension"]),
                (count, new),
            )

    def test_every_kernel_witness_and_declared_domain_is_retained(self):
        expected = [
            ("D1", 4, 1750, 65),
            ("D1", 5, 7975, 659),
            ("D2", 5, 670, 11),
            ("D2", 6, 3775, 127),
            ("D2", 7, 15400, 776),
        ]
        actual = []
        for row in self.maps["stages"]:
            value = row["evaluation"]
            actual.append(
                (row["map"], value["grade"], value["domain_columns"], value["nullity"])
            )
            self.assertEqual(
                len(value["full_original_coordinate_kernel_basis"]), value["nullity"]
            )
            self.assertEqual(
                sum(b["nullity"] for b in value["weight_blocks"]), value["nullity"]
            )
            self.assertEqual(value["rank"] + value["nullity"], value["domain_columns"])
        self.assertEqual(actual, expected)

    def test_ordered_basis_descriptors_reconstruct_full_modules(self):
        for row in self.maps["stages"]:
            value = row["evaluation"]
            target = (
                self.maps["F0_generators"]
                if row["map"] == "D1"
                else self.maps["D1_columns"]
            )
            domain = (
                self.maps["D1_columns"]
                if row["map"] == "D1"
                else self.maps["D2_columns"]
            )
            target_basis = self.helper.module_basis(target, value["grade"])
            domain_basis = self.helper.module_basis(domain, value["grade"])
            self.assertEqual(len(target_basis), value["full_target_rows"])
            self.assertEqual(
                self.upstream.digest_rows(target_basis), value["target_basis_sha256"]
            )
            self.assertEqual(
                self.upstream.digest_rows(domain_basis), value["domain_basis_sha256"]
            )

    def test_proof_object_and_distinct_contract_scope(self):
        body = {k: v for k, v in self.payload.items() if k != "proof_object_sha256"}
        self.assertEqual(R.digest(body), self.payload["proof_object_sha256"])
        self.assertEqual(self.payload["cache_provenance"], self.source.cache_provenance)
        self.assertEqual(self.payload["owned_sha256_lf"], R.owned_bindings())
        self.assertFalse(
            self.payload["row_restriction_contract"]["old_26_test_contract_replaced"]
        )
        self.assertTrue(self.maps["complete_resolution_constructed"])
        self.assertFalse(self.maps["marked_basis_is_GL3_equivariant"])
        self.assertTrue(self.maps["independent_global_exactness_proof_required"])


class RowRestrictedSourceAcceptance(unittest.TestCase):
    def test_authentication_precedes_any_compilation(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("changed freeze")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaisesRegex(ValueError, "changed freeze"):
                R.load_frozen()
            compiler.assert_not_called()

    def test_missing_exact_cache_freeze_refuses_execution(self):
        with (
            patch.object(R, "CACHE_FREEZE", None),
            patch.object(R.subprocess, "check_output") as process,
        ):
            with self.assertRaisesRegex(ValueError, "exact freeze"):
                R.authenticate()
            process.assert_not_called()

    def test_wrong_frozen_blob_fails_before_cache_interpretation(self):
        with (
            patch.object(R, "CACHE_FREEZE", "0" * 40),
            patch.object(R, "CACHE_PINS", {"missing": "1" * 40}),
            patch.object(R.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaisesRegex(ValueError, "certified cache source mismatch"),
        ):
            R.authenticate()

    def test_cache_verification_cannot_be_skipped(self):
        verifier = Mock()
        verifier.verify_cache.side_effect = ValueError("invalid kernel witness")
        with patch.object(R, "load_frozen", return_value=(verifier, {}, {})):
            with self.assertRaisesRegex(ValueError, "invalid kernel witness"):
                R.verified_source()
            verifier.source.assert_not_called()

    def test_build_routes_only_through_verified_source_and_continuation(self):
        sentinel = object()
        with (
            patch.object(R, "verified_source", return_value=sentinel) as verified,
            patch.object(
                R, "extend_maps", side_effect=ValueError("continuation reached")
            ) as extended,
        ):
            with self.assertRaisesRegex(ValueError, "continuation reached"):
                R.build_maps(6)
            verified.assert_called_once_with()
            extended.assert_called_once_with(sentinel, 6, R.DIRECTORY)

    def test_stage_types_rejected_before_source_loading(self):
        with patch.object(R, "verified_source") as source:
            for bad in (True, 6.0, 5, 8):
                with self.assertRaises(ValueError):
                    R.build_maps(bad)
            source.assert_not_called()

    def test_original_coordinate_kernel_and_cap_are_unchanged(self):
        source = context()
        evaluation = {
            "grade": 4,
            "columns": [{0: 2, 1: 1}, {0: 6, 1: 3}, {1: 1}],
            "weights": [(4, 4, 4)] * 3,
        }
        relations, _, stats = source.upstream.kernel(source.helper, evaluation)
        self.assertEqual(relations, [{0: -3, 1: 1}])
        self.assertEqual((stats[0]["rank"], stats[0]["nullity"]), (2, 1))
        large = {"grade": 6, "columns": [{0: 1}] * 513, "weights": [(6, 6, 6)] * 513}
        with self.assertRaisesRegex(ValueError, "preflight weight-block cap"):
            source.upstream.kernel(source.helper, large)

    def test_old_span_retains_actual_dependence(self):
        source = context()
        span = source.upstream.Span(source.helper)
        self.assertTrue(span.add({0: 2, 1: 3}))
        self.assertFalse(span.add({0: 4, 1: 6}))
        self.assertTrue(span.add({1: 1}))
        self.assertEqual(len(span.pivots), 2)

    def test_numeric_aliases_and_unchanged_hash_are_rejected(self):
        good = {"rank": 1, "complete": True, "proof_object_sha256": "old"}
        for key, value in (("rank", True), ("rank", 1.0), ("complete", 1)):
            bad = dict(good)
            bad[key] = value
            with self.assertRaises(ValueError):
                R.check_payload(bad, good)

    def test_strict_input_rejects_duplicates_floats_and_nonfinite(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}', b'{"a":Infinity}'):
            with self.assertRaises(ValueError):
                R.read_json(raw)

    def test_nonfinite_containers_and_coverage_counterfeits_fail(self):
        for bad in (
            {"rank": float("nan")},
            {"rank": float("inf")},
            {"rank": (1,)},
            {},
            {"rank": 1, "extra": 0},
        ):
            with self.assertRaises(ValueError):
                R.check_payload(bad, {"rank": 1})


class OriginalRowCertification(unittest.TestCase):
    """Bounded controls runnable before either higher-degree acquisition."""

    @classmethod
    def setUpClass(cls):
        cls.source = context()
        cls.weight = (6, 6, 6)

    def evaluation(self, columns):
        size = max((row for column in columns for row in column), default=-1) + 1
        return {
            "grade": 6,
            "target_basis": [[i] for i in range(size)],
            "domain_basis": [[i] for i in range(len(columns))],
            "columns": columns,
            "weights": [self.weight] * len(columns),
        }

    def attempt(self, columns, modulus=65521):
        return R.fresh_attempt(self.source, columns, self.weight, 6, modulus)

    def test_selected_rows_are_literal_original_rows(self):
        columns = [{2: 2, 9: 4, 20: 1}, {2: 6, 9: 12, 20: 3}, {20: 1}]
        attempt, vectors = self.attempt(columns)
        self.assertEqual(attempt["row_selection"]["selected_original_rows"], [2, 20])
        self.assertEqual(vectors, [{0: -3, 1: 1}])
        self.assertTrue(attempt["certificate"]["full_and_restricted_kernels_equal"])

    def test_full_600_rows_pass_only_new_preflight(self):
        columns = [{i: i + 1 for i in range(600)}, {i: 3 * (i + 1) for i in range(600)}]
        evaluation = self.evaluation(columns)
        self.assertEqual(
            R.preflight_full(self.source.upstream, evaluation)[0]["rows"], 600
        )
        with self.assertRaisesRegex(ValueError, "preflight weight-block cap"):
            self.source.upstream.preflight(evaluation)
        attempt, vectors = self.attempt(columns)
        self.assertEqual(vectors, [{0: -3, 1: 1}])
        self.assertEqual(attempt["row_selection"]["selected_original_rows"], [0])
        self.assertTrue(attempt["certificate"]["every_full_original_row_checked"])

    def test_bad_first_prime_retains_full_residual_then_fallback(self):
        evaluation = self.evaluation([{0: 65521}, {1: 1}])
        with TemporaryDirectory() as directory:
            vectors, _, stats, certificates = R.certified_kernel(
                self.source, evaluation, directory
            )
        self.assertEqual(vectors, [])
        self.assertEqual(stats[0]["successful_modulus"], 1000003)
        attempts = certificates[0]["attempts"]
        self.assertEqual(
            [a["row_selection"]["modulus"] for a in attempts], [65521, 1000003]
        )
        self.assertEqual(
            attempts[0]["certificate"]["full_composition_failures"],
            [{"kernel_vector": 0, "full_original_residual": [[0, 65521]]}],
        )
        self.assertFalse(
            attempts[0]["certificate"]["full_and_restricted_kernels_equal"]
        )
        self.assertTrue(attempts[1]["certificate"]["full_and_restricted_kernels_equal"])

    def test_zero_modular_rank_is_not_assumed_zero_rational_rank(self):
        attempt, vectors = self.attempt([{0: 65521}, {1: 65521}])
        self.assertEqual(attempt["row_selection"]["modular_row_rank"], 0)
        self.assertEqual(vectors, [{0: 1}, {1: 1}])
        self.assertEqual(len(attempt["certificate"]["full_composition_failures"]), 2)

    def test_both_bad_primes_leave_failure_but_no_completed_block(self):
        evaluation = self.evaluation([{0: 65521 * 1000003}, {1: 1}])
        with TemporaryDirectory() as directory:
            with self.assertRaisesRegex(
                ValueError, "both fixed row-selection moduli failed"
            ):
                R.certified_kernel(self.source, evaluation, directory)
            paths = list(Path(directory).glob("*.json"))
            self.assertEqual(len(paths), 1)
            self.assertTrue(paths[0].name.endswith(".failure.json"))
            payload = R.read_json(paths[0].read_bytes())
            self.assertEqual(payload["status"], "FIXED_MODULI_FAILED")
            self.assertEqual(len(payload["attempts"]), 2)
            self.assertTrue(
                all(
                    a["certificate"]["full_composition_failures"]
                    for a in payload["attempts"]
                )
            )

    def test_missing_kernel_vector_fails_dimension_completeness(self):
        columns = [{0: 1}, {0: 2}, {0: 3}]
        attempt, _ = self.attempt(columns)
        attempt["restricted_kernel"].pop()
        with self.assertRaisesRegex(ValueError, "complete restricted kernel dimension"):
            R.certify_attempt(
                self.source.verifier, self.source.helper, columns, self.weight, attempt
            )

    def test_duplicate_kernel_vectors_fail_independence(self):
        columns = [{0: 1}, {0: 2}, {0: 3}]
        attempt, _ = self.attempt(columns)
        attempt["restricted_kernel"][1] = copy.deepcopy(attempt["restricted_kernel"][0])
        with self.assertRaisesRegex(ValueError, "triangular independence"):
            R.certify_attempt(
                self.source.verifier, self.source.helper, columns, self.weight, attempt
            )

    def test_kernel_coefficient_corruption_fails_actual_composition(self):
        columns = [{0: 1}, {0: 2}]
        attempt, _ = self.attempt(columns)
        attempt["restricted_kernel"][0][0][1] = -3
        with self.assertRaisesRegex(
            ValueError, "actual restricted kernel compositions"
        ):
            R.certify_attempt(
                self.source.verifier, self.source.helper, columns, self.weight, attempt
            )

    def test_selected_row_numeric_aliases_are_rejected(self):
        columns = [{0: 1}, {0: 2}]
        for alias in (False, 0.0):
            attempt, _ = self.attempt(columns)
            attempt["row_selection"]["selected_original_rows"][0] = alias
            with self.assertRaises(ValueError):
                R.certify_attempt(
                    self.source.verifier,
                    self.source.helper,
                    columns,
                    self.weight,
                    attempt,
                )

    def test_reused_completed_block_rechecks_without_rational_kernel(self):
        evaluation = self.evaluation([{0: 1, 1: 2}, {0: 3, 1: 6}])
        with TemporaryDirectory() as directory:
            first = R.certified_kernel(self.source, evaluation, directory)
            with patch.object(
                self.source.upstream, "kernel", side_effect=AssertionError("must reuse")
            ):
                second = R.certified_kernel(self.source, evaluation, directory)
        R.check_payload(first, second)

    def test_checkpoint_source_binding_cannot_be_replaced_even_with_new_digest(self):
        evaluation = self.evaluation([{0: 1}, {0: 2}])
        with TemporaryDirectory() as directory:
            R.certified_kernel(self.source, evaluation, directory)
            path = next(Path(directory).glob("*.json"))
            payload = R.read_json(path.read_bytes())
            payload["input"]["ownership"]["algorithm_sha256_lf"] = "0" * 64
            payload["proof_object_sha256"] = R.digest(
                {
                    key: value
                    for key, value in payload.items()
                    if key != "proof_object_sha256"
                }
            )
            R.write_atomic(path, payload)
            with self.assertRaises(ValueError):
                R.certified_kernel(self.source, evaluation, directory)

    def test_checkpoint_does_not_accept_false_full_composition_flag(self):
        evaluation = self.evaluation([{0: 1}, {0: 2}])
        with TemporaryDirectory() as directory:
            R.certified_kernel(self.source, evaluation, directory)
            path = next(Path(directory).glob("*.json"))
            payload = R.read_json(path.read_bytes())
            payload["attempts"][0]["certificate"]["every_full_original_row_checked"] = 1
            payload["proof_object_sha256"] = R.digest(
                {
                    key: value
                    for key, value in payload.items()
                    if key != "proof_object_sha256"
                }
            )
            R.write_atomic(path, payload)
            with self.assertRaises(ValueError):
                R.certified_kernel(self.source, evaluation, directory)

    def test_incomplete_temporary_files_are_never_reused(self):
        evaluation = self.evaluation([{0: 1}, {0: 2}])
        with TemporaryDirectory() as directory:
            (Path(directory) / "interrupted.json.tmp").write_bytes(b'{"partial":')
            result = R.certified_kernel(self.source, evaluation, directory)
            self.assertEqual(result[0], [{0: -2, 1: 1}])
            self.assertEqual(len(list(Path(directory).glob("*.json"))), 1)

    def test_caps_and_literal_weights_checked_before_group_aliasing(self):
        for columns in ([{0: 1}] * 513, [{i: 1 for i in range(4097)}]):
            with self.assertRaisesRegex(ValueError, "new full weight-block cap"):
                R.preflight_full(self.source.upstream, self.evaluation(columns))
        evaluation = self.evaluation([{0: 1}, {0: 2}])
        evaluation["weights"][1] = (6.0, 6, 6)
        with self.assertRaisesRegex(
            ValueError, "literal source weights before grouping"
        ):
            R.preflight_full(self.source.upstream, evaluation)

    def test_input_coefficient_bit_cap_precedes_checkpoint_work(self):
        evaluation = self.evaluation([{0: 1 << 4096}])
        with TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "bit cap"):
                R.certified_kernel(self.source, evaluation, directory)
            self.assertFalse(list(Path(directory).iterdir()))

    def test_nonfixed_modulus_and_atomic_byte_cap_are_rejected(self):
        for modulus in (True, 65521.0, 7):
            with self.assertRaises(ValueError):
                R.select_original_rows([{0: 1}], modulus)
        with TemporaryDirectory() as directory, patch.object(R, "MAX_BYTES", 7):
            with self.assertRaisesRegex(ValueError, "byte cap"):
                R.write_atomic(Path(directory) / "too-large.json", {"a": 1})
            self.assertFalse((Path(directory) / "too-large.json").exists())


if __name__ == "__main__":
    unittest.main()

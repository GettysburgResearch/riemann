"""Small exact controls for durable source maps and rational-rank certificates."""

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/resolution_stage5_cache.py"
)
SPEC = importlib.util.spec_from_file_location("segre_stage5_cache", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ModularCertificates(unittest.TestCase):
    def test_declared_moduli_are_primes(self):
        self.assertTrue(all(R.is_prime(p) for p in R.MODULI))
        self.assertFalse(R.is_prime(65520))

    def test_finite_field_rank_is_only_a_lower_bound(self):
        matrix = [{0: 65521}]
        self.assertEqual(R.modular_rank(matrix, 65521)["rank"], 0)
        self.assertEqual(R.modular_rank(matrix, 1000003)["rank"], 1)

    def test_actual_independence_and_original_column_indices(self):
        matrix = [{0: 1, 2: 3}, {0: 2, 2: 6}, {1: 1}]
        result = R.modular_rank(matrix, 65521)
        self.assertEqual(result["rank"], 2)
        self.assertEqual(result["independent_local_column_indices"], [0, 2])

    def test_fixed_moduli_caps_and_literal_integer_entries(self):
        for modulus in (True, 65521.0, 65520):
            with self.assertRaises(ValueError):
                R.modular_rank([{0: 1}], modulus)
        for matrix in ([{0: True}], [{0: 1.0}], [{0: 1}] * 513):
            with self.assertRaises(ValueError):
                R.modular_rank(matrix, 65521)


class RationalKernelCompleteness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upstream, _, _ = R.source()
        cls.helper, _, _, _ = cls.upstream.source()

    def model(self):
        zero = (0,) * 10
        evaluation = {
            "grade": 4,
            "target_basis": ((0, zero),),
            "domain_basis": ((0, zero), (1, zero), (2, zero)),
            "columns": [{0: 1}, {0: 2}, {0: 3}],
            "weights": [(4, 4, 4)] * 3,
        }
        relations = [{0: -2, 1: 1}, {0: -3, 2: 1}]
        stats = [
            {
                "weight": (4, 4, 4),
                "rows": 1,
                "columns": 3,
                "rank": 1,
                "nullity": 2,
                "max_exact_bits": 2,
            }
        ]
        record = R.normalized(
            self.upstream.evaluation_record(evaluation, stats, relations)
        )
        return evaluation, record

    def test_independent_integer_kernel_plus_modular_lower_bound_is_complete(self):
        evaluation, record = self.model()
        relations, weights, certificate = R.certify_kernel(
            self.upstream, self.helper, evaluation, record
        )
        self.assertEqual(len(relations), 2)
        self.assertEqual(weights, [(4, 4, 4)] * 2)
        self.assertEqual(certificate["rank"], 1)
        self.assertTrue(certificate["independence_by_distinct_largest_coordinates"])

    def test_forged_dimensions_do_not_certify_an_incomplete_kernel(self):
        evaluation, record = self.model()
        record["full_original_coordinate_kernel_basis"].pop()
        record["nullity"], record["rank"] = 1, 2
        record["weight_blocks"][0]["nullity"] = 1
        record["weight_blocks"][0]["rank"] = 2
        with self.assertRaisesRegex(ValueError, "declared primes"):
            R.certify_kernel(self.upstream, self.helper, evaluation, record)

    def test_actual_composition_is_checked_before_dimensions(self):
        evaluation, record = self.model()
        record["full_original_coordinate_kernel_basis"][0][0][1] = -3
        with self.assertRaisesRegex(ValueError, "nonzero actual composition"):
            R.certify_kernel(self.upstream, self.helper, evaluation, record)

    def test_repeated_largest_coordinate_cannot_fake_independence(self):
        evaluation, record = self.model()
        record["full_original_coordinate_kernel_basis"][1] = copy.deepcopy(
            record["full_original_coordinate_kernel_basis"][0]
        )
        with self.assertRaisesRegex(ValueError, "independence witness duplicated"):
            R.certify_kernel(self.upstream, self.helper, evaluation, record)

    def test_actual_basis_digest_and_sparse_integer_types_are_bound(self):
        evaluation, record = self.model()
        record["domain_basis_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            R.certify_kernel(self.upstream, self.helper, evaluation, record)
        for raw in ([[0, True]], [[0, 1.0]], [[0, 1], [0, 2]], [[0, -1]]):
            with self.assertRaises(ValueError):
                R.parse_vector(raw, 3, self.helper)

    def test_block_weight_labels_reject_coercible_numeric_aliases(self):
        for replacement in (4.0, True, "4"):
            evaluation, record = self.model()
            record["weight_blocks"][0]["weight"][0] = replacement
            with self.assertRaisesRegex(
                ValueError, "literal integer cached block weight"
            ):
                R.certify_kernel(self.upstream, self.helper, evaluation, record)


class DurableAcceptance(unittest.TestCase):
    def test_authentication_precedes_compilation(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("source changed")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaises(ValueError):
                R.source()
            compiler.assert_not_called()

    def test_cache_replays_verification_with_strict_numeric_types(self):
        payload = {
            "schema": "ternary-stage5-certified-cache-v1",
            "candidate": {},
            "verification": {"rank": 1},
            "requires_exact_frozen_blob_before_continuation": True,
        }
        payload["proof_object_sha256"] = R.digest(payload)
        with patch.object(R, "verify_candidate", return_value={"rank": 1}):
            R.verify_cache(json.loads(json.dumps(payload)))
            for replacement in (True, 1.0):
                changed = copy.deepcopy(payload)
                changed["verification"]["rank"] = replacement
                changed["proof_object_sha256"] = R.digest(
                    {k: v for k, v in changed.items() if k != "proof_object_sha256"}
                )
                with self.assertRaises(ValueError):
                    R.verify_cache(changed)

    def test_body_digest_nonfinite_and_scope_counterfeits(self):
        payload = {
            "schema": "ternary-stage5-certified-cache-v1",
            "candidate": {},
            "verification": {},
            "requires_exact_frozen_blob_before_continuation": True,
        }
        payload["proof_object_sha256"] = R.digest(payload)
        bad = copy.deepcopy(payload)
        bad["requires_exact_frozen_blob_before_continuation"] = 1
        with self.assertRaises(ValueError):
            R.verify_cache(bad)
        bad = copy.deepcopy(payload)
        bad["verification"]["unverified"] = True
        with self.assertRaises(ValueError):
            R.verify_cache(bad)
        for value in (float("nan"), float("inf"), (1, 2)):
            with self.assertRaises(ValueError):
                R.canonical({"x": value})


if __name__ == "__main__":
    unittest.main()

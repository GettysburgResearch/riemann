"""Resumable exact weight blocks without trusting cached dimensions."""

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/resolution_blockwise_acquire.py"
)
SPEC = importlib.util.spec_from_file_location("ternary_blockwise", PATH)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class ExactDurableBlocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verifier, cls.upstream, _, _, cls.provenance = R.source()
        cls.helper, _, _, _ = cls.upstream.source()

    def model(self):
        zero = (0,) * 10
        return {
            "grade": 4,
            "target_basis": ((0, zero), (1, zero)),
            "domain_basis": tuple((i, zero) for i in range(5)),
            "columns": [{0: 1}, {1: 1}, {0: 2}, {1: 3}, {0: 3}],
            "weights": [(4, 4, 4), (3, 4, 5), (4, 4, 4), (3, 4, 5), (4, 4, 4)],
        }

    def run_blocks(self, directory, kernel=None, ownership=None):
        manifest = []
        result = R.blockwise_kernel(
            self.verifier,
            self.upstream,
            self.upstream.kernel if kernel is None else kernel,
            self.helper,
            self.model(),
            {"test_source": 1} if ownership is None else ownership,
            manifest,
            directory,
        )
        return result, manifest

    def test_exact_frozen_verifier_and_three_source_pins(self):
        self.assertEqual(len(self.provenance), 3)
        self.assertEqual(self.verifier.MODULI, (65521, 1000003))
        self.assertEqual(self.upstream.MAX_BLOCK, 512)

    def test_restricted_kernel_translates_nonconsecutive_original_indices(self):
        expected = self.upstream.kernel(self.helper, self.model())
        with tempfile.TemporaryDirectory() as directory:
            actual, manifest = self.run_blocks(Path(directory))
        self.assertEqual(R.normalized(actual), R.normalized(expected))
        self.assertIn({0: -2, 2: 1}, actual[0])
        self.assertIn({1: -3, 3: 1}, actual[0])
        self.assertEqual(len(manifest), 2)

    def test_completed_blocks_reused_without_rational_kernel_call(self):
        with tempfile.TemporaryDirectory() as directory:
            first, _ = self.run_blocks(Path(directory))
            forbidden = Mock(side_effect=AssertionError("rational kernel rerun"))
            second, manifest = self.run_blocks(Path(directory), forbidden)
        self.assertEqual(R.normalized(first), R.normalized(second))
        self.assertTrue(all(row["reused"] for row in manifest))
        forbidden.assert_not_called()

    def test_changed_source_ownership_uses_new_checkpoint_keys(self):
        with tempfile.TemporaryDirectory() as directory:
            _, old = self.run_blocks(Path(directory))
            counter = Mock(wraps=self.upstream.kernel)
            _, new = self.run_blocks(Path(directory), counter, {"test_source": 2})
        self.assertEqual(counter.call_count, 2)
        self.assertTrue(
            {row["key"] for row in old}.isdisjoint(row["key"] for row in new)
        )

    def test_incomplete_temporary_file_is_not_a_completed_block(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / ("0" * 64 + ".json.tmp")).write_bytes(b"incomplete")
            _, manifest = self.run_blocks(path)
        self.assertFalse(any(row["reused"] for row in manifest))

    def block(self):
        evaluation = self.model()
        weight, indices = (4, 4, 4), [0, 2, 4]
        identity = R.matrix_identity(self.upstream, evaluation)
        input_record = R.block_input(
            self.upstream, evaluation, identity, weight, indices, {"test": True}
        )
        columns = [evaluation["columns"][i] for i in indices]
        relations, _, stats = self.upstream.kernel(
            self.helper, {"grade": 4, "columns": columns, "weights": [weight] * 3}
        )
        output = R.normalized(
            {
                "local_kernel": [self.upstream.sparse(vector) for vector in relations],
                "stat": stats[0],
            }
        )
        _, certificate = R.certify_output(
            self.verifier, self.helper, columns, weight, output
        )
        return (
            columns,
            weight,
            input_record,
            R.make_checkpoint(input_record, output, certificate),
        )

    def test_checkpoint_rechecks_actual_compositions(self):
        columns, weight, record, payload = self.block()
        payload["output"]["local_kernel"][0][0][1] -= 1
        payload["proof_object_sha256"] = R.digest(
            {k: v for k, v in payload.items() if k != "proof_object_sha256"}
        )
        with self.assertRaisesRegex(ValueError, "nonzero actual composition"):
            R.check_checkpoint(
                payload, record, self.verifier, self.helper, columns, weight
            )

    def test_forged_rank_cannot_replace_missing_kernel_vector(self):
        columns, weight, record, payload = self.block()
        payload["output"]["local_kernel"].pop()
        payload["output"]["stat"]["rank"] = 2
        payload["output"]["stat"]["nullity"] = 1
        payload["proof_object_sha256"] = R.digest(
            {k: v for k, v in payload.items() if k != "proof_object_sha256"}
        )
        with self.assertRaisesRegex(ValueError, "fixed primes"):
            R.check_checkpoint(
                payload, record, self.verifier, self.helper, columns, weight
            )

    def test_repeated_peak_fails_kernel_independence(self):
        columns, weight, _, payload = self.block()
        output = payload["output"]
        output["local_kernel"][1] = copy.deepcopy(output["local_kernel"][0])
        with self.assertRaisesRegex(ValueError, "triangular kernel independence"):
            R.certify_output(self.verifier, self.helper, columns, weight, output)

    def test_source_matrix_and_checkpoint_status_are_bound(self):
        columns, weight, record, payload = self.block()
        wrong = copy.deepcopy(record)
        wrong["matrix"]["grade"] = 5
        with self.assertRaisesRegex(ValueError, "source/matrix"):
            R.check_checkpoint(
                payload, wrong, self.verifier, self.helper, columns, weight
            )
        payload["status"] = "INCOMPLETE"
        with self.assertRaisesRegex(ValueError, "completed blocks"):
            R.check_checkpoint(
                payload, record, self.verifier, self.helper, columns, weight
            )

    def test_literal_numeric_metadata_is_preserved(self):
        columns, weight, _, payload = self.block()
        for key, value in (("rank", True), ("rank", 1.0), ("weight", [4.0, 4, 4])):
            output = copy.deepcopy(payload["output"])
            output["stat"][key] = value
            with self.assertRaises(ValueError):
                R.certify_output(self.verifier, self.helper, columns, weight, output)

    def test_atomic_replace_failure_never_creates_final_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            with patch.object(
                R.os, "replace", side_effect=OSError("simulated reserve termination")
            ), self.assertRaises(OSError):
                R.write_checkpoint(path, {"complete": True})
            self.assertFalse(path.exists())
            self.assertTrue(path.with_suffix(".json.tmp").is_file())


class BlockwiseSourceAcceptance(unittest.TestCase):
    def test_authentication_precedes_compilation(self):
        with (
            patch.object(R, "authenticate", side_effect=ValueError("source changed")),
            patch("builtins.compile") as compiler,
        ):
            with self.assertRaises(ValueError):
                R.source()
            compiler.assert_not_called()

    def test_wrong_git_object_rejected(self):
        with (
            patch.object(R, "PINS", {"missing": "1" * 40}),
            patch.object(R.subprocess, "check_output", return_value="wrong\n"),
            self.assertRaisesRegex(ValueError, "verifier mismatch"),
        ):
            R.authenticate()

    def test_strict_checkpoint_parser_rejects_aliases_and_duplicate_keys(self):
        for raw in (b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}'):
            with self.assertRaises(ValueError):
                R.read_json(raw)
        with self.assertRaises(ValueError):
            R.equal({"rank": True}, {"rank": 1}, "typed rank")


if __name__ == "__main__":
    unittest.main()

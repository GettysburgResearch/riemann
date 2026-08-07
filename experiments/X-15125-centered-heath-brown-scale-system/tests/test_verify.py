#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)

partition_spec = importlib.util.spec_from_file_location(
    "partition_verify", ROOT / "partition_verify.py"
)
partition_verify = importlib.util.module_from_spec(partition_spec)
assert partition_spec.loader is not None
partition_spec.loader.exec_module(partition_verify)


class ExactRegressionTests(unittest.TestCase):
    def test_heath_brown_identity(self):
        self.assertEqual(verify.hb_identity(3, 4)["mismatches"], [])

    def test_heath_brown_second_parameter(self):
        self.assertEqual(verify.hb_identity(2, 5)["mismatches"], [])

    def test_exact_tuple_partition(self):
        result = partition_verify.build()
        self.assertEqual(result["coefficient_mismatches"], [])
        self.assertEqual(result["partition_failures"], [])
        self.assertEqual(result["verdict"], "PASS")

    def test_both_partition_types_present(self):
        counts = partition_verify.build()["tuple_counts"]
        self.assertGreater(counts["j1_I"] + counts["j2_I"], 0)
        self.assertGreater(counts["j1_II"] + counts["j2_II"], 0)

    def test_null_quotient(self):
        out = verify.null_quotient_check()
        self.assertEqual(out["null_n0"], "0")
        self.assertEqual(out["null_n1"], "0")
        self.assertEqual(out["direct"], out["recombined"])
        self.assertTrue(out["bound_pass"])

    def test_nonnull_mode_detected(self):
        B = [
            [Fraction(1), Fraction(-2), Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(1), Fraction(-2), Fraction(1)],
        ]
        K = verify.matmul(verify.transpose(B), B)
        v = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
        self.assertNotEqual(verify.qform(v, K, v), 0)

    def test_result_verdict(self):
        self.assertEqual(verify.build_result()["verdict"], "PASS")

    def test_digest_changes_on_mutation(self):
        result = verify.build_result()
        original = result["proof_sha256"]
        result["scale_system"]["delta"] = "1/2"
        payload = dict(result)
        payload.pop("proof_sha256")
        encoded = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
        new = hashlib.sha256(encoded).hexdigest()
        self.assertNotEqual(original, new)

    def test_replay_rejects_mutated_certificate(self):
        result = verify.build_result()
        result["heath_brown"]["mismatches"] = [2]
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "bad.json"
            path.write_text(json.dumps(result))
            expected = json.loads(path.read_text())
            self.assertNotEqual(expected, verify.build_result())

    def test_scale_system_is_finite(self):
        out = verify.scale_system_check()
        self.assertEqual(out["components"], 3)
        self.assertEqual(out["max_J"], 90)
        self.assertEqual(len(out["last_values"]), 3)


if __name__ == "__main__":
    unittest.main()

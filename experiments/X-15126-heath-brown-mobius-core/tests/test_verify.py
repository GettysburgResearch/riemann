#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class ExactMobiusCoreTests(unittest.TestCase):
    def test_three_cases_pass(self):
        for K, V in [(2, 5), (3, 4), (4, 3)]:
            case = verify.verify_case(K, V)
            self.assertEqual(case["inverse_mismatches"], [])
            self.assertEqual(case["lambda_mismatches"], [])
            self.assertEqual(case["q2_slice_mismatches"], [])

    def test_result_verdict(self):
        self.assertEqual(verify.build_result()["verdict"], "PASS")

    def test_wrong_last_binomial_sign_fails(self):
        K, V = 3, 4
        X = V**K
        bad = verify.packet_inverse(K, V, X, mutate_sign=True)
        mu = verify.mobius_table(X)
        self.assertTrue(any(bad[n] != mu[n] for n in range(1, X + 1)))

    def test_q2_slice_is_nontrivial(self):
        case = verify.verify_case(3, 4)
        self.assertEqual(case["q2_slice_mismatches"], [])
        self.assertGreater(case["X"] // 2, 1)

    def test_digest_changes_on_mutation(self):
        result = verify.build_result()
        original = result["proof_sha256"]
        result["cases"][0]["sample_A"]["2"] += 1
        payload = dict(result)
        payload.pop("proof_sha256")
        mutated = hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertNotEqual(original, mutated)

    def test_expected_certificate_replay(self):
        result = verify.build_result()
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "result.json"
            path.write_text(json.dumps(result))
            self.assertEqual(json.loads(path.read_text()), verify.build_result())

    def test_mu_square_zero(self):
        mu = verify.mobius_table(64)
        self.assertEqual(mu[4], 0)
        self.assertEqual(mu[12], 0)

    def test_prime_power_lambda_basis(self):
        primes, _ = verify.log_vectors(64)
        lam = verify.lambda_vectors(64, primes)
        self.assertEqual(lam[2], lam[4])
        self.assertEqual(lam[2], lam[64])
        self.assertNotEqual(lam[6], lam[2])


if __name__ == "__main__":
    unittest.main()

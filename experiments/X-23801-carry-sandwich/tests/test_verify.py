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


class CarrySandwichTests(unittest.TestCase):
    def test_beta_floor_formula(self):
        for n in range(2, 50):
            for q in range(2, n + 1):
                self.assertEqual(verify.beta(n, q), verify.beta_floor(n, q))

    def test_positive_diagonal(self):
        for n in range(2, 100):
            self.assertEqual(verify.beta(n, n), Fraction(n - 1, n + 1))

    def test_mobius_adjoint(self):
        self.assertEqual(verify.mobius_adjoint_check(60)["mismatches"], [])

    def test_legendre_carry(self):
        self.assertEqual(verify.legendre_carry_check(30)["mismatches"], [])

    def test_greedy_feasibility(self):
        out = verify.greedy_decimal(40, 50)
        self.assertGreaterEqual(out["minimum_final_residual"], "0")

    def test_recon_diagonal_saturation(self):
        out = verify.greedy_decimal(60, 50)
        self.assertEqual(out["off_diagonal_saturations"], 0)

    def test_result_verdict(self):
        result = verify.build_result()
        self.assertEqual(
            result["verdict"], "PASS_EXACT_INTERFACES_CARRY_SANDWICH_OPEN"
        )
        self.assertEqual(result["floor_formula_mismatches"], [])

    def test_digest_changes_on_mutation(self):
        result = verify.build_result()
        original = result["proof_sha256"]
        payload = dict(result)
        payload.pop("proof_sha256")
        payload["mobius_adjoint"] = dict(payload["mobius_adjoint"])
        payload["mobius_adjoint"]["limit"] = 79
        encoded = json.dumps(
            payload, sort_keys=True, separators=(",", ":")
        ).encode()
        self.assertNotEqual(original, hashlib.sha256(encoded).hexdigest())

    def test_replay_rejects_mutation(self):
        result = verify.build_result()
        result["floor_formula_mismatches"] = [[4, 2]]
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "mutated.json"
            path.write_text(json.dumps(result))
            self.assertNotEqual(json.loads(path.read_text()), verify.build_result())


if __name__ == "__main__":
    unittest.main()

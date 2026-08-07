from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x23201_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ProposalRegressionTests(unittest.TestCase):
    def test_resolvent_identity(self):
        result = module.verify_resolvent(80, 4)
        self.assertEqual(result["mismatch_count"], 0)
        self.assertGreater(result["first_residual_support"], result["cutoff_v"])

    def test_difference_inversion(self):
        result = module.verify_geometric_inversion(120)
        self.assertEqual(result["checks"], 600)

    def test_terminal_adapter(self):
        result = module.verify_terminal_adapter()
        self.assertEqual(result["terminal_energy"], [2, 1])
        self.assertEqual(result["hankel_energy"], [4, 1])

    def test_resolvent_mutation_detected(self):
        mu = module.mobius_table(30)
        v = module.ceil_kth_root(30, 3)
        eps = [0] * 31
        eps[1] = 1
        one = [0] + [1] * 30
        mu_v = [0] * 31
        for n in range(1, v + 1):
            mu_v[n] = mu[n]
        conv = module.dirichlet_convolution(one, mu_v, 30)
        r = [eps[n] - conv[n] for n in range(31)]
        r[v] = 1
        self.assertTrue(any(r[n] != 0 for n in range(1, v + 1)))

    def test_bad_domination_rejected(self):
        bad = [
            [module.Fraction(-1), module.Fraction(0)],
            [module.Fraction(0), module.Fraction(1)],
        ]
        self.assertFalse(module.ldl_positive_semidefinite(bad))

    def test_proof_digest_stable(self):
        first = module.verify()
        second = module.verify()
        self.assertEqual(first["proof_object_sha256"], second["proof_object_sha256"])


if __name__ == "__main__":
    unittest.main()

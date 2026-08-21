import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestCycleCapacityDebt(unittest.TestCase):
    def test_proof_object(self):
        result = verify.proof_object()
        self.assertEqual(
            result["classification"],
            "EXACT_CYCLE_CAPACITY_DEBT_IDENTITIES_VERIFIED",
        )

    def test_target_roundtrip(self):
        for x in range(6, 14):
            w = verify.target(x)
            r = verify.target_divergence(w)
            d = verify.canonical_flow(r)
            self.assertEqual(verify.divergence(d, x), r)
            self.assertEqual(verify.loads(d, x), w)

    def test_cycle_invariance(self):
        x = 18
        memo = {}
        for n, j in verify.balanced_edges(x):
            if j == n // 2:
                continue
            c = verify.fundamental_cycle(n, j, memo)
            self.assertEqual(
                verify.divergence(c, x),
                [verify.Fraction(0)] * (x + 1),
            )

    def test_variation_identity(self):
        x = 14
        w = verify.target(x)
        r = verify.target_divergence(w)
        d = verify.canonical_flow(r)
        edges = verify.balanced_edges(x)
        omega = verify.capacities(edges, x)
        baseline = sum(verify.Fraction(1, q) * w[q] for q in range(2, x + 1))
        total = sum(abs(d.get(e, 0)) * omega[e] for e in edges)
        debt = verify.negative_debt(d, omega)
        self.assertEqual(total, baseline + 2 * debt)

    def test_wrong_cycle_fails(self):
        x = 12
        memo = {}
        c = verify.fundamental_cycle(12, 4, memo)
        first = next(iter(c))
        c[first] += 1
        self.assertNotEqual(
            verify.divergence(c, x),
            [verify.Fraction(0)] * (x + 1),
        )


if __name__ == "__main__":
    unittest.main()

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestPascalCycleKernel(unittest.TestCase):
    def test_pascal_cycle(self):
        for n in range(4, 25):
            for j in range(2, n // 2 + 1):
                self.assertEqual(verify.divergence(verify.pascal_cycle(n, j), n), [0] * (n + 1))

    def test_tree_divergence_and_size(self):
        memo = {}
        X = 40
        for n in range(2, X + 1):
            t = verify.tree(n, memo)
            r = verify.divergence(t, X)
            expected = [0] * (X + 1)
            expected[1] = -n
            expected[n] = 1
            self.assertEqual(r, expected)
            self.assertEqual(verify.l1(t), n - 1)

    def test_fundamental_cycle(self):
        memo = {}
        X = 50
        for n, j in verify.balanced_edges(X):
            if j == verify.canonical_child(n):
                continue
            c = verify.fundamental_cycle(n, j, memo)
            self.assertEqual(verify.divergence(c, X), [0] * (X + 1))
            self.assertEqual(c[(n, j)], 1)

    def test_wrong_sign_fails(self):
        c = verify.pascal_cycle(12, 5)
        verify.add_term(c, verify.edge(12, 1), 2)
        self.assertNotEqual(verify.divergence(c, 12), [0] * 13)

    def test_full_proof_object(self):
        obj = verify.proof_object()
        self.assertEqual(
            obj["classification"],
            "EXACT_PASCAL_AND_BALANCED_FUNDAMENTAL_CYCLE_BASES_VERIFIED",
        )


if __name__ == "__main__":
    unittest.main()

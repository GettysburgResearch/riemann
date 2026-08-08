import importlib.util
from fractions import Fraction
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestTernaryFragmentation(unittest.TestCase):
    def test_split_identity(self):
        for n in range(2, 100):
            a, _ = verify.children(n)
            for q in range(2, n + 1):
                self.assertEqual(
                    verify.carry(n, a, q),
                    verify.continuum_ternary_carry(n, q) - verify.ternary_correction(n, q),
                )

    def test_exact_target_reconstruction(self):
        X = 30
        w = [Fraction(0) for _ in range(X + 1)]
        for q in range(2, X + 1):
            w[q] = Fraction(X - q, X * q)
        _, r = verify.target_divergence(w)
        A = verify.ternary_flow(r)
        self.assertEqual(verify.divergence(A), r)
        self.assertEqual(verify.loads(A), w)

    def test_tail_renewal(self):
        X = 36
        w = [Fraction(0) for _ in range(X + 1)]
        for q in range(2, X + 1):
            w[q] = Fraction(X - q, q * (q + 1))
        u, r = verify.target_divergence(w)
        A = verify.ternary_flow(r)
        S = verify.tails(A)
        for n in range(2, X + 1):
            self.assertEqual(S[n], u[n] + S[(3 * n + 1) // 2] + S[3 * n - 2])

    def test_base3_endpoint(self):
        for N in range(1, 1000):
            self.assertEqual(
                sum(1 - 2 * verify.v3(n) for n in range(1, N + 1)),
                verify.base3_digit_sum(N),
            )

    def test_full_object(self):
        obj = verify.proof_object()
        self.assertEqual(obj["classification"], "EXACT_TERNARY_FRAGMENTATION_ALGEBRA_VERIFIED")


if __name__ == "__main__":
    unittest.main()

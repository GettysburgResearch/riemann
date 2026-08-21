from __future__ import annotations
import unittest
from certify import certify_factorization, factor_small_integer, is_prime_u64, validate_factorization

class PrimalityTests(unittest.TestCase):
    def test_u64(self):
        for p in (2,3,5,97,99_999_989,18_446_744_073_709_551_557):
            self.assertTrue(is_prime_u64(p), p)
        for n in (0,1,4,9,341,561,1_000_000_000):
            self.assertFalse(is_prime_u64(n), n)
    def test_composite_rejected(self):
        with self.assertRaisesRegex(ValueError,"not prime"):
            validate_factorization([{"p":4,"a":1}])

class RobinCertificateTests(unittest.TestCase):
    def certify(self,n):
        return certify_factorization(factor_small_integer(n), precision=50, gamma_terms=10_000)
    def test_5040_outside_domain(self):
        r=self.certify(5040)
        self.assertEqual(r["verdict"],"OUT_OF_DOMAIN")
        self.assertGreaterEqual(float(r["intervals"]["difference_sigma_over_n_minus_rhs"]["lower"]),0)
    def test_5041_satisfies(self):
        self.assertEqual(self.certify(5041)["verdict"],"CERTIFIED_SATISFACTION")
    def test_55440_satisfies(self):
        r=self.certify(55440)
        self.assertEqual(r["verdict"],"CERTIFIED_SATISFACTION")
        self.assertLess(float(r["intervals"]["difference_sigma_over_n_minus_rhs"]["upper"]),0)
    def test_precision_stability(self):
        f=factor_small_integer(55440)
        lo=certify_factorization(f,precision=45,gamma_terms=5000)
        hi=certify_factorization(f,precision=70,gamma_terms=20000)
        self.assertEqual(lo["verdict"],"CERTIFIED_SATISFACTION")
        self.assertEqual(hi["verdict"],"CERTIFIED_SATISFACTION")

if __name__ == "__main__": unittest.main()

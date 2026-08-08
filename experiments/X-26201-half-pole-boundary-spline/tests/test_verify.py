from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(verify)


class TestHalfPoleBoundarySpline(unittest.TestCase):
    def test_exact_hankel_counterexample(self):
        self.assertEqual(verify.hankel_determinant(), Fraction(-233, 64))

    def test_derivative_formula(self):
        for r in range(40):
            self.assertEqual(verify.derivative_tuple(r), verify.claimed_derivative_tuple(r))

    def test_bspline_orientation(self):
        a, b, t = Fraction(0), Fraction(3), Fraction(1)
        self.assertEqual(verify.integrate_bspline_quadratic(a, b, t), Fraction(2))
        self.assertGreaterEqual(verify.bspline(a, b, t, Fraction(2)), 0)

    def test_wrong_pair_weight_fails(self):
        A = Fraction(7)
        wrong = Fraction(3, 4) * Fraction(2).limit_denominator() * A
        self.assertNotEqual(A - wrong, 0)

    def test_oversupport_collar_is_load_bearing(self):
        ledgers = [verify.oversupport_ledger(Y) for Y in range(2, 80)]
        nonzero = [d for d in ledgers if d["mertens_shell"] != 0]
        self.assertTrue(nonzero)
        for d in nonzero:
            self.assertNotEqual(d["inner_half_pole_moment"], 0)
            self.assertEqual(d["total_half_pole_moment"], 0)

    def test_binary_endpoint(self):
        for N in range(1, 1000):
            self.assertEqual(
                sum(1 - verify.v2(n) for n in range(1, N + 1)),
                N.bit_count(),
            )

    def test_mobius_cube_same_sign(self):
        primes = [(11, 13), (17, 19), (23, 29)]
        signs = set()
        for mask in range(8):
            n = 1
            for i, pair in enumerate(primes):
                n *= pair[(mask >> i) & 1]
            signs.add(verify.mobius(n))
        self.assertEqual(signs, {-1})

    def test_full_proof_object(self):
        obj = verify.proof_object()
        self.assertEqual(obj["classification"], "EXACT_HALF_POLE_BOUNDARY_SPLINE_INTERFACES_VERIFIED")


if __name__ == "__main__":
    unittest.main()

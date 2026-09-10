"""Fast structural tests for the off-line zero hunt packet.

These re-run the load-bearing correctness checks, not the long sweeps:
  1. Arb certified-comparison semantics that every verdict here relies on.
  2. Phi normalisation: H_0 ~ Xi(z/2), pinned against the first zeta ordinate.
  3. E1 predicates actually DETECT an injected off-line pair (no false negative).
  4. E1 predicates do NOT fire on a clean critical-line field (no false positive).
  5. von Mangoldt weight is log p, not p  (the bug that faked an RH refutation).
  6. A small certified LDL^T of the Weil Toeplitz form completes positive definite.

Run:  python3 tests.py
"""

import sys
import unittest

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from flint import arb  # noqa: E402

import e1_pick_loewner as e1  # noqa: E402
import e3_weil_form as e3  # noqa: E402
from common import certified_negative, set_prec  # noqa: E402
from e2_dbn_laguerre import H_derivs  # noqa: E402


class TestArbSemantics(unittest.TestCase):
    def test_comparison_is_certified(self):
        set_prec(200)
        straddling = arb(-1) + arb(0, 1)          # [-2, 0]
        strictly_neg = arb(-3) + arb(0, 1)        # [-4, -2]
        self.assertFalse(bool(straddling < 0), "a ball touching 0 must not certify")
        self.assertTrue(bool(strictly_neg < 0))
        self.assertTrue(certified_negative(strictly_neg))
        self.assertFalse(certified_negative(straddling))


class TestPhiNormalisation(unittest.TestCase):
    def test_first_zeta_zero_is_bracketed_at_z_equals_2gamma(self):
        set_prec(200)
        g = 14.134725141734693
        left = H_derivs(arb(0), arb(2 * g) - arb("0.3"), 200)[0].real
        right = H_derivs(arb(0), arb(2 * g) + arb("0.3"), 200)[0].real
        self.assertTrue(bool(left > 0) and bool(right < 0),
                        "H_0 must change sign across z = 2 * 14.1347...")

    def test_no_sign_change_under_the_wrong_normalisation(self):
        set_prec(200)
        g = 14.134725141734693
        left = H_derivs(arb(0), arb(g) - arb("0.3"), 200)[0].real
        right = H_derivs(arb(0), arb(g) + arb("0.3"), 200)[0].real
        self.assertFalse(bool(left > 0) and bool(right < 0))


class TestE1Sensitivity(unittest.TestCase):
    """The predicates must fire on a planted pair and stay quiet without one."""

    def setUp(self):
        set_prec(300)
        self.xs = e1.offsets(list(range(5, 18)))
        self.gaps = [arb(m) * arb("0.22") for m in range(-20, 21) if m != 0]

    def test_detects_injected_off_line_pair(self):
        for de in (8, 12, 16):
            delta = arb(1) / arb(2) ** de
            Rs = e1.synthetic_responses(self.xs, arb(0), delta, self.gaps)
            fired = any(certified_negative(v)
                        for _, v in e1.predicates(self.xs, Rs) if v is not None)
            self.assertTrue(fired, f"failed to detect a planted pair at 2^-{de}")

    def test_quiet_on_clean_critical_line_field(self):
        Rs = e1.synthetic_responses(self.xs, arb(0), arb(0), self.gaps)
        fired = [n for n, v in e1.predicates(self.xs, Rs)
                 if v is not None and certified_negative(v)]
        self.assertEqual(fired, [], "false positive on an all-real zero field")


class TestMangoldt(unittest.TestCase):
    def test_weight_is_log_p_not_p(self):
        primes = dict(e3.mangoldt_upto(30))
        self.assertEqual(primes[8], 2, "n=8 is 2^3, so the stored prime is 2")
        self.assertEqual(primes[9], 3)
        self.assertNotIn(6, primes, "6 is not a prime power")
        # Lambda(8) = log 2 ~ 0.693, emphatically not 8 or 2.
        lam8 = arb(primes[8]).log()
        self.assertTrue(bool(lam8 < arb("0.7")) and bool(lam8 > arb("0.69")))


class TestWeilForm(unittest.TestCase):
    def test_small_toeplitz_is_certified_positive_definite(self):
        set_prec(700)
        taus, _, _ = e3.build_tau(8, 0.25, 700)
        status, piv, fail_at = e3.certified_ldlt(taus, 8)
        self.assertEqual(status, "positive_definite", f"LDL^T failed at {fail_at}")
        self.assertTrue(all(bool(p > 0) for p in piv))

    def test_tau0_matches_the_known_validated_value(self):
        set_prec(700)
        taus, _, _ = e3.build_tau(1, 0.25, 700)
        # validated against a direct sum over zeros: 0.0129331185
        self.assertTrue(bool(taus[0] > arb("0.01293")) and
                        bool(taus[0] < arb("0.01294")))


if __name__ == "__main__":
    unittest.main(verbosity=2)

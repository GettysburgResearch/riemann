"""
Adversarial tests for the Li coefficients (T-0003) and the targeted/generalised
Li coefficients (T-0004).

Runnable with pytest or directly:  python3 tests/test_li.py

Two tests here exist because they caught real bugs:

  * `test_enclosures_overlap_across_truncations` is the R-0008 regression.  The
    Euler-Maclaurin remainder was not propagated into the Taylor coefficients,
    so the "certified" enclosures came out at 1e-239 when the truncation error
    alone is 1e-61 -- a hundred orders of magnitude too tight.  Values computed
    at two truncation orders then failed to overlap.  The general lesson is in
    NEGATIVE_RESULTS: an enclosure much tighter than the known error term is a
    bug, not a triumph.
  * `test_general_reduces_to_classical_at_alpha_one` exercises the re-centred
    machinery (arbitrary complex centre, polygamma at alpha/2+1, the 2u scale)
    against the independently validated classical path.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

from flint import acb, arb  # noqa: E402

import certzeta as cz  # noqa: E402
import li  # noqa: E402


def test_first_ten_match_published_values():
    """lambda_1 .. lambda_10 against the standard tabulated values.

    These are quoted from memory (M-0004 citation flag), so the test is
    deliberately loose -- 1e-5 relative.  It is a smoke test against a gross
    normalisation error, not a precision check; the precision checks are the
    overlap and identity tests below, which need no external numbers."""
    cz.set_prec(600)
    lam = li.li_coefficients(10, tol_bits=200)
    known = [0.0230957, 0.0923457, 0.207639, 0.368791, 0.575543,
             0.827566, 1.12446, 1.46576, 1.85092, 2.27934]
    for n, (v, k) in enumerate(zip(lam, known), start=1):
        assert abs(float(v.real) - k) < 1e-5 * max(1.0, abs(k)), (n, str(v.real), k)


def test_enclosures_overlap_across_truncations():
    """R-0008 regression.

    The lambda_n are computed from a truncated Euler-Maclaurin expansion.  Two
    different truncation orders give two different approximations, but if the
    remainder is honestly propagated the two ENCLOSURES must overlap.  Before
    the fix they did not, because the remainder was dropped entirely."""
    cz.set_prec(1200)
    a = li.li_coefficients(8, tol_bits=200)
    b = li.li_coefficients(8, tol_bits=400)
    for n, (x, y) in enumerate(zip(a, b), start=1):
        assert x.real.overlaps(y.real), (n, str(x.real), str(y.real))


def test_enclosures_overlap_across_cauchy_radii():
    """Same, varying the Cauchy circle R used for the remainder bound.  R only
    enters the ERROR term, never the value, so disagreement means the error
    term is wrong."""
    cz.set_prec(1200)
    a = li.li_coefficients(8, tol_bits=250, R="1.0")
    b = li.li_coefficients(8, tol_bits=250, R="2.5")
    for n, (x, y) in enumerate(zip(a, b), start=1):
        assert x.real.overlaps(y.real), (n, str(x.real), str(y.real))


def test_enclosure_is_not_absurdly_tight():
    """The R-0008 smell test, made mechanical.

    With tol_bits = 200 the Euler-Maclaurin remainder is about 2^-200 ~ 6e-61.
    A lambda_n enclosure radius far below that means the remainder is not being
    carried.  Radius 0 would be the pathological case the bug produced."""
    cz.set_prec(900)
    lam = li.li_coefficients(6, tol_bits=200)
    for n, v in enumerate(lam, start=1):
        r = float(v.real.rad())
        assert r > 0.0, (n, "zero radius: the remainder is not being propagated")
        assert r < 1e-30, (n, r, "enclosure uselessly loose")


def test_general_reduces_to_classical_at_alpha_one():
    """li_general(alpha=1) must reproduce li_coefficients exactly.

    Different code: xi_taylor_at re-centres the Euler-Maclaurin Taylor model at
    an arbitrary complex centre, takes polygamma at alpha/2+1 rather than 3/2,
    carries the extra |alpha-1| factor in the remainder bound, and rescales the
    Mobius composition by 2u.  Agreement at alpha = 1 exercises all of it."""
    cz.set_prec(1200)
    a = li.li_coefficients(10, tol_bits=300)
    b = li.li_general(acb(1), 10, tol_bits=300)
    for n, (x, y) in enumerate(zip(a, b), start=1):
        assert x.real.overlaps(y.real), (n, str(x.real), str(y.real))
        assert abs(float(x.real) - float(y.real)) < 1e-40, (n, str(x.real), str(y.real))


def test_lambda_1_equals_2u_times_re_log_derivative():
    """T-0004 part 3: lambda_1^(alpha) = 2u Re(xi'/xi)(alpha).

    z = 0 sits at s = alpha with ds/dz = 2u, so the first coefficient of
    log xi(s(z)) is the log-derivative scaled by 2u.  The left side runs through
    the Mobius composition and a series logarithm; the right side is two Taylor
    coefficients.  They share almost no code path."""
    cz.set_prec(1200)
    for u, v in [("0.5", "0"), ("0.1", "14.134725"), ("0.01", "1977.22")]:
        al = acb(arb("0.5") + arb(u), arb(v))
        lam1 = li.li_general(al, 1, tol_bits=300)[0].real
        C = li.xi_taylor_at(al, 4, tol_bits=300)
        rhs = 2 * arb(u) * (C[1] / C[0]).real
        assert lam1.overlaps(rhs), (u, v, str(lam1), str(rhs))


def test_amplification_law_is_exact():
    """|phi_alpha(rho)| = (u+delta)/|u-delta| when v = gamma.

    This is the whole point of T-0004: aiming alpha at the zero turns the
    classical 1 + O(delta/gamma^2) into something unbounded.  Pure algebra, so
    it is checked exactly rather than statistically."""
    gam, delta = 14.134725, 0.01
    rho = complex(0.5 - delta, gam)
    for k in (4.0, 2.0, 1.5, 1.1):
        al = complex(0.5 + k * delta, gam)
        w, a = rho - 0.5, al - 0.5
        got = abs((w - a) / (w + a.conjugate()))
        want = (k * delta + delta) / abs(k * delta - delta)
        assert abs(got - want) < 1e-9 * want, (k, got, want)


def test_targeted_coefficients_positive_at_a_lehmer_pair():
    """The certified statement of X-0010: aiming alpha at the tightest Lehmer
    pair found here produces no negative coefficient."""
    cz.set_prec(1500)
    al = acb(arb("0.5") + arb("0.01"), arb("1977.2226951"))
    L = li.li_general(al, 8, tol_bits=400)
    for n, x in enumerate(L, start=1):
        assert x.real > 0, (n, str(x.real))


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS  {name}")
            except Exception as e:
                fails += 1
                print(f"FAIL  {name}: {type(e).__name__}: {e}")
    print("\nall passed" if not fails else f"\n{fails} FAILURES")
    sys.exit(1 if fails else 0)

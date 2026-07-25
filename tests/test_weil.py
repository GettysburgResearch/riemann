"""
Adversarial tests for the Weil explicit-formula machinery (T-0002) and the
interval-Newton isolation (L-0007).

Runnable with pytest or directly:  python3 tests/test_weil.py

The decisive test is the first one: the explicit formula computed from PRIMES
must reproduce the sum over the CERTIFIED ZEROS.  The two sides share no code,
so a sign or normalisation error anywhere fails it immediately -- and it did
catch one during development (the even part of a complex g against e^{-c|u|}).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

from flint import acb, arb, ctx  # noqa: E402

import certzeta as cz  # noqa: E402
import hermite as Herm  # noqa: E402
import newton as nw  # noqa: E402
import weil  # noqa: E402
import weil_mod as wm  # noqa: E402


def ordinates():
    p = os.path.join(HERE, "..", "experiments", "X-0004-lehmer-pairs",
                     "results", "lehmer-T2000.json")
    with open(p) as fh:
        return [float(z.split(" ")[0].lstrip("[")) for z in json.load(fh)["zeros"]]


def zero_side(a, m, g0, ords):
    """2 sum_{gamma>0} h(gamma) with h(r) = a^2 sinc^{2m}(a(r-g0)/2),
    summed over r = +- gamma."""
    A, G = arb(a), arb(g0)
    tot = arb(0)
    for g in ords:
        for r in (arb(g), -arb(g)):
            x = A * (r - G) / 2
            sc = (x.sin() / x) if abs(x) > arb("1e-30") else arb(1)
            tot += A**2 * sc ** (2 * m)
    return tot


def test_explicit_formula_matches_certified_zeros():
    """The decisive cross-check: primes vs zeros, no shared code."""
    ctx.prec = 250
    ords = ordinates()
    for a, m in [(1.0, 2), (1.5, 2), (1.0, 3)]:
        lhs = zero_side(a, m, 0.0, ords)
        rhs = weil.F_terms(a, 0.0, m=m, nsub=20000)["total"]
        # zero-sum tail beyond T = 2000 plus the formula's own uncertainty
        import math
        T = 2000.0
        dens = math.log(T / (2 * math.pi)) / (2 * math.pi)
        tail = 2 * (a**2) * ((2 / a) ** (2 * m)) * dens / ((2 * m - 1) * T ** (2 * m - 1))
        slack = 20 * (tail + float(rhs.rad()) + 1e-30)
        assert abs(float(lhs) - float(rhs)) < slack, (a, m, float(lhs), float(rhs))


def test_modulated_formula_matches_certified_zeros():
    ctx.prec = 250
    ords = ordinates()
    for g0 in [14.134725141734693, 100.0]:
        lhs = zero_side(1.0, 4, g0, ords)
        rhs = wm.F_terms_mod(1.0, 0.0, g0, m=4, N=4000, K=2)["total"]
        assert rhs.imag.contains(arb(0)), f"modulated entry not real at {g0}"
        assert abs(float(lhs) - float(rhs.real)) < 1e-6, (g0, float(lhs))


def test_modulated_reduces_to_unmodulated_at_zero():
    """gamma_0 = 0 must reproduce weil.py, which is a different code path."""
    ctx.prec = 250
    for d in [0.0, 0.5]:
        u = weil.F_terms(1.0, d, m=4, nsub=20000)["total"]
        v = wm.F_terms_mod(1.0, d, 0.0, m=4, N=4000, K=2)["total"]
        assert v.imag.contains(arb(0))
        assert abs(float(u) - float(v.real)) < 1e-8, (d, float(u), float(v.real))


def test_watson_acceleration_agrees():
    """K = 2 must agree with the unaccelerated K = 0, and be far tighter."""
    ctx.prec = 300
    slow = wm.F_terms_mod(1.0, 0.0, 14.134725, m=4, N=60000, K=0)["total"]
    fast = wm.F_terms_mod(1.0, 0.0, 14.134725, m=4, N=4000, K=2)["total"]
    assert slow.real.overlaps(fast.real), (str(slow), str(fast))
    assert float(fast.real.rad()) < float(slow.real.rad()) / 1000


def test_weil_matrix_is_positive_definite():
    ctx.prec = 220
    Q = weil.weil_matrix(1.0, [0.5 * j for j in range(6)], m=2, nsub=20000)
    verdict, piv = Herm.ldl_signs(Q)
    assert verdict == "PD", (verdict, [str(x) for x in piv])


def test_bspline_partition_and_support():
    ctx.prec = 120
    # B_n vanishes outside [-n/2, n/2] and integrates to 1 (checked by a coarse
    # Riemann sum -- enough to catch a normalisation error)
    for n in (2, 4, 6):
        assert weil.bspline(n, arb(n) / 2 + 1) == 0
        assert weil.bspline(n, -arb(n) / 2 - 1) == 0
        h = arb(1) / 200
        tot = sum((weil.bspline(n, -arb(n) / 2 + h * (k + arb(1) / 2))
                   for k in range(200 * n)), arb(0)) * h
        assert abs(float(tot) - 1.0) < 1e-3, (n, float(tot))


def test_prime_powers_are_prime_powers():
    pp = weil.prime_powers(4.0)
    for n, p in pp:
        assert n % p == 0
        q, k = n, 0
        while q % p == 0:
            q //= p
            k += 1
        assert q == 1 and p ** k == n
    assert (2, 2) in pp and (4, 2) in pp and (3, 3) in pp


# ---------------------------------------------------------------------------
# interval Newton (L-0007)
# ---------------------------------------------------------------------------
def test_newton_certifies_low_zeros():
    cz.set_prec(400)
    for t in ["14.134725141734693790", "21.022039638771554993",
              "25.010857580145688763"]:
        res = nw.certify_zero(acb("0.5", t), tol_bits=120)
        assert res["certified"], t


def test_newton_refinement_is_quadratic():
    cz.set_prec(800)
    Nw = nw.refine(acb("0.5", "14.134725141734693790"), "0.05", iters=4,
                   tol_bits=250)
    assert Nw is not None
    assert float(abs(Nw.real - arb(1) / 2).upper()) < 1e-60


def test_newton_fails_away_from_a_zero():
    """Between zeros the test must ABSTAIN, not certify."""
    cz.set_prec(400)
    res = nw.certify_zero(acb("0.5", "17.5"), r_start="0.05", shrink=4,
                          tol_bits=120)
    assert not res["certified"], res


def test_newton_abstains_on_a_disc_holding_two_zeros():
    """A disc large enough to contain two zeros makes eta' vanish inside, so
    the enclosure of eta' contains 0 and the test abstains."""
    cz.set_prec(400)
    c = acb("0.5", "17.6")          # midway between 14.13 and 21.02
    Nw, ok, _ = nw.newton_step(c, arb("4.0"), 120)
    assert not ok


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

"""
Adversarial tests for the certified zeta stack (L-0001, L-0006).

Runnable with pytest or directly:  python3 tests/test_certzeta.py

The tests that matter are the ones whose expected value does NOT come from the
implementation being tested:
  * exact special values of zeta,
  * agreement with Arb's acb.zeta (a different algorithm and a different error
    analysis -- used here ONLY as an independent oracle, never in scripts/),
  * the functional equation xi(s) = xi(1-s),
  * integer-valuedness of a contour integral (the only test sensitive to a
    derivative error -- see NEGATIVE_RESULTS R-0002).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from flint import acb, arb, ctx  # noqa: E402

import certzeta as cz  # noqa: E402

POINTS = ["2", "3", "0.5", "0.25", "0.75", "-0.5"]
HEIGHTS = ["0", "14.134725141734693", "30", "100.5", "1000.25", "-45.7"]


def test_against_independent_arb_zeta():
    """R-0001 defence: agreement with a completely different implementation."""
    cz.set_prec(220)
    for sig in POINTS:
        for t in HEIGHTS:
            s = acb(sig, t)
            if (s - 1).abs_lower() < arb("0.01"):
                continue
            mine = cz.zeta_ball(s)
            ref = acb(s).zeta()          # independent oracle (Arb)
            assert mine.contains(ref), f"enclosure misses Arb value at {s}"


def test_exact_special_values():
    """Expected values independent of the implementation."""
    cz.set_prec(300)
    pi = arb.pi()
    assert cz.zeta_ball(acb(2)).contains(acb(pi**2 / 6))
    assert cz.zeta_ball(acb(4)).contains(acb(pi**4 / 90))
    assert cz.zeta_ball(acb(6)).contains(acb(pi**6 / 945))
    assert cz.zeta_ball(acb(0)).contains(acb(arb(-1) / 2))
    assert cz.zeta_ball(acb(-1)).contains(acb(arb(-1) / 12))
    assert cz.zeta_ball(acb(-3)).contains(acb(arb(1) / 120))


def test_xi_functional_equation_and_values():
    """xi(s) = xi(1-s) is an end-to-end structural test: it catches sign,
    factorial and rising-factorial indexing errors (it caught R-0001)."""
    cz.set_prec(250)
    assert cz.xi_ball(acb(0)).contains(acb(arb(1) / 2))
    assert cz.xi_ball(acb(1)).contains(acb(arb(1) / 2))
    for s in [acb("0.3", "7"), acb("0.9", "21.5"), acb("0.5", "40"), acb("0.1", "3")]:
        a = cz.xi_ball(s)
        b = cz.xi_ball(1 - s)
        assert a.overlaps(b), f"functional equation fails at {s}: {a} vs {b}"


def test_xi_vanishes_at_known_zeros():
    cz.set_prec(260)
    for t in ["14.134725141734693790457251983562470270784257115699",
              "21.022039638771554992628479593896902777334340524903",
              "25.010857580145688763213790992562821818659549672558"]:
        v = cz.xi_ball(acb("0.5", t))
        assert v.contains(acb(0)), f"xi should vanish at 0.5+{t}i"


def test_ball_enclosure_contains_interior_points():
    """An enclosure that does not enclose is the worst possible bug."""
    cz.set_prec(250)
    c = acb("0.3", "20")
    for rad in ["0.05", "0.01"]:
        B = cz.eta_taylor_ball(c, rad)
        r = float(rad)
        for dx, dy in [(0, 0), (r, 0), (-r, 0), (0, r), (0, -r),
                       (r * 0.7, r * 0.7), (-r * 0.5, r * 0.5)]:
            z = acb(arb("0.3") + arb(dx), arb("20") + arb(dy))
            assert B.contains(cz.zeta_pole_free_ball(z)), \
                f"Taylor model misses eta at offset {dx},{dy} (rad {rad})"


def test_taylor_model_is_tighter_than_naive():
    """L-0006's whole justification (R-0003)."""
    cz.set_prec(250)
    c = acb("0.2", "14.23")
    for rad in ["0.15", "0.05", "0.01"]:
        naive = cz.zeta_pole_free_ball(
            acb(arb("0.2", float(rad)), arb("14.23", float(rad)))
        )
        tay = cz.eta_taylor_ball(c, rad)
        assert float(tay.rad()) < float(naive.rad()) / 3, \
            f"Taylor model not tighter at rad {rad}"


def test_eta_and_deta_derivative():
    """R-0002 defence, part 1: the derivative must match a finite difference
    computed by the *other* (naive) evaluator."""
    cz.set_prec(400)
    for c in [acb("0.2", "14.23"), acb("0.6", "30.5"), acb("0.5", "5")]:
        _v, d = cz.eta_and_deta(c)
        h = arb("1e-25")
        fd = (cz.zeta_pole_free_ball(c + acb(h)) - cz.zeta_pole_free_ball(c - acb(h))) / (2 * h)
        assert d.overlaps(fd), f"eta' disagrees with finite difference at {c}"


def test_eta_value_matches_zeta():
    cz.set_prec(250)
    for s in [acb("2", "0"), acb("0.5", "14"), acb("0.3", "40")]:
        e, _ = cz.eta_and_deta(s)
        assert e.overlaps((s - 1) * cz.zeta_ball(s))


def test_hardy_Z_is_real_and_matches_modulus():
    cz.set_prec(250)
    for t in ["10", "14.1", "25.5", "60"]:
        z = cz.hardy_Z(t)
        zeta = cz.zeta_ball(acb("0.5", t))
        assert arb(z.abs_upper()) >= arb(zeta.abs_lower()) * arb("0.999")
        assert arb(z.abs_lower()) <= arb(zeta.abs_upper()) * arb("1.001")


def test_bernoulli_exact():
    from fractions import Fraction
    assert cz.bernoulli(0) == Fraction(1)
    assert cz.bernoulli(1) == Fraction(-1, 2)
    assert cz.bernoulli(2) == Fraction(1, 6)
    assert cz.bernoulli(4) == Fraction(-1, 30)
    assert cz.bernoulli(12) == Fraction(-691, 2730)
    assert cz.bernoulli(3) == 0 and cz.bernoulli(9) == 0


def test_increasing_M_shrinks_enclosure():
    cz.set_prec(300)
    s = acb("0.5", "30")
    prev = None
    for M in [4, 8, 16]:
        v = cz.zeta_ball(s, cz.EMParams(40, M))
        if prev is not None:
            assert float(v.rad()) <= float(prev.rad()) * 1.001
            assert v.overlaps(prev)
        prev = v


def test_pole_is_rejected():
    cz.set_prec(200)
    try:
        cz.zeta_ball(acb(1))
        raise AssertionError("zeta_ball must refuse the pole s=1")
    except ValueError:
        pass
    # ...but eta is fine there, with eta(1) = 1
    assert cz.zeta_pole_free_ball(acb(1)).contains(acb(1))


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

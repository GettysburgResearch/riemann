"""
Adversarial tests for the zero-counting machinery (L-0002, T-0001).

Runnable with pytest or directly:  python3 tests/test_winding.py

The most important tests here are the ABSTENTION tests: a certified counter
that returns a wrong number is a catastrophe, one that says "I don't know" is
merely expensive.  We check that a zero on the contour produces abstention.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from flint import acb, arb  # noqa: E402

import certzeta as cz  # noqa: E402
import hermite as H  # noqa: E402
import winding as W  # noqa: E402
import zeros as Z  # noqa: E402


def poly(roots):
    def f(s):
        p = acb(1)
        for r in roots:
            p = p * (s - r)
        return p

    def fp(s):
        tot = acb(0)
        for i, _ in enumerate(roots):
            p = acb(1)
            for j, r2 in enumerate(roots):
                if i != j:
                    p = p * (s - r2)
            tot += p
        return tot

    return f, fp


def test_polynomial_counts():
    cz.set_prec(200)
    cases = [
        ([acb(0)], 1),
        ([acb(0), acb(0)], 2),                       # double zero
        ([acb(0, 1), acb(0, -1)], 2),                # z^2+1
        ([acb("0.3", "0")] * 5, 5),                  # (z-0.3)^5
        ([acb(5, 5)], 0),                            # zero outside the box
    ]
    for roots, expected in cases:
        f, _ = poly(roots)
        c = W.count_zeros_rect(-2, 2, -2, 2, f=f, n0=8)
        assert c.ok, f"unexpected abstention for {roots}: {c.reason}"
        assert c.count == expected, f"{roots}: got {c.count}, want {expected}"


def test_abstains_when_zero_on_contour():
    """A zero exactly on the boundary must produce abstention, never a number."""
    cz.set_prec(200)
    f, _ = poly([acb(0)])
    c = W.count_zeros_rect(0, 1, 0, 1, f=f, n0=4, max_depth=8)   # zero at a corner
    assert not c.ok, "must abstain when a zero lies on the contour"
    f2, _ = poly([acb("0.5", "0")])
    c2 = W.count_zeros_rect(-1, 1, 0, 2, f=f2, n0=4, max_depth=8)  # zero on bottom edge
    assert not c2.ok, "must abstain when a zero lies on an edge"


def test_xi_low_zero_counts():
    """Counts must match independent knowledge of the low-lying ordinates
    (14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33, 48.01, 49.77)."""
    cz.set_prec(250)
    for T, expected in [(20, 1), (30, 3), (50, 10)]:
        c = W.count_zeros_rect(0, 1, 0, T, f=cz.xi_ball, n0=8)
        assert c.ok and c.count == expected, f"T={T}: {c.count} != {expected} ({c.reason})"


def test_additivity_of_counts():
    cz.set_prec(250)
    whole = W.count_zeros_rect(0, 1, 0, 40, f=cz.xi_ball, n0=8)
    split = W.count_zeros_rect_split(0, 1, 0, 40, pieces=4, f=cz.xi_ball, n0=8)
    assert whole.ok and split.ok
    assert whole.count == split.count


def test_functional_equation_symmetry_of_counts():
    """L-0002 adversarial test 4: mirrored off-critical strips must agree."""
    cz.set_prec(250)
    left = W.count_zeros_rect(0, "0.49", 0, 60, f=cz.xi_ball, n0=8)
    right = W.count_zeros_rect("0.51", 1, 0, 60, f=cz.xi_ball, n0=8)
    assert left.ok and right.ok
    assert left.count == right.count == 0


def test_sign_changes_match_box_count():
    """L-0004 end to end, at small height."""
    cz.set_prec(250)
    box = W.count_zeros_rect(0, 1, 0, 50, f=cz.xi_ball, n0=8)
    _zs, undet, nsign = Z.certified_zeros(0, 50, "0.1")
    assert box.ok and not undet and nsign == box.count == 10


def test_coarse_scan_fails_loudly():
    """L-0004 adversarial test: a scan too coarse to see every zero must
    produce a DEFICIT, not a false success."""
    cz.set_prec(250)
    _zs, _u, nsign = Z.certified_zeros(0, 100, "2.0")
    assert nsign < 29, "a 2.0 step should miss zeros near t=100"


def test_moment_zero_count_is_an_integer():
    """R-0002 defence, part 2: the single most sensitive test of eta'."""
    cz.set_prec(250)
    qs, _ = H.contour_moments("0.2", "0.8", "12", "23", 0, panel_len="0.3",
                              rad="0.1", nsub=24)
    q0 = qs[0]
    assert q0.imag.contains(arb(0)), f"count has nonzero imaginary part: {q0}"
    assert q0.real.contains(arb(2)), f"count should enclose 2, got {q0}"
    assert float(q0.rad()) < 0.01


def test_hermite_pd_on_online_polynomial():
    cz.set_prec(250)
    f, fp = poly([acb("0.5", t) for t in ["1", "2", "3"]])
    r = H.box_certificate("0.1", "0.9", "0.5", "3.5", f=f, fp=fp,
                          panel_len="0.2", rad="0.15", nsub=16)
    assert r["N"] == 3 and r["verdict"] == "PD"


def test_hermite_detects_planted_off_line_pair():
    """M-0003: a detector that has never fired proves nothing."""
    cz.set_prec(250)
    roots = [acb("0.5", "1"), acb("0.4", "2"), acb("0.6", "2"), acb("0.5", "3")]
    f, fp = poly(roots)
    r = H.box_certificate("0.1", "0.9", "0.5", "3.5", f=f, fp=fp,
                          panel_len="0.2", rad="0.15", nsub=16)
    assert r["N"] == 4, r
    assert r["verdict"] == "NOT_PSD", f"detector failed to fire: {r['verdict']}"


def test_hermite_pd_on_real_zeta_box():
    cz.set_prec(250)
    r = H.box_certificate("0.2", "0.8", "12", "23", panel_len="0.3", rad="0.1",
                          nsub=32)
    assert r["N"] == 2 and r["verdict"] == "PD", r


def test_hermite_moments_are_real():
    """T-0001(b): reality of q_k is what licenses the real symmetric Hankel
    form.  It relies on the box being symmetric about the critical line."""
    cz.set_prec(250)
    qs, _ = H.contour_moments("0.2", "0.8", "12", "23", 2, panel_len="0.3",
                              rad="0.1", nsub=24)
    for k, q in enumerate(qs):
        assert q.imag.contains(arb(0)), f"q_{k} is not real: {q}"


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

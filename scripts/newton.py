"""
newton.py -- certified zero isolation by the interval Newton method.

Agent: claude-01
Implements: L-0007.

The sign-change certificates of L-0004 prove that a zero EXISTS in an interval
of the critical line.  They do not prove it is the only zero there, they do not
prove it is simple, and they cannot say anything about a zero that is not on
the line.  The interval Newton test does all three:

    THEOREM (interval Newton, complex analytic case).  Let f be analytic on a
    neighbourhood of the closed disc D = B(c, r).  Suppose 0 is not in the
    enclosure f'(D), and put

        Nw(D) := c - f(c) / f'(D)          (a set, computed in ball arithmetic).

    If Nw(D) is contained in the INTERIOR of D, then f has exactly one zero in
    D, that zero is simple, and it lies in Nw(D).

Proof sketch: 0 not in f'(D) makes f injective on the convex set D (if
f(z1) = f(z2) then the mean value form 0 = f(z2)-f(z1) = INT_0^1 f'(z1+t(z2-z1))
dt (z2-z1) forces z2 = z1 since the integral lies in the convex hull of f'(D),
which omits 0).  Existence follows from the standard interval Newton argument /
degree theory: Nw(D) subset int(D) makes the Newton map a self-map of D, and
its fixed point is a zero of f.  Simplicity is immediate from f'(zero) != 0.

WHAT THIS BUYS
  * uniqueness and simplicity, independently of the count-matching of L-0004;
  * ordinate enclosures limited only by working precision, not by bisection;
  * the SAME test applied to a candidate off the critical line would certify an
    off-critical zero -- so it is also a counterexample acceptance test, and the
    most direct one in the repository: one disc, one inclusion.
"""

from __future__ import annotations

import sys

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["newton_step", "certify_zero", "refine"]


def newton_step(c: acb, r, tol_bits: int = 40) -> tuple:
    """Return (Nw, ok, diag) for f = eta on the disc B(c, r)."""
    r = arb(r)
    fc, _ = cz.eta_and_deta(c, tol_bits=tol_bits)
    fpD = cz.eta_deriv_ball(c, r, tol_bits=tol_bits)
    if fpD.contains(acb(0)):
        return None, False, "f'(D) contains 0"
    Nw = c - fc / fpD
    # Nw subset int(D)?  centre distance + radius < r, componentwise is enough
    dx = arb((Nw.real - c.real).abs_upper()) + arb(Nw.real.rad())
    dy = arb((Nw.imag - c.imag).abs_upper()) + arb(Nw.imag.rad())
    inside = (dx < r) and (dy < r)
    return Nw, bool(inside), {
        "f_at_centre": str(fc), "f_prime_enclosure": str(fpD),
        "newton_image": str(Nw), "r": str(r),
        "reach_x": str(dx), "reach_y": str(dy),
    }


def certify_zero(c: acb, r_start="0.05", shrink=8, tol_bits: int = 40):
    """Try a ladder of radii; return the first radius at which the interval
    Newton test succeeds, together with the resulting enclosure."""
    r = arb(r_start)
    for _ in range(shrink):
        Nw, ok, diag = newton_step(c, r, tol_bits)
        if ok:
            return {"certified": True, "radius": str(r), "enclosure": str(Nw),
                    "diag": diag}
        r = r / 2
    return {"certified": False, "radius": str(r), "diag": diag}


def refine(c: acb, r="0.05", iters: int = 3, tol_bits: int = 120):
    """Certify, then iterate.  Each Newton step squares the error, so two or
    three steps take a bisection-quality centre down to the floor set by
    `tol_bits`.  Returns the tightest certified enclosure found.

    The radius for the next step is taken generously (8x the current enclosure)
    so that the inclusion test still has room to succeed."""
    cur, rr, best = c, arb(r), None
    for _ in range(iters):
        Nw, ok, _ = newton_step(cur, rr, tol_bits)
        if not ok:
            break
        if best is None or float(Nw.rad()) < float(best.rad()):
            best = Nw
        cur = acb(arb(Nw.real.mid()), arb(Nw.imag.mid()))
        nxt = float(Nw.rad()) * 8
        if nxt <= 0 or nxt >= float(rr):
            break
        rr = arb(nxt)
    return best


if __name__ == "__main__":
    cz.set_prec(300)
    for t in ["14.134725141734693790", "21.022039638771554993",
              "25.010857580145688763"]:
        c = acb("0.5", t)
        res = certify_zero(c)
        print(f"gamma ~ {t}: certified={res['certified']} r={res['radius'][:10]}")
        if res["certified"]:
            print("   unique simple zero in", res["enclosure"][:70])

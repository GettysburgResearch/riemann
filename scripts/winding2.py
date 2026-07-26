"""
winding2.py -- an INDEPENDENT reimplementation of certified winding-number
zero counting, for the Q-0003 review.

Agent: claude-02.

This is not a refactor of claude-01's `winding.py`: it was written from the
STATEMENT of L-0002, with a different argument-tracking rule, different
subdivision control, and no shared code beyond the certified evaluator
`certzeta` (whose own validity is covered by L-0001/L-0006 and the oracle
tests).  Agreement between the two implementations on the same boxes is
therefore evidence that the counting LAYER implements the lemma, which is
what Q-0003 asks.  (A fully independent evaluator is still open; that half of
Q-0003 is not claimed here.)

THE RULE USED HERE (proved below, three lines).  Let a contour segment sigma
have a certified enclosure: a complex ball B = B(m, r) with f(sigma) subset B
and 0 not in B (i.e. r < |m|).  Then

  (1) the image path stays in B, a convex set avoiding 0, so it cannot wind
      about 0 within the segment;
  (2) every value in B has argument within alpha = arcsin(r/|m|) < pi/2 of
      arg m, so the argument along the segment varies inside an interval of
      width 2 alpha < pi;
  (3) hence the TOTAL argument change along the segment is exactly the
      principal difference  Arg(f(b)/f(a))  of its endpoint values, which
      lies in (-pi, pi):  any other candidate differs by a multiple of 2 pi
      and would leave the width-(2 alpha) interval.

Summing certified principal differences over a closed contour gives 2 pi W
with W the exact winding number; the ball-arithmetic sum must contain a
unique integer multiple of 2 pi, else we ABSTAIN.

Interface: count_zeros_rect2(x0, x1, y0, y1) -> (count, ok, reason).
"""

from __future__ import annotations

import sys

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["count_zeros_rect2"]


def _eta_ball_seg(c: acb, r: float, f=None):
    """Certified enclosure of f (default eta) over the disc B(c, r), which
    contains the segment of half-length r centred at c."""
    if f is not None:
        return f(acb(arb(c.real.mid(), r), arb(c.imag.mid(), r)))
    if r == 0.0:
        e, _ = cz.eta_and_deta(c)
        return e
    return cz.eta_taylor_ball(c, r)


def _principal_diff(za: acb, zb: acb) -> arb:
    """Principal Arg(zb/za) as a ball, in (-pi, pi] -- valid when neither
    ball straddles 0 and the quotient ball avoids the negative real axis'
    branch ambiguity; the caller guarantees the segment cone width < pi so
    the quotient cannot approach -1 within a segment."""
    q = zb / za
    return q.arg()


def _walk(p0: acb, p1: acb, f, depth_limit=60, min_len=2.0 ** -20):
    """Certified total argument change of f along the straight segment
    p0 -> p1, by adaptive bisection.  Returns (delta, ok, reason)."""
    total = arb(0)
    stack = [(p0, p1, 0)]
    # endpoint value cache along the way; we re-evaluate at split points
    while stack:
        a, b, depth = stack.pop()
        c = (a + b) / 2
        half = (abs(float((b - a).abs_upper()))) / 2
        m = _eta_ball_seg(c, half * 1.0000001, f)
        rad = max(float(m.real.rad()), float(m.imag.rad()))
        mid = acb(arb(m.real.mid()), arb(m.imag.mid()))
        # rule (1)-(2): the enclosure must avoid 0 with margin, so the image
        # cone from the origin has half-angle < pi/2
        if float(abs(mid).abs_lower()) > 1.42 * rad:      # sin(alpha) < 0.71
            fa = _eta_ball_seg(a, 0.0, f)
            fb = _eta_ball_seg(b, 0.0, f)
            d = _principal_diff(fa, fb)
            # rule (3): endpoints lie in a cone of full width < pi, so the
            # principal difference is the exact change; its ball must also
            # certify |d| < pi
            if float(abs(d).abs_upper()) < 3.14159:
                total += d
                continue
        if depth >= depth_limit or half * 2 < min_len:
            return arb(0), False, (f"abstain: cannot certify segment near "
                                   f"{complex(float(c.real.mid()), float(c.imag.mid()))}")
        stack.append((a, c, depth + 1))
        stack.append((c, b, depth + 1))
    return total, True, ""


def count_zeros_rect2(x0, x1, y0, y1, f=None):
    """Certified zero count of eta (or f) in the closed rectangle, by the
    independent argument-tracking rule above.  Returns (count, ok, reason)."""
    X0, X1, Y0, Y1 = arb(x0), arb(x1), arb(y0), arb(y1)
    corners = [acb(X0, Y0), acb(X1, Y0), acb(X1, Y1), acb(X0, Y1),
               acb(X0, Y0)]
    total = arb(0)
    for k in range(4):
        d, ok, reason = _walk(corners[k], corners[k + 1], f)
        if not ok:
            return 0, False, reason
        total += d
    two_pi = 2 * arb.pi()
    w = total / two_pi
    lo, hi = float(w.lower()), float(w.upper())
    n = round((lo + hi) / 2)
    if not (n - 0.45 < lo and hi < n + 0.45):
        return 0, False, f"winding not pinned: [{lo}, {hi}]"
    return n, True, ""

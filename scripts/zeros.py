"""
zeros.py -- certified isolation of zeros of the Hardy function Z(t).

Agent: claude-01
Implements: L-0004 (sign-change / IVT certificate) support code.

A certified sign change of the real-analytic function Z on [a,b] (both
endpoint enclosures strictly nonzero, opposite signs) proves by the
intermediate value theorem that Z has a zero in (a,b), i.e. that zeta has a
zero exactly ON the critical line at height in (a,b).

Combining a certified count of sign changes with a certified argument-principle
count of zeros in the corresponding rectangle proves that *all* zeros in that
rectangle lie on the critical line and are simple (L-0004).
"""

from __future__ import annotations

import sys

from flint import arb, ctx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402


def _sign(x: arb) -> int:
    """Rigorous sign of an arb ball: +1, -1, or 0 if undetermined."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def scan_sign_changes(t0, t1, step="0.1", refine_depth: int = 6):
    """Return a list of certified sign-change brackets (a, b, sign_a, sign_b)
    for Z on [t0, t1], plus a list of intervals where the sign could not be
    determined."""
    t0, t1, h = arb(t0), arb(t1), arb(step)
    n = int(float((t1 - t0) / h)) + 1
    pts, sgns, undetermined = [], [], []
    for i in range(n + 1):
        t = t0 + h * i
        if t > t1:
            t = t1
        z = cz.hardy_Z(t)
        s = _sign(z)
        d = 0
        # tiny refinement: raise working precision if the sign is undetermined
        while s == 0 and d < refine_depth:
            old = ctx.prec
            ctx.prec = old * 2
            z = cz.hardy_Z(t)
            s = _sign(z)
            ctx.prec = old
            d += 1
        if s == 0:
            undetermined.append(str(t))
        pts.append(t)
        sgns.append(s)
        if t >= t1:
            break

    brackets = []
    for i in range(len(pts) - 1):
        if sgns[i] != 0 and sgns[i + 1] != 0 and sgns[i] != sgns[i + 1]:
            brackets.append((pts[i], pts[i + 1], sgns[i], sgns[i + 1]))
    return brackets, undetermined


def bisect(a: arb, b: arb, sa: int, iters: int = 80):
    """Bisect a certified sign-change bracket down to a narrow certified
    enclosure of a zero of Z. Returns an arb ball containing the zero."""
    for _ in range(iters):
        m = (a + b) / 2
        s = _sign(cz.hardy_Z(m))
        if s == 0:
            break
        if s == sa:
            a = m
        else:
            b = m
        if float(b - a) < 1e-40:
            break
    mid = (a + b) / 2
    rad = (b - a) / 2
    return arb(mid.mid(), (rad + arb(mid.rad())).upper())


def certified_zeros(t0, t1, step="0.1", bisect_iters: int = 60):
    """Certified enclosures of on-line zeros (ordinates) in (t0, t1)."""
    brackets, undet = scan_sign_changes(t0, t1, step)
    out = []
    for a, b, sa, _sb in brackets:
        out.append(bisect(a, b, sa, bisect_iters))
    return out, undet, len(brackets)


if __name__ == "__main__":
    cz.set_prec(200)
    zs, undet, nb = certified_zeros(0, 50, "0.1")
    for z in zs:
        print(z)
    print("sign changes:", nb, "undetermined:", len(undet))

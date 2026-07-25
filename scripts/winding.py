"""
winding.py -- rigorous zero counting in rectangles by the argument principle.

Agent: claude-01
Implements: L-0002 (certified winding-number scheme).

Method (proved in claims/lemmas/L-0002-certified-winding-number.md):

  Let R be a closed rectangle with zeta analytic on a neighbourhood of dR
  (i.e. 1 not in R) and zeta nonvanishing on dR.  Split dR into finitely many
  arcs g_1, ..., g_m.  For each arc, cover it by a closed disc B_j and compute
  a ball enclosure Z_j of zeta(B_j).  If 0 is not in Z_j then Z_j is a disc
  missing the origin, hence subtends an angle < pi at 0, hence the continuous
  variation of arg zeta along g_j lies in (-pi, pi) and equals the principal
  value Arg(zeta(b_j)/zeta(a_j)).  Summing gives the total variation, and

      #zeros in R (with multiplicity) = (1/2 pi) * sum_j Arg(zeta(b_j)/zeta(a_j)).

  Every quantity is a certified enclosure, so if the resulting interval
  contains exactly one integer, that integer is the exact zero count.

The same routine works for any analytic f supplied as a callable on balls.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field

from flint import acb, arb, ctx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402


@dataclass
class WindingCertificate:
    """Machine-checkable summary of one argument-principle computation."""

    x0: str
    x1: str
    y0: str
    y1: str
    count: int | None
    total_arg: str
    segments: int
    max_depth: int
    min_modulus_lower: str
    prec: int
    ok: bool
    reason: str = ""
    subboxes: list = field(default_factory=list)

    def as_dict(self):
        d = dict(self.__dict__)
        d.pop("subboxes", None)
        return d


class WindingFailure(Exception):
    pass


def _seg_ball(a: acb, b: acb) -> acb:
    """Smallest axis-aligned ball (in the acb sense) covering the segment [a,b]."""
    mid = (a + b) / 2
    half = (b - a) / 2
    return acb(
        arb(mid.real.mid(), (abs(half.real) + mid.real.rad()).upper()),
        arb(mid.imag.mid(), (abs(half.imag) + mid.imag.rad()).upper()),
    )


class _Counter:
    def __init__(self, f, max_depth=22, min_arg_gap=0.25):
        self.f = f
        self.max_depth = max_depth
        self.min_arg_gap = min_arg_gap  # keep |Delta arg| <= (1-gap)*pi
        self.cache: dict[str, acb] = {}
        self.segments = 0
        self.deepest = 0
        self.min_mod = arb("+inf")

    def fval(self, z: acb) -> acb:
        key = f"{z.real.mid()}|{z.imag.mid()}"
        v = self.cache.get(key)
        if v is None:
            v = self.f(z)
            self.cache[key] = v
        return v

    def arc(self, a: acb, b: acb, depth: int = 0) -> arb:
        """Certified enclosure of the variation of arg f along [a, b]."""
        self.deepest = max(self.deepest, depth)
        if depth > self.max_depth:
            raise WindingFailure(
                f"max depth exceeded near {a.real.mid()}+{a.imag.mid()}i "
                "(zero on or very close to the contour?)"
            )
        B = _seg_ball(a, b)
        try:
            Z = self.f(B)
        except ValueError as e:
            raise WindingFailure(str(e))
        if Z.contains(acb(0)):
            m = (a + b) / 2
            return self.arc(a, m, depth + 1) + self.arc(m, b, depth + 1)

        lo = Z.abs_lower()
        if lo < self.min_mod:
            self.min_mod = arb(lo)

        ratio = self.fval(b) / self.fval(a)
        inc = ratio.arg()
        limit = arb.pi() * (1 - self.min_arg_gap)
        if not (arb(abs(inc).upper()) < limit) or not (arb(inc.rad()) < arb(0.05)):
            m = (a + b) / 2
            return self.arc(a, m, depth + 1) + self.arc(m, b, depth + 1)
        self.segments += 1
        return inc


def count_zeros_rect(
    x0, x1, y0, y1, f=None, n0: int = 8, prec: int | None = None, max_depth: int = 22
) -> WindingCertificate:
    """Certified number of zeros of f (default: zeta) in the closed rectangle
    [x0,x1] x [y0,y1], counted with multiplicity.

    n0 = initial number of subdivisions per edge (adaptive refinement follows).
    """
    if prec is not None:
        cz.set_prec(prec)
    f = f or (lambda z: cz.zeta_ball(z))

    X0, X1, Y0, Y1 = arb(x0), arb(x1), arb(y0), arb(y1)
    corners = [acb(X0, Y0), acb(X1, Y0), acb(X1, Y1), acb(X0, Y1)]

    c = _Counter(f, max_depth=max_depth)
    total = arb(0)
    ok, reason = True, ""
    try:
        for i in range(4):
            a, b = corners[i], corners[(i + 1) % 4]
            for k in range(n0):
                p = a + (b - a) * arb(k) / n0
                q = a + (b - a) * arb(k + 1) / n0
                total += c.arc(p, q)
    except WindingFailure as e:
        ok, reason = False, str(e)

    count = None
    if ok:
        w = total / (2 * arb.pi())
        lo, hi = float(w.lower()), float(w.upper())
        import math

        if math.floor(lo) == math.floor(hi) or (
            math.ceil(lo) == math.floor(hi) and hi - lo < 0.5
        ):
            cand = round((lo + hi) / 2)
            if cand - 0.5 < lo and hi < cand + 0.5:
                count = int(cand)
        if count is None:
            ok, reason = False, f"winding interval too wide: [{lo}, {hi}]"

    return WindingCertificate(
        x0=str(x0),
        x1=str(x1),
        y0=str(y0),
        y1=str(y1),
        count=count,
        total_arg=str(total),
        segments=c.segments,
        max_depth=c.deepest,
        min_modulus_lower=str(c.min_mod),
        prec=ctx.prec,
        ok=ok,
        reason=reason,
    )


def count_zeros_rect_split(x0, x1, y0, y1, pieces: int = 1, **kw) -> WindingCertificate:
    """Split the height range into `pieces` stacked rectangles and add the counts.
    Useful when a contour would otherwise pass too near a zero."""
    total = 0
    subs = []
    Y0, Y1 = arb(y0), arb(y1)
    for i in range(pieces):
        a = Y0 + (Y1 - Y0) * arb(i) / pieces
        b = Y0 + (Y1 - Y0) * arb(i + 1) / pieces
        cert = count_zeros_rect(x0, x1, a, b, **kw)
        subs.append(cert.as_dict())
        if not cert.ok:
            cert.subboxes = subs
            return cert
        total += cert.count
    return WindingCertificate(
        x0=str(x0),
        x1=str(x1),
        y0=str(y0),
        y1=str(y1),
        count=total,
        total_arg="(sum of sub-boxes)",
        segments=sum(s["segments"] for s in subs),
        max_depth=max(s["max_depth"] for s in subs),
        min_modulus_lower=min(s["min_modulus_lower"] for s in subs),
        prec=ctx.prec,
        ok=True,
        subboxes=subs,
    )


if __name__ == "__main__":
    import json

    cz.set_prec(200)
    cert = count_zeros_rect(0, 1, 0, 30)
    print(json.dumps(cert.as_dict(), indent=2))

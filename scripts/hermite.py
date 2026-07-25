"""
hermite.py -- the Hermite-Hankel box criterion (T-0001).

Agent: claude-01

IDEA
----
Let D be a rectangle symmetric about the critical line, with xi nonvanishing on
dD, containing N zeros of xi (with multiplicity).  Put

    w(s) = (s - 1/2 - i c) / (i r)          (c = centre height, r = half height)

so that the zeros of xi inside D correspond to points w_1, ..., w_N and

    zeta has all its zeros in D on the critical line
        <=>  every w_j is REAL.

The power sums of the w_j are computable by certified contour integration
(Delves-Lyness moments):

    q_k = sum_j w_j^k = (1/2 pi i) INT_{dD} w(s)^k (xi'/xi)(s) ds.

By Hermite's theorem the real symmetric Hankel matrix H = (q_{i+j})_{i,j<N}
has signature = (#distinct real roots) - (#distinct non-real conjugate pairs)
and rank = #distinct roots.  Hence

    all w_j real   <=>   H is positive semidefinite.

So a *certified negative* leading principal minor of H is a FINITE ALGEBRAIC
WITNESS of an off-critical zero inside D -- i.e. a counterexample certificate.
Conversely a certified positive definite H proves RH inside D.

RELATION TO KNOWN WORK (stated honestly)
----------------------------------------
The moment computation is the classical Delves-Lyness algorithm; the
real-rootedness test is classical Hermite/Hankel theory.  What is (as far as
this agent knows) not standard is packaging the two into a *box-local,
certificate-emitting RH test* whose failure mode is a single negative number.
This must not be described as new mathematics; it is new plumbing.  See
claims/theorems/T-0001 for the statement and proof, and NEGATIVE_RESULTS for
what it cannot do.
"""

from __future__ import annotations

import sys

from flint import acb, arb, ctx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402


# ---------------------------------------------------------------------------
# certified derivative of an analytic function from ball evaluations
# ---------------------------------------------------------------------------
def d_central(f, s: acb, h: arb, r: arb) -> acb:
    """Certified enclosure of f'(s) for analytic f, via the central difference

        f'(s) = (f(s+h) - f(s-h))/(2h) - sum_{k>=1} f^{(2k+1)}(s) h^{2k}/(2k+1)!

    and the Cauchy estimate |f^{(m)}(s)| <= m! M(r)/r^m, where M(r) is an upper
    bound for |f| on the closed ball B(s, r).  Requires 0 < h < r and f
    analytic on B(s, r).  The tail is bounded by

        (M/r) * (h/r)^2 / (1 - (h/r)^2).
    """
    h, r = arb(h), arb(r)
    if not (h < r):
        raise ValueError("need h < r")
    approx = (f(s + acb(h)) - f(s - acb(h))) / (2 * h)
    M = arb(f(acb(arb(s.real.mid(), r.upper()), arb(s.imag.mid(), r.upper()))).abs_upper())
    x = (h / r) ** 2
    tail = (M / r) * x / (1 - x)
    pad = arb(0, tail.upper())
    return approx + acb(pad, pad)


def xi_and_dxi(s: acb, h="1e-8", r="0.25"):
    """Certified (xi(s), xi'(s))."""
    return cz.xi_ball(s), d_central(cz.xi_ball, s, arb(h), arb(r))


# ---------------------------------------------------------------------------
# certified contour moments
# ---------------------------------------------------------------------------
class MomentFailure(Exception):
    pass


class EtaEvaluator:
    """Evaluator for f = eta(s) = (s-1) zeta(s), whose zeros inside the
    critical strip (with 0 < Im s) are exactly the nontrivial zeros of zeta.
    Using eta rather than xi avoids the Gamma factor entirely -- Gamma's ball
    enclosure is the widest ingredient of xi and is not needed here, because
    pi^{-s/2} Gamma(s/2+1) is zero-free.

    Point values use the two lowest Taylor coefficients (tight); ball bounds
    use the degree-19 Taylor model (L-0006).
    """

    name = "eta"

    def point(self, s: acb):
        return cz.eta_and_deta(s)

    def __call__(self, s: acb) -> acb:
        return cz.eta_and_deta(s)[0]

    def ball(self, centre: acb, r) -> acb:
        return cz.eta_taylor_ball(centre, r)

    def dball_sup(self, centre: acb, r) -> arb:
        return cz.deta_sup_ball(centre, r)


def _panel_bound(f, fp, centre: acb, rad: arb, wfun, kmax: int, shrinks: int = 6):
    """Upper bound, over a ball B(centre, rho) with rho <= rad, of
    |w|^kmax * |f'/f|, together with the radius actually used.

    The radius is halved until the enclosure of f over the ball provably
    excludes 0 (which is what makes f'/f analytic there, and is required by the
    Cauchy remainder estimate).  Raises MomentFailure if that never happens --
    the honest signal that a zero is on or extremely near the contour.
    """
    r = rad
    for _ in range(shrinks):
        B = acb(arb(centre.real.mid(), r.upper()), arb(centre.imag.mid(), r.upper()))
        fv = f(B)
        if not fv.contains(acb(0)):
            fpv = fp(B)
            wabs = arb(wfun(B).abs_upper())
            g_bound = (
                (wabs ** kmax if kmax > 0 else arb(1))
                * arb(fpv.abs_upper())
                / arb(fv.abs_lower())
            )
            return g_bound, r
        r = r / 2
    raise MomentFailure(
        f"contour ball may contain a zero near {centre.real.mid()}+{centre.imag.mid()}i "
        "even after shrinking"
    )


def _panel_bound_taylor(ev, centre: acb, rad: arb, wfun, kmax: int, shrinks: int = 7):
    """Same as _panel_bound but using the Taylor-model enclosures of the
    evaluator, which are ~10x tighter than naive interval evaluation."""
    r = rad
    for _ in range(shrinks):
        fv = ev.ball(centre, r)
        if not fv.contains(acb(0)):
            B = acb(arb(centre.real.mid(), r.upper()), arb(centre.imag.mid(), r.upper()))
            wabs = arb(wfun(B).abs_upper())
            g_bound = (
                (wabs ** kmax if kmax > 0 else arb(1))
                * ev.dball_sup(centre, r)
                / arb(fv.abs_lower())
            )
            return g_bound, r
        r = r / 2
    raise MomentFailure(
        f"contour ball may contain a zero near {centre.real.mid()}+{centre.imag.mid()}i "
        "even after shrinking"
    )


def contour_moments(
    x0, x1, y0, y1, kmax: int, f=None, fp=None, wfun=None,
    panel_len="0.2", rad="0.15", nsub=8, verbose=False,
):
    """Certified enclosures of

        q_k = (1/2 pi i) INT_{dD} w(s)^k f'(s)/f(s) ds ,   k = 0..kmax,

    where D = [x0,x1] x [y0,y1], by a composite 2-point Gauss-Legendre rule
    with a rigorous Cauchy remainder.

    Quadrature error control.  On a subsegment of length L the 2-point Gauss
    rule has error  (L^5/4320) * |g^{(4)}(z)|  for some z on the segment, and
    Cauchy's estimate on a ball of radius rho around the segment gives
    |g^{(4)}| <= 24 M / rho^4 where M = sup_B |g|.  Hence the certified
    per-subsegment remainder is  L^5 M / (180 rho^4).  M is computed once per
    panel from ball enclosures of f, f' and w, and rho = rad/2 (so that a ball
    of radius rho around any point of the panel stays inside the panel ball).

    Returns (list_of_acb, diagnostics).
    """
    ev = None
    if f is None:
        ev = EtaEvaluator()
        f = ev
        fp = lambda z: ev.point(z)[1]  # noqa: E731
    if fp is None:
        fp = lambda z: d_central(f, z, arb("1e-8"), arb("0.1"))  # noqa: E731
    X0, X1, Y0, Y1 = arb(x0), arb(x1), arb(y0), arb(y1)
    if wfun is None:
        c = (Y0 + Y1) / 2
        r = (Y1 - Y0) / 2
        wfun = lambda s: (s - acb(arb(1) / 2, c)) / acb(0, 1) / r  # noqa: E731

    corners = [acb(X0, Y0), acb(X1, Y0), acb(X1, Y1), acb(X0, Y1)]
    qs = [acb(0) for _ in range(kmax + 1)]
    plen = arb(panel_len)
    rr = arb(rad)
    npanels = 0
    nevals = 0
    inv_sqrt3 = 1 / arb(3).sqrt()
    total_rem = arb(0)

    for e in range(4):
        A, Bc = corners[e], corners[(e + 1) % 4]
        edge_len = arb((Bc - A).abs_upper())
        npan = max(1, int(float(edge_len / plen)) + 1)
        npanels += npan
        for p in range(npan):
            pa = A + (Bc - A) * arb(p) / npan
            pb = A + (Bc - A) * arb(p + 1) / npan
            centre = (pa + pb) / 2
            if ev is not None:
                gb, r_used = _panel_bound_taylor(ev, centre, rr, wfun, kmax)
            else:
                gb, r_used = _panel_bound(f, fp, centre, rr, wfun, kmax)
            rho = r_used / 2
            d = (pb - pa) / nsub
            L = arb(d.abs_upper())
            rem_each = (L ** 5) * gb / (180 * rho ** 4)
            total_rem += rem_each * nsub
            pad = arb(0, rem_each.upper())
            padc = acb(pad, pad)
            for i in range(nsub):
                m = pa + d * (arb(i) + arb(1) / 2)
                half = d / 2
                for node in (m - half * inv_sqrt3, m + half * inv_sqrt3):
                    u = fp(node) / f(node) * (d / 2)
                    nevals += 1
                    wv = wfun(node)
                    wk = acb(1)
                    for k in range(kmax + 1):
                        qs[k] += wk * u
                        wk = wk * wv
                for k in range(kmax + 1):
                    qs[k] += padc

    twopii = acb(0, 2 * arb.pi())
    qs = [q / twopii for q in qs]
    diag = {
        "panels": npanels,
        "nsub": nsub,
        "nodes": nevals,
        "prec": ctx.prec,
        "quadrature_remainder_bound": str(total_rem),
    }
    return qs, diag


# ---------------------------------------------------------------------------
# Hankel PSD certification
# ---------------------------------------------------------------------------
def hankel(qs, m: int):
    """The m x m Hankel matrix (q_{i+j}) as a list of lists of arb (real parts;
    the imaginary parts must be certified to contain 0, which is checked)."""
    H = []
    for i in range(m):
        row = []
        for j in range(m):
            v = qs[i + j]
            if not v.imag.contains(arb(0)):
                raise MomentFailure(
                    f"q_{i+j} has certified nonzero imaginary part {v.imag}; "
                    "the zero multiset is not conjugation-symmetric -- either "
                    "the box is not symmetric about the critical line or the "
                    "quadrature is wrong"
                )
            row.append(v.real)
        H.append(row)
    return H


def ldl_signs(H):
    """Interval LDL^T without pivoting.  Returns (verdict, diagonal entries).

    verdict = 'PD'          all pivots certified > 0  (positive definite)
              'NOT_PSD'     some pivot certified < 0  (a genuine witness!)
              'UNDECIDED'   a pivot's enclosure straddles 0
    """
    m = len(H)
    A = [row[:] for row in H]
    d = []
    for k in range(m):
        piv = A[k][k]
        d.append(piv)
        if piv < 0:
            return "NOT_PSD", d
        if not (piv > 0):
            return "UNDECIDED", d
        for i in range(k + 1, m):
            fac = A[i][k] / piv
            for j in range(k, m):
                A[i][j] = A[i][j] - fac * A[k][j]
    return "PD", d


def box_certificate(x0, x1, y0, y1, ndeg: int | None = None, **kw):
    """Full pipeline: moments -> Hankel -> PSD verdict for the rectangle."""
    qs0, diag = contour_moments(x0, x1, y0, y1, 0, **kw)
    q0 = qs0[0]
    if not q0.imag.contains(arb(0)):
        raise MomentFailure("zero count has nonzero imaginary part")
    lo, hi = float(q0.real.lower()), float(q0.real.upper())
    if hi - lo > 0.5:
        raise MomentFailure(f"zero count not pinned down: [{lo},{hi}]")
    N = round((lo + hi) / 2)
    if not (N - 0.5 < lo and hi < N + 0.5):
        raise MomentFailure(f"zero count not pinned down: [{lo},{hi}]")

    m = ndeg or N
    if m == 0:
        return {"N": 0, "verdict": "PD", "diag": diag, "pivots": []}
    qs, diag = contour_moments(x0, x1, y0, y1, 2 * m - 2, **kw)
    H = hankel(qs, m)
    verdict, d = ldl_signs(H)
    return {
        "N": N,
        "m": m,
        "verdict": verdict,
        "pivots": [str(x) for x in d],
        "moments": [str(q) for q in qs],
        "diag": diag,
    }

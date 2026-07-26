"""
pick.py -- the Nevanlinna-Pick criterion for RH, certified.

Agent: claude-01
Implements: the computational side of T-0005 / X-0011.

THE CRITERION

Because xi is entire of order 1 with zeros exactly at the nontrivial zeros of
zeta, Hadamard's factorisation gives

    F(s) := xi'(s)/xi(s)  =  sum_rho 1/(s - rho)          (paired rho, 1-rho).

If every zero lies on Re s = 1/2 then each summand maps the half-plane
Re s > 1/2 into Re w > 0, so F does too: **RH is exactly the statement that F is
a Herglotz (Nevanlinna) function of the half-plane Re s > 1/2.**

By the Nevanlinna-Pick theorem a function is Herglotz on a half-plane iff for
EVERY finite set of points alpha_1..alpha_N in it, the Pick matrix

    P_jk  =  ( F(alpha_j) + conj(F(alpha_k)) )
             / ( (alpha_j - 1/2) + conj(alpha_k - 1/2) )

is positive semidefinite.  Hence

    a certified NOT-PSD Pick matrix is a counterexample to RH,

and the witness is a finite Hermitian matrix -- the same format as T-0001
(Hermite-Hankel) and T-0002 (Weil positivity), but from a completely different
source: no contour, no primes, no zero-finding.

WHY IT MATTERS: IT BREAKS THE 1/delta WALL

Every other criterion in this repository resolves an off-line zero at depth
delta only at cost ~1/delta:

  * the classical Li coefficients need n ~ gamma^2/delta          (T-0003)
  * the Weil form needs a test function of bandwidth ~1/delta, hence
    exp(c/delta) prime powers                                     (T-0002, X-0006)
  * the targeted Li coefficients need the centre within delta of the ordinate,
    so a scan needs a grid of spacing delta                       (T-0004)
  * a winding contour must separate 1/2 - delta from 1/2          (L-0002)

The Pick matrix does not.  N points held at distance ~1 from the ordinate detect
delta = 1e-12 (measured, X-0011).  The cost moves out of the probe count and
into precision, where it is only logarithmic:

    |min pivot| ~ delta^3            (measured slope 3.0 +/- 0.6)
    baseline floor ~ 10^{-2.5 N}     (measured)
    so  N ~ (4/3) log10(1/delta) + 8  points at ~8.3 N bits suffice.

N = 1 recovers the Herglotz positivity Re F(alpha) >= 0, which by T-0004 is
exactly lambda_1^(alpha)/(2u) -- the first targeted Li coefficient.  So this is
the multi-point strengthening of T-0004, and the strengthening is what buys the
resolution.

SOUNDNESS OF THE ONE-POINT CASE (no citation needed)

Re F(1/2+u+iv) = sum_rho (u - beta_rho)/|alpha - rho|^2 with beta_rho =
Re rho - 1/2.  Every zero with Re rho <= 1/2 + u contributes a NONNEGATIVE term.
So a certified Re F < 0 forces a zero with Re rho > 1/2 + u, i.e.
|Re rho - 1/2| > u, with no domination argument anywhere.  The conclusion is
quantitative, not merely "RH is false".
"""

from __future__ import annotations

import sys

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["xi_logderiv", "pick_matrix", "ldl_hermitian", "pick_certificate",
           "probe_cluster"]


def xi_logderiv(s, tol_bits: int = 200) -> acb:
    """Certified enclosure of xi'/xi at the point s (Re s > 1/2 assumed).

    xi = pi^{-s/2} Gamma(s/2+1) eta,  so

        xi'/xi = -log(pi)/2 + psi(s/2+1)/2 + eta'/eta .

    Costs one Euler-Maclaurin evaluation (eta and eta' together) and one
    digamma.  No zero of zeta is used."""
    s = acb(s)
    e, ep = cz.eta_and_deta(s, tol_bits=tol_bits)
    if e.contains(acb(0)):
        raise ValueError("eta enclosure contains 0; cannot divide")
    return -acb(arb.pi().log()) / 2 + (s / 2 + 1).polygamma(acb(0)) / 2 + ep / e


def pick_matrix(alphas, tol_bits: int = 200, F=None):
    """The Pick matrix of F = xi'/xi at the given points, in ball arithmetic."""
    Fv = [xi_logderiv(a, tol_bits) if F is None else F(a) for a in alphas]
    al = [acb(a) for a in alphas]
    n = len(al)
    return [[(Fv[j] + Fv[k].conjugate())
             / ((al[j] - acb(1) / 2) + (al[k] - acb(1) / 2).conjugate())
             for k in range(n)] for j in range(n)]


def ldl_hermitian(P):
    """Interval Hermitian LDL^H without pivoting.

    Returns (verdict, pivots) with verdict in {'PD', 'NOT_PSD', 'UNDECIDED'}.

    Soundness of 'NOT_PSD': without pivoting the k-th pivot is
    det(P_k)/det(P_{k-1}), so a certified negative pivot means two consecutive
    leading principal minors have opposite signs, which no PSD matrix admits.
    The same argument as hermite.ldl_signs, for Hermitian rather than real
    symmetric matrices; the elimination is the ordinary Schur complement, which
    keeps Hermitian matrices Hermitian because the pivots are real."""
    n = len(P)
    A = [row[:] for row in P]
    piv = []
    for k in range(n):
        d = A[k][k].real
        piv.append(d)
        if d < 0:
            return "NOT_PSD", piv
        if not (d > 0):
            return "UNDECIDED", piv
        for i in range(k + 1, n):
            f = A[i][k] / d
            for j in range(k, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return "PD", piv


def probe_cluster(v0, v1, N, u="0.05"):
    """N points evenly spaced in [v0, v1] at height 1/2 + u.

    The measured geometry of X-0011: hold every probe at distance >= D from the
    ordinate of interest and span [v0, v1] = [gamma+D, gamma+2D]."""
    lo, hi, uu = arb(repr(v0)), arb(repr(v1)), arb(u)
    return [acb(arb(1) / 2 + uu, lo + (hi - lo) * arb(j) / (N - 1))
            for j in range(N)]


def tuned_vector(alphas, null_ordinates, opt_ordinate=None):
    """Direction v with Ahat_v(omega) = sum_j conj(v_j)/(a_j' - i omega) = 0
    at each null ordinate, chosen within that nullspace to MAXIMISE the
    delta^2 response coefficient |Ahat'(g0)|^2 + |Ahat'(-g0)|^2 over v*v
    (L-0009(iv)) when opt_ordinate = g0 is given.

    L-0009: a nulled on-line zero contributes 0 to v*Pv; every other on-line
    zero contributes |Ahat(gamma_k)|^2 >= 0; an off-line pair at a nulled
    ordinate contributes -2 delta^2 (|Ahat'|^2 sum)/... .  Certified census
    ordinates are therefore DESIGN INPUTS.

    The v produced here is a DESIGN, not a certificate: it may be computed
    non-rigorously, because tuned_form certifies q for whatever v it is
    handed.  (A first version pinned v_N = 1 in the ill-conditioned Cauchy
    solve and produced |Ahat'| ~ 1e-5 relative to |v| -- a detector that
    nulled everything, including its own sensitivity.  See X-0015.)"""
    N = len(alphas)
    k = len(null_ordinates)
    if k >= N:
        raise ValueError("need len(null_ordinates) < N")
    ap = [acb(a) - acb(1) / 2 for a in alphas]

    # -- nullspace basis of the k x N constraint matrix, by elimination ------
    M = [[1 / (ap[j] - acb(0, 1) * acb(arb(repr(w)))) for j in range(N)]
         for w in null_ordinates]
    piv_cols, r = [], 0
    for c in range(N):
        if r >= k:
            break
        best, mag = None, None
        for rr in range(r, k):
            m = float(abs(M[rr][c]).mid())
            if best is None or m > mag:
                best, mag = rr, m
        if mag is None or mag == 0.0:
            continue
        M[r], M[best] = M[best], M[r]
        for rr in range(k):
            if rr != r:
                f = M[rr][c] / M[r][c]
                for cc in range(N):
                    M[rr][cc] = M[rr][cc] - f * M[r][cc]
        piv_cols.append(c)
        r += 1
    free = [c for c in range(N) if c not in piv_cols]
    basis = []
    for fc in free:
        x = [acb(0)] * N
        x[fc] = acb(1)
        for i, pc in enumerate(piv_cols):
            x[pc] = -M[i][fc] / M[i][pc]
        basis.append(x)                       # x = conj(v) coordinates

    if opt_ordinate is None or len(basis) == 1:
        x = basis[0]
    else:
        # -- maximise x*(dd* + ee*)x / x*x over the nullspace ---------------
        g0 = acb(arb(repr(opt_ordinate)))
        d = [acb(0, 1) / (ap[j] - acb(0, 1) * g0) ** 2 for j in range(N)]
        e = [acb(0, 1) / (ap[j] + acb(0, 1) * g0) ** 2 for j in range(N)]
        # project into basis coordinates: R_{ab} = (Ba.d)(conj Bb.d) + (e term)
        m = len(basis)
        Bd = [sum(basis[a][j] * d[j] for j in range(N)) for a in range(m)]
        Be = [sum(basis[a][j] * e[j] for j in range(N)) for a in range(m)]
        Gram = [[sum(basis[a][j] * basis[b][j].conjugate() for j in range(N))
                 for b in range(m)] for a in range(m)]
        # power iteration on Gram^{-1} R (generalised eigenproblem), at mids
        y = [acb(1)] * m
        for _ in range(60):
            # z = R y  with R = Bd Bd* + Be Be*
            s1 = sum(Bd[b].conjugate() * y[b] for b in range(m))
            s2 = sum(Be[b].conjugate() * y[b] for b in range(m))
            z = [Bd[a] * s1 + Be[a] * s2 for a in range(m)]
            # solve Gram w = z  (small m: Gaussian elimination each time)
            A = [row[:] + [z[i]] for i, row in enumerate(Gram)]
            for cc in range(m):
                p = max(range(cc, m), key=lambda rr: float(abs(A[rr][cc]).mid()))
                A[cc], A[p] = A[p], A[cc]
                for rr in range(m):
                    if rr != cc:
                        f = A[rr][cc] / A[cc][cc]
                        for c2 in range(cc, m + 1):
                            A[rr][c2] = A[rr][c2] - f * A[cc][c2]
            w = [A[i][m] / A[i][i] for i in range(m)]
            nrm = sum((t * t.conjugate()).real for t in w).sqrt()
            y = [acb(arb((t / nrm).real.mid()), arb((t / nrm).imag.mid()))
                 for t in w]              # strip radii: design phase only
        x = [sum(y[a] * basis[a][j] for a in range(m)) for j in range(N)]

    # freeze the design: exact point values, then hand back v = conj(x)
    x = [acb(arb(t.real.mid()), arb(t.imag.mid())) for t in x]
    nrm = sum((t * t.conjugate()).real for t in x).sqrt()
    x = [t / nrm for t in x]
    x = [acb(arb(t.real.mid()), arb(t.imag.mid())) for t in x]
    return [t.conjugate() for t in x]


def _nullspace(ap, ordinates):
    """Basis of {x : sum_j x_j/(ap_j - i w) = 0 for each w in ordinates}."""
    N, k = len(ap), len(ordinates)
    M = [[1 / (ap[j] - acb(0, 1) * acb(arb(repr(w)))) for j in range(N)]
         for w in ordinates]
    piv_cols, r = [], 0
    for c in range(N):
        if r >= k:
            break
        best, mag = None, None
        for rr in range(r, k):
            m = float(abs(M[rr][c]).mid())
            if best is None or m > mag:
                best, mag = rr, m
        if not mag:
            continue
        M[r], M[best] = M[best], M[r]
        for rr in range(k):
            if rr != r:
                f = M[rr][c] / M[r][c]
                for cc in range(N):
                    M[rr][cc] = M[rr][cc] - f * M[r][cc]
        piv_cols.append(c)
        r += 1
    basis = []
    for fc in (c for c in range(N) if c not in piv_cols):
        x = [acb(0)] * N
        x[fc] = acb(1)
        for i, pc in enumerate(piv_cols):
            x[pc] = -M[i][fc] / M[i][pc]
        basis.append(x)
    return basis


def mvdr_vector(alphas, gamma0, window_ordinates, tail_to=4000.0,
                ridge="1e-40"):
    """Maximise the L-0009 delta^2 response at gamma0 against a modelled
    floor, SUBJECT to hard nulls Ahat(+-gamma0) = 0:

        maximise   x* R x / x* W x    over    x in null(C),

    R = response form (|Ahat'(+-gamma0)|^2), W = sum over the interference
    model of |Ahat|^2: the census window (both signs) plus a density-weighted
    pseudo-tail out to +-tail_to, which is what drives the optimiser to kill
    its own far-field moments (an explicit window alone rewards designs whose
    Ahat blows up just outside it -- measured in X-0015, design 2).

    This is an MVDR beamformer with the certified zeros as interference.  The
    output is a DESIGN, possibly non-rigorous; tuned_form certifies q for
    whatever v it is handed."""
    import math
    N = len(alphas)
    ap = [acb(a) - acb(1) / 2 for a in alphas]
    B = _nullspace(ap, [gamma0, -gamma0])
    m = len(B)
    g0 = acb(arb(repr(gamma0)))
    d = [acb(0, 1) / (ap[j] - acb(0, 1) * g0) ** 2 for j in range(N)]
    e = [acb(0, 1) / (ap[j] + acb(0, 1) * g0) ** 2 for j in range(N)]

    # interference rows: census window, then pseudo-tail at average density
    pts = [(g, 1.0) for g in window_ordinates for _ in (0,)]
    gmax = max((abs(g) for g in window_ordinates), default=abs(gamma0) + 5)
    g = gmax + 0.5
    while g < tail_to:
        step = max(0.9, g * 0.02)
        w = math.sqrt(max(math.log(g / (2 * math.pi)), 0.1) / (2 * math.pi) * step)
        pts.append((g, w))
        g += step
    rows = []
    for gg, wt in pts:
        for sgn in (1, -1):
            z = acb(arb(repr(sgn * gg)))
            rows.append([acb(arb(repr(wt))) / (ap[j] - acb(0, 1) * z)
                         for j in range(N)])

    # project everything into the nullspace basis
    def proj(vec):
        return [sum(vec[j].conjugate() * B[a][j] for j in range(N)).conjugate()
                for a in range(m)]
    dR, eR = proj(d), proj(e)
    rowsR = [proj(r) for r in rows]
    Gram = [[sum(B[a][j] * B[b][j].conjugate() for j in range(N))
             for b in range(m)] for a in range(m)]
    W = [[sum(r[i] * r[j].conjugate() for r in rowsR)
          + acb(arb(ridge)) * Gram[i][j] for j in range(m)] for i in range(m)]

    y = [acb(1)] * m
    for _ in range(80):
        s1 = sum(dR[b].conjugate() * y[b] for b in range(m))
        s2 = sum(eR[b].conjugate() * y[b] for b in range(m))
        z = [dR[a] * s1 + eR[a] * s2 for a in range(m)]
        A = [row[:] + [z[i]] for i, row in enumerate(W)]
        for c in range(m):
            p = max(range(c, m), key=lambda rr: float(abs(A[rr][c]).mid()))
            A[c], A[p] = A[p], A[c]
            for rr in range(m):
                if rr != c:
                    f = A[rr][c] / A[c][c]
                    for cc in range(c, m + 1):
                        A[rr][cc] = A[rr][cc] - f * A[c][cc]
        w = [A[i][m] / A[i][i] for i in range(m)]
        nrm = sum((t * t.conjugate()).real for t in w).sqrt()
        y = [acb(arb((t / nrm).real.mid()), arb((t / nrm).imag.mid()))
             for t in w]
    x = [sum(y[a] * B[a][j] for a in range(m)) for j in range(N)]
    x = [acb(arb(t.real.mid()), arb(t.imag.mid())) for t in x]
    nrm = sum((t * t.conjugate()).real for t in x).sqrt()
    x = [acb(arb((t / nrm).real.mid()), arb((t / nrm).imag.mid())) for t in x]
    return [t.conjugate() for t in x]


def tuned_form(alphas, v, tol_bits: int = 200, F=None):
    """The scalar statistic q = v* P v.  Certified q < 0 refutes RH (T-0005 +
    L-0008: P is a sum of PSD matrices under RH, so every quadratic form is
    >= 0).  The witness is one real ball plus the pair (alphas, v)."""
    P = pick_matrix(alphas, tol_bits, F=F)
    n = len(v)
    q = sum(v[j].conjugate() * P[j][k] * v[k]
            for j in range(n) for k in range(n)).real
    vv = sum((z * z.conjugate()).real for z in v)
    return q / vv


def ldl_witness_direction(P):
    """Given a Pick matrix whose LDL has a negative pivot, return the witness
    direction x with x* P x = d_k, by the exact identity x = L^{-*} e_k.

    The point (X-0015): when the LDL search fires NOT_PSD, this converts the
    matrix verdict into the COMPACT witness (probes, x, q): a verifier needs
    only the N values of xi'/xi and O(N^2) arithmetic to certify q < 0 --
    no factorisation, and by L-0008 the soundness of "q < 0 refutes RH" does
    not depend on where x came from.  Runs on midpoints (the design may be
    non-rigorous; the certification of q is not its job).  Returns None if no
    pivot midpoint is negative."""
    N = len(P)
    A = [[acb(arb(P[i][j].real.mid()), arb(P[i][j].imag.mid()))
          for j in range(N)] for i in range(N)]
    L = [[acb(1) if i == j else acb(0) for j in range(N)] for i in range(N)]
    kneg = None
    for k in range(N):
        if float(A[k][k].real.mid()) < 0:
            kneg = k
            break
        for i in range(k + 1, N):
            f = A[i][k] / A[k][k]
            L[i][k] = f
            for j in range(k, N):
                A[i][j] = A[i][j] - f * A[k][j]
    if kneg is None:
        return None
    x = [acb(0)] * N
    x[kneg] = acb(1)
    for i in range(kneg - 1, -1, -1):
        x[i] = -sum(L[j][i].conjugate() * x[j] for j in range(i + 1, kneg + 1))
    return [acb(arb(t.real.mid()), arb(t.imag.mid())) for t in x]


def pick_certificate(alphas, tol_bits: int = 200, F=None):
    """Full pipeline: evaluate F, build the Pick matrix, take the LDL verdict."""
    P = pick_matrix(alphas, tol_bits, F=F)
    verdict, piv = ldl_hermitian(P)
    return {
        "N": len(alphas),
        "verdict": verdict,
        "min_pivot": min(float(p.mid()) for p in piv),
        "min_pivot_rad": max(float(p.rad()) for p in piv),
        "pivots": [str(p) for p in piv],
        "refutes_rh": verdict == "NOT_PSD",
    }

"""
[!] WARNING (added after PR #173 review): the inertia routine in this file uses 1x1
    diagonal pivots only and returns (0,0,2) on [[0,1],[1,0]], whose true inertia is
    (1,1,0) -- it cannot see a hyperbolic negative direction.  Use inertia_correct.py
    instead.  Re-running this file's published tables with the correct routine
    reproduced them identically, but do not reuse the routine below.
"""
"""What does the finite Weil form think the zeros are?  The moment test.

L-16006(b): Q induces an inner product on P_{2N} through Phi: x -> P_x.  L-16006(c): if the
source is a pole sum with positive weights, that inner product is L^2(nu) for a positive
measure nu on the poles.  L-16006 sec 4 showed the ARITHMETIC form's inner product is NOT
L^2(nu_zeta).  So: does it have a representing measure AT ALL, and if so, where?

Phi is invertible in closed form.  From P_x(s) = Omega(s)<x, ell(s)> and Omega(lam_j) = 0,

        P_x(lam_j) = x_j * prod_{k != j}(lam_k - lam_j)      =>    x_j = P(lam_j) * w_j,
        w_j := 1 / prod_{k != j}(lam_k - lam_j).

Hence     <P,R>_Q = sum_{i,j} P(lam_i) Qt_{ij} R(lam_j),      Qt_{ij} := w_i Q_{ij} w_j.

Define    M_{ab} := <s^a, s^b>_Q = sum_{ij} lam_i^a Qt_{ij} lam_j^b,   0 <= a,b <= 2N.

THE TEST.  The form is a moment functional -- equivalently it has a representing measure on
R -- if and only if M_{ab} depends only on a+b, i.e. M is HANKEL.  This is NOT automatic for
a general positive definite form.  For a pole-sum source it holds exactly, with
mu_k = sum_mu a_mu mu^k / Omega(mu)^2.

So measure the Hankel defect of the arithmetic M.  If it is small, extract the measure:
the Hankel moment matrix H_{ab} = mu_{a+b} has orthogonal polynomials whose roots are the
GAUSS NODES and whose Christoffel numbers are the WEIGHTS -- that is the honest answer to
"where does the finite Weil form put its mass".

HIGH-PRECISION FLOAT.  Everything is scaled before comparison, since lam^a spans ~10^20.
"""
import sys; sys.path.insert(0, '.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve, polyroots
import x0001

GAM = [mpf(v) for v in ['14.134725141734693790', '21.022039638771554993',
                        '25.010857580145688763', '30.424876125859513210',
                        '32.935061587739189691', '37.586178158825671257']]


def analyse(cut, N, dps, label):
    mp.mp.dps = dps
    A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=dps)
    d = 2 * N + 1
    nodes = [mpf(k) for k in range(-N, N + 1)]
    w = []
    for j in range(d):
        p = mpf(1)
        for k in range(d):
            if k != j:
                p *= (nodes[k] - nodes[j])
        w.append(1 / p)
    Qt = [[w[i] * A[i, j] * w[j] for j in range(d)] for i in range(d)]
    # M_{ab}
    V = [[nodes[i] ** a for a in range(d)] for i in range(d)]     # V[i][a] = lam_i^a
    M = [[sum(V[i][a] * Qt[i][j] * V[j][b] for i in range(d) for j in range(d))
          for b in range(d)] for a in range(d)]
    # Hankel defect: for each k = a+b, compare all M_{ab} with a+b = k
    worst = mpf(0); worst_k = None
    mus = []
    for k in range(2 * d - 1):
        vals = [M[a][k - a] for a in range(max(0, k - d + 1), min(d - 1, k) + 1)]
        m = sum(vals) / len(vals)
        mus.append(m)
        sc = max(abs(v) for v in vals)
        if sc > 0 and len(vals) > 1:
            spread = max(abs(v - m) for v in vals) / sc
            if spread > worst:
                worst, worst_k = spread, k
    print(f"--- {label}: cutoff {cut}, N={N}, dim={d}, dps={dps} ---")
    print(f"  worst RELATIVE Hankel defect over all antidiagonals: {nstr(worst,5)}  (at a+b={worst_k})")
    print(f"    [0 would mean the form IS a moment functional / has a representing measure]")
    # Even if not exactly Hankel, the SYMMETRISED moments mus[] define a candidate measure.
    # Test it: is the Hankel matrix of mus positive definite?  (Hamburger: PD => a measure exists.)
    H = [[mus[a + b] for b in range(d)] for a in range(d)]
    piv = []
    B = [row[:] for row in H]
    ok = True
    for kk in range(d):
        best = max(range(kk, d), key=lambda t: abs(B[t][t]))
        if best != kk:
            B[kk], B[best] = B[best], B[kk]
            for r in range(d):
                B[r][kk], B[r][best] = B[r][best], B[r][kk]
        dd = B[kk][kk]; piv.append(dd)
        if dd == 0:
            ok = False; break
        for i in range(kk + 1, d):
            f = B[i][kk] / dd
            for j in range(kk, d):
                B[i][j] -= f * B[kk][j]
            for j in range(kk, d):
                B[j][i] = B[i][j]
    npos = sum(1 for p in piv if p > 0); nneg = sum(1 for p in piv if p < 0)
    print(f"  symmetrised Hankel matrix inertia (LDL pivots): ({npos},{nneg},{d-npos-nneg})"
          f"   -> representing measure {'plausible' if nneg == 0 else 'RULED OUT (not PD)'}")
    # Gauss nodes of the ACTUAL form: roots of the monic degree-2N orthogonal polynomial,
    # which by L-16006(b) is P_xi.  Christoffel weights from the quadrature conditions.
    x = lu_solve(A, matrix([1] * d))
    ts = 1 / sum(x[i] for i in range(d))
    xi = [x[i] * ts for i in range(d)]
    Om = [mpf(1)]
    for k in nodes:
        Om = [(Om[i - 1] if i > 0 else mpf(0)) * (-1) + (Om[i] * k if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * d
    for a, lj in enumerate(nodes):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * lj; Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xi[a] * Qj[i]
    rts = polyroots(P[::-1], maxsteps=600, extraprec=25 * dps)
    nds = sorted([mp.re(r) for r in rts if abs(mp.im(r)) < mpf(10) ** (-20) * max(1, abs(mp.re(r)))])
    # Christoffel weights: solve the Vandermonde system sum_i W_i nds_i^k = mus[k], k=0..2N-1
    n = len(nds)
    if n == 2 * N:
        VA = matrix(n, n)
        rhs = matrix(n, 1)
        for k in range(n):
            for i in range(n):
                VA[k, i] = nds[i] ** k
            rhs[k] = mus[k]
        try:
            W = lu_solve(VA, rhs)
            L = mp.log(mpf(cut))
            tot = sum(abs(W[i]) for i in range(n))
            print(f"  Gauss nodes (positive half) in w = 2 pi r / L, with Christoffel weight fraction:")
            for i in range(n // 2, n):
                ww = 2 * mp.pi * nds[i] / L
                near = min(GAM, key=lambda g: abs(g - ww))
                tag = f"~gamma (rel {nstr(abs(ww-near)/near,2)})" if abs(ww - near) / near < mpf('1e-2') else ""
                print(f"     w={nstr(ww,10):>14}   weight frac {nstr(abs(W[i])/tot,4):>10}   "
                      f"sign {'+' if W[i] > 0 else '-'}   {tag}")
            print(f"  any NEGATIVE Christoffel weight? "
                  f"{'YES -- no positive representing measure with these nodes' if any(W[i] < 0 for i in range(n)) else 'no'}")
        except Exception as e:
            print(f"  weight solve failed: {type(e).__name__}")
    print()


for cut, N, dps in [('200', 4, 120), ('2000', 4, 120), ('2000', 6, 160), ('2000', 8, 220)]:
    analyse(cut, N, dps, "arithmetic Weil form")

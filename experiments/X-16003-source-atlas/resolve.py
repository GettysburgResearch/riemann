"""Resolve the apparent conflict between O-16004 (roots -> zeta zeros) and the e2
report (roots interlace the integer nodes).  Print the RAW roots, the node set,
and an explicit interlacing test.  Nothing is converted until after the test."""
import sys; sys.path.insert(0, '.')
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots
import x0001

mp.dps = 60

def build_P(xis, N):
    idx = list(range(-N, N + 1))
    Om = [mpf(1)]
    for k in idx:
        Om = [(Om[i-1] if i > 0 else mpf(0)) * (-1) + (Om[i] * mpf(k) if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * (2 * N + 1)
    for a, j in enumerate(idx):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * mpf(j); Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xis[a] * Qj[i]
    return P

for cut, N in [('500', 6), ('2000', 10)]:
    A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=60)
    dim = A.rows
    eta = matrix([1] * dim)
    x = lu_solve(A, eta)
    denom = sum(x[i] for i in range(dim))
    tstar = 1 / denom
    xi = [x[i] * tstar for i in range(dim)]
    P = build_P(xi, N)
    rts = polyroots(P[::-1], maxsteps=400, extraprec=3000)
    rr = sorted([mp.re(r) for r in rts if abs(mp.im(r)) < mpf(10)**(-25) * max(1, abs(mp.re(r)))])
    L = mp.log(mpf(cut))
    print(f"=== X-0001, cutoff {cut}, N={N}, nodes = -{N}..{N}, deg P = {len(P)-1} ===")
    print(f"  #real roots {len(rr)} of {len(P)-1}")
    print(f"  RAW roots  : {[nstr(v, 8) for v in rr]}")
    print(f"  in (-N,N)? : {[bool(-N < v < N) for v in rr]}")
    print(f"  2pi r / L  : {[nstr(2*mp.pi*v/L, 9) for v in rr]}")
    # explicit interlacing test: sign of P at the nodes
    def peval(P, s):
        acc = mpf(0)
        for c in reversed(P):
            acc = acc * s + c
        return acc
    sg = [int(mp.sign(peval(P, mpf(k)))) for k in range(-N, N + 1)]
    print(f"  sign P at nodes -N..N : {sg}")
    alt = all(sg[i] * sg[i+1] < 0 for i in range(len(sg) - 1))
    print(f"  strictly alternating at nodes (=> full interlacing)? {alt}")
    # normalised kernel vector, and the CvS centring (-1)^j
    m = max(abs(v) for v in xi)
    print(f"  xi/max      : {[nstr(v/m, 6) for v in xi]}")
    print(f"  (-1)^j xi_j : {[nstr((-1)**j * xi[a]/m, 6) for a, j in enumerate(range(-N, N+1))]}")
    print()

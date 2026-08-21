"""How many zeta zeros does the finite Weil gate actually resolve, and what buys resolution?

L-16006(c) says the kernel polynomial's roots are Gauss nodes for a measure whose atom
weights carry the factor Omega(mu)^{-2}, and Omega(s) = prod_{k=-N}^{N}(k-s) depends ONLY
on the nodes -- not on the prime cutoff c.  PREDICTION: the number of zeros resolved is
controlled by N alone, and raising c buys little or nothing.

That is a falsifiable and practically important claim (it says where to spend compute), so
test it: count how many gamma_j are recovered to 1e-3 / 1e-6 / 1e-9 relative, over a grid
in (c, N).

HIGH-PRECISION FLOAT (mpmath).  Nothing certified.
"""
import sys, time; sys.path.insert(0, '.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve, polyroots
import x0001

GAM = [mpf(v) for v in [
    '14.134725141734693790', '21.022039638771554993', '25.010857580145688763',
    '30.424876125859513210', '32.935061587739189691', '37.586178158825671257',
    '40.918719012147495187', '43.327073280914999519', '48.005150881167159727',
    '49.773832477672302182', '52.970321477714460644', '56.446247697063394805']]


def build_P(xis, N):
    nodes = [mpf(k) for k in range(-N, N + 1)]
    Om = [mpf(1)]
    for k in nodes:
        Om = [(Om[i - 1] if i > 0 else mpf(0)) * (-1) + (Om[i] * k if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * len(nodes)
    for a, lj in enumerate(nodes):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * lj; Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xis[a] * Qj[i]
    return P


CUTS = ['50', '200', '1000', '5000', '20000']
NS = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("count of gamma_j recovered to the stated RELATIVE tolerance, as (1e-3 / 1e-6 / 1e-9)")
print(f"{'N':>3} | " + " | ".join(f"c={c:>7}" for c in CUTS))
print("-" * (6 + 13 * len(CUTS)))
grid = {}
for N in NS:
    dps = 40 + 6 * N
    cells = []
    for cut in CUTS:
        t0 = time.time()
        try:
            mp.mp.dps = dps
            A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=dps)
            dim = A.rows
            x = lu_solve(A, matrix([1] * dim))
            ts = 1 / sum(x[i] for i in range(dim))
            xi = [x[i] * ts for i in range(dim)]
            P = build_P(xi, N)
            rts = polyroots(P[::-1], maxsteps=600, extraprec=20 * dps)
            L = mp.log(mpf(cut))
            ws = sorted([2 * mp.pi * mp.re(r) / L for r in rts
                         if abs(mp.im(r)) < mpf(10) ** (-15) * max(1, abs(mp.re(r))) and mp.re(r) > 0])
            cnt = []
            for tol in ('1e-3', '1e-6', '1e-9'):
                k = 0
                while k < min(len(ws), len(GAM)) and abs(ws[k] - GAM[k]) / GAM[k] < mpf(tol):
                    k += 1
                cnt.append(k)
            grid[(cut, N)] = cnt
            cells.append(f"{cnt[0]}/{cnt[1]}/{cnt[2]}".rjust(9))
        except Exception as e:
            cells.append("   err   ")
    print(f"{N:>3} | " + " | ".join(c.rjust(9) for c in cells))
    sys.stdout.flush()

print()
print("Same data, read the two ways that matter:")
for cut in CUTS:
    v = [grid.get((cut, N), [0, 0, 0])[1] for N in NS]
    print(f"  at c={cut:>7} fixed, zeros to 1e-6 vs N={NS}: {v}")
print()
for N in NS:
    v = [grid.get((cut, N), [0, 0, 0])[1] for cut in CUTS]
    print(f"  at N={N:>2} fixed, zeros to 1e-6 vs c={CUTS}: {v}")

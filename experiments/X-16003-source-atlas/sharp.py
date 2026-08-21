"""t*(N,c) = min { x^T Q_W x : sum_j x_j = 1 }  --  the minimum of the truncated Weil
functional over normalised test vectors (L-16006(b)).

The pilot suggested  t* * N * log(c)  is roughly constant.  Map it properly and look for
drift.  Precision discipline: Q_W is ferociously ill-conditioned (spectrum cascades like
10^{-4.5N}), so the solve loses ~4.5N digits.  Use dps = 40 + 6N and REPEAT every row at
2x dps, reporting the agreement.  A row whose two precisions disagree is not reported as
a measurement.

HIGH-PRECISION FLOAT throughout.  Nothing certified.
"""
import sys, time; sys.path.insert(0, '.')
from mpmath import mp, mpf, nstr, matrix, lu_solve
import x0001

CUTS = ['50', '200', '1000', '5000', '20000', '100000']
NS = [2, 4, 6, 8, 10, 12, 14, 16]


def tstar(cut, N, dps):
    mp.dps = dps
    A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=dps)
    dim = A.rows
    x = lu_solve(A, matrix([1] * dim))
    return 1 / sum(x[i] for i in range(dim))


print(f"{'cut':>7} {'L=log c':>9} {'N':>3} {'dps':>4} {'t*':>18} {'agree':>9} "
      f"{'t* * N * L':>12} {'t* * N':>12} {'t* * L':>12}  time")
print("-" * 108)
rows = []
for cut in CUTS:
    for N in NS:
        dps = 40 + 6 * N
        t0 = time.time()
        try:
            a = tstar(cut, N, dps)
            b = tstar(cut, N, 2 * dps)
        except Exception as e:
            print(f"{cut:>7} {'':>9} {N:>3} {dps:>4}  FAILED: {e}")
            continue
        mp.dps = 30
        rel = abs(a - b) / abs(b) if b != 0 else mpf(1)
        L = mp.log(mpf(cut))
        ok = rel < mpf(10) ** (-12)
        rows.append((cut, float(L), N, float(b), float(rel), ok))
        print(f"{cut:>7} {nstr(L,7):>9} {N:>3} {dps:>4} {nstr(b,12):>18} {nstr(rel,3):>9} "
              f"{nstr(b*N*L,8):>12} {nstr(b*N,8):>12} {nstr(b*L,8):>12}  {time.time()-t0:6.1f}s")
        sys.stdout.flush()

print()
good = [r for r in rows if r[5]]
if good:
    K = [r[3] * r[2] * r[1] for r in good]
    print(f"t* * N * log c  over {len(good)} converged points:")
    print(f"   min {min(K):.6f}   max {max(K):.6f}   mean {sum(K)/len(K):.6f}   spread {max(K)/min(K):.4f}x")
    for lbl, f in (("t* * N", lambda r: r[3]*r[2]), ("t* * L", lambda r: r[3]*r[1]),
                   ("t* * N * L", lambda r: r[3]*r[2]*r[1]),
                   ("t* * N * L^2", lambda r: r[3]*r[2]*r[1]**2),
                   ("t* * N^2 * L", lambda r: r[3]*r[2]**2*r[1]),
                   ("t* * (2N+1) * L", lambda r: r[3]*(2*r[2]+1)*r[1])):
        v = [f(r) for r in good]
        print(f"   {lbl:<18} spread {max(v)/min(v):8.4f}x   mean {sum(v)/len(v):.6f}")

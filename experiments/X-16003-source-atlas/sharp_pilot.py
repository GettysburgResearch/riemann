"""PILOT: cost of mapping t*(N, c) = min { x^T Q_W x : sum_j x_j = 1 }.

By L-16006(b) this is the minimum of the truncated Weil functional over normalised
test vectors in the span of the first 2N+1 CvS modes.  It needs ONE linear solve,
not an inertia -- so it should be much cheaper than the congruence scans.

Time a few points, then extrapolate before committing to the full grid.
"""
import sys, time; sys.path.insert(0, '.')
from mpmath import mp, mpf, nstr, matrix, lu_solve
import x0001

for dps, cut, N in [(60, '500', 4), (60, '500', 8), (60, '5000', 8), (60, '50000', 6), (90, '500', 12)]:
    mp.dps = dps
    t0 = time.time(); A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=dps); tb = time.time() - t0
    dim = A.rows
    t0 = time.time()
    x = lu_solve(A, matrix([1] * dim))
    ts = 1 / sum(x[i] for i in range(dim))
    tl = time.time() - t0
    L = mp.log(mpf(cut))
    print(f"dps={dps:3d} cut={cut:>6} N={N:2d} dim={dim:3d}  build {tb:7.2f}s  solve {tl:6.2f}s  "
          f"t*={nstr(ts,10):>16}  L={nstr(L,6)}  t*L={nstr(ts*L,8)}  t*L*N={nstr(ts*L*N,8)}")

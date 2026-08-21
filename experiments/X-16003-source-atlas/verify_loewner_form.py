"""Independent check of the atlas headline: is the X-0001 cutoff-free Weil matrix of Loewner form?
Test (L1): D_ij := (i-j)*Q_ij must be a coboundary psi_i - psi_j, equivalently
           D_ij + D_jk + D_ki = 0 on every triple.  Normalization-independent."""
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, nstr
import x0001

for dps, c, N in [(60,'100',5),(60,'200',5),(80,'200',7)]:
    mp.dps = dps
    A,meta = x0001.build_cutoff_free_matrix(c, N, dps=dps)
    dim = 2*N+1
    idx = [i-N for i in range(dim)]
    # scale of the matrix, for a relative statement
    scale = max(abs(A[i,j]) for i in range(dim) for j in range(dim))
    # cocycle defect on all triples
    worst = mpf(0); worst_t=None
    for a in range(dim):
        for b in range(a+1,dim):
            for cc in range(b+1,dim):
                i,j,k = idx[a],idx[b],idx[cc]
                D_ij = (i-j)*A[a,b]; D_jk=(j-k)*A[b,cc]; D_ki=(k-i)*A[cc,a]
                d = abs(D_ij+D_jk+D_ki)
                if d>worst: worst, worst_t = d, (i,j,k)
    # recover psi from row 0 and verify every off-diagonal entry
    psi = [mpf(0)]*dim
    for b in range(1,dim):
        psi[b] = psi[0] - (idx[0]-idx[b])*A[0,b]
    off_worst = mpf(0)
    for a in range(dim):
        for b in range(dim):
            if a==b: continue
            pred = (psi[a]-psi[b])/(idx[a]-idx[b])
            off_worst = max(off_worst, abs(pred-A[a,b]))
    # is the recovered source ODD?
    oddness = max(abs(psi[i]+psi[dim-1-i]-(psi[N]+psi[N])) for i in range(dim))
    print(f"dps={dps} c={c} N={N}  matrix scale={nstr(scale,4)}")
    print(f"   worst cocycle defect over all triples : {nstr(worst,4)}   (relative {nstr(worst/scale,4)})")
    print(f"   worst off-diagonal reconstruction err : {nstr(off_worst,4)}   (relative {nstr(off_worst/scale,4)})")
    print(f"   recovered psi at nodes -N..N          : {[nstr(p,6) for p in psi[:4]]} ...")
    print(f"   oddness residual (psi_n + psi_-n cst) : {nstr(oddness,4)}")
    print()

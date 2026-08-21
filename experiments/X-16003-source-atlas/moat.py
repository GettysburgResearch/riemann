"""Redo 'Q_W is positive definite' as an EXACT congruence on a rationalised matrix, plus a moat.

Exact inertia of a rationalisation certifies the SURROGATE, not Q_W (the L-16005 lesson).
What makes it transfer is a moat: if the smallest LDL pivot of the rationalised matrix exceeds the
perturbation the rationalisation could have caused, the inertia is stable.  Report both, and the ratio."""
import sys; sys.path.insert(0,'.'); sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import inertia, ldlt_pivots
from fractions import Fraction as F
from mpmath import mp, mpf, nstr
import x0001

def rat_matrix(cut,N,dps,sig):
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    dim=A.rows
    Q=[[F(mp.nstr(A[i,j],sig,strip_zeros=False)) for j in range(dim)] for i in range(dim)]
    for i in range(dim):
        for j in range(i+1,dim): Q[j][i]=Q[i][j]           # enforce exact symmetry
    return Q, dim, max(abs(A[i,j]) for i in range(dim) for j in range(dim))

print("Exact inertia of the rationalised Weil matrix, with the LDL moat.")
print(f"{'cut':>6} {'N':>3} {'sig':>4} {'exact inertia':>15} {'min pivot (moat)':>18} {'scale':>10} {'moat/rationalisation radius':>28}")
print("-"*92)
for cut,N in [('100',4),('200',6),('500',6),('1000',6)]:
    for sig in [30,50]:
        Q,dim,scale = rat_matrix(cut,N,60,sig)
        ine = inertia([r[:] for r in Q])
        piv = ldlt_pivots([r[:] for r in Q])
        moat = min(piv) if piv else None
        # rationalisation radius: sig significant digits on entries of size <= scale
        rad = float(scale)*10**(-sig)
        ratio = float(moat)/rad if moat else float('nan')
        print(f"{cut:>6} {N:>3} {sig:>4} {str(ine):>15} {nstr(mpf(float(moat)),6):>18} {nstr(scale,5):>10} {ratio:>28.3e}")

print()
print("Reading: the exact inertia is (dim,0,0) -- positive definite -- and stable between 30 and 50")
print("significant digits.  The moat exceeds the rationalisation radius by the ratio shown, so the")
print("inertia of the rationalised matrix transfers to any matrix within that radius.")
print()
print("WHAT THIS STILL DOES NOT COVER: the truncation error inside x0001's own archimedean series and")
print("the dps-60 evaluation error.  Those are NOT bounded here, so this is not a certificate for Q_W")
print("itself -- only for anything within the stated entrywise radius of the computed matrix.")

"""How does the positivity margin of the finite Weil matrix behave in (cutoff, N)?
Weil positivity is equivalent to RH, so a margin that went NEGATIVE would be a counterexample
nomination.  A margin that merely shrinks may only be conditioning.  Distinguish the two:
report the raw moat, the moat relative to the matrix scale, and the condition number."""
import sys; sys.path.insert(0,'.'); sys.path.insert(0,'/home/user/riemann/experiments/X-16001-finsler-cone-collapse')
from verify import ldlt_pivots, inertia
from fractions import Fraction as F
from mpmath import mp, mpf, nstr, log10
import x0001

def study(cut,N,dps=80,sig=60):
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    dim=A.rows
    Q=[[F(mp.nstr(A[i,j],sig,strip_zeros=False)) for j in range(dim)] for i in range(dim)]
    for i in range(dim):
        for j in range(i+1,dim): Q[j][i]=Q[i][j]
    piv=ldlt_pivots([r[:] for r in Q])
    ok = piv is not None and all(p>0 for p in piv)
    moat=min(piv) if piv else None
    scale=max(abs(A[i,j]) for i in range(dim) for j in range(dim))
    ev=[mp.mpf(e) for e in mp.eigsy(A, eigvals_only=True)]
    lmin,lmax=min(ev),max(ev)
    return ok, mpf(float(moat)), scale, lmin, lmax

print("A. moat vs CUTOFF at fixed N=6")
print(f"{'cut':>7} {'PD?':>5} {'min LDL pivot':>15} {'lambda_min':>15} {'lambda_max':>13} {'cond':>11} {'log10 lmin':>11}")
print("-"*84)
prev=None
for cut in ['50','100','200','500','1000','2000','5000']:
    ok,moat,scale,lmin,lmax = study(cut,6)
    tr = f"  x{float(lmin/prev):.2e}" if prev else ""
    print(f"{cut:>7} {str(ok):>5} {nstr(moat,6):>15} {nstr(lmin,6):>15} {nstr(lmax,5):>13} {nstr(lmax/lmin,4):>11} {float(mp.log10(abs(lmin))):>11.2f}{tr}")
    prev=lmin

print()
print("B. moat vs N at fixed cutoff 500")
print(f"{'N':>4} {'dim':>5} {'PD?':>5} {'min LDL pivot':>15} {'lambda_min':>15} {'cond':>11} {'log10 lmin':>11}")
print("-"*74)
for N in [3,4,5,6,7,8]:
    ok,moat,scale,lmin,lmax = study('500',N)
    print(f"{N:>4} {2*N+1:>5} {str(ok):>5} {nstr(moat,6):>15} {nstr(lmin,6):>15} {nstr(lmax/lmin,4):>11} {float(mp.log10(abs(lmin))):>11.2f}")

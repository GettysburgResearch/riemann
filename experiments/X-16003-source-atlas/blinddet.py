"""
[!] WARNING (added after PR #173 review): the inertia routine in this file uses 1x1
    diagonal pivots only and returns (0,0,2) on [[0,1],[1,0]], whose true inertia is
    (1,1,0) -- it cannot see a hyperbolic negative direction.  Use inertia_correct.py
    instead.  Re-running this file's published tables with the correct routine
    reproduced them identically, but do not reuse the routine below.
"""
"""Combining O-16007 (residue law) with O-16008 (detectability).

O-16007: the finite Weil form weights the zero gamma by a(gamma) = (log c/pi^2) sin^2(gamma log c/2),
which VANISHES at the "blind" cutoffs where gamma*Delta is an integer.

O-16008: an off-line zero is detectable only when it moves lambda_min above the conditioning floor.

PREDICTION: at a blind cutoff the form should be far LESS able to detect an off-line gamma_1,
because it is weighting that zero by almost nothing.  Test it: build the zero-side Loewner form
with the MEASURED residues (not unit residues), displace gamma_1, and find the critical
displacement delta_c as a function of the cutoff.  If delta_c spikes exactly at the blind
cutoffs, the two claims lock together.  If it does not, one of them is wrong.
"""
import mpmath as mp
from mpmath import mpf, mpc, nstr

GAMS=None
def gammas(n=30):
    global GAMS
    if GAMS is None or len(GAMS)<n:
        GAMS=[mp.im(mp.zetazero(k)) for k in range(1,n+1)]
    return GAMS[:n]

def build(L, N, M, d, dps):
    """Zero-side Loewner form with O-16007 residues; gamma_1 displaced by d (in node units)."""
    mp.mp.dps=dps
    Delta=L/(2*mp.pi)
    dim=2*N+1
    nodes=[mpf(k) for k in range(-N,N+1)]
    Q=[[mpf(0)]*dim for _ in range(dim)]
    for idx,g in enumerate(gammas(M)):
        a=(L/mp.pi**2)*mp.sin(g*L/2)**2
        mu=g*Delta
        if idx==0 and d>0:
            pts=[(mu+mpc(0,1)*d,a/2),(mu-mpc(0,1)*d,a/2),(-mu+mpc(0,1)*d,a/2),(-mu-mpc(0,1)*d,a/2)]
        else:
            pts=[(mu,a),(-mu,a)]
        for m,wt in pts:
            ell=[1/(nodes[j]-m) for j in range(dim)]
            for i in range(dim):
                for j in range(dim):
                    Q[i][j]+=mp.re(wt*ell[i]*ell[j])
    return Q

def nneg(Q):
    n=len(Q);A=[r[:] for r in Q];piv=[]
    for k in range(n):
        b=max(range(k,n),key=lambda t:abs(A[t][t]))
        if b!=k:
            A[k],A[b]=A[b],A[k]
            for r in range(n): A[r][k],A[r][b]=A[r][b],A[r][k]
        dd=A[k][k];piv.append(dd)
        if dd==0: continue
        for i in range(k+1,n):
            f=A[i][k]/dd
            for j in range(k,n): A[i][j]-=f*A[k][j]
            for j in range(k,n): A[j][i]=A[i][j]
    tol=max(abs(p) for p in piv)*mpf(10)**(-mp.mp.dps+12)
    return sum(1 for p in piv if p<-tol), min(piv)

def delta_c(L,N,M,dps,lo=mpf('1e-40'),hi=mpf('1e3')):
    if nneg(build(L,N,M,hi,dps))[0]==0: return None
    if nneg(build(L,N,M,lo,dps))[0]>0: return lo
    for _ in range(55):
        mid=mp.sqrt(lo*hi)
        if nneg(build(L,N,M,mid,dps))[0]>0: hi=mid
        else: lo=mid
    return mp.sqrt(lo*hi)

N,M,dps=10,25,150
G1=None
mp.mp.dps=dps
G1=gammas(1)[0]
print(f"N={N}, M={M} zeros, dps={dps}.  Blind cutoffs for gamma_1: log c = 2 pi k / gamma_1 = 0.44454 k")
print(f"{'c':>9} {'L=log c':>9} {'g1*Delta':>10} {'frac':>7} {'a_1':>13} {'unperturbed n_-':>16} "
      f"{'delta_c':>13} {'delta_c/a_1':>13}")
print("-"*104)
for c in ['9.23136','11.529','14.3985','17.9823','22.458','28.0478','35.0288','43.7473','54.6359']:
    mp.mp.dps=dps
    L=mp.log(mpf(c))
    r1=G1*L/(2*mp.pi)
    frac=r1-mp.floor(r1)
    a1=(L/mp.pi**2)*mp.sin(G1*L/2)**2
    ne,minp=nneg(build(L,N,M,mpf(0),dps))
    dc=delta_c(L,N,M,dps)
    mp.mp.dps=25
    tag=""
    if abs(frac-mp.floor(frac+mpf('0.5')))<mpf('0.03') or frac<0.03 or frac>0.97: tag="  <-- near-BLIND"
    print(f"{c:>9} {nstr(L,7):>9} {nstr(r1,8):>10} {nstr(frac,3):>7} {nstr(a1,8):>13} {ne:>16} "
          f"{(nstr(dc,7) if dc else 'never'):>13} {(nstr(dc/a1,6) if dc else '-'):>13}{tag}")

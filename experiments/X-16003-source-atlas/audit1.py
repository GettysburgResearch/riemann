"""Verify the reviewer's two invalidating claims before patching anything.

(A) INERTIA BUG. Several of my routines use 1x1 diagonal pivots only and 'continue' on a
    zero pivot. On [[0,1],[1,0]], whose true inertia is (1,1,0), they should wrongly report
    no negative direction. Check every routine I shipped.

(B) THE PHYSICS BUG in blinddet.py. The reviewer's identity is
        g_u(z) = (L/pi^2) sin^2(pi mu) <u, ell(mu)>^2,   mu = Delta z,
    so the residue is NOT a frozen real constant a(gamma) -- the sin^2 factor must be
    continued with the pole. At mu = k + i y with k integer,
        sin^2(pi(k+iy)) = -sinh^2(pi y)   -- NEGATIVE.
    blinddet.py froze a(gamma) at its tiny real value and moved only the poles, so it never
    introduced the negative term at all. Check the identity and the two resonance cases.
"""
import mpmath as mp
from mpmath import mpf, mpc, nstr

mp.mp.dps = 40

print("="*92)
print("(A) INERTIA ROUTINE AUDIT on M = [[0,1],[1,0]], true inertia (1,1,0)")
print("="*92)

def buggy_1x1(Q):
    """The pattern shipped in signs.py / blinddet.py / mech.py / overdet.py."""
    n=len(Q); A=[r[:] for r in Q]; piv=[]
    for k in range(n):
        b=max(range(k,n),key=lambda t:abs(A[t][t]))
        if b!=k:
            A[k],A[b]=A[b],A[k]
            for r in range(n): A[r][k],A[r][b]=A[r][b],A[r][k]
        d=A[k][k]; piv.append(d)
        if d==0: continue                      # <-- the defect
        for i in range(k+1,n):
            f=A[i][k]/d
            for j in range(k,n): A[i][j]-=f*A[k][j]
            for j in range(k,n): A[j][i]=A[i][j]
    tol=max(abs(p) for p in piv)*mpf(10)**(-mp.mp.dps+12) if any(piv) else mpf(0)
    return (sum(1 for p in piv if p>tol),sum(1 for p in piv if p<-tol),
            sum(1 for p in piv if abs(p)<=tol))

M=[[mpf(0),mpf(1)],[mpf(1),mpf(0)]]
print(f"  buggy 1x1-only routine on [[0,1],[1,0]] : {buggy_1x1(M)}   (truth (1,1,0))")
M2=[[mpf(0),mpf(1),mpf(0)],[mpf(1),mpf(0),mpf(0)],[mpf(0),mpf(0),mpf(1)]]
print(f"  same routine on diag-augmented 3x3      : {buggy_1x1(M2)}   (truth (2,1,0))")
print("  => the reviewer is right: the routine cannot see a hyperbolic 2x2 block.\n")

print("  Which of my shipped scripts use it?")
import os,re
for fn in sorted(os.listdir('.')):
    if not fn.endswith('.py'): continue
    src=open(fn).read()
    if 'piv.append' in src or 'piv=[]' in src or 'piv = []' in src:
        has2x2 = ('hyperbolic' in src) or ('if k is None' in src)
        print(f"    {fn:22s}  2x2 pivots handled: {has2x2}")
print()

print("="*92)
print("(B) THE RESIDUE MUST BE CONTINUED.  sin^2(pi(k+iy)) = -sinh^2(pi y) ?")
print("="*92)
for k in (0,5,14):
    for y in ('0.1','0.5','1.0'):
        z=mpc(k, mpf(y))
        lhs=mp.sin(mp.pi*z)**2
        rhs=-mp.sinh(mp.pi*mpf(y))**2
        print(f"  k={k:>3} y={y:>4}: sin^2(pi(k+iy)) = {nstr(lhs,10):>26}   "
              f"-sinh^2(pi y) = {nstr(rhs,10):>16}   diff {nstr(abs(lhs-rhs),3)}")
print("  => confirmed: at an integer node-coordinate the sine factor becomes NEGATIVE REAL")
print("     as soon as the zero leaves the line, growing like -(pi y)^2.  My blinddet.py")
print("     froze a(gamma) at its real value and never introduced this term.\n")

print("="*92)
print("(C) REMOVABLE RESONANCE:  lim_{mu->k} (L/pi^2) sin^2(pi mu) ell(mu) ell(mu)^T = L e_k e_k^T ?")
print("="*92)
N=6; L=mpf(7)
nodes=[mpf(j) for j in range(-N,N+1)]
for k in (0,3,-5):
    for eps in ('1e-3','1e-6','1e-10'):
        mu=mpf(k)+mpf(eps)
        ell=[1/(nodes[j]-mu) for j in range(len(nodes))]
        pref=(L/mp.pi**2)*mp.sin(mp.pi*mu)**2
        idx=nodes.index(mpf(k))
        print(f"  k={k:>3} eps={eps:>6}: pref*ell_k^2 = {nstr(pref*ell[idx]**2,12):>18}  vs  L = {nstr(L,8)}"
              f"   ratio {nstr(pref*ell[idx]**2/L,10)}")
    print()
print("  => the k-th diagonal entry tends to L exactly; the 'zero weight' is REMOVABLE when")
print("     the resonance sits INSIDE the node band.  Only an integer OUTSIDE the band")
print("     gives a genuine on-line notch.")

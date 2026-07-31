"""(i) removable resonance inside the band, (ii) genuine notch outside the band,
(iii) the reviewer's universal Loewner-Hankel identity, (iv) does the 1x1-pivot bug
change any PUBLISHED result?  Re-run signs.py and overdet.py with a correct routine."""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, mpc, nstr
from fractions import Fraction as F
import blinddet2 as B

mp.mp.dps = 60

print("="*94)
print("(i) REMOVABLE RESONANCE.  gamma_1*Delta = k INSIDE the node band: is the packet L e_k e_k^T?")
print("="*94)
N=10
for c,k in [('9.23136',5),('14.3985',6),('22.458',7)]:
    L=mp.log(mpf(c)); Delta=L/(2*mp.pi)
    g=B.gammas(1)[0]; mu=Delta*g
    dim=2*N+1; nodes=[mpf(j) for j in range(-N,N+1)]
    ell=[1/(nodes[j]-mu) for j in range(dim)]
    pref=(L/mp.pi**2)*mp.sin(mp.pi*mu)**2
    row=[pref*ell[i]*ell[j] for i in range(dim) for j in [i]]
    kk=nodes.index(mpf(k))
    offmax=max(abs(pref*ell[i]*ell[j]) for i in range(dim) for j in range(dim) if not(i==kk and j==kk))
    print(f"  c={c:>9} k={k}: (packet)_{{kk}} = {nstr(pref*ell[kk]**2,12):>16}  L = {nstr(L,10):>12}"
          f"   ratio {nstr(pref*ell[kk]**2/L,10):>12}   max other entry {nstr(offmax,3)}")
print("  => the packet is L e_k e_k^T to working precision: NOT a vanishing contribution.\n")

print("="*94)
print("(ii) GENUINE NOTCH: integer OUTSIDE the band (|k| > N).  On-line vs off-line.")
print("="*94)
N=4                      # so that k=5..9 sits outside [-4,4]
for c,k in [('9.23136',5),('14.3985',6),('22.458',7)]:
    L=mp.log(mpf(c)); Delta=L/(2*mp.pi)
    dim=2*N+1
    onl=B.inertia(B.build(L,N,25,mpf(0),60))
    res=[]
    for d in ('1e-6','1e-3','1e-1'):
        res.append((d, B.inertia(B.build(L,N,25,mpf(d),60))))
    print(f"  c={c:>9} k={k} (N={N}, so k outside band): on-line inertia {onl}")
    for d,ine in res:
        print(f"      delta={d:>6}: inertia {ine}   {'NEGATIVE DIRECTION' if ine[1]>0 else 'still PSD'}")
print()

print("="*94)
print("(iii) UNIVERSAL LOEWNER-HANKEL.  Is H_{a+1,b} = H_{a,b+1} for an ARBITRARY source?")
print("="*94)
import random
def hankel_defect(psi,dpsi,N,dps):
    mp.mp.dps=dps
    d=2*N+1; nodes=[mpf(j) for j in range(-N,N+1)]
    w=[]
    for j in range(d):
        p=mpf(1)
        for kk in range(d):
            if kk!=j: p*=(nodes[kk]-nodes[j])
        w.append(1/p)
    Q=[[dpsi(nodes[i]) if i==j else (psi(nodes[i])-psi(nodes[j]))/(nodes[i]-nodes[j])
        for j in range(d)] for i in range(d)]
    Qt=[[w[i]*Q[i][j]*w[j] for j in range(d)] for i in range(d)]
    V=[[nodes[i]**a for a in range(d)] for i in range(d)]
    M=[[sum(V[i][a]*Qt[i][j]*V[j][b] for i in range(d) for j in range(d)) for b in range(d)] for a in range(d)]
    worst=mpf(0)
    for a in range(d-1):
        for b in range(d-1):
            sc=max(abs(M[a+1][b]),abs(M[a][b+1]))
            if sc>0: worst=max(worst,abs(M[a+1][b]-M[a][b+1])/sc)
    return worst
srcs={
 "psi(x)=x^3 (not Pick, not a pole sum)": (lambda x:x**3, lambda x:3*x**2),
 "psi(x)=x^5 - 2x":                       (lambda x:x**5-2*x, lambda x:5*x**4-2),
 "psi(x)=exp(x/9) (entire, non-odd)":     (lambda x:mp.e**(x/9), lambda x:mp.e**(x/9)/9),
 "psi(x)=sin(x) (oscillatory)":           (lambda x:mp.sin(x), lambda x:mp.cos(x)),
 "psi(x)=1/(x-30.5) (single real pole)":  (lambda x:1/(x-mpf('30.5')), lambda x:-1/(x-mpf('30.5'))**2),
 "psi(x)=log(x+40) (non-rational)":       (lambda x:mp.log(x+40), lambda x:1/(x+40)),
}
for name,(p,dp) in srcs.items():
    for N in (3,5):
        print(f"  N={N}  {name:42s}  worst |H_{{a+1,b}} - H_{{a,b+1}}| / scale = {nstr(hankel_defect(p,dp,N,80),4)}")
print("  => Hankel-ness is a UNIVERSAL identity for Loewner matrices, not arithmetic evidence.\n")

print("="*94)
print("(iv) DOES THE 1x1-PIVOT BUG CHANGE A PUBLISHED RESULT?  Re-run O-16005's sign scan.")
print("="*94)
mp.mp.dps=60
import signs as SG
print(f"{'signs':>14} {'buggy routine':>14} {'CORRECT routine':>16}  agree?")
for pat in [(1,-1,-1),(1,1,-1),(1,-1,1),(-1,-1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(-1,1,-1)]:
    A,L=SG.build('200',6,*pat,dps=60)
    dim=A.rows
    old=SG.ldl_inertia(A)
    new=B.inertia([[A[i,j] for j in range(dim)] for i in range(dim)])
    print(f"{str(pat):>14} {str(old):>14} {str(new):>16}  {old==new}")

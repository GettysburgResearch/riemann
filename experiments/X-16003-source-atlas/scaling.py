"""The relative errors r_i/gamma_i - 1 were nearly IDENTICAL across i at each cutoff.
That is a common scale factor kappa(c), not convergence.  What is kappa?

Guess: the CvS node variable n carries frequency 2 pi n / L, L = log c.  So a root at node
position s corresponds to frequency 2 pi s / L.  If the roots are the zeta zeros in that natural
coordinate, then 2 pi r_i / L = gamma_i."""
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots, zetazero, log, pi
import x0001
mp.dps = 60
GAM=[mp.im(zetazero(n)) for n in range(1,9)]

def nominate(cut,N,dps=60):
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    dim=A.rows; eta=matrix([1]*dim)
    x=lu_solve(A,eta); t=1/sum(x[i] for i in range(dim))
    xi=[x[i]*t for i in range(dim)]
    idx=list(range(-N,N+1)); Om=[mpf(1)]
    for k in idx:
        Om=[ (Om[i-1] if i>0 else mpf(0))*(-1) + (Om[i]*mpf(k) if i<len(Om) else mpf(0)) for i in range(len(Om)+1)]
    P=[mpf(0)]*dim
    for a,j in enumerate(idx):
        Omd=Om[::-1]; acc=mpf(0); Qd=[]
        for i in range(len(Omd)-1):
            acc=Omd[i]+acc*mpf(j); Qd.append(acc)
        for i,cc in enumerate([-c for c in Qd[::-1]]): P[i]+=xi[a]*cc
    rts=polyroots(P[::-1],maxsteps=400,extraprec=3000)
    return sorted([mp.re(r) for r in rts if mp.re(r)>0 and abs(mp.im(r))<mpf(10)**(-25)])

print("Roots converted to the natural CvS frequency coordinate  w_i = 2*pi*r_i/L,  L = log c.")
print(f"{'cutoff':>8} {'L=log c':>9} | " + " ".join(f"{'w_'+str(i+1):>11}" for i in range(4)))
print("-"*66)
rows=[]
for cut in ['50','100','200','500','1000','2000','5000']:
    L=log(mpf(cut)); pos=nominate(cut,6)
    w=[2*pi*p/L for p in pos[:4]]
    rows.append((cut,L,w))
    print(f"{cut:>8} {nstr(L,6):>9} | " + " ".join(f"{nstr(x,9):>11}" for x in w))
print(f"{'zeta':>8} {'':>9} | " + " ".join(f"{nstr(g,9):>11}" for g in GAM[:4]))
print()
print("Relative error of w_i against gamma_i:")
print(f"{'cutoff':>8} | " + " ".join(f"{'w_'+str(i+1)+'/g-1':>13}" for i in range(4)))
print("-"*72)
for cut,L,w in rows:
    print(f"{cut:>8} | " + " ".join(f"{nstr(w[i]/GAM[i]-1,4):>13}" for i in range(4)))
print()
print("Same, at larger N (better resolution of the higher zeros), cutoff 2000:")
L=log(mpf('2000'))
for N in [6,8,10]:
    pos=nominate('2000',N); w=[2*pi*p/L for p in pos[:5]]
    print(f"   N={N}: " + " ".join(f"{nstr(x,9):>11}" for x in w))
print("   zeta: " + " ".join(f"{nstr(g,9):>11}" for g in GAM[:5]))

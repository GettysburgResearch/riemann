"""The part that is NOT automatic.

Automatic (Sherman-Morrison + CvS Thm 5.6): if Q_W > 0 then at t* = 1/(eta^T Q^-1 eta) the matrix
Q - t* eta eta^T is PSD with a 1-dim kernel, and P is then real-rooted BY THE THEOREM. So the
real-rootedness is guaranteed, not discovered; the whole content sits in "is Q_W positive definite",
i.e. finite Weil positivity.

NOT automatic: WHERE the roots of P sit.  Do they track the zeta zeros as the prime cutoff grows?"""
import sys; sys.path.insert(0,'.')
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots, zetazero
import x0001

mp.dps = 60
GAM=[mp.im(zetazero(n)) for n in range(1,9)]
print("zeta zeros:", [nstr(g,8) for g in GAM[:6]])
print()
def nominate(cut,N,dps=60):
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    dim=A.rows; eta=matrix([1]*dim)
    x=lu_solve(A,eta); t=1/sum(x[i] for i in range(dim))
    xi=[x[i]*t for i in range(dim)]
    idx=list(range(-N,N+1))
    Om=[mpf(1)]
    for k in idx:
        Om=[ (Om[i-1] if i>0 else mpf(0))*(-1) + (Om[i]*mpf(k) if i<len(Om) else mpf(0)) for i in range(len(Om)+1)]
    P=[mpf(0)]*dim
    for a,j in enumerate(idx):
        Omd=Om[::-1]; acc=mpf(0); Qd=[]
        for i in range(len(Omd)-1):
            acc=Omd[i]+acc*mpf(j); Qd.append(acc)
        Qj=[-c for c in Qd[::-1]]
        for i in range(len(Qj)): P[i]+=xi[a]*Qj[i]
    rts=polyroots(P[::-1],maxsteps=400,extraprec=3000)
    pos=sorted([mp.re(r) for r in rts if mp.re(r)>0 and abs(mp.im(r))<mpf(10)**(-25)])
    return t,pos

print("Positive roots of P for the ARITHMETIC-nominated target, versus the zeta zeros.")
print(f"{'cutoff c':>9} {'N':>3} {'t*':>12}   first positive roots")
print("-"*104)
for cut,N in [('50',6),('100',6),('200',6),('500',6),('1000',6),('2000',6),('5000',6)]:
    try:
        t,pos = nominate(cut,N)
        print(f"{cut:>9} {N:>3} {nstr(t,6):>12}   {[nstr(p,7) for p in pos[:6]]}")
    except Exception as e:
        print(f"{cut:>9} {N:>3}   failed: {e}")
print(f"{'zeta':>9} {'':>3} {'':>12}   {[nstr(g,7) for g in GAM[:6]]}")
print()
print("Relative error of the first three roots against gamma_1, gamma_2, gamma_3:")
print(f"{'cutoff':>9}  {'r1/g1-1':>12} {'r2/g2-1':>12} {'r3/g3-1':>12}")
for cut in ['100','200','500','1000','2000','5000']:
    try:
        t,pos=nominate(cut,6)
        e=[nstr(pos[i]/GAM[i]-1,4) for i in range(3)]
        print(f"{cut:>9}  {e[0]:>12} {e[1]:>12} {e[2]:>12}")
    except Exception as ex:
        print(f"{cut:>9}  failed")

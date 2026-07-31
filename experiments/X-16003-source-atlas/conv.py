"""The end-to-end test converges upward but slowly.  Diagnose and push.

Why slow: t* = min over MONIC degree-2N P of int P^2 dnu.  At large mu the minimiser grows like
mu^{2N}, so P(mu)^2 ~ mu^{4N}, while the weight a(gamma)/Omega(mu)^2 ~ mu^{-(4N+2)} (a is bounded).
The tail terms therefore decay only like mu^{-2}, and with gamma_k ~ 2 pi k / log k the tail of the
sum is ~ (log M)^2 / M -- so hundreds or thousands of zeros are needed, NOT tens.

If that diagnosis is right the ratio should climb steadily toward 1 like 1 - C (log M)^2 / M.
Test it.  (Also worth noting on its own: t* is NOT dominated by the resolved low zeros, even
though the measure's MASS is.  The sharpness of finite Weil positivity at level N depends on the
whole zero set.)
"""
import sys,time; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf,nstr,matrix,lu_solve
import x0001

t0=time.time()
mp.mp.dps=40
NZ=400
Z=[mp.im(mp.zetazero(k)) for k in range(1,NZ+1)]
print(f"got {NZ} zeros in {time.time()-t0:.0f}s; gamma_{NZ} = {mp.nstr(Z[-1],10)}")

def tstar_model(L,N,M,dps):
    mp.mp.dps=dps
    Delta=L/(2*mp.pi); d=2*N+1
    nodes=[mpf(k) for k in range(-N,N+1)]
    def Om(s):
        p=mpf(1)
        for k in nodes: p*=(k-s)
        return p
    H=matrix(d,d)
    for g in Z[:M]:
        a=(L/mp.pi**2)*mp.sin(g*L/2)**2
        mu=g*Delta
        w1=a/Om(mu)**2; w2=a/Om(-mu)**2
        for i in range(d):
            for j in range(d):
                H[i,j]+= w1*mu**(i+j) + w2*(-mu)**(i+j)
    e=matrix(d,1); e[d-1]=1
    return 1/lu_solve(H,e)[d-1]

for cut,N,dps in [('200',4,150),('2000',4,150)]:
    L=mp.log(mpf(cut))
    mp.mp.dps=dps
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    d=A.rows
    tw=1/sum(lu_solve(A,matrix([1]*d))[i] for i in range(d))
    print(f"\n=== cutoff {cut}, N={N}: t* from Q_W = {mp.nstr(tw,14)} ===")
    print(f"{'M zeros':>9} {'t* from measure':>22} {'ratio':>12} {'deficit':>10} {'(log M)^2/M':>13}")
    for M in (10,30,60,100,150,220,300,400):
        tm=tstar_model(L,N,M,dps)
        mp.mp.dps=30
        r=tm/tw
        print(f"{M:>9} {nstr(tm,14):>22} {nstr(r,8):>12} {nstr(1-r,6):>10} "
              f"{float(mp.log(M)**2/M):>13.4f}")
        sys.stdout.flush()

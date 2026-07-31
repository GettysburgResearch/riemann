"""END-TO-END TEST of the closed-form measure.

O-16007 claims the finite Weil form's representing measure is

    nu = sum_gamma a(gamma) * [ delta_{gamma Delta} + delta_{-gamma Delta} ] / Omega(gamma Delta)^2,
    a(gamma) = (log c / pi^2) sin^2(gamma log c / 2),   Delta = log c / 2 pi.

If that is right then t* -- which by L-16006(b) is the monic degree-2N orthogonal-polynomial
norm of the SAME inner product -- must be reproducible from nu ALONE, with no Weil matrix
anywhere in the computation.  In the monomial basis, with H_{ab} = int s^{a+b} dnu the moment
matrix, min over monic degree-2N P of P^T H P is  1 / (H^{-1})_{2N,2N}.

So: compute t*_model from nu, compare against t* computed from X-0001's Q_W.  The two share no
code path.  Agreement would validate the residue law, the moment reading, and the identification
of the support all at once.  Disagreement localises which of them is wrong.
"""
import sys; sys.path.insert(0,'.')
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve
import x0001

def zeros(n):
    return [mp.im(mp.zetazero(k)) for k in range(1,n+1)]

def tstar_model(L,N,M,dps):
    mp.mp.dps=dps
    Delta=L/(2*mp.pi); d=2*N+1
    nodes=[mpf(k) for k in range(-N,N+1)]
    def Om(s):
        p=mpf(1)
        for k in nodes: p*=(k-s)
        return p
    H=matrix(d,d)
    for g in zeros(M):
        a=(L/mp.pi**2)*mp.sin(g*L/2)**2
        mu=g*Delta
        wt=a/Om(mu)**2
        wt2=a/Om(-mu)**2
        for i in range(d):
            for j in range(d):
                H[i,j]+= wt*mu**(i+j) + wt2*(-mu)**(i+j)
    e=matrix(d,1); e[d-1]=1
    y=lu_solve(H,e)
    return 1/y[d-1]

def tstar_weil(cut,N,dps):
    mp.mp.dps=dps
    A,_=x0001.build_cutoff_free_matrix(cut,N,dps=dps)
    d=A.rows
    x=lu_solve(A,matrix([1]*d))
    return 1/sum(x[i] for i in range(d))

print(f"{'cut':>7} {'N':>3} {'M zeros':>8} {'t* from Q_W':>20} {'t* from the measure':>22} {'ratio':>14}")
print("-"*82)
for cut,N,dps in [('200',4,150),('2000',4,150),('2000',6,190),('20000',6,190),('2000',8,240)]:
    L=mp.log(mpf(cut))
    tw=tstar_weil(cut,N,dps)
    for M in (10,30,60):
        tm=tstar_model(L,N,M,dps)
        mp.mp.dps=30
        print(f"{cut:>7} {N:>3} {M:>8} {nstr(tw,14):>20} {nstr(tm,14):>22} {nstr(tm/tw,10):>14}")
    print()
    sys.stdout.flush()

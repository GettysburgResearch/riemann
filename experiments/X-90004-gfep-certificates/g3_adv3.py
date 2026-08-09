"""G3: (i) c>=0 census over ALL exits; (ii) coeffs-vs-flow cross-check at true mu;
(iii) critical A*(X,n) by bisection: largest A with adversarial min_p Sigma >= 0 under
     |m(N)|<=A/sqrt(N) (N in (K0,Kmax]), K0=40; depth scan; (iv) five-parent identity."""
import numpy as np
from mpmath import mp, mpf, log as mlog, sqrt as msqrt
from scipy.optimize import linprog
mp.dps = 30
from g3_adv import mobius_sieve, children, Gtab, coeffs, flow_sigma_exact
K0=40

def census(X,n):
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=mlog(mpf(X)/q)/msqrt(mpf(q))
    Kmax=X//n; W=list(range(n,min(2*n,X+1)))
    sf=[k for k in range(1,Kmax+1) if mu[k]!=0]
    C={p:coeffs(X,n,p,w) for p in W}
    negc=0; totc=0; worstneg=0.0
    for p in W:
        for k in sf:
            v=C[p][k]; totc+=1
            if v<0: negc+=1; worstneg=min(worstneg,v)
    # cross-check vs flow at true mu
    Sig=flow_sigma_exact(X,n,mu)
    err=max(abs(float(Sig[p])-sum(mu[k]*C[p][k] for k in sf)) for p in W)
    print(f"X={X} n={n}: c_pk<0 count {negc}/{totc} (worst {worstneg:.2e}); max|coeffs-flow|={err:.2e}")
    return mu,w,Kmax,W,C,sf

def Astar(X,n,mu,Kmax,W,C,sf):
    deep=[k for k in sf if k>K0]
    if not deep: return None
    m_known=sum(mu[k]/k for k in sf if k<=K0)
    nd=len(deep)
    Arow=[]
    for N in range(K0+1,Kmax+1):
        a=np.zeros(nd)
        for j,k in enumerate(deep):
            if k<=N: a[j]=1.0/k
        Arow.append((N,a))
    A_ub=np.vstack([a for _,a in Arow]+[-a for _,a in Arow])
    def minSig(A):
        b=np.concatenate([np.array([A/np.sqrt(N)-m_known for N,_ in Arow]),
                          np.array([A/np.sqrt(N)+m_known for N,_ in Arow])])
        worst=1e9
        for q in W:
            cq=C[q]; knq=sum(mu[k]*cq[k] for k in sf if k<=K0)
            dv=np.array([cq[k] for k in deep])
            res=linprog(dv,A_ub=A_ub,b_ub=b,bounds=[(-1,1)]*nd,method='highs')
            val=knq+res.fun if res.status==0 else 1e9
            worst=min(worst,val)
        return worst
    lo,hi=0.0,8.0
    if minSig(hi)>=0: return hi
    for _ in range(22):
        mid=(lo+hi)/2
        if minSig(mid)>=0: lo=mid
        else: hi=mid
    return lo

def five_parent(X,n):
    """Sigma(n) = nR(n) + sum_{m in {2n,2n+1,3n-2,3n-1,3n}, m<=X} g(m) n/(2m)*mult."""
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=mlog(mpf(X)/q)/msqrt(mpf(q))
    U=[mpf(0)]*(X+2)
    for m in range(1,X+1):
        U[m]=sum(mu[k]*w[m*k] for k in range(1,X//m+1) if mu[k])
    S=[mpf(0)]*(X+2)
    for m in range(n,X+1): S[m]=m*(U[m]-U[m+1])
    g=[mpf(0)]*(X+2); infl=[mpf(0)]*(X+2)
    for m in range(X,2*n-1,-1):
        g[m]=S[m]+infl[m]
        for c in children(m):
            if c>=n: infl[c]+=g[m]*mpf(c)/(2*m)
    direct=S[n]+infl[n]
    fp=S[n]
    for m in set([2*n,2*n+1,3*n-2,3*n-1,3*n]):
        if m<=X and m>=2*n:
            mult=sum(1 for c in children(m) if c==n)
            fp+=g[m]*mpf(n)/(2*m)*mult
    print(f"   five-parent identity X={X} n={n}: |direct-5parent| = {float(abs(direct-fp)):.2e}  (Sigma(n)={float(direct):+.5f})")

if __name__=="__main__":
    for (X,n) in [(2000,20),(3000,25),(3000,15),(4000,20),(4000,15)]:
        mu,w,Kmax,W,C,sf=census(X,n)
        a=Astar(X,n,mu,Kmax,W,C,sf)
        print(f"   A*(X={X},n={n}, Kmax={Kmax}) = {a:.4f}" if a is not None else "   no deep vars")
    five_parent(2000,20); five_parent(3000,25); five_parent(1960,196)

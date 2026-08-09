"""G3 sharpening: (i) known/deep split + sign census of c_{p,k}; (ii) K0-scan;
(iii) sparse adversary (min #flips to kill); (iv) RH-strength tail-magnitude LP:
     constraints |m(N)| <= A/sqrt(N) for all N in [K0,Kmax], m(N)=m_true(K0)+sum_{deep k<=N} eps_k/k,
     eps in [-1,1]; scan A to find flip threshold A*.
"""
import numpy as np
from fractions import Fraction
from mpmath import mp, mpf, log as mlog, sqrt as msqrt
from scipy.optimize import linprog
mp.dps = 30
from g3_adv import mobius_sieve, children, Gtab, coeffs, flow_sigma_exact

def build(X,n):
    mu=mobius_sieve(X)
    w=[mpf(0)]*(X+2)
    for q in range(1,X+1): w[q]=mlog(mpf(X)/q)/msqrt(mpf(q))
    Kmax=X//n
    W=list(range(n,min(2*n,X+1)))
    C={p:coeffs(X,n,p,w) for p in W}
    return mu,Kmax,W,C

def analyze(X,n,K0list=(40,60,80),Ascan=(0.5,1.0,1.5,2.0,3.0)):
    mu,Kmax,W,C=build(X,n)
    sf=[k for k in range(1,Kmax+1) if mu[k]!=0]
    print(f"== X={X} n={n} Kmax={Kmax}")
    p=W[0]  # bottom exit (weakest per g3_adv)
    c=C[p]
    for K0 in K0list:
        if K0>=Kmax: continue
        deep=[k for k in sf if k>K0]
        known=sum(mu[k]*c[k] for k in sf if k<=K0)
        true=sum(mu[k]*c[k] for k in sf)
        dvec=np.array([c[k] for k in deep])
        deep_true=true-known
        npos=(dvec>0).sum(); nneg=(dvec<0).sum()
        print(f"  K0={K0}: p={p} true={true:+.4f} known={known:+.4f} deep_true={deep_true:+.4f} "
          f"sum|c_deep|={np.abs(dvec).sum():.4f} FREEmin={known-np.abs(dvec).sum():+.4f} "
          f"c-signs +{npos}/-{nneg} max|c|={np.abs(dvec).max():.4f}")
    # sparse adversary at K0=40
    K0=40
    deep=[k for k in sf if k>K0]
    known=sum(mu[k]*c[k] for k in sf if k<=K0)
    true=sum(mu[k]*c[k] for k in sf)
    contrib=sorted([(abs(c[k])+ (mu[k]*c[k] if k in deep else 0),k) for k in deep], reverse=True)
    # flipping k changes Sigma by -2*mu(k)c(k) if mu(k)=sign... general: set eps_k=-sign(c_k): delta = (-sign(c_k)-mu(k))*c_k
    deltas=sorted([(((-np.sign(c[k]))-mu[k])*c[k],k) for k in deep])
    acc=true; used=[]
    for d,k in deltas:
        if acc<0: break
        if d<0: acc+=d; used.append(k)
    print(f"  sparse adversary: flips needed to kill exit {p}: {len(used)} (kills to {acc:+.4f}); flipped k={used}")
    # RH-strength tail LP at K0=40, per exit, scan A
    m_known=sum(mu[k]/k for k in sf if k<=K0)
    nd=len(deep)
    rows=[]; rhs=[]
    for N in range(K0+1,Kmax+1):
        a=np.zeros(nd)
        for j,k in enumerate(deep):
            if k<=N: a[j]=1.0/k
        bnd=1.0/np.sqrt(N)
        rows.append(( a, bnd - m_known))   #  m_known + a.eps <= A*bnd
        rows.append((-a, bnd + m_known))   # -(...) <= A*bnd
    print(f"  RH-tail LP (|m(N)|<=A/sqrt(N), N in ({K0},{Kmax}]):")
    for A in Ascan:
        A_ub=np.vstack([r[0] for r in rows]); b_ub=np.array([ (A*(1.0/np.sqrt(K0+1+i//2 if False else 1)))for i in range(len(rows))])
        # rebuild rhs properly
        b=[]
        for N in range(K0+1,Kmax+1):
            bnd=A/np.sqrt(N)
            b.append(bnd-m_known); b.append(bnd+m_known)
        b_ub=np.array(b)
        worst=None; wp=None
        for q in W:
            cq=C[q]
            knq=sum(mu[k]*cq[k] for k in sf if k<=K0)
            dv=np.array([cq[k] for k in deep])
            res=linprog(dv,A_ub=A_ub,b_ub=b_ub,bounds=[(-1,1)]*nd,method='highs')
            if res.status!=0:
                val=float('inf')  # infeasible constraint set (A too small for m_known)
            else:
                val=knq+res.fun
            if worst is None or val<worst: worst=val; wp=q
        tag="INFEASIBLE(all)" if worst==float('inf') else f"{worst:+.5f} at p={wp}"
        print(f"    A={A}: adversarial min_p Sigma = {tag}")

if __name__=="__main__":
    analyze(3000,25)
    analyze(2000,20,K0list=(40,60),Ascan=(0.5,1.0,2.0,3.0))

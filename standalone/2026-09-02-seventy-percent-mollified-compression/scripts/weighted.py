# RH-numerics of the multiplicative-weight certificate  s1 >= 2 tr W - ||W||^2,
# W = sum_rho w_rho v v^T,  w_rho = |1 + eps F(rho)|^2,  ||W||^2 = sum w w' sinc^2(L(g-g')/2).
import numpy as np, sys
rows=[l.split() for l in open('../outputs/zetaprime_first18816.txt') if not l.startswith('#')]
n=np.array([int(r[0]) for r in rows]); g=np.array([float(r[1]) for r in rows])
zp=np.array([float(r[2])+1j*float(r[3]) for r in rows])
n0=int(sys.argv[1]) if len(sys.argv)>1 else 6000
sel=n>=n0; g=g[sel]; zp=zp[sel]; M=len(g); T=g[M//2]
BAND=400
inner=np.zeros(M,dtype=bool); inner[BAND:M-BAND]=True; Mi=int(inner.sum())
# precompute banded sinc^2 with local L
offs=[]; 
for k in range(1,BAND+1):
    a=np.arange(0,M-k); b=a+k
    Lloc=np.log((g[a]+g[b])/2/(2*np.pi)); x=Lloc*(g[b]-g[a])/2
    offs.append((np.sin(x)/x)**2)
def quad(w):  # sum_{rho,rho'} w w' S^2 counting pairs with an inner endpoint (each inner rho once)
    tot=np.sum(w[inner]**2)
    for k,s2 in enumerate(offs,1):
        a=np.arange(0,M-k); b=a+k
        wt=inner[a].astype(float)+inner[b].astype(float)
        tot+=np.sum(wt*w[a]*w[b]*s2)
    return tot
def cert(w): return (2*np.sum(w[inner])-quad(w))/Mi
def mobius(N):
    mu=np.ones(N+1,dtype=int); isp=np.ones(N+1,dtype=bool)
    for p in range(2,N+1):
        if isp[p]: isp[2*p::p]=False; mu[p::p]*=-1; mu[p*p::p*p]=0
    return mu
def moll(theta):
    y=T**theta; K=int(y); mu=mobius(max(K,2)); B=np.zeros(M,dtype=complex)
    for k in range(1,K+1):
        if mu[k]==0: continue
        x=np.log(y/k)/np.log(y); B+=mu[k]*(-theta*x*x+(1+theta)*x)*k**(-0.5-1j*g)
    return B,K
print(f"M={M} inner={Mi} T={T:.0f}  unweighted cert (AF) = {cert(np.ones(M)):.4f}")
# unconstrained optimum 1^T (S^2)^{-1} 1 by conjugate gradient on the banded operator
def Sq(v):
    out=v.copy()
    for k,s2 in enumerate(offs,1):
        out[:-k]+=s2*v[k:]; out[k:]+=s2*v[:-k]
    return out
b=np.ones(M); x=np.zeros(M); r=b-Sq(x); p=r.copy(); rs=r@r
for it in range(300):
    Ap=Sq(p); al=rs/(p@Ap); x+=al*p; r-=al*Ap; rs2=r@r
    if np.sqrt(rs2)<1e-9: break
    p=r+(rs2/rs)*p; rs=rs2
print(f"unconstrained optimum 1^T(S^2)^-1 1 / M = {np.sum(x[inner])/Mi:.4f}  (min weight {x.min():.3f}, max {x.max():.3f}, mean {x.mean():.3f})  CG iters {it}")
for name,F in [("F=1",np.ones(M,dtype=complex)),("F=zeta'",zp),("F=B zeta' th=0.45",moll(0.45)[0]*zp),("F=B zeta' th=0.35",moll(0.35)[0]*zp),("F=B zeta' th=0.2",moll(0.2)[0]*zp)]:
    m=np.mean(F[inner]); best=(-1,None)
    out=[]
    for em in np.linspace(-0.6,0.3,91):
        eps=em/m if abs(m)>0 else em
        w=np.abs(1+eps*F)**2; c=cert(w); out.append((em,c))
        if c>best[0]: best=(c,em)
    print(f"{name:22s} mean F={m:.3f} |S1|^2/(S2 M)={abs(np.sum(F[inner]))**2/(np.sum(np.abs(F[inner])**2)*Mi):.4f}  best cert={best[0]:.4f} at eps*mean(F)={best[1]:+.3f};  cert at em=-0.134: {[c for em,c in out if abs(em+0.134)<0.006][0]:.4f}")

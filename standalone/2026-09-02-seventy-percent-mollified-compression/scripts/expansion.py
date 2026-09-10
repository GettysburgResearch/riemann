# Decomposition of the weighted certificate into the functionals Lambda_1, Lambda_2, Lambda_2', and the
# small-eps gain formula 4X^2/Y versus the exact optimum.  F = B zeta' (BHB theta=0.45).
import numpy as np, sys
rows=[l.split() for l in open('../outputs/zetaprime_first18816.txt') if not l.startswith('#')]
n=np.array([int(r[0]) for r in rows]); g=np.array([float(r[1]) for r in rows])
zp=np.array([float(r[2])+1j*float(r[3]) for r in rows])
n0=int(sys.argv[1]) if len(sys.argv)>1 else 6000
sel=n>=n0; g=g[sel]; zp=zp[sel]; M=len(g); T=g[M//2]
BAND=400; inner=np.zeros(M,dtype=bool); inner[BAND:M-BAND]=True; Mi=int(inner.sum())
offs=[]
for k in range(1,BAND+1):
    a=np.arange(0,M-k); b=a+k; Lloc=np.log((g[a]+g[b])/2/(2*np.pi)); x=Lloc*(g[b]-g[a])/2; offs.append((np.sin(x)/x)**2)
def bil(u,v):  # sum_{rho,rho'} u_rho v_rho' S^2 (inner-endpoint counting), real inputs
    tot=np.sum(u[inner]*v[inner])
    for k,s2 in enumerate(offs,1):
        a=np.arange(0,M-k); b=a+k; wt=inner[a].astype(float)+inner[b].astype(float)
        tot+=np.sum(wt*(u[a]*v[b]+u[b]*v[a])*s2)/2*1.0  # symmetric
    return tot
def mobius(N):
    mu=np.ones(N+1,dtype=int); isp=np.ones(N+1,dtype=bool)
    for p in range(2,N+1):
        if isp[p]: isp[2*p::p]=False; mu[p::p]*=-1; mu[p*p::p*p]=0
    return mu
theta=0.45; y=T**theta; K=int(y); mu=mobius(K); B=np.zeros(M,dtype=complex)
for k in range(1,K+1):
    if mu[k]==0: continue
    x=np.log(y/k)/np.log(y); B+=mu[k]*(-theta*x*x+(1+theta)*x)*k**(-0.5-1j*g)
F=B*zp; one=np.ones(M); R=np.real(F); A2=np.abs(F)**2
HS0=bil(one,one); L1=bil(R,one); L2=bil(A2,one); L2p=bil(R,R); L3=bil(A2,R); L4=bil(A2,A2)
S1=np.sum(F[inner]); S2=np.sum(A2[inner])
print(f"M={Mi} T={T:.0f}  HS0/M={HS0/Mi:.4f}  ReS1/M={S1.real/Mi:.4f}  S2/M={S2/Mi:.4f}")
print(f"Lambda1/M={L1/Mi:.4f} (ReS1/M*HS0/M would be {S1.real/Mi*HS0/Mi:.4f}: the weight-density correlation is {L1/Mi-S1.real/Mi*HS0/Mi:+.4f})")
print(f"Lambda2/M={L2/Mi:.4f} (S2/M*HS0/M={S2/Mi*HS0/Mi:.4f})   Lambda2'/M={L2p/Mi:.4f}   Lambda3/M={L3/Mi:.4f}  Lambda4/M={L4/Mi:.4f}")
# exact certificate as polynomial in real eps: 2 tr W - HS with w = 1 + 2 eps R + eps^2 A2
def cert(eps):
    trW=Mi+2*eps*S1.real+eps*eps*S2
    hs=HS0+4*eps*L1+eps**2*(2*L2+4*L2p)+4*eps**3*L3+eps**4*L4
    return (2*trW-hs)/Mi
X=L1-S1.real; Y=(2*L2+4*L2p)-2*S2   # gain(eps) = -4 eps X - eps^2 Y + O(eps^3) relative to eps=0 value
print(f"X/M={X/Mi:.4f}  Y/M={Y/Mi:.4f}  small-eps optimum eps*=-2X/Y={-2*X/Y:.5f} (eps*mean F={-2*X/Y*S1.real/Mi:+.4f})  predicted gain 4X^2/(Y M)={4*X*X/(Y*Mi):.4f}")
es=np.linspace(-0.05,0.02,141); vals=[cert(e) for e in es]; i=int(np.argmax(vals))
print(f"exact: cert(0)={cert(0):.4f}  max cert={vals[i]:.4f} at eps={es[i]:.5f} (eps*meanF={es[i]*S1.real/Mi:+.3f});  cubic+quartic share at optimum: {(4*es[i]**3*L3+es[i]**4*L4)/Mi:+.5f}")

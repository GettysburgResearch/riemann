# Numerical test of the mollified-compression gain A = S2 - S2pc for weights F on zeta zeros.
# S2pc = sum_{n,n'} F_n conj(F_n') sinc^2(L (g_n-g_n')/2),  B = sum |F_n|^2 |F_n'|^2 sinc^2.
# Certificate (RH numerics): s1/M >= (2 - HS/M) + A^2/(B M) if A>0.
import numpy as np, sys
rows=[l.split() for l in open('../outputs/zetaprime_first18816.txt') if not l.startswith('#')]
n=np.array([int(r[0]) for r in rows]); g=np.array([float(r[1]) for r in rows])
zp=np.array([float(r[2])+1j*float(r[3]) for r in rows])
n0=int(sys.argv[1]) if len(sys.argv)>1 else 6000
sel=n>=n0; g=g[sel]; zp=zp[sel]; M=len(g); T=g[M//2]; L0=np.log(T/(2*np.pi))
print(f"M={M} heights {g[0]:.1f}..{g[-1]:.1f} center T={T:.1f} L0={L0:.3f}")
def mobius(N):
    mu=np.ones(N+1,dtype=int); isp=np.ones(N+1,dtype=bool)
    for p in range(2,N+1):
        if isp[p]:
            isp[2*p::p]=False; mu[p::p]*=-1; mu[p*p::p*p]=0
    return mu
def moll(theta,P):
    y=T**theta; K=int(y); mu=mobius(max(K,2)); B=np.zeros(M,dtype=complex)
    for k in range(1,K+1):
        if mu[k]==0: continue
        x=np.log(y/k)/np.log(y); B+=mu[k]*P(x,theta)*k**(-0.5-1j*g)
    return B,K
Pbhb=lambda x,th: -th*x*x+(1+th)*x
Plev=lambda x,th: x
BAND=400
def pairsums(F):
    # returns S2, S2pc, B, HS(=sum sinc^2 over all pairs incl diag), using local L per pair; inner window excludes edges
    inner=np.zeros(M,dtype=bool); inner[BAND:M-BAND]=True
    S2=np.sum(np.abs(F[inner])**2); S2pc=S2.copy(); Bq=np.sum(np.abs(F[inner])**4); HS=float(inner.sum())
    S1=np.sum(F[inner])
    for k in range(1,BAND+1):
        a=np.arange(0,M-k); b=a+k          # pair (a,b), b=a+k
        Lloc=np.log((g[a]+g[b])/2/(2*np.pi)); x=Lloc*(g[b]-g[a])/2
        s2=(np.sin(x)/x)**2
        w=(inner[a].astype(float)+inner[b].astype(float))  # count pair once for each inner endpoint
        S2pc+=np.sum(w*np.real(F[a]*np.conj(F[b]))*s2)
        Bq+=np.sum(w*np.abs(F[a])**2*np.abs(F[b])**2*s2)
        HS+=np.sum(w*s2)
    Mi=inner.sum()
    return S1,S2,S2pc,Bq,HS,Mi
def report(name,F):
    S1,S2,S2pc,Bq,HS,Mi=pairsums(F)
    A=S2-S2pc; gain=A*A/(Bq*Mi) if A>0 else 0.0
    print(f"{name:28s} HS/M={HS/Mi:.4f} CGG=|S1|^2/(S2 M)={abs(S1)**2/(S2*Mi):.4f}  S2pc/S2={S2pc/S2:.4f}  A/S2={A/S2:+.4f}  gain=A^2/(B M)={gain:.5f}  cert={2-HS/Mi+gain:.4f}")
report("F=1",np.ones(M,dtype=complex))
report("F=zeta'(rho)",zp)
# Z'-type: real alternating: zeta'(rho) = -i e^{-i theta} Z'  => Z' = i e^{i theta} zeta'
from mpmath import siegeltheta, mpf
th=np.array([float(siegeltheta(mpf(x))) for x in g])
Zp=np.real(1j*np.exp(1j*th)*zp)
report("F=Z'(gamma) real alt.",Zp.astype(complex))
report("F=|zeta'(rho)|",np.abs(zp).astype(complex))
for theta in (0.2,0.35,0.45):
    B,K=moll(theta,Pbhb); report(f"F=B zeta' BHB th={theta} y={K}",B*zp)
    B,K=moll(theta,Plev); report(f"F=B zeta' Lev th={theta} y={K}",B*zp)
    B,K=moll(theta,Pbhb); report(f"F=B(rho) only th={theta}",B)

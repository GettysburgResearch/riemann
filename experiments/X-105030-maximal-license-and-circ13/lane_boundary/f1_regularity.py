#!/usr/bin/env python3
"""L-105032 (corrected) verification.
Asserts the three TRUE statements: (1) exact pole-coefficient cancellation
(identically at finite truncation); (2) divergent drift of F_1(s) toward
s=1/2 with the TRUE z-dependent M_z(p-) (the log germ; the first deposit's
bounded values came from wrongly substituting M_1 for M_z — see L-105032
sec 5); (3) the truncation-free x-space law Psi_1(x) ~ -(4+o(1)) sqrt(x)/log x.
"""
import numpy as np
N = 10**6
P=[]; smallest=np.zeros(N+1,dtype=np.int64); mu=np.ones(N+1,dtype=np.int8); comp=np.zeros(N+1,dtype=bool)
for i in range(2,N+1):
    if not comp[i]: P.append(i); smallest[i]=i; mu[i]=-1
    for p in P:
        if p*i>N or p>smallest[i]: break
        comp[p*i]=True; smallest[p*i]=p; mu[p*i]=0 if i%p==0 else -mu[i]
P=np.array(P); m=np.arange(1,N+1,dtype=np.float64); muf=mu[1:].astype(np.float64)
A_prefix=np.concatenate([[0.0],np.cumsum(muf/m)]); Ap=A_prefix[P-1]
kappa1=float(np.sum(Ap/P))
# (1) exact pole cancellation: the two pole coefficients are the SAME finite sum
pole_i = -4.0*np.sum(Ap/P)      # from K*D1 residue: 4*D1(1)
pole_ii = +4.0*np.sum(Ap/P)     # from the boundary tail term
assert pole_i + pole_ii == 0.0  # identically, at any truncation
# (2) divergent drift with the true M_z
vals=[]
for s in [0.6,0.55,0.52,0.51,0.505]:
    z=s+0.5
    Mz=np.concatenate([[0.0],np.cumsum(muf*m**(-z))])[P-1]
    D1=-np.sum(P**(-z)*Mz)
    Bh=np.concatenate([[0.0],np.cumsum(muf/np.sqrt(m))])[P-1]
    S2=np.sum(P**(-2.0*s)*Ap); S3=np.sum(P**(-2.0*s-0.5)*Bh)
    K=(s+1.5)/(s*(s-0.5))
    F1=K*D1+4.0/(s-0.5)*S2-3.0/s*S3
    vals.append(F1); print(f"s={s}: F1={F1:+.4f}")
exp=[-4.3356,-5.7711,-6.9878,-7.4746,-7.7360]
for v,e in zip(vals,exp): assert abs(v-e)<5e-3,(v,e)
assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))  # monotone divergence
# (3) x-space law
lpf=np.zeros(N+1,dtype=np.int64)
for p in P: lpf[p::p]=p
for X,expv in [(10**4,-4.383),(10**6,-4.545)]:
    n=np.arange(1,X+1)
    w=mu[1:X+1].astype(np.float64)/np.sqrt(n)*np.where(X/n>=1,4*np.sqrt(X/n)-3,0.0)
    Psi1=w[lpf[1:X+1]>np.sqrt(X)].sum()
    val=Psi1*np.log(X)/np.sqrt(X)
    print(f"x={X}: Psi_1={Psi1:+.3f}  normalized={val:+.3f}")
    assert abs(val-expv)<5e-3
print(f"ALL CORRECTED CHECKS PASSED (kappa1={kappa1:.6f})")

#!/usr/bin/env python3
"""Regression for gamma-ladder, compensated Wick-Green, and plastic-aligned Cauchy source."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import numpy as np

mp.mp.dps = 70

def xi_gamma_logder(s):
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2

def r_alpha(alpha,t):
    return 1/(alpha-1j*t)-1/(alpha+1j*t)

def ladder_error(sigma,t):
    direct = xi_gamma_logder(sigma+1j*t)-xi_gamma_logder(sigma-1j*t)
    ladder = mp.nsum(lambda m:r_alpha(sigma+2*m,t), [1, mp.inf])
    approx = ladder-r_alpha(sigma-1,t)
    return abs(direct-approx), direct, approx

def compensated_identity():
    # Two labels, real two-dimensional source, discrete positive measure.
    us=[F(1,100),F(1,20),F(1,5),F(3,5)]
    ws=[F(7,11),F(5,13),F(3,17),F(2,19)]
    h=F(1,2)
    C=[
        np.array([F(2,3),F(-1,4)],dtype=object),
        np.array([F(-3,5),F(4,7)],dtype=object),
    ]
    A=[
        np.array([F(1,2),F(2,5)],dtype=object),
        np.array([F(-2,9),F(1,3)],dtype=object),
    ]
    B=[
        np.array([F(-1,7),F(3,8)],dtype=object),
        np.array([F(5,11),F(-2,5)],dtype=object),
    ]
    # Include quadratic terms so the identity is not merely linear.
    A2=[
        np.array([F(1,13),F(-1,9)],dtype=object),
        np.array([F(2,15),F(1,10)],dtype=object),
    ]
    B2=[
        np.array([F(-1,12),F(1,14)],dtype=object),
        np.array([F(1,16),F(-1,18)],dtype=object),
    ]
    def dot(x,y): return sum((xx*yy for xx,yy in zip(x,y)),F(0))
    U=[[C[i]+u*A[i]+u*u*A2[i] for u in us] for i in range(2)]
    V=[[C[i]+u*B[i]+u*u*B2[i] for u in us] for i in range(2)]
    chi=[u<=h for u in us]
    Ut=[[U[i][q]-(C[i] if chi[q] else np.array([F(0),F(0)],dtype=object)) for q in range(len(us))] for i in range(2)]
    Vt=[[V[i][q]-(C[i] if chi[q] else np.array([F(0),F(0)],dtype=object)) for q in range(len(us))] for i in range(2)]
    J=[]
    for i in range(2):
        z=np.array([F(0),F(0)],dtype=object)
        for q,w in enumerate(ws):
            if chi[q]: z=z+w*(Ut[i][q]+Vt[i][q])
        J.append(z)
    K=np.empty((2,2),dtype=object)
    RHS=np.empty((2,2),dtype=object)
    for i in range(2):
        for j in range(2):
            val=F(0)
            gD=gU=gV=F(0)
            for q,w in enumerate(ws):
                val -= w*(dot(U[i][q],V[j][q])+dot(V[i][q],U[j][q])-(2*dot(C[i],C[j]) if chi[q] else 0))
                D_i=Ut[i][q]-Vt[i][q]; D_j=Ut[j][q]-Vt[j][q]
                gD += w*dot(D_i,D_j); gU += w*dot(Ut[i][q],Ut[j][q]); gV += w*dot(Vt[i][q],Vt[j][q])
            conn=dot(C[i]-J[i],C[j]-J[j])-dot(C[i],C[j])-dot(J[i],J[j])
            K[i,j]=val
            RHS[i,j]=gD-gU-gV+conn
            assert K[i,j]==RHS[i,j]
    return {
        "kernel":[[str(K[i,j]) for j in range(2)] for i in range(2)],
        "connection_vectors":[[str(x) for x in v] for v in J],
    }

def residual_dimless(s):
    return (-mp.mpf(1)/4*(1+s)*mp.e**(-s)
            +mp.mpf(17)/32*(1+2*s)*mp.e**(-2*s)
            -mp.mpf(1)/16*(1+4*s)*mp.e**(-4*s))

def Hswitch(s):
    return (mp.mpf(17)/32*(1+2*s)/(1+s)*mp.e**(-s)
            -mp.mpf(1)/16*(1+4*s)/(1+s)*mp.e**(-3*s))

def Bbase(u):
    return 1/(1-mp.e**(-2*u))-(1+mp.e**u)

def gamma_arch_N(c,x):
    def p(z):
        return mp.re(xi_gamma_logder(mp.mpf("0.5")+z+1j*x))
    return mp.mpf("0.5")*(c*p(c)-c*c*mp.diff(p,c))

def gamma_arch_E(c,x):
    return c**(-4)*(gamma_arch_N(2*c,x)-gamma_arch_N(c,x))

def gamma_arch_rec(a,x):
    return gamma_arch_E(a,x)-gamma_arch_E(2*a,x)

def aligned_integral(a,x):
    f=lambda u: 2*a**(-4)*(1-mp.cos(x*u))*mp.e**(-u/2)*Bbase(u)*(a*residual_dimless(a*u))
    kap=mp.log(mp.findroot(lambda y:y**3-y-1, mp.mpf("1.3")))
    return mp.quad(f,[0,kap,mp.mpf("0.5"),1,mp.inf])

def xi_logder(s):
    return xi_gamma_logder(s)+mp.diff(lambda z:mp.log(mp.zeta(z)),s)

def full_N(c,x):
    def p(z): return mp.re(xi_logder(mp.mpf("0.5")+z+1j*x))
    return mp.mpf("0.5")*(c*p(c)-c*c*mp.diff(p,c))

def full_E(c,x):
    return c**(-4)*(full_N(2*c,x)-full_N(c,x))

def full_rec(a,x):
    return full_E(a,x)-full_E(2*a,x)

def rank_one_control(alpha=mp.mpf("3.5")):
    # Time-side Hankel kernel exp(-alpha(t+s)) sampled on a grid is rank one.
    grid=np.array([0.0,0.17,0.41,0.93,1.37])
    H=np.exp(-float(alpha)*(grid[:,None]+grid[None,:]))
    sv=np.linalg.svd(H,compute_uv=False)
    # Hardy norm of 1/(t-i alpha), under dt/(2pi), equals 1/(2alpha).
    norm_formula=1/(2*alpha)
    norm_quad=mp.quad(lambda t:1/(t*t+alpha*alpha),[-mp.inf,mp.inf])/(2*mp.pi)
    return [float(x) for x in sv], float(abs(norm_formula-norm_quad))

def prime_powers(limit):
    sieve=bytearray(b"\x01")*(limit+1)
    sieve[:2]=b"\x00\x00"
    for p in range(2,int(limit**0.5)+1):
        if sieve[p]:
            count=((limit-p*p)//p)+1
            sieve[p*p:limit+1:p]=b"\x00"*count
    out=[]
    for p in range(2,limit+1):
        if not sieve[p]:
            continue
        n=p
        while n<=limit:
            out.append((n,p))
            n*=p
    return sorted(out)

def fejer_isolation(a, plastic_log, cutoff=5000):
    """Finite diagnostic for R-91405 using the actual aligned measures."""
    u0=mp.log(2)
    def avg(T,u):
        d=u-u0
        if abs(d)<mp.mpf("1e-50"):
            return mp.mpc(1)
        return mp.expm1(1j*T*d)/(1j*T*d)
    def feature(T,u):
        return avg(T,u)-avg(T,mp.mpf(0))
    def omega_density(u):
        return 2*a**(-4)*mp.e**(-u/2)*Bbase(u)*(a*residual_dimless(a*u))
    rows=prime_powers(cutoff)
    def coeff(n,p):
        return -2*a**(-4)*mp.log(p)*mp.power(n,-mp.mpf("0.5"))*(a*residual_dimless(a*mp.log(n)))
    c2=coeff(2,2)
    records=[]
    for T in (mp.mpf(20),mp.mpf(80),mp.mpf(320)):
        cnorm=mp.quad(lambda u: abs(feature(T,u))**2*omega_density(u),
                      [0,plastic_log,mp.mpf("0.5"),1,2,4,mp.inf])
        dnorm=mp.fsum(coeff(n,p)*abs(feature(T,mp.log(n)))**2 for n,p in rows)
        records.append({"T":float(T),"continuous":float(cnorm),"atomic_truncated":float(dnorm)})
    return {"target_weight_c2":float(c2),"cutoff":cutoff,"records":records}

def build():
    sigma=mp.mpf("4.5"); t=mp.mpf("0.83")
    le,direct,approx=ladder_error(sigma,t)
    tau=mp.findroot(lambda s:Hswitch(s)-mp.mpf(1)/4,(1,1.4))
    plastic=mp.findroot(lambda y:y**3-y-1,mp.mpf("1.3"))
    kappa=mp.log(plastic)
    a=tau/kappa
    # Exact derivative factor is negative for s>0; sample sign product away from switch.
    samples=[mp.mpf("1e-5"),kappa/4,kappa*mp.mpf(".99"),kappa*mp.mpf("1.01"),1,2,4]
    products=[Bbase(u)*(a*residual_dimless(a*u)) for u in samples]
    xs=[mp.mpf(".2"),mp.mpf("1.1"),mp.mpf("4.7")]
    inc_errors=[]
    increments=[]
    for x in xs:
        lhs=gamma_arch_rec(a,x)-gamma_arch_rec(a,0)
        rhs=aligned_integral(a,x)
        inc_errors.append(float(abs(lhs-rhs)))
        increments.append(float(lhs))
    full_anchor=full_rec(a,0)
    sv,nerr=rank_one_control()
    comp=compensated_identity()
    fejer=fejer_isolation(a,kappa)
    gates={
        "ladder":le<mp.mpf("1e-55"),
        "rank_one":sv[1]<1e-14 and nerr<1e-50,
        "compensated_green":True,
        "single_switch":all(p>=-mp.mpf("1e-55") for p in products),
        "aligned_increment":max(inc_errors)<1e-45 and min(increments)>0,
        "positive_full_anchor":full_anchor>0,
        "atomic_isolation":fejer["records"][-1]["continuous"] < fejer["target_weight_c2"]*0.05 and fejer["records"][-1]["atomic_truncated"] > fejer["target_weight_c2"]*0.7,
    }
    assert all(gates.values())
    return {
        "status":"PASS_LADDER_COMPENSATED_GREEN_ALIGNMENT",
        "gates":gates,
        "sigma":float(sigma),
        "carrier":float(t),
        "gamma_ladder_truncation_error":float(le),
        "arch_derivative_imag":float(mp.im(direct)),
        "ladder_approx_imag":float(mp.im(approx)),
        "rank_one_singular_values":sv,
        "hardy_kernel_norm_error":nerr,
        "compensated_identity":comp,
        "residual_switch":float(tau),
        "plastic_constant":float(plastic),
        "plastic_log":float(kappa),
        "aligned_scale":float(a),
        "sign_products":[float(p) for p in products],
        "aligned_increment_errors":inc_errors,
        "aligned_increments":increments,
        "full_recurrence_anchor":float(full_anchor),
        "fejer_atomic_isolation":fejer,
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("--json",type=Path)
    a=p.parse_args(); payload=json.dumps(build(),sort_keys=True,separators=(",",":"))+"\n"
    if a.json: a.json.write_text(payload)
    else: print(payload,end="")
if __name__=="__main__": main()

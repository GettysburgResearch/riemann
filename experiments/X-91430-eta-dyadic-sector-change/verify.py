#!/usr/bin/env python3
"""Finite regression for the eta-paired dyadic sector-change route."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp
import numpy as np
mp.mp.dps=70

def pair_coeff(s,m):
    return mp.power(2*m-1,-s)-mp.power(2*m,-s)

def eta_factor(s):
    return mp.altzeta(s)

def jordan_zeta(s,w):
    return mp.zeta(s-w)/mp.zeta(s+w)

def jordan_eta(s,w):
    return (eta_factor(s-w)/eta_factor(s+w)
            *(1-mp.power(2,1-s-w))/(1-mp.power(2,1-s+w)))

def positive_weights(sig,M):
    return np.array([float(pair_coeff(mp.mpf(sig),m)) for m in range(1,M+1)])

def complex_vector(sig,t,M):
    return np.array([complex(pair_coeff(mp.mpf(sig)+1j*mp.mpf(t),m))
                     for m in range(1,M+1)],dtype=complex)

def build():
    w=mp.mpf("0.2")
    s=mp.mpf("1.37")+mp.mpf("0.41")*1j
    factor_error=abs(jordan_zeta(s,w)-jordan_eta(s,w))

    s0=1-w
    eps=mp.mpf("1e-12")
    derivative_numeric=jordan_zeta(s0+eps,w)/eps
    derivative_exact=mp.zeta(1-2*w)
    derivative_error=abs(derivative_numeric-derivative_exact)

    sp=mp.mpf("0.6")+mp.mpf("0.7")*1j
    Mpair=200000
    partial=mp.fsum(pair_coeff(sp,m) for m in range(1,Mpair+1))
    pair_error=abs(partial-eta_factor(sp))
    tail_bound=abs(sp)/mp.re(sp)*mp.power(2*Mpair,-mp.re(sp))

    M=8000
    p=positive_weights(1.0,M)
    q=positive_weights(float(1-2*w),M)
    u=np.sqrt(p); v=np.sqrt(q)
    u=u/np.linalg.norm(u); v=v/np.linalg.norm(v)
    d=u-v
    H=np.eye(M)-2*np.outer(d,d)/np.vdot(d,d).real
    householder_error=float(np.linalg.norm(H@u-v))
    orthogonality_error=float(np.linalg.norm(H.T@H-np.eye(M)))
    hellinger=float(np.vdot(u,v).real)

    carriers=[0.0,0.7,1.4]
    def gram(sig):
        cols=[]
        for t in carriers:
            z=complex_vector(sig,t,M)
            z=z/np.linalg.norm(z)
            cols.append(z)
        A=np.column_stack(cols)
        return A.conj().T@A
    G1=gram(1.0)
    Gh=gram(float(1-2*w))
    carrier_gram_mismatch=float(np.linalg.norm(G1-Gh))

    dyadic_zero=abs(1-mp.power(2,1-s0-w))
    denominator=1-mp.power(2,1-s0+w)
    local_coeff=(mp.log(2)/denominator)*(eta_factor(1-2*w)/eta_factor(1))
    local_coeff_error=abs(local_coeff-derivative_exact)

    gates={
        "eta_factorization":bool(factor_error<mp.mpf("1e-60")),
        "pole_coefficient":bool(derivative_error<mp.mpf("1e-8") and local_coeff_error<mp.mpf("1e-60")),
        "paired_convergence":bool(pair_error<tail_bound),
        "householder":bool(householder_error<1e-12 and orthogonality_error<1e-10),
        "full_family_firewall":bool(carrier_gram_mismatch>1e-3),
        "dyadic_zero":bool(dyadic_zero<mp.mpf("1e-60") and denominator!=0),
    }
    assert all(gates.values())
    return {
        "status":"PASS_ETA_DYADIC_SECTOR_CHANGE",
        "gates":gates,
        "omega":float(w),
        "eta_factorization_error":float(factor_error),
        "pole_derivative_error_at_eps_1e-12":float(derivative_error),
        "local_pole_coefficient_error":float(local_coeff_error),
        "paired_partial_error":float(pair_error),
        "paired_tail_bound":float(tail_bound),
        "householder_error":householder_error,
        "householder_orthogonality_error":orthogonality_error,
        "hellinger_overlap":hellinger,
        "carrier_gram_mismatch":carrier_gram_mismatch,
        "dyadic_zero_error":float(dyadic_zero),
        "dyadic_denominator":float(denominator),
    }

def main():
    p=argparse.ArgumentParser();p.add_argument("--json",type=Path);a=p.parse_args()
    payload=json.dumps(build(),sort_keys=True,separators=(",",":"))+"\n"
    if a.json:a.json.write_text(payload)
    else:print(payload,end="")

if __name__=="__main__":main()

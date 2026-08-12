#!/usr/bin/env python3
"""Finite regression for the parity-domain-wall CPPD reduction."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

def gram(X: np.ndarray) -> np.ndarray:
    return X.conj().T @ X

def herm_error(A: np.ndarray, B: np.ndarray) -> float:
    return float(np.linalg.norm(A-B))

def build() -> dict[str, object]:
    rng=np.random.default_rng(91414)
    h,n=9,5
    U=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    V=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    E=(U+V)/np.sqrt(2.0)
    O=(U-V)/np.sqrt(2.0)

    cross=-(U.conj().T@V+V.conj().T@U)
    parity=gram(O)-gram(E)
    prime_error=herm_error(cross,parity)

    reversed_cross=-cross
    reversed_parity=gram(E)-gram(O)
    long_error=herm_error(reversed_cross,reversed_parity)

    C=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    J=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    comp=gram(C-J)-gram(C)-gram(J)
    comp_parity=0.5*(gram(C-J)-gram(C+J))
    compensation_error=herm_error(comp,comp_parity)

    phases=np.array([0.13,0.47,1.11,2.01,2.71])
    T=np.diag(np.exp(1j*phases))
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    UU=T@X
    VV=X
    EE=(UU+VV)/np.sqrt(2.0)
    OO=(UU-VV)/np.sqrt(2.0)
    A=(np.eye(n)-T)@np.linalg.inv(np.eye(n)+T)
    cayley_error=float(np.linalg.norm(OO + A@EE))
    symbol_error=float(np.max(np.abs(np.diag(A)+1j*np.tan(phases/2))))

    eps=1e-8
    ratio_even_over_odd=abs(1+np.exp(1j*eps))**2/abs(1-np.exp(1j*eps))**2
    ratio_odd_over_even=abs(1-np.exp(1j*(np.pi-eps)))**2/abs(1+np.exp(1j*(np.pi-eps)))**2

    Up=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Vp=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Ush=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Csh=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Jsh=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Ul=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Vl=rng.normal(size=(h,n))+1j*rng.normal(size=(h,n))
    Dp=(Up-Vp)/np.sqrt(2); Sp=(Up+Vp)/np.sqrt(2)
    Sl=(Ul+Vl)/np.sqrt(2); Dl=(Ul-Vl)/np.sqrt(2)
    P=gram(Dp)+gram(Ush)+0.5*gram(Csh-Jsh)+gram(Sl)
    N=gram(Sp)+0.5*gram(Csh+Jsh)+gram(Dl)
    w,Q=np.linalg.eigh((N-P+N.conj().T-P.conj().T)/2)
    Conn=Q@np.diag(np.maximum(w,0.0)+0.25)@Q.conj().T
    residual=(Conn+P-N+ (Conn+P-N).conj().T)/2
    residual_eigs=np.linalg.eigvalsh(residual)

    gates={
        "prime_hadamard":bool(prime_error<1e-12),
        "long_hadamard":bool(long_error<1e-12),
        "compensation_hadamard":bool(compensation_error<1e-12),
        "cayley_graph":bool(cayley_error<1e-12 and symbol_error<1e-12),
        "firewall":bool(ratio_even_over_odd>1e15 and ratio_odd_over_even>1e15),
        "synthetic_schur":bool(float(residual_eigs.min())>0.2),
    }
    assert all(gates.values())
    return {
        "status":"PASS_PARITY_DOMAIN_WALL_CPPD",
        "gates":gates,
        "prime_hadamard_error":prime_error,
        "long_hadamard_error":long_error,
        "compensation_hadamard_error":compensation_error,
        "cayley_graph_error":cayley_error,
        "cayley_symbol_error":symbol_error,
        "even_over_odd_ratio_near_zero":float(ratio_even_over_odd),
        "odd_over_even_ratio_near_pi":float(ratio_odd_over_even),
        "synthetic_residual_eigenvalues":[float(x) for x in residual_eigs],
    }

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--json",type=Path)
    a=p.parse_args()
    payload=json.dumps(build(),sort_keys=True,separators=(",",":"))+"\n"
    if a.json: a.json.write_text(payload)
    else: print(payload,end="")

if __name__=="__main__":
    main()

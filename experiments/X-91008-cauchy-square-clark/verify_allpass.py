#!/usr/bin/env python3
"""Finite high-precision checks for the dyadic Cauchy three-state all-pass."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

def generator():
    return mp.matrix([
        [0, mp.sqrt(6)/2, 0],
        [-mp.sqrt(6)/2, 0, mp.sqrt(10)/2],
        [0, -mp.sqrt(10)/2, 0],
    ])

def transfer(a,u):
    den=4*(a*a+u*u)
    return mp.matrix([
        [(4*a*a+u*u)/den, 2*mp.sqrt(6)*a*u/den, mp.sqrt(15)*u*u/den],
        [-2*mp.sqrt(6)*a*u/den, (4*a*a-4*u*u)/den, 2*mp.sqrt(10)*a*u/den],
        [mp.sqrt(15)*u*u/den, -2*mp.sqrt(10)*a*u/den, (4*a*a-u*u)/den],
    ])

def h(a,u):
    return a*a/(a*a+u*u)

def g1(a,u):
    return 2*mp.sqrt(6)*a**3*u/((a*a+u*u)*(4*a*a+u*u))

def g2(a,u):
    return mp.sqrt(15)*a*a*u*u/((a*a+u*u)*(4*a*a+u*u))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--json",type=Path,default=None)
    args=ap.parse_args()
    A=generator()
    checks=0
    max_orth=mp.mpf(0)
    max_det=mp.mpf(0)
    max_cayley=mp.mpf(0)
    max_channel=mp.mpf(0)
    max_eigen=mp.mpf(0)

    A3=A*A*A
    max_generator=max(abs(A3[i,j]+4*A[i,j]) for i in range(3) for j in range(3))
    assert max_generator < mp.mpf("1e-75")
    checks += 9

    for a in [mp.mpf("0.07"),mp.mpf("0.2"),mp.mpf("0.63"),mp.mpf("1.4")]:
        for u in [mp.mpf("-5.0"),mp.mpf("-0.8"),mp.mpf("0"),mp.mpf("0.13"),mp.mpf("2.7")]:
            U=transfer(a,u)
            orth=U*U.T-mp.eye(3)
            err=max(abs(orth[i,j]) for i in range(3) for j in range(3))
            max_orth=max(max_orth,err)
            assert err < mp.mpf("1e-75")
            det=mp.det(U)
            max_det=max(max_det,abs(det-1))
            assert abs(det-1)<mp.mpf("1e-75")
            C=(mp.eye(3)-u*A/(2*a))**-1*(mp.eye(3)+u*A/(2*a))
            err=max(abs(U[i,j]-C[i,j]) for i in range(3) for j in range(3))
            max_cayley=max(max_cayley,err)
            assert err < mp.mpf("1e-75")
            vec=[h(2*a,u)*U[0,j] for j in range(3)]
            target=[h(a,u),g1(a,u),g2(a,u)]
            err=max(abs(vec[j]-target[j]) for j in range(3))
            max_channel=max(max_channel,err)
            assert err < mp.mpf("1e-75")
            eig=mp.eig(U,left=False,right=False)
            expected=[1,(a-1j*u)/(a+1j*u),(a+1j*u)/(a-1j*u)]
            import itertools
            best=min(
                max(abs(eig[i]-expected[p[i]]) for i in range(3))
                for p in itertools.permutations(range(3))
            )
            max_eigen=max(max_eigen,best)
            assert best < mp.mpf("1e-65")
            checks += 9+1+9+3+3

    result={
        "classification":"PASS_DYADIC_CAUCHY_THREE_STATE_ALLPASS",
        "checks":checks,
        "max_generator_cubic_error":mp.nstr(max_generator,12),
        "max_orthogonality_error":mp.nstr(max_orth,12),
        "max_determinant_error":mp.nstr(max_det,12),
        "max_cayley_error":mp.nstr(max_cayley,12),
        "max_first_row_channel_error":mp.nstr(max_channel,12),
        "max_eigenvalue_matching_error":mp.nstr(max_eigen,12),
        "scope":"finite high-precision scattering checks only; no critical-boundary positivity or RH claim",
    }
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.json:
        args.json.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    print(result["classification"])
    return 0

if __name__=="__main__":
    raise SystemExit(main())

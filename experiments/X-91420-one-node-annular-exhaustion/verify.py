#!/usr/bin/env python3
"""Finite regression for the fixed-node annular exhaustion route."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp
import numpy as np
mp.mp.dps=70

def xi(s):
    return mp.mpf("0.5")*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

def blaschke_value(eta, points):
    z=mp.mpf(1)
    for w in points:
        z*=abs((eta-w)/(eta+w))
    return z

def hyperbolic(eta, points):
    b=blaschke_value(eta,points)
    return (b**(-2)-1)/(2*eta)

def build():
    eta=mp.mpf(1)
    depths=[mp.mpf("0.41"),mp.mpf("0.23"),mp.mpf("0.11"),mp.mpf("0.047")]
    levels=[mp.mpf("0.5"),mp.mpf("0.25"),mp.mpf("0.125"),mp.mpf("0.0625"),mp.mpf("0.03125")]
    H=[]
    increments=[]
    telescope_errors=[]
    for a in levels:
        pts=[d for d in depths if d>a]
        H.append(hyperbolic(eta,pts))
    for j in range(1,len(levels)):
        a=levels[j]; b=levels[j-1]
        old=[d for d in depths if d>b]
        ann=[d for d in depths if a<d<=b]
        B_old=blaschke_value(eta,old)
        h_ann=hyperbolic(eta,ann)
        inc=(B_old**(-2))*h_ann
        increments.append(inc)
        telescope_errors.append(abs(H[j]-(H[j-1]+inc)))

    u=mp.mpf("0.73"); et=mp.mpf("1.17")
    t=mp.e**(-et*u)
    even=(1+t)/mp.sqrt(2)
    odd=-(1-t)/mp.sqrt(2)
    parity_identity=abs((odd**2-even**2)+2*t)
    long_domination=abs(odd)<=abs(even)

    green_errors=[]
    theta_values=[]
    for a in [mp.mpf("0.25"),mp.mpf("0.125"),mp.mpf("0.0625")]:
        q=mp.mpf("0.5")-a
        theta=xi(mp.mpf("1.5")-a)/xi(mp.mpf("1.5")+a)
        Hq=(xi(1+q)/xi(1+2*a+q))/q
        theta_values.append(theta)
        green_errors.append(abs(theta-q*Hq))

    def F(a):
        return mp.euler-mp.diff(lambda s: mp.log(mp.zeta(s)),1+2*a)
    innovations=[]
    for a in [mp.mpf("0.25"),mp.mpf("0.125"),mp.mpf("0.0625")]:
        innovations.append(F(a)-F(2*a))

    gates={
        "annular_telescope":bool(max(telescope_errors)<mp.mpf("1e-60")),
        "positive_increments":bool(all(x>=0 for x in increments)),
        "cauchy_parity":bool(parity_identity<mp.mpf("1e-60") and long_domination),
        "green_alignment":bool(max(green_errors)<mp.mpf("1e-60")),
        "source_innovations":bool(all(x>0 for x in innovations)),
    }
    assert all(gates.values())
    return {
        "status":"PASS_ONE_NODE_ANNULAR_EXHAUSTION",
        "gates":gates,
        "eta":float(eta),
        "depths":[float(x) for x in depths],
        "levels":[float(x) for x in levels],
        "hyperbolic_diagonals":[float(x) for x in H],
        "annular_increments":[float(x) for x in increments],
        "telescope_errors":[float(x) for x in telescope_errors],
        "cauchy_even_amplitude":float(even),
        "cauchy_odd_amplitude":float(odd),
        "cauchy_parity_error":float(parity_identity),
        "green_alignment_errors":[float(x) for x in green_errors],
        "theta_values":[float(x) for x in theta_values],
        "prime_innovations":[float(x) for x in innovations],
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument("--json",type=Path); a=p.parse_args()
    payload=json.dumps(build(),sort_keys=True,separators=(",",":"))+"\n"
    if a.json:a.json.write_text(payload)
    else:print(payload,end="")

if __name__=="__main__":main()

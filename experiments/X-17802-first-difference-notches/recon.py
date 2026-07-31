#!/usr/bin/env python3
"""Ordinary high-precision discovery scan for hybrid first-difference notches."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp


def Mval(z,terms=120):
    out=mp.mpc(1)
    for j in range(1,terms+1):
        r=mp.ldexp(1,-j); rz=r*z
        out *= -mp.expm1(-rz)/rz
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--dps',type=int,default=60)
    args=ap.parse_args();mp.mp.dps=args.dps
    zeros=[mp.im(mp.zetazero(j)) for j in range(1,101)];design=zeros[:5];h=mp.log(4)
    base=[];box=[[None]*100 for _ in range(5)];diff=[[None]*100 for _ in range(5)]
    for k,gamma in enumerate(zeros):
        z=mp.j*gamma;m=Mval(z)
        base.append(mp.exp(-2*z)*m*m*(1-2*mp.exp(-h*z)))
        for j,g0 in enumerate(design):
            r=2*mp.pi/g0;A=-mp.expm1(-r*z)
            box[j][k]=(A/(r*z))**2;diff[j][k]=A/2
    T=mp.mpf(3000175332800);upp=[15,22,26,31,33]
    floors=[(3*T/u)**2 for u in upp]
    rows=[]
    for mask in range(32):
        total=mp.mpf(0)
        for k in range(100):
            v=base[k]
            for j in range(5):v*=diff[j][k] if mask>>j&1 else box[j][k]
            total+=abs(v)**2
        gain=mp.mpf(1)
        for j in range(5):
            if mask>>j&1:gain*=floors[j]
        rows.append({'difference_indices':[j+1 for j in range(5) if mask>>j&1],
                     'first100_rh_rms':mp.nstr(mp.sqrt(2*total),30),
                     'rigorous_verified_frontier_gain_lower':mp.nstr(gain,30)})
    result={'classification':'EMPIRICAL_NON_DIRECTED','decimal_digits':args.dps,
            'zero_count':100,'rows':rows,
            'proof_boundary':'Midpoint mpmath zeta zeros and ordinary complex arithmetic; scheduling only.'}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()

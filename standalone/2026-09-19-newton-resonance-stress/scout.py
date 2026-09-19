#!/usr/bin/env python3
"""Floating candidate chooser, NOT the accepting checker or a ball calculation."""
import argparse
import base64
import json
import math
from pathlib import Path
import zlib


def smooth(x):
    if x<=0:return 0.0
    if x>=1:return 1.0
    return x*x*x*(10+x*(-15+6*x))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('candidate.json'))
    args=parser.parse_args()
    if args.output.exists():raise SystemExit('Refusing to overwrite an existing file')
    R=65536;Q=25*2**20;T=.65*math.sqrt(R);L=math.log(4/3);ramp=.08
    start=R-2;end=4*R//3+3;H={}
    for n in range(start,end+1):
        u=math.log(n/R)
        phi=smooth(u/ramp)*smooth((L-u)/ramp)
        H[n]=round(Q*math.sqrt(n)/T*phi*math.sin(T*u))
    coeff={};old=0
    for n in range(start+1,end):
        z=n*(H[n+1]-H[n])-H[n]
        cumulative=(2*z+Q)//(2*Q)
        change=cumulative-old;old=cumulative
        if change:coeff[n]=change
    if old or not set(coeff.values())<={-1,1}:raise SystemExit('Candidate not ternary/zero-total')
    a=min(coeff);b=max(coeff)
    word=''.join('+' if coeff.get(n,0)==1 else '-' if coeff.get(n,0)==-1 else '0' for n in range(a,b+1))
    alpha={1:1,2:-1,3:-1,5:-1,6:-1,10:1,15:1,30:1}
    data={'kind':'ternary-cumulative-rounding-v1','R':R,'Y':2*R,'start':a,
          'alpha':[[k,v] for k,v in alpha.items()], 'X0':R*R,'X1':(4*R//3+2)**2,
          'bins':4096,'word_codec':'zlib-base64-ascii','word_length':len(word),
          'word_zlib_b64':base64.b64encode(zlib.compress(word.encode(),9)).decode()}
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print('Candidate written; no certificate or cross-platform transcendental identity claimed.')


if __name__=='__main__':main()

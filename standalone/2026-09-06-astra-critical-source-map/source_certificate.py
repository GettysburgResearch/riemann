#!/usr/bin/env python3
"""Directed elementary first-vector certificate; no zeta/gamma oracle.

Reconstructs d_(3/4) from the exact factorial cells. Every calculation uses
integer intervals on a fixed dyadic grid. The infinite positive tail is
bounded analytically. This is ONE projection, not a high-rank/RH proof.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path

BITS = 192
Q = 1 << BITS
TERMS = 72
MAX_CELLS = 4096

class Interval:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo: int, hi: int):
        if lo > hi:
            raise ValueError('reversed endpoints')
        self.lo, self.hi = lo, hi
    @classmethod
    def rat(cls, p: int, q: int = 1):
        if q <= 0:
            raise ValueError('nonpositive denominator')
        return cls(p*Q//q, -((-p*Q)//q))
    def __add__(self, other):
        if isinstance(other, int): other=Interval.rat(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi, -self.lo)
    def __sub__(self, other):
        if isinstance(other, int): other=Interval.rat(other)
        return self+-other
    def __rsub__(self, other): return (-self)+other
    def __mul__(self, other):
        if isinstance(other, int): other=Interval.rat(other)
        v=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(v)//Q, -((-max(v))//Q))
    __rmul__=__mul__
    def __truediv__(self, other):
        if isinstance(other, int): other=Interval.rat(other)
        if other.lo <= 0 <= other.hi:
            raise ValueError('division by a zero-containing interval')
        vals=[(x*Q,y) for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        lows=[];his=[]
        for x,y in vals:
            if y<0:x,y=-x,-y
            lows.append(x//y);his.append(-((-x)//y))
        return Interval(min(lows),max(his))
    def __rtruediv__(self, other):
        return Interval.rat(other)/self
    def square(self):
        if self.lo<=0<=self.hi:
            return Interval(0,-((-max(self.lo*self.lo,self.hi*self.hi))//Q))
        return self*self
    def record(self):
        return {'lower_numerator':str(self.lo),'upper_numerator':str(self.hi),
                'denominator_power_of_two':BITS}


def atanh_log_ratio(p: int, q: int) -> Interval:
    """log(p/q) for 1<=p/q<=2 using an explicit positive-series tail."""
    if not q<=p<=2*q:
        raise ValueError('ratio outside [1,2]')
    if p==q:return Interval.rat(0)
    z=Interval.rat(p-q,p+q)
    z2=z*z; power=z; value=Interval.rat(0)
    for j in range(TERMS):
        value=value+power*Interval.rat(2,2*j+1)
        power=power*z2
    # z<=1/3; 2 sum_(j>=m) z^(2j+1)/(2j+1)
    # <=(9/4)*3^(-(2m+1))/(2m+1).
    tail=Interval.rat(9,4*(2*TERMS+1)*3**(2*TERMS+1))
    return Interval(value.lo,value.hi+tail.hi)

LOG2=atanh_log_ratio(2,1)

def log_int(n: int) -> Interval:
    if n<1:raise ValueError('log input')
    k=n.bit_length()-1
    return k*LOG2+atanh_log_ratio(n,1<<k)

def inverse_quarter_power(n: int, k: int) -> Interval:
    """n^(-k/4) enclosed by fourth-root integer inequalities."""
    if n<1 or k<0:raise ValueError('power input')
    v=(Q**4)//(n**k)
    r=math.isqrt(math.isqrt(v))
    if not r**4*n**k<=Q**4<(r+1)**4*n**k:
        raise RuntimeError('integer fourth-root invariant')
    return Interval(r,r if r**4*n**k==Q**4 else r+1)


def run(kmax: int=MAX_CELLS):
    if not 16<=kmax<=MAX_CELLS:
        raise ValueError('cell limit outside published bounded contract')
    logs=[None]+[log_int(n) for n in range(1,kmax+1)]
    sqpow=[None]+[inverse_quarter_power(n,6) for n in range(1,kmax+1)]
    lapow=[None]+[inverse_quarter_power(n,7) for n in range(1,kmax+1)]
    lam2=Interval.rat(3,2);lam1=Interval.rat(7,4)
    fact=Interval.rat(0);norm=Interval.rat(0);lap=Interval.rat(0)
    for n in range(1,kmax):
        fact=fact+logs[n]
        A=fact+n
        def norm_end(idx):
            v=A-n*logs[idx]
            p=v.square()/lam2-2*n*v/(lam2*lam2)+Interval.rat(2*n*n)/(lam2*lam2*lam2)
            return sqpow[idx]*p
        def lap_end(idx):
            v=A-n*logs[idx]
            return lapow[idx]*(v/lam1-Interval.rat(n)/(lam1*lam1))
        norm=norm+norm_end(n)-norm_end(n+1)
        lap=lap+lap_end(n)-lap_end(n+1)
    T=logs[kmax]
    # Positive tails bounded using 0<g(t)<=1+t.
    norm_tail=sqpow[kmax]*((1+T).square()/lam2+2*(1+T)/(lam2*lam2)+2/(lam2*lam2*lam2))
    lap_tail=lapow[kmax]*((1+T)/lam1+1/(lam1*lam1))
    ng=Interval(norm.lo,norm.hi+norm_tail.hi)
    dl=Interval(lap.lo,lap.hi+lap_tail.hi)
    # Independently enclose D_b(1) through its positive Dirichlet series.
    zsum=Interval.rat(0)
    for n in range(1,kmax+1): zsum=zsum+lapow[n]
    ztail_lo=Interval.rat(4,3)*inverse_quarter_power(kmax+1,3)
    ztail_hi=Interval.rat(4,3)*inverse_quarter_power(kmax,3)
    dz=Interval.rat(12,49)*Interval(zsum.lo+ztail_lo.lo,zsum.hi+ztail_hi.hi)
    dl_source=dl
    dl=Interval(max(dl.lo,dz.lo),min(dl.hi,dz.hi))
    eps=1-2*dl.square()/ng
    if not (0<ng.lo<=ng.hi and 0<dl.lo<=dl.hi):
        raise RuntimeError('source positivity failed')
    if eps.lo<0 or eps.hi>=Q:
        raise RuntimeError('projection range failed')
    coarse=Interval.rat(11,50)
    if kmax==MAX_CELLS and not eps.hi<coarse.lo:
        raise RuntimeError('published 11/50 upper bound failed')
    return {
        'schema':'csm26.factorial-source-first-vector.v1',
        'arithmetic':'DIRECTED_INTERVAL','implementation':'DYADIC_INTEGER',
        'b':{'numerator':3,'denominator':4},'eta':1,
        'integer_cutoff':kmax,'complete_cells':kmax-1,
        'precision_bits':BITS,'atanh_terms':TERMS,
        'norm_squared':ng.record(),'laplace_at_one':dl.record(),
        'laplace_source_enclosure':dl_source.record(),'laplace_dirichlet_enclosure':dz.record(),
        'first_projection_error_squared':eps.record(),
        'norm_tail_upper':str(norm_tail.hi),
        'laplace_tail_upper':str(lap_tail.hi),
        'coarse_error_upper':'11/50' if kmax==MAX_CELLS else None,
        'RH_proved':False,'higher_rank_extrapolation':False,
        'zeta_gamma_oracle_used':False,
        'boundary':'One actual source-vector projection, with all real cells and the infinite tail bounded.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    p.add_argument('--compare',type=Path)
    args=p.parse_args()
    result=run()
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.compare and args.compare.read_text()!=text:
        raise ValueError('retained certificate does not match reconstruction')
    if args.output:args.output.write_text(text)
    else:print(text,end='')

if __name__=='__main__':
    main()

#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path

DEN=10**65
TERMS=170

class I:
    def __init__(self,lo,hi=None):
        self.lo=Fraction(lo);self.hi=Fraction(lo if hi is None else hi)
    def __add__(self,o):
        o=as_i(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+(-as_i(o))
    def __rsub__(self,o):return as_i(o)-self
    def __mul__(self,o):
        o=as_i(o);v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o);assert not(o.lo<=0<=o.hi)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return as_i(o)/self

def as_i(x):return x if isinstance(x,I) else I(x)

def sqrt_i(n):
    lo=isqrt(n*DEN*DEN);hi=lo if lo*lo==n*DEN*DEN else lo+1
    return I(Fraction(lo,DEN),Fraction(hi,DEN))

def invsqrt_i(n):return 1/sqrt_i(n)

def log_i(x):
    x=Fraction(x);e=0;y=x
    while y>=2:y/=2;e+=1
    while y<1:y*=2;e-=1
    def base(z):
        z2=z*z;p=z;s=Fraction(0)
        for k in range(TERMS):s+=p/Fraction(2*k+1);p*=z2
        s*=2;tail=2*p/(Fraction(2*TERMS+1)*(1-z2))
        return I(s,s+tail)
    return base((y-1)/(y+1))+e*base(Fraction(1,3))

def gamma_i(j,m):
    if m==j:return Fraction(j+1,j-1)*invsqrt_i(j)
    if m==j+1:return -Fraction((j+1)*(j-2),j*(j-1))*invsqrt_i(j+1)
    if m>=j+2:return Fraction(2,j*(j-1))*invsqrt_i(m)
    return I(0)

def main():
    sqrt67=sqrt_i(67);log67=log_i(67)
    minimum=None;gates=0
    for j in range(2,67):
        c=Fraction(2,j*(j-1));H=I(0);Hlog=I(0)
        for m in range(1,j):
            inv=invsqrt_i(m);H+=inv;Hlog+=inv*log_i(m)
        a=Fraction(j+2,j)*invsqrt_i(j);b=invsqrt_i(j+1)
        eta=c*(1+H)-a+b
        K=-4*c+c*Hlog-a*log_i(j)+b*log_i(j+1)
        D=22*c+10*eta+5*K
        p_gate=10*eta*(log67/2)+5*eta*log_i(j)-D+10*eta
        assert p_gate.lo>0,(j,p_gate.lo)
        C=I(0);Dcell=I(0)
        for N in range(j,67):
            g=gamma_i(j,N);C+=g;Dcell+=g*log_i(N)
            Q=C*log_i(N)-Dcell
            S=5*sqrt_i(N)-3
            M=5*sqrt_i(N)*(2*C-Q)-6*C
            child_upper=M/(2*S*S)
            parent_lower=(sqrt67/(50*sqrt_i(N+1))
                          *(5*eta*(log67+log_i(N))-D)
                          +3*eta/Fraction(25*(N+1)))
            gap=parent_lower-child_upper
            assert gap.lo>0,(j,N,gap.lo)
            rec=(gap.lo,j,N)
            if minimum is None or rec[0]<minimum[0]:minimum=rec
            gates+=1
    result={
      'classification':'PASS_INNER_CAUSAL_COMPONENT_RATIO_MONOTONICITY',
      'p_monotonicity_gates':65,
      'child_cell_gates':gates,
      'minimum_gap_lower':str(minimum[0]),
      'minimum_gap_decimal':float(minimum[0]),
      'worst_row':minimum[1],
      'worst_cell':minimum[2],
      'scope':(
        'Exact Fraction arithmetic and directed square-root/logarithm intervals '
        'certify the compact derivative-scaling gates. Together with L-91359 '
        'and the analytic derivative identity in L-91360, this proves the full '
        'causal row-per-score source ordering. It does not prove the remaining '
        'full even/odd determinant or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification']);print(out)
if __name__=='__main__':main()

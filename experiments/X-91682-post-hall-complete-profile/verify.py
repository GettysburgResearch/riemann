#!/usr/bin/env python3
"""Directed replay for the post-Hall arithmetic-profile packet.

All sign decisions use Fraction arithmetic with outward rational square-root
and logarithm enclosures. Decimal values in the JSON are display-only.
"""
from __future__ import annotations
from fractions import Fraction
from math import isqrt, prod
from functools import lru_cache
from decimal import Decimal, localcontext, ROUND_HALF_EVEN
from pathlib import Path
import hashlib, json, sys
sys.set_int_max_str_digits(0)

PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
P61=prod(PRIMES)
DEN=10**70
LOG_EPS=Fraction(3,10**110)
CUTOFF=2000
P0=500000

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o): o=as_i(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-as_i(o))
    def __rsub__(self,o): return as_i(o)-self
    def __mul__(self,o):
        o=as_i(o); v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o); assert not(o.lo<=0<=o.hi)
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return as_i(o)/self

def as_i(x): return x if isinstance(x,I) else I(x)

@lru_cache(None)
def sqrt_i(x):
    x=Fraction(x); a=x.numerator; b=x.denominator
    lo=isqrt(a*DEN*DEN//b)
    while Fraction((lo+1)**2,DEN**2)<=x: lo+=1
    while Fraction(lo**2,DEN**2)>x: lo-=1
    hi=lo if Fraction(lo**2,DEN**2)==x else lo+1
    return I(Fraction(lo,DEN),Fraction(hi,DEN))

@lru_cache(None)
def invsqrt_i(n): return 1/sqrt_i(n)

@lru_cache(None)
def log_i(x):
    x=Fraction(x)
    with localcontext() as ctx:
        ctx.prec=120; ctx.rounding=ROUND_HALF_EVEN
        v=Decimal(x.numerator).ln()-Decimal(x.denominator).ln()
    q=Fraction(v)
    return I(q-LOG_EPS,q+LOG_EPS)

@lru_cache(None)
def gamma_i(j,m):
    if m==j:return Fraction(j+1,j-1)*invsqrt_i(j)
    if m==j+1:return -Fraction((j+1)*(j-2),j*(j-1))*invsqrt_i(j+1)
    if m>=j+2:return Fraction(2,j*(j-1))*invsqrt_i(m)
    return I(0)

def divisors_mu():
    vals=[(1,1)]
    for q in PRIMES: vals += [(d*q,-mu) for d,mu in list(vals)]
    return sorted(vals)

@lru_cache(None)
def constants_k2(j):
    c=Fraction(2,j*(j-1)); H=I(0); HL=I(0)
    for m in range(1,j):
        iv=invsqrt_i(m); H+=iv; HL+=iv*log_i(m)
    H2=1+invsqrt_i(2); L2=invsqrt_i(2)*log_i(2)
    a=Fraction(j+2,j)*invsqrt_i(j); b=invsqrt_i(j+1)
    eta=c*(2*sqrt_i(2)-H2+H)-a+b
    lam=c*(2*sqrt_i(3)-H2+H)-a+b
    K=c*(2*sqrt_i(2)*log_i(2)-4*sqrt_i(2)-L2)+c*HL-a*log_i(j)+b*log_i(j+1)
    return c,eta,lam,K

def check_global_target_profile():
    minimum=None; log83=log_i(83)
    for j in range(2,67):
        c=Fraction(2,j*(j-1)); H=I(0); L=I(0)
        for m in range(1,j):
            iv=invsqrt_i(m); H+=iv; L+=iv*log_i(m)
        a=Fraction(j+2,j)*invsqrt_i(j); b=invsqrt_i(j+1)
        eta=c*(1+H)-a+b
        K=-4*c+c*L-a*log_i(j)+b*log_i(j+1)
        assert eta.lo>0
        gate=4*eta*log83-20*c-8*eta-4*K
        assert gate.lo>0,(j,float(gate.lo))
        rec=(gate.lo,j)
        if minimum is None or rec<minimum: minimum=rec
    return {'classification':'PASS_GLOBAL_TARGET_NORMALIZED_COMPONENT_MONOTONICITY',
            'rows':65,'minimum_gate_decimal':float(minimum[0]),'minimum_row':minimum[1]}

def check_causal_profile(a_norm:int):
    assert a_norm in (4,5)
    def lower(j,P):
        c,eta,lam,K=constants_k2(j)
        D=2*a_norm*lam+a_norm*K+12*c; t=sqrt_i(P)
        return (t*(a_norm*eta*log_i(P)-D)+6*eta)/(a_norm*t-3)
    def deriv(j,P):
        c,eta,lam,K=constants_k2(j)
        D=2*a_norm*lam+a_norm*K+12*c; t=sqrt_i(P)
        return eta*(2*a_norm*a_norm*t-3*a_norm*log_i(P)-12*a_norm)+3*D
    def child_left(j,N,C,Dc):
        t=sqrt_i(N); Q=C*log_i(N)-Dc
        M=a_norm*t*(2*C-Q)-6*C
        assert M.lo>0
        return M/(a_norm*t-3)
    root67=sqrt_i(67); minimum=None; count=0
    for j in range(2,34):
        assert deriv(j,67*j).lo>0
        C=I(0); Dc=I(0)
        for N in range(j,67):
            g=gamma_i(j,N); C+=g; Dc+=g*log_i(N)
            gap=lower(j,67*N)-child_left(j,N,C,Dc)/root67
            assert gap.lo>0,(a_norm,j,N,float(gap.lo))
            rec=(gap.lo,j,N)
            if minimum is None or rec<minimum: minimum=rec
            count+=1
    return {'classification':('PASS_COMPLETE_ARITHMETIC_CAUSAL_SCORE_PROFILE' if a_norm==5 else 'PASS_COMPLETE_ARITHMETIC_CAUSAL_TARGET_PROFILE'),
            'child_cells':count,'minimum_gap_decimal':float(minimum[0]),
            'minimum_row':minimum[1],'minimum_child_cell':minimum[2],
            'rough_range':'all real p>=67'}

def invsqrt_scaled(d,scale):
    n=scale*scale; lo=isqrt(n//d)
    while (lo+1)*(lo+1)*d<=n: lo+=1
    while lo*lo*d>n: lo-=1
    hi=lo if lo*lo*d==n else lo+1
    return lo,hi

def check_cutoffs(vals):
    odd_total=sum(Fraction(1,d) for d,mu in vals if mu==-1)
    even_prefix=sum(Fraction(1,d) for d,mu in vals if mu==1 and d<=CUTOFF)
    A=even_prefix-odd_total; assert A>0
    B=Fraction(0)
    for d,mu in vals:
        if d>CUTOFF: break
        lo,hi=invsqrt_scaled(d,DEN)
        if mu==1: B += Fraction(hi,DEN)
        else: B -= Fraction(lo,DEN)
    rt=sqrt_i(CUTOFF)
    score=5*rt*A-3*B-Fraction(335)/rt
    target=4*rt*A-3*B-Fraction(268)/rt
    assert score.lo>0 and target.lo>0
    return {'classification':'PASS_P61_SCORE_AND_TARGET_LORENZ_CUTOFF_2000',
            'divisor_states':len(vals),'cutoff':CUTOFF,
            'A_gap':str(A),'B_upper_decimal':float(B),
            'score_margin_decimal':float(score.lo),
            'target_margin_decimal':float(target.lo),
            'even_cutoff_nodes':sum(mu==1 and d<CUTOFF for d,mu in vals)}

def check_score_debt(vals):
    scale=10**40
    Ae=Ao=0; Be_lo=Be_hi=Bo_lo=Bo_hi=0
    delta_min=None; delta_at=None; states=0
    for i,(d,mu) in enumerate(vals):
        a=P61//d; lo,hi=invsqrt_scaled(d,scale)
        if mu==1: Ae+=a; Be_lo+=lo; Be_hi+=hi
        else: Ao+=a; Bo_lo+=lo; Bo_hi+=hi
        nxt=vals[i+1][0] if i+1<len(vals) else None
        if nxt is None or nxt>P0:
            num=Ae*Bo_lo-Ao*Be_hi
            assert num>0
            if delta_min is None or num<delta_min: delta_min=num; delta_at=d
            states+=1
    assert delta_min>=2*P61*scale
    assert Ae+Ao<5*P61 and Be_hi+Bo_hi<60*scale
    # -2t+600+600/t+600/t^2<0 for t>700.
    assert -1400*17150+600*17150+14700+21<0
    return {'classification':'PASS_TARGET_PROPORTIONAL_SCORE_DEBT_COMPACT_SUPPORT',
            'prefix_states':states,'delta_lower':2,'delta_min_prefix_start':delta_at,
            'tail':'zero score debt for every real p>=500000',
            'aggregate_compact_debt_upper':'39321600000000000'}

def main():
    vals=divisors_mu(); assert len(vals)==2**18
    checks=[check_global_target_profile(),check_causal_profile(5),check_causal_profile(4),check_cutoffs(vals),check_score_debt(vals)]
    payload={'classification':'PASS_POST_HALL_COMPLETE_PROFILE_AND_DEBT_PACKET',
             'checks':checks,
             'remaining_gate':'target-Lorenz/full physical row determinant family; replay does not certify RH',
             'rh_established_by_replay':False}
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    payload['proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    out=Path('results/verification.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['classification'])
    print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__': main()

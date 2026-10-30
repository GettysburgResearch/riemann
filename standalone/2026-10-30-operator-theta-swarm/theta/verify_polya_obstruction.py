#!/usr/bin/env python3
"""Exact rational interval proof of a negative 8th theta-envelope derivative.

Uses only the Python standard library. The proof obligation is G^(8)(0)<0,
where G(t)=exp(2*pi*cosh(2*t))*Phi(t), and Phi has the explicit theta sum
in PROOF.md. Infinite n>=5 derivative tail is bounded analytically below.
"""
from fractions import Fraction as F
from math import comb
import json

Q=10**70
class I:
    def __init__(self,lo,hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        self.lo=F((lo*Q).numerator//(lo*Q).denominator,Q)
        self.hi=F(-((-hi*Q).numerator//(-hi*Q).denominator),Q)
    def __add__(self,o):
        o=cv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-cv(o)
    def __rsub__(self,o): return cv(o)+-self
    def __mul__(self,o):
        o=cv(o); v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=cv(o)
        if o.lo<=0<=o.hi: raise ArithmeticError('zero in denominator')
        return self*I(1/o.hi,1/o.lo)
    def __pow__(self,n):
        if n<0: return cv(1)/(self**(-n))
        r=cv(1)
        for _ in range(n): r=r*self
        return r

def cv(x): return x if isinstance(x,I) else I(x)
def atan_inv(q,terms=65):
    s=F(0)
    for k in range(terms): s+=F((-1)**k,(2*k+1)*q**(2*k+1))
    r=F((-1)**terms,(2*terms+1)*q**(2*terms+1))
    return I(min(s,s+r),max(s,s+r))

def exp_point(x):
    # Reduce to |u|<=1/2; sum alternating or positive series by a two-sided
    # absolute tail bound. All arithmetic and comparisons are rational.
    x=F(x); scale=0
    while abs(x)>F(1,2): x/=2; scale+=1
    s=F(1); term=F(1)
    for k in range(1,90): term*=x/k; s+=term
    next_abs=abs(term*x/90)
    tail=next_abs/(1-abs(x)/91)
    y=I(s-tail,s+tail)
    for _ in range(scale): y=y*y
    return y

def exp_interval(x):
    x=cv(x)
    return I(exp_point(x.lo).lo,exp_point(x.hi).hi)

PI=16*atan_inv(5)-4*atan_inv(239)
if not F(314159,100000)<PI.lo<PI.hi<F(22,7): raise ArithmeticError('pi bracket')

def derivative(a,A,B,m):
    ell=[I(0)]+[(a if j==1 else 0)-A*2**j+B*(-2)**j for j in range(1,m+1)]
    val=[exp_interval(-A+B)]
    for k in range(1,m+1):
        val.append(sum((comb(k-1,j-1)*ell[j]*val[k-j] for j in range(1,k+1)),I(0)))
    return val[m]

m=8; partial=I(0); terms=[]
for n in range(1,5):
    A=PI*(n*n-1); B=PI
    z=4*PI**2*n**4*derivative(F(9,2),A,B,m)-6*PI*n*n*derivative(F(5,2),A,B,m)
    partial+=z
    terms.append({'n':n,'lo':str(z.lo),'hi':str(z.hi)})
# For n>=5, |ell_j| <= 2^j*4n^2. The complete Bell polynomial obeys
# B_8(2C,4C,...,256C)=256*T_8(C)<=256*B_8*C^8 for C>=1.
# B_8 = 4140; source coefficient absolute sum <60 n^4.
# Hence derivative term <= C n^20 exp[-3(n^2-2)], C=60*256*4140*4^8.
# The ratio of adjacent bounds <=(6/5)^20 exp(-33)<1/2 for n>=5.
ratio=(I(F(6,5))**20)*exp_interval(I(-33))
if ratio.hi>=F(1,2): raise ArithmeticError('tail ratio')
C=60*256*4140*4**8
tail=2*C*5**20*exp_interval(I(-69))
if tail.hi>=F(1,1000): raise ArithmeticError('tail bound too wide')
answer=I(partial.lo-tail.hi,partial.hi+tail.hi)
if not answer.hi < -8951860: raise ArithmeticError('negative derivative proof failed')
if not answer.lo > -8951861: raise ArithmeticError('displayed interval failed')
report={
 'status':'PASS: exact rational intervals and analytic infinite-source derivative tail',
 'claim':'-8951861 < d^8/dt^8 [exp(2*pi*cosh(2*t))*Phi(t)] at t=0 < -8951860',
 'normalization':'Phi(t)=sum_n>=1 (4*pi^2*n^4*exp(9t/2)-6*pi*n^2*exp(5t/2))*exp(-pi*n^2*exp(2t))',
 'pi_lo':str(PI.lo),'pi_hi':str(PI.hi),
 'partial_terms':terms,'tail_upper_rational':str(tail.hi),
 'result_lo_rational':str(answer.lo),'result_hi_rational':str(answer.hi),
 'result_lo_float_for_display':float(answer.lo),'result_hi_float_for_display':float(answer.hi),
 'not_proved':['RH','any Xi zero-free improvement','any Bessel-sum hyperbolicity theorem']
}
print(json.dumps(report,indent=2))

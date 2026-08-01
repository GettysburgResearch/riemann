from __future__ import annotations
import json, hashlib, sys
sys.set_int_max_str_digits(0)
from dataclasses import dataclass
from fractions import Fraction

@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction
    def __post_init__(self):
        if self.lo > self.hi: raise ValueError('reversed interval')
    def __add__(self,o): return I(self.lo+o.lo,self.hi+o.hi)
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(p),max(p))
    def recip(self):
        if self.lo <= 0 <= self.hi: raise ZeroDivisionError('interval contains zero')
        p=(1/self.lo,1/self.hi); return I(min(p),max(p))
    def __truediv__(self,o): return self*o.recip()
    @property
    def mid(self): return (self.lo+self.hi)/2
    @property
    def rad(self): return (self.hi-self.lo)/2

def pt(x): return I(Fraction(x),Fraction(x))
def asI(x): return x if isinstance(x,I) else pt(x)
def ep(x): return Fraction(int(x['mantissa']))*Fraction(2)**int(x['exponent'])
def iv(x): return I(ep(x['lower']),ep(x['upper']))
def ep_json(q):
    if q==0:return {'mantissa':'0','exponent':0}
    d=q.denominator
    if d & (d-1): return {'numerator':str(q.numerator),'denominator':str(q.denominator)}
    return {'mantissa':str(q.numerator),'exponent':-(d.bit_length()-1)}
def iv_json(x): return {'lower':ep_json(x.lo),'upper':ep_json(x.hi)}
def mat_iv(x): return [[iv(v) for v in row] for row in x]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def qform(A,x,y=None):
    if y is None:y=x
    s=pt(0)
    for i in range(len(x)):
        for j in range(len(y)): s=s+asI(x[i])*A[i][j]*asI(y[j])
    return s
def upper_abs(x): return max(abs(x.lo),abs(x.hi))
def congruence(B,Y):
    n=len(B);m=len(Y[0]);out=[[pt(0)for _ in range(m)]for __ in range(m)]
    for i in range(m):
        for j in range(m):
            s=pt(0)
            for k in range(n):
                if Y[k][i]==0:continue
                for l in range(n):
                    if Y[l][j]==0:continue
                    s=s+pt(Y[k][i])*B[k][l]*pt(Y[l][j])
            out[i][j]=s
    return out
def gersh_lower(H):
    rows=[]
    for i in range(len(H)):
        rows.append(H[i][i].lo-sum((upper_abs(H[i][j]) for j in range(len(H)) if j!=i),Fraction(0)))
    return min(rows),rows
def canonical_sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def file_sha(path):
    h=hashlib.sha256();h.update(open(path,'rb').read());return h.hexdigest()
def frac(s): return Fraction(s)

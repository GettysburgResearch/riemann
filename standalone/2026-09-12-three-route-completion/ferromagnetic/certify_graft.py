"""Directed rational certificate for compensated one-edge derivatives.

Conditional on the explicitly cited ICR26 root-box theorem. This program
authenticates a new algebraic calculation on that WHOLE box; it does not
recompute the predecessor's theta integrals or prove target crossing.
"""
import argparse
from fractions import Fraction as F
from math import factorial, comb, isqrt
import json
import hashlib
from pathlib import Path

BITS=256
DEN=1 << BITS
SEED_SHA256='bf6895caf995e334bfe7b039a74a6f87ecc9961f7861f0c28edda7cd16f66d4f'

def validate_seed(data):
    required={'predecessor','source_path','q','multiplicities','centers','radius'}
    if set(data)!=required: raise ValueError('unexpected seed fields')
    if data['predecessor']!='0640c9c59be0bf20c18258460a7517fb09728e82': raise ValueError('wrong predecessor')
    if data['source_path']!='standalone/2026-09-12-astra-interacting-cluster-realization/parameters.json': raise ValueError('wrong predecessor path')
    payload={k:data[k] for k in ['q','multiplicities','centers','radius']}
    digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    if digest!=SEED_SHA256: raise ValueError('root box differs from cited predecessor')

def floorq(x): return x.numerator // x.denominator
def ceilq(x): return -((-x.numerator) // x.denominator)

class I:
    def __init__(self, lo, hi=None):
        self.lo=floorq(F(lo)*DEN)
        self.hi=ceilq(F(lo if hi is None else hi)*DEN)
    @classmethod
    def raw(cls,lo,hi):
        v=object.__new__(cls); v.lo=lo; v.hi=hi; return v
    @staticmethod
    def coerce(x): return x if isinstance(x,I) else I(x)
    def __add__(self,other):
        other=self.coerce(other); return I.raw(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I.raw(-self.hi,-self.lo)
    def __sub__(self,other): return self+-self.coerce(other)
    def __rsub__(self,other): return self.coerce(other)+-self
    def __mul__(self,other):
        other=self.coerce(other)
        p=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I.raw(min(p)//DEN,-((-max(p))//DEN))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=self.coerce(other)
        if other.lo<=0<=other.hi: raise ArithmeticError('zero denominator interval')
        endpoints=[F(DEN,other.lo),F(DEN,other.hi)]
        return self*I(min(endpoints),max(endpoints))
    def __pow__(self,n):
        if n<0: return I(1)/(self**(-n))
        ans=I(1)
        for _ in range(n): ans=ans*self
        return ans
    def sqrt(self):
        if self.lo<0: raise ArithmeticError('negative square-root interval')
        a=isqrt(self.lo*DEN); b=isqrt(self.hi*DEN)
        return I.raw(a,b+(b*b<self.hi*DEN))
    def bound(self): return [self.lo,self.hi]

def cumulants(m):
    k=[F(0)]*len(m)
    for n in range(1,len(m)):
        k[n]=m[n]-sum(F(comb(n-1,j-1))*k[j]*m[n-j] for j in range(1,n))
    return k

def sinh_quotient(q,n):
    """Coefficients of sinh(h)/(h*(cosh(h)+q)), in h squared."""
    a=[]
    for k in range(n):
        a.append((F(1,factorial(2*k+1))-sum(a[j]*F(1,factorial(2*(k-j))) for j in range(k)))/(1+q))
    return a

def polynomial_product(roots):
    p=[I(1)]
    for x in roots:
        a=[I(0)]*(len(p)+1)
        for j,v in enumerate(p): a[j]=a[j]-x*v; a[j+1]=a[j+1]+v
        p=a
    return p

def evaluate_box(data):
    centers=[F(x) for x in data['centers']]
    radius=F(data['radius'])
    xs=[I(x-radius,x+radius) for x in centers[:6]]
    y=I(centers[6]-radius,centers[6]+radius)
    q=F(*data['q'])
    c=cumulants([F(k%2==0) for k in range(17)])
    p=1/(1+q)
    d=cumulants([F(1)]+[p if k%2==0 else F(0) for k in range(1,17)])
    ar=[None]+[d[2*r]/c[2*r] for r in range(1,9)]
    P=polynomial_product(xs)
    ell=sum(P[k]*ar[k+1]*y**k for k in range(7))
    ell_t=sum(P[k]*ar[k+2]*y**(k+1) for k in range(7))
    z=ell_t/ell
    Q=[I(0)]*8
    for k,v in enumerate(P): Q[k]=Q[k]-8*z*v; Q[k+1]=Q[k+1]+8*v
    lam=[None]+[-Q[r-1]/r for r in range(1,8)]
    u=sinh_quotient(q,8)
    t=sinh_quotient(F(0),8)
    rows=[]
    for owner,x in enumerate(xs):
        delta=[None]+[F(factorial(2*r),1)/c[2*r]*sum(u[k]*t[r-1-k]*y**k*x**(r-1-k) for k in range(r)) for r in range(1,9)]
        slope=c[16]*(x*y).sqrt()*(delta[8]-sum(lam[r]*delta[r] for r in range(1,8)))
        rows.append({'owner_group':owner,'standardized_moment16_slope':slope.bound()})
    return {'schema':'ferromagnetic-graft-signs-v1','status':'conditional-component-not-RH',
            'bits':BITS,'predecessor':data['predecessor'],'root_box_radius':data['radius'],
            'component_polynomial_denominator':ell.bound(),'rows':rows,
            'target_crossing_proved':False,'all_order_realization_proved':False,'rh_proved':False}

def validate(result):
    # Exact simple rational brackets, chosen well wider than computed endpoints.
    brackets=[(-28,-27,10000),(17,18,100),(-12,-11,1000),(71,72,100),(25,26,100),(78,82,1000)]
    if result['component_polynomial_denominator'][0]<=0<=result['component_polynomial_denominator'][1]:
        raise ArithmeticError('singular lower-moment Jacobian not excluded')
    for row,(lo,hi,den) in zip(result['rows'],brackets):
        a,b=row['standardized_moment16_slope']
        if not F(lo,den)<F(a,DEN)<=F(b,DEN)<F(hi,den):
            raise ArithmeticError('whole-box slope enclosure missed its bracket')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--emit',action='store_true')
    args=parser.parse_args()
    folder=Path(__file__).resolve().parent
    data=json.loads((folder/'seed-box.json').read_text())
    validate_seed(data)
    result=evaluate_box(data); validate(result)
    target=folder/'graft-certificate.json'
    if args.emit: target.write_text(json.dumps(result,indent=2)+'\n')
    else:
        if json.loads(target.read_text())!=result: raise ArithmeticError('certificate differs from full reconstruction')
    print('PASS conditional whole-box compensated graft signs; target crossing and RH remain open')
    for row in result['rows']:
        a,b=row['standardized_moment16_slope']
        print(row['owner_group'],float(F(a,DEN)),float(F(b,DEN)))

if __name__=='__main__': main()

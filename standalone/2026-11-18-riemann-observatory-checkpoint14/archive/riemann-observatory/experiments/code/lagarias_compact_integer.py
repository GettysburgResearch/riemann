#!/usr/bin/env python3
"""Standard-library-only rigorous integer interval replay of Lagarias cells.
No float, Decimal, mpmath, FLINT or external package is used. Endpoints are
integers divided by 2**BITS. Every arithmetic operation rounds outward.
Proof of log/exp remainder bounds is in the compact campaign document.
"""
import argparse,json,math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
BITS=192;S=1<<BITS;LOG_TERMS=128;EXP_TERMS=80

def ceildiv(a,b):
 assert b>0
 return -((-a)//b)

class I:
 __slots__=('lo','hi')
 def __init__(self,lo,hi=None,raw=False):
  if raw:self.lo,self.hi=lo,hi
  else:
   q=Fraction(lo);self.lo=(q.numerator*S)//q.denominator
   self.hi=ceildiv(q.numerator*S,q.denominator)
  assert self.lo<=self.hi
 def __add__(self,o):
  o=asI(o);return I(self.lo+o.lo,self.hi+o.hi,raw=True)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo,raw=True)
 def __sub__(self,o):return self+-asI(o)
 def __rsub__(self,o):return asI(o)+-self
 def __mul__(self,o):
  o=asI(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
  return I(min(v)//S,ceildiv(max(v),S),raw=True)
 __rmul__=__mul__
 def reciprocal(self):
  assert self.lo>0 or self.hi<0,'division interval contains zero'
  # Reciprocal is decreasing on either component of R minus zero.
  # Python // already rounds toward minus infinity, even for negative divisors.
  lower=(S*S)//self.hi
  upper=-((-S*S)//self.lo)
  return I(lower,upper,raw=True)
 def __truediv__(self,o):return self*asI(o).reciprocal()
 def __rtruediv__(self,o):return asI(o)*self.reciprocal()
 def __pow__(self,n):
  assert isinstance(n,int)and n>=0
  result=I(1);x=self
  while n:
   if n&1:result=result*x
   n//=2
   if n:x=x*x
  return result
 def log(self):
  assert self.lo>0
  a=log_point(self.lo);b=log_point(self.hi)
  return I(a.lo,b.hi,raw=True)
 def exp(self):
  a=exp_point(self.lo);b=exp_point(self.hi)
  return I(a.lo,b.hi,raw=True)

def asI(x):return x if isinstance(x,I)else I(x)
def log_small(y):
 # Actual y lies in [1,2], and the outward arithmetic also verifies r<=1/2.
 r=(y-1)/(y+1)
 assert r.lo>=0 and 2*r.hi<=S
 r2=r*r;term=r;total=I(0)
 for j in range(LOG_TERMS):
  total+=term/(2*j+1);term=term*r2
 # 0<=remainder<=3*2^(-2M), from atanh geometric tail for 0<=r<=1/2.
 tail=ceildiv(3*S,1<<(2*LOG_TERMS))
 return 2*total+I(0,tail,raw=True)

@lru_cache(None)
def log_two():return log_small(I(2))
@lru_cache(None)
def log_point(z):
 assert z>0
 k=z.bit_length()-1-BITS
 # z/S=2**k * y with exact 1<=y<2; enclose y with outward dyadic rounding.
 if k>=0:y=I(Fraction(z,S*(1<<k)))
 else:y=I(Fraction(z*(1<<(-k)),S))
 assert y.lo>=S and y.hi<=2*S
 return log_small(y)+k*log_two()

@lru_cache(None)
def exp_point(z):
 if z==0:return I(1)
 if z<0:return exp_point(-z).reciprocal()
 k=max(0,z.bit_length()-BITS)
 y=I(Fraction(z,S*(1<<k)))
 assert y.lo>=0 and y.hi<=S
 term=I(1);total=I(1)
 for j in range(1,EXP_TERMS+1):
  term=term*y/j;total+=term
 # Lagrange remainder <=e*y**(M+1)/(M+1)! <3/(M+1)! for 0<=y<=1.
 tail=ceildiv(3*S,math.factorial(EXP_TERMS+1))
 total+=I(0,tail,raw=True)
 for _ in range(k):total=total*total
 return total

@lru_cache(None)
def H_at(q,terms):
 x=I(q);total=I(0)
 for k in range(1,terms+1):total+=x/(k*(x+k))
 lower=total+(1+x/(terms+1)).log()
 upper=total+(1+x/terms).log()
 return lower,upper

def calculate(a,b,terms):
 x=I(I(a).lo,I(b).hi,raw=True)
 ha,_=H_at(a,terms);_,hb=H_at(b,terms)
 h=I(ha.lo,hb.hi,raw=True)
 ell=h.log();eh=h.exp()
 B=h+eh*ell
 Bp=1+eh*(ell+1/h)
 N=-(eh**2)*(ell+1)/(h**2)+eh*((h-2)*ell+2-3/h)-1
 P=N*(x/(x+1))**2+Bp*B/(2*x)
 assert B.lo>0 and Bp.lo>0 and N.hi<0 and P.hi<0,('failed cell',str(a),str(b))
 return {'a':str(a),'b':str(b),'B_lower':str(Fraction(B.lo,S)),
         'Bprime_lower':str(Fraction(Bp.lo,S)),
         'fsecond_numerator_upper':str(Fraction(N.hi,S)),
         'curvature_numerator_upper':str(Fraction(P.hi,S))}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cells',type=Path)
 ap.add_argument('--bits',type=int,default=192)
 args=ap.parse_args()
 global BITS,S
 BITS=args.bits;assert BITS>=64;S=1<<BITS
 root=Path(__file__).resolve().parents[2]
 source=args.cells or(root/'experiments/results/lagarias_compact_arb.json')
 data=json.loads(source.read_text());terms=data.get('harmonic_terms',32)
 left,right=map(Fraction,data['domain']);previous=left;rows=[]
 for c in data['cells']:
  a,b=Fraction(c['a']),Fraction(c['b']);assert a==previous and b>a
  rows.append(calculate(a,b,terms));previous=b
 assert previous==right
 result={'status':'validated standard-library integer interval proof replay',
         'domain':[str(left),str(right)],'certified_cells':len(rows),'precision_bits':BITS,
         'harmonic_terms':terms,'log_series_terms':LOG_TERMS,'exp_series_terms':EXP_TERMS,
         'external_packages':[],'acceptance':'all B and Bprime lower bounds positive; all N and P upper bounds strictly negative',
         'cells':rows}
 p=root/'experiments/results/lagarias_compact_integer.json'
 p.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items()if k!='cells'},indent=2))
if __name__=='__main__':main()

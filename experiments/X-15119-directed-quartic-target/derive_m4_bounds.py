#!/usr/bin/env python3
"""Directed symbolic fourth-derivative envelopes for the theta moments."""
from fractions import Fraction
from decimal import Decimal, localcontext, getcontext, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
import json
PREC=80; getcontext().prec=PREC

def atan_bounds(q,K):
 s=Fraction(0)
 for k in range(K+1):
  t=Fraction(1,(2*k+1)*q**(2*k+1)); s=s+t if k%2==0 else s-t
 nxt=Fraction(1,(2*K+3)*q**(2*K+3)); nxt=-nxt if (K+1)%2 else nxt
 return min(s,s+nxt),max(s,s+nxt)
a5=atan_bounds(5,110); a239=atan_bounds(239,30)
pilo=16*a5[0]-4*a239[1]; pihi=16*a5[1]-4*a239[0]
def decfrac(f,rounding):
 with localcontext() as c: c.prec=PREC;c.rounding=rounding;return Decimal(f.numerator)/Decimal(f.denominator)
PI_LO=decfrac(pilo,ROUND_FLOOR);PI_HI=decfrac(pihi,ROUND_CEILING)
def exp_upper(x):
 with localcontext() as c: c.prec=PREC+20;c.rounding=ROUND_HALF_EVEN;y=x.exp()
 with localcontext() as c: c.prec=PREC;c.rounding=ROUND_CEILING;y=+y;return y.next_plus(c)
def D(fr): return decfrac(fr,ROUND_CEILING)

def poly4(k,a):
 # d^4[u^k exp(a u-z)] = P(u,z) exp(a u-z), z=pi n^2 exp(2u)
 P={(k,0):Fraction(1)}
 for _ in range(4):
  Q={}
  def add(key,v): Q[key]=Q.get(key,Fraction(0))+v
  for (pu,pz),c in P.items():
   if pu: add((pu-1,pz),c*pu)
   if pz: add((pu,pz),c*2*pz)
   add((pu,pz),c*a)
   add((pu,pz+1),-2*c)
  P={key:v for key,v in Q.items() if v}
 return P

def zmexp_upper(n,m):
 # sup_{z>=pi*n^2} z^m exp(-z)
 b_lo=PI_LO*Decimal(n*n); b_hi=PI_HI*Decimal(n*n)
 if m==0: return exp_upper(-b_lo)
 if b_lo>=Decimal(m): return (b_hi**m)*exp_upper(-b_lo)
 return (Decimal(m)**m)*exp_upper(-Decimal(m))

def component_bound(k,a,outer_kind):
 P=poly4(k,a); U=Decimal(2); ea=exp_upper(D(a)*U); total=Decimal(0)
 for n in range(1,22):
  pref=(Decimal(2)*(PI_HI**2)*Decimal(n**4) if outer_kind=='pos'
        else Decimal(3)*PI_HI*Decimal(n*n))
  sn=sum(D(abs(c))*(U**pu)*zmexp_upper(n,pz) for (pu,pz),c in P.items())
  total += pref*ea*sn
 n=22
 for (pu,pz),coef in P.items():
  degree=(4 if outer_kind=='pos' else 2)+2*pz
  const=(Decimal(2)*(PI_HI**2) if outer_kind=='pos' else Decimal(3)*PI_HI)
  const*=D(abs(coef))*(U**pu)*ea*(PI_HI**pz)
  first=const*(Decimal(n)**degree)*exp_upper(-Decimal(3*n*n))
  total += first/(Decimal(1)-Decimal('1e-50'))
 return total
out={}
for k in (0,2,4):
 bp=component_bound(k,Fraction(9,2),'pos'); bn=component_bound(k,Fraction(5,2),'neg')
 out[str(k)]={'positive':str(bp),'negative':str(bn),'total':str(bp+bn)}
print(json.dumps(out,indent=2))

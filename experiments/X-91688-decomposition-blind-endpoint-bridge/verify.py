#!/usr/bin/env python3
from fractions import Fraction
import hashlib,json
from pathlib import Path

def add(a,b):return tuple(a[i]+b[i] for i in range(len(a)))
def scale(c,a):return tuple(c*x for x in a)
def gamma(a,q):return sum(Fraction((i+1)*q+1,(i+2)*q+3)*x for i,x in enumerate(a))
def quant(a):return tuple(a[i]+(a[i-1] if i else 0) for i in range(len(a)))
def main():
 colors=[(Fraction(1,3),Fraction(2,5),Fraction(3,7),Fraction(5,11)),
         (Fraction(2,7),Fraction(1,4),Fraction(4,9),Fraction(7,13)),
         (Fraction(5,17),Fraction(3,8),Fraction(2,11),Fraction(1,5))]
 total=(Fraction(0),)*4
 for a in colors:total=add(total,a)
 checks=0
 assert quant(total)==tuple(sum(quant(a)[i] for a in colors) for i in range(4));checks+=1
 for q in (2,3,5,11):
  assert gamma(total,q)==sum(gamma(a,q) for a in colors);checks+=1
  xi=gamma(total,q)-2*gamma(total,4*q)
  xis=sum(gamma(a,q)-2*gamma(a,4*q) for a in colors)
  assert xi==xis;checks+=1
 sig=Fraction(17,19)
 cut=lambda a:(a[0],a[1],a[2],Fraction(0))
 assert scale(sig,cut(total))==tuple(sum(scale(sig,cut(a))[i] for a in colors) for i in range(4));checks+=1
 payload={'classification':'PASS_DECOMPOSITION_BLIND_ENDPOINT_BRIDGE','exact_linear_checks':checks,
 'scope':'Exact rational regression of common-parent sum, ordinary maps, q/4q detail, one global quantizer, restriction and safety scaling. It does not certify the analytic endpoint density or RH.'}
 payload['proof_object_sha256']=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 p=Path(__file__).resolve().parent/'results'/'verification.json';p.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(payload['classification']);print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Independent ordinary high-precision cumulative-moment replay for X-17804.

This is an algebraically independent midpoint check, not a directed certificate.
"""
from __future__ import annotations
import argparse, json, math, time
from fractions import Fraction
from math import comb
from pathlib import Path
import mpmath as mp

X=Fraction(17730793345827,2**40)
R=[Fraction(n,2**96) for n in (
35218599699163919097920611990,23680158309013251518610419821,
19903564882942428266376244912,16361783185744983922054900136,
15114750136364744335442418335)]

def sieve(n:int)->list[int]:
 s=bytearray(b'\x01')*(n+1);s[0:2]=b'\x00\x00'
 for p in range(2,math.isqrt(n)+1):
  if s[p]:s[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
 return [i for i in range(2,n+1) if s[i]]

def events(limit:int):
 out=[]
 for p in sieve(limit):
  v=p
  while v<=limit:
   out.append((v,p))
   if v>limit//p:break
   v*=p
 return sorted(out)

def queries():
 q={}
 for mask in range(32):
  shift=sum((R[j] for j in range(5) if mask>>j&1),Fraction())
  sign=-1 if mask.bit_count()&1 else 1
  for pole,base in ((0,1),(1,-2)):
   for k in range(25):
    key=(pole,Fraction(2)+shift+Fraction(k,12))
    q[key]=q.get(key,Fraction())+Fraction(sign*base*(-1 if k&1 else 1)*comb(24,k),32)
 return q

def run(dps:int):
 mp.mp.dps=dps; start=time.time(); h=mp.log(4)
 norm=mp.mpf(12)**24/mp.factorial(23)
 rows=[]
 for (pole,off),c in queries().items():
  y=mp.mpf(X.numerator)/X.denominator-mp.mpf(off.numerator)/off.denominator-(h if pole else 0)
  rows.append((y,norm*mp.mpf(c.numerator)/c.denominator))
 rows.sort(key=lambda z:z[0]); ev=events(1364177)
 S=[mp.mpf(0)]*24; idx=0; total=mp.mpf(0); absolute=mp.mpf(0)
 for y,c in rows:
  while idx<len(ev):
   n,p=ev[idx]; ln=mp.log(n)
   if ln>y:break
   w=mp.log(p)/mp.sqrt(n); power=mp.mpf(1)
   for m in range(24):S[m]+=w*power;power*=ln
   idx+=1
  value=S[0]
  for m in range(1,24):value=value*y+(-1 if m&1 else 1)*comb(23,m)*S[m]
  term=c*value;total+=term;absolute+=abs(term)
 return {"classification":"ORDINARY_HIGH_PRECISION_INDEPENDENT_REPLAY","dps":dps,
  "value":mp.nstr(total,dps-5),"query_count":len(rows),"event_count":len(ev),
  "global_expansion_condition":mp.nstr(absolute/abs(total),30),"runtime_seconds":time.time()-start}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--dps',type=int,default=170);ap.add_argument('--output',type=Path)
 a=ap.parse_args();r=run(a.dps);text=json.dumps(r,indent=2,sort_keys=True)+'\n'
 if a.output:a.output.write_text(text)
 print(text,end='')
if __name__=='__main__':main()

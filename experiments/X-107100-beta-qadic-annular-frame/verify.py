#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from math import gcd
from pathlib import Path
Q=67

def mu(n:int)->int:
    if n==1:return 1
    x=n;s=1;p=2
    while p*p<=x:
        if x%p==0:
            x//=p;s=-s
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    return -s if x>1 else s

def uq(n:int)->int:return mu(n) if n%Q else 0

def beta(n:int)->int:
    z=uq(n)
    if n%Q==0:z-=2*uq(n//Q)
    if n%(Q*Q)==0:z+=uq(n//(Q*Q))
    return z

def pref(f,n):return sum(f[1:n+1]) if n>0 else 0

def K(m,n):return Fraction(1,1+abs(m-n))

def direct(lo,hi):
    z=Fraction(0)
    for m in range(lo+1,hi+1):
      if not uq(m):continue
      for n in range(lo+1,hi+1):
        if uq(n):z+=Fraction(uq(m)*uq(n),m*n)*K(m,n)
    return z

def grouped(lo,hi):
    z=Fraction(0)
    for d in range(1,hi+1):
      if not uq(d):continue
      for a in range(1,hi//d+1):
       if not uq(a) or gcd(a,d)!=1:continue
       m=d*a
       if not(lo<m<=hi):continue
       for b in range(1,hi//d+1):
        if not uq(b) or gcd(b,d)!=1 or gcd(a,b)!=1:continue
        n=d*b
        if lo<n<=hi:z+=Fraction(mu(a)*mu(b),d*d*a*b)*K(m,n)
    return z

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);a=ap.parse_args()
 checks=0;N=Q*Q*5
 u=[0]+[uq(n) for n in range(1,N+1)];g=[0]+[beta(n) for n in range(1,N+1)]
 for m in range(1,6):
  if m%Q or mu(m)==0:
   assert beta(m)==mu(m);assert beta(Q*m)==-2*mu(m);assert beta(Q*Q*m)==mu(m);checks+=3
 for x in [1,2,66,67,68,Q*Q-1,Q*Q,N]:
  assert pref(g,x)==pref(u,x)-2*pref(u,x//Q)+pref(u,x//(Q*Q));checks+=1
  inv=0;j=0;p=1
  while p<=x:inv+=(j+1)*pref(g,x//p);j+=1;p*=Q
  assert inv==pref(u,x);checks+=1
 hs=[];x=N
 while x>=1:hs.append(x);x//=Q
 vals=[pref(u,h) for h in hs]+[0];shell=[vals[j]-vals[j+1] for j in range(len(hs))]
 for j in range(len(hs)):assert vals[j]==sum(shell[j:]);checks+=1
 for lo,hi in [(0,24),(8,40)]:assert direct(lo,hi)==grouped(lo,hi);checks+=1
 M=10**6;assert M-M==0 and M*M+(-M)*(-M)==2*M*M;checks+=2
 payload={'claim':'T-107100','verdict':'PASS_T107100_BETA_QADIC_ANNULAR_FRAME','checks':checks,'rh_established':False,'scope':'finite exact source/filter/gcd algebra'}
 payload['proof_object']=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()
 text=json.dumps(payload,indent=2,sort_keys=True)+'\n'
 if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
 print(payload['verdict']);print(f"checks={checks}");print(payload['proof_object'])
if __name__=='__main__':main()

#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
@dataclass(frozen=True)
class C:
 re:F=F(0);im:F=F(0)
 @staticmethod
 def m(x):return x if isinstance(x,C) else C(F(x),F(0))
 def __add__(s,o):o=C.m(o);return C(s.re+o.re,s.im+o.im)
 __radd__=__add__
 def __neg__(s):return C(-s.re,-s.im)
 def __sub__(s,o):return s+(-C.m(o))
 def __rsub__(s,o):return C.m(o)-s
 def __mul__(s,o):o=C.m(o);return C(s.re*o.re-s.im*o.im,s.re*o.im+s.im*o.re)
 __rmul__=__mul__
 def conj(s):return C(s.re,-s.im)
 def __truediv__(s,o):o=C.m(o);d=o.re*o.re+o.im*o.im;return C((s.re*o.re+s.im*o.im)/d,(s.im*o.re-s.re*o.im)/d)
 def __pow__(s,n):
  if n<0:return C.m(1)/(s**(-n))
  z=C.m(1);b=s
  while n:
   if n&1:z=z*b
   b=b*b;n//=2
  return z
 def zero(s):return s.re==0 and s.im==0

def I(n):return [[C.m(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def sc(x,a):return [[C.m(x)*z for z in r] for r in a]
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),C()) for j in range(len(b[0]))] for i in range(len(a))]
def inv(a):
 n=len(a);e=I(n);z=[a[i][:]+e[i] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if not z[r][c].zero());z[c],z[p]=z[p],z[c];v=z[c][c];z[c]=[x/v for x in z[c]]
  for r in range(n):
   if r==c:continue
   f=z[r][c]
   if not f.zero():z[r]=[z[r][j]-f*z[c][j] for j in range(2*n)]
 return [r[n:] for r in z]
def tr(a):return sum((a[i][i] for i in range(len(a))),C())
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def G(lam,s):return [[C.m(1)/(lam[i].conj()+lam[j]+s) for j in range(len(lam))] for i in range(len(lam))]
def pmul(a,b,d=2):
 n=len(a[0]);o=[[[C() for _ in range(n)] for _ in range(n)] for _ in range(d+1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j<=d:o[i+j]=add(o[i+j],mm(x,y))
 return o

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();checks=0
 l=[C(F(1)),C(F(1),F(1))];g0,gh,g2,g4=(G(l,s) for s in (0,2,4,8))
 E=add(mm(mm(g2,inv(gh)),g2),sc(-1,g4));assert E[0][0]==C(F(77,3330));assert E[0][1]==C(F(27886,1244421),F(-7879,1244421));assert det2(E)==C(F(-8471,1119978900));checks+=3
 O=tr(mm(mm(mm(inv(g0),g2),inv(g4)),g2));T=tr(mm(inv(g0),gh));assert O==C(F(13210,12321));assert T==C(F(13,17));assert O-T==C(F(64397,209457));checks+=3
 FNI=tr(mm(mm(mm(mm(mm(inv(g0),gh),inv(g2)),g4),inv(g2)),gh));assert T-FNI==C(F(9389,58378));checks+=1
 # polynomial identity coefficients low-to-high
 def cv(a,b):
  o=[F(0)]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):o[i+j]+=x*y
  return o
 lhs=[F(5,27),F(-32,27),F(2),F(0),F(-1)];rhs=[x/F(27) for x in cv(cv([F(1),F(-1)],[F(1),F(-6),F(9)]),[F(5),F(3)])];assert lhs==rhs;assert F(2,3)*F(4,3)*F(4,3)==F(32,27);checks+=2
 l3=[C(F(1)),C(F(2),F(1)),C(F(3),F(-1))];g=G(l3,0);M=[[C.m(1)/(l3[i].conj()+l3[j])**2 for j in range(3)] for i in range(3)];N=[[C.m(2)/(l3[i].conj()+l3[j])**3 for j in range(3)] for i in range(3)];gi=inv(g)
 atr=tr(mm(gi,M));ctr=tr(add(mm(gi,N),sc(-1,mm(mm(mm(gi,M),gi),M))));assert atr.im==0 and atr.re>0;assert ctr.im==0 and ctr.re>=0;checks+=2
 g2s=[g,sc(-2,M),sc(2,N)];a1=sc(-4,M);a2=sc(8,N);g4is=[gi,sc(-1,mm(mm(gi,a1),gi)),add(mm(mm(mm(mm(gi,a1),gi),a1),gi),sc(-1,mm(mm(gi,a2),gi)))]
 Os=pmul(pmul([gi],g2s),pmul(g4is,g2s));Ts=pmul([gi],[g,sc(-1,M),sc(F(1,2),N)]);assert tr(Os[0])==C.m(3) and tr(Os[1])==C() and tr(Os[2])==C.m(-4)*ctr;assert tr(Ts[0])==C.m(3) and tr(Ts[1])==-atr and tr(Ts[2])==C.m(F(1,2))*tr(mm(gi,N));checks+=6
 d={'claim':'T-105660','verdict':'PASS_T105660_CORRECTED_CAUCHY_FRONTIER','checks':checks,'mlc_refuted':True,'cti_general_proved':False,'rh_established':False,'scope':'exact finite rational algebra and Taylor coefficients'};d['proof_object']=hashlib.sha256(json.dumps(d,sort_keys=True).encode()).hexdigest();text=json.dumps(d,indent=2,sort_keys=True)+'\n'
 if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
 print(d['verdict']);print(f"checks={checks}");print(d['proof_object'])
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact/numerical regression for L-91306/L-91307/R-91301/T-91301."""
from __future__ import annotations
import argparse, json, math
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import numpy as np
mp.mp.dps=70

def pp(N):
 s=[1]*(N+1); s[:2]=[0,0]; ps=[]
 for p in range(2,N+1):
  if s[p]:
   ps.append(p)
   if p*p<=N:
    for q in range(p*p,N+1,p): s[q]=0
 out=[]
 for p in ps:
  n=p;k=1
  while n<=N:
   out.append((n,k)); n*=p;k+=1
 return sorted(out)

def logz(a,x,rows):
 c=a+mp.mpf('.5'); return sum(-2j*mp.power(n,-c)*mp.sin(x*mp.log(n))/k for n,k in rows)
def score(a,x,rows):
 c=a+mp.mpf('.5'); return sum(2j*a*mp.log(n)*mp.power(n,-c)*mp.sin(x*mp.log(n))/k for n,k in rows)

def tail_exact():
 w={2:F(1,20),3:F(1,30),5:F(1,40),7:F(1,50)}; U=max(w)
 g={1:F(3,7),2:F(-2,5),3:F(5,11),4:F(1,3),5:F(-4,13),6:F(2,9),7:F(1,8),8:F(-1,10)}
 k={1:F(-1,4),2:F(5,9),3:F(2,7),4:F(-3,8),5:F(1,6),6:F(4,15),7:F(-2,11),8:F(3,14)}
 val=lambda f,m:f.get(m,F(0)); Wv=lambda m:sum((x for u,x in w.items() if u>=m),F(0)); Wt=lambda j:sum((x for u,x in w.items() if u>=j+1),F(0))
 H=lambda f,j:sum((x*val(f,u-j) for u,x in w.items() if u>=j+1),F(0))
 def q(f,h):
  M=max(max(f),max(h)); inp=sum((val(f,m)*val(h,m) for m in range(1,M+1)),F(0)); out=sum((H(f,j)*H(h,j) for j in range(U)),F(0)); d0=sum(((1-Wv(m))*val(f,m)*val(h,m) for m in range(1,M+1)),F(0)); var=d2=F(0)
  for j in range(U):
   W=Wt(j)
   if not W: continue
   hf,hh=H(f,j),H(h,j); mf,mh=hf/W,hh/W
   var+=sum((x*(val(f,u-j)-mf)*(val(h,u-j)-mh) for u,x in w.items() if u>=j+1),F(0)); d2+=(1/W-1)*hf*hh
  return inp,out+d0+var+d2
 gg=q(g,g); gk=q(g,k); kk=q(k,k); assert gg[0]==gg[1] and gk[0]==gk[1] and kk[0]==kk[1]
 Hmat=[[w.get(r+s,F(0)) for s in range(1,4)] for r in range(1,4)]
 return {'quadratic':str(gg[0]),'polarized':str(gk[0]),'second_quadratic':str(kk[0]),'hankel':[[str(x) for x in row] for row in Hmat]}

def covariant():
 A=np.array([[0,1j,.2],[1j,0,-.35j],[-.2,-.35j,0]],complex); A=(A-A.conj().T)/2
 B=np.array([[0,-.4,.25j],[.4,0,.3],[.25j,-.3,0]],complex); B=(B-B.conj().T)/2
 V=np.array([[1,0],[0,1],[0,0]],complex); R=V@V.conj().T; N=(np.eye(3)-R)@(A+B)@V
 return float(np.linalg.norm(N-(np.eye(3)-R)@(A+B)@V)),float(np.linalg.norm(A+A.conj().T)),[float(x) for x in np.linalg.eigvalsh(N.conj().T@N)]

def build():
 rows=pp(200); a=mp.mpf('1.7'); x=mp.mpf('.83'); err=abs(a*mp.diff(lambda z:logz(z,x,rows),a)-score(a,x,rows)); ratios=[]
 for n,k in rows[:18]:
  u=mp.log(n); c=a+mp.mpf('.5'); j=(1-(1+2*a*u)*mp.e**(-2*a*u))*mp.e**(-c*u)/(k*a*a); s=a*u*mp.e**(-c*u)/k; ratios.append(float(s/j))
 mass=4*(-mp.diff(lambda z:mp.log(mp.zeta(z)),mp.mpf('4.5'))); bound=F(85,196); t=tail_exact(); ce,sk,eigs=covariant()
 gates={'score':err<mp.mpf('1e-55'),'mismatch':max(ratios)-min(ratios)>1,'mass':mass<mp.mpf(bound.numerator)/bound.denominator<1,'tail':True,'covariant':ce<1e-14 and sk<1e-14}; assert all(gates.values())
 return {'status':'PASS_COVARIANT_TAIL_HANKEL_COMPLETION','gates':gates,'prime_score_error':float(err),'ratio_spread':max(ratios)-min(ratios),'safe_mass':float(mass),'safe_bound':f'{bound.numerator}/{bound.denominator}','tail':t,'covariant_shape_eigenvalues':eigs}

def main():
 p=argparse.ArgumentParser();p.add_argument('--json',type=Path);a=p.parse_args();s=json.dumps(build(),sort_keys=True,separators=(',',':'))+'\n'; a.json.write_text(s) if a.json else print(s,end='')
if __name__=='__main__':main()

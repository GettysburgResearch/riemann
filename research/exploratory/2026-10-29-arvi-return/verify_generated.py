"""Pinned PR94 row-certificate tool. Pass a prepared tracker checkout path.
This script modifies generated rows when regenerating; use an isolated checkout.
"""
import sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
import sympy as s
import re

D,P=s.symbols('D P'); R=s.Rational
B=R(96232839,10**8); L=R(3853,2000); cap=R(9999,100000); PB=R(49283557,50000000); PL=R(4503,2000); PC=R(31,500)
theta=R(8738702,10**7);h=R(8056,10000); c=1-theta; ell=4*c-R(1,3); x=1+ell-h;y=h-2*ell;k=1-2*c;dm=R(19,25);dp=h+R(1,10**10); eps=R(1,10**7);sm=R(3,100);mm=R(377,1000);nat=(1-R(9,2)*sm)/2
edges=[(R(1,200), min(R(1,200),2*y-R(1,200))/(6*k)), (dm,min(dm,2*y-dm)/(6*k)), (dm,min(R(619,10000)*dm,(2*y-(2-PB)*dm)/PL)),(dp,min(R(619,10000)*dp,(2*y-(2-PB)*dp)/PL))]
raw=(root/'submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/Return/Windows.lean').read_text()
windows=[(n,R(a),R(b),R(c)) for n,a,b,c in re.findall(r'branch := \.(\w+)\s+nonold := by decide\s+deltaLo := \(([^:]+):ℝ\)\s+deltaHi := \(([^:]+):ℝ\)\s+pLo := \(([^:]+):ℝ\)',raw)]
assert len(windows)==31
branches=[('old',0,1,R(1,25)),('C',B,L,cap),('capC',B,L,cap),('weakC7',B-R(7,4000),L,cap),('capP',PB,PL,PC)]

def coeff(e):
 p=s.Poly(e,D,P); return [(int(a),int(b),q) for (a,b),q in p.terms()]
def calc(cs,d,p):
 # Bernstein convex hull on [a,b] x [c,d] via exact rational arithmetic.
 a,b=d; c,e=p; wd=b-a; wp=e-c
 max_i=max(i for i,j,q in cs); max_j=max(j for i,j,q in cs)
 temp={}
 for k in range(max_i+1):
  for l in range(max_j+1):
   temp[k,l]=sum((q*int(s.binomial(i,k))*a**(i-k)*wd**k*int(s.binomial(j,l))*c**(j-l)*wp**l for i,j,q in cs if i>=k and j>=l),R(0))
 values=[]
 for i in range(max_i+1):
  for j in range(max_j+1):
   q=sum((temp[k,l]*int(s.binomial(i,k))/int(s.binomial(max_i,k))*int(s.binomial(j,l))/int(s.binomial(max_j,l)) for k in range(i+1) for l in range(j+1)),R(0))
   values.append(q)
 return min(values)

allchecks=[]
for idx,(dist,C) in enumerate(edges):
 checks=[]
 for name,b,l,capb in branches:
  V=R(5,6)-D
  if name=='old':
   dd=3-P-2*P/(3*k);aa=2*(1-P)*(1-P/(3*k)); J=V*dd+D*aa; N=(1-D)*J+D*aa*V/2;guards=[J]
  else:
   ic=name in ('capC','capP');z=capb-eps;dd=3-P if ic else 3-P-4*P/l;aa=2 if ic else 2-4*P/l;c0=1-2*P*z if ic else 1-2*P*b/l;zz=2*P*z if ic else 2*P*b/l;U=(1-P)*c0;J=V*dd+D*(1-P)*aa;T=J+D*U;rn=aa*T+(zz-P)*J;mn=dd*T-rn;dj=dd*J
   low=mm+eps if ic else max(mm+eps,(b-l*(capb-eps))/2+eps);high=min(R(11,25)-eps,nat-eps, (b-l*(z if ic else sm+eps))/2-eps); derd=-1 if ic else -1-4/l;dera=0 if ic else -4/l;derc=-2*z if ic else -2*b/l;deru=-c0+(1-P)*derc;derj=V*derd+D*(-aa+(1-P)*dera);N=(1-D)*J+V*D*U
   guards=[dd,aa,c0,J,T-J,R(12499,10000)*J-T,rn-R(23,37)*dj,dj-rn,mn-low*dj,high*dj-mn,N-(1-2*D*nat-2*D*P*sm)*J,U*derj-deru*J,R(11,25)-nat-eps,b-2*nat-l*(sm+eps)-2*eps,(z-sm-eps)*dj if ic else 1]
  base=R(1,2)+R(13,75)*h-y/2-ell/2-R(9,100)*dist+D/2+D*P*(ell-C/2)
  margin=(theta-R(1,10**8)-base)*J-R(3,4)*dist*N
  checks.append((name,[coeff(e) for e in guards],coeff(margin)))
 allchecks.append(checks)

import glob,re
seen=set()
for path in glob.glob(str(root/'submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/Return/Rows/Edge_*.lean')):
 t=open(path).read();pattern=r'def (row\d+)_coefficients : Fin (\d+) → Fin (\d+) → ℝ := (.*?)\ntheorem \1_identity .*?rowMargin \.(\w+) \.(\w+) δ p =\s*Record12518109.Bernstein.bsum (\d+) (\d+) \(([^:]+):ℝ\) (\w+) \(([^:]+):ℝ\) \(([^:]+):ℝ\) \(([^:]+):ℝ\) \(([^:]+):ℝ\)'
 for name,ni,nj,txt,edge,branch,degx,degy,mm,coeffname,aa,bb,cc,dd in re.findall(pattern,t,re.S):
  assert name not in seen
  seen.add(name)
  assert int(ni)==int(degx)+1 and int(nj)==int(degy)+1 and coeffname == name+'_coefficients',name
  a,b,c,d,m=map(R,(aa,bb,cc,dd,mm)); ni=int(ni);nj=int(nj);co=[R(i) for i in re.findall(r'\(([^:]+):ℝ\)',txt)];assert len(co)==ni*nj
  z=m+sum(co[i*nj+j]*(D-a)**i*(b-D)**(ni-1-i)*(P-c)**j*(d-P)**(nj-1-j) for i in range(ni) for j in range(nj))
  ii=['oldSmall','oldSwitch','newSwitch','newTop'].index(edge);q=dict((name,g) for name,guards,g in allchecks[ii])[branch];original=sum(qc*D**i*P**j for i,j,qc in q)
  assert s.Poly(z-original,D,P).is_zero,name
  assert m>0 and min(co)>=0
assert seen == {f'row{i:03}' for i in range(1,48)}, seen
print('all 47 independent polynomial identity and dimension checks pass')

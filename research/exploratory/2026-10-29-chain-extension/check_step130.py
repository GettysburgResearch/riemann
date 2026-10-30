"""Exact rational Bernstein validation of the listed scalar gates, not a Lean build."""
import sympy as s
from itertools import product
from collections import deque
from math import comb
from pathlib import Path
import hashlib
base=Path("/workspace/scratch/pr94-prepared/submission/src/Submissions")
for path,digest in [("arvi_density/Source/HybridGates.lean","a726377f3252b355f1f2d988190950e6200ca7cf31a3dfd681c041c992304ef1"),("arvi_density/Source/HybridGatesMarked.lean","347e17ea4cd90ab4380cccb6809fbfe356da9335f452f00a7f98a7831b589bd7"),("arvi_repeated_marks_on_sil_face_20261025/Gain/Gain.lean","13b29ec2c675e327e9ad7dd128526770d0a1d885cc1659a0e21af791344ae4f7")]:
 assert hashlib.sha256((base/path).read_bytes()).hexdigest()==digest, path
R=s.Rational;x,y,z=s.symbols('x y z')
B0=R(96232839,10**8); L0=R(3853,2000); h=R(1,10); B=R(96223839,10**8);L=R(3851,2000);A=R(6,5);D=R(80)
# Crossing (B0-B)/(L0-L)=9/100, remaining width 1/100.
cross=(B0-B)/(L0-L);assert cross==R(9,100)
v=x/100;p=y/2;t=z;w=cross+v;X=1+D*v;sel=A*v/X;H=1-6*sel
E=(L0-L)*X+(6*B0-L0)*A;K=R(999,1000)*L0*A;nu=K/E
assert all(q>0 for q in [B0-R(22,23),1-B0,B0-B,L0-L,L-1,R(1,6)-h,h-cross,A,D])
def bern(poly):
 poly=s.Poly(s.expand(poly),x,y,z); degrees=[max(0,poly.degree(q)) for q in [x,y,z]]
 terms={(i,j,k):coef for (i,j,k),coef in poly.terms()};out={}
 for I in product(*(range(d+1) for d in degrees)):
  val=R(0)
  for J,c in terms.items():
   if all(J[k]<=I[k] for k in range(3)):
    q=c
    for k in range(3):q*=R(comb(I[k],J[k]),comb(degrees[k],J[k]))
    val+=q
  out[I]=val
 return out,tuple(degrees)
def split(B,deg,axis):
 left={};right={};others=[i for i in range(3) if i!=axis]
 for pair in product(*(range(deg[i]+1) for i in others)):
  ids=[]
  for n in range(deg[axis]+1):
   idx=[0,0,0];idx[axis]=n
   for i,q in zip(others,pair):idx[i]=q
   ids.append(tuple(idx))
  levels=[[B[idx] for idx in ids]]
  while len(levels[-1])>1:
   a=levels[-1];levels.append([(a[i]+a[i+1])/2 for i in range(len(a)-1)])
  for i,idx in enumerate(ids):left[idx]=levels[i][0];right[idx]=levels[deg[axis]-i][i]
 return left,right
def certify(expr,label):
 init,degree=bern(expr); todo=deque([(init,0)]);leaves=0;minv=None;maxdep=0
 while todo:
  coeff,dep=todo.pop();m=min(coeff.values())
  if m>0:
   leaves+=1;minv=m if minv is None else min(minv,m);maxdep=max(maxdep,dep);continue
  if dep>=18:raise RuntimeError((label,dep,float(m)))
  axis=(dep%3)
  if degree[axis]==0:axis=next((i for i,d in enumerate(degree) if d),axis)
  a,b=split(coeff,degree,axis);todo.append((a,dep+1));todo.append((b,dep+1))
 print(label,'degrees',degree,'leaves',leaves,'depth',maxdep,'strict numerator floor',minv,flush=True)
# Q, H, retained and reference gates. Multiply E and/or X positive denominators.
qs=[('q_lower',2*K-E),('q_upper',3*E-4*K),('H_lower',X-60*A*v),
 ('retained_cap',h*(X-6*A*v)-(w*X-A*v)),('retained_width',w*X-A*v),
 ('principal',(1-B+(L-2)*w)*X-R(9,2)*A*v),
 ('second_ref',(R(1,20)+R(3,2)*(1-B)+(R(3,2)*L-R(5,2))*w)*X-R(9,2)*A*v),
 ('second_diag',(1-B+(L-1)*w)*X-4*A*v),('ref_upper',(R(1,3)-2*w)*X-3*A*v)]
for label,poly in qs:certify(poly,label)
# Source cNumY after ν=Y/E; denominator E*cDenY is positive by q bounds.
Y=K*(1-t)+R(3,4)*t*E
branches=[(1,17*p,0,0),(1,16*p,h*p,0),(L0-2*p,16*p*(L0-2*p),p*B0,p),
 (1-p,p*(1-p),p,p),(1-p,0,p+h*p*(1-p),p),
 ((1-p)*(L0-2*p),0,p*(L0-2*p)+B0*p*(1-p),p*(L0-2*p)+p*(1-p))]
for i,(U,alpha,beta,ee) in enumerate(branches):
 C=Y*(5*(X-6*A*v)*U*E+(5*E-6*Y)*(alpha*(w*X-A*v)+beta*(X-6*A*v)))+Y*((1-2*p)*(w*X-A*v)-((B-(L-1)*w)*X-A*v))*((15*E-6*Y)*U/2+(5*E-6*Y)*ee)+E*(A*v)*((15*E-6*Y)*U/2+(5*E-6*Y)*ee)
 certify(C,f'high_{i//3}{i%3}')
print('low identity and derivative are algebraic source identities; E>0 and X>0 from parameters.')

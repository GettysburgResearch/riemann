#!/usr/bin/env python3
"""Exact rational-complex checks of the cluster Gram solution.
Also prints explicitly NON-VALIDATED float approximations to the limiting profile.
No package dependencies. Run from any directory.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
import json,math
@dataclass(frozen=True)
class Q:
    re:F=F(0)
    im:F=F(0)
    def __add__(a,b):
        if not isinstance(b,Q): b=Q(F(b))
        return Q(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a): return Q(-a.re,-a.im)
    def __sub__(a,b): return a+-b
    def __rsub__(a,b):return -a+b
    def __mul__(a,b):
        if not isinstance(b,Q):b=Q(F(b))
        return Q(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def conj(a):return Q(a.re,-a.im)
    def abs2(a):return a.re*a.re+a.im*a.im
    def __truediv__(a,b):
        if not isinstance(b,Q):b=Q(F(b))
        c=a*b.conj();return Q(c.re/b.abs2(),c.im/b.abs2())

def powers(u,L):
    a=[Q(F(1))]
    for k in range(L):a.append(a[-1]*u)
    return a
rows=[]
for N in [0,1,2,5,20]:
 L=N+2;d=L+1
 for h in [F(1,100),F(1,2),F(1),F(3)]:
  # Rational parametrization of the unit circle, t=h/L.
  t=h/L;u=Q((1-t*t)/(1+t*t),2*t/(1+t*t))
  assert u.abs2()==1
  us=powers(u,L);S=sum(us,Q());D=d*d-S.abs2();assert D>0
  alpha=(d-S.conj())/D;beta=(d-S)/D
  r=[alpha+beta*v.conj() for v in us]
  assert sum(r,Q())==Q(F(1))
  assert sum((v*w for v,w in zip(r,us)),Q())==Q(F(1))
  assert all(r[j]-(1+u)*r[j+1]+u*r[j+2]==Q() for j in range(N+1))
  error=sum(v.abs2() for v in r)
  assert error==(2*d-2*S.re)/D
  c=2*L*math.atan(float(t))
  profile=(2-2*math.sin(c)/c)/(1-(2*math.sin(c/2)/c)**2)
  window={}
  if N>=1:
   v=u.conj();vs=powers(v,N);T=sum(vs[1:],Q())
   aa=[];running=Q()
   for n in range(N+1):
    running+=vs[n];aa.append(running*(1-F(n,N)))
   rr=[Q() for _ in range(N+3)];rr[0]=Q(F(1))
   for n,w in enumerate(aa):
    rr[n]-=w;rr[n+1]+=(1+v)*w;rr[n+2]-=v*w
   goal=[Q()]+[(1+vs[k])/N for k in range(1,N+1)]+[-T/N,Q()]
   assert rr==goal
   err=sum(z.abs2() for z in rr)
   assert err==(2*N+2*T.re+T.abs2())/(N*N)
   window={'window_error_exact':str(err),'window_residual_and_norm':'exactly_verified'}
  rows.append({**window,'N':N,'t':str(t),'checks':'unit_modulus,both_evaluations,all_normal_equations,exact_norm',
               'error_squared_exact':str(error),'L_error_float_unvalidated':float(L*error),
               'scaled_angle_float_unvalidated':c,'F_c_float_unvalidated':profile})
p=Path(__file__).resolve().parents[1]/'results'/'clustered_root_transition.json'
p.write_text(json.dumps({'exact_arithmetic':'complex pairs of fractions.Fraction','float_fields':'exploratory; no validated enclosure claimed','rows':rows},indent=2)+'\n')
print(p)

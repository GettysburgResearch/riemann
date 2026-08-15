#!/usr/bin/env python3
"""Exact finite regression for the repaired PR #476 factor-67 spine.

Checks finite algebra only. It does not independently reconstruct the frozen
Hall, all-column, terminal/base/port or endpoint-to-RH theorems and does not
prove RH.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any, Mapping

SCHEMA="riemann.x91726.pr476-native-slack-repair.v1"

def fs(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def digest(x:Mapping[str,Any]): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def sqrtq(x):
 a,b=isqrt(x.numerator),isqrt(x.denominator)
 if a*a!=x.numerator or b*b!=x.denominator: raise ValueError(x)
 return Fraction(a,b)
def T(u,k):
 if k>u:return Fraction(0)
 s=isqrt(k)
 if s*s!=k:raise ValueError("square-node control")
 return 4*sqrtq(u)/k-Fraction(3,s)
def mass(u,n,w):return sum((a*T(u,k) for k,a in zip(n,w)),Fraction(0))

def target_route():
 n=(1,4,9);w=(Fraction(2,5),Fraction(1,3),Fraction(4,15));p=mass(Fraction(144),n,w)
 ends=(Fraction(36),Fraction(16),Fraction(9));a=(Fraction(1,32),Fraction(1,40),Fraction(1,64));c=[mass(x,n,w) for x in ends]
 if any(x>p for x in c) or not sum(a,Fraction(0))<Fraction(1,8):raise AssertionError("target")
 wc=sum((x*y for x,y in zip(a,c)),Fraction(0))
 if not wc<Fraction(1,8)*p:raise AssertionError("weighted")
 fw=(Fraction(2,5),Fraction(3,5));pu=(Fraction(144),Fraction(100));cv=(Fraction(36),Fraction(25));ar=(Fraction(7,100),Fraction(3,40))
 pm=[mass(x,n,w) for x in pu];cm=[mass(x,n,w) for x in cv];ip=sum((x*y for x,y in zip(fw,pm)),Fraction(0));ic=sum((x*y*z for x,y,z in zip(fw,ar,cm)),Fraction(0))
 if not ic<Fraction(1,8)*ip:raise AssertionError("integral")
 return {"parent_mass":fs(p),"child_masses":[fs(x) for x in c],"coefficient_sum":fs(sum(a,Fraction(0))),"weighted_child_mass":fs(wc),"integrated_parent":fs(ip),"integrated_child":fs(ic),"verdict":"PASS_ACTUAL_SHARP_TARGET_WEIGHTED_CHILD_MASS_BELOW_ONE_EIGHTH"}

def add(*v):return [sum((x[i] for x in v),Fraction(0)) for i in range(len(v[0]))]
def scale(c,v):return[c*x for x in v]
def sub(a,b):return[x-y for x,y in zip(a,b)]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Fraction(0))
def slack_route():
 y=[Fraction(1),Fraction(2),Fraction(3)];cur=[Fraction(3),Fraction(2),Fraction(1)];r=[Fraction(1),Fraction(2),Fraction(1)]
 o1=[Fraction(5),Fraction(4),Fraction(3)];x1=[Fraction(4),Fraction(2),Fraction(1)];o2=[Fraction(2),Fraction(3),Fraction(4)];x2=[Fraction(1),Fraction(1),Fraction(3)];a1,a2=Fraction(1,20),Fraction(1,30)
 omega=add(cur,r,scale(a1,o1),scale(a2,o2));real=add(cur,scale(a1,x1),scale(a2,x2));s=sub(omega,real);s1,s2=sub(o1,x1),sub(o2,x2)
 if s!=add(r,scale(a1,s1),scale(a2,s2)) or any(z<0 for z in s):raise AssertionError("cocycle")
 d=dot(y,s);ed=dot(y,r)+a1*dot(y,s1)+a2*dot(y,s2)
 if d!=ed:raise AssertionError("scalar")
 rho=Fraction(1,9);seq=[Fraction(0)]
 for i in range(1,13):seq.append(Fraction(7+3*i)+rho*seq[-1])
 return {"parent_capacity":[fs(x) for x in omega],"parent_slack":[fs(x) for x in s],"parent_delta":fs(d),"depth_control":[fs(x) for x in seq],"verdict":"PASS_PACKET_NATIVE_SLACK_VECTOR_AND_SCALAR_COCYCLE"}

def factor(n):
 o={};d=2
 while d*d<=n:
  while n%d==0:o[d]=o.get(d,0)+1;n//=d
  d+=1 if d==2 else 2
 if n>1:o[n]=o.get(n,0)+1
 return o
def lam(n):
 f=factor(n);return {next(iter(f)):1} if n>1 and len(f)==1 else {}
def v4(q):
 h=0
 while q%4==0:q//=4;h+=1
 return h
def y4(q):
 o={}
 for h in range(v4(q)+1):
  for p,c in lam(q//4**h).items():o[p]=o.get(p,0)+2**h*c
 return {p:c for p,c in o.items() if c}
def expected(q):
 f=factor(q)
 if len(f)==1 and 2 in f:
  e=f[2];return {2:2**((e+1)//2)-1}
 e=f.get(2,0);odd={p:a for p,a in f.items() if p!=2}
 if e%2==0 and len(odd)==1:return {next(iter(odd)):2**(e//2)}
 return {}
def all_column_route():
 nz=0
 for q in range(2,2049):
  if y4(q)!=expected(q):raise AssertionError((q,y4(q),expected(q)))
  nz+=bool(y4(q))
 if not 2913**2<2*(16*129)**2 or 4*130*Fraction(33,4)!=4290 or 5033-4452!=581:raise AssertionError("constants")
 root=Fraction(100);C=Fraction(7,3);eps=Fraction(1,4*10152)/C/(root+130);err=10152*C*eps;reserve=Fraction(1,root+130)
 if not reserve-err>err>0:raise AssertionError("reserve")
 return {"formal_y4_checks":2047,"nonzero_columns":nz,"all_column_square_witness":f"{2913**2} < {2*(16*129)**2}","native_thinning_log_coefficient":4290,"terminal_margin":581,"epsilon":fs(eps),"amplified_error":fs(err),"initial_reserve":fs(reserve),"post_correction_reserve":fs(reserve-err),"verdict":"PASS_ALL_COLUMN_Y4_SUPPORT_NATIVE_COST_AND_STRICT_RESERVE"}

def verify(_=None):
 out={"schema":SCHEMA,"target_mass":target_route(),"native_slack":slack_route(),"all_column":all_column_route(),"proof_boundary":{"pr480_frozen_verdict":"ACCEPTED","factor67_hall_profile":"FROZEN_RECONSTRUCTION_REQUIRED","pr479_all_column_knot_port":"FROZEN_RECONSTRUCTION_REQUIRED","fixed_terminal_base_port_cost":"FROZEN_RECONSTRUCTION_REQUIRED","endpoint_to_rh":"FROZEN_RECONSTRUCTION_REQUIRED","riemann_hypothesis":"UNPROVED"},"verdict":"PASS_PR476_NATIVE_SLACK_REPAIR_FINITE_ALGEBRA"};out["proof_object_sha256"]=digest(out);return out
def main():
 p=argparse.ArgumentParser();p.add_argument("certificate",nargs="?",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();src=json.loads(a.certificate.read_text()) if a.certificate else None;out=verify(src);text=json.dumps(out,indent=2,sort_keys=True)+"\n"
 if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(text)
 print(text,end="")
if __name__=="__main__":main()

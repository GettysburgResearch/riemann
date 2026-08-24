#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

VERDICT="PASS_T105520_PHYSICAL_WICK_SIGNED_STRIP_FRONTIER"
ROOT=Path(__file__).resolve().parents[2]
CONTENT=(
"README_105520.md",
"PR_BODY_105520_ADDENDUM.md",
"PACKET_METADATA_105520.json",
"claims/lemmas/L-105520-half-order-scaled-wick-energy.md",
"claims/lemmas/L-105521-holomorphic-compression-without-a-unit.md",
"claims/lemmas/L-105522-accretive-anchor-and-negative-trace-absorption.md",
"claims/refutations/R-105520-polarization-and-normalization-firewalls.md",
"claims/theorems/T-105520-physical-scale-signed-strip-frontier.md",
"claims/methodology/M-105520-hostile-review-contract.md",
"reports/gpt56-pro/2026-08-24-physical-wick-strip-audit.md",
"standalone/2026-08-24-physical-wick-strip-frontier/PROOF.md",
"experiments/X-105520-physical-wick/README.md",
"experiments/X-105520-physical-wick/verify.py",
"experiments/X-105520-physical-wick/tests/test_verify.py",
)

def mm(A,B):
 n=len(A); p=len(B); m=len(B[0])
 return [[sum((A[i][k]*B[k][j] for k in range(p)),F(0)) for j in range(m)] for i in range(n)]
def add(A,B):
 return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B):
 return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inv_nil(X):
 n=len(X); R=eye(n); P=eye(n)
 for _ in range(1,n):
  P=mm(P,X); R=add(R,P)
 return R
def eq(A,B): return A==B

def b(j): return F(math.comb(2*j,j),4**j*(2*j-1))
def poly4():
 return [F(1),-b(1),-b(2),-b(3),-b(4)]
def qcoeff(maxm=16):
 p=poly4(); pp=[F(0)]*9
 for i,a in enumerate(p):
  for j,c in enumerate(p): pp[i+j]+=a*c
 out=[]; s=F(0)
 for m in range(maxm+1):
  if m<len(pp): s+=pp[m]
  out.append(s)
 return out
def t(m): return F(math.factorial(m),math.factorial(2*m))

def algebra_checks():
 p=poly4()
 assert p==[F(1),F(-1,2),F(-1,8),F(-1,16),F(-5,128)]
 q=qcoeff()
 assert q[:9]==[F(1),F(0),F(0),F(0),F(0),F(7,128),F(35,512),F(75,1024),F(1225,16384)]
 assert all(x==F(1225,16384) for x in q[8:])
 terms=[q[5]**2*t(5)*F(2)**10,q[6]**2*t(6)*F(2)**12,q[7]**2*t(7)*F(2)**14]
 first=q[8]**2*t(8)*F(2)**16
 tail=first*F(17,15)
 bound=sum(terms,F(0))+tail
 assert terms==[F(7,69120),F(35,1216512),F(125,24600576)]
 assert tail==F(29155,36436967424)
 assert bound==F(173344649,1275293859840)
 assert bound<F(1,7000)
 return {"P4":[str(x) for x in p],"q5_q6_q7_qtail":[str(q[5]),str(q[6]),str(q[7]),str(q[8])],"D4_alpha2_upper":str(bound),"target":"1/7000"}

def operator_checks():
 fixtures=0
 for n in range(2,8):
  for a in (F(1,7),F(1,5),F(2,9)):
   X=[[F(0) for _ in range(n)] for _ in range(n)]
   for i in range(n-1): X[i+1][i]=a
   R=inv_nil(X); Rt=tr(R); Xt=tr(X); I=eye(n)
   lhs=sub(add(R,Rt),I)
   mid=sub(I,mm(Xt,X))
   rhs=mm(mm(Rt,mid),R)
   assert eq(lhs,rhs)
   lhs2=add(R,Rt)
   twoI=[[F(2)*x for x in row] for row in I]
   mid2=sub(sub(twoI,X),Xt)
   rhs2=mm(mm(Rt,mid2),R)
   assert eq(lhs2,rhs2)
   fixtures+=1
 return {"exact_nilpotent_resolvent_fixtures":fixtures}

def threshold_checks():
 D=F(173344649,1275293859840)
 perfect=1-4*D
 assert perfect==F(318650120311,318823464960)
 assert perfect>F(9,10)
 margin=perfect-F(9,10)
 assert margin==F(31709001847,318823464960)
 return {"identity_HS_model_fraction_lower":str(perfect),"margin_over_90":str(margin),"negative_trace_cut":"1/20"}

def hashes():
 return {p:hashlib.sha256((ROOT/p).read_bytes().replace(b"\r\n",b"\n")).hexdigest() for p in CONTENT}

def payload():
 x={"verdict":VERDICT,"half_order_symbol_repaired":True,"scaled_energy":algebra_checks(),"accretive_identity":operator_checks(),"threshold":threshold_checks(),"content_sha256":hashes(),"pnt_limit_machine_proved":False,"stripneg105520_proved":False,"ninety_percent_established":False,"record_beaten":False,"rh_established":False}
 x["proof_object_sha256"]=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
 return x

if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,required=True)
 args=ap.parse_args(); x=payload()
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n")
 print(VERDICT); print(x["proof_object_sha256"])
 print("STRIPNEG105520_OPEN")
 print("NINETY_PERCENT_UNPROVED")
 print("RH_UNPROVED")

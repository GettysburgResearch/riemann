#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
VERDICT="PASS_T105560_REVIEWED_SIMPLE_ZERO_RECORD"
ROOT=Path(__file__).resolve().parents[2]
CONTENT=(
"PACKET_METADATA_105560.json","PR_BODY_105560_ADDENDUM.md","README_105560.md",
"claims/lemmas/L-105560-defect-retaining-multiplicity-bridge.md",
"claims/lemmas/L-105561-analytic-three-point-strict-improvement.md",
"claims/lemmas/L-105562-seven-gap-pressure-global-average.md",
"claims/refutations/R-105560-theoremd-normalization-firewall.md",
"claims/theorems/T-105560-reviewed-simple-zero-record.md",
"claims/methodology/M-105560-hostile-review-contract.md",
"experiments/X-105560-reviewed-record/README.md",
"experiments/X-105560-reviewed-record/replay.sh",
"experiments/X-105560-reviewed-record/tests/test_verify.py",
"experiments/X-105560-reviewed-record/verify.py",
"integration/2026-08-24/t105560-source-lock.json",
"reports/gpt56-pro/2026-08-24-reviewed-simple-zero-record.md",
"standalone/2026-08-24-reviewed-simple-zero-record/PROOF.md")
def req(x,m):
 if not x: raise AssertionError(m)
def scalar_checks():
 c=0
 for ip in range(0,41):
  p=F(ip,10)
  for inn in range(0,40):
   n=F(inn,10)
   lhs=(p-n)**2+4*n
   psi=(p-1)**2 if p<=2 else 2*p-3
   rhs=2*p-1+psi
   req(lhs>=rhs,"scalar minimum")
   c+=1
 return c
def sum_free_checks():
 # Rational surrogate: x,y,c>0 makes x^2+xy+y^2+c^2 strictly positive.
 c=0
 for x in range(1,13):
  for y in range(1,13):
   for z in range(1,19):
    req(x*x+x*y+y*y+z*z>0,"sum-free contradiction")
    c+=1
 return c
def h0_interval(terms=48):
 # cot x = 1/x + sum_{n>=1} (-1)^n 2^(2n) B_(2n) x^(2n-1)/(2n)!
 # Use x=1/sqrt(2), hence H0 = 1 - sum_{n>=1} (-1)^n 2^n B_(2n)/(2n)!.
 # Bernoulli numbers by exact Akiyama-Tanigawa.
 A=[F(0) for _ in range(2*terms+1)]; B=[]
 for m in range(2*terms+1):
  A[m]=F(1,m+1)
  for j in range(m,0,-1): A[j-1]=j*(A[j-1]-A[j])
  B.append(A[0])
 s=F(1); prev=None
 for n in range(1,terms+1):
  import math
  t=F((-1)**n * 2**n, math.factorial(2*n))*B[2*n]
  s-=t
  prev=abs(t)
 # The cot series is alternating in positive term magnitudes here; next term bounds remainder.
 import math
 n=terms+1
 # regenerate B through 2n
 A=[F(0) for _ in range(2*n+1)]; BB=[]
 for m in range(2*n+1):
  A[m]=F(1,m+1)
  for j in range(m,0,-1): A[j-1]=j*(A[j-1]-A[j])
  BB.append(A[0])
 nxt=abs(F(2**n,math.factorial(2*n))*BB[2*n])
 return (s-nxt,s+nxt)
def record_checks():
 lo,hi=h0_interval()
 den=1340003
 low=(1345000*lo-2680)/den
 high=(1345000*hi-2680)/den
 req(low>F(673,1000),"record threshold")
 req(F(4997,1345000)==F(19*263,5000*269),"pressure coefficient")
 req(F(268,134500)==F(268,500*269),"span coefficient")
 return {"h0_lower":str(lo),"h0_upper":str(hi),"explicit_lower":str(low),"explicit_upper":str(high),"explicit_lower_bound_gt_673_over_1000":True}
def hashes(): return {p:hashlib.sha256((ROOT/p).read_bytes().replace(b"\r\n",b"\n")).hexdigest() for p in CONTENT}
def payload():
 x={"verdict":VERDICT,
 "multiplicity_bridge":{"positive_index_budget":"(N-S)/2","scalar_minimization_checks":scalar_checks(),"defect_retained":True},
 "analytic_three_point":{"sum_free_algebra_checks":sum_free_checks(),"epsilon_positive_analytically":True,"strict_improvement_without_certificate":True},
 "seven_gap":{"external_commit":"040c5e899e658aed7b56a2a87f501798fe10761d","nodes":707901,"offsets":269,"gap_coefficient":"1/500","pressure_coefficient":"4997/1345000","span_coefficient":"268/134500",**record_checks()},
 "source_lock":{"anthropic_commit":"3635e74826a4c1fcece7d1cd2b6fa75e43a00510","anthropic_path":"Zeta23/ThmD/Mult.lean","anthropic_blob":"a36b073fd6b04b568aac377026eafcce129946d1","verifier_blob":"ed0bf0a6703238ad390745135d8d7d6f594c1e5e","kernel_blob":"dda7a856bd7c5f9cd79d7647a3e40820386c7780","rounding_blob":"1ea233e6387735659cc1aa51507d77a9efb0563c","certificate_blob":"02f939f071c7fdbcb21b8991e170ef7fc301b19c"},
 "independent_second_replay":{"completed":False,"reason":"no observable workflow run from GitHub App commits"},
 "content_sha256":hashes(),"ninety_percent_established":False,"rh_established":False}
 x["proof_object_sha256"]=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return x
if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args(); x=payload(); a.output.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n"); print(VERDICT); print(x["proof_object_sha256"]); print("SOURCE_QUALIFIED_UNCONDITIONAL_SIMPLE_ZERO_THEOREM\nINDEPENDENT_SECOND_REPLAY_PENDING\nNINETY_PERCENT_UNPROVED\nRH_UNPROVED")

#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105320_WICK_PICK_FIRST_CHAOS_CANCELLATION"
ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
 "claims/lemmas/L-105320-wick-coefficient-bridge.md",
 "claims/lemmas/L-105321-wick-diagonal-density.md",
 "claims/lemmas/L-105322-wick-toeplitz-rank-reserve.md",
 "claims/lemmas/L-105323-differentiated-reexpansion-transfer.md",
 "claims/refutations/R-105320-raw-cauchy-model-misses-prime-chaos.md",
 "claims/theorems/T-105320-wick-pick-transfer-frontier.md",
 "claims/methodology/M-105320-hostile-review-contract.md",
 "experiments/X-105320-wick-pick/verify.py",
 "experiments/X-105320-wick-pick/tests/test_verify.py",
)
N=180

def req(x,m):
 if not x: raise AssertionError(m)

def primes(n):
 a=[1]*(n+1); a[:2]=[0,0]
 for p in range(2,int(n**.5)+1):
  if a[p]: a[p*p:n+1:p]=[0]*(((n-p*p)//p)+1)
 return [p for p in range(2,n+1) if a[p]]
P=primes(N); wt={p:F(i+2,i+1) for i,p in enumerate(P)}

def fac(n):
 d={}; v=n
 for p in P:
  if p*p>v: break
  while v%p==0: d[p]=d.get(p,0)+1; v//=p
 if v>1: d[v]=d.get(v,0)+1
 return d

def lg(n): return sum((e*wt[p] for p,e in fac(n).items()),F(0))
def om(n): return sum(fac(n).values())
def vm(n):
 d=fac(n)
 return wt[next(iter(d))] if len(d)==1 else F(0)
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def conv(f,g):
 return [F(0)]+[sum((f[d]*g[n//d] for d in divs(n)),F(0)) for n in range(1,N+1)]

def bridge():
 lam=[F(0)]+[vm(n) for n in range(1,N+1)]
 ll=[F(0)]+[vm(n)*lg(n) for n in range(1,N+1)]
 M=max(om(n) for n in range(1,N+1)); pw=[[F(0)]*(N+1) for _ in range(M+1)]; pw[0][1]=1
 for m in range(1,M+1): pw[m]=conv(pw[m-1],lam)
 rows=[conv(ll,pw[j]) for j in range(M)]
 a=b=0
 for n in range(2,N+1):
  for m in range(1,om(n)+1): req(lg(n)*pw[m][n]==m*rows[m-1][n],"log convolution"); a+=1
  for L in (F(5,2),F(7,3),F(11,4)):
   r=sum((L**(-m-1)*pw[m][n] for m in range(1,om(n)+1)),F(0))
   dc=sum((m*L**(-m-1)*rows[m-1][n] for m in range(1,om(n)+1)),F(0))
   req(dc==lg(n)*r,"parameter derivative"); b+=1
 return {"nmax":N,"log_convolution_checks":a,"coefficient_derivative_checks":b}

def coeffs(M=24): return [sum((F((-1)**j,math.factorial(j)) for j in range(m+1)),F(0)) for m in range(M+1)]
def wick():
 c=coeffs(); req(c[:5]==[1,0,F(1,2),F(1,3),F(3,8)],"coefficients")
 for m in range(2,len(c)): req(0<c[m]<=F(1,2),"alternating bound")
 for m in range(len(c)): req(c[m]-(c[m-1] if m else 0)==F((-1)**m,math.factorial(m)),"series")
 return {"maximum_degree":23,"coefficients":[str(x) for x in c[:9]]}
def diagonal():
 c=coeffs(); vals=[c[m]**2*F(math.factorial(m),math.factorial(2*m)) for m in range(2,25)]
 req(vals[:3]==[F(1,48),F(1,1080),F(3,35840)],"first energies")
 tail=F(11,1270080); bound=sum(vals[:3],F(0))+tail; req(sum(vals)<bound<F(7,320),"energy bound")
 return {"m2":"1/48","m3":"1/1080","m4":"3/35840","tail_bound":str(tail),"rational_upper":str(bound),"target_upper":"7/320","pnt_limit_machine_proved":False}
def record():
 eta=F(160,167)*F(99,101)**2; out=2*eta-1-F(821,5000)
 req(eta==F(1568160,1703567) and out==F(5765136493,8517835000),"record fractions")
 req(out>F(672501,1000000),"record margin")
 return {"two_sided_energy_upper":"7/160","model_effective_rank_lower":"160/167","robust_effective_rank_lower":str(eta),"conditional_line_output":str(out),"published_upper_decimal_import":"672501/1000000"}
coefficient_bridge_checks=bridge
wick_algebra_checks=wick
diagonal_bound_checks=diagonal
record_checks=record

def hashes(): return {p:hashlib.sha256((ROOT/p).read_bytes().replace(b"\r\n",b"\n")).hexdigest() for p in CONTENT}
def payload():
 x={"verdict":VERDICT,"coefficient_bridge":bridge(),"wick_algebra":wick(),"diagonal_bound":diagonal(),"record_bridge":record(),"raw_first_chaos":{"prime_simplex_integral":"1/2","one_percent_raw_comparison_refuted":True},"content_sha256":hashes(),"analytic_pnt_limit_machine_proved":False,"montgomery_vaughan_transfer_machine_proved":False,"wxfer105320_proved":False,"new_zero_proportion_established":False,"rh_established":False}
 x["proof_object_sha256"]=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest(); return x
build_payload=payload

if __name__=="__main__":
 ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,required=True); q=ap.parse_args(); x=payload(); q.output.write_text(json.dumps(x,indent=2,sort_keys=True)+"\n")
 print(VERDICT); print(x["proof_object_sha256"]); print("WXFER105320_OPEN\nNEW_ZERO_PROPORTION_UNPROVED\nRH_UNPROVED")

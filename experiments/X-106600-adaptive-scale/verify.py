#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json

# Complex numbers over Q represented as pairs.
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0],-z[1])
def abs2(z): return z[0]*z[0]+z[1]*z[1]
I=(Q(0),Q(1))

checks=0

# Endpoint algebra on exact rational fixtures.
for F in [Q(-3),Q(-1),Q(1),Q(2),Q(5)]:
  for Fp in [Q(-4),Q(-1),Q(1),Q(3)]:
    for G in [Q(-5),Q(-2),Q(1),Q(4)]:
      for Gp in [Q(-3),Q(-1),Q(2),Q(5)]:
        for a in [Q(1,7),Q(1,3),Q(2,5),Q(3,2)]:
          Em=(F,-a*Fp); Ep=(F,a*Fp)
          GpC=(G,a*Gp); GmC=(G,-a*Gp)
          N=mul(Em,GpC); D=mul(Ep,GmC)
          expected=(Q(0),2*a*(F*Gp-Fp*G))
          assert sub(N,D)==expected
          assert abs2(N)==abs2(D)
          lhs=abs2(sub(D,N))*abs2(D)
          rhs=4*a*a*(F*Gp-Fp*G)**2*abs2(D)
          assert lhs==rhs
          checks+=1

# Monochromatic carrier with exact Pythagorean circle points.
for c,s in [(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(7,25),Q(24,25))]:
  assert c*c+s*s==1
  for w in [Q(1),Q(2),Q(5,3)]:
    for K,sgn in [(1,-1),(3,1),(5,-1),(7,1)]:
      F=c; Fp=-w*s
      G=sgn*(w**K)*s
      Gp=sgn*(w**(K+1))*c
      a=1/w
      N=mul((F,-a*Fp),(G,a*Gp))
      D=mul((F,a*Fp),(G,-a*Gp))
      assert N==(-D[0],-D[1])
      assert D!=(Q(0),Q(0))
      checks+=1

# One-factor concentrated phase identity:
# (1/(4pi))*8 a^3 * pi/(2a^3) = 1.
for a in [Q(1,100),Q(1,7),Q(1),Q(9,4)]:
  charge=Q(1,4)*8*a**3*Q(1,2)/a**3
  assert charge==1
  checks+=1

allowance=Q(97,1000)
deep=Q(3,40)
shallow=Q(11,500)
assert deep+shallow==allowance
assert Q(997,1000)-allowance==Q(9,10)

result={
  "verdict":"PASS_T106600_ADAPTIVE_SCALE_ENDPOINT",
  "exact_checks":checks,
  "fifth_endpoint_allowance":"97/1000",
  "deep_height_payment":"3/40",
  "adaptive_shallow_allowance":"11/500",
  "monochromatic_reduced_hankel_charge":"0",
  "pointwise_alignment_fixture_charge":"1",
  "adaptiveangle106600_proved":False,
  "ninety_percent_established":False,
  "rh_established":False,
}
canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
result["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
out=Path(__file__).parent/"results"/"verification.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(result["verdict"])
print(result["proof_object_sha256"])

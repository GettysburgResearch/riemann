#!/usr/bin/env python3
from fractions import Fraction
import hashlib, itertools, json, math

# Exact largest-prime telescoping and activation-tail identities.
prime_sets=[[67],[67,71],[67,71,73],[71,73,79,83]]
telescoping=0
activation=0
for ps in prime_sets:
    e=Fraction(1); dec=Fraction(0)
    for p in ps:
        dec += e/Fraction(p)
        e *= 1-Fraction(1,p)
    assert dec==1-e
    telescoping += 1
    full=e
    for X in range(1,500):
        trunc=Fraction(0); inactive=Fraction(0)
        for mask in range(1<<len(ps)):
            prod=1; parity=0
            for i,p in enumerate(ps):
                if mask>>i & 1:
                    prod*=p; parity^=1
            term=Fraction(-1 if parity else 1,prod)
            if prod<=X: trunc+=term
            else: inactive+=term
        assert trunc==full-inactive
        activation += 1

# Exact cell-minimum formula on rational fixtures.
cell=0
for a,b,r in [(Fraction(-4),Fraction(-6),Fraction(5)),
              (Fraction(-3),Fraction(-4),Fraction(7))]:
    q=Fraction(4)*a/(Fraction(3)*b)  # q=1/sqrt(X_*)
    value=16*r+24*a*q-9*b*q*q
    assert value==16*(r+a*a/b)
    cell += 1

# Numerical rank-one determinant lemma regression.
rank=0
for N in range(2,100):
    for beta in (-2,-1,1):
        t=7/5; a=-3/7; b=11/13
        q=beta/(N**1.5); rN=math.sqrt(N)
        lhs=(t-q)*(b-q*N)-(a+q*rN)**2
        rhs=(t*b-a*a)-q*(b+2*a*rN+t*N)
        assert abs(lhs-rhs)<1e-10
        rank += 1

payload={
  'schema':'riemann.t100200.two-terminal-routes.v1',
  'base_sha':'2a351548eb7960ff8ae99f193c10e278984c5657',
  'external_blpte_sha':'d42817f4de15b97d37f760578d64d067a77be5c5',
  'telescoping_checks':telescoping,
  'activation_tail_checks':activation,
  'cell_critical_checks':cell,
  'rank_one_determinant_checks':rank,
  'cehc100200_proved':False,
  'rapc100210_proved':False,
  'rh_established':False,
  'verdict':'PASS_T100200_CELL_HANKEL_AND_LARGEST_PRIME_TERMINAL_ASSAULT'
}
payload['proof_object_sha256']=hashlib.sha256(
    json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
print(json.dumps(payload,indent=2,sort_keys=True))
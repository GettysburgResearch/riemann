#!/usr/bin/env python3
from fractions import Fraction as F
import json
from pathlib import Path

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A): return [list(x) for x in zip(*A)]
def ma(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def ms(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sm(c,A): return [[c*x for x in row] for row in A]
def det2(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def psd2(A): return A[0][0]>=0 and A[1][1]>=0 and det2(A)>=0

S=[[F(1),F(-1)],[F(1),F(-2)]]
Sinv=[[F(2),F(-1)],[F(1),F(-1)]]
H=mm(mt(S),S)
I=[[F(1),F(0)],[F(0),F(1)]]
assert H==[[F(2),F(-3)],[F(-3),F(5)]]
assert psd2(ms(sm(F(7),I),H))

def state_matrix(A,B): return mm(mm(Sinv,[[A,F(0)],[F(0),B]]),S)
def innovation(M): return ms(H,mm(mm(mt(M),H),M))

def check_r(r):
    A=1-r*r; B=1-r; tau=r*(1-r)
    M=state_matrix(A,B)
    D=innovation(M)
    direct=mm(mt(S),mm([[1-A*A,F(0)],[F(0),1-B*B]],S))
    assert D==direct and psd2(D)
    alpha=1-A*A; beta=1-B*B
    harmonic=alpha*beta/(alpha+beta)
    assert harmonic>2*tau*tau
    return {"r":str(r),"innovation_det":str(det2(D)),"harmonic_over_tau2":str(harmonic/(tau*tau))}

rows=[check_r(F(1,n)) for n in (8,9,10,11,12,16,32)]

# Three-factor exact telescope at rational test multipliers.
Ms=[state_matrix(1-r*r,1-r) for r in (F(1,9),F(1,11),F(1,16))]
P=I
suminnov=[[F(0),F(0)],[F(0),F(0)]]
for M in Ms:
    D=innovation(M)
    suminnov=ma(suminnov,mm(mm(mt(P),D),P))
    P=mm(M,P)
assert suminnov==ms(H,mm(mm(mt(P),H),P))

# Endpoint port floor and H embedding for the extremal |t|=8/9.
for t in (F(8,9),F(-8,9),F(0)):
    Port=[[F(1),t],[t,F(1)]]
    assert psd2(ms(Port,sm(F(1,9),I)))
    assert psd2(ms(sm(F(63,2),Port),sm(F(1,2),H)))

result={
  "classification":"PASS_HILBERT_INNOVATION_ENDPOINT_PORT",
  "H":[[str(x) for x in row] for row in H],
  "rank_one_checks":rows,
  "three_factor_telescope":True,
  "endpoint_embedding_constant":"63/2",
  "bounded_mass_constant":"147",
  "scope":"Exact Fraction algebra. This verifies the common quadratic port budget, not the least-prime positive source partition or RH."
}
out=Path(__file__).resolve().parent/"results"/"verification.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(result["classification"])

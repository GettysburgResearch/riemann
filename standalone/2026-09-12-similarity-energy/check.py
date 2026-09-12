#!/usr/bin/env python3
"""Exact finite controls only; no theta quadrature or RH acceptance."""
from fractions import Fraction as Q
from pathlib import Path
import argparse, json

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def T(A): return [list(row) for row in zip(*A)]
def mm(A,B):
    return [[sum((x*y for x,y in zip(row,col)),Q(0))
             for col in zip(*B)] for row in A]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,c): return [[c*x for x in row] for row in A]
def tr(A): return sum((A[i][i] for i in range(len(A))), Q(0))
def norm2(A): return sum((x*x for row in A for x in row), Q(0))
def ident(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A); W=[list(map(Q,row))+r for row,r in zip(A,ident(n))]
    for j in range(n):
        k=next((k for k in range(j,n) if W[k][j]),None)
        require(k is not None,'singular matrix')
        W[j],W[k]=W[k],W[j]
        v=W[j][j]; W[j]=[x/v for x in W[j]]
        for i in range(n):
            if i!=j:
                v=W[i][j]; W[i]=[x-v*y for x,y in zip(W[i],W[j])]
    return [row[n:] for row in W]
def diag(vals):
    return [[Q(vals[i]) if i==j else Q(0) for j in range(len(vals))]
            for i in range(len(vals))]
def frac(q):
    q=Q(q); return [str(q.numerator),str(q.denominator)]

def reconstruct():
    K=list(map(lambda row:list(map(Q,row)),[
        [0,0,0,0],[-1,0,0,0],[1,3,0,-1],[0,0,1,0]]))
    require(tr(mm(K,K))==-2,'synthetic trace')
    energies=[]
    for R in [1,2,3,10,100]:
        S=diag([R*R,R,1,1])
        A=mm(mm(S,K),inv(S))
        expected=Q(2)+Q(10,R*R)+Q(1,R**4)
        require(norm2(A)==expected,'two-score full energy')
        H=scale(add(A,T(A)),Q(1,2))
        require(2*norm2(H)==norm2(A)+tr(mm(A,A)),
                'Hermitian identity')
        energies.append({'R':R,'energy':frac(expected)})
    S2=[[Q(2),Q(1)],[Q(1),Q(1)]]
    G=mm(S2,S2); Gi=inv(G)
    S=[[Q(2),Q(1),Q(0),Q(0)],[Q(1),Q(1),Q(0),Q(0)],
       [Q(0),Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(0),Q(1)]]
    A=[row[:2] for row in K[:2]]; B=[row[2:] for row in K[:2]]
    C=[row[:2] for row in K[2:]]; D=[row[2:] for row in K[2:]]
    rhs=(tr(mm(mm(mm(G,A),Gi),T(A)))+tr(mm(G,mm(B,T(B))))
         +tr(mm(Gi,mm(T(C),C)))+norm2(D))
    lhs=norm2(mm(mm(S,K),inv(S)))
    require(lhs==rhs,'full four-block identity')
    a_hi=Q('2.7912'); b_lo=Q('12.2172')
    c_lo=((6-a_hi)*b_lo-5*a_hi*a_hi)/(180*(a_hi-1))
    require(c_lo>Q(7,10000),'inherited-moment cycle bound')
    delta=Q(1,3000000)
    require(delta*(1+delta)**3 < Q(7,10000)**2,
            'diagonal energy exclusion')
    # Independent expansion of the polynomial-cycle formula.
    for a,b in [(Q(3),Q(15)),(Q(14,5),Q(61,5)),(Q(5,2),Q(11))]:
        aa=-(b-a)/(a-1); bb=-a-aa
        direct=(b/5+aa*a/3+bb)/24
        simplified=((6-a)*b-5*a*a)/(180*(a-1))
        require(direct==simplified,'cycle algebra')
    return {'status':'BOUNDED_EXACT_CONTROLS_ONLY','rh_proved':False,
            'theta_integrals_evaluated':False,
            'source_moment_intervals':'INHERITED_NOT_RECOMPUTED',
            'synthetic_energy_panels':energies,
            'nonlocal_block_energy':frac(lhs),
            'cycle_lower_bound':frac(c_lo),
            'excluded_diagonal_excess':frac(delta)}

def pairs(items):
    d={}
    for k,v in items:
        require(k not in d,'duplicate JSON key')
        d[k]=v
    return d
def bad_float(s): raise ValueError('floating JSON value not permitted')
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',type=Path)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    result=reconstruct()
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.check:
        got=json.loads(args.check.read_text(),object_pairs_hook=pairs,
                       parse_float=bad_float,parse_constant=bad_float)
        require(json.dumps(got,sort_keys=True,separators=(',',':'))==
                json.dumps(result,sort_keys=True,separators=(',',':')),
                'receipt mismatch')
    if args.write: args.write.write_text(text)
    print(text,end='')
if __name__=='__main__':
    main()

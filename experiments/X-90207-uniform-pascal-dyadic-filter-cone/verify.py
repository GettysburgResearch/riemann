#!/usr/bin/env python3
"""Exact replay for L-90216 uniform-Pascal dyadic filter cone."""
from __future__ import annotations
from fractions import Fraction
from dataclasses import dataclass
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results'/'verification.json'

@dataclass(frozen=True)
class Q2:
    a: Fraction=Fraction(0)
    b: Fraction=Fraction(0)
    def __add__(self,o):
        o=toQ(o);return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q2(-self.a,-self.b)
    def __sub__(self,o):return self+(-toQ(o))
    def __rsub__(self,o):return toQ(o)-self
    def __mul__(self,o):
        o=toQ(o);return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=toQ(o);den=o.a*o.a-2*o.b*o.b
        return Q2((self.a*o.a-2*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def approx(self):return float(self.a)+float(self.b)*2**0.5

def toQ(x):return x if isinstance(x,Q2) else Q2(Fraction(x),Fraction(0))

def cone_data(q):
    J=len(q)-1
    S=[];z=toQ(0)
    for x in q:z=z+x;S.append(z)
    rows=[]
    for j in range(1,J+1):
        A=2*sum((2**l)*S[l] for l in range(j))
        L=A-(2**j-1)*S[j]
        rows.append((j,S[j],A,L))
    At=2*sum((2**l)*S[l] for l in range(J+1))
    return S,rows,At

def direct_drift(q,m):
    J=len(q)-1
    S=[];z=toQ(0)
    for x in q:z=z+x;S.append(z)
    j=min(m.bit_length()-1,J)
    e=-S[j]
    F=toQ(m)+e
    f=F/m
    pf=toQ(0)
    for k in range(1,m):
        jk=min(k.bit_length()-1,J)
        ek=-S[jk]
        fk=(toQ(k)+ek)/k
        pf += Fraction(2*k,m*(m-1))*fk
    return f-pf

def rational_cases():
    cases={
      'haar':[Fraction(1),Fraction(-1)],
      'canonical':[Fraction(1),Fraction(-3,2),Fraction(1,2)],
      'higher_feasible':[Fraction(1),Fraction(-7,5),Fraction(1,2),Fraction(-1,10)],
      'mutation_above_canonical':[Fraction(1),Fraction(-151,100),Fraction(51,100)],
    }
    out={}
    for name,q0 in cases.items():
        q=[toQ(x) for x in q0]
        S,rows,At=cone_data(q)
        algebra_ok=all(r[2].approx()>=-1e-14 and r[3].approx()>=-1e-14 for r in rows) and At.approx()>=-1e-14
        direct_ok=all(direct_drift(q,m).approx()>=-1e-14 for m in range(2,2**(len(q)+1)+20))
        assert algebra_ok==direct_ok
        out[name]={
          'q':[str(x) for x in q0],
          'cone_feasible':algebra_ok,
          'min_direct_drift':min(direct_drift(q,m).approx() for m in range(2,100)),
          'tail_A':At.approx(),
        }
    assert out['haar']['cone_feasible']
    assert out['canonical']['cone_feasible']
    assert out['higher_feasible']['cone_feasible']
    assert not out['mutation_above_canonical']['cone_feasible']
    return out

def factor64_case():
    h=Fraction(1,2)
    q=[
      Q2(1,0),
      Q2(Fraction(-1,4),-h),
      Q2(Fraction(-3,4),Fraction(1,8)),
      Q2(Fraction(-3,4),Fraction(3,8)),
      Q2(Fraction(-1,4),Fraction(3,8)),
      Q2(1,Fraction(1,8)),
      Q2(0,-h),
    ]
    S,rows,At=cone_data(q)
    j3=rows[2]
    assert j3[2]==Q2(5,-5)
    assert j3[2].approx()<0
    d15=direct_drift(q,15)
    assert d15==Q2(Fraction(1,42),Fraction(-1,42))
    assert d15.approx()<0
    return {
      'A3_exact':'5-5*sqrt(2)',
      'd15_exact':'(1-sqrt(2))/42',
      'A3_approx':j3[2].approx(),
      'd15_approx':d15.approx(),
      'tail_A_approx':At.approx(),
    }

def main():
    result={
      'verdict':'PASS_X_90207_UNIFORM_PASCAL_DYADIC_FILTER_CONE',
      'rational_cases':rational_cases(),
      'factor64_no_go':factor64_case(),
      'cone_statement':{
        'S_j':'sum_(l<=j) q_l',
        'A_j':'2 sum_(l<j) 2^l S_l',
        'conditions':'A_j>=0 and A_j-(2^j-1)S_j>=0, plus tail A_(J+1)>=0',
      }
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['verdict']);print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()

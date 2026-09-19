#!/usr/bin/env python3
"""Exact Sylvester reference algebra and rank-deflation regression fixtures.

No CM integrals, heights, L-value or zero computations are performed. Analytic
rank one is an explicitly attributed external theorem, not proved by this code.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from pathlib import Path


def need(ok: bool, message: str):
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, "a", F(self.a)); object.__setattr__(self, "b", F(self.b))
    @staticmethod
    def cast(x):
        return x if isinstance(x,K) else K(F(x))
    def __add__(self, other):
        other=K.cast(other);return K(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self, other):return self+-K.cast(other)
    def __rsub__(self, other):return K.cast(other)+-self
    def __mul__(self, other):
        other=K.cast(other)
        return K(self.a*other.a-self.b*other.b,self.a*other.b+self.b*other.a-self.b*other.b)
    __rmul__=__mul__
    def conjugate(self):return K(self.a-self.b,-self.b)
    def __truediv__(self, other):
        other=K.cast(other);norm=other.a**2-other.a*other.b+other.b**2
        need(norm!=0,"division by zero")
        z=self*other.conjugate();return K(z.a/norm,z.b/norm)
    def __pow__(self, n):
        need(type(n) is int and n>=0,"nonnegative integer exponent required")
        v=K(1)
        for _ in range(n):v=v*self
        return v
    def data(self):return [str(self.a),str(self.b)]


omega=K(0,1)
lam=1-omega


def projector(n: int, j: int):
    need(type(n) is int and n>0 and n%3==0,"group order must be divisible by three")
    need(type(j) is int and j in (1,2),"nontrivial cubic character required")
    Pi=[omega**((-j*k)%3) for k in range(n)]
    D=[(1-z)/lam for z in Pi]
    need(all(x.a.denominator==x.b.denominator==1 for x in D),"nonintegral divided projector")
    unit=-(omega**j-1)/lam
    need(all(lam*D[k]==1-Pi[k] for k in range(n)),"norm minus projector")
    need(all(D[(k-1)%n]-D[k]==unit*Pi[k] for k in range(n)),"cyclic divided-difference identity")
    need(all(D[k]==D[k%3] for k in range(n)),"period-three failure")
    return {"n":n,"j":j,"periodic_coefficients":[x.data() for x in D[:3]],"unit":unit.data()}


def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def primary(q):
    values=[(a,b) for b in range(3,2*isqrt(q)+3,3) for a in range(-2*isqrt(q)-2,2*isqrt(q)+3)
            if a%3==1 and a*a-a*b+b*b==q]
    need(len(values)==1,"ambiguous primary factor")
    return values[0]


def family_row(p):
    need(prime(p) and p%9==8,"prime in class 8 mod 9 required")
    for q in range(2,100):
        if not prime(q) or q%9!=4:continue
        a,b=primary(q)
        w=(-a*pow(b,-1,q))%q
        residue=pow(p,(q-1)//3,q)
        beta=next((j for j in (0,1,2) if pow(w,j,q)==residue),None)
        need(beta is not None,"not a cubic residue value")
        if beta:break
    else:raise ValueError("no bounded auxiliary prime found; no theorem of failure implied")
    matrices=[]
    for d in (2,1):
        c=d*beta%3
        matrix=[[2,2*c%3],[0,c]]
        need(2*c%3!=0,"singular descent matrix")
        matrices.append(matrix)
    v=0;t=p+1
    while t%3==0:v+=1;t//=3
    return {"p":p,"q":q,"varpi":[a,b],"residue_exponent":beta,
            "boundary_sign_relative_to_eta_q":1 if beta==2 else -1,
            "eta_q":1 if q in (13,31) else "not determined here",
            "class_group_order":(p+1)//3,"three_primary_quotient":3**(v-1),
            "descent_matrices_mod_3":matrices}


def fermat(q, u, v):
    a,b=primary(q);varpi=K(a,b);bar=varpi.conjugate()
    need(varpi*v**3-u**3==bar,"Fermat cubic identity")
    y=(u**3+varpi*v**3)/2
    xt=u*v  # x=xt*t, t^3=varpi
    need(y*y-bar*bar/4==varpi*xt**3,"image curve equation")
    need(y+bar/2==varpi*v**3 and y-bar/2==u**3,"descent factors")
    return {"q":q,"u":u.data(),"v":v.data(),"x_coefficient_of_t":xt.data(),"y":y.data()}


def imaginary_pick(rank: int, epsilon: int, ys):
    """X(z)=z^rank(z^2+epsilon), sampled at z=i*y, exact rational matrix."""
    need(type(rank) is int and rank>=0,"rank")
    need(epsilon in (-1,1),"polynomial sign")
    yy=list(map(F,ys));need(all(y>0 and epsilon-y*y!=0 for y in yy),"point at pole or outside domain")
    h=[F(rank,y)-2*y/(epsilon-y*y) for y in yy]
    return [[(h[i]+h[j])/(yy[i]+yy[j]) for j in range(len(yy))] for i in range(len(yy))]


def fixture():
    need(omega**2+omega+1==K(),"Eisenstein relation")
    need(lam**2==-3*omega,"lambda normalization")
    projectors=[projector(n,j) for n in (3,6,9,18,27,81) for j in (1,2)]
    family=[family_row(p) for p in range(2,500) if prime(p) and p%9==8]
    need(len(family)==14,"fourteen primes below 500")
    need(family[0]["q"]==13 and family[0]["residue_exponent"]==2,"q13 p17 orientation")
    need(next(x for x in family if x["p"]==107)["residue_exponent"]==1,"q13 p107 orientation")
    lifts=[fermat(13,omega-1,K(1)),fermat(31,(-2-10*omega)/7,(-5+3*omega)/7)]
    ys=[F(1,2),F(1,3),F(2,3)]
    cases=[]
    for r in (1,3):
        for eps in (-1,1):
            raw=imaginary_pick(r,eps,ys);deflated=imaginary_pick(0,eps,ys)
            need(all(raw[i][j]-F(r,ys[i]*ys[j])==deflated[i][j]
                     for i in range(len(ys)) for j in range(len(ys))),"rank-one deflation identity")
            cases.append({"rank":r,"epsilon":eps,"imaginary_heights":list(map(str,ys)),
                          "raw":[list(map(str,row)) for row in raw],
                          "deflated":[list(map(str,row)) for row in deflated]})
    raw=imaginary_pick(1,1,[F(1,2)])[0][0]
    df=imaginary_pick(0,1,[F(1,2)])[0][0]
    under=imaginary_pick(3,1,[F(1,2)])[0][0]-4
    need((raw,df,under)==(F(4,3),F(-8,3),F(16,3)),"masking regression")
    return {"schema":"BCP26.sylvester-lfamily.v1",
            "external_theorem":"Burungale--Tian arXiv:2609.14893v2 Theorem 1.1; not re-proved by this code",
            "projectors":projectors,"fermat_lifts":lifts,"family_below_500":family,
            "rank_deflation_cases":cases,
            "synthetic_masking":{"raw":"4/3","correctly_deflated":"-8/3","rank_three_underdeflated":"16/3"}}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--output",type=Path);ap.add_argument("--check",type=Path)
    args=ap.parse_args();text=json.dumps(fixture(),sort_keys=True,indent=2)+"\n"
    if args.check:
        need(args.check.read_text()==text,"fixture changed or not reproduced")
        print("BCP26 L-family algebra PASS: 14 families, 12 projectors, 2 Fermat lifts, 4 exact Pick matrices")
    elif args.output:args.output.write_text(text)
    else:print(text,end="")

if __name__=="__main__":main()

#!/usr/bin/env python3
from fractions import Fraction
import json

class Q2:
    def __init__(self,a=0,b=0): self.a,self.b=Fraction(a),Fraction(b)
    def __add__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __mul__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def zero(self): return self.a==0 and self.b==0
    def obj(self):
        return {"rational":f"{self.a.numerator}/{self.a.denominator}",
                "sqrt2":f"{self.b.numerator}/{self.b.denominator}"}

def invsqrt(r):
    return Q2(Fraction(1,2**(r//2))) if r%2==0 else Q2(0,Fraction(1,2**((r+1)//2)))

LOW={1:Fraction(5),2:Fraction(-63),3:Fraction(170)}
HIGH={1:Fraction(-1,3),2:Fraction(1),3:Fraction(-2,3)}
A=[1,1,-8,-8,16,16]; B=[0,-1,-8,0,32,16]
Q=[Fraction(1),Fraction(-7,8),Fraction(7,32),Fraction(-1,64)]

def band(src,j):
    out={1:Q2(),2:Q2(),3:Q2()}
    for h,q in enumerate(Q):
        for r,c in enumerate(src):
            if not c: continue
            t=r+h
            branch=LOW if t<=j-2 else HIGH if t in (j-1,j) else None
            if branch is None: continue
            pref=Q2(q*c)*invsqrt(r)
            for k,w in branch.items(): out[k]=out[k]+pref*w*2**(t*k)
    return out

def certificate():
    bands=[]
    for j in range(10):
        bands.append({"index":j,"interval":f"(2^-{j+1},2^-{j}]",
                      "J0":{f"x^{k}":band(A,j)[k].obj() for k in (1,2,3)},
                      "J1":{f"x^{k}":band(B,j)[k].obj() for k in (1,2,3)}})
    for src in (A,B):
        for j in range(10,17): assert all(v.zero() for v in band(src,j).values())
    return {"schema":"riemann.q4.95400.exact-kernels.v1","bands":bands,
            "support":"zero on [0,2^-10] and (1,infinity)",
            "scale_filter":["1","-7/8","7/32","-1/64"]}

if __name__=="__main__": print(json.dumps(certificate(),indent=2,sort_keys=True))

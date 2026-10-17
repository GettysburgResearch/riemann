#!/usr/bin/env python3
"""Exact Laurent-polynomial checks of the displayed Euler-factor identities.

The ring variables are (D,W,V,E,r). Negative exponents are permitted, so the
original r**(-1) formula can be checked without floating-point evaluation.
This does not verify the primary source or any analytic projection theorem.
"""
from fractions import Fraction as Q
import json
from hashlib import sha256
from pathlib import Path

def require(condition, message):
    if not condition:
        raise ValueError(message)


class P:
    def __init__(self, terms=None):
        if isinstance(terms, (int,Q)):
            terms={(0,0,0,0,0):Q(terms)}
        self.terms={e:Q(c) for e,c in (terms or {}).items() if c}
    def __add__(self, other):
        other=other if isinstance(other,P) else P(other)
        out=self.terms.copy()
        for e,c in other.terms.items(): out[e]=out.get(e,Q(0))+c
        return P(out)
    __radd__=__add__
    def __neg__(self): return P({e:-c for e,c in self.terms.items()})
    def __sub__(self, other): return self+-coerce(other)
    def __rsub__(self, other): return coerce(other)+-self
    def __mul__(self, other):
        other=coerce(other)
        out={}
        for e,c in self.terms.items():
            for f,d in other.terms.items():
                g=tuple(x+y for x,y in zip(e,f))
                out[g]=out.get(g,Q(0))+c*d
        return P(out)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:
            require(len(self.terms)==1, "exact check 36")
            e,c=next(iter(self.terms.items()))
            return P({tuple(n*x for x in e):c**n})
        out=P(1)
        for _ in range(n): out=out*self
        return out
    def __eq__(self, other): return self.terms==coerce(other).terms
    def diagonal(self):
        # W=r/D: D^a W^b V^c E^d r^e -> D^(a-b) V^c E^d r^(e+b)
        out={}
        for (a,b,c,d,e),coeff in self.terms.items():
            key=(a-b,0,c,d,e+b)
            out[key]=out.get(key,Q(0))+coeff
        return P(out)

def coerce(x): return x if isinstance(x,P) else P(x)
def variable(i):
    e=[0]*5
    e[i]=1
    return P({tuple(e):Q(1)})
D,W,V,E,r=(variable(i) for i in range(5))

# N=(1-D)(1-E)H, computed directly by clearing the source denominators.
source=(1-V*W)*(1-E)+E*(1-W)*((1-r)+W*(1-V))-D*(1-W)*((1-V)+(r**-1-1)*W*V)
expanded=1-D+D*W+V*(D-W-r**-1*D*W+(r**-1-1)*D*W**2)+E*(-r+r*W-(1-V)*W**2)
require(source==expanded, "exact check 61")
# The diagonal simplification retains V independently, then V=r^3 is inserted analytically.
diagonal=1-D+r+V*(D-1-r*W)+E*(-r+r*W-(1-V)*W**2)
require(source.diagonal()==diagonal.diagonal(), "exact check 64")
# Exact leading cancellation after multiplying by 1-DW and clearing 1-D.
require((1-D*W)*(1-D+D*W)-(1-D)==D**2*W*(1-W), "exact check 66")
# Exact remainder after subtracting H^0=1+DW/(1-D), clearing denominators.
remainder=V*(D-W-r**-1*D*W+(r**-1-1)*D*W**2)+E*((1-r)-D+D*W+r*W-(1-V)*W**2)
require(source-(1-D+D*W)*(1-E)==remainder, "exact check 69")
# A missing zeta(xi+w) extraction leaves a genuine linear DW term.
require((1-D+D*W)-(1-D)==D*W, "exact check 71")
require((1-D*W)*(1-D+D*W)-(1-D)!=D*W, "exact check 72")
# Uniform exact rational margin for exterior Q>=3.
margin_bound=Q(29,405)+Q(46,243)
require(margin_bound==Q(317,1215)<Q(3,4), "exact check 75")
print(json.dumps({"status":"PASS", "proof_sha256":sha256(Path(__file__).with_name("DIAGONAL_FINITE_PART.md").read_bytes()).hexdigest(), "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(), "identities":["source expansion", "diagonal specialization", "Euler leading cancellation", "exact remainder"],
    "strict_margin":str(Q(3,4)-margin_bound),
    "negative_control":"bare diagonal misses the zeta(xi+w) pole",
    "not_verified":["primary-source import", "full Poisson identity", "signed finite-part extraction"]}, indent=2))

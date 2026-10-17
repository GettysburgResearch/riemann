#!/usr/bin/env python3
"""Exact finite algebra checks; no imported analytic theorem is certified."""
from fractions import Fraction as Q
import json
from hashlib import sha256
from pathlib import Path

def require(condition, message):
    if not condition:
        raise ValueError(message)


checks = 0
for sigma in (Q(1,2), Q(3,5), Q(3,4), Q(9,10)):
    for delta in (Q(1,100), Q(1,1000)):
        h=Q(1,2)+delta
        theta=(sigma-Q(1,2))/h
        p=2/(1-theta)
        dual=2/(1+theta)
        require(1/p+1/dual == 1, "exact check 13")
        require(1/p-(1-sigma)==delta*(2*sigma-1)/(1+2*delta), "exact check 14")
        for nu in (Q(0),Q(1,3),Q(1,2),Q(7,10),Q(1)):
            require(nu*(1-1/p)+1/p == nu+(1-nu)/p, "exact check 16")
            checks+=1
for y in (Q(1,10),Q(1,4),Q(2,5),Q(1,2)):
    for nu in (Q(0),Q(1,3),Q(1,2),Q(7,10),Q(1)):
        reflected=Q(1,2)-y+nu*(1-y)+y
        target=Q(1,2)+nu*(1-y)
        convexity=nu+(1-y)/2
        require(reflected==target, "exact check 23")
        require(convexity-target==y*(nu-Q(1,2)), "exact check 24")
        require((target<convexity)==(nu>Q(1,2)), "exact check 25")
        for a in (Q(449,1000),Q(23,50),Q(1,2)):
            h=1-a
            x=Q(4,5)
            z=Q(2,5)
            E=a/2+x-1+h*z+a*(y-1)
            R=target-z
            require(E+h*R==x-Q(1,2)+(h*nu-a)*(1-y), "exact check 32")
            checks+=1
# Hölder's subset exponent is sharp for arbitrary finite positive arrays.
# This is a negative control for an unjustified independence improvement,
# not an assertion that this array is realized by L-functions.
U=256
selected=16
p=4
value=2
require(selected*value**p==U, "exact check 41")
require(selected*value==32, "exact check 42")
require((selected*value)**8==U**5, "exact check 43")  # exponent nu*sigma+1-sigma=5/8
# Omitting the primitive conductor factor would lose this positive exponent.
y=Q(1,4)
nu=Q(7,10)
wrong_without_conductor=nu*(1-y)+y
correct=Q(1,2)+nu*(1-y)
require(correct-wrong_without_conductor==Q(1,2)-y>0, "exact check 49")
print(json.dumps({"status":"PASS", "proof_sha256":sha256(Path(__file__).with_name("INTERPOLATED_NUMERATOR.md").read_bytes()).hexdigest(), "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(), "rational_instances":checks,
    "negative_controls":["dependent-subset Holder saturation", "omitted conductor factor"],
    "not_verified":["actual central family mean", "primitive functional equation", "full contour comparison"]}, indent=2))

#!/usr/bin/env python3
"""Exact independent algebra replay for Formalization Reviewer C cross-review.

No floating-point evaluation is used. SymPy reduces each polynomial/rational
identity to an exact zero numerator and checks every finite firewall witness.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

def require_zero(name: str, expr) -> None:
    reduced = sp.factor(sp.together(expr))
    if reduced != 0:
        raise SystemExit(f"{name}: FAIL: {reduced}")
    RESULTS[name] = "PASS"

RESULTS: dict[str, object] = {}

a,b,c,d,e,f,x,y,z = sp.symbols("a b c d e f x y z")
det3 = a*d*f + 2*b*c*e - a*e**2 - d*c**2 - f*b**2
quad3 = a*x**2 + 2*b*x*y + 2*c*x*z + d*y**2 + 2*e*y*z + f*z**2
minor = a*d-b**2
require_zero("ldl3_identity", a*minor*quad3 - (minor*(a*x+b*y+c*z)**2 + (minor*y+(a*e-b*c)*z)**2 + a*det3*z**2))

x1,x2,x3,p1,p2,p3 = sp.symbols("x1 x2 x3 p1 p2 p3")
def entry(x,p,y,q):
    return (x*p+y*q)/(x+y)
pick2 = p1*p2-entry(x1,p1,x2,p2)**2
require_zero("two_point_pick_identity", pick2 + ((p1-p2)*(x1**2*p1-x2**2*p2))/(x1+x2)**2)

def det3f(a,b,c,d,e,f):
    return a*d*f+2*b*c*e-a*e**2-d*c**2-f*b**2
pick3 = det3f(p1, entry(x1,p1,x2,p2), entry(x1,p1,x3,p3), p2, entry(x2,p2,x3,p3), p3)
t1,t2,t3 = x1**2,x2**2,x3**2
delta = (t2-t1)*(t3-t1)*(t3-t2)
def dd(t1,t2,t3,y1,y2,y3):
    return y1/((t1-t2)*(t1-t3)) + y2/((t2-t1)*(t2-t3)) + y3/((t3-t1)*(t3-t2))
den = (x1+x2)**2*(x1+x3)**2*(x2+x3)**2
rhs = p1*p2*p3*delta**2/den * dd(t1,t2,t3,1/p1,1/p2,1/p3) * dd(t1,t2,t3,t1*p1,t2*p2,t3*p3)
require_zero("three_node_pick_determinant_identity", pick3-rhs)

fv,ff,fs,gv,gf,gs = sp.symbols("fv ff fs gv gf gs")
ef = fv*fs-2*ff**2
eg = gv*gs-2*gf**2
cross = fv*gs+gv*fs-4*ff*gf
require_zero("reciprocal_concavity_cross_square", fv*gv*cross - (fv**2*eg+gv**2*ef+2*(gv*ff-fv*gf)**2))

m,U,B = sp.symbols("m U B")
q0 = 4*m*U/(U**2+B**2)
q1 = 4*m*(B**2-U**2)/(U**2+B**2)**2
q2 = 8*m*U*(U**2-3*B**2)/(U**2+B**2)**3
require_zero("offline_orbit_defect", q0*q2-2*q1**2 + 32*m**2*B**2/(U**2+B**2)**3)

assert sp.Rational(3,5)**2 + sp.Rational(3,5)**2 <= 1
assert (sp.Rational(3,5)+sp.Rational(3,5))**2 > 1
assert 2*1*(-1) == -2
assert (-1)**2 + 1 >= 0 and -1 < 0
assert 1**2 + 2*2*1*(-1) + 1*(-1)**2 == -2
assert 1**2-0**2 > 0 and 1**2-2**2 < 0
RESULTS["finite_firewalls"] = "PASS"
RESULTS["floating_point_used"] = False
RESULTS["rh_proved"] = False
Path(__file__).with_name("SYMBOLIC_RESULTS.json").write_text(json.dumps(RESULTS, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("PASS_B_CROSS_C_SYMBOLIC_REPLAY", len(RESULTS)-2, "checks")

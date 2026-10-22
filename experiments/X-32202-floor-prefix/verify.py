#!/usr/bin/env python3
"""Exact symbolic certificate for L-32204 floor-prefix positivity.

This script proves an all-parameter polynomial statement.  It is not a finite
scan in N,q,M.  SymPy is used only as an exact polynomial ring / expansion
engine over Q.
"""

import hashlib
import json
import sympy as sp


def nonnegative_coefficients(expr, variables):
    poly = sp.Poly(sp.expand(expr), *variables, domain=sp.QQ)
    bad = [(mon, str(coeff)) for mon, coeff in poly.terms() if coeff < 0]
    return len(poly.terms()), bad


a, b, q, r, s = sp.symbols("a b q r s", integer=True, nonnegative=True)
A, u, v, w = sp.symbols("A u v w", integer=True, nonnegative=True)

N = a*q + r
M = (a+b)*q + s
AN = q*a*(a-1)/2 + a*(r+1)
AM = q*(a+b)*(a+b-1)/2 + (a+b)*(s+1)

# P = 2 N(N+1) K_(N,q)(M).
P = sp.expand(2*((M-N)*N*(N+1) - AM*N*(N+1) + M*(M+1)*AN))

b2 = sp.factor(sp.Poly(P, b).coeff_monomial(b**2))
expected_b2 = -q*(a*q*(q-1) + r*(r+1))
assert sp.simplify(b2 - expected_b2) == 0

certificates = {}

# A: b=0, s>r.
PA = sp.expand(P.subs({b: 0, a: A+1, s: r+1+u, q: r+u+2+w}))
certificates["A"] = nonnegative_coefficients(PA, (A, r, u, w))

# B: b=1, s<=r.
PB = sp.expand(P.subs({b: 1, a: A+1, r: s+v, q: s+v+1+w}))
certificates["B"] = nonnegative_coefficients(PB, (A, s, v, w))

# C: b=a-1, s>2r, a>=2.  a=1 belongs to A.
PC = sp.expand(P.subs({a: A+2, b: A+1, s: 2*r+1+u, q: 2*r+u+2+w}))
certificates["C"] = nonnegative_coefficients(PC, (A, r, u, w))

# D: b=a and 2r-q<s<=2r.
# Put u=2r-s, q=u+1+w, v=q-1-s.  Then 0<=v<=L=u+w and
# r=u+(w-v)/2.  Clear the half-integral parametrization by multiplying by 4.
PD = sp.expand(4*P.subs({
    a: A+1,
    b: A+1,
    q: u+1+w,
    s: u+w-v,
    r: u+(w-v)/2,
}))
poly_v = sp.Poly(PD, v, domain=sp.QQ[A,u,w])
coeff = [sp.expand(poly_v.coeff_monomial(v**i)) for i in range(4)]
L = u+w

# Degree-three Bernstein coefficients on [0,L].
B0 = coeff[0]
B1 = sp.expand(coeff[0] + coeff[1]*L/3)
B2 = sp.expand(coeff[0] + 2*coeff[1]*L/3 + coeff[2]*L**2/3)
B3 = sp.expand(sum(coeff[i]*L**i for i in range(4)))

certificates["D0"] = nonnegative_coefficients(B0, (A, u, w))
certificates["D1"] = nonnegative_coefficients(3*B1, (A, u, w))
certificates["D2"] = nonnegative_coefficients(3*B2, (A, u, w))
certificates["D3"] = nonnegative_coefficients(B3, (A, u, w))

# E: b=a+1, s<=2r-q.
PE = sp.expand(P.subs({
    a: A+1,
    b: A+2,
    q: u+2*v+2+w,
    r: u+v+1+w,
    s: w,
}))
certificates["E"] = nonnegative_coefficients(PE, (A, u, v, w))

for name, (_, bad) in certificates.items():
    if bad:
        raise AssertionError(f"negative coefficient in {name}: {bad[:4]}")

summary = {
    "classification": "EXACT_ALL_PARAMETER_FLOOR_PREFIX_POSITIVITY_VERIFIED",
    "b2_coefficient": str(b2),
    "certificates": {
        name: {"monomials": count, "negative_coefficients": len(bad)}
        for name, (count, bad) in certificates.items()
    },
}
payload = json.dumps(summary, sort_keys=True, separators=(",", ":"))
summary["proof_object_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
print(json.dumps(summary, indent=2, sort_keys=True))

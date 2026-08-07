#!/usr/bin/env python3
from fractions import Fraction as F
import json, hashlib

# Complex numbers as (real, imag), exact Fractions.
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0], -z[1])
def inv(z):
    d=z[0]*z[0]+z[1]*z[1]
    return (z[0]/d, -z[1]/d)
def div(z,w): return mul(z,inv(w))
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def sq(z): return mul(z,z)

def canonical(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

# Synthetic off-line centered zero Omega=3+i and two distinct limiting frequencies 1,2.
Omega=(F(3),F(1))
O2=sq(Omega)

def r(a):
    return div(Omega, sub(O2,(F(a*a),F(0))))

r1,r2=r(1),r(2)
# q=Im(r1 conjugate(r2))
prod=mul(r1,conj(r2))
q=prod[1]
# Choose a harmless common complex scalar S=2+i; determinant must remain -|S|^4 q^2.
S=(F(2),F(1))
u1,u2=mul(S,r1),mul(S,r2)
# Matrix Re(u u^T)
m11=sq(u1)[0]
m22=sq(u2)[0]
m12=mul(u1,u2)[0]
det=m11*m22-m12*m12
expected=-(S[0]*S[0]+S[1]*S[1])**2*q*q
trace=m11+m22
verdict=(q!=0 and det==expected and det<0)
result={
  'schema':'riemann.x19842-offline-two-mode.result.v1',
  'verdict':'PASS_EXACT_INDEFINITE_TWO_MODE' if verdict else 'FAIL',
  'Omega':['3','1'],
  'frequencies':['1','2'],
  'imag_cross':str(q),
  'matrix':[[str(m11),str(m12)],[str(m12),str(m22)]],
  'trace':str(trace),
  'determinant':str(det),
  'expected_determinant':str(expected),
}
result['proof_object_sha256']=canonical(result)
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if verdict else 1)

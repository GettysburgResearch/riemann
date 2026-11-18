#!/usr/bin/env python3
"""Exact fourth-cumulant check independent of the matrix-series inverse code."""
import hashlib
import json
from fractions import Fraction as Q
from itertools import product
from math import factorial, lcm, prod
from pathlib import Path
import sympy as sp

N=40
n=N+1
frequencies=(9,10,11)
den=lcm(*(2*k for k in frequencies))
laurent={sign*k:-den//(2*k) for k in frequencies for sign in (-1,1)}
linear=sp.Matrix([2*j-n+1 for j in range(n)])
normal=int((linear.T*linear)[0])
assert normal % n == 0
projection_numerator=normal*sp.eye(n)-(normal//n)*sp.ones(n)-linear*linear.T
assert projection_numerator**2==normal*projection_numerator
polynomial={0:1}
compressed=[]
for degree in range(1,5):
    next_poly={}
    for i,a in polynomial.items():
        for j,b in laurent.items():next_poly[i+j]=next_poly.get(i+j,0)+a*b
    polynomial=next_poly
    toeplitz=sp.Matrix(n,n,lambda i,j:polynomial.get(i-j,0))
    compressed.append(projection_numerator*toeplitz)
B1,B2,B3,B4=compressed
tr=lambda m:int(sp.trace(m))
square=B1*B1
k1=Q(tr(B1),normal*den)
k2=Q(normal*tr(B2)-tr(square),normal**2*den**2)
k3=Q(normal**2*tr(B3)-3*normal*tr(B1*B2)+2*tr(square*B1),normal**3*den**3)
k4=Q(normal**3*tr(B4)-4*normal**2*tr(B1*B3)-3*normal**2*tr(B2*B2)
     +12*normal*tr(square*B2)-6*tr(square*square),normal**4*den**4)
H=sum((Q(1,k) for k in frequencies),Q())
mean=k1-H
raw4=k4+4*mean*k3+3*k2*k2+6*mean*mean*k2+mean**4
assert raw4==Q(483952530159221,9042666599736000)

# Compute the scalar surrogate separately using Gaussian raw moments and a
# fourth-degree polynomial, without the complementary inverse matrix.
d=Q(len(frequencies),n)
q=Q(2*sum(k*k for k in frequencies),n**3)
eps=Q(1,n*n)
prefactor=[Q(1),(-4*d+q+2*eps*d)/(1-eps),
           (6*d*d-q*d-eps*d*d)/(1-eps),-4*d**3/(1-eps),d**4/(1-eps)]
gaussian=[Q(1),H]
for j in range(1,4):gaussian.append(H*gaussian[j]+j*(H/2)*gaussian[j-1])
formal4=sum((Q(factorial(4),factorial(4-j))*prefactor[j]*gaussian[4-j]
             for j in range(5)),Q())
counts={'below':0,'equal':0,'above':0}
crossing=Q()
for word in product(frequencies,repeat=4):
    s=sum(word)
    counts['below' if s<n else 'equal' if s==n else 'above']+=1
    if s>n:crossing+=Q(2*(s-n)*(s*s+n*s-n*n+1),n*(n*n-1)*prod(word))
prediction=-crossing/8
assert raw4-formal4==prediction==Q(-3384187,302541624000)
print(json.dumps(dict(
    scope='Exact finite rooted CUE only; fourth cumulant from projection traces, independent of the matrix-series inverse recurrence.',
    N=N,mode_dimension=n,frequencies=frequencies,
    direct_fourth=str(raw4),formal_fourth=str(formal4),difference=str(prediction),
    tuple_counts=counts,free_cumulants=[str(x) for x in (k1,k2,k3,k4)],
    code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
),indent=2))

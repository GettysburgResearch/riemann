#!/usr/bin/env python3
"""Exact finite Petrov/CUE factor comparison; no asymptotic or RH input."""
import hashlib
import json
from pathlib import Path
import sympy as s

z = s.Symbol('z')
n, m = 5, 3
X = s.zeros(n, m)
for j in range(m):
    for i, c in enumerate((1, -2, 1)):
        X[j+i, j] = c
q = s.Rational(1, 4)
# C=T(exp(-z w^-2/4))X. The upper factor preserves the n modes.
U = s.eye(n)
for i in range(n):
    for j in range(i+1, n):
        if (j-i) % 2 == 0:
            h = (j-i)//2
            U[i,j] = (-z*q)**h / s.factorial(h)
C = U*X
norm = (X.T*X).det()
gram = s.series((C.T*C).det()/norm, z, 0, 3).removeO()
# T(exp(zF)) through degree two, F=-(w^2+w^-2)/4.
A = s.eye(n)
for i in range(n):
    for j in range(n):
        d = i-j
        if abs(d) == 2:
            A[i,j] -= z*q
        if d == 0:
            A[i,j] += z*z*q*q
        elif abs(d) == 4:
            A[i,j] += z*z*q*q/2
free = s.series((X.T*A*X).det()/norm, z, 0, 3).removeO()
ambient = s.series(A.det(), z, 0, 3).removeO()
complement = s.series(free/ambient, z, 0, 3).removeO()
assert gram == 1+z/4+s.Rational(33,800)*z*z
assert complement == 1+z/4-s.Rational(3,200)*z*z
gap = s.expand(gram-complement).coeff(z, 2)
assert gap == s.Rational(9,160)
B = s.Matrix([[1-z/4,-2,1],[z/2,1-z/4,-2],
              [z*z/32-z/4,z/2,1-z/4]])
chart = s.factor(B.det())
assert s.expand(chart + (z**3+4*z*z-64*z-128)/128) == 0
assert chart.subs(z,0)==1 and chart.subs(z,8)==-1
source = Path(__file__).resolve()
result = dict(status='PASS', scope='finite exact rational calculation only',
              N=4, J=2, ambient_n=5, frequency=2,
              normalized_gram=str(gram), complement=str(complement),
              quadratic_gap=str(gap), optional_chart_determinant=str(chart),
              code_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
target = source.parents[1]/'results/director_petrov_quadratic_round13.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

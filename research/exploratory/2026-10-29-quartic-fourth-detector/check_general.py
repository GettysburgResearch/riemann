#!/usr/bin/env python3
"""Exact scalar quartic/prime-order fourth-witness calculations only."""
from fractions import Fraction as F
import sympy as s
n=s.symbols('n', positive=True)
c=F(1,10)+s.Rational(2,3)/n
u=(3*n-10)/(30*(n-2))
assert s.factor(1/n+u*(1-2/n)-c)==0
R=s.Rational(1,2)+s.Rational(2,3)/n
assert s.factor(c+s.Rational(2,5)-R)==0
assert s.factor(1-c+(2/n-s.Rational(3,5))*s.Rational(2,3)-R)==0
c=s.Rational(4,3)/n;u=1/(3*(n-2))
assert s.factor(1/n+u*(1-2/n)-c)==0
assert s.factor(1-c+(2/n-s.Rational(3,5))*s.Rational(2,3)-s.Rational(3,5))==0
D=(12*n*n-38*n+5)/(21*n*n-80*n+50)
assert s.factor((s.Rational(4,3)*D-s.Rational(3,5))-(51*n*n-40*n-350)/(15*(21*n*n-80*n+50)))==0
for N in range(4,101):
 U=F(3*N-10,30*(N-2)) if N<=6 else F(1,3*(N-2))
 C=F(1,N)+U*(1-F(2,N)); RR=F(1,2)+F(2,3*N) if N<=6 else F(3,5)
 assert 0<U<F(1,2)
 # On s in [2/3,1], the decreasing first and third faces peak at 2/3;
 # the increasing second peaks at 1.
 assert max(F(3,5),C+F(2,5),1-C+(F(2,N)-F(3,5))*F(2,3))==RR
 Dn=F(12*N*N-38*N+5,21*N*N-80*N+50)
 assert (1+(N-2)*U)*Dn>RR
 if N in (4,5,6,7): print('n',N,'u',U,'c',C,'R',RR,'natural comparator',(1+(N-2)*U)*Dn)
print('Scalar identities and sampled feasibility checked; analytic inputs untested.')

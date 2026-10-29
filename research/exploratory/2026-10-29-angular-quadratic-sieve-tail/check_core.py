#!/usr/bin/env python3
"""Exact arithmetic for fixed-k quadratic-prefix physical core bounds."""
from fractions import Fraction as F
import sympy as s
p,d,k,b,g,C=s.symbols('p d k b g C')
pref=1-p+d-k+(2*p-1+k-2*d-b)/6
D=p-d-g
q0=b+k
q1=s.Rational(11,7)*b+s.Rational(12,7)*k+s.Rational(4,7)*g-D/7
q2=s.Rational(5,4)*b+s.Rational(3,2)*k+g/2
exp0=s.factor((pref+q0).subs(p,s.Rational(6,5)))
exp1=s.factor((pref+q1).subs(p,s.Rational(6,5)))
exp2=s.factor((pref+q2).subs(p,s.Rational(6,5)))
assert s.expand(exp0-(s.Rational(1,30)+s.Rational(2,3)*d+k/6+s.Rational(5,6)*b))==0
assert s.expand(exp1-(-s.Rational(29,210)+s.Rational(17,21)*d+s.Rational(37,42)*k+s.Rational(59,42)*b+s.Rational(5,7)*g))==0
assert s.expand(exp2-(s.Rational(1,30)+s.Rational(2,3)*d+s.Rational(2,3)*k+s.Rational(13,12)*b+g/2))==0
edge={d:C,k:0,g:0}
assert s.factor(exp0.subs(edge)-(s.Rational(1,30)+s.Rational(2,3)*C+s.Rational(5,6)*b))==0
assert s.factor(exp1.subs(edge)-(-s.Rational(29,210)+s.Rational(17,21)*C+s.Rational(59,42)*b))==0
assert s.factor(exp2.subs(edge)-(s.Rational(1,30)+s.Rational(2,3)*C+s.Rational(13,12)*b))==0
# On d+g+6k/5<=C, k<=d, substituting g=C-d-6k/5
# yields positive d,k coefficients; after d=C-6k/5, both
# expressions decrease in k, so the maximum is d=C,k=g=0.
for expression in (exp1,exp2):
 edge1=s.factor(expression.subs(g,C-d-s.Rational(6,5)*k).subs(d,C-s.Rational(6,5)*k))
 assert s.diff(edge1,k)<0
assert -F(1,2)+F(2,7)+F(1,14)==-F(1,7)
assert -F(1,2)+F(1,4)==-F(1,4)
for target,c,b1,b2 in [(F(21,20),F(7,50),F(2257,2950),F(277,325)),(F(19949123,18750000),F(1925877,15625000),F(723364487,921875000),F(88917107,101562500))]:
 assert -F(29,210)+F(17,21)*c+F(59,42)*b1==target
 assert F(1,30)+F(2,3)*c+F(13,12)*b2==target
 assert b1<b2
 assert F(1,30)+F(2,3)*c+F(5,6)*b1<target
 print('target',target,'limiting core b',b1,'decimal',float(b1),'second-face threshold',b2)
print('Fixed-k quadratic-sieve cube-tail core arithmetic passed.')

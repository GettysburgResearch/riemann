#!/usr/bin/env python3
"""Exact algebra for stated source bounds, not a proof of analytic inputs."""
import sympy as s
from fractions import Fraction as F
d,k,g=s.symbols('d k g')
L1=s.Rational(7,30)-d/3-5*k/6
L2=s.Rational(11,10)-3*d-k/2
L3=s.Rational(8,25)-3*d/5-4*k/5
assert s.factor((L2-L1).subs(k,d-s.Rational(1,5))-(s.Rational(4,5)-7*d/3))==0
assert s.factor((L2-L3).subs(k,d-s.Rational(1,5))-(s.Rational(18,25)-21*d/10))==0
assert s.factor(L2.subs(k,d-s.Rational(1,5))-(s.Rational(12,10)-s.Rational(7,2)*d))==0
assert s.factor((1-k)/2-L2-3*(d-s.Rational(1,5)))==0
assert s.factor(L2.subs(k,s.Rational(11,5)-6*d))==0
assert s.factor(L2.subs(k,d)-(s.Rational(11,10)-s.Rational(7,2)*d))==0
M1=s.Rational(11,30)-d-k/6
M2=s.Rational(7,10)-d-5*k/2
M3=s.Rational(2,5)-d-2*k/5
assert s.factor(M1-M2-(7*k-1)/3)==0
assert s.factor(M1-M3-(7*k-1)/30)==0
assert s.factor(M2.subs(k,d-s.Rational(1,5))-L2.subs(k,d-s.Rational(1,5)))==0
vertices=[(s.Rational(1,5),s.Rational(0)),(s.Rational(1,5),s.Rational(1,5)),
 (s.Rational(11,35),s.Rational(11,35)),(s.Rational(12,35),s.Rational(1,7))]
for m in (M1,M2,M3):
 assert all(s.factor((L2-m).subs({d:D,k:K}))>=0 for D,K in vertices)
assert s.solve(s.Eq(s.Rational(12,10)-s.Rational(7,2)*d,g),d)[0]==(12-10*g)/35
assert [((F(12)-10*G)/35) for G in [F(0),F(1,10),F(1,4),F(1,2)]]==[F(12,35),F(11,35),F(19,70),F(1,5)]
# Test interior wedge samples; theta and generic do not claim those points.
for D in [F(1,5),F(1,4),F(3,10),F(11,35),F(1,3)]:
 lo=D-F(1,5);hi=min(D,F(11,5)-6*D)
 if lo>=hi: continue
 K=(lo+hi)/2
 vals=[F(7,30)-D/3-5*K/6,F(11,10)-3*D-K/2,F(8,25)-3*D/5-4*K/5]
 assert vals[1]>=max(vals[0],vals[2],0)
 assert vals[1]<=F(6,5)-D
print('Source-bound algebra, active face and fixed-g thresholds verified.')
print('Analytic inputs, source normalizations and dyadic feasibility are not checked here.')

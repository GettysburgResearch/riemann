#!/usr/bin/env python3
"""Exact physical monomial, e-mask and residual-core arithmetic."""
import sympy as s
from fractions import Fraction as F
d,k,g,b,C=s.symbols('d k g b C', nonnegative=True)
p=s.Rational(6,5)
# H exponent is 7/5+k-2d; divide physical factor by B^(1/6).
pref=s.Rational(1,30)+2*d/3-5*k/6-b/6
D=p-d-g; FF=g+k
rows=[(F(19,14),F(8,7),F(4,7),F(-1,7)),(F(9,8),F(1),F(1,2),F(0)),(F(27,20),F(4,5),F(2,5),F(-1,5)),(F(1),F(1,2),F(1,4),F(0)),(F(18,13),F(14,13),F(7,13),F(-2,13)),(F(25,22),F(10,11),F(5,11),F(0))]
core=[(-F(29,210),F(17,21),F(25,21)),(F(1,30),F(2,3),F(23,24)),(-F(31,150),F(13,15),F(71,60)),(F(1,30),F(2,3),F(5,6)),(-F(59,390),F(32,39),F(95,78)),(F(1,30),F(2,3),F(32,33))]
e_expected=[-F(1,7),-F(1,4),-F(1,5),-F(3,8),-F(2,13),-F(3,11)]
for (B,K,FFpow,Dpow),(c0,c1,c2),em in zip(rows,core,e_expected):
 expr=s.expand(pref+s.Rational(B.numerator,B.denominator)*b+s.Rational(K.numerator,K.denominator)*k+s.Rational(FFpow.numerator,FFpow.denominator)*FF+s.Rational(Dpow.numerator,Dpow.denominator)*D)
 assert s.factor(expr.subs({d:C,k:0,g:0})-(s.Rational(c0.numerator,c0.denominator)+s.Rational(c1.numerator,c1.denominator)*C+s.Rational(c2.numerator,c2.denominator)*b))==0
 assert F(-1,2)+(FFpow-Dpow)/2==em
 # Maximizing each expression over g<=C-d-6k/5, k<=d
 # is bounded by value at d=C,k=g=0.
 assert s.diff(expr,g)>=0
 edge=s.expand(expr.subs(g,C-d-s.Rational(6,5)*k))
 assert s.diff(edge,d)>=0
 edge=s.expand(edge.subs(d,C-s.Rational(6,5)*k))
 assert s.diff(edge,k)<=0
for target,Cv,bv in [(F(21,20),F(7,50),F(223,250)),(F(19949123,18750000),F(1925877,15625000),F(1357811867,1484375000))]:
 vals=[x+y*Cv+z*bv for x,y,z in core]
 assert vals[4]==target and all(val<=target for val in vals)
 assert F(17,10)-4*Cv-bv>0
 print('target',target,'cutoff',bv,'float',float(bv),'e-guard margin',F(17,10)-4*Cv-bv)
print('All six physical faces, e powers and source guards passed.')

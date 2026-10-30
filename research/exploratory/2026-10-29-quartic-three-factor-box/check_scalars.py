#!/usr/bin/env python3
"""Exact scalar box/exponent checks; analytic sieve/detector inputs untested."""
import sympy as s
R=s.Rational;b=R(1,100);u=R(19,600);v=R(23,24);t=R(77,75)
assert b+u+v==1 and u<v
c=R(1,4)+3*b/4+u/2;d=R(3,4)+b/4-u/2
assert c==R(41,150) and d==R(221,300)
lo=t-R(1,2);bound=R(171,250)
assert lo==R(79,150)
assert 1-R(3,5)*lo==bound and d-lo/10==bound
assert c+R(2,5)*t==bound
assert b+(1-b)*R(13,25)==R(328,625)
assert bound/(3-b)==R(342,1495)
B,U,T=s.symbols('B U T');C=R(1,4)+3*B/4+U/2;D=R(3,4)+B/4-U/2
Ucurve=R(1,30)-B/6;Tcurve=R(31,30)-2*B/3;rcurve=R(17,25)+2*B/5
assert s.factor(C.subs(U,Ucurve)-(R(4,15)+2*B/3))==0
assert s.factor(D.subs(U,Ucurve)-(R(11,15)+B/3))==0
assert s.factor(1-R(3,5)*(Tcurve-R(1,2))-rcurve)==0
assert s.factor(D.subs(U,Ucurve)-(Tcurve-R(1,2))/10-rcurve)==0
assert s.factor(C.subs(U,Ucurve)+R(2,5)*Tcurve-rcurve)==0
assert s.factor(s.diff(rcurve/(3-B),B)-R(47,25)/(3-B)**2)==0
assert Ucurve.subs(B,R(1,20))==R(1,40) and Tcurve.subs(B,R(1,20))==1
assert (1-B-Ucurve).subs(B,R(1,20))==R(37,40)
assert rcurve.subs(B,R(1,20))==R(7,10)
assert (B+(1-B)*R(13,25)).subs(B,R(1,20))==R(68,125)
assert (rcurve/(3-B)).subs(B,R(1,20))==R(14,59)
r4=R(2,3)+2*B/3
assert s.factor(C.subs(U,Ucurve)+R(2,5)-r4)==0
assert s.factor((D.subs(U,Ucurve)-R(1,15))-(R(2,3)+B/3))==0
assert r4.subs(B,R(1,100))==R(101,150)
assert (r4/(3-B)).subs(B,R(1,100))==R(202,897)
assert r4.subs(B,R(1,20))==rcurve.subs(B,R(1,20))==R(7,10)
upper=s.factor((R(17,25)-C)/(R(2,5)))
lower=s.factor(R(10)*(D+R(1,20)-R(17,25)))
assert s.factor(upper-(R(43,40)-15*B/8-5*U/4))==0
assert s.factor(lower-(R(6,5)+5*B/2-5*U))==0
assert s.factor(upper-lower-(15*U/4-1/s.Integer(8)-35*B/8))==0
assert s.factor(C+R(2,5)*R(31,30)-R(17,25)-(U/2+3*B/4-R(1,60)))==0
print('Three-factor example and relaxed-minimax scalar inequalities verified.')
print('Source sieves, detector and quotient/field inputs are not proved here.')

#!/usr/bin/env python3
import sympy as s
D=s.symbols('D');sigma=s.symbols('sigma')
den=18*D**2-39*D+5
t=-2*(15*D-2)/den;r=-(42*D-5)/(2*den);m=t-r
f2=lambda x:s.Rational(5,6)+(s.Rational(1,3)-D)*x
f3=lambda x:s.Rational(1,3)+(s.Rational(5,6)-D)*x
h=1-2*D*m
R=(36*D**2-42*D+5)/den
assert s.factor(f2(r)-R)==0 and s.factor(f3(t)-R)==0 and s.factor(h-R)==0
cases=[(s.Rational(4,5),s.Rational(181,298)),(s.Rational(4369347,5000000),s.Rational(19615469784638,44055542392319))]
for sig,expected in cases:
 d=2*sig-1; T=t.subs(D,d);r0=r.subs(D,d);m0=m.subs(D,d)
 assert s.simplify(R.subs(D,d)-expected)==0
 assert 1<T<s.Rational(3,2) and T-s.Rational(1,2)<r0<1 and 0<m0<s.Rational(1,2)
 assert s.Rational(1,3)<d<s.Rational(5,6)
 print('sigma',sig,'t',T,'r0',r0,'m0',m0,'R',expected)
A=-den
B=-18*D**2+30*D-5
assert s.factor(t-1-(3*D-1)*(6*D-1)/A)==0
assert s.factor(s.Rational(3,2)-t-(-54*D**2+57*D-7)/(2*A))==0
assert s.factor(1-r-(5-6*D)*(6*D-1)/(2*A))==0
assert s.factor(s.Rational(1,2)-m-(-18*D**2+21*D-2)/(2*A))==0
old=s.Rational(1,3)+9*(s.Rational(5,6)-D)/(11-6*D)
assert s.factor(old-R-(3*D-1)*(5-6*D)*(6*D+1)/(6*(11-6*D)*A))==0
sig=(1+D)/2
Df=1-D*(36*D-(6*sig-2)*6+3)/(36*D*(3-2*sig)-24*sig+2)
assert s.factor(Df-R-3*D*(3*D-1)*(5-6*D)*(6*D-1)/(2*A*B))==0
print('Exact continuum faces, ranges and comparisons passed.')

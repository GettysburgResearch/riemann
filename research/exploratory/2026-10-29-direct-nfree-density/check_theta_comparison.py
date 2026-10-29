#!/usr/bin/env python3
"""Check exact four-face endpoint and named-source comparison identities."""
import sympy as s
n,z=s.symbols('n z')
for sigma in (s.Rational(4369347,5000000),s.Rational(4,5)):
 delta=2*sigma-1
 t=3*(n-3)/(n*(3-delta)-7);L=2*t/3
 f0=lambda x:1-delta*x
 fd=lambda x:(1-delta)*x
 f2=lambda x:1-1/n+(2/n-delta)*x
 f3=lambda x:2/n+(1-1/n-delta)*x
 R=2/n+3*(n-3)*(1-1/n-delta)/(n*(3-delta)-7)
 assert s.factor(f2(L)-R)==0 and s.factor(f3(t)-R)==0
 x=s.symbols('x')
 assert s.factor(f2(x)-f0(x)-(2*x-1)/n)==0
 assert s.factor(f3(x)-fd(x)-(2-x)/n)==0
 assert s.factor(f2(x)-f3(x)-(1-3/n)*(1-x))==0
 D=1-delta*(delta*n**2-(6*sigma-2)*n+3)/(delta*(3-2*sigma)*n**2-4*sigma*n+2)
 if sigma==s.Rational(4369347,5000000):
  assert s.factor(R-(1891959*n**2-1914571*n-12500000)/(7*n*(804379*n-2500000)))==0
  Q=1869347*n**2-9977388*n+12500000
  den=7*n*(804379*n-2500000)*(5852276793591*n**2-21846735000000*n+12500000000000)
  assert s.factor(D-R-(630653*n-2500000)*(1869347*n-5000000)*Q/den)==0
  assert all(c>0 for c in s.Poly(s.expand(Q.subs(n,z+4)),z).all_coeffs())
  assert s.limit(R,n,s.oo)==s.Rational(1891959,5630653)
  assert s.limit(D,n,s.oo)==s.Rational(1261306,3130653)
 else:
  assert s.factor(R-(6*n*n-9*n-25)/(n*(12*n-35)))==0
  gap=(2*n-5)*(3*n-10)*(3*n*n-17*n+25)/(n*(12*n-35)*(21*n*n-80*n+50))
  assert s.factor(D-R-gap)==0
  previous=(3*n*n-10)/(n*(6*n-10))
  assert s.factor(previous-R-(3*n-10)**2/(2*n*(3*n-5)*(12*n-35)))==0
  assert all(c>0 for c in s.Poly((3*n*n-17*n+25).subs(n,z+4),z).all_coeffs())
d=s.symbols('d')
sig=(1+d)/2
R=2/n+3*(n-3)*(1-1/n-d)/(n*(3-d)-7)
D=1-d*(d*n**2-(6*sig-2)*n+3)/(d*(3-2*sig)*n**2-4*sig*n+2)
H=n*n*d*(2-d)-2*n*(1+d)+2
gap=(n*d-2)*(n*(1-d)-1)*(n*(n-4)*d-n+5)/(n*(n*(3-d)-7)*H)
assert s.factor(D-R-gap)==0
assert s.factor(H.subs(d,2/n)-2*(n-3))==0
assert s.factor(H.subs(d,1-1/n)-(n-3)*(n-1))==0
P=7*n*(n-1)*d**2-(16*n**2-27*n-5)*d+9*n**2-22*n+5
K=4*(1-d)/(1+d)
assert s.factor(K-R-P/(n*(1+d)*(n*(3-d)-7)))==0
assert s.factor(s.diff(P,d).subs(d,1-1/n)-(-2*n**2-n+19))==0
assert s.factor(P.subs(d,1-1/n)-4*(n-3)/n)==0
print('All four-face, continuum and exact-boundary identities passed.')

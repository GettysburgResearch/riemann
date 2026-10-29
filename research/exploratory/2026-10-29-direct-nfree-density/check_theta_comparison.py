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
h=s.symbols('h', positive=True)
dhi=1-h
thi=(5-n*h)/2
Rhi=h*(5-n*h)/2
f3hi=lambda x:2/n+(1-1/n-dhi)*x
fdhi=lambda x:(1-dhi)*x
assert s.factor(f3hi(thi-s.Rational(1,2))-Rhi)==0
assert s.factor(fdhi(thi)-Rhi)==0
Dhi=h*(3-(n+2)*h)/(1-n*h*h)
assert s.factor(Dhi-Rhi-h*(1-n*h)*(n*h*h-4*h+1)/(2*(1-n*h*h)))==0
Khi=4*h/(2-h)
assert s.factor(Khi-Rhi-h*(-n*h*h+(2*n+5)*h-2)/(2*(2-h)))==0
Dlow=1-d/(4-n*d)
assert s.factor((1+1/n-d)-Dlow-(n*d-2)**2/(n*(4-n*d)))==0
h3=1-2*s.Rational(4369347,5000000)+1
assert s.factor(thi.subs({n:3,h:h3})-s.Rational(10608041,5000000))==0
assert s.factor(Rhi.subs({n:3,h:h3})-s.Rational(6689992880773,12500000000000))==0
assert s.factor(Dhi.subs({n:3,h:h3})-s.Rational(2741281467955,5056830380773))==0
assert s.factor((n*h*h-4*h+1).subs(n,3)-(1-h)*(1-3*h))==0
t8=10/(4+n*h); L8=4*t8/5; R8=h*t8
assert s.factor(f3hi(L8)-R8)==0 and s.factor(fdhi(t8)-R8)==0
assert s.factor(Rhi-R8-n*h*h*(1-n*h)/(2*(4+n*h)))==0
assert s.factor(Dhi-R8-h*(1-n*h)*(2+(n-8)*h)/((4+n*h)*(1-n*h*h)))==0
assert s.factor(Khi-R8-2*h*((2*n+5)*h-2)/((2-h)*(4+n*h)))==0
assert s.factor(t8.subs({n:3,h:h3})-s.Rational(25000000,11891959))==0
assert s.factor(R8.subs({n:3,h:h3})-s.Rational(6306530,11891959))==0
v=2/(4+n*h)
dh=1-h
f0h=lambda x:1-dh*x
f2h=lambda x:1-1/n+(2/n-dh)*x
f3h=lambda x:2/n+(1-1/n-dh)*x
fdh=lambda x:h*x
Rstar=5*h*v
assert s.factor(f3h(4*v)-Rstar)==0 and s.factor(fdh(5*v)-Rstar)==0
assert s.factor(f0h(v)-Rstar-(2+(n-8)*h)/(4+n*h))==0
assert s.factor(f2h(2*v)-Rstar-(4+n*(n-7)*h)/(n*(4+n*h)))==0
print('All four-face, high-cutoff, continuum and exact-boundary identities passed.')

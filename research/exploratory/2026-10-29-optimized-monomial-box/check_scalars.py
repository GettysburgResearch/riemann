#!/usr/bin/env python3
"""Exact scalar identities; imports no analytic theorem or Lean result."""
import sympy as s
n,a,u=s.symbols('n a u');d=s.Rational(3,5)
c=1/n+a*(1-2/n)
t1=1-c+d/2;t2=(1-2*c-1/n+d/2)/(1-2/n)
a_cross=(3*n-10)/(5*(n+2)*(n-2))
assert s.factor((t1-t2).subs(a,a_cross))==0
assert s.factor(c.subs(a,a_cross)-s.Rational(8,5)/(n+2))==0
r_cross=s.factor((c+(1-d)*t1).subs(a,a_cross))
assert s.factor(r_cross-(13*n+50)/(25*(n+2)))==0
r_zero=s.factor((c+(1-d)*t2).subs(a,0))
assert s.factor(r_zero-(13*n*n-5*n-50)/(25*n*(n-2)))==0
# t2 dominates below the crossing, t1 above; each has increasing a dependence
# after multiplying by c+(1-d)t. The first derivative is negative for n<10,
# zero at 10, positive for n>10; the other is always positive.
assert s.factor(s.diff(c+(1-d)*t2,a)-(n-10)/(5*n))==0
assert s.factor(s.diff(c+(1-d)*t1,a)-s.Rational(3,5)*(1-2/n))==0
Dn=(12*n*n-38*n+5)/(21*n*n-80*n+50)
diff_cross=s.factor((1+(n-2)*a_cross)*Dn-r_cross)
diff_zero=s.factor(Dn-r_zero)
assert s.factor(diff_cross-(3*n-10)*(69*n*n-280*n+250)/(25*(n+2)*(21*n*n-80*n+50)))==0
assert s.factor(diff_zero-(3*n-10)**2*(3*n*n-25*n+25)/(25*n*(n-2)*(21*n*n-80*n+50)))==0
# These shifted polynomials have positive coefficients for all u≥0.
for p,shift in [(69*n*n-280*n+250,4),(21*n*n-80*n+50,4),(3*n*n-25*n+25,11)]:
 assert all(v>0 for v in s.Poly(s.expand(p.subs(n,u+shift)),u).all_coeffs())
for N in range(4,101):
 av=a_cross.subs(n,N) if N<=10 else s.Integer(0)
 cv=c.subs({n:N,a:av});t=max(t1.subs({n:N,a:av}),t2.subs({n:N,a:av}))
 rv=r_cross.subs(n,N) if N<=10 else r_zero.subs(n,N)
 assert 0<=av<s.Rational(1,2) and d>2*cv and 1<t<s.Rational(3,2)
 assert s.factor(cv+(1-d)*t-rv)==0 and (1+(N-2)*av)*Dn.subs(n,N)>rv
 print(N,'a =',av,'t =',t,'R =',rv) if N in (4,5,7,10,11) else None
print('Symbolic formulas and comparison verified; analytic inputs untested.')

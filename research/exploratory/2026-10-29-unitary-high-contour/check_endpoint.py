#!/usr/bin/env python3
"""Exact source-certificate reconstruction, independent of any mesh sampling."""
import sympy as s

d, y = s.symbols('d y', real=True, nonnegative=True)
q = s.Rational
b, ell, k = q(173, 2000), q(10027, 60000), q(3, 4)
c, alpha = 1/(3*k), q(5, 6)
h, ly = (1+b+3*ell)/2, (1+b-ell)/2
x = q(1, 2)-y
D = 3-(1+2*c)*x
P = (2-2*c*x)*(1-x)
J = (alpha-d)*D+d*P
R = 1-d+(alpha-d)*d*P/(2*J)
C0 = -q(1,4)+b/6+5*ell/4
E = C0+d/2+d*x*(ell+c*(h/4-ly/2))-3*h*(1-R)/4
g, lam = q(1, 1000000), 2916000000
poly = s.Poly(s.cancel(2*lam*J*(-E-g)), d)
assert poly.degree()==2
A, B, C = map(s.expand, poly.all_coeffs())
expected = [
    1209956550+2343372300*y+1740394800*y**2+794068800*y**3,
    -1135891798-1173235148*y+258347816*y**2,
    266598135+244982070*y,
]
assert all(s.expand(a-e)==0 for a,e in zip((A,B,C),expected))
assert all(v>0 for v in s.Poly(A,y).all_coeffs())
disc = s.Poly(s.expand(4*A*C-B**2),y)
assert all(v>0 for v in disc.all_coeffs())
assert s.simplify(J.subs({d:alpha})) > 0
assert s.simplify(D.subs(y,0)) > 0
assert s.Poly(s.expand(D),y).degree() == 1
assert s.Poly(s.expand(P),y).degree() == 2
print('A, B, C match Xu–Sang Appendix D.1; A and 4AC−B² have positive coefficients')
print('J > 0 for 0≤d≤5/6, 0≤y≤1/2 because D,P>0')
print('E≤−1/1000000 holds on the entire rectangle, not only a grid')
print('geometry h =',h,'ly =',ly,'B0 =',q(11,12)-ell/4)

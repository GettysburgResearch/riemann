#!/usr/bin/env python3
"""Exact conditional zero-density scalar comparison, not an analytic proof."""
import sympy as s
n,d,x=s.symbols('n d x');sigma=(d+1)/2
R=1/n+(1-d)*(1-3/n+d/2)/(1-2/n)
t1=1-1/n+d/2;t2=(1-3/n+d/2)/(1-2/n)
assert s.factor(t2-t1-(d*n-2)/(n*(n-2)))==0
assert s.factor(t2-1-(d*n-2)/(2*(n-2)))==0
assert s.factor(s.Rational(3,2)-t2-(1-d)/(2*(1-2/n)))==0
D=1-d*(d*n*n-(6*sigma-2)*n+3)/(d*(3-2*sigma)*n*n-4*sigma*n+2)
expr=(d*n-2)**2*(d*(1-d)*n*n-2*n+2)/(2*n*(n-2)*((2*d-d*d)*n*n-2*d*n-2*n+2))
assert s.factor(D-R-expr)==0
quad=(d*d-2*d)*n*n+2*d*n+2*n-2
assert s.expand(quad.subs(d,2/n))==6-2*n
assert s.expand(quad.subs(d,1-1/n))==-n*n+4*n-3
assert s.factor(n*n-8*(n-1)-((n-7)*(n-1)+1))==0
r=R.subs({n:7,d:s.Rational(1,2)});z=D.subs({n:7,d:s.Rational(1,2)})
assert r==s.Rational(201,280) and z==s.Rational(51,71) and z-r==s.Rational(9,19880)
r=R.subs({n:31,d:s.Rational(3,5)});z=D.subs({n:31,d:s.Rational(3,5)})
assert r==s.Rational(12288,22475) and z==s.Rational(3453,5917)
print('Factorization, endpoint signs, discriminant and n=7/n=31 examples verified.')
print('All analytic estimates and source-to-detector transfers remain assumptions.')

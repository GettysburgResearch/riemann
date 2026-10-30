"""Exact Bernstein replay of the rational endpoint expression; see README."""
import sympy as s
from functools import lru_cache
D,X,u,v=s.symbols('D X u v'); R=s.Rational
p=R(214651,1250000000); b=R(192821,1562500); B=R(7,8)-p/4; ell=R(1,6)+p; ly=(1-ell+b)/2; h=(1+3*ell+b)/2
A=R(5,6); Dx=3-17*X/9; Px=(2-8*X/9)*(1-X); J=(A-D)*Dx+D*Px
count=1-D+(A-D)*D*Px/(2*J)
E=(1+D)/2-B+h*(R(17,50)-R(1,6))-(1+D)*ly/2-ell/2+D*X*ell+h*(count+D/2-R(17,50))
Q=s.Poly(s.cancel((-E-R(1,10**12))*J),D,X)
assert Q.degree_list() == (2, 3)
print('Q degree',Q.degree_list(),flush=True)
coeff={(i,j):Q.coeff_monomial(D**i*X**j) for i in range(3) for j in range(4)}
def boxcoeff(a,b,c,d):
    # expand Q(a+(b-a)u,c+(d-c)v) directly in rationals
    powers={}
    for k in range(3):
      for l in range(4):
       powers[k,l]=sum(coeff[i,j]*s.binomial(i,k)*a**(i-k)*(b-a)**k*s.binomial(j,l)*c**(j-l)*(d-c)**l for i in range(k,3) for j in range(l,4))
    return [sum(powers[k,l]*s.binomial(i,k)/s.binomial(2,k)*s.binomial(j,l)/s.binomial(3,l) for k in range(i+1) for l in range(j+1)) for i in range(3) for j in range(4)]
stack=[(R(1,50),R(3,4),R(0),R(1,2),0)]; n=0; maxdepth=0; least=None
while stack:
 a,b,c,d,depth=stack.pop(); cs=boxcoeff(a,b,c,d); n+=1
 if min(cs)>=0:
  maxdepth=max(maxdepth,depth); least=min(cs) if least is None else min(least,min(cs)); continue
 if depth>=60: raise Exception(('depth',a,b,c,d,min(cs)))
 # alternate dimensions
 if depth%2==0:
  m=(a+b)/2;stack.extend([(a,m,c,d,depth+1),(m,b,c,d,depth+1)])
 else:
  m=(c+d)/2;stack.extend([(a,b,c,m,depth+1),(a,b,m,d,depth+1)])
print('nodes',n,'leaves',(n+1)//2,'maxdepth',maxdepth,'smallest Bernstein coefficient',least,'~',float(least),flush=True)

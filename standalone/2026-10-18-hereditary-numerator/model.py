"""Exact exponent arithmetic for the source-qualified hereditary-family argument.

This module proves no analytic input. All arithmetic is rational; exploratory
optimization is absent from the verifier and from the published certificate.
"""
from fractions import Fraction as F

A_SCALE = F(149,350)
B_SHIFT = F(5,6)-A_SCALE/3
BOUND = B_SHIFT+A_SCALE/2
EMAX = F(1,10**9)
ZLINE = F(2,5)

def k(v):
    return max(F(1),v,F(5,6)+v/3,F(1,3)+5*v/6)

def vzero(nu):
    if not 0<=nu<=1: raise ValueError('count exponent outside [0,1]')
    if nu>=F(1,2): return 1-nu
    if nu>=F(1,6): return F(5,4)-3*nu/2
    return 2-6*nu

def phi(nu,y,L):
    if not 0<=y<=1 or L<0: raise ValueError('invalid strip or length')
    v0=vzero(nu)
    if L<=v0: return nu+(2-2*y)*L
    return max(nu+(2-2*y)*v0,k(L)+(1-2*y)*L)

def selected_kappa(r,nu,y):
    if r<1 or not isinstance(r,int): raise ValueError('moment order must be positive integer')
    if y<F(1,2): return selected_kappa(r,nu,1-y)+r*(1-2*y)
    return phi(nu,y,F(r,2))

def mean(r,nu,y):
    return (1-F(1,2*r))*nu+selected_kappa(r,nu,y)/(2*r)

def tail(s,a,b):
    return [(2-2*s)*b,1+(1-2*s)*a]+[
      F(1,3)+(F(11,6)-2*s)*v for v in (a,b)]+[
      F(5,6)+(F(4,3)-2*s)*v for v in (a,b)]

def density_terms(method,s,t,a,b):
    if not 0<=a<=b: raise ValueError('bad detector lengths')
    if not F(1,2)<=t<s<1: raise ValueError('bad detector line')
    if method=='DF':
        if t!=F(1,2): raise ValueError('DF contract uses central line')
        return [(F(1)+d+c*a)/2+(F(1,2)-s)*b
                for c,d in [(1,0),(0,1),(F(1,3),F(5,6)),(F(5,6),F(1,3))]]+tail(s,a,b)
    if method!='H': raise ValueError('unknown density contract')
    out=[1+(t-s)*b/(F(3,2)*(1-t)),
         (F(37,24)-F(3,2)*t+(t-s)*b)/(F(5,4)-t)]
    for c,d in [(2-2*t,F(0)),(F(4,3)-2*t,F(5,6)),(F(11,6)-2*t,F(1,3))]:
        out += [((1-t+d)/2+c*a/2+(t-s)*b)/(1-t/2),
                F(13,18)-2*t/3+2*d/3+2*c*a/3+F(4,3)*(t-s)*b]
    return out+tail(s,a,b)+[F(1,2)]

def domain(x,y,z):
    return [x-F(1,2),y,z,6*z+y-1,x+6*z-1,x+y-1,
            x+y+6*z-2,6*x+6*z-5]

def cost(nu,x,y,r,a=A_SCALE):
    m=mean(r,nu,y)
    return x-1-a/2+a*y+(1-a)*m

def best_contour(nu,x):
    candidates=[]
    v0=vzero(nu)
    for r in (1,2,3,4):
        ys={1-x,F(1,2),F(1)}
        if F(r,2)>v0:
            yl=(nu+F(r,2)-k(F(r,2)))/(r-2*v0)
            ys.update([yl,1-yl])
        for y in ys:
            if 0<y<=1 and x+y>=1:
                candidates.append((cost(nu,x,y,r),y,r))
    return min(candidates)

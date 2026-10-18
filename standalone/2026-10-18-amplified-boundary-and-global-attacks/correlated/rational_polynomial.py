"""Small exact rational polynomial operations, coefficients in ascending order."""
from fractions import Fraction as F

def trim(p):
    p=list(map(F,p))
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(p,q):
    return trim([(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(max(len(p),len(q)))])

def scale(p,c):
    return trim([v*c for v in p])

def sub(p,q):
    return add(p,scale(q,-1))

def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j]+=a*b
    return trim(out)

def endpoint_coefficients(b,ell,kappa,g):
    alpha=F(5,6)
    c=1/(3*kappa)
    x=[F(1,2),F(-1)]
    D=sub([F(3)],scale(x,1+2*c))
    P=mul(sub([F(2)],scale(x,2*c)),sub([F(1)],x))
    h=(1+b+3*ell)/2
    ly=(1+b-ell)/2
    C0=-F(1,4)+b/6+5*ell/4
    AA=add([F(1,2)-3*h/4],scale(x,ell+c*(h/4-ly/2)))
    Pd=sub(P,D)
    A=scale(sub(mul(AA,Pd),scale(P,3*h/8)),-8)
    B=scale(add(add(scale(Pd,C0+g),scale(mul(AA,D),alpha)),scale(P,3*h*alpha/8)),-8)
    C=scale(D,-8*(C0+g)*alpha)
    disc=sub(scale(mul(A,C),4),mul(B,B))
    return A,B,C,disc

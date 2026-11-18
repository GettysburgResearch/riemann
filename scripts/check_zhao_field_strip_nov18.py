"""Certify unconditional completed-logarithmic derivative bounds for number fields."""
from math import comb
from sympy import Poly, Rational as R, oo, symbols

x=symbols('x')


def certify(s, weights, signatures):
    # Boundary at Re rho = 0, paired with Re rho = 1. The other boundary
    # exchanges the same terms. x is the square of the imaginary part.
    m=len(weights)+1
    denom=(s*s+x)**m*((s-1)**2+x)**m
    num=denom
    for a,other in [(s,s-1),(s-1,s)]:
        for k,b in enumerate(weights,1):
            real=sum(comb(k+1,2*j)*a**(k+1-2*j)*(-x)**j
                     for j in range((k+1)//2+1))
            num+=b/2*(1+x)*real*(x+a*a)**(m-k-1)*(x+other*other)**m
    p=Poly(num,x)
    assert p.eval(0)>0 and p.count_roots(0,oo)==0

    def f(t):
        return sum(b/t**(k+1) for k,b in enumerate(weights,1))

    def arch(t):
        cut=t+128
        return sum(f(t+2*i) for i in range(64))+sum(
            b/(2*k*cut**k) for k,b in enumerate(weights,1))

    for r1,r2 in signatures:
        floor=(r1+r2)*arch(s)+r2*arch(s+1)-f(s)-f(s-1)
        assert floor>2
        print(r1,r2, "strict lower bound", int(floor*10**6)/10**6)


if __name__ == '__main__':
    # Nine real degree-equivalents, with all gamma factors counted at
    # the smaller complex-place-per-degree floor.
    certify(R(7,2),[R(1),R(3),R(16)],[(0,R(9,2))])
    certify(R(4),list(map(R,['.998','5.24','23.92','30.43','332.6'])),[(5,1),(2,3)])

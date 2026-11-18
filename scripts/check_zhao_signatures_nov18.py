"""Exact rational certificate excluding signatures (2,3) and (5,1) and above."""
from fractions import Fraction as F
from math import comb

# Ascending coefficients after clearing the positive zero-test denominator.
P = [F(1609620558301,409600), F(182196401149,51200), -F(21804169401,25600),
     F(90726951,1600), -F(1629701,1600), F(1349,200), F(1,100)]
weights = [F(99,100),F(21,4),F(25),F(28),F(420)]


def poly_at(x):
    a = F(7,2)
    den = (a*a+x)**6
    for k,b in enumerate(weights,1):
        real = sum(comb(k+1,2*j)*(-x)**j*a**(k+1-2*j) for j in range((k+1)//2+1))
        den += b*(x+F(1,4))*real*(a*a+x)**(5-k)
    return den


def check_positive():
    assert all(poly_at(x) == sum(c*x**k for k,c in enumerate(P)) for x in range(7))
    for left,right in zip([0,8,16,32,64,128,256], [8,16,32,64,128,256,512]):
        # Coefficients of (1+t)^6 P((left+right*t)/(1+t)).
        for d in range(7):
            value = sum(c*comb(k,i)*left**(k-i)*right**i*comb(6-k,d-i)
                        for k,c in enumerate(P)
                        for i in range(max(0,d-(6-k)),min(d,k)+1))
            assert value > 0
    for j in range(7):
        assert sum(P[k]*comb(k,j)*512**(k-j) for k in range(j,7)) > 0


def f(v):
    return sum(b/v**(k+1) for k,b in enumerate(weights,1))


def arch(v):
    t = v+128
    return sum(f(v+2*j) for j in range(64))+sum(b/(2*k*t**k) for k,b in enumerate(weights,1))


if __name__ == '__main__':
    check_positive()
    for r1,r2 in [(5,1),(2,3)]:
        bound=(r1+r2)*arch(F(4))+r2*arch(F(5))-f(F(4))-f(F(3))
        assert bound>F(202,100)
        print(r1,r2, "B_K >", int(bound*10**6)/10**6)

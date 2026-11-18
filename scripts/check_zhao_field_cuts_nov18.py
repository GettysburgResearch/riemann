"""Discriminant caps via a positive combination of two zero tests, using Arb."""
from flint import arb, ctx
from check_zhao_field_weight_nov18 import primes_through

# s and t below are given in hundredths.
PARAMS = {5:[(213,70),(212,71),(212,71)],
          6:[(209,115),(209,115),(209,115),(215,69)],
          7:[(201,326),(211,114),(211,114),(210,114)],
          8:[None,None,None,(213,112),(212,113)]}


def arch_derivative(a):
    z=arb(7)/2+a
    f=lambda x: x**-2+3*x**-3+16*x**-4
    m=64
    v=z+2*m
    return sum(f(z+2*j) for j in range(m))+(1/v+3/(2*v**2)+16/(3*v**3))/2


def derivative_floor(n, r2):
    z=arb(7)/2
    f=lambda x: x**-2+3*x**-3+16*x**-4
    return (n-r2)*arch_derivative(0)+r2*arch_derivative(1)-f(z)-f(z-1)


def cap(n, r2, a, t):
    s=arb(a)/100
    t=arb(t)/100
    z=arb(7)/2
    # Sum positive parts of coefficients, with the worst prime splitting.
    P=5000
    pos=arb(0)
    for p in primes_through(P):
        m=p
        while m<=P:
            v=arb(m).log()
            diff=(-s*v).exp()-t*(v+3*v**2/2+8*v**3/3)*(-z*v).exp()
            if not diff<0:
                pos+=arb(p).log()*abs(diff)
            m*=p
    # All omitted prime powers are bounded by the sum over integers.
    pos+=arb(P)**(1-s)*(arb(P).log()+1/(s-1))/(s-1)
    upper=(4*(s-arb(1)/2)-2/s-2/(s-1)+n*arb.pi().log()
           -(n-r2)*(s/2).digamma()-r2*((s+1)/2).digamma()
           +2*t*(2-derivative_floor(n,r2))+2*n*pos)
    return int(upper.exp().ceil().unique_fmpz())


if __name__=="__main__":
    ctx.prec=96
    for n, row in PARAMS.items():
        for r2, pars in enumerate(row):
            if pars is None:
                assert derivative_floor(n,r2)>2
                print(n,r2,"excluded")
            else:
                print(n,r2,cap(n,r2,*pars))

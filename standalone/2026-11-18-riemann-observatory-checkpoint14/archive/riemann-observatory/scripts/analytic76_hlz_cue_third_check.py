from fractions import Fraction
from itertools import product
from math import factorial

import sympy as sy

A, B, C = sy.symbols("A B C")
x, y, z = sy.symbols("x y z")

def exp_coefficient(allocations, base, degree):
    total = 0
    for terms in product(*allocations):
        coefficient = sy.prod(term[1] for term in terms)
        exponent = base + sum(term[0] for term in terms)
        total += coefficient * exponent**degree
    return sy.expand(total) / factorial(degree)


def derivatives(log_primes):
    j = 0
    i = 0
    for flags in product((0, 1), repeat=len(log_primes)):
        h = [ell for flag, ell in zip(flags, log_primes) if flag == 0]
        k = [ell for flag, ell in zip(flags, log_primes) if flag == 1]
        j += ((-B*sum(h)-A*sum(k))**3
              -(-A-B+A*sum(h)+B*sum(k))**3) / (6*(A+B))
        for a, b in ((A, B), (B, A)):
            triples = ((a,b,C,0), (-b,-a,C,-a-b), (a,-C,-b,-b-C))
            for u,v,w,time in triples:
                hs = time-v*sum(h)
                polys = [[(-u*ell,1),(-w*ell,1),(0,-1)] for ell in k]
                # Differentiate the quarter-degree numerator and residue factor separately.
                qp = exp_coefficient(polys, hs, 4)
                frac = v/((u+v)*(v+w))
                i += sy.diff(frac*qp, C).subs(C, 0)
    den = 2**len(log_primes)
    j = sy.cancel(j)/den
    i = sy.cancel(i)/den
    jcoef = sy.Poly(j,A,B).coeff_monomial(A*B)
    icoef = sy.Poly(i,A,B).coeff_monomial(A*B)
    return sy.expand(jcoef+icoef)

normalizer = derivatives(())
assert normalizer == sy.Rational(1,12)
F = derivatives((x,))/normalizer
K2 = derivatives((x,y))/normalizer
K3 = derivatives((x,y,z))/normalizer
centered = sy.expand(K3-K2*F.subs(x,z)-K2.subs({x:y,y:z},simultaneous=True)*F
    -K2.subs(y,z)*F.subs(x,y)+2*F*F.subs(x,y)*F.subs(x,z))
integrand = sy.cancel(centered/(x*y*z)).expand()
print('Normalization:', normalizer)
print('F:', F)
print('K2:', K2)
print('K3:', K3)
print('C3/(xyz):', integrand)
a,b=Fraction(1,20),Fraction(1,10)
term_integrals = []
for power, coef in sy.Poly(integrand,x,y,z).terms():
    term_integrals.append(Fraction(coef)*sy.prod((b**(i+1)-a**(i+1))/(i+1) for i in power))
witness = sum(term_integrals)
assert witness == -Fraction(818904257,864000000000)
print('Witness:', witness)

from functools import lru_cache

def cue_correction(shifts, representative):
    def endpoint(offset):
        return offset.subs(dict(zip((x,y,z),representative)))

    @lru_cache(None)
    def transfer(segment):
        offsets = [sy.S.Zero]
        for step in segment:
            offsets.append(offsets[-1] + step)
        low = -min(offsets,key=endpoint)
        high = 1-max(offsets,key=endpoint)
        d = offsets[-1]
        L = high-low
        M = (high**2-low**2-L)/2
        Q = (high**3-low**3)/3-(high**2-low**2)/2+L/4
        # Orthogonal rank-two basis with norm-square matrix diag(1,1/12).
        return sy.Matrix([[L, M], [12*(M+d*L),12*(Q+d*M)]]).applyfunc(sy.expand)

    def trace_difference(blocks):
        result = 0
        n = len(blocks)
        for flags in product((False,True),repeat=n):
            if not any(flags):
                continue
            start = flags.index(True)
            matrix = sy.eye(2)
            current = []
            for j in range(1,n+1):
                loc = (start-j)%n
                current.append(blocks[loc])
                if flags[loc]:
                    matrix = (transfer(tuple(current))*matrix).applyfunc(sy.expand)
                    current = []
            result += (-1)**sum(flags)*sy.trace(matrix)
        return result

    k,l,m=shifts
    return sy.expand(trace_difference((k+l+m,))
             -trace_difference((k,l+m))-trace_difference((l,k+m))-trace_difference((m,k+l))
             +trace_difference((k,l,m))+trace_difference((k,m,l)))

for representative in ((2,3,4),(2,3,6)):
    frequencies = (x,y,z)
    signs = ((1,1,1),(-1,1,1),(1,-1,1),(1,1,-1))
    cue_kernel = -sy.expand(sum(cue_correction(tuple(s*r for s,r in zip(row,frequencies)),
                                               representative) for row in signs))/4
    assert sy.expand(cue_kernel-centered)==0
    print('CUE chamber verified at order x<y<z, z<x+y:',representative[2]<sum(representative[:2]))

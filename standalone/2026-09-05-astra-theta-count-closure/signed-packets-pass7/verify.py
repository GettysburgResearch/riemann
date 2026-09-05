#!/usr/bin/env python3
"""Finite exact controls for signed-packets-pass7. Standard library only.

This does not machine-prove the analytic results or evaluate infinite prime
sums. The six directed low-zero endpoint signs have a separate executable.
Saved records are compared to canonical freshly reconstructed JSON text,
so numeric aliases and duplicate JSON keys do not pass.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import json


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        if any(type(v) not in (int, F) for v in (self.re, self.im)):
            raise TypeError('Gaussian rational components must be int or Fraction')
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))

    @staticmethod
    def of(x):
        if isinstance(x, C):
            return x
        if type(x) not in (int, F):
            raise TypeError('Only exact real scalars are accepted')
        return C(F(x))

    def __add__(self, other):
        q = C.of(other)
        return C(self.re+q.re, self.im+q.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self+-C.of(other)

    def __rsub__(self, other):
        return C.of(other)+-self

    def __mul__(self, other):
        q = C.of(other)
        return C(self.re*q.re-self.im*q.im, self.re*q.im+self.im*q.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = C.of(other)
        n = q.abs2()
        if n == 0:
            raise ZeroDivisionError('Gaussian rational division by zero')
        return self*C(q.re/n, -q.im/n)

    def __rtruediv__(self, other):
        return C.of(other)/self

    def __pow__(self, n):
        if type(n) is not int:
            raise TypeError('Integer exponent required')
        if n < 0:
            return (C(1)/self)**(-n)
        out, base = C(1), self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n >>= 1
        return out

    def abs2(self):
        return self.re*self.re+self.im*self.im


def mul(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def evaluate(p, z):
    out = 0
    for c in reversed(p):
        out = out*z+c
    return out


def integral(p, end=F(1)):
    return sum((F(c)*end**(i+1)/(i+1) for i,c in enumerate(p)), F())


def interpolate(nodes, values):
    out = [C() for _ in nodes]
    for i, (x,y) in enumerate(zip(nodes,values)):
        basis, denominator = [C(1)], C(1)
        for j,z in enumerate(nodes):
            if i != j:
                basis = mul(basis, [-z, C(1)])
                denominator *= x-z
        for k,b in enumerate(basis):
            out[k] += y*b/denominator
    return out


def ldl_inertia(matrix):
    """Exact unpivoted LDL; fixtures avoid nonzero off-diagonal zero pivots."""
    a = [list(row) for row in matrix]
    signs = []
    for i in range(len(a)):
        v = a[i][i]
        if v == 0:
            if any(a[j][i] != 0 for j in range(i+1,len(a))):
                raise ArithmeticError('A symmetric pivot is required for this fixture')
            signs.append(0)
            continue
        signs.append(1 if v>0 else -1)
        for j in range(i+1,len(a)):
            for k in range(j,len(a)):
                a[j][k] -= a[j][i]*a[k][i]/v
                a[k][j] = a[j][k]
    return {'positive': signs.count(1), 'negative': signs.count(-1),
            'zero': signs.count(0)}


def beta_moments(beta, count):
    # B(k+1/2,beta+1)/B(1/2,beta+1), exact rational ratios.
    out = [F(1)]
    for k in range(count):
        out.append(out[-1]*F(2*k+1,2)/(beta+F(3,2)+k))
    return out


def reconstruct():
    records = []
    def check(name, good, **details):
        if not good:
            raise ArithmeticError('FAILED: '+name)
        records.append({'name':name, **details})

    # Exact pullback and finite Laplace generator identities.
    for m in [2,5,12]:
        for d in range(7):
            coeff = [F((-1)**i*(i+1), i+2) for i in range(d+1)]
            for av in [F(1,4), F(3,2), F(8), C(F(8),F(1))]:
                a = C.of(av)
                z = (a-F(1,4))/(a+1)
                left = a/(a+1)**m*evaluate(coeff,z)
                right = C()
                for j,b in enumerate(coeff):
                    for r in range(j+1):
                        right += b*comb(j,r)*(-F(5,4))**r*a/(a+1)**(m+r)
                check(f'pullback_{m}_{d}_{len(records)}', left==right)

    # Every finite polynomial direction: exact matrix PSD tests, not samples of vectors.
    for m in [5,12,42,100]:
        beta = F(4*m-7,2)
        for d in range(min(7,m-3)):
            n=d+1
            s=beta_moments(beta,2*d+5)
            g=[[F(1,16)*s[i+j]+F(1,2)*s[i+j+1]+s[i+j+2]
                for j in range(d+1)] for i in range(d+1)]
            x=[[F(5,4)/beta*(F(1,16)*(F(1,2)+i+j)*s[i+j]
                    +F(1,2)*(F(3,2)+i+j)*s[i+j+1]
                    +(F(5,2)+i+j)*s[i+j+2])
                for j in range(d+1)] for i in range(d+1)]
            bound=F(10*(d+2),m)
            gi=ldl_inertia(g)
            bi=ldl_inertia([[bound*g[i][j]-x[i][j] for j in range(d+1)]
                           for i in range(d+1)])
            check(f'beta_full_matrix_{m}_{d}', gi['positive']==d+1 and bi['positive']==d+1,
                  dimension=d+1)
            t=beta_moments(beta,2*n+3)
            k=n*(n+beta+F(1,2))
            jmat=[[k*t[i+j]-(i*j*(t[i+j-1]-t[i+j]) if i*j else 0)
                   for j in range(n+1)] for i in range(n+1)]
            ji=ldl_inertia(jmat)
            check(f'jacobi_energy_matrix_{m}_{n}',ji['negative']==0 and ji['zero']==1,
                  dimension=n+1)

    legendre=[]
    for j in range(9):
        legendre.append([F((-1)**(j-r)*comb(j,r)*comb(j+r,r)) for r in range(j+1)])
        for k in range(j+1):
            value=integral(mul(legendre[j],legendre[k]))
            check(f'legendre_orthogonality_{j}_{k}',value==(F(1,2*j+1) if j==k else 0))
    for m in [2,8,32]:
        for d in range(7):
            p=[F((-1)**j,j+1) for j in range(d+1)]
            norm=integral(mul(p,p),F(1,m))
            upper=m*(d+1)**4*(8*m)**(2*d)*norm
            for j,z in enumerate([C(1),C(-1),C(F(1,2),F(1,3))]):
                check(f'legendre_complex_bound_{m}_{d}_{j}',evaluate(p,z).abs2()<=upper)

    # Large exponent comparisons performed as integers, not floating-point logs.
    for d in [0,1,2,3]:
        m=256*(d+2)*((d+1).bit_length()+1)
        numerator=16*2592*m*(d+1)**4*(8*m)**(2*d)*25**m
        denominator=64**m
        check(f'uniform_residue_bound_{d}',numerator<denominator,
              m=m, numerator_bits=numerator.bit_length(), denominator_bits=denominator.bit_length())
    for d in [0,1,2,5,10,50]:
        for ell in [1,4,60,1000]:
            m=(d+2)*max(256*((d+1).bit_length()+1),40*(17+ell*ell))
            variance=F(10*(d+2),m)
            check(f'all_vector_cutoff_constants_{d}_{ell}',
                  variance<=F(1,4*(17+ell*ell)) and 5-17*variance>=F(19,4)
                  and 1-F(ell*ell,2)*variance>=F(7,8),m=m,dimension=d+1)

    # Three real reservoir intervals; no approximate ordinates enter these calculations.
    ranges=[(14,15),(21,22),(25,26)]
    lo=[F(4,4*b*b+5) for a,b in ranges]
    hi=[F(4,4*a*a+5) for a,b in ranges]
    radi=F(1,10001)
    lk=[]
    for i in range(3):
        value=F(1)
        for j in range(3):
            if i==j: continue
            sep=lo[i]-hi[j] if i<j else lo[j]-hi[i]
            check(f'reservoir_separation_{i}_{j}',sep>0,separation=str(sep))
            value *= (radi+hi[j])/sep
        lk.append(value)
    k=sum(v*v for v in lk)
    check('reservoir_interpolation_norm',k<164,squared_norm_bound=str(k),ceiling=164)
    ratio=F(328*10000**3,196**2)*F(678,10000)**10
    check('reservoir_full_signed_seed_m5',ratio<F(1,32),tail_ratio_bound=str(ratio))
    check('reservoir_all_shift_contraction',F(678,10000)**2<1,
          contraction=str(F(678,10000)**2))

    # Exact negative full forms with arbitrary coefficient cancellation at high shift.
    atoms=[C(4),C(8,1),C(8,-1)]
    nodes=[(a-F(1,4))/(a+1) for a in atoms]
    for m in [2,5,42,100,1000,4096]:
        target=[C(),C(0,1)*(atoms[1]+1)**m/atoms[1],
                C(0,-1)*(atoms[2]+1)**m/atoms[2]]
        p=interpolate(nodes,target)
        values=[a/(a+1)**m*evaluate(p,z) for a,z in zip(atoms,nodes)]
        q=sum((v*v for v in values),C())
        check(f'negative_signed_block_{m}',q==C(-2) and all(v.im==0 for v in p),
              full_form=-2,coefficient_bits=max(v.re.numerator.bit_length() for v in p))

    # A leading cluster of three real locations and one pair, plus a remote real tail.
    fixture=[C(4),C(9),C(16),C(25,1),C(25,-1),C(100)]
    for m in [5,10,20]:
        matrix=[]
        for i in range(5):
            row=[]
            for j in range(5):
                value=sum((a*a/(a+1)**(2*m+i+j) for a in fixture),C())
                if value.im!=0: raise ArithmeticError('Fixture conjugation failed')
                row.append(value.re)
            matrix.append(row)
        inertia=ldl_inertia(matrix)
        check(f'leading_cluster_inertia_{m}',inertia=={'positive':4,'negative':1,'zero':0},
              inertia=inertia)

    return {'status':'PASS_SIGNED_PACKET_FINITE_CONTROLS',
        'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
        'distinct_checks':len(records), 'analytic_proofs_machine_verified':False,
        'rh_proved':False, 'infinite_prime_sum_evaluated':False,
        'six_endpoint_signs':'separate verify_low_zeros.py replay',
        'checks':records}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    value=reconstruct()
    text=json.dumps(value,indent=2,sort_keys=True)+'\n'
    if args.check and args.check.read_text()!=text:
        raise SystemExit('Saved exact record differs from fresh reconstruction')
    print(text,end='')

if __name__=='__main__':
    main()

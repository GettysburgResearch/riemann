"""Classify eventual negative integrated bias in progressions under GRH + LI."""
import csv
from functools import lru_cache
from math import gcd
from pathlib import Path
from flint import acb, arb, arb_series, ctx, dirichlet_char
from census import factor_distinct


def divisors(q):
    return [f for f in range(1,q+1) if q%f==0]


def square_roots(q):
    e = 0
    while q%2==0:
        e += 1
        q //= 2
    return (1 if e<=1 else 2 if e==2 else 4)*2**len(factor_distinct(q))


def conductor_bound(q):
    ps = factor_distinct(q)
    phi = q
    for p in ps:
        phi = phi//p*(p-1)
    return (phi*((arb(q)/arb.pi()).log()-arb.const_euler()-arb('1.14')
                 -sum(arb(p).log()/(p-1) for p in ps))+3)/3


@lru_cache(None)
def primitive_tables(f):
    data = []
    for j in range(1,f):
        if gcd(f,j)>1:
            continue
        chi = dirichlet_char(f,j)
        if chi.is_primitive():
            data.append((chi.parity(),[chi(r) for r in range(1,f)]))
    return data


@lru_cache(None)
def primitive_mass(f, j, panels):
    theta = arb.pi()*j/(2*panels)
    c = (arb(1)/4+2*theta.sin()**2).sqrt()
    s = arb(1)/2+c
    if f == 1:
        if j == 0:
            return 2+arb.const_euler()-(4*arb.pi()).log()
        z = arb_series([s,1], prec=2).zeta()
        return (1/s+1/(s-1)+z[1]/z[0]+((s/2).digamma()-arb.pi().log())/2)/c
    chars = primitive_tables(f)
    if not chars:
        return arb(0)
    ss = arb_series([s,1], prec=2)
    zeta = [ss.zeta(arb(r)/f, deflate=True) for r in range(1,f)]
    mass = arb(0)
    for a, chi in chars:
        val = sum(ch*z[0] for ch,z in zip(chi,zeta))
        der = sum(ch*z[1] for ch,z in zip(chi,zeta))
        assert not val.contains(0)
        mass += ((2*(der/val).real - (arb(f)*arb.pi()).log() + ((s+a)/2).digamma())/(2*c))
    return mass


def classify(q):
    fs = divisors(q)
    target = 2*arb(square_roots(q))/3
    def mass(j, panels):
        d = gcd(j, panels)
        return sum(primitive_mass(f,j//d,panels//d) for f in fs)
    lo = mass(1,1)
    hi = mass(0,1)
    middle = arb(0)
    panels = 1
    while panels <= 8192:
        low = (lo+middle)/panels
        high = (hi+middle)/panels
        if low > target or high < target:
            return (q,'negative_squares' if high < target else 'both_all',panels,
                    int((1000*low).lower().floor().unique_fmpz()),
                    int((1000*high).upper().ceil().unique_fmpz()))
        panels *= 2
        for j in range(1,panels,2):
            middle += mass(j,panels)
    raise ValueError(f'unresolved {q}')


def zero_phase(q):
    # Sum of the completed logarithmic derivatives at 1 minus those at 2,
    # including the principal zeta pole correction. Real parts pair conjugates.
    return (sum(primitive_mass(f, 0, 1)/2-
                3*primitive_mass(f, 1, 1)/2 for f in divisors(q)))


if __name__=='__main__':
    ctx.prec = 96
    assert (3*arb(2000).log()-3*arb(2).log()-arb(3).log())/4 > arb(130).log()
    assert (arb(130)/arb.pi()).log()-arb.const_euler()-arb('1.14') > 2
    with Path('progression-norms.tsv').open('w') as output:
        out = csv.writer(output,delimiter='\t',lineterminator='\n')
        out.writerow(('modulus','li_decision','panels','norm_lower_milli','norm_upper_milli'))
        for q in range(1,2000):
            if conductor_bound(q) <= 2*arb(square_roots(q))/3:
                out.writerow(classify(q))

    with Path('progression-counterexamples.tsv').open('w') as output:
        out = csv.writer(output, delimiter='\t', lineterminator='\n')
        out.writerow(('modulus', 'class', 'limsup_lower_milli'))
        for q in (11,21,22,28,36,40,42,48,60,84,120):
            margin = -2*arb(square_roots(q))/3-zero_phase(q)
            assert margin > 0
            out.writerow((q, 1, int((1000*margin).lower().floor().unique_fmpz())))

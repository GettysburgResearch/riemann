"""Certified bounds for the sum of reciprocal squared distances to GRH zeros.

Euler data maps rational primes to a list of residue degrees, one entry per
prime ideal over that prime, including ramified primes. Omitted entries are
unknown and are bounded by the full degree. Inputs describe a number field.
"""
from math import isqrt
from flint import arb, ctx


def primes_through(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            first = p*p
            sieve[first::p] = bytes(1 + (limit - first)//p)
    return [p for p in range(2, limit + 1) if sieve[p]]


def field_terms(limit):
    p = arb(limit)
    u = p.log()
    g = (p-1)/(p+1)
    delta = 2*p.sqrt()/(p+1)
    two = arb(2)
    a0 = (g*(-arb.const_euler()-2*two.log()-arb.pi().log())
          + 2*((p+1)/2).log()/(p+1) + 2*g*(1/p).atanh())
    a1 = (g*(-arb.const_euler()-arb.pi().log())
          + 2*(2*p/(p+1)).log()/(p+1) - g*(1-1/p**2).log())
    return g, delta, 2*u*g, a0, a1


def prime_term(limit, p, f):
    norm = p**f
    m = norm
    summands = arb(0)
    while m <= limit:
        summands += arb(limit)/m-1
        m *= norm
    return 2*f*arb(p).log()*summands/(limit+1)


def weight_bounds(discriminant, r1, r2, limit, residue_degrees):
    if limit < 2 or not discriminant or r1 < 0 or r2 < 0 or r1+2*r2 == 0:
        raise ValueError("Invalid signature, discriminant, or prime cutoff")
    g, delta, pole, a0, a1 = field_terms(limit)
    upper = g*arb(abs(discriminant)).log()+pole+(r1+r2)*a0+r2*a1
    uncertainty = arb(0)
    for p in primes_through(limit):
        if p in residue_degrees:
            degrees = residue_degrees[p]
            if not degrees or min(degrees) < 1 or sum(degrees) > r1+2*r2:
                raise ValueError("Invalid residue degree list")
            upper -= sum(prime_term(limit, p, f) for f in degrees)
        else:
            uncertainty += (r1+2*r2)*prime_term(limit, p, 1)
    return (upper-uncertainty)/(1+delta), upper/(1-delta)


if __name__ == "__main__":
    ctx.prec = 96
    for limit in [20, 100, 1000]:
        bounds = weight_bounds(1, 1, 0, limit, {p:[1] for p in primes_through(limit)})
        exact = 2+arb.const_euler()-(4*arb.pi()).log()
        assert bounds[0] < exact and bounds[1] > exact
        print(limit, *bounds)

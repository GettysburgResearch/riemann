"""An explicit sextic Kummer family over the Eisenstein field.

Rows are integral exterior ideals with their UNIQUE generator congruent
to 1 modulo (3). Columns are actual ideals. Character values are exact
elements of Z[w], w^2+w+1=0; nonunits always have character value zero.
"""
from array import array
from functools import lru_cache
from math import isqrt

import ideals as I

ZERO = (0, 0)
ONE = (1, 0)
ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(n, x):
    return n*x[0], n*x[1]


def absolute_squared(x):
    return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]


@lru_cache(None)
def primary_generator(ideal):
    I.require(I.valid(ideal) and I.norm(ideal) % 3 != 0, 'Ideal must be prime to 3.')
    q = I.norm(ideal)
    candidates = set()
    # Solving (2a-b)^2=4q-3b^2 gives every element of norm q.
    bound = 2*isqrt(q)+2
    for b in range(-bound, bound+1):
        if b % 3:
            continue
        disc = 4*q-3*b*b
        if disc < 0:
            continue
        root = isqrt(disc)
        if root*root != disc:
            continue
        for r in {root, -root}:
            if (b+r) % 2:
                continue
            a = (b+r)//2
            if (a-1) % 3 == 0 and I.member(ideal, (a, b)):
                candidates.add((a, b))
    I.require(len(candidates) == 1, 'Unique primary generator was not reconstructed.')
    return candidates.pop()


@lru_cache(None)
def fast_primes_over(p):
    if p % 3 == 2:
        return ((p, 0, p),)
    if p == 3:
        return ((3, 2, 1),)
    I.require(p > 3 and p % 6 == 1, 'Exterior rational prime required.')
    # A primitive sixth root r solves r^2-r+1=0; its inverse is 1-r.
    for g in range(2, p):
        r = pow(g, (p-1)//6, p)
        if r != p-1 and pow(r, 3, p) == p-1:
            roots = sorted((r, (1-r) % p))
            return tuple((p, b, 1) for b in roots)
    raise ValueError('A split prime had no primitive sixth root.')


def residue(ideal, x):
    a, b, c = ideal
    y, quotient = x[1] % c, x[1] // c
    return (x[0]-b*quotient) % a, y


def power_mod_prime(x, exponent, prime):
    if prime[2] == 1:
        return pow(residue(prime, x)[0], exponent, prime[0]), 0
    p = prime[0]
    result = ONE
    x = x[0] % p, x[1] % p
    while exponent:
        if exponent & 1:
            result = I.element_product(result, x)
            result = result[0] % p, result[1] % p
        exponent //= 2
        if exponent:
            x = I.element_product(x, x)
            x = x[0] % p, x[1] % p
    return result


def symbol_at_prime(alpha, prime):
    I.require(I.norm(prime) % 6 == 1, 'Sixth-power residue field required.')
    if I.member(prime, alpha):
        return ZERO
    value = power_mod_prime(alpha, (I.norm(prime)-1)//6, prime)
    candidates = [root for root in ROOTS if residue(prime, root) == value]
    I.require(len(candidates) == 1, 'Residue did not identify a unique sixth root.')
    return candidates[0]


def symbol(alpha, column):
    result = ONE
    for prime, exponent in I.factor(column):
        value = symbol_at_prime(alpha, prime)
        for _ in range(exponent):
            result = I.element_product(result, value)
    return result


def prime_coefficients(alpha, p):
    if p % 3 == 2:
        return ZERO, scale(-1, symbol_at_prime(alpha, (p, 0, p)))
    left, right = fast_primes_over(p)
    x, y = symbol_at_prime(alpha, left), symbol_at_prime(alpha, right)
    return scale(-1, add(x, y)), I.element_product(x, y)


def smallest_prime_factors(limit):
    out = array('I', range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if out[p] == p:
            for n in range(p*p, limit+1, p):
                if out[n] == n:
                    out[n] = p
    return out


def norm_coefficients(ideal, limit, principal_support=None, smallest=None):
    """All ideal Mobius-times-character norm coefficients, two int32 arrays.

    A split prime contributes 1-(chi(P)+chi(Pbar))X+chi(P)chi(Pbar)X^2;
    an inert prime contributes 1-chi(P)X^2. S={primes over 2,3} is deleted.
    """
    I.require(I.exterior(ideal), 'Exterior row required.')
    alpha = primary_generator(ideal)
    if smallest is None:
        smallest = smallest_prime_factors(limit)
    if principal_support is None:
        principal_support = I.norm_mobius_coefficients(limit, compact=True)
    real_basis = array('i', [0])*(limit+1)
    omega_basis = array('i', [0])*(limit+1)
    real_basis[1] = 1
    local = {}
    for n in range(2, limit+1):
        if not principal_support[n]:
            continue
        p = smallest[n]
        m, exponent = n, 0
        while m % p == 0:
            m //= p
            exponent += 1
        if p not in local:
            local[p] = prime_coefficients(alpha, p)
        value = local[p][exponent-1]
        out = I.element_product(value, (real_basis[m], omega_basis[m]))
        real_basis[n], omega_basis[n] = out
    return real_basis, omega_basis

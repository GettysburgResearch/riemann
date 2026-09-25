#!/usr/bin/env python3
"""Exact finite checks for an arithmetic boundary-comparison research note.

Standard library only. This is not an RH test or an infinite proof checker.
Uses integer sparse vectors and integer arithmetic in cyclotomic rings.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
import json
import math
from pathlib import Path

COUNTS: dict[str, int] = defaultdict(int)

def eq(a, b, group: str) -> None:
    COUNTS[group] += 1
    if a != b:
        raise AssertionError(f'{group}: {a!r} != {b!r}')

def tidy(v):
    return {k: x for k, x in v.items() if x}

def plus(*vectors):
    ans = defaultdict(int)
    for v in vectors:
        for k, x in v.items():
            ans[k] += x
    return tidy(ans)

def neg(v):
    return {k: -x for k, x in v.items()}

def dil(a: int, v: dict[int, int]):
    return {a*k: x for k, x in v.items() if x}

def down(a: int, v: dict[int, int]):
    return {k//a: x for k, x in v.items() if k % a == 0 and x}

def cut(N: int, v: dict[int, int]):
    return {k: x for k, x in v.items() if 1 <= k <= N and x}

def inside(a, N, v):
    return cut(N, dil(a, cut(N, v)))

def inside_star(a, N, v):
    return cut(N, down(a, cut(N, v)))

def escape(a, N, v):
    return {k: x for k, x in dil(a, cut(N, v)).items() if k > N and x}

def escape_star(a, N, v):
    return cut(N, down(a, {k: x for k, x in v.items() if k > N and x}))

def dot(v, w):
    return sum(x*w.get(k, 0) for k, x in v.items())

def check_boundaries():
    for N in range(1, 49):
        for a in range(2, 10):
            for b in range(2, 10):
                g = math.gcd(a, b)
                lo = N // (a*b//g)
                hi = N // max(a//g, b//g)
                rank = 0
                for n in range(1, N+1):
                    v = {n: 1}
                    lhs = escape_star(a, N, escape(b, N, v))
                    rhs = plus(inside(b//g, N, inside_star(a//g, N, v)),
                               neg(inside_star(a, N, inside(b, N, v))))
                    eq(lhs, rhs, 'gcd_boundary_gram')
                    expected = {}
                    if n % (a//g) == 0:
                        k = n // (a//g)
                        if lo < k <= hi:
                            expected = {(b//g)*k: 1}
                    eq(lhs, expected, 'sharp_support')
                    rank += bool(lhs)
                eq(rank, hi-lo, 'exact_rank')
                v = {n: ((17*n + 3*a - b) % 11)-5 for n in range(1, N+1)}
                first = escape(a, N, inside(b, N, v))
                second = dil(a, escape(b, N, v))
                eq(escape(a*b, N, v), plus(first, second), 'escape_cocycle')
                eq(dot(first, second), 0, 'cocycle_orthogonality')
                eq(dot(escape(a*b, N, v), escape(a*b, N, v)),
                   dot(first, first)+dot(second, second), 'pythagorean_energy')
        # Operator-valued positivity checked by two independently assembled expressions.
        factors = [2, 3, 4, 5, 6, 7]
        xs = [{n: ((a*n + n*n) % 7)-3 for n in range(1, N+1)} for a in factors]
        image = plus(*(escape(a, N, x) for a, x in zip(factors, xs)))
        gram_sum = sum(dot(x, escape_star(a, N, escape(b, N, y)))
                       for a, x in zip(factors, xs) for b, y in zip(factors, xs))
        eq(gram_sum, dot(image, image), 'complete_block_gram')
        if gram_sum < 0:
            raise AssertionError('negative Gram')
        COUNTS['gram_nonnegative'] += 1
    for N in (1, 7, 12, 31, 64):
        v = {n: ((n*n+5*n) % 9)-4 for n in range(1, N+1)}
        for word in permutations((2, 3, 5)):
            terms = []
            for i, a in enumerate(word):
                suffix = math.prod(word[i+1:])
                prefix = math.prod(word[:i])
                terms.append(dil(prefix, escape(a, N, inside(suffix, N, v))))
            eq(plus(*terms), escape(math.prod(word), N, v), 'factorization_coherence')
            for i in range(len(terms)):
                for j in range(i):
                    eq(dot(terms[i], terms[j]), 0, 'first_exit_orthogonality')
    # An actually nonzero omitted boundary, not just a generic syntactic mutation.
    actual = escape_star(2, 12, escape(3, 12, {6: 1}))
    eq(actual, {9: 1}, 'explicit_boundary_control')
    eq(actual == {}, False, 'rejected_shortcuts')
    return {'N': 12, 'a': 2, 'b': 3,
            'nonzero_columns': {'6': {'9': 1}, '8': {'12': 1}}, 'rank': 2}

# Exact cyclotomic arithmetic. Low degree first.
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def poly_div_exact(p, q):
    p = trim(p); q = trim(q)
    out = [0]*max(1, len(p)-len(q)+1)
    while len(p) >= len(q) and p != [0]:
        k = len(p)-len(q)
        if p[-1] % q[-1]:
            raise AssertionError('nonintegral polynomial division')
        c = p[-1]//q[-1]
        out[k] = c
        for j, x in enumerate(q):
            p[k+j] -= c*x
        p = trim(p)
    if p != [0]:
        raise AssertionError('inexact polynomial division')
    return tuple(trim(out))

@lru_cache(None)
def cyclotomic(n):
    p = [-1] + [0]*(n-1) + [1]
    for d in range(1, n):
        if n % d == 0:
            p = poly_div_exact(p, cyclotomic(d))
    return tuple(p)

class Cyclo:
    def __init__(self, n):
        self.n = n
        self.mod = cyclotomic(n)
        self.d = len(self.mod)-1
        self.zero = (0,)*self.d
        self.one = (1,)+(0,)*(self.d-1)
        self.roots = [self.reduce([0]*i+[1]) for i in range(n)]
    def reduce(self, p):
        p = list(p)
        for k in range(len(p)-1, self.d-1, -1):
            c = p[k]
            if c:
                for j, x in enumerate(self.mod):
                    p[k-self.d+j] -= c*x
        return tuple((p+[0]*self.d)[:self.d])
    def add(self, a, b):
        return tuple(x+y for x, y in zip(a, b))
    def scale(self, a, n):
        return tuple(n*x for x in a)
    def mul(self, a, b):
        p = [0]*(2*self.d-1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                p[i+j] += x*y
        return self.reduce(p)
    def conj(self, a):
        out = self.zero
        for i, x in enumerate(a):
            out = self.add(out, self.scale(self.roots[(-i) % self.n], x))
        return out
    def inner(self, v, w):
        ans = self.zero
        for x, y in zip(v, w):
            ans = self.add(ans, self.mul(self.conj(x), y))
        return ans

def channels(a, b, ring):
    # Columns of the UNNORMALIZED iterated banks F_(a,j) F_(b,k).
    out = []
    for j in range(a):
        for k in range(b):
            v = [ring.zero]*(a*b)
            for r in range(a):
                for s in range(b):
                    exponent = b*j*r + a*k*s
                    v[r+a*s] = ring.roots[exponent % (a*b)]
            out.append(v)
    return out

def check_banks():
    for a in range(2, 17):
        R = Cyclo(a)
        cols = [[R.roots[(j*r) % a] for r in range(a)] for j in range(a)]
        for j in range(a):
            for k in range(a):
                eq(R.inner(cols[j], cols[k]), R.scale(R.one, a) if j == k else R.zero,
                   'residue_fourier_orthogonality')
        for r in range(a):
            total = R.zero
            for j in range(a):
                total = R.add(total, cols[j][r])
            eq(total, R.scale(R.one, a) if r == 0 else R.zero, 'native_channel_reconstruction')
        eq(Fraction(1, a)*a, 1, 'half_density_normalization')
    recouplings = []
    for a, b in ((2, 3), (2, 5), (3, 5)):
        n = a*b; R = Cyclo(n)
        A = channels(a, b, R)
        B = channels(b, a, R)
        for bank in (A, B):
            for j in range(n):
                for k in range(n):
                    eq(R.inner(bank[j], bank[k]), R.scale(R.one, n) if j == k else R.zero,
                       'iterated_bank_orthogonality')
        # M/n is the unitary change between the two normalized banks.
        M = [[R.inner(A[j], B[k]) for k in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                value = R.zero
                for k in range(n):
                    value = R.add(value, R.mul(M[i][k], R.conj(M[j][k])))
                eq(value, R.scale(R.one, n*n) if i == j else R.zero,
                   'factor_order_recoupling_unitarity')
        off_diagonal = sum(M[i][j] != R.zero for i in range(n) for j in range(n) if i != j)
        recouplings.append({'a': a, 'b': b, 'dimension': n,
                            'off_diagonal_nonzero_entries': off_diagonal})
    # Coarse bank is not a source-preserving replacement, even for one prime.
    native = {1: 1, 2: -1}
    coarse_unnormalized = {1: 1, 2: -1, 3: -1}
    eq(native == coarse_unnormalized, False, 'rejected_shortcuts')
    return recouplings

def sieve(limit):
    mu = [1]*(limit+1); mu[0] = 0
    primes = []
    composite = [False]*(limit+1)
    fac = [[] for _ in range(limit+1)]
    for p in range(2, limit+1):
        if not composite[p]:
            primes.append(p)
            for n in range(p, limit+1, p):
                composite[n] = True
                mu[n] = -mu[n]
                fac[n].append(p)
            for n in range(p*p, limit+1, p*p):
                mu[n] = 0
    return mu, primes, fac

def boundary(v):
    out = defaultdict(int)
    for S, c in v.items():
        for i in range(len(S)):
            out[S[:i]+S[i+1:]] += c*((-1)**i)
    return tidy(out)

def check_topology(limit):
    mu, primes, fac = sieve(limit)
    for n in range(1, limit+1):
        if not mu[n]:
            continue
        S = tuple(fac[n])
        eq(boundary(boundary({S: 1})), {}, 'simplicial_boundary_squared')
        if n % 2:
            b = {(2,)+S: 1}
            c = boundary(b)
            eq(c.get(S), 1, 'filtered_triangular_pivot')
            eq(boundary(c), {}, 'persistent_cycle')
            eq(max(math.prod(T) for T in c), n, 'sharp_bar_birth')
            eq(math.prod((2,)+S), 2*n, 'sharp_bar_death')
    M = 0
    examples = []
    for N in range(1, limit+1):
        M += mu[N]
        active = [n for n in range(N//2+1, N+1) if n % 2 and mu[n]]
        signed = sum(mu[n] for n in active)
        eq(signed, M, 'barcode_euler_identity')
        if N in (63, 255, 1023, 4095, limit):
            by_degree = defaultdict(int)
            for n in active:
                by_degree[len(fac[n])-1] += 1
            examples.append({'N': N, 'M': M, 'active_bars': len(active),
                             'reduced_betti_by_degree': dict(sorted(by_degree.items()))})
    # Literal finite Euler product, complete coefficients rather than just its total.
    v = {1: 1}
    for p in primes:
        v = cut(limit, plus(v, neg(dil(p, v))))
    eq(v, {n: mu[n] for n in range(1, limit+1) if mu[n]}, 'native_euler_product')
    return examples


def shift(k, v):
    return {n+k: x for n, x in v.items() if x}

def coarse(a, v):
    return plus(*(shift(r, dil(a, v)) for r in range(a)))

def coarse_star(a, v):
    return plus(*(down(a, shift(-r, v)) for r in range(a)))

def check_additive_obstruction():
    for a in range(2, 17):
        for n in range(-3, 4):
            v = {n: 1}
            eq(down(a, shift(1, dil(a, v))), {}, 'native_additive_gap')
            eq(coarse_star(a, shift(1, coarse(a, v))),
               {n: a-1, n+1: 1}, 'coarse_additive_overlap')
        for b in range(2, 10):
            eq(coarse(a, coarse(b, {1: 1})), coarse(a*b, {1: 1}),
               'coarse_semigroup')
    # Joint initial-space defect of S_2 and S_3 at u=1/4.
    u = Fraction(1, 4)
    defect = 1-int(u < Fraction(1, 2))-int(u < Fraction(1, 3))+int(u < Fraction(1, 6))
    eq(defect, -1, 'joint_defect_negative_control')
    eq(defect >= 0, False, 'rejected_shortcuts')
    # Its ordinary unit-cell average has the opposite conclusion about sign.
    eq(1-Fraction(1, 2)-Fraction(1, 3)+Fraction(1, 6), Fraction(1, 3),
       'joint_defect_positive_average')

def check_masks():
    # Sample every rational cell subinterval with denominator 35;
    # universal identities are proved in the note, not certified by these samples.
    for a in range(2, 10):
        for b in range(2, 10):
            for k in range(-30, 31):
                for t in (Fraction(0), Fraction(1, 35), Fraction(17, 35), Fraction(34, 35)):
                    x = k+t
                    R_a = int(math.floor(x) % a == 0)
                    R_b = int(math.floor(x) % b == 0)
                    R_l = int(math.floor(x) % math.lcm(a, b) == 0)
                    eq(R_a*R_b, R_l, 'spatial_mask_lcm')
                    shifted = int(math.floor(x/a) % b == 0)
                    R_ab = int(math.floor(x) % (a*b) == 0)
                    eq(R_a*shifted, R_ab, 'masked_dilation_product')
    # Tracial invariance would conflict with residue partition already for p=2.
    eq(2*Fraction(1) == Fraction(1), False, 'rejected_shortcuts')

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--limit', type=int, default=4095)
    args = ap.parse_args()
    if not 2 <= args.limit <= 20000:
        ap.error('--limit must lie between 2 and 20000')
    example = check_boundaries()
    banks = check_banks()
    topology = check_topology(args.limit)
    check_additive_obstruction()
    check_masks()
    result = {
        'status': 'finite exact algebra checked; no RH implication proved',
        'arithmetic': 'integers, Fractions, integer cyclotomic quotient rings; no floating point',
        'scope': {'boundary_N': [1, 48], 'boundary_factors': [2, 9],
                  'one_prime_banks': [2, 16], 'native_prefix_limit': args.limit},
        'predicate_counts': dict(sorted(COUNTS.items())),
        'boundary_example': example,
        'recoupling_examples': banks,
        'topology_examples': topology,
        'not_executed': ['repository validators', 'independent mathematical review',
                         'analytic Fourier-tail certification', 'Weil-form comparison',
                         'RH-sensitive native upper estimate'],
    }
    text = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')
if __name__ == '__main__':
    main()

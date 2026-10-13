#!/usr/bin/env python3
"""Exact finite checks; no asymptotic claim follows from the output.

Uses every squarefree ideal column prime to 6 below the specified norm cap.
Arithmetic is in Z[omega], omega^2+omega+1=0. No third-party packages.
The optional larger table is the principal native norm-coefficient model,
not ordinary integer Mobius. Diagnostic W0 is C^1, not C^infinity.
"""
from __future__ import annotations
import itertools
import json
import math
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction

Z = tuple[int, int]
ZERO: Z = (0, 0)
ONE: Z = (1, 0)
COUNTS: Counter[str] = Counter()


def require(ok: bool, category: str) -> None:
    COUNTS[category] += 1
    if not ok:
        raise RuntimeError(f"Failed exact check: {category}")


def add(x: Z, y: Z) -> Z:
    return x[0] + y[0], x[1] + y[1]


def neg(x: Z) -> Z:
    return -x[0], -x[1]


def mul(x: Z, y: Z) -> Z:
    a, b = x; c, d = y
    return a*c-b*d, a*d+b*c-b*d


def conj(x: Z) -> Z:
    return x[0]-x[1], -x[1]


def norm(x: Z) -> int:
    return x[0]**2-x[0]*x[1]+x[1]**2


def scale(x: Z, a: int) -> Z:
    return a*x[0], a*x[1]


def power(x: Z, n: int, modulus: int | None = None) -> Z:
    out = ONE
    while n:
        if n & 1:
            out = mul(out, x)
            if modulus:
                out = out[0] % modulus, out[1] % modulus
        x = mul(x, x)
        if modulus:
            x = x[0] % modulus, x[1] % modulus
        n //= 2
    return out


UNITS = [power((1, 1), i) for i in range(6)]


@dataclass(frozen=True)
class PrimeIdeal:
    p: int
    root: int | None
    q: int

    def character(self, u: Z) -> Z:
        if self.root is not None:
            v = (u[0] + self.root*u[1]) % self.p
            if v == 0:
                return ZERO
            residue = pow(v, (self.p-1)//6, self.p)
            for i, unit in enumerate(UNITS):
                if (unit[0]+unit[1]*self.root) % self.p == residue:
                    return UNITS[i]
        else:
            v = (u[0] % self.p, u[1] % self.p)
            if v == ZERO:
                return ZERO
            residue = power(v, (self.q-1)//6, self.p)
            for unit in UNITS:
                if (unit[0] % self.p, unit[1] % self.p) == residue:
                    return unit
        raise RuntimeError('Residue did not lie in mu_6')


def rational_primes(cap: int) -> list[int]:
    sieve = bytearray(b'\x01') * (cap+1)
    if cap >= 0: sieve[0] = 0
    if cap >= 1: sieve[1] = 0
    for p in range(2, math.isqrt(cap)+1):
        if sieve[p]:
            sieve[p*p:cap+1:p] = b'\x00'*((cap-p*p)//p+1)
    return [p for p in range(2, cap+1) if sieve[p]]


def ideal_primes(cap: int) -> list[PrimeIdeal]:
    out = []
    for p in rational_primes(cap):
        if p in (2, 3):
            continue
        if p % 3 == 1:
            roots = [r for r in range(p) if (r*r+r+1) % p == 0]
            require(len(roots) == 2, 'split_prime_roots')
            out.extend(PrimeIdeal(p, r, p) for r in roots)
        elif p*p <= cap:
            out.append(PrimeIdeal(p, None, p*p))
    return sorted(out, key=lambda x: (x.q, x.p, -1 if x.root is None else x.root))


def squarefree_ideals(primes: list[PrimeIdeal], cap: int) -> list[tuple[int, int]]:
    ideals = [(0, 1)]
    for i, p in enumerate(primes):
        ideals += [(mask | (1 << i), n*p.q) for mask, n in ideals if n*p.q <= cap]
    return sorted(ideals, key=lambda t: (t[1], t[0]))


def weight_numerator(n: int, D: int) -> int:
    # W0(n/D)=30*(n/D-1)^2*(2-n/D)^2 inside [1,2].
    return 30*(n-D)**2*(2*D-n)**2 if D <= n <= 2*D else 0


Poly = dict[int, Z]


def clean(P: Poly) -> Poly:
    return {m: c for m, c in P.items() if c != ZERO}


def multiply(P: Poly, Q: Poly) -> Poly:
    out: Poly = {}
    for a, x in P.items():
        for b, y in Q.items():
            key = a ^ b
            out[key] = add(out.get(key, ZERO), mul(x, y))
    return clean(out)


def poly_power(P: Poly, k: int) -> Poly:
    Q = {0: ONE}
    for _ in range(k):
        Q = multiply(Q, P)
    return Q


def freeze(P: Poly, bit: int) -> Poly:
    out: Poly = {}
    for mask, z in P.items():
        key = mask & ~bit
        out[key] = add(out.get(key, ZERO), neg(z) if mask & bit else z)
    return clean(out)


def energy(Q: Poly) -> int:
    return sum(norm(z) for z in Q.values())


def evaluate(P: Poly, signs: dict[int, int]) -> Z:
    out = ZERO
    for mask, z in P.items():
        s = 1
        for bit, val in signs.items():
            if mask & bit:
                s *= val
        out = add(out, scale(z, s))
    return out


def direct_increment(P: Poly, bit: int, k: int, later: list[int]) -> Fraction:
    total = 0
    for values in itertools.product((-1, 1), repeat=len(later)):
        signs = dict(zip(later, values))
        signs[bit] = -1
        minus = norm(evaluate(P, signs))**k
        signs[bit] = 1
        plus = norm(evaluate(P, signs))**k
        total += minus-plus
    return Fraction(total, 2**(len(later)+1))


def norm_coefficients(cap: int) -> tuple[list[int], list[int]]:
    """mu_K aggregated by norm, and largest ideal-prime norm, S over 2,3."""
    spf = list(range(cap+1))
    for p in range(2, math.isqrt(cap)+1):
        if spf[p] == p:
            for n in range(p*p, cap+1, p):
                if spf[n] == n:
                    spf[n] = p
    coef = [0]*(cap+1); largest = [0]*(cap+1)
    coef[1] = 1; largest[1] = 1
    for n in range(2, cap+1):
        p = spf[n]; m = n; exponent = 0
        while m % p == 0:
            m //= p; exponent += 1
        if p in (2, 3):
            continue
        if p % 3 == 1 and exponent <= 2:
            local = -2 if exponent == 1 else 1
            coef[n] = coef[m]*local
            largest[n] = max(largest[m], p)
        elif p % 3 == 2 and exponent == 2:
            coef[n] = -coef[m]
            largest[n] = max(largest[m], p*p)
    return coef, largest


def main() -> dict:
    D = 48; cap = 2*D
    primes = ideal_primes(cap)
    ideals = squarefree_ideals(primes, cap)
    bound = math.isqrt(2*13)+2
    rows = [(a, b) for a in range(-bound, bound+1) for b in range(-bound, bound+1)
            if 0 < norm((a, b)) <= 13]
    require(len(rows) == 54, 'row_domain')
    coef, largest = norm_coefficients(cap)
    counted = Counter()
    for mask, n in ideals:
        counted[n] += (-1)**mask.bit_count()
    for n in range(1, cap+1):
        require(counted[n] == coef[n], 'all_ideal_norm_coefficients')
    require(sum(p.p == 7 for p in primes) == 2, 'conjugate_ideals_retained')
    require(any(p.q == 25 and p.root is None for p in primes), 'inert_ideal_retained')

    paths = {}; plus = minus = zeros = 0
    for row_index, u in enumerate(rows):
        phases = [p.character(u) for p in primes]
        for p, phase in zip(primes, phases):
            require(phase == ZERO or power(phase, 6) == ONE, 'sextic_values_and_zeros')
            require(p.character(mul(u, u)) == mul(phase, phase), 'local_multiplicativity')
            require(p.character(power(u, 6)) == (ZERO if phase == ZERO else ONE),
                    'sixth_power_masks')
        P: Poly = {}
        for mask, n in ideals:
            w = weight_numerator(n, D)
            if not w:
                continue
            z = ONE
            for i, phase in enumerate(phases):
                if mask & (1 << i):
                    z = mul(z, phase)
            if z != ZERO:
                P[mask] = scale(z, w)
        orders = [1, 2, 3, 4] if row_index < 6 or u == (1, 0) else [1, 2]
        for k in orders:
            Q = poly_power(P, k); current = P.copy()
            sequence = [energy(Q)]
            for i, prime in enumerate(primes):
                bit = 1 << i
                Qnext = freeze(Q, bit)
                cross_twice = 0
                for mask, z in Q.items():
                    if not mask & bit:
                        other = Q.get(mask | bit, ZERO)
                        prod = mul(z, conj(other))
                        cross_twice += 2*prod[0]-prod[1]
                delta = energy(Qnext)-energy(Q)
                require(delta == -cross_twice, 'exact_walsh_flux')
                plus += delta > 0; minus += delta < 0; zeros += delta == 0
                remaining_bits = sorted({1 << j for mask in current for j in range(len(primes))
                                         if j != i and mask & (1 << j)})
                if len(remaining_bits) <= 4:
                    require(delta == direct_increment(current, bit, k, remaining_bits),
                            'independent_sign_enumeration')
                current = freeze(current, bit)
                if i in (0, len(primes)//2, len(primes)-1):
                    require(Qnext == poly_power(current, k), 'freeze_and_power_commute')
                Q = Qnext
                sequence.append(energy(Q))
                if prime.q**2 > cap:
                    require(all(mask.bit_count() <= 1 for mask in current),
                            'single_large_prime_exact')
                    mean = current.get(0, ZERO)
                    smooth = ZERO
                    for mask, n in ideals:
                        if any(mask & (1 << j) for j in range(i+1, len(primes))):
                            continue
                        z = ONE
                        for j, phase in enumerate(phases):
                            if mask & (1 << j): z = mul(z, phase)
                        smooth = add(smooth, scale(z, (-1)**mask.bit_count()*weight_numerator(n, D)))
                    require(mean == smooth, 'native_friable_mean')
            require(sequence[-1] == norm(current.get(0, ZERO))**k, 'native_endpoint')
            require(sum(b-a for a, b in zip(sequence, sequence[1:])) == sequence[-1]-sequence[0],
                    'full_telescope')
            if u == (1, 0):
                paths[str(2*k)] = sequence
    require(plus > 0 and minus > 0, 'reject_monotone_freezing')
    # Wrongly setting nonunit characters to one must fail on an actual row.
    p7 = next(p for p in primes if p.p == 7)
    require(p7.character((-p7.root, 1)) == ZERO, 'reject_erased_zero_mask')
    require(counted[49] == 1 and coef[7] == -2, 'reject_collapsed_conjugate_primes')

    # Actual generators, literal prime masks, and exact unchanged rough replicas.
    principal: Poly = {mask: (weight_numerator(n, D), 0) for mask, n in ideals
                       if weight_numerator(n, D)}
    for qi, q in enumerate(primes):
        if q.root is None:
            generator = (q.p, 0)
        else:
            zbound = 2*math.isqrt(q.q)+2
            candidates = [(a, b) for a in range(-zbound, zbound+1)
                          for b in range(-zbound, zbound+1)
                          if norm((a, b)) == q.q and q.character((a, b)) == ZERO]
            require(bool(candidates), 'prime_ideal_generator_exists')
            generator = candidates[0]
        replica = power(generator, 6)
        require(norm(replica) == q.q**6, 'physical_replica_height')
        for pi, p in enumerate(primes):
            require(p.character(replica) == (ZERO if pi == qi else ONE),
                    'exact_prime_replica_zero_pattern')
        masked = {mask: z for mask, z in principal.items() if not mask & (1 << qi)}
        plain = principal.copy()
        for pi, p in enumerate(primes):
            if p.q >= q.q:
                break
            masked = freeze(masked, 1 << pi)
            plain = freeze(plain, 1 << pi)
            require(masked.get(0, ZERO) == plain.get(0, ZERO),
                    'rough_prime_replica_mean_unchanged')

    for j in range(9):
        R = [0] + [(-2)**i for i in range(1, 10)]
        T = [3**i for i in range(10)]
        lhs = sum(math.comb(j, ell)*(-1)**ell*R[ell]*(-1)**(j-ell)*T[j-ell]
                  for ell in range(j+1))
        rhs = (-1)**j*sum(math.comb(j, ell)*R[ell]*T[j-ell] for ell in range(j+1))
        require(lhs == rhs, 'mellin_leibniz_sign')
    for r in range(7):
        Wjets = [0]*r + [5] + [0]*8
        Rjets = [0, 7] + [0]*8
        jet = sum(math.comb(r+1, ell)*Rjets[ell]*Wjets[r+1-ell] for ell in range(r+2))
        require(jet == (r+1)*7*5, 'first_nonzero_mellin_jet')

    # Exact finite principal illustration. Not asymptotic verification.
    co, la = norm_coefficients(200_000)
    table = []
    for d in (1000, 10000, 100000):
        full = sum(co[n]*weight_numerator(n, d) for n in range(d, 2*d+1))
        for num, den in ((3, 5), (3, 4), (9, 10)):
            y = 1
            # Integer binary search avoids any floating cutoff ambiguity.
            lo, hi = 1, 2*d
            while lo <= hi:
                mid = (lo+hi)//2
                if mid**den <= d**num:
                    y = mid; lo = mid+1
                else: hi = mid-1
            mean_num = sum(co[n]*weight_numerator(n, d) for n in range(d, 2*d+1)
                           if la[n] <= y)
            table.append({'D': d, 'theta': f'{num}/{den}', 'Y': y,
                          'mean_numerator': mean_num, 'full_numerator': full,
                          'common_denominator': d**4})
    return {
        'status': 'finite exact identities only; no asymptotic certification',
        'scope': {'field': 'Q(sqrt(-3))', 'excluded': 'prime ideals over 2 and 3',
                  'D': D, 'column_cap': cap, 'prime_ideals': len(primes),
                  'all_squarefree_ideal_columns_below_cap': len(ideals),
                  'element_rows': len(rows),
                  'moment_coverage': 'orders 2,4 on all rows; 6,8 on first six rows and row 1',
                  'weight': 'W0(t)=30(t-1)^2(2-t)^2 on [1,2], zero outside; C^1 diagnostic'},
        'checks_by_category': dict(sorted(COUNTS.items())),
        'total_predicates': sum(COUNTS.values()),
        'flux_step_sign_counts': {'positive': plus, 'negative': minus, 'zero': zeros},
        'principal_paths_integer_numerators': paths,
        'path_denominator_for_order_2k': 'D^(8k)',
        'prime_norms_in_path_order': [p.q for p in primes],
        'native_principal_illustrations_not_asymptotic_evidence': table,
    }


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, sort_keys=True))

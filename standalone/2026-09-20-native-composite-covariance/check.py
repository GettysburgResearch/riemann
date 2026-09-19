#!/usr/bin/env python3
"""NCG28 finite reconstruction. Integers/Fraction and outward dyadic bounds only.

The infinite native-sector theorem is a written proof, not a consequence of
this finite checker. No parent producer is imported or executed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import gcd, isqrt, lcm
from pathlib import Path

BITS = 112
SCALE = 1 << BITS
IV = tuple[int, int]
ZERO: IV = (0, 0)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def root(n: int, degree: int) -> int:
    require(type(n) is int and n >= 0 and degree > 0, 'invalid root')
    lo, hi = 0, 1 << ((n.bit_length() + degree - 1) // degree)
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if mid ** degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


@lru_cache(None)
def factors(n: int) -> tuple[tuple[int, int], ...]:
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            out.append((p, a))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


@lru_cache(None)
def divisors(n: int) -> tuple[int, ...]:
    out = [1]
    for p, a in factors(n):
        out = [d * p ** j for d in out for j in range(a + 1)]
    return tuple(sorted(out))


def mobius_trial(n: int) -> int:
    fs = factors(n)
    return 0 if any(a > 1 for _, a in fs) else (-1) ** len(fs)


def mobius_sieve(n: int) -> list[int]:
    mu = [1] * (n + 1)
    mu[0] = 0
    composite = bytearray(n + 1)
    for p in range(2, n + 1):
        if not composite[p]:
            for j in range(p, n + 1, p):
                mu[j] = -mu[j]
                if j > p:
                    composite[j] = 1
            for j in range(p * p, n + 1, p * p):
                mu[j] = 0
    return mu


def prime(q: int) -> bool:
    return factors(q) == ((q, 1),)


def pp_base(q: int) -> int:
    fs = factors(q)
    return fs[0][0] if len(fs) == 1 else 0


def jordan2(q: int) -> int:
    return sum(mobius_trial(q // d) * d * d for d in divisors(q))


def rational(x: F | int) -> IV:
    x = F(x)
    a = x.numerator * SCALE
    return a // x.denominator, -((-a) // x.denominator)


def add(a: IV, b: IV) -> IV:
    return a[0] + b[0], a[1] + b[1]


def neg(a: IV) -> IV:
    return -a[1], -a[0]


def sub(a: IV, b: IV) -> IV:
    return add(a, neg(b))


def mul(a: IV, b: IV) -> IV:
    v = [a[i] * b[j] for i in (0, 1) for j in (0, 1)]
    return min(v) // SCALE, -((-max(v)) // SCALE)


def square(a: IV) -> IV:
    low = 0 if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2)
    high = max(a[0] ** 2, a[1] ** 2)
    return low // SCALE, -((-high) // SCALE)


def times(a: IV, x: F | int) -> IV:
    x = F(x)
    v = (a[0] * x.numerator, a[1] * x.numerator)
    return min(v) // x.denominator, -((-max(v)) // x.denominator)


def contains(a: IV, x: F | int) -> bool:
    return F(a[0], SCALE) <= x <= F(a[1], SCALE)


def overlap(a: IV, b: IV) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


def sumiv(xs) -> IV:
    a = b = 0
    for lo, hi in xs:
        a += lo
        b += hi
    return a, b


def log_series(x: F) -> tuple[F, F]:
    """Exact positive atanh series for 1<=x<=2, including its entire tail."""
    require(F(1) <= x <= 2, 'log series range')
    z = (x - 1) / (x + 1)
    z2, power, acc = z * z, z, F()
    for j in range(96):
        acc += 2 * power / (2 * j + 1)
        power *= z2
    tail = 2 * power / (193 * (1 - z2))
    return acc, acc + tail


@lru_cache(None)
def log_iv(n: int) -> IV:
    require(n >= 1, 'log domain')
    e = n.bit_length() - 1
    a, b = log_series(F(n, 1 << e))
    c, d = log_series(F(2))
    return rational(a + e * c)[0], rational(b + e * d)[1]


def harmonics(stop: int, extra: set[int]) -> tuple[list[IV], dict[int, IV]]:
    """Stream to the maximum requested argument; keep only the needed values."""
    wanted = {x for x in extra if x > stop}
    last = max(wanted, default=stop)
    require(last <= 20_000_000, 'bounded campaign limit exceeded')
    small = [ZERO]
    other = {}
    lo = 0
    for n in range(1, last + 1):
        lo += SCALE // n
        v = (lo, lo + n)  # every reciprocal rounding error is <= 1 unit
        if n <= stop:
            small.append(v)
        elif n in wanted:
            other[n] = v
    return small, other


def completion(Y: int) -> tuple[list[F], F]:
    require(type(Y) is int and 2 <= Y <= 127, 'Y outside bounded checker range')
    mu = mobius_sieve(Y)
    require(all(mu[n] == mobius_trial(n) for n in range(1, Y + 1)), 'seed mismatch')
    c = [F(v) for v in mu]
    m, energy = F(), F()
    for n in range(1, Y + 1):
        m += c[n] / n
        energy += m * m
    while m:
        n = len(c)
        v = -min(F(3), n * abs(m)) * (1 if m > 0 else -1)
        c.append(v)
        m += v / n
    require(len(c) - 1 <= 2 * Y, 'completion support')
    return c, energy


def amplitudes(c: list[F]) -> tuple[dict[int, F], list[F], list[int], int]:
    """Producer: gcd-partition formula. Independent check: product convolution."""
    L = len(c) - 1
    U = [F()] * (L * L + 1)
    for d in range(1, L + 1):
        U[d] = sum((c[n] / n for n in range(d, L + 1, d)), F())
    require(U[1] == 0, 'source is not reciprocally balanced')
    amps = {}
    for q in range(2, L * L + 1):
        v = sum((mobius_trial(e) * U[d * e] * U[q // d]
                 for d in divisors(q) for e in divisors(q // d)), F())
        if v:
            amps[q] = v
    D = lcm(*(a.denominator for a in c))
    ci = [int(a * D) for a in c]
    zz = [0] * (L * L + 1)
    for r in range(1, L + 1):
        for s in range(1, L + 1):
            zz[r * s] += ci[r] * ci[s]
    recovered = [F()] * len(zz)
    for q, a in amps.items():
        for d in divisors(q):
            recovered[d] += mobius_trial(q // d) * a
    for d in range(1, len(zz)):
        require(recovered[d] == F(zz[d], D * D * d), 'full B-to-product mismatch')
    for p in range(2, L + 1):
        if prime(p):
            total = F()
            q = p
            while q <= L * L:
                total += amps.get(q, F())
                q *= p
            require(total == 0, 'uncancelled formal prime-log coefficient')
    return amps, U, zz, D


def R(q: int, k: int) -> F:
    return sum((mobius_trial(q // d) * (F(d - 1, 2) - k % d)
                for d in divisors(q)), F())


def component_coefficients(amps: dict[int, F], selected: set[int]) -> tuple[list[tuple[int, IV]], IV]:
    weights: dict[int, F] = {}
    logs: dict[int, F] = {}
    for q in selected:
        a = amps[q]
        for d in divisors(q):
            weights[d] = weights.get(d, F()) + mobius_trial(q // d) * a
        p = pp_base(q)
        if p:
            logs[p] = logs.get(p, F()) + a
    coeff = [(d, rational(a)) for d, a in sorted(weights.items()) if a]
    const = sumiv(times(log_iv(p), a) for p, a in logs.items() if a)
    return coeff, const


def evaluate(coeff: list[tuple[int, IV]], const: IV, k: int, H) -> IV:
    lo, hi = const
    for d, a in coeff:
        v = mul(a, H(k // d))
        lo += v[0]
        hi += v[1]
    return lo, hi


def enc(a: IV) -> dict:
    return {'bits': BITS, 'lower': str(a[0]), 'upper': str(a[1])}


def canonical(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n').encode()


def vector_hash(values) -> str:
    h = hashlib.sha256()
    for row in values:
        h.update(canonical([list(v) for v in row]))
    return h.hexdigest()


def panel(Y: int) -> dict:
    c, F0 = completion(Y)
    L, b, stop = len(c) - 1, Y + 1, (Y + 1) ** 2 - 1
    amps, U, zz, D = amplitudes(c)
    Q = root(Y ** 10, 11)
    primes = {q for q in amps if prime(q)}
    composites = set(amps) - primes
    activation = {}
    for q in composites:
        X = b
        while q ** 11 > Y ** 4 * X ** 6:
            X *= 2
        activation[q] = X
    extra = {activation[q] // 1 - 1 for q in composites}
    extra |= {(activation[q] - 1) // d for q in composites for d in divisors(q)}
    smallH, otherH = harmonics(stop, extra)
    def H(n):
        return smallH[n] if n <= stop else otherH[n]
    def Zq(q, k):
        p = pp_base(q)
        return sumiv([times(H(k // d), mobius_trial(q // d)) for d in divisors(q)]
                     + ([log_iv(p)] if p else []))
    activation_tail = {q: sub(rational(R(q, activation[q] - 1) / activation[q]),
                              Zq(q, activation[q] - 1)) for q in composites}
    prime_spec = component_coefficients(amps, primes)
    fixed_spec = component_coefficients(amps, {q for q in composites if q <= Q})
    # Independently reconstruct EVERY native coefficient in the complete annulus.
    divisor_sum = [0] * (stop + 1)
    for d, z in enumerate(zz):
        if d and z:
            for k in range(d, stop + 1, d):
                divisor_sum[k] += z
    direct_mu = mobius_sieve(stop)
    ci = [int(a * D) for a in c]
    reconstructed = [0] * (stop + 1)
    for k in range(1, stop + 1):
        v = (2 * D * ci[k] if k < len(ci) else 0) - divisor_sum[k]
        require(v % (D * D) == 0, 'nonintegral Newton prefix')
        reconstructed[k] = v // (D * D)
        require(reconstructed[k] == direct_mu[k], 'native Newton coefficient mismatch')
    native, cm = ZERO, ZERO
    rows = []
    E = [ZERO] * 4
    cross = {(i, j): ZERO for i in range(4) for j in range(i + 1, 4)}
    Fnew, fixed_energy = ZERO, ZERO
    first_correction = None
    X = b
    active = set()
    dyn_spec = ([], ZERO)
    correction = ZERO
    for k in range(1, stop + 1):
        native = add(native, rational(F(reconstructed[k], k)))
        if k < len(c):
            cm = add(cm, rational(c[k] / k))
        if k < b:
            continue
        if k == X:
            active = {q for q in composites if activation[q] <= X}
            dyn_spec = component_coefficients(amps, active)
            correction = sumiv(times(activation_tail[q], amps[q])
                               for q in composites - active)
            if first_correction is None:
                first_correction = correction
            X *= 2
        p = evaluate(*prime_spec, k, H)
        naive_low = evaluate(*dyn_spec, k, H)
        low = sub(naive_low, correction)
        fixed = evaluate(*fixed_spec, k, H)
        u = times(cm, 2)
        high = sub(sub(sub(u, native), p), low)
        # Signed components sum to native m. High is the exact complementary
        # transform, evaluated by subtraction after the full coefficient check.
        v = (u, neg(p), neg(low), neg(high))
        require(overlap(sumiv(v), native), 'complete component identity')
        for i in range(4):
            E[i] = add(E[i], square(v[i]))
            for j in range(i + 1, 4):
                cross[i, j] = add(cross[i, j], times(mul(v[i], v[j]), 2))
        Fnew = add(Fnew, square(native))
        fixed_energy = add(fixed_energy, square(fixed))
        rows.append(v)
    ledger = sumiv(E + list(cross.values()))
    require(overlap(ledger, Fnew), 'mixed-term energy ledger')
    require(first_correction is not None and not contains(first_correction, 0),
            'activation correction control unexpectedly contains zero')
    # Finite whole-tail bound (3.3), using EXACT coefficient mass and a simple
    # rational upper bound H_(Q^2)<=1+bit_length(Q^2). No Euler constant is fitted.
    selected = {q for q in composites if q <= Q}
    coefmass = sum((amps[q] ** 2 * F(jordan2(q), 12) for q in selected), F())
    fixed_budget = (F(2, b) + F(4 * Q * Q * (1 + (Q * Q).bit_length()), 3 * b * b)) * coefmass
    require(F(fixed_energy[1], SCALE) <= fixed_budget, 'fixed-sector analytic bound')
    return {
        'Y': Y, 'L': L, 'B': stop, 'fixed_Q': Q,
        'annular_cells': stop - Y, 'nonzero_amplitudes': len(amps),
        'last_activation': max(activation.values(), default=b),
        'seed_F_exact': [str(F0.numerator), str(F0.denominator)],
        'native_F_increment': enc(Fnew), 'native_F_next': enc(add(rational(F0), Fnew)),
        'fixed_composite_energy': enc(fixed_energy),
        'fixed_entire_tail_budget': enc(rational(fixed_budget)),
        'signed_component_order': ['2m_c', '-W_prime', '-W_low_dynamic', '-W_high_dynamic'],
        'component_energies': [enc(a) for a in E],
        'twice_signed_cross_terms': {f'{i},{j}': enc(a) for (i,j),a in cross.items()},
        'first_activation_correction': enc(first_correction),
        'complete_ledger': enc(ledger), 'vector_sha256': vector_hash(rows),
        'centering_prime_log_coefficients': 'all exactly zero after full summation',
        'high_evaluation': 'exact complement after independent full Newton coefficient check',
        'future_mu_use': 'separate finite cross-check only; amplitudes use prefix through Y',
    }


def reject_duplicates(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise ValueError('duplicate JSON key')
        out[k] = v
    return out


def read_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def same_types(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same_types(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same_types(x,y) for x,y in zip(a,b))
    return a == b


def produce(cutoffs: list[int]) -> dict:
    require(cutoffs and len(set(cutoffs)) == len(cutoffs), 'empty/duplicate campaign')
    return {'packet': 'NCG28', 'schema': 1, 'bits': BITS,
            'infinite_theorem_verified_by_code': False, 'RH_proved': False,
            'panels': [panel(y) for y in cutoffs]}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write', type=Path)
    g.add_argument('--check', type=Path)
    ap.add_argument('--cutoffs', type=int, nargs='+', default=[7, 15, 31, 63, 95])
    args = ap.parse_args()
    actual = produce(args.cutoffs)
    if args.write:
        args.write.write_bytes(canonical(actual))
    else:
        require(same_types(read_json(args.check), actual), 'report differs from full reconstruction')
    print('PASS_NCG28', hashlib.sha256(canonical(actual)).hexdigest())


if __name__ == '__main__':
    main()

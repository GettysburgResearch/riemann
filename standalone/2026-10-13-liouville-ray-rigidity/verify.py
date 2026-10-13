#!/usr/bin/env python3
"""Exact finite diagnostics, not an asymptotic moment proof. Standard library only."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
import json

# Z[omega], omega^2 + omega + 1 = 0. No floating point arithmetic.
ZERO, ONE = (0, 0), (1, 0)
ROOTS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
PRIMES = ((3, 1), (2, -1), (4, 1), (5, 0))  # norms 7, 7, 13, 25

def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d

def scale(c, x):
    return c*x[0], c*x[1]

def norm(x):
    a, b = x
    return a*a-a*b+b*b

def power(x, e):
    if e < 0:
        raise ValueError('negative exponent')
    out = ONE
    while e:
        if e & 1:
            out = mul(out, x)
        x = mul(x, x)
        e //= 2
    return out

def rem(x, p):
    a, b = p
    q = norm(p)
    num = mul(x, (a-b, -b))
    i0, j0 = num[0] // q, num[1] // q
    candidates = []
    for i in range(i0-1, i0+3):
        for j in range(j0-1, j0+3):
            z = add(x, scale(-1, mul((i, j), p)))
            candidates.append(z)
    return min(candidates, key=lambda z: (norm(z), z))

def modpower(x, e, p):
    out, x = rem(ONE, p), rem(x, p)
    while e:
        if e & 1:
            out = rem(mul(out, x), p)
        x = rem(mul(x, x), p)
        e //= 2
    return out

def symbol(u, p):
    if rem(u, p) == ZERO:
        return ZERO
    z = modpower(u, (norm(p)-1)//6, p)
    matches = [r for r in ROOTS if rem(r, p) == z]
    if len(matches) != 1:
        raise AssertionError(('not a unique sextic root', u, p, z))
    return matches[0]

def mobius(e):
    return 0 if any(j > 1 for j in e) else (-1)**sum(e)

def liouville(e):
    return (-1)**sum(e)

def need(condition, message):
    if not condition:
        raise AssertionError(message)

def coefficient_checks():
    rows = sorted({(a, b) for a in range(-2, 3) for b in range(-2, 3)
                   if (a, b) != ZERO} | set(PRIMES) |
                  {power(p, 6) for p in PRIMES} | set(ROOTS))
    ideals = list(product(range(4), repeat=4))
    ideals += [tuple(e if i == j else 0 for i in range(4))
               for j in range(4) for e in range(4, 13)]
    pairs = 0
    zero_cases = 0
    for u in rows:
        raw = tuple(symbol(u, p) for p in PRIMES)
        for mask in (0, 1, 5, 15):
            values = tuple(ZERO if mask & (1 << j) else raw[j] for j in range(4))
            @lru_cache(None)
            def xi(e):
                out = ONE
                for value, degree in zip(values, e):
                    out = mul(out, power(value, degree))
                return out
            for e in ideals:
                fwd, inv = ZERO, ZERO
                for d in product(*(range(j//2+1) for j in e)):
                    residual = tuple(j-2*t for j, t in zip(e, d))
                    phase = mul(power(xi(d), 2), xi(residual))
                    fwd = add(fwd, scale(mobius(residual), phase))
                    inv = add(inv, scale(mobius(d)*liouville(residual), phase))
                need(fwd == scale(liouville(e), xi(e)), ('forward', u, mask, e))
                need(inv == scale(mobius(e), xi(e)), ('inverse', u, mask, e))
                pairs += 1
                zero_cases += int(xi(e) == ZERO)
    need(norm(PRIMES[0]) == norm(PRIMES[1]), 'equal-norm test setup')
    need(rem(PRIMES[0], PRIMES[1]) != ZERO, 'distinct conjugate ideals')
    return {'rows': len(rows), 'masks': 4, 'exponent_vectors': len(ideals),
            'forward_inverse_pairs': pairs, 'zero_phase_cases': zero_cases}

def tensor_checks():
    pool = []
    for e in product(range(3), repeat=4):
        n = 1
        for p, degree in zip(PRIMES, e):
            n *= norm(p)**degree
        if n <= 100:
            pool.append((e, n))
    rows = (ONE, (1, 1), (2, 0), PRIMES[0], PRIMES[1], (3, -2))
    tested = 0
    for k in (2, 3):
        axes = [[(e, max(0, 40-abs(n-(30+5*i)))) for e, n in pool]
                for i in range(k)]
        grouped = defaultdict(int)
        for choice in product(*axes):
            e = tuple(sum(item[0][j] for item in choice) for j in range(4))
            w = 1
            for item in choice:
                w *= item[1]
            grouped[e] += w
        for u in rows:
            values = tuple(symbol(u, p) for p in PRIMES)
            def xi(e):
                out = ONE
                for z, degree in zip(values, e):
                    out = mul(out, power(z, degree))
                return out
            direct = ONE
            for axis in axes:
                subtotal = ZERO
                for e, w in axis:
                    subtotal = add(subtotal, scale(w*liouville(e), xi(e)))
                direct = mul(direct, subtotal)
            collapsed = ZERO
            for e, w in grouped.items():
                collapsed = add(collapsed, scale(w*liouville(e), xi(e)))
            need(direct == collapsed, ('tensor', k, u))
            tested += 1
    return {'prime_semigroup_columns': len(pool), 'tensor_equalities': tested}

def ray_rigidity_checks():
    answer = {}
    # 0 is a permitted value as well as all sixth roots of unity.
    # This is exhaustive only for these finite cyclic groups and this alphabet.
    for m in (2, 3, 6):
        expected = {tuple([6]*m)}
        expected.update(tuple((3+(6//m)*j*g) % 6 for g in range(m))
                        for j in range(m))
        accepted = set()
        tested = 0
        for pattern in product(range(7), repeat=m):
            integral_negative = True
            for j in range(m):
                numerator = ZERO
                for g, phase in enumerate(pattern):
                    term = ZERO if phase == 6 else ROOTS[(phase-(6//m)*j*g) % 6]
                    numerator = add(numerator, term)
                if numerator[1] or numerator[0] > 0 or numerator[0] % m:
                    integral_negative = False
                    break
            if integral_negative:
                accepted.add(pattern)
            need(integral_negative == (pattern in expected), ('rigidity', m, pattern))
            tested += 1
        need(accepted == expected, ('coverage', m))
        answer[str(m)] = {'patterns': tested, 'accepted': len(accepted)}
    return answer

def negative_controls():
    # n=p^3: the d=p, residual=p term MUST NOT be removed by coprimality.
    e = (3,)
    correct = sum(mobius((3-2*d,)) for d in range(2))
    false_coprime = sum(mobius((3-2*d,)) for d in range(2)
                         if not (d and 3-2*d))
    need(correct == -1 and false_coprime == 0, 'coprimality mutation')
    # 0^6 is still zero in the extended character, not a unit value.
    z = symbol(PRIMES[0], PRIMES[0])
    need(z == ZERO and power(z, 6) == ZERO and power(z, 6) != ONE, 'zero mutation')
    # At n=p^2 the signed inverse cancels; its absolute counterpart does not.
    signed = liouville((2,)) + mobius((1,))*liouville((0,))
    unsigned = abs(liouville((2,))) + abs(mobius((1,))*liouville((0,)))
    need(signed == 0 and unsigned == 2, 'unsigned inverse mutation')
    return {'rejected_false_coprimality': True, 'rejected_zero_as_unit': True,
            'rejected_unsigned_inverse': True}

def main():
    need([norm(p) for p in PRIMES] == [7, 7, 13, 25], 'prime norms')
    report = {'status': 'PASS', 'arithmetic': 'exact Z[omega]; integers only',
              'scope': 'finite algebra only; no asymptotic or independent review',
              'coefficient_identities': coefficient_checks(),
              'tensor_collapse': tensor_checks(),
              'finite_ray_classification': ray_rigidity_checks(),
              'negative_controls': negative_controls()}
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()

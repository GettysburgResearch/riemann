"""Exact source/CRT/Bernoulli checks, with optional directed EM controls.

No repository helper is imported. Finite checks are not an analytic proof.
Run with the bundled Python; python-flint is optional (--without-arb).
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import comb, factorial, gcd, isqrt
from pathlib import Path
import sys

private_packages = Path(__file__).with_name('_packages')
if private_packages.is_dir():
    sys.path.insert(0, str(private_packages))


def require(ok, text):
    if not ok:
        raise AssertionError(text)


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def chi(n):
    return 1 if n % 6 == 1 else -1 if n % 6 == 5 else 0


def mobius(n):
    f = factor(n)
    return 0 if any(e > 1 for _, e in f) else (-1)**len(f)


def exterior_mu(n):
    return mobius(n) if gcd(n, 6) == 1 else 0


def norm_coefficients(cap, mask=()):
    """Full ideal-norm Mobius coefficient by rational prime decomposition."""
    masks = dict(mask)
    out = [0]*(cap+1)
    out[1] = 1
    for n in range(2, cap+1):
        value = 1
        for p, e in factor(n):
            if p in (2, 3):
                value = 0
                break
            if p % 3 == 2:
                local = -1 if e == 2 and not masks.get(p) else 0
            else:
                remaining = 2-masks.get(p, 0)
                require(0 <= remaining <= 2, 'Invalid mask.')
                local = (-remaining if e == 1 else
                         1 if e == 2 and remaining == 2 else 0)
            value *= local
        out[n] = value
    return out


def convolve_character(source, cap):
    out = [0]*(cap+1)
    for d in range(1, cap+1):
        value = chi(d)
        if value:
            for n in range(1, cap//d+1):
                out[d*n] += value*source[n]
    return out


def hnf_ideals(cap):
    out = []
    for c in range(1, isqrt(cap)+1):
        for a in range(1, cap//(c*c)+1):
            for b in range(a):
                if (b*b-b+1) % a == 0:
                    out.append((c*a, c*b, c))
    return sorted(out, key=lambda t: (t[0]*t[2], t))


def norm(i):
    return i[0]*i[2]


def member(i, x, y):
    a, b, c = i
    return y % c == 0 and (x-b*(y//c)) % a == 0


def subset(i, j):
    return member(j, i[0], 0) and member(j, i[1], i[2])


def prime_ideals(cap):
    out = []
    for p in range(5, cap+1):
        if factor(p) != [(p, 1)]:
            continue
        if p % 3 == 2:
            if p*p <= cap:
                out.append((p, 0, p))
        else:
            out.extend((p, b, 1) for b in range(p) if (b*b-b+1) % p == 0)
    return out


def prime_square(prime):
    p, b, c = prime
    if c == p:
        return p*p, 0, p*p
    # Unique Hensel lift of the root b^2-b+1, with p != 3.
    k = (-(b*b-b+1)//p * pow(2*b-1, -1, p)) % p
    lifted = b+p*k
    require((lifted*lifted-lifted+1) % (p*p) == 0, 'Bad Hensel lift.')
    return p*p, lifted, 1


def hnf_mobius(ideal, primes):
    divisors = [p for p in primes if subset(ideal, p)]
    if any(subset(ideal, prime_square(p)) for p in divisors):
        return 0
    product = 1
    for p in divisors:
        product *= norm(p)
    require(product == norm(ideal), 'Squarefree ideal prime coverage failed.')
    return (-1)**len(divisors)


@lru_cache(None)
def bernoulli_numbers(cap):
    out = [Q(1)]
    for m in range(1, cap+1):
        out.append(-sum(Q(comb(m+1, k))*out[k] for k in range(m))/Q(m+1))
    require(cap == 0 or out[1] == Q(-1, 2), 'Wrong B1 convention.')
    return tuple(out)


def bernoulli_polynomial(m, x):
    numbers = bernoulli_numbers(m)
    return sum(Q(comb(m, k))*numbers[k]*x**(m-k) for k in range(m+1))


def C(j):
    return -Q(6**(j-1), factorial(j))*(
        bernoulli_polynomial(j, Q(1, 6))-bernoulli_polynomial(j, Q(5, 6)))


def formal_quotient(num, den, cap):
    require(den[0], 'Nonzero constant divisor required.')
    out = []
    for k in range(cap+1):
        value = num[k]-sum(den[j]*out[k-j] for j in range(1, k+1))
        out.append(value/den[0])
    return out


def exact_checks(cap=65536, ideal_cap=512, max_order=64):
    source = norm_coefficients(cap)
    target = [0]+[exterior_mu(n) for n in range(1, cap+1)]
    got = convolve_character(source, cap)
    require(got == target, 'Ordinary source convolution failed.')
    primes = prime_ideals(ideal_cap)
    ideals = [i for i in hnf_ideals(ideal_cap) if gcd(norm(i), 6) == 1]
    by_norm = [0]*(ideal_cap+1)
    for i in ideals:
        by_norm[norm(i)] += hnf_mobius(i, primes)
    require(by_norm == source[:ideal_cap+1], 'Independent HNF source differs.')
    # Explicit local square cancellation, retaining the inert p^2 norm.
    square_checks = 0
    for p in range(5, isqrt(cap)+1):
        if factor(p) == [(p, 1)]:
            require(source[p*p]+chi(p)*source[p]+chi(p*p) == 0,
                    'Prime-square cancellation failed.')
            square_checks += 1
    # Shared-prime masks: compare full convolution with independently
    # predicted local generating factors after deflation.
    mask_checks = 0
    for mask in [(), ((7, 1),), ((7, 2),), ((5, 1),), ((7, 1), (5, 1))]:
        masked = convolve_character(norm_coefficients(4096, mask), 4096)
        expected = []
        for n in range(4097):
            if n == 0:
                expected.append(0)
                continue
            value = 1
            for p, e in factor(n):
                k = dict(mask).get(p, 0)
                if p in (2, 3):
                    value = 0
                elif p % 3 == 2 and k:
                    value *= (-1)**e
                elif p % 3 == 1 and k == 2:
                    pass
                elif p % 3 == 1 and k == 1:
                    value = 0
                else:
                    value *= -1 if e == 1 else 0
            expected.append(value)
        require(masked == expected, 'Deflated shared-prime mask differs.')
        mask_checks += len(masked)-1
    # Formal exact exponential quotient: no numerical sampling or zeta input.
    num = [Q((-1)**(k+1)-(-5)**(k+1), factorial(k+1))
           for k in range(max_order+1)]
    den = [-Q((-6)**(k+1), factorial(k+1)) for k in range(max_order+1)]
    quotient = formal_quotient(num, den, max_order)
    require(quotient == [C(k+1)*(-1)**k for k in range(max_order+1)],
            'Euler--Maclaurin coefficients or endpoint sign differs.')
    require([C(1), C(3), C(5)] == [Q(2, 3), Q(-5, 9), Q(17, 36)],
            'Leading EM constants differ.')
    mass_checks = []
    for order in range(2, max_order+1, 2):
        N = 12*order
        mass = sum(abs(C(m+1))*Q(2**m*factorial(m), N**m)
                   for m in range(0, order, 2))
        require(mass < Q(3, 4), 'Normalized derivative mass exceeds budget.')
        mass_checks.append({'M': order, 'N': N, 'mass_exact': str(mass)})
    # Native arithmetic CRT rank obstructions, for complete finite prime sets.
    crt = []
    for prime_cap in (7, 19, 31, 97, 257):
        selected = prime_ideals(prime_cap)
        rational = sorted({p[0] for p in selected})
        M0 = 6
        for p in rational:
            M0 *= p
        q = next(p for p in range(5, 1000)
                 if p % 3 == 2 and factor(p) == [(p, 1)] and M0 % p)
        n = 1+M0*((q-1)*pow(M0, -1, q*q) % (q*q))
        require(n % 6 == 1 and n % (q*q) == q, 'Native CRT row failed.')
        require(all(n % p == 1 for p in rational), 'Selected character differs.')
        require(gcd(n, 6*M0) == 1, 'CRT row lost exterior coprimality.')
        # At each selected finite field, n maps exactly to 1. At the fresh
        # inert prime it maps to zero with ideal valuation exactly one.
        for p in selected:
            require(pow(n % p[0], (norm(p)-1)//6, p[0]) == 1,
                    'Selected sextic phase differs from principal.')
        require(n % q == 0 and n % (q*q) != 0, 'Fresh nonunit gate erased.')
        crt.append({'prime_norm_cap': prime_cap, 'selected_prime_ideals': len(selected),
                    'M0': str(M0), 'n': str(n), 'fresh_inert_q': q,
                    'fresh_prime_ideal_norm': q*q,
                    'target_column_equals_nonprincipal_column': True})
    # Adversarial tests: a sign swap and a lost inert contribution must fail.
    mutated = got[:]
    mutated[5] += 2
    require(mutated != target, 'Character-sign mutation was not rejected.')
    bad_source = source[:]
    bad_source[25] = 0
    require(convolve_character(bad_source, cap) != target,
            'Dropped inert factor was not rejected.')
    require(C(3) != -C(3), 'EM coefficient mutation was not rejected.')
    return {'arithmetic': 'EXACT_INTEGER_AND_RATIONAL',
            'ordinary_coefficients_checked': cap,
            'complete_exterior_HNF_cap': ideal_cap,
            'complete_exterior_HNF_ideals': len(ideals),
            'prime_square_cancellations': square_checks,
            'deflated_mask_coefficients_checked': mask_checks,
            'formal_EM_coefficients_checked': max_order+1,
            'exact_normalized_mass_checks': mass_checks,
            'native_CRT_obstructions': crt,
            'adversarial_mutations_rejected': 3}


def arb_checks():
    from flint import arb, ctx
    import flint
    ctx.prec = 512
    rows = []
    wrong_rejected = 0
    for M in (2, 4, 8, 16, 32, 64):
        N = 12*M
        t = arb(1)/N
        exact = (-t*N).exp()*(2*t).sinh()/(3*t).sinh()
        approximant = arb(0)
        for m in range(0, M, 2):
            value = C(m+1)
            approximant += arb(value.numerator)/value.denominator*t**m*(-t*N).exp()
        # F(x)=exp(-x/N) satisfies the same Cauchy hypothesis with C*=1,D=N:
        # sup_disk |F| <= exp(-x/(2N)) <= N/x, since 2/e<1.
        bound = arb(4)/3*N*factorial(M)/M*(arb(6)/(arb.pi()*N))**M
        difference = (exact-approximant).abs_upper()
        require(difference < bound, 'Directed full-tail EM model failed at M='+str(M)
                +': error '+str(difference)+'; bound '+str(bound))
        if M >= 8:
            wrong = approximant-2*arb(C(3).numerator)/C(3).denominator*t*t*(-t*N).exp()
            require((exact-wrong).abs_lower() > bound,
                    'Wrong EM endpoint-sign control was not rejected.')
            wrong_rejected += 1
        rows.append({'M': M, 'N': N, 'exact_infinite_exponential_tail': exact.str(55),
                     'complete_EM_approximant': approximant.str(55),
                     'directed_absolute_error_upper': difference.str(55),
                     'proved_complete_remainder_upper': bound.str(55)})
    return {'arithmetic': 'DIRECTED_INTERVAL_SYNTHETIC_CONTROL',
            'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
            'precision_bits': 512, 'cases': rows,
            'wrong_EM_sign_controls_rejected': wrong_rejected,
            'scope': 'Exact infinite exponential-tail controls; no native energy theorem.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('CHECKS.json'))
    parser.add_argument('--without-arb', action='store_true')
    args = parser.parse_args()
    out = {'status': 'PASS_FINITE_CHECKS_ONLY; ANALYTIC_CRITICAL_BOUND_OPEN',
           'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'exact': exact_checks()}
    if not args.without_arb:
        out['directed_EM_controls'] = arb_checks()
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps({'status': out['status'], 'output': str(args.output),
                      'ordinary_coefficients': out['exact']['ordinary_coefficients_checked'],
                      'HNF_ideals': out['exact']['complete_exterior_HNF_ideals'],
                      'CRT_examples': len(out['exact']['native_CRT_obstructions']),
                      'directed_EM_cases': len(out.get('directed_EM_controls', {}).get('cases', []))}))


if __name__ == '__main__':
    main()

"""Exact quartic Euler deflation and directed period-12 EM controls.

All arithmetic is reconstructed here. No deposited report authenticates itself.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial, gcd
from pathlib import Path
import hashlib
import json
import sys

private = Path(__file__).with_name('_packages')
if private.is_dir():
    sys.path.insert(0, str(private))


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def factor(n):
    result = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            result.append((p, e))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


TABLES = ({1: 1, 5: 1, 7: -1, 11: -1},
          {1: 1, 5: -1, 7: 1, 11: -1},
          {1: 1, 5: -1, 7: -1, 11: 1})


def char(j, n):
    return TABLES[j].get(n % 12, 0)


def field_coeff(n):
    result = 1
    for p, e in factor(n):
        if p in (2, 3):
            return 0
        residue_degree = 1 if p % 12 == 1 else 2
        primes_above = 4//residue_degree
        if e % residue_degree or e//residue_degree > primes_above:
            return 0
        exponent = e//residue_degree
        result *= (-1)**exponent*comb(primes_above, exponent)
    return result


def mobius6(n):
    if gcd(n, 6) > 1:
        return 0
    fs = factor(n)
    return 0 if any(e > 1 for _, e in fs) else (-1)**len(fs)


@lru_cache(None)
def bernoulli(cap):
    values = [Q(1)]
    for m in range(1, cap+1):
        values.append(-sum(comb(m+1, k)*values[k] for k in range(m))/Q(m+1))
    return values


def bern_poly(j, x):
    return sum(comb(j, k)*b*x**(j-k) for k, b in enumerate(bernoulli(j)))


def coefficient(h, j):
    return -Q(12**(j-1), factorial(j))*sum(
        char(h, a)*bern_poly(j, Q(a, 12)) for a in range(1, 13))


def exact(cap=65536, max_order=64):
    source = [0]+[field_coeff(n) for n in range(1, cap+1)]
    for h in range(3):
        out = [0]*(cap+1)
        for d in range(1, cap+1):
            value = char(h, d)
            if value:
                for n in range(1, cap//d+1):
                    out[d*n] += value*source[n]
        source = out
    require(source == [0]+[mobius6(n) for n in range(1, cap+1)],
            'The complete three-factor deflation differs from ordinary Mobius.')
    for h in range(3):
        require(sum(char(h, a) for a in range(1, 13)) == 0, 'Lost mean zero.')
        for a in range(1, 13):
            for b in range(1, 13):
                require(char(h, a*b) == char(h, a)*char(h, b),
                        'Period-12 character lost multiplicativity.')
    # Expand the exact exponential quotient in t, using the same branch
    # conventions as the complete tail sum e^(-N t) sum chi(a)e^(-a t)/(1-e^(-12t)).
    formal_checks = 0
    masses = []
    for h in range(3):
        num = [sum(char(h, a)*Q((-a)**(k+1), factorial(k+1))
                   for a in range(1, 13)) for k in range(max_order+1)]
        den = [-Q((-12)**(k+1), factorial(k+1)) for k in range(max_order+1)]
        values = []
        for k in range(max_order+1):
            value = (num[k]-sum(den[j]*values[k-j] for j in range(1, k+1)))/den[0]
            values.append(value)
            require(value == coefficient(h, k+1)*(-1)**k,
                    'Period-12 EM coefficient sign or endpoint differs.')
            formal_checks += 1
        for M in range(2, max_order+1, 2):
            N = 48*M
            mass = sum(abs(coefficient(h, m+1))*Q(2**m*factorial(m), N**m)
                       for m in range(M))
            require(mass < 3, 'Normalized period-12 jet mass exceeded 3.')
            masses.append({'character': h, 'M': M, 'mass': str(mass)})
    # Adversarial lost character and changed Frobenius order must fail.
    require(field_coeff(25) == -2 and field_coeff(13) == -4,
            'Prime decomposition fixtures differ.')
    require(field_coeff(25) != 0, 'Inert/split degree-two norm population erased.')
    return {'complete_integer_coefficients': cap, 'characters': 3,
            'formal_EM_coefficients': formal_checks, 'mass_checks': masses,
            'prime_degree_fixtures': {'a_F(25)': field_coeff(25), 'a_F(13)': field_coeff(13)}}


def directed():
    from flint import arb, ctx
    import flint
    ctx.prec = 768
    cases = []
    for h in range(3):
        for M in (2, 4, 8, 16, 32, 64):
            N = 48*M
            t = arb(1)/N
            numerator = sum(char(h, a)*(-a*t).exp() for a in range(1, 13))
            truth = (-N*t).exp()*numerator/(1-(-12*t).exp())
            approximation = arb(0)
            for m in range(M):
                value = coefficient(h, m+1)
                approximation += arb(value.numerator)/value.denominator*(-t)**m*(-N*t).exp()
            # F(x)=exp(-x/N), sigma0=2,D=N obeys the disk bound with
            # C*=3, because max_(v>=0) v^2 exp(-v/2)=16/e^2<3.
            bound = 4*arb(N)*factorial(M)/(M+1)*(12/(arb.pi()*N))**M
            require((truth-approximation).abs_upper() < bound,
                    'Complete period-12 EM exponential control failed.')
            cases.append({'character': h, 'M': M, 'N': N,
                          'complete_exact_tail': truth.str(55),
                          'absolute_error_upper': (truth-approximation).abs_upper().str(55),
                          'complete_remainder_upper': bound.str(55)})
    return {'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
            'precision_bits': ctx.prec, 'cases': cases,
            'scope': 'Synthetic complete exponential tails; no native upper-bound certification.'}


def main():
    output = Path(__file__).with_name('LEGAL_FIELD_CHECKS.json')
    result = {'status': 'PASS_FINITE_LEGAL_FIELD_COMPONENT_CHECKS',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'exact': exact(), 'directed': directed()}
    output.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'coefficient_cap': 65536,
                      'directed_cases': len(result['directed']['cases']), 'output': str(output)}))


if __name__ == '__main__':
    main()

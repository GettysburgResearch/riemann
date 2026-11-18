"""Sharpen the remaining individual tests using periodic summation and Arb."""
import argparse
import csv
import io
import lzma
from decimal import Decimal, localcontext
from functools import lru_cache
from math import comb, isqrt
from pathlib import Path

import numpy as np
from flint import arb, arb_series, ctx

from census import character, DISCRIMINANT_LIMIT, PERIODS


ctx.prec = 128
SCALE = 2**56
DEGREE = 24
MAX_PHASE = 1_000_000


def initial_tables():
    nmax = PERIODS*DISCRIMINANT_LIMIT
    weights = np.zeros((nmax+1, 4), dtype=np.int64)
    with localcontext() as context:
        context.prec = 40
        for n in range(1, nmax+1):
            log_n = Decimal(n).ln()
            weights[n] = (SCALE//n, int(SCALE*log_n/n),
                          SCALE//n**2, int(SCALE*log_n/n**2))
    return weights


@lru_cache(maxsize=None)
def coefficients(j, k):
    shifted = arb_series([j+k, 1], prec=2).zeta(PERIODS)
    factor = (-1)**k * comb(j+k-1, k)
    harmonic = sum(1/arb(i) for i in range(j, j+k))
    return factor*shifted[0], factor*(shifted[1]+harmonic*shifted[0])


def ratios(char, weights):
    q = len(char)
    nmax = PERIODS*q
    residues = np.roll(char, -1)
    sums = residues @ weights[1:nmax+1].reshape(PERIODS, q, 4).sum(axis=0)
    fractions = [arb(int(s), 2*nmax)/SCALE for s in sums]
    nonzero = [(r, int(c)) for r, c in enumerate(residues, 1) if c]
    moments = [arb(sum(c*r**k for r, c in nonzero))/(q**k)
               for k in range(1, DEGREE+1)]
    log_q = arb(q).log()
    ans = []
    for off, j in ((0, 1), (2, 2)):
        f, deriv = arb(0), arb(0)
        for k, m in enumerate(moments, 1):
            a, b = coefficients(j, k)
            f += m*a
            deriv += m*b
        remainder = arb(0, '1e-23')
        val = fractions[off] + f/q**j + remainder
        neg_deriv = fractions[off+1] - (deriv-log_q*f)/q**j + remainder
        assert val > 0
        ans.append(neg_deriv/val)
    return ans


def prime_powers():
    prime = np.ones(MAX_PHASE+1, dtype=np.bool_)
    prime[:2] = False
    for p in range(2, isqrt(MAX_PHASE)+1):
        if prime[p]:
            prime[p*p::p] = False
    data = []
    for p in np.flatnonzero(prime):
        n = int(p)
        while n <= MAX_PHASE:
            data.append((n, int(p)))
            n *= int(p)
    return np.array(sorted(data), dtype=np.int64).T


def best_phase(q, char, powers, primes, b1, b2):
    # The maximum is only a proposal. Precise testing follows in reflected().
    w = np.log(primes) * char[powers % q] / powers**2
    line_slope = np.cumsum(w) - float(b2)
    intercept = float(b1) - np.cumsum(powers*w)
    # In each gap the score/ sqrt(x) is affine. Test the knots as a cheap search.
    scores = np.sqrt(powers)*(line_slope*powers + intercept)
    i = int(np.argmax(scores))
    return int(powers[i]), float(scores[i])


@lru_cache(maxsize=None)
def log_p(p):
    return arb(p).log()


def reflected(x, d, char, powers, primes, b1, b2):
    n = int(np.searchsorted(powers, x, side='left'))
    # Fixed-point vector summation for the untrusted search is replaced by Arb.
    correction = arb(0)
    for power, prime, sign in zip(powers[:n], primes[:n], char[powers[:n] % len(char)]):
        if sign:
            t = int(power)
            correction += log_p(int(prime))*(int(sign)*(x-t))/t**2
    a = int(d<0)
    arch = 1/(arb(x)**(1+a)*(1+a)*(2+a))
    return arb(x).sqrt()*(b1-x*b2+correction+arch)


def absolute_majorant(q, a, b1, b2):
    ell = (arb(q)/arb.pi()).log()
    first = ell + (arb(1+a)/2).digamma()-2*b1
    second = (ell+(arb(2+a)/2).digamma()-2*b2)/3
    assert first > 0 and second > 0
    return (first*second).sqrt()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--first', type=Path, default=Path('witnesses.tsv.xz'))
    parser.add_argument('--output', type=Path, default=Path('refined.tsv'))
    args = parser.parse_args()
    with lzma.open(args.first, 'rt') as handle:
        done = {int(row['discriminant']) for row in csv.DictReader(handle, delimiter='\t')}
    weights = initial_tables()
    powers, primes = prime_powers()
    with args.output.open('w') as handle:
        writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
        writer.writerow(('discriminant', 'decision', 'phase_x', 'directed_milli'))
        for d in sorted(range(-DISCRIMINANT_LIMIT, DISCRIMINANT_LIMIT+1), key=abs):
            if abs(d) <= 1 or d in done:
                continue
            char = character(d)
            if char is None:
                continue
            b1, b2 = ratios(char, weights)
            majorant = absolute_majorant(abs(d), int(d<0), b1, b2)
            if majorant < arb(2)/3:
                writer.writerow((d, 'negative_on_grh', 0, int((1000*majorant).upper().ceil().unique_fmpz())))
                continue
            x, approx = best_phase(abs(d), char, powers, primes, b1, b2)
            if approx > 0.66:
                lower = reflected(x, d, char, powers, primes, b1, b2)
                if lower > arb(2)/3:
                    writer.writerow((d, 'both_signs', x, int((1000*lower).lower().floor().unique_fmpz())))
                    continue
            writer.writerow((d, 'open', 0, 0))


if __name__ == '__main__':
    main()

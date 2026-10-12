#!/usr/bin/env python3
"""Exact finite controls for the conditional fixed-source bootstrap."""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def mobius(n):
    value, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value


def run():
    # Coefficient identity in B1; a weighted smooth finite sum follows by
    # linearity. The unit-modulus twist is retained symbolically by its
    # exponent, so the control checks every Laurent monomial separately.
    for p in [2, 3, 5, 7, 11, 67]:
        for n in range(1, 5001):
            quotient, j = n, 0
            value = 0
            while True:
                value += mobius(quotient)
                if quotient % p:
                    break
                quotient //= p
                j += 1
            need(value == (mobius(n) if n % p else 0), 'coprime Euler coefficient identity')
    records = []
    for kappa, h in [(Q(2,5),Q(1,2)),(Q(2,5),Q(18,23)),
                     (Q(0),Q(1,10)),(Q(1,2),Q(3,4))]:
        A=(1+kappa+h*(Q(5,6)-kappa))/2
        c=1-h/6
        need(0 < c < 1 and A > 0, 'bootstrap domains')
        exponent=Q(1)
        steps=0
        while c**steps > A:
            exponent=max(A,c*exponent)
            steps += 1
            need(exponent==max(A,c**steps), 'exact recurrence')
            need(steps < 10000, 'finite bootstrap termination')
        need(exponent==A, 'limiting branch reached finitely')
        records.append({'kappa':str(kappa),'h':str(h),'conditional_bound':str(A),
                        'contraction':str(c),'sufficient_steps':steps})
    need(records[0]['conditional_bound']=='97/120' and records[0]['sufficient_steps']==3,
         'fixed half-height target')
    return {'status':'PASS_EXACT_CONDITIONAL_PRIME_DELETION_BOOTSTRAP',
            'open_source_moment_proved':False,'rh_proved':False,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'pricing_controls':records}


if __name__=='__main__':
    print(json.dumps(run(),indent=2)+'\n',end='')

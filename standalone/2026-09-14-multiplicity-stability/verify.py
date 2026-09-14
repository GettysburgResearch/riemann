#!/usr/bin/env python3
"""Exact bounded checks for the multiplicity-sensitive stability deduction.

This does NOT replay the imported seven-gap continuum certificate, prove the
pair-correlation theorem, evaluate zeta, or mechanically verify PROOF.md.
Only Python's standard library is used. No assert controls acceptance.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import factorial, isqrt
from pathlib import Path
import random


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        need(self.lo <= self.hi, 'reversed interval')

    @staticmethod
    def lift(x):
        return x if isinstance(x, Interval) else Interval(x)

    def __add__(self, x):
        x = self.lift(x)
        return Interval(self.lo+x.lo, self.hi+x.hi)
    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, x):
        return self + -self.lift(x)

    def __rsub__(self, x):
        return self.lift(x) + -self

    def __mul__(self, x):
        x = self.lift(x)
        v = [self.lo*x.lo, self.lo*x.hi, self.hi*x.lo, self.hi*x.hi]
        return Interval(min(v), max(v))
    __rmul__ = __mul__

    def __truediv__(self, x):
        x = self.lift(x)
        need(not x.lo <= 0 <= x.hi, 'zero denominator')
        return self * Interval(1/x.hi, 1/x.lo)

    def __rtruediv__(self, x):
        return self.lift(x)/self

    def square(self):
        if self.lo <= 0 <= self.hi:
            return Interval(0, max(self.lo*self.lo, self.hi*self.hi))
        return Interval(min(self.lo*self.lo, self.hi*self.hi),
                        max(self.lo*self.lo, self.hi*self.hi))

    def sqrt(self, bits=192):
        need(self.lo >= 0, 'negative square root')
        scale = 1 << bits
        a = isqrt((self.lo.numerator*scale*scale)//self.lo.denominator)
        b = isqrt((self.hi.numerator*scale*scale)//self.hi.denominator)
        return Interval(F(a, scale), F(b+1, scale))

    def decimals(self, places=30):
        s = 10**places
        a = (self.lo.numerator*s)//self.lo.denominator
        b = -((-self.hi.numerator*s)//self.hi.denominator)
        def fmt(n):
            sign = '-' if n < 0 else ''
            n = abs(n)
            return f'{sign}{n//s}.{n%s:0{places}d}'
        return [fmt(a), fmt(b)]


def cos_and_sinc_at_inv_sqrt_two():
    # Alternating series at x^2=1/2; odd last index is a lower bound.
    # Successive term magnitudes decrease, including the first term.
    def partial(last, shift):
        return sum((F((-1)**j, 2**j*factorial(2*j+shift))
                    for j in range(last+1)), F(0))
    return (Interval(partial(31, 0), partial(32, 0)),
            Interval(partial(31, 1), partial(32, 1)))


def psi(x: F, h: F) -> F:
    return (x-1)**2-max(x-h, F(0))**2


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def transpose(a):
    return [list(c) for c in zip(*a)]


def check_scalar_and_matrix():
    nscalar = 0
    for h in [F(1), F(3, 2), F(2), F(17, 5), F(4)]:
        for lam in [F(j, 4) for j in range(25)]:
            optimum = max(lam-h, F(0))
            fmin = lam*lam-max(lam-h, F(0))**2
            need((lam-optimum)**2+2*h*optimum == fmin, 'scalar minimizer')
            for v in [F(j, 3) for j in range(16)]:
                need((lam-v)**2+2*h*v >= fmin, 'scalar inequality')
                nscalar += 1
    # Noncommuting real symmetric matrices with known rational spectra.
    # P has trace m; Q's orthogonal conjugation is not aligned with P.
    nmatrix = 0
    rng = random.Random(20260914)
    for m in range(2, 8):
        for rep in range(12):
            raw = [rng.randrange(1, 20) for _ in range(m)]
            eigen_p = [F(m*x, sum(raw)) for x in raw]
            eigen_q = [F(rng.randrange(-9, 10), 3) for _ in range(m)]
            o = [[F(int(i == j)) for j in range(m)] for i in range(m)]
            for j in range(m-1):
                for row in o:
                    a, b = row[j], row[j+1]
                    row[j], row[j+1] = (3*a+4*b)/5, (-4*a+3*b)/5
            ot = transpose(o)
            need(mm(o, ot) == [[F(int(i == j)) for j in range(m)]
                              for i in range(m)], 'orthogonality')
            q = mm([[o[i][j]*eigen_q[j] for j in range(m)]
                    for i in range(m)], ot)
            t = [[q[i][j]+(eigen_p[i] if i == j else 0)
                  for j in range(m)] for i in range(m)]
            energy = sum((v*v for row in t for v in row), F(0))
            tr = sum((t[i][i] for i in range(m)), F(0))
            b = sum(v > 0 for v in eigen_q)
            for h in [F(2), F(17, 5), F(4)]:
                defect = sum((psi(x, h) for x in eigen_p), F(0))
                rhs = 2*h*tr-h*h*b-(2*h-1)*m+defect
                need(energy >= rhs, 'free-threshold stability')
                nmatrix += 1
    return nscalar, nmatrix


def check_caps():
    rng = random.Random(1701)
    count = 0
    for m in range(2, 13):
        for _ in range(80):
            raw = [rng.randrange(0, 21) for _ in range(m)]
            if not sum(raw):
                raw[0] = 1
            eig = [F(m*x, sum(raw)) for x in raw]
            energy = sum(((x-1)**2 for x in eig), F(0))
            for h in [F(1), F(3, 2), F(2), F(17, 5), F(4)]:
                defect = sum((psi(x, h) for x in eig), F(0))
                cap = F(m, m-1)*(h-1)**2
                need(defect >= min(energy, cap), 'spectral cap')
                target = cap*F(3, 4)
                pressure = max(target-energy, F(0))
                need(defect+pressure >= target, 'cap absorption')
                count += 1
    return count


def check_multiplicities():
    count = 0
    for mults in product(range(1, 6), repeat=4):
        central, off = mults[:2], mults[2:]
        n = sum(central)+2*sum(off)
        r = sum(central)
        s = sum(x == 1 for x in central)
        bad = 2*sum(x for x in off if x >= 2)
        b_allreal = len(off)
        b_simple = sum(x >= 2 for x in central)+len(off)
        need(F(b_allreal) <= F(n-r, 2)-F(bad, 4), 'all-real inertia')
        need(F(b_simple) <= F(n-s, 2)-F(bad, 4), 'simple-real inertia')
        ns = s+2*sum(x == 1 for x in off)
        need(ns+r == n+s-bad, 'union/intersection ledger')
        count += 1
    return count


def check_windows():
    count = 0
    for k in [1, 2, 6, 8]:
        for m in range(k+1, k+25):
            charges = [0]*(m-1)
            for start in range(m-k):
                for j in range(start, start+k):
                    charges[j] += 1
            need(sum(charges) == k*(m-k), 'exact window pressure')
            need(max(charges) <= k, 'gap multiplicity')
            for span in range(1, k+1):
                for i in range(m-span):
                    copies = sum(start <= i and i+span <= start+k
                                 for start in range(m-k))
                    need(F(2*copies, k+1-span) <= 2, 'pair capacity')
            count += 1
    # Directly count all block offsets on several finite input lists.
    for n, m, k in [(35, 11, 6), (31, 9, 6), (29, 13, 8)]:
        full = []
        for offset in range(m):
            full.extend(range(offset, n-m+1, m))
        need(sorted(full) == list(range(n-m+1)), 'offset coverage')
        gap_charge = [0]*(n-1)
        for start in full:
            for w in range(start, start+m-k):
                for j in range(w, w+k):
                    gap_charge[j] += 1
        need(max(gap_charge) <= k*(m-k), 'global pressure')
        count += 1
    for m, k in [(1536, 6), (269, 6), (963, 8)]:
        charges = [0]*(m-1)
        for start in range(m-k):
            for j in range(start, start+k):
                charges[j] += 1
        need(sum(charges) == k*(m-k), 'headline window count')
        count += 1
    return count


def reconstruct():
    scalar, matrices = check_scalar_and_matrix()
    caps = check_caps()
    mult = check_multiplicities()
    windows = check_windows()
    cosine, sinc = cos_and_sinc_at_inv_sqrt_two()
    energy = F(1, 2)+cosine/sinc
    h0 = 2+Interval(2).sqrt()
    old_union = 1-4*(energy-1)/h0.square()
    epsilon, pressure = F(19, 5000), F(1, 3000)
    m, k = 1536, 6
    target = epsilon*(m-k)
    d = target/m
    tax = pressure*k*F(m-k, m)
    h = 2+Interval(2-2*d).sqrt()
    cap = F(m, m-1)*(h-1).square()
    need(cap.lo > target, 'headline cap not established')
    need(d == F(969, 256000), 'd exact normalization')
    need(d-tax == F(459, 256000), 'net pressure normalization')
    new_union = 1-4*(energy-1-d+tax)/h.square()
    improvement = new_union-old_union
    need(new_union.lo > F('0.88805965'), 'union lower bound')
    need(new_union.hi < F('0.88805966'), 'union upper display')
    need(improvement.lo > F('0.00043964'), 'strict comparison')
    m = 269
    target_avg = epsilon*(m-k)
    da = target_avg/m
    ba = pressure*k*F(m-k, m)
    need(target_avg <= F(m, m-1), 'average cap')
    average = (1+(2-energy-ba)/(1-da))/2
    need(average.lo > F('0.83652292'), 'average lower bound')
    # Optional corollary: these numbers are imported, NOT reconstructed
    # window integrals or a replay of the external nine-point certificate.
    m, k, ep, pp = 963, 8, F(15211, 2500000), F(1, 2500)
    target9 = ep*(m-k)
    d9 = target9/m
    b9 = pp*k*F(m-k, m)
    h9 = 2+Interval(2-2*d9).sqrt()
    need((F(m, m-1)*(h9-1).square()).lo > target9, 'optional cap')
    energy9 = 2-F(3362285207, 5000000000)
    union9 = 1-4*(energy9-1-d9+b9)/h9.square()
    need(union9.lo > F('0.88830717'), 'optional conditional comparison')
    return {
        'status': 'proposed mathematical deduction; independent review required',
        'rh_proved': False,
        'seven_gap_certificate_replayed': False,
        'pair_correlation_reproved': False,
        'checks': {'scalar': scalar, 'noncommuting_matrices': matrices,
                   'spectral_cap': caps, 'multiplicity': mult, 'windows': windows},
        'MT_pair_energy': energy.decimals(),
        'Lamzouri_union': old_union.decimals(),
        'union_1536': new_union.decimals(),
        'union_gain': improvement.decimals(),
        'threshold_h': h.decimals(),
        'cap_minus_target': (cap-target).decimals(),
        'average_269': average.decimals(),
        'optional_nine_point_union_IMPORTS_NOT_REPLAYED': union9.decimals(),
    }


def no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path)
    parser.add_argument('--write', type=Path)
    args = parser.parse_args()
    need(bool(args.check) != bool(args.write), 'choose --check or --write')
    out = reconstruct()
    if args.check:
        supplied = json.loads(args.check.read_text(encoding='utf-8'),
                              object_pairs_hook=no_duplicates)
        need(canonical(supplied) == canonical(out), 'reconstruction mismatch')
        print('PASS: exact bounded reconstruction; imported analytic inputs NOT replayed')
    else:
        args.write.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

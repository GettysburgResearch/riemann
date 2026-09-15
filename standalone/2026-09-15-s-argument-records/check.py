#!/usr/bin/env python3
"""SARG26: directed scalar replay, NOT a Hardy-Z evaluator.

Python >=3.10, standard library only. All transcendental enclosures use
384-bit outward integer arithmetic and explicit convergent-series tails.
See RESEARCH.md for the analytic remainder and monotone-defect argument.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
import sys

BITS = 384
SCALE = 1 << BITS
ROOT = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def ceildiv(a, b):
    return -((-a) // b)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self):
        need(self.lo <= self.hi, 'reversed interval')

    def __add__(self, other):
        b = iv(other)
        return I(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-iv(other))

    def __rsub__(self, other):
        return iv(other) + (-self)

    def __mul__(self, other):
        b = iv(other)
        p = [x*y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(p)//SCALE, ceildiv(max(p), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = iv(other)
        need(not b.lo <= 0 <= b.hi, 'division interval contains zero')
        return self * I(SCALE*SCALE//b.hi, ceildiv(SCALE*SCALE, b.lo))

    def __rtruediv__(self, other):
        return iv(other) / self


def iv(x):
    if isinstance(x, I):
        return x
    need(type(x) in (int, str, Q), 'exact inputs only; floats/bools forbidden')
    q = Q(x)
    return I(q.numerator*SCALE//q.denominator,
             ceildiv(q.numerator*SCALE, q.denominator))


def hull(a, b):
    a, b = iv(a), iv(b)
    return I(a.lo, b.hi)


def error(e):
    e = iv(e)
    r = max(abs(e.lo), abs(e.hi))
    return I(-r, r)


def atanh2(z, terms=180):
    """2*atanh(z), 0 <= z <= 1/3, including complete positive tail."""
    z = iv(z)
    need(0 <= z.lo and z.hi*3 <= SCALE+3, 'atanh domain')
    z2, p, out = z*z, z, iv(0)
    for j in range(terms):
        out += 2*p/(2*j+1)
        p *= z2
    tail = 2*p/((2*terms+1)*(1-z2))
    return out + I(0, tail.hi)


@lru_cache(None)
def log2():
    return atanh2(Q(1, 3))


@lru_cache(None)
def log_point(q):
    q = Q(q)
    need(q > 0, 'log domain')
    k = q.numerator.bit_length() - q.denominator.bit_length()
    r = q / (Q(2)**k)
    while r < 1:
        r *= 2
        k -= 1
    while r >= 2:
        r /= 2
        k += 1
    return atanh2((r-1)/(r+1)) + k*log2()


def log_interval(a):
    a = iv(a)
    need(a.lo > 0, 'log interval domain')
    return I(log_point(Q(a.lo, SCALE)).lo, log_point(Q(a.hi, SCALE)).hi)


def atan_small(q, terms=180):
    z, p, out = iv(q), iv(q), iv(0)
    need(0 < Q(q) < 1, 'atan domain')
    z2 = z*z
    for j in range(terms):
        out += (1 if j % 2 == 0 else -1)*p/(2*j+1)
        p *= z2
    return out + error(p/(2*terms+1))


@lru_cache(None)
def pi():
    return 16*atan_small(Q(1, 5))-4*atan_small(Q(1, 239))


def decimal_integer(n, places):
    sign = '-' if n < 0 else ''
    n = abs(n)
    base = 10**places
    return f'{sign}{n//base}.{n%base:0{places}d}' if places else sign+str(n)


def bounds(a, places=12):
    a, p = iv(a), 10**places
    return [decimal_integer(a.lo*p//SCALE, places),
            decimal_integer(ceildiv(a.hi*p, SCALE), places)]


def inward_core(left, right, places=9):
    p = 10**places
    # One extra unit makes endpoints strictly interior, even in exact ties.
    lo = ceildiv(left.hi*p, SCALE)+1
    hi = right.lo*p//SCALE-1
    need(lo < hi, 'empty core')
    return [decimal_integer(lo, places), decimal_integer(hi, places)]


def one(pattern, text):
    found = re.findall(pattern, text, flags=re.M)
    need(len(found) == 1, f'expected one match: {pattern}')
    return found[0]


def parse_news(text):
    text = text.replace('\u2212', '-')
    sections = text.split('Certificate for ')[1:]
    need(len(sections) == 2, 'need two certificate sections')
    records = []
    number = r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?'
    for i, section in enumerate(sections, 1):
        t = int(one(rf'^t{i}=(\d+)$', text))
        n = int(one(rf'^N\(t{i}\)=(\d+)$', section))
        count, width = one(r'(\d+) Hardy-Z brackets, width (\.[0-9]+)\.', section)
        body = section.split('endpoints:')[1].split('Turing:')[0]
        starts = [Q(x) for x in body.split()]
        w = Q(width)
        need(len(starts) == int(count), 'bracket count mismatch')
        need(all(-20 < x < x+w < 20 for x in starts), 'padding domain')
        need(all(a+w < b for a, b in zip(starts, starts[1:])), 'overlap/order')
        need(all(x+w < 0 or x > 0 for x in starts), 'bracket straddles anchor')
        gamma = tuple(map(Q, one(rf'γ{i}-t{i}∈\[({number}),({number})\]', text)))
        need(gamma[0] < gamma[1], 'record interval order')
        idx = [j for j, x in enumerate(starts) if x <= gamma[0] < gamma[1] <= x+w]
        need(len(idx) == 1, 'fine bracket must refine exactly one coarse bracket')
        neg = sum(x < 0 for x in starts)
        need(idx[0] == (neg-1 if i == 1 else neg), 'record/anchor adjacency')
        quoted_s = tuple(map(Q, one(rf'^({number})<S\(γ{i}[+-]0\)<({number})$', text)))
        quoted_d = tuple(map(Q, one(rf'D∈\[({number}),({number})\] ⇒ D=0', section)))
        supplied = one(rf'I\+=({number}), I-=({number}), B=({number}), E\+=({number}), E-=({number})', section)
        z = re.findall(rf'Z\(t{i}({number})\)∈\[({number}),({number})\]', section)
        need(len(z) == 2, 'need two record endpoint intervals')
        zz = [tuple(map(Q, v)) for v in z]
        need(tuple(v[0] for v in zz) == gamma, 'record endpoint binding')
        need(all(v[1] <= v[2] for v in zz), 'Z interval order')
        need(zz[0][1] > 0 and zz[1][2] < 0, 'quoted signs do not separate zero')
        records.append(dict(id=i, t=t, n=n, starts=starts, width=w,
                            gamma=gamma, index=idx[0], printed=tuple(map(Q, supplied)),
                            quoted_s=quoted_s, quoted_d=quoted_d))
    return records


class Model:
    def __init__(self, record):
        self.r = record
        t = record['t']
        need(t > 10**20, 'this affine certificate requires t > 10^20')
        ell = log_point(Q(t))-log2()-log_interval(pi())
        self.a = ell/(2*pi())
        self.b = record['n']-(iv(t)/(2*pi())*(ell-1)+Q(7, 8))
        self.e = 101/(pi()*(t-20))
        self.B = iv('2.067')+iv('.059')*log_point(Q(t+20))

    def brackets(self, refined):
        r = self.r
        return [r['gamma'] if refined and j == r['index'] else (x, x+r['width'])
                for j, x in enumerate(r['starts'])]

    def s_at(self, lo, hi, count_delta=0):
        return self.b+count_delta-self.a*hull(lo, hi)+error(self.e)

    def half(self, h, side, refined):
        h = Q(h)
        need(0 < h <= 20 and side in (-1, 1), 'half-window domain')
        loc = [(j, u, v) for j, (u, v) in enumerate(self.brackets(refined))
               if (-h <= u < v < 0 if side == -1 else 0 < u < v <= h)]
        mids = [(u+v)/2 for _, u, v in loc]
        err = sum(((v-u)/2 for _, u, v in loc), Q(0))
        val = h*self.b-side*self.a*(h*h/2)
        val += sum((h-x for x in mids), Q(0)) if side == 1 else -sum((h+x for x in mids), Q(0))
        nominal = val+error(h*self.e)
        integral = nominal+error(err)
        budget = self.B-integral if side == 1 else self.B+integral
        return dict(h=h, loc=loc, error=err, nominal=nominal,
                    integral=integral, budget=budget)

    def pair(self, left, right, refined):
        m, p = self.half(left, -1, refined), self.half(right, 1, refined)
        defect = I((-m['budget']/m['h']).lo, (p['budget']/p['h']).hi)
        need(-SCALE < defect.lo <= 0 <= defect.hi < SCALE, 'integer anchor not isolated')
        core = inward_core(m['budget']-m['h'], p['h']-p['budget'])
        return dict(m=m, p=p, defect=defect, core=core)


def half_report(h):
    return dict(padding=str(h['h']), count=len(h['loc']),
                midpoint_integral=bounds(h['nominal']), root_uncertainty=str(h['error']))


def pair_report(p):
    return dict(left=half_report(p['m']), right=half_report(p['p']),
                anchor_defect=bounds(p['defect']), conditional_complete_core=p['core'])


PADS = {1: ('7', '7.32'), 2: ('7.67', '7.34')}


def reconstruct(text):
    result = dict(schema='SARG26.scalar-replay.v1', arithmetic='384-bit outward integer intervals',
                  source_sha256=hashlib.sha256(text.encode()).hexdigest(),
                  status='SCALAR_REPLAY_PASSED_PRIMITIVE_Z_REPLAY_PENDING',
                  primitive_z_replayed=False, record_independently_certified=False,
                  rh_established=False, records=[])
    jobs = []
    for r in parse_news(text):
        m = Model(r)
        full = m.pair(20, 20, False)
        ip, im, bp, ep, em = r['printed']
        for half, printed in ((full['p'], ip), (full['m'], im)):
            d = half['nominal']-printed
            need(d.lo > -iv('0.00000005').lo and d.hi < iv('0.00000005').lo,
                 'printed midpoint integral fails 7-place rounding check')
        need(m.B.hi < iv(bp).lo and (iv(bp)-m.B).hi < iv('0.0000001').lo,
             'printed B is not an outward 7-place bound')
        need(full['p']['error'] == ep and full['m']['error'] == em, 'printed E mismatch')
        dl, du = r['quoted_d']
        need(iv(dl).hi <= full['defect'].lo and full['defect'].hi <= iv(du).lo,
             'printed D fails outward enclosure')
        small = m.pair(*PADS[r['id']], True)
        need(Q(small['core'][0]) < -1 and Q(small['core'][1]) > 1, 'compressed core must contain [-1,1]')
        rec = m.s_at(*r['gamma'])
        sl, su = r['quoted_s']
        need(iv(sl).hi < rec.lo and rec.hi < iv(su).lo, 'printed S fails strict enclosure')
        target = iv('4.1843') if r['id'] == 1 else iv('-4.3383')
        need(rec.lo > target.hi if r['id'] == 1 else rec.hi < target.lo, 'record target fails')
        all_brackets = m.brackets(True)
        j = r['index']
        u, v = (all_brackets[j], all_brackets[j+1]) if r['id'] == 1 else (all_brackets[j-1], all_brackets[j])
        gap = hull(v[0]-u[1], v[1]-u[0])
        normalized = m.a*gap
        chosen = sorted(small['m']['loc']+small['p']['loc'])
        for j, lo, hi in chosen:
            jobs.append((r['id'], str(r['t']), j, str(lo), str(hi)))
        result['records'].append(dict(id=r['id'], t=str(r['t']), claimed_N=str(r['n']),
            supplied_brackets=len(r['starts']), S_at_anchor=bounds(m.s_at(0, 0)),
            density=bounds(m.a), recomputed_B=bounds(m.B), full=pair_report(full),
            compressed=pair_report(small), compressed_indices=[j for j, _, _ in chosen],
            conditional_S_record=bounds(rec), adjacent_gap=bounds(gap),
            normalized_adjacent_gap=bounds(normalized)))
    result['full_coarse_brackets'] = sum(r['supplied_brackets'] for r in result['records'])
    result['compressed_brackets'] = len(jobs)
    result['compressed_endpoint_jobs'] = 2*len(jobs)
    return result, jobs


def unique_object(pairs):
    out = {}
    for k, v in pairs:
        need(k not in out, 'duplicate JSON key')
        out[k] = v
    return out


def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--news', type=Path, default=ROOT/'news.txt')
    p.add_argument('--check', type=Path)
    p.add_argument('--jobs', type=Path, help='write exact rational endpoint job TSV')
    p.add_argument('--require-primitive', action='store_true', help='fail: no Z backend exists in this packet')
    args = p.parse_args()
    try:
        result, jobs = reconstruct(args.news.read_text(encoding='utf-8'))
        if args.check:
            expected = json.loads(args.check.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
            need(canonical(result) == canonical(expected), 'result differs from complete reconstruction')
        if args.require_primitive:
            raise ValueError('primitive Hardy-Z endpoint evaluation is not implemented or replayed')
        if args.jobs:
            args.jobs.write_text('record\tt_integer\tcoarse_index_0based\tleft_offset_rational\tright_offset_rational\n'+
                                 ''.join('\t'.join(map(str, row))+'\n' for row in jobs), encoding='utf-8')
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError, KeyError, IndexError, ZeroDivisionError) as e:
        print(f'REFUSED: {e}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

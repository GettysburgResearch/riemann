#!/usr/bin/env python3
"""Exact bounded controls and rigorous scalar enclosures for SR26.

This does not rerun the imported seven-point certificate or prove pair
correlation. Infinite-dimensional and analytic arguments are paper proofs.
Standard library only; no floating-point arithmetic enters acceptance.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import factorial, isqrt
from pathlib import Path


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        require(self.lo <= self.hi, 'reversed interval')

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        o = I.cast(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I.cast(other)

    def __rsub__(self, other):
        return I.cast(other) + -self

    def __mul__(self, other):
        o = I.cast(other)
        v = [self.lo * o.lo, self.lo * o.hi,
             self.hi * o.lo, self.hi * o.hi]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I.cast(other)
        require(not o.lo <= 0 <= o.hi, 'division through zero')
        return self * I(1 / o.hi, 1 / o.lo)

    def square(self):
        if self.lo >= 0:
            return I(self.lo ** 2, self.hi ** 2)
        if self.hi <= 0:
            return I(self.hi ** 2, self.lo ** 2)
        return I(0, max(self.lo ** 2, self.hi ** 2))


def sqrt_i(q: F, bits=220) -> I:
    require(q >= 0, 'negative square root')
    scale = 1 << bits
    k = isqrt((q.numerator * scale * scale) // q.denominator)
    out = I(F(k, scale), F(k + 1, scale))
    require(out.lo ** 2 <= q <= out.hi ** 2, 'square root bound')
    return out


def alternating(odd: bool, terms=48) -> I:
    """cos(1/sqrt2), or sin(1/sqrt2)/(1/sqrt2), with next-term bound."""
    shift = int(odd)
    s = sum(((-1) ** k * F(1, 2 ** k * factorial(2*k+shift))
             for k in range(terms)), F(0))
    nxt = (-1) ** terms * F(1, 2 ** terms * factorial(2*terms+shift))
    return I(min(s, s+nxt), max(s, s+nxt))


def outward_decimal(x: I, places=18):
    scale = 10 ** places
    lo = x.lo.numerator * scale // x.lo.denominator
    hi = -((-x.hi.numerator * scale) // x.hi.denominator)
    return {'lo': str(F(lo, scale)), 'hi': str(F(hi, scale))}


def bound(m: int, c: F, h0: I):
    q = F(19*(m-6), 5000)
    u = sqrt_i(F(m-1, m)*q)
    b = c-1
    if u.hi <= b:
        defect = I(q)
    else:
        require(u.lo > b, 'ambiguous clipping branch')
        defect = q - (u-b).square()
    penalty = (c-2)**2/2
    denominator = 1-penalty-defect/m
    require(denominator.lo > 0, 'nonpositive density denominator')
    value = (h0-penalty-F(m-1, 500*m))/denominator
    return value, defect


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, length-1):
                yield (first,)+rest


def spectral_controls():
    """Check the sharp bound without approximating an eigenvalue or square root."""
    count = sharp = 0
    for m in range(2, 7):
        for row in compositions(2*m, m):
            lam = [F(x,2) for x in row]
            xs = [x-1 for x in lam]
            energy = sum((x*x for x in xs), F(0))
            for c in (F(1), F(3,2), F(2), F(400059,200000), F(3)):
                b=c-1
                excess = sum((max(x-b, F(0))**2 for x in xs), F(0))
                if excess:
                    slack=F(m-1,m)*energy-b*b-excess
                    require(slack>=0 and slack*slack>=4*b*b*excess,
                            'sharp spectral envelope fails')
                count += 1
        # Exact attainable one-outlier spectra at every sampled rational height.
        for numerator in range(0, 3*(m-1)+1):
            u=F(numerator,3)
            xs=[u]+[-u/(m-1)]*(m-1)
            energy=sum(x*x for x in xs)
            require(F(m-1,m)*energy == u*u, 'extremal energy')
            for c in (F(1), F(3,2), F(2), F(400059,200000), F(3)):
                observed=energy-sum(max(x-(c-1),F(0))**2 for x in xs)
                expected=energy-max(u-(c-1),F(0))**2
                require(observed==expected, 'sharpness witness')
                sharp += 1
    # The stronger false assertion Delta >= E is explicitly rejected.
    xs=[F(2),F(-1),F(-1)]
    e=sum(x*x for x in xs)
    delta=e-sum(max(x-F(1),F(0))**2 for x in xs)
    require(delta < e, 'negative control does not separate')
    return count,sharp


def scalar_controls():
    count=0
    for c in (F(1),F(3,2),F(2),F(400059,200000),F(3)):
        for p in (F(k,8) for k in range(65)):
            minimizing_n=max(p-c,F(0))
            minimum=p*p if p<=c else 2*c*p-c*c
            require((p-minimizing_n)**2+2*c*minimizing_n==minimum,
                    'scalar minimizer')
            for n in (F(k,4) for k in range(25)):
                require((p-n)**2+2*c*n >= minimum,'scalar minimum bound')
                count+=1
    return count


def matrix_controls():
    # P is diagonal with integer eigenvalues, realized by repeated unit columns.
    # Q is genuinely noncommuting, with known inertia via rational Householder.
    z = [F(1), F(2), F(3)]
    norm = sum(x*x for x in z)
    U = [[F(i == j)-2*z[i]*z[j]/norm for j in range(3)] for i in range(3)]
    count = 0
    for eigen in itertools.product((F(-2), F(0), F(3)), repeat=3):
        Q = [[sum(U[i][k]*eigen[k]*U[j][k] for k in range(3))
              for j in range(3)] for i in range(3)]
        b = sum(x > 0 for x in eigen)
        for ps in itertools.product(range(4), repeat=3):
            r = sum(ps)
            A = [[Q[i][j]+(ps[i] if i == j else 0) for j in range(3)]
                 for i in range(3)]
            energy = sum(x*x for row in A for x in row)
            tr = sum(A[i][i] for i in range(3))
            for c in (F(1), F(3,2), F(2), F(400059,200000), F(3)):
                hc = [x*x if x <= c else 2*c*x-c*c for x in ps]
                defect = sum(hc)-r
                lower = 2*c*tr-(2*c-1)*r-c*c*b+defect
                require(energy >= lower, 'noncommuting rank-inertia control')
                count += 1
    return count


def offset_controls():
    count=0
    for m in (2,3,7,269,280,281):
        for size in (0,1,m-1,m,m+1,2*m+3):
            starts=list(range(max(0,size-m+1)))
            require(sum(len([s for s in starts if s%m==a]) for a in range(m))
                    == max(0,size-m+1), 'block offset cover')
            for gap in range(max(0,size-1)):
                multiplicity=sum(s<=gap<s+m-1 for s in starts)
                require(multiplicity<=m-1,'span charge')
            count+=1
    return count


def payload():
    # The input kernel, pressure constant and external scope are deliberately visible.
    h0=F(3,2)-alternating(False)/alternating(True)
    old,old_d=bound(280,F(2),h0)
    new,new_d=bound(281,F(400059,200000),h0)
    older,_=bound(269,F(2),h0)
    gain=new-old
    require(new.lo>F(67300966525,10**11),'new rational lower bound')
    require(gain.lo>F(129,10**10),'strict baseline improvement')
    require(gain.hi<F(131,10**10),'gain magnitude')
    require(old.lo>F(6730096522791,10**13),'baseline reconstruction')
    c1,c2=spectral_controls()
    return {
        'schema':'SR26/v1',
        'status':'PROPOSED_SOURCE_QUALIFIED_NOT_RH',
        'inputs':{'pressure':'19/5000','span_charge':'1/500',
                  'main':'f99d9e3908dde4865377c75d9ca051c1f545bf4f',
                  'new_block':281,'new_threshold':'400059/200000',
                  'old_block':280,'old_threshold':'2'},
        'intervals':{'H0':outward_decimal(h0),
                     'old_269':outward_decimal(older),
                     'old_280':outward_decimal(old),
                     'new_281':outward_decimal(new),
                     'gain_over_280':outward_decimal(gain),
                     'new_block_defect':outward_decimal(new_d)},
        'controls':{'spectral_envelopes':c1,'attained_extrema':c2,
                    'scalar_minima':scalar_controls(),'noncommuting_matrices':matrix_controls(),
                    'offset_panels':offset_controls()},
        'not_executed':['seven_point_exhaustion','pair_correlation_proof',
                        'zeta_zero_census','formalization','full_checkout_validator']
    }


def canonical(data):
    return json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()


def record():
    data=payload()
    return {'payload':data,'sha256':hashlib.sha256(canonical(data)).hexdigest()}


def strict_pairs(items):
    d={}
    for k,v in items:
        require(k not in d, 'duplicate JSON key')
        d[k]=v
    return d


def reject_float(s):
    raise ValueError('noninteger JSON number')


def accept(obj, expected):
    require(type(obj) is dict and set(obj)=={'payload','sha256'}, 'record fields')
    # Comparing canonical encodings prevents True==1 and 1.0==1 aliases.
    require(canonical(obj)==canonical(expected), 'record differs from reconstruction')


def self_test(expected):
    mutations=[]
    for key,value in [('pressure','1/250'),('new_block',280),
                      ('new_threshold','2'),('new_block',True)]:
        a=copy.deepcopy(expected)
        a['payload']['inputs'][key]=value
        mutations.append(a)
    a=copy.deepcopy(expected);a['payload']['status']='RH_PROVED';mutations.append(a)
    a=copy.deepcopy(expected)
    a['payload']['intervals']['new_281']['lo']='674/1000';mutations.append(a)
    for a in mutations:
        a['sha256']=hashlib.sha256(canonical(a['payload'])).hexdigest()
        try:
            accept(a,expected)
        except ValueError:
            pass
        else:
            raise ValueError('resealed mutation accepted')
    try:
        json.loads('{"x":1,"x":2}',object_pairs_hook=strict_pairs)
    except ValueError:
        pass
    else:
        raise ValueError('duplicate accepted')
    return len(mutations)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    expected=record()
    if args.check:
        obj=json.loads(args.check.read_text(),object_pairs_hook=strict_pairs,
                       parse_float=reject_float,parse_constant=reject_float)
        accept(obj,expected)
    if args.write:
        args.write.write_bytes(canonical(expected)+b'\n')
    refused=self_test(expected) if args.self_test else 0
    print(json.dumps({'result':'PASS','sha256':expected['sha256'],
                      'resealed_refusals':refused,'controls':expected['payload']['controls']}))

if __name__=='__main__':
    main()

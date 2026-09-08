#!/usr/bin/env python3
"""Bounded rational controls, not a proof of RH or the analytic mean-square input."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(label)


def rat(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def kernel(m: int, n: int) -> F:
    return F(min(m, n), max(m, n))


def gram_energy(ns: tuple[int, ...], coeff: tuple[F, ...]) -> F:
    return sum((coeff[i] * coeff[j] * kernel(m, n)
                for i, m in enumerate(ns) for j, n in enumerate(ns)), F(0))


def past_energy(ns: tuple[int, ...], coeff: tuple[F, ...], end: int) -> F:
    # The grid coordinate is x=exp(t); the state between events is S/x.
    total = F(0)
    state_numerator = F(0)
    previous = 1
    for n, c in zip(ns, coeff):
        if n > end:
            break
        total += state_numerator**2 * (F(1, previous**2)-F(1, n**2))/2
        state_numerator += n*c
        previous = n
    total += state_numerator**2 * (F(1, previous**2)-F(1, end**2))/2
    return total


def state_energy(ns: tuple[int, ...], coeff: tuple[F, ...]) -> F:
    end = ns[-1]
    numerator = sum((n*c for n, c in zip(ns, coeff)), F(0))
    return past_energy(ns, coeff, end) + numerator**2/F(2*end**2)


def positive_pivots(ns: tuple[int, ...]) -> list[F]:
    a = [[kernel(m, n) for n in ns] for m in ns]
    pivots = []
    for k in range(len(ns)):
        d = a[k][k]
        require(d > 0, 'positive physical Gram pivot')
        pivots.append(d)
        for i in range(k+1, len(ns)):
            for j in range(k+1, len(ns)):
                a[i][j] -= a[i][k]*a[k][j]/d
    return pivots


def run() -> dict:
    groups = []
    def retain(name: str, rows: list) -> None:
        raw = json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()
        groups.append({'name': name, 'cases': len(rows),
                       'rational_payload_sha256': hashlib.sha256(raw).hexdigest()})
    packets = [(2,), (2,3), (2,3,5), (3,5,7,11), (2,4,8), (2,3,4,5,7)]
    norm_rows, cutoff_rows, average_rows, piv_rows = [], [], [], []
    for ns in packets:
        piv_rows.append([list(ns), [rat(x) for x in positive_pivots(ns)]])
        for trial in range(1,6):
            cs = tuple(F((trial*(i+1))%7-3, i+1) for i in range(len(ns)))
            g = gram_energy(ns, cs)
            s = state_energy(ns, cs)
            require(g == 2*s and s >= 0, 'whole future / Fourier factor two')
            c0 = sum((c/n for n,c in zip(ns,cs)), F(0))
            realg = sum((cs[i]*cs[j]*(kernel(m,n)+F(1,m*n))/2
                         for i,m in enumerate(ns) for j,n in enumerate(ns)), F(0))
            require(realg == s+c0*c0/2, 'real-part rank-one correction')
            norm_rows.append([list(ns), [rat(c) for c in cs], rat(g), rat(realg)])
            for end in (1,2,3,6,12):
                tail = s-past_energy(ns,cs,end)
                value = sum((n*c for n,c in zip(ns,cs) if n<=end),F(0))/end
                later = tuple(c if n>end else F(0) for n,c in zip(ns,cs))
                err = state_energy(ns,later)
                require(tail >= 0 and err <= value**2+2*tail, 'complete cutoff error')
                cutoff_rows.append([list(ns),trial,end,rat(err),rat(value**2+2*tail)])
            weights = (F(1,6), F(1,3), F(1,2))
            cuts = (2,5,11)
            avg = tuple(c*sum((w for k,w in zip(cuts,weights) if n<=k),F(0))
                        for n,c in zip(ns,cs))
            rhs = sum((w*state_energy(ns, tuple(c if n<=k else F(0)
                           for n,c in zip(ns,cs))) for k,w in zip(cuts,weights)),F(0))
            require(state_energy(ns,avg) <= rhs, 'finite average Jensen control')
            for n,c,av in zip(ns,cs,avg):
                if n<=min(cuts):
                    require(c==av, 'initial horizon unchanged')
            average_rows.append([list(ns),trial,rat(state_energy(ns,avg)),rat(rhs)])
    retain('physical Gram and complete state future',norm_rows)
    retain('all signed cutoff-error comparisons',cutoff_rows)
    retain('finite average and initial horizon',average_rows)
    retain('strict physical Gram pivots',piv_rows)
    require(F(1,2)/2 == F(1,4), 'prime2 state normalization')
    require(F(1,2)*(1+F(1,4))/2 == F(5,16), 'prime2 real normalization')
    retain('literal prime2 normalization', [['1/4','5/16']])
    # Exact atanh enclosure for log 2, with its full positive series tail.
    z=F(1,3); n=20
    lo=2*sum((z**(2*k+1)/(2*k+1) for k in range(n)),F(0))
    hi=lo+2*z**(2*n+1)/((2*n+1)*(1-z*z))
    require(F(2,3)<lo<hi<F(7,10), 'directed log2 enclosure')
    require(2*(6+4*F(3,2)) == 24, 'sqrt2 upper constant; strictness analytic')
    require(F(16)/(F(2,3)**2) == 36, 'tail constant lower endpoint')
    require(F(24)+F(15,4)<28, 'tail constant K_e')
    require(F(3)+F(18)/(2*F(2,3))<20, 'prime-power transfer constant')
    retain('directed logarithm and transfer constants',
           [[rat(lo),rat(hi)],['24','36','111/4','33/2']])
    # Taylor tails at the fixed safe point in ATTEMPT.md. No exponential oracle.
    q=F(3,4)
    rows=[]
    for n in range(1,13):
        finite_tail=sum((q**k/k for k in range(n+1,n+41)),F(0))
        upper=q**(n+1)/((n+1)*(1-q))
        require(0<finite_tail<upper, 'safe Taylor-tail geometric bound')
        require(F(1,2)-F(1,2)==0, 'synthetic limiting target zero')
        rows.append([n,rat(finite_tail),rat(upper)])
    retain('synthetic safe-limit Taylor controls', rows)
    return {'status':'PASS_BOUNDED_CONTROLS_ONLY','rh_proved':False,
            'conditional_input':'RH implies Cramer mean-square bound; not established here',
            'groups':groups,'total_cases':sum(g['cases'] for g in groups)}


def strict_object(pairs: list) -> dict:
    d={}
    for k,v in pairs:
        require(k not in d, 'duplicate JSON key')
        d[k]=v
    return d


def canonical(x: object) -> str:
    return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument('--check',type=Path)
    args=p.parse_args()
    value=run()
    if args.check:
        saved=json.loads(args.check.read_text(),object_pairs_hook=strict_object)
        require(canonical(saved)==canonical(value),'retained result differs from reconstruction')
    print(json.dumps(value,indent=2,sort_keys=True))


if __name__=='__main__':
    main()

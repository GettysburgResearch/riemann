#!/usr/bin/env python3
"""Exact algebra and finite coefficient counts; optional numerical quadrature.
Not a proof of any infinite arithmetic bound. Runtime checks survive -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import importlib.util
import json
import math

counts: Counter[str] = Counter()

def check(ok: bool, label: str) -> None:
    counts[label] += 1
    if not ok:
        raise RuntimeError(label)


def exact() -> dict:
    vals = [Q(-3), Q(-1, 2), Q(0), Q(2, 3), Q(4)]
    for a, b, x, c in product(vals, vals, vals, (Q(0), Q(1, 2), Q(5, 6))):
        beta, mu = 2*c-1, (a+b)/2
        old = (2*c-1)*x-c*(a+b)-((x-a)**2+(x-b)**2)/4
        new = -(x-mu-beta)**2/2-mu+beta**2/2-(a-b)**2/8
        check(old == new, 'gaussian_kernel_square_completion')
    for alpha, D, N in product((1, 2, 3), (Q(1), Q(7), Q(25)), (Q(4), Q(9), Q(25))):
        lhs = D**(2*alpha-1)/((2*alpha-1)*N**(2*alpha))
        rhs = (D/N)**(2*alpha-1)/(N*(2*alpha-1))
        check(lhs == rhs, 'critical_energy_dilation')
    for m in range(2, 101):
        check(Q(m, 2)-1-Q(m, 2) == -1, 'channel_critical_weight')
        check((m-2)-m == -2, 'second_mass_power_cancellation')
        check(Q(m, 2)-1-m <= -2, 'first_mass_uniform_degree')
    # Complete rational ideal norm counts, with conservative majorants.
    cap = 40000
    spf = list(range(cap+1))
    for p in range(2, math.isqrt(cap)+1):
        if spf[p] == p:
            for n in range(p*p, cap+1, p):
                if spf[n] == n:
                    spf[n] = p
    fixtures = []
    for m in (2, 4, 6, 8):
        first = second = allowed = powerful = 0
        for n in range(1, cap+1):
            v, d, r, ok = n, 1, 1, (math.gcd(n, 6) == 1)
            while v > 1:
                p, e = spf[v], 0
                while v % p == 0:
                    v //= p
                    e += 1
                if e == 1:
                    r *= p
                elif e == m:
                    d *= p
                else:
                    ok = False
            if ok:
                check(r*d**m == n and math.gcd(r, d) == 1, 'unique_occupied_decomposition')
                weight = d**(m//2-1)
                first += weight
                second += weight*weight
                allowed += 1
                powerful += (d != 1)
            check(first <= 2*n and second <= 2*n, 'complete_prefix_mass_bound')
        fixtures.append({'m':m, 'norm_cap':cap, 'allowed_ideals':allowed,
                         'powerful_ideals':powerful, 'first_majorant_mass':first,
                         'second_majorant_mass':second})
    # Explicitly false proposed substitutes.
    check(Q(1, 4) != Q(1, 16), 'reject_wrong_energy_jacobian')
    c, x, a, b = Q(5, 6), Q(0), Q(0), Q(0)
    correct = (2*c-1)*x-c*(a+b)-((x-a)**2+(x-b)**2)/4
    wrong = -(x-(a+b)/2)**2/2-(a+b)/2+(2*c-1)**2/2-(a-b)**2/8
    check(correct != wrong, 'reject_missing_normal_cdf_shift')
    check((1-1)**2 == 0 and 1+1 != 0, 'reject_discarding_equal_norm_cross_terms')
    check(abs((1-Q(1,2))**2-1) > Q(1,2)**2, 'reject_tail_diagonal_only_error')
    check([1, -2, 1] != [1, 0, 0], 'reject_mobius_inverse_sign')
    check(8**2 > 8, 'reject_gram_diagonal_as_full_energy')
    # At a masked prime, p^m must vanish together with p.
    check([1,0,0] != [1,0,-25], 'reject_neutral_power_mask_erasure')
    return {'coefficient_counts':fixtures,
            'counts':dict(sorted(counts.items())),
            'total_predicates_including_prefix_guards':sum(counts.values()),
            'scope':'Finite rational algebra and complete rational-ideal prefix majorants. No analytic certification.'}


def numerical(helper: Path) -> dict:
    import mpmath as mp
    mp.mp.dps = 60
    spec = importlib.util.spec_from_file_location('es_energy', helper)
    if spec is None or spec.loader is None:
        raise RuntimeError('missing primitive helper')
    es = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(es)
    generators = [(-3,-2), (-3,-1), (-5,0)]
    qs = [es.en(p) for p in generators]
    if qs != [7,7,25]:
        raise RuntimeError('prime norm mismatch')
    rows = [(1,0), (2,1), (-3,-2), (-5,0)]
    c = mp.mpf(5)/6
    beta = 2*c-1
    K = mp.exp(beta**2/2)/(2*mp.sqrt(2*mp.pi))
    root6 = mp.mpc(mp.mpf(1)/2, mp.sqrt(3)/2)
    def mpr(v):
        return mp.mpf(v.numerator)/v.denominator
    def cv(v):
        return mpr(Q(v[0])) + mpr(Q(v[1]))*root6
    # Independent embedding checks: helper pairs use zeta_6, not omega.
    for j in range(6):
        target = mp.exp(mp.pi*1j*j/3)
        if abs(cv(es.ROOTS[j])-target)>mp.mpf('1e-50'):
            raise RuntimeError('wrong primitive sixth-root embedding')
    for i,j in product(range(6),repeat=2):
        if abs(cv(es.mul(es.ROOTS[i],es.ROOTS[j]))-cv(es.ROOTS[i])*cv(es.ROOTS[j]))>mp.mpf('1e-50'):
            raise RuntimeError('embedding is not multiplicative')
    badroot = mp.mpc(-mp.mpf(1)/2, mp.sqrt(3)/2)
    if abs(abs(-1+badroot)-1)<mp.mpf('1e-5'):
        raise RuntimeError('failed to reject cubic/sixth-root confusion')
    cases=[]
    for m in (2,6):
        for row in rows:
            chars=[es.prime_character(p,row) for p in generators]
            terms=[]
            for exps in product((0,1,m),repeat=3):
                coef=es.ONE
                N=1
                for q,ch,e in zip(qs,chars,exps):
                    N*=q**e
                    if e==0:
                        fac=es.ONE
                    elif ch is None:
                        fac=es.ZERO
                    elif e==1:
                        fac=es.scale(es.ROOTS[ch],-Q(q-1,q))
                    else:
                        fac=es.scale(es.ROOTS[(m*ch)%6],-Q(q**(m//2-1)))
                    coef=es.mul(coef,fac)
                direct_coef = mp.mpc(1)
                for q,ch,e in zip(qs,chars,exps):
                    if e==0:
                        continue
                    if ch is None:
                        direct_coef = 0
                        break
                    scalar = -mp.mpf(q-1)/q if e==1 else -mp.mpf(q)**(m//2-1)
                    direct_coef *= scalar*mp.exp(mp.pi*1j*(e*ch)/3)
                if abs(cv(coef)-direct_coef)>mp.mpf('1e-45')*max(1,abs(direct_coef)):
                    raise RuntimeError('independent character coefficient mismatch')
                terms.append((mp.log(N),cv(coef)))
            D=128 if m==2 else 7**6
            L=mp.log(D)
            pair=mp.mpc(0)
            diagonal=mp.mpf(0)
            for i,(a,ca) in enumerate(terms):
                for j,(b,cb) in enumerate(terms):
                    ker=K*mp.exp(-(a+b)/2-(a-b)**2/8)*mp.erfc(-(L-(a+b)/2-beta)/mp.sqrt(2))/2
                    pair+=ca*mp.conj(cb)*ker
                    if i==j:
                        diagonal+=abs(ca)**2*ker
            def integrand(t):
                S=sum(coef*mp.exp(-c*(a-t)-(a-t)**2/4)/(2*mp.sqrt(mp.pi))
                      for a,coef in terms)
                return abs(S)**2*mp.exp(-t)
            direct=mp.quad(integrand,[-mp.inf,-10,0,L/2,L])
            rel=abs(direct-pair)/max(1,abs(direct))
            if rel>mp.mpf('1e-45'):
                raise RuntimeError('quadrature/kernel disagreement')
            cases.append({'m':m,'row':list(row),'D':D,'occupied_patterns':27,
                          'energy':mp.nstr(direct,40),'diagonal':mp.nstr(diagonal,40),
                          'off_diagonal':mp.nstr(mp.re(pair)-diagonal,40),
                          'relative_discrepancy_below':'1e-45'})
    return {'precision_decimal_digits':60,'cases':cases,
            'scope':'Uncertified high-precision quadrature of finite three-prime Eisenstein polynomials, NOT the full infinite Gaussian source, a full native census, or evidence for an asymptotic bound.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--numerical-helper',type=Path)
    args=p.parse_args()
    result=numerical(args.numerical_helper) if args.numerical_helper else exact()
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()

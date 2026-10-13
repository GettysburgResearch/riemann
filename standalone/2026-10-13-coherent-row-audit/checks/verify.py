#!/usr/bin/env python3
"""Exact finite reconstruction and negative controls, not analytic certification.

Uses a direct scalar assembly as a second implementation; its primitive
Eisenstein arithmetic is shared with the producer and is explicitly disclosed.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
import itertools
import json
from pathlib import Path
import numpy as np
import census as C
import eisenstein_source as E

COUNTS = defaultdict(int)


def check(condition, group):
    COUNTS[group] += 1
    if not condition:
        raise RuntimeError(f"{group}: predicate {COUNTS[group]} failed")


def reject(operation, name):
    try:
        operation()
    except (RuntimeError, ValueError):
        COUNTS['negative_controls'] += 1
        return name
    raise RuntimeError(f"invalid substitution not rejected: {name}")


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for l, y in enumerate(b):
            out[j+l] += x*y
    return out


def convolve_power(a, k):
    out = [1]
    for _ in range(k):
        out = convolution(out, a)
    return out


def direct_columns(cap):
    primes = C.make_primes(cap)
    result = []
    for z in {E.canonical(z) for z in E.elements(cap)}:
        n = E.en(z)
        if n % 2 == 0 or n % 3 == 0 or 2*n <= cap:
            continue
        fs = tuple(j for j, p in enumerate(primes) if E.divides(p, z))
        if any(E.divides(E.emul(primes[j], primes[j]), z) for j in fs):
            continue
        product = 1
        for j in fs:
            product *= E.en(primes[j])
        check(product == n, 'ideal_factorization_coverage')
        result.append((n, fs))
    return sorted(result)


def scalar_char(primes, factors, u):
    value = E.ONE
    for j in factors:
        exp = E.prime_character(primes[j], u)
        if exp is None:
            return E.ZERO
        value = E.mul(value, E.ROOTS[exp])
    return value


def scalar_case(D, H, k):
    primes = C.make_primes(D)
    columns = direct_columns(D)
    rows = E.elements(H)
    sixth = {C.epower(b, 6) for b in E.elements(C.integer_root(H, 6))}
    m = k*max(len(fs) for _, fs in columns) + 1
    grams = {g: [[E.ZERO for _ in range(m)] for _ in range(m)]
             for g in ('all', 'sixth_powers', 'not_sixth_powers')}
    native = Counter()
    # Different scalar assembly, with no NumPy or degree-polynomial multiplication.
    for u in rows:
        values = [scalar_char(primes, fs, u) for _, fs in columns]
        A = E.ZERO
        for (_, fs), val in zip(columns, values):
            A = E.add(A, E.scale(val, (-1)**len(fs)))
        B = [E.ZERO for _ in range(m)]
        for indices in itertools.product(range(len(columns)), repeat=k):
            value, degree = E.ONE, 0
            for i in indices:
                value = E.mul(value, values[i])
                degree += len(columns[i][1])
            B[degree] = E.add(B[degree], value)
        group = 'sixth_powers' if u in sixth else 'not_sixth_powers'
        for g in ('all', group):
            native[g] += E.norm(A)**k
            for j in range(m):
                for l in range(m):
                    grams[g][j][l] = E.add(grams[g][j][l], E.mul(B[j], E.conj(B[l])))
    return grams, native


def direct_principal(D, H):
    primes = C.make_primes(D)
    columns = direct_columns(D)
    products = Counter(tuple(sorted(f+g)) for _, f in columns for _, g in columns)
    total = 0
    for u in E.elements(H):
        for fs, mult in products.items():
            if all(not E.divides(primes[j], u) for j in set(fs)):
                total += mult*mult
    return total


def main():
    for n in range(0, 1001):
        for d in range(1, 9):
            r = C.integer_root(n, d)
            check(r**d <= n < (r+1)**d, 'exact_roots')
    for D in range(2, 301):
        H = C.ceil_height(D)
        check((H-1)**20 < D**21 <= H**20, 'exact_height')
    rows = np.array(E.elements(13), dtype=np.int64)
    for p in C.make_primes(256):
        values = C.char_vec(p, rows)
        for u, value in zip(rows, values):
            reference = E.prime_character(p, tuple(map(int, u)))
            check(int(value) == (-1 if reference is None else reference), 'literal_character_comparison')
    for cap in (64, 128, 256):
        check(C.make_columns(C.make_primes(cap), cap) == direct_columns(cap), 'all_column_coverage')
    for D,H,k in ((64,13,1),(64,13,2),(64,13,3),(64,13,4),(128,13,2)):
        result = C.run_case(D,H,k,with_reference=(k==2))
        grams, native = scalar_case(D,H,k)
        V = convolve_power(result['degree_counts'], k)
        for name in grams:
            a = result['groups'][name]
            check(a['native_moment'] == native[name], 'scalar_direct_moment')
            for j in range(len(V)):
                for l in range(len(V)):
                    check(grams[name][j][l] == (a['gram'][j][l],0), 'scalar_direct_gram')
                    if name == 'sixth_powers':
                        check(a['gram'][j][l] == a['rows']*V[j]*V[l], 'exact_rank_one')
        if k == 2:
            check(result['principal_reference']['physical'] == direct_principal(D,H), 'direct_masked_principal')
    for k in range(1,7):
        for c in ((1,2,3),(0,3,4,2),(5,1),(1,1,1,1)):
            V = convolve_power(c,k)
            U = sum(c)
            check(sum(V) == U**k, 'positive_profile')
            check(len(V)*sum(x*x for x in V) >= U**(2*k), 'cauchy_profile')
            for j in range(len(c)):
                if c[j] == 0:
                    continue
                b = list(c)
                b[j] -= 1
                Vp = convolve_power(b,k)
                delta = sum(x-y for x,y in zip(c,b))
                diff = [x-y for x,y in zip(V,Vp)]
                check(min(diff)>=0, 'mask_positive_coefficients')
                check(sum(diff)<=k*U**(k-1)*delta, 'mask_convolution_bound')
                # Trace and Frobenius controls imply the stated operator control.
                l1diff = sum(diff)
                trace_diff = abs(sum(x*x-y*y for x,y in zip(V,Vp)))
                check(trace_diff <= 2*U**k*l1diff+l1diff*l1diff, 'mask_trace_bound')
                squares = sum((x*y-a*b)**2 for x,a in zip(V,Vp) for y,b in zip(V,Vp))
                check(squares <= (2*U**k*l1diff+l1diff*l1diff)**2, 'mask_frobenius_bound')
    path = Path(__file__).resolve().parents[1] / 'results.json'
    report = json.loads(path.read_text())
    check(len(report['cases']) == 9, 'saved_coverage')
    for r in report['cases']:
        g = r['groups']
        for a,b in (('sixth_powers','not_sixth_powers'),
                    ('unit_times_sixth_powers','not_unit_times_sixth_powers')):
            for key in ('rows','native_moment','degree_energy','cross_degree'):
                check(g[a][key]+g[b][key] == g['all'][key], 'saved_row_partition')
            for j in range(len(g['all']['gram'])):
                for l in range(len(g['all']['gram'])):
                    check(g[a]['gram'][j][l]+g[b]['gram'][j][l] == g['all']['gram'][j][l], 'saved_gram_partition')
        V=convolve_power(r['degree_counts'],r['k'])
        R=g['sixth_powers']['rows']
        for j in range(len(V)):
            for l in range(len(V)):
                check(g['sixth_powers']['gram'][j][l] == R*V[j]*V[l], 'saved_rank_one')
        for a in ('all','sixth_powers','not_sixth_powers'):
            check(g[a]['native_moment']-g[a]['principal_reference'] ==
                  g[a]['native_nonprincipal_remainder'], 'saved_reference_difference')
    large=next(r for r in report['cases'] if (r['D'],r['H'])==(8192,12855))
    g=large['groups']
    for key, val in [('rows',46608),('columns',1145),('degree_counts',[0,459,562,124])]:
        check(large[key] == val, 'published_full_case_control')
    for group, values in {
        'all':(114923460372,1652703692676,-1537780232304,114879621108,43839264),
        'sixth_powers':(583443,1544518075635,-1544517492192,8416731,-7833288),
        'not_sixth_powers':(114922876929,108185617041,6737259888,114871204377,51672552)
    }.items():
        for key,val in zip(('native_moment','degree_energy','cross_degree',
                            'principal_reference','native_nonprincipal_remainder'),values):
            check(g[group][key] == val, 'published_exact_values')
    check(large['sixth_power_rows'] == [[-27,0],[1,0],[64,0]], 'actual_sixth_power_rows')
    sharp=next(r for r in report['cases'] if (r['D'],r['H'])==(8192,8192))
    check(sharp['groups']['not_sixth_powers']['native_nonprincipal_remainder']==-1184937090,
          'opposite_remainder_sign')
    aliases=sum(E.norm(E.add(E.ONE,z))**6 for z in E.ROOTS)
    check(Fraction(aliases,6)==926, 'sixth_power_alias')
    negative=[]
    negative.append(reject(lambda:C.require(Fraction(aliases,6)==924,'missing sixth aliases'),
                           'equal powers are not all sixth-charge aliases'))
    six={C.epower(b,6) for b in E.elements(1)}
    negative.append(reject(lambda:C.require((-1,0) in six,'unit is not sixth power'),
                           'norm perfect sixth power does not classify element rows'))
    p=C.make_primes(13)[0]
    negative.append(reject(lambda:C.require(E.prime_character(p,C.epower(p,6))==0,'masked nonunit'),
                           'sixth-power row does not erase a good-prime zero'))
    negative.append(reject(lambda:C.require(g['not_sixth_powers']['cross_degree']<=0,'sign'),
                           'complement cross-degree need not be negative'))
    negative.append(reject(lambda:C.require(g['sixth_powers']['degree_energy']==g['sixth_powers']['principal_reference'],'different references'),
                           'principal-row degree Gram is not principal-tuple reference'))
    negative.append(reject(lambda:C.require(g['all']['native_moment']+1==114923460372,'mutation'),
                           'one-unit corrupted census total'))
    negative.append(reject(lambda:C.run_case(64,13,16,False),'explicit int64 overflow guard'))
    text=json.dumps({'status':'PASS','predicates':sum(COUNTS.values()),
                     'counts':dict(sorted(COUNTS.items())), 'negative_controls':negative,
                     'scope':'exact finite algebra and small independent assemblies; shared primitive helper; not an asymptotic proof'},
                    indent=2,sort_keys=True)+'\n'
    print(text,end='')


if __name__=='__main__':
    main()

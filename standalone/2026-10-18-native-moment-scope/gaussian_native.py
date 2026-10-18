"""Directed full-row Gaussian experiment for the explicit Kummer family.

The row cap is on u itself, unlike gaussian.py's principal-sector b cap.
All characters and norm coefficients are reconstructed from primitive data.
"""
import argparse
import json
from pathlib import Path
import sys

from flint import arb, ctx
import gaussian as G
import ideals as I
import kummer as K


def produce(max_power=10, H=64, ratio=4096, precision=256, progress=False):
    I.require(0 <= max_power <= 10 and 7 <= H <= 64 and 16 <= ratio <= 8192,
              'Declared finite native coverage limits exceeded.')
    I.require(precision >= 192, 'Directed native replay requires at least 192 bits.')
    ctx.prec = precision
    cap = ratio*2**max_power
    rows = tuple(u for u in I.ideals_up_to(H) if I.exterior(u))
    principal = I.norm_mobius_coefficients(cap, compact=True)
    spf = K.smallest_prime_factors(cap)
    coefficients, coverage = {}, []
    for u in rows:
        if progress:
            print('Primitive native row '+str(u), file=sys.stderr, flush=True)
        a, b = K.norm_coefficients(u, cap, principal, spf)
        I.require(a.itemsize == b.itemsize == 4, 'Portable signed int32 source required.')
        coefficients[u] = a, b
        coverage.append({'ideal_HNF': list(u), 'norm': I.norm(u),
                         'primary_generator': list(K.primary_generator(u)),
                         'basis_A_int32_le_sha256': G.coefficient_digest(a),
                         'basis_B_int32_le_sha256': G.coefficient_digest(b)})
    del spf
    values = []
    sqrt3_over2 = arb(3).sqrt()/2
    for j in range(max_power+1):
        D, Y = 2**j, ratio*2**j
        if progress:
            print('Complete native Gaussian D='+str(D), file=sys.stderr, flush=True)
        sums_a, sums_b = {u: arb(0) for u in rows}, {u: arb(0) for u in rows}
        for n in range(1, Y+1):
            if not principal[n]:
                continue
            w = G.weight(n, D)
            for u in rows:
                a, b = coefficients[u]
                if a[n]:
                    sums_a[u] += a[n]*w
                if b[n]:
                    sums_b[u] += b[n]*w
        tail = G.tail_bound(Y, D)
        error = arb(0, tail.abs_upper())
        entries, squares = [], []
        for u in rows:
            real = sums_a[u]-sums_b[u]/2+error
            imag = sqrt3_over2*sums_b[u]+error
            squared = G.square_ball(real)+G.square_ball(imag)
            squares.append(squared)
            entries.append({'ideal_HNF': list(u), 'real': G.render(real),
                            'imag': G.render(imag), 'absolute_squared': G.render(squared)})
        moments = {str(2*k): G.render(sum((G.integer_power(v, k).nonnegative_part()
                                         for v in squares), arb(0)).nonnegative_part())
                   for k in (1, 2, 4, 8, 16)}
        values.append({'D': D, 'complete_norm_cutoff': Y,
                       'complete_complex_tail_modulus_bound': G.render(tail),
                       'all_native_rows': entries, 'full_native_moments': moments})
    return {'status': 'DIRECTED FINITE FULL-ROW EXPERIMENT; no asymptotic or RH conclusion',
            'field': 'Q(w), w^2+w+1=0', 'S': 'prime ideals above 2 and 3',
            'family': 'chi_u(n)=(alpha_u/n)_6; unique alpha_u=1 mod (3)',
            'normalization': {'c': 0, 'tau': 1},
            'parameters': {'max_power': max_power, 'all_u_norm_cap': H,
                           'cutoff_ratio': ratio, 'precision_bits': precision},
            'complete_source_coverage': {'all_norms_through': cap, 'rows': coverage},
            'arithmetic': {'python_flint': G.flint.__version__, 'FLINT': G.flint.__FLINT_VERSION__},
            'values': values}


def replay(path, progress=False):
    recorded = json.loads(path.read_text(encoding='utf-8'))
    p = recorded['parameters']
    expected = tuple(u for u in I.ideals_up_to(p['all_u_norm_cap']) if I.exterior(u))
    actual = tuple(tuple(row['ideal_HNF']) for row in recorded['complete_source_coverage']['rows'])
    I.require(actual == expected, 'Complete native ideal row coverage changed.')
    original = produce(p['max_power'], p['all_u_norm_cap'], p['cutoff_ratio'],
                       p['precision_bits'], progress)
    I.require(recorded == original, 'Primitive native source replay differs.')
    longer = produce(p['max_power'], p['all_u_norm_cap'], 2*p['cutoff_ratio'],
                     p['precision_bits']+128, progress)
    comparisons = 0
    for old, new in zip(recorded['values'], longer['values'], strict=True):
        for a, b in zip(old['all_native_rows'], new['all_native_rows'], strict=True):
            I.require(a['ideal_HNF'] == b['ideal_HNF'], 'Native row order changed.')
            for key in ('real', 'imag', 'absolute_squared'):
                I.require(arb(a[key]).contains(arb(b[key])), 'Longer native Gaussian is not contained.')
                comparisons += 1
        for order, ball in old['full_native_moments'].items():
            I.require(arb(ball).contains(arb(new['full_native_moments'][order])),
                      'Longer native moment is not contained.')
            comparisons += 1
    # Independently aggregate actual ideal columns on the first two scales.
    cap = min(512, p['cutoff_ratio']//2)
    columns = [n for n in I.ideals_up_to(cap) if I.exterior(n)]
    direct_checks = 0
    for entry in recorded['values'][:2]:
        D = entry['D']
        error = arb(0, G.tail_bound(cap, D).abs_upper())
        for row in entry['all_native_rows']:
            u = tuple(row['ideal_HNF'])
            a_sum, b_sum = arb(0), arb(0)
            for n in columns:
                a, b = K.scale(I.mobius(n), K.symbol(K.primary_generator(u), n))
                w = G.weight(I.norm(n), D)
                a_sum += a*w
                b_sum += b*w
            real = a_sum-b_sum/2+error
            imag = arb(3).sqrt()*b_sum/2+error
            I.require(real.contains(arb(row['real'])) and imag.contains(arb(row['imag'])),
                      'Individual-ideal native Gaussian source disagrees.')
            direct_checks += 1
    return {'status': 'PASS: full native primitive and directed replay',
            'complete_native_rows': len(expected), 'scales': len(recorded['values']),
            'longer_enclosure_comparisons': comparisons,
            'direct_individual_ideal_comparisons': direct_checks,
            'old_precision_bits': p['precision_bits'], 'new_precision_bits': p['precision_bits']+128,
            'old_cutoff_ratio': p['cutoff_ratio'], 'new_cutoff_ratio': 2*p['cutoff_ratio'],
            'boundary': 'The explicitly defined finite Kummer family only; no infinite moment estimate.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-power', type=int, default=10)
    parser.add_argument('--replay', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    result = replay(args.replay, args.progress) if args.replay else produce(args.max_power, progress=args.progress)
    text = G.serial(result)
    if args.output:
        args.output.write_text(text, encoding='utf-8', newline='\n')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()

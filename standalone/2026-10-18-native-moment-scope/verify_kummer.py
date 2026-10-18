"""Complete small-ideal fixtures for the explicit sextic Kummer family."""
import argparse
from collections import Counter
import json
from pathlib import Path

import ideals as I
import kummer as K


def verify(H=64, N=256):
    rows = [u for u in I.ideals_up_to(H) if I.exterior(u)]
    columns = [n for n in I.ideals_up_to(N) if I.exterior(n)]
    counts = Counter()

    def check(ok, group):
        counts[group] += 1
        I.require(ok, group+' failed.')

    for p in range(5, N+1):
        if I.integer_factors(p) == ((p, 1),):
            check(K.fast_primes_over(p) == I.primes_over(p), 'independent-prime-ideal-roots')
    for u in rows:
        alpha = K.primary_generator(u)
        check(K.absolute_squared(alpha) == I.norm(u) and I.member(u, alpha), 'literal-primary-generator')
        for v in rows:
            uv = I.multiply(u, v)
            check(K.primary_generator(uv) == I.element_product(alpha, K.primary_generator(v)),
                  'multiplicative-primary-generator')
        actual = [(0, 0) for _ in range(N+1)]
        prefix = K.ZERO
        for n in columns:
            value = K.symbol(alpha, n)
            check(value == K.ZERO or value in K.ROOTS, 'exact-sixth-root-or-nonunit')
            check((value == K.ZERO) == (not I.coprime(u, n)), 'literal-native-character-zero')
            actual[I.norm(n)] = K.add(actual[I.norm(n)], K.scale(I.mobius(n), value))
        x, y = K.norm_coefficients(u, N)
        check(actual == list(zip(x, y)), 'complete-native-norm-source')

    # Direct finite-field repeated multiplication, independent of binary
    # powering, authenticates the local sixth-power symbol on every residue.
    prime_ideals = {p for n in columns for p, _ in I.factor(n)}
    for p in sorted(prime_ideals):
        q = I.norm(p)
        distribution = Counter()
        for y in range(p[2]):
            for x in range(p[0]):
                value, current = K.symbol_at_prime((x, y), p), K.ONE
                for _ in range((q-1)//6):
                    current = K.residue(p, I.element_product(current, (x, y)))
                check(K.residue(p, value) == current, 'independent-local-repeated-multiplication')
                distribution[value] += 1
        check(distribution[K.ZERO] == 1 and all(distribution[r] == (q-1)//6 for r in K.ROOTS),
              'complete-residue-field-character-distribution')

    # All same-source sixth-power copies, including common primes.
    for b in rows:
        alpha = K.primary_generator(I.power(b, 6))
        for n in columns:
            check(K.symbol(alpha, n) == (K.ONE if I.coprime(b, n) else K.ZERO),
                  'complete-principal-sixth-power-copy')

    caps = (7, 13, 25, 64, 128, 256)
    moments = []
    for D in caps:
        if D > N:
            continue
        values = []
        for u in rows:
            alpha = K.primary_generator(u)
            v = K.ZERO
            for n in columns:
                if I.norm(n) <= D:
                    v = K.add(v, K.scale(I.mobius(n), K.symbol(alpha, n)))
            values.append(K.absolute_squared(v))
        moments.append({'D': D, 'orders': {str(2*k): str(sum(v**k for v in values))
                                          for k in (1, 2, 4, 8)}})
    return {'status': 'PASS: complete finite ideal and residue-field algebra; no analytic conclusion',
            'field': 'Q(w), w^2+w+1=0',
            'family': 'chi_u(n)=(alpha_u/n)_6; alpha_u=1 mod (3)',
            'S': 'all prime ideals above 2 and 3',
            'complete_coverage': {'row_ideal_norm_cap': H, 'rows': len(rows),
                                  'column_ideal_norm_cap': N, 'columns': len(columns),
                                  'prime_ideal_residue_fields': len(prime_ideals)},
            'predicates_by_group': dict(sorted(counts.items())),
            'compact_native_moment_fixtures': moments,
            'scope': 'W=1_(0,1] only. Every declared ideal and residue occurs. No Gaussian, theta value, zero census, infinite bound or GRH verdict.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(verify(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8', newline='\n')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()

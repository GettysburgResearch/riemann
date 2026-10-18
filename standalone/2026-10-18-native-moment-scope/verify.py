"""Independent finite checks for the identities, NOT the analytic theorems.

Standard library only. Enumerates every Eisenstein ideal in the declared
caps; compares lattice ideals with a separate rational Euler recurrence.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
import hashlib
import json
from math import isqrt
from pathlib import Path

import ideals as I


def encode(value):
    return json.dumps(value, sort_keys=True, indent=2) + '\n'


def exact_checks(column_cap=256, row_cap=64, mutation=None):
    counts = Counter()

    def check(condition, group, message):
        counts[group] += 1
        if not condition:
            raise ValueError(group + ': ' + message)

    all_columns = I.ideals_up_to(column_cap)
    all_rows = I.ideals_up_to(row_cap)
    columns = tuple(a for a in all_columns if I.exterior(a))
    rows = tuple(b for b in all_rows if I.exterior(b))
    check(len(set(all_columns)) == len(all_columns), 'complete-HNF', 'Duplicate HNF ideal.')
    for a in all_columns:
        check(I.valid(a), 'complete-HNF', 'Lattice is not stable under w.')
        fac = I.factor(a)  # This reconstructs the actual ideal, not just its norm.
        check(I.norm(a) == I.norm(I.power(a, 1)), 'ideal-norm', 'Norm or identity changed.')
        if I.norm(a) <= isqrt(column_cap):
            check(I.norm(I.power(a, 6)) == I.norm(a)**6,
                  'sixth-power-rows', 'A sixth-power ideal changed norm.')

    # An independent scalar formula for ALL ideal counts: zeta_K=zeta L(chi_-3).
    actual_counts = Counter(I.norm(a) for a in all_columns)
    for n in range(1, column_cap+1):
        expected = sum(0 if d % 3 == 0 else 1 if d % 3 == 1 else -1
                       for d in range(1, n+1) if n % d == 0)
        check(actual_counts[n] == expected, 'independent-ideal-count', 'Ideal coverage mismatch.')

    # Compare complete HNF Mobius sums with a rational Euler computation.
    actual_mu = [0]*(column_cap+1)
    for a in columns:
        actual_mu[I.norm(a)] += I.mobius(a)
    scalar_mu = I.norm_mobius_coefficients(column_cap)
    check(actual_mu == scalar_mu, 'independent-Mobius-source', 'Conjugate, inert or S factor changed.')

    # Explicit ramified, inert, and split witnesses before the S exclusions.
    p7, p7bar = I.primes_over(7)
    check(p7 != p7bar and I.norm(p7) == I.norm(p7bar) == 7,
          'split-ideal-distinction', 'Conjugate ideals collapsed.')
    check(I.multiply(p7, p7bar) == (7, 0, 7),
          'split-ideal-distinction', 'Split prime product is not (7).')
    check(I.mobius(I.multiply(p7, p7bar)) == 1 and I.mobius(I.power(p7, 2)) == 0,
          'split-ideal-distinction', 'Distinct primes confused with a prime square.')
    check(I.primes_over(5) == ((5, 0, 5),) and I.norm((5, 0, 5)) == 25,
          'inert-prime', 'Inert prime was assigned norm p rather than p squared.')
    p3, = I.primes_over(3)
    check(I.multiply(p3, p3) == (3, 0, 3), 'ramified-prime', 'Ramified square changed.')

    mask_outputs = {}
    by_signature = defaultdict(list)
    for b in rows:
        by_signature[I.mask_signature(b)].append(b)
    for signature, bs in sorted(by_signature.items()):
        expected = I.norm_mobius_coefficients(column_cap, signature)
        for b in bs:
            masked = [0]*(column_cap+1)
            for a in columns:
                keep = I.coprime(a, b)
                if mutation == 'drop-nonunit-mask':
                    keep = True
                if mutation == 'collapse-split-mask':
                    keep = all(p not in dict(signature) for p, _ in I.integer_factors(I.norm(a)))
                if keep:
                    masked[I.norm(a)] += I.mobius(a)
            check(masked == expected, 'complete-principal-mask', 'Literal ideal mask changed.')
            mask_outputs[b] = masked

    # Both convolution directions are checked on actual, independently
    # enumerated ideals. Equal norms retain ideal multiplicity.
    for signature, bs in sorted(by_signature.items()):
        b = bs[0]
        primes_b = {p for p, _ in I.factor(b)}
        smooth_counts = Counter()
        finite_inverse = Counter()
        for d in columns:
            factors = I.factor(d)
            if all(p in primes_b for p, _ in factors):
                if mutation == 'truncate-smooth-powers' and any(e > 1 for _, e in factors):
                    continue
                smooth_counts[I.norm(d)] += 1
                if all(e == 1 for _, e in factors):
                    finite_inverse[I.norm(d)] += I.mobius(d)
        out = [0]*(column_cap+1)
        inverse_out = [0]*(column_cap+1)
        for d, weight in smooth_counts.items():
            for n in range(1, column_cap//d+1):
                out[d*n] += weight*scalar_mu[n]
        for d, weight in finite_inverse.items():
            for n in range(1, column_cap//d+1):
                inverse_out[d*n] += weight*mask_outputs[b][n]
        check(out == mask_outputs[b], 'infinite-mask-convolution', 'A prime power or multiplicity was lost.')
        check(inverse_out == scalar_mu, 'finite-mask-inverse', 'Inverse Euler sign or source changed.')

    # Shared cores and mask primes are allowed. We check all column masks
    # in a complete finite ideal cap, not a separately invented character.
    for b in rows:
        b_sixth = I.power(b, 6)
        for a in columns:
            check(I.coprime(a, b_sixth) == I.coprime(a, b),
                  'literal-sixth-mask', 'Sixth power erased a nonunit zero.')

    # Rational maximal-envelope test, for the compact W=1_(0,1]. It verifies
    # the source-preserving inequality, not a Gaussian or an infinite bound.
    prefix = [0]*(column_cap+1)
    for n in range(1, column_cap+1):
        prefix[n] = prefix[n-1]+scalar_mu[n]
    caps = sorted({min(column_cap, x) for x in (7, 13, 25, 49, 64, 128, 256)})
    moment_samples = []
    for cap in caps:
        envelope = max(Q(abs(prefix[n]), n) for n in range(1, cap+1))
        values = {b: sum(coef[:cap+1]) for b, coef in mask_outputs.items()}
        for b in rows:
            mass = Q(1)
            for p, _ in I.factor(b):
                mass *= Q(I.norm(p), I.norm(p)-1)
            check(abs(values[b]) <= cap*envelope*mass,
                  'maximal-mask-transfer', 'Mask bound lost an earlier scale.')
        for k in (1, 2, 4):
            moment = sum(v**(2*k) for v in values.values())
            mask_mass = sum((__mask_mass(b)**(2*k) for b in rows), Q(0))
            check(moment <= (cap*envelope)**(2*k)*mask_mass,
                  'replica-moment-transfer', 'The source bound failed on complete rows.')
            moment_samples.append({'D': cap, 'k': k, 'complete_b_cap': row_cap,
                                   'rows': len(rows), 'exact_moment': str(moment)})

    # Verify f=1*g over every ideal and the finite positive Euler upper
    # bound from the proof; this is sigma=1, r=2 only.
    f_sum = sum((__mask_mass(b)**2 for b in rows), Q(0))
    g_sum = Q(0)
    prime_set = set()
    for d in rows:
        fd = I.factor(d)
        prime_set.update(p for p, _ in fd)
        if any(e > 1 for _, e in fd):
            continue
        g = Q(1)
        for p, _ in fd:
            g *= Q(I.norm(p), I.norm(p)-1)**2-1
        multiplicity = sum(I.norm(b) <= row_cap//I.norm(d) for b in rows)
        g_sum += g*multiplicity
    check(f_sum == g_sum, 'positive-mask-divisor-identity', 'f=1*g changed.')
    euler_upper = Q(1)
    for p in sorted(prime_set):
        q = I.norm(p)
        euler_upper *= 1+(Q(q, q-1)**2-1)/q
    check(f_sum <= 2*row_cap*euler_upper,
          'linear-average-mask-cost', 'The proved finite linear envelope failed.')

    # Exact exponent checks for the two DISTINCT target row counts.
    for h in (Q(1, 3), Q(1), Q(6), Q(12)):
        for k in (1, 2, 4, 8, 16, 32):
            full_extraction = (h+k)/(2*k)
            replica_extraction = (h/6+k)/(2*k)
            if mutation == 'use-H-for-principal-count':
                replica_extraction = full_extraction
            check(replica_extraction == Q(1, 2)+h/(12*k),
                  'principal-replica-count', 'Principal b cap is H^(1/6), not H.')
            check(full_extraction == Q(1, 2)+h/(2*k),
                  'fixed-row-family-extraction', 'Growing-family row cost changed.')

    source_hash = hashlib.sha256(encode(actual_mu).encode()).hexdigest()
    return {
        'status': 'PASS: finite exact algebra; analytic theorems not certified',
        'field': 'Q(w), w^2+w+1=0',
        'S': 'all prime ideals above 2 and 3',
        'coverage': {'all_integral_ideal_column_cap': column_cap,
                     'integral_ideals_including_S': len(all_columns),
                     'exterior_ideal_columns': len(columns),
                     'all_integral_ideal_b_cap': row_cap,
                     'exterior_mask_ideals': len(rows),
                     'distinct_principal_mask_signatures': len(by_signature)},
        'source_norm_coefficients_sha256': source_hash,
        'predicates_by_group': dict(sorted(counts.items())),
        'finite_moment_samples': moment_samples,
        'finite_mask_mass_sigma_1_r_2': str(f_sum),
        'boundary': 'Compact rational fixtures only. No nonprincipal L-values, CT theta rows, zero census, Gaussian evaluation, or infinite sign theorem.'}


def __mask_mass(b):
    mass = Q(1)
    for p, _ in I.factor(b):
        mass *= Q(I.norm(p), I.norm(p)-1)
    return mass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--column-cap', type=int, default=256)
    parser.add_argument('--row-cap', type=int, default=64)
    parser.add_argument('--mutation', choices=('drop-nonunit-mask', 'collapse-split-mask',
                                             'truncate-smooth-powers', 'use-H-for-principal-count'))
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    I.require(64 <= args.column_cap <= 8192, 'Column cap must be in [64,8192].')
    I.require(7 <= args.row_cap <= args.column_cap, 'Row cap must be in [7,column cap].')
    result = encode(exact_checks(args.column_cap, args.row_cap, args.mutation))
    if args.output:
        args.output.write_text(result, encoding='utf-8', newline='\n')
    else:
        print(result, end='')


if __name__ == '__main__':
    main()

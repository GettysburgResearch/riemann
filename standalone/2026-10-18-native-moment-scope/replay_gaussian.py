"""Reconstruct the primitive source and validate the deposited Gaussian balls.

Uses a longer cutoff and higher precision, plus an individual HNF sum on
the two smallest scales. This is a different replay, not an independent
analytic referee or a second interval-arithmetic implementation.
"""
import argparse
import json
from pathlib import Path
import sys

from flint import arb, ctx
import ideals as I
from gaussian import produce, principal_masks, render, serial, tail_bound, weight


def replay(path, progress=False):
    recorded = json.loads(path.read_text(encoding='utf-8'))
    p = recorded['parameters']
    I.require(recorded['normalization'] == {
        'c': 4, 'tau': 1, 'weight': 'y^-4 exp[-log(y)^2/4]/sqrt(4 pi)'},
        'Wrong fixed Gaussian normalization.')
    # Authenticate the literal B cap independently of the producer's
    # grouping function. A self-consistent omission of a repeated or
    # conjugate masking ideal must not pass by repeating that omission.
    expected_b = {b for b in I.ideals_up_to(p['all_b_norm_cap']) if I.exterior(b)}
    seen_b = []
    seen_signatures = set()
    for group in recorded['coefficient_coverage']['mask_signatures']:
        signature = tuple(tuple(x) for x in group['signature'])
        I.require(signature not in seen_signatures, 'Repeated principal mask signature.')
        seen_signatures.add(signature)
        group_b = [tuple(x) for x in group['ideals']]
        I.require(group['multiplicity'] == len(group_b), 'Incorrect principal mask multiplicity.')
        for b in group_b:
            I.require(b in expected_b and I.mask_signature(b) == signature,
                      'A recorded ideal is not in its literal principal mask class.')
        seen_b.extend(group_b)
    I.require(len(seen_b) == len(set(seen_b)) and set(seen_b) == expected_b,
              'Complete principal ideal B-cap coverage changed.')
    # First regenerate the exact original integer source hashes and its
    # entire declared result. No deposited coefficient array is trusted.
    original = produce(p['max_power'], p['all_b_norm_cap'], p['cutoff_ratio'],
                       p['precision_bits'], progress)
    I.require(original == recorded, 'Original primitive replay did not reproduce the report.')
    longer = produce(p['max_power'], p['all_b_norm_cap'], 2*p['cutoff_ratio'],
                     p['precision_bits']+128, progress)
    comparisons = 0
    for old, new in zip(recorded['values'], longer['values'], strict=True):
        I.require(old['D'] == new['D'], 'Scale grid changed.')
        for a, b in zip(old['rows'], new['rows'], strict=True):
            I.require(a['signature'] == b['signature'] and a['multiplicity'] == b['multiplicity'],
                      'Principal row coverage or multiplicity changed.')
            I.require(arb(a['enclosure']).contains(arb(b['enclosure'])),
                      'Deposited enclosure failed longer/higher-precision containment.')
            comparisons += 1
        for order, enclosure in old['complete_principal_replica_moments'].items():
            I.require(arb(enclosure).contains(arb(new['complete_principal_replica_moments'][order])),
                      'Deposited moment failed longer/higher-precision containment.')
            comparisons += 1

    # Direct ideal-by-ideal computation uses no rational norm coefficients.
    # Its complete tail is deliberately broader than the long production
    # tail, and must contain the already authenticated narrow enclosure.
    direct_cap = min(512, p['cutoff_ratio']//2)
    columns = [a for a in I.ideals_up_to(direct_cap) if I.exterior(a)]
    masks = principal_masks(p['all_b_norm_cap'])
    direct_comparisons = 0
    for entry in recorded['values'][:2]:
        D = entry['D']
        tail = tail_bound(direct_cap, D)
        for row in entry['rows']:
            signature = tuple(tuple(x) for x in row['signature'])
            b = masks[signature][0]
            direct = sum((I.mobius(a)*weight(I.norm(a), D)
                          for a in columns if I.coprime(a, b)), arb(0))
            direct += arb(0, tail.abs_upper())
            I.require(direct.contains(arb(row['enclosure'])),
                      'Individual-ideal primitive Gaussian sum disagreed.')
            direct_comparisons += 1
    return {'status': 'PASS: primitive source reproduced and longer directed replay contained',
            'original_grid_scales': len(recorded['values']),
            'original_precision_bits': p['precision_bits'],
            'replay_precision_bits': p['precision_bits']+128,
            'original_cutoff_ratio': p['cutoff_ratio'],
            'replay_cutoff_ratio': 2*p['cutoff_ratio'],
            'direct_individual_ideal_cap': direct_cap,
            'direct_individual_ideal_comparisons': direct_comparisons,
            'authenticated_complete_principal_ideals': len(expected_b),
            'longer_replay_enclosure_comparisons': comparisons,
            'boundary': 'Finite principal Gaussian values and moments only; no infinite bound or independent mathematical review.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=Path(__file__).with_name('GAUSSIAN.json'))
    parser.add_argument('--output', type=Path)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    result = serial(replay(args.certificate, args.progress))
    if args.output:
        args.output.write_text(result, encoding='utf-8', newline='\n')
    else:
        print(result, end='')


if __name__ == '__main__':
    main()

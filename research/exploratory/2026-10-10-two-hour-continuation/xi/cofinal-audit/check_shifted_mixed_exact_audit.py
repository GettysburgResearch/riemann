#!/usr/bin/env python3
"""Independent exact derived audit; imports native intervals, never replays signs."""
from __future__ import annotations
import argparse
import ast
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
XI = HERE.parent
EXPLORATORY = XI.parent.parent
OLD = EXPLORATORY / '2026-10-10-four-hour-wave'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit('FAIL: ' + message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cmul(a: tuple[Q, Q], b: tuple[Q, Q]) -> tuple[Q, Q]:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def corner(height: int, k: int) -> Q:
    # Re((H+i/2)^(-2k)), using Gaussian-rational repeated multiplication.
    h, a = Q(height), Q(1, 2)
    d = h*h+a*a
    inverse = (h/d, -a/d)
    value = (Q(1), Q(0))
    for _ in range(2*k):
        value = cmul(value, inverse)
    return value[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'shifted_mixed_exact_audit.json')
    args = parser.parse_args()
    source = XI/'shifted_hierarchy_v2.json'
    cone_source = XI/'mixed_cone_v2.json'
    need(sha(source) == 'd6cf40e46dbe0292aff5a48dc5ebec357f378ffed4b2e3aefbfe4d848d517ba3', 'frozen V2 native receipt')
    need(sha(cone_source) == 'd7b25f57a33807e8d46e45755b7c962df1ccf8ad92540b6561fcfef7ad62d336', 'frozen V2 cone receipt')
    native = json.loads(source.read_text())
    cone = json.loads(cone_source.read_text())
    bound = {}
    for receipt in (native, cone):
        for name, expected in receipt['source_sha256'].items():
            path = EXPLORATORY/name
            need(sha(path) == expected, 'direct source binding ' + name)
            bound[name] = expected
    prior = json.loads((OLD/'xi/outer-ray/sixteenth_moment_census.json').read_text())
    primitive = json.loads((OLD/'xi/outer-ray/native_slab_certificate.json').read_text())
    for receipt in (prior, primitive):
        for name, expected in receipt['source_sha256'].items():
            need(sha(OLD/name) == expected, 'inherited direct source binding ' + name)
            bound['2026-10-10-four-hour-wave/'+name] = expected
    tree = ast.parse((XI/'check_shifted_hierarchy_v2.py').read_text())
    need(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)), 'native gates survive optimization')
    forbidden = {'zeta_zeros', 'zeta_nzeros', 'nzeros'}
    need(not any(isinstance(node, ast.Attribute) and node.attr in forbidden for node in ast.walk(tree)), 'checker has no candidate/count calls')

    original = json.loads((OLD/'xi/outer-ray/native_candidates.json').read_text())
    refined = json.loads((XI/'continuation_prefix_candidates.json').read_text())
    need(len(original['interval_numerators']) == 8049 and len(refined['interval_numerators']) == 5756, 'all selected occurrences represented')
    old_den, new_den = Q(original['denominator']), Q(refined['denominator'])
    selected = []
    previous = Q(0)
    for index, (lo, hi) in enumerate(original['interval_numerators']):
        a, b = Q(lo)/old_den, Q(hi)/old_den
        need(previous < a < b < 8192 and hi == lo+1, 'original disjoint geometry')
        previous = b
        if index < 5756:
            nl, nh = refined['interval_numerators'][index]
            l, h = Q(nl)/new_den, Q(nh)/new_den
            need(a < l < h < b and nh == nl+1 and h < 6144, 'strict refined geometry')
            a, b = l, h
        selected.append((a, b))
    need(sum(b < 5419 for a, b in selected) == 4968 and all(b < 5419 or a > 5419 for a, b in selected), 'unique imported low-root identification')

    guards = []
    need(len(native['moments']) == 21, 'complete declared finite hierarchy')
    for record in native['moments']:
        k, t = record['order'], Q(record['shift'])
        lower, upper = map(Q, record['native_residual_interval'])
        need(lower <= upper and upper > 0 and upper-lower == Q(record['native_residual_interval_width']), 'native residual interval contract')
        if t:
            need(k in (8, 16, 24, 32) and t == 512 and record['kind'] == 'shifted', 'shifted inventory')
            q, c = Q(k, 1000), 1-Q(k, 1000)**2/2
            need(0 < q < 1 and k*k*Q(1, 4) <= q*q*(t*t-Q(1, 4)) and c > 0, 'global rational acute projection')
            def ratio(h: int) -> Q:
                return upper*(h*h+Q(1, 4)+t*t)**k/c
        else:
            need(8 <= k <= 24 and record['kind'] == 'unshifted' and (2*k+1)*Q(1, 2)/5419 < 1, 'unshifted imported-head angle')
            def ratio(h: int) -> Q:
                cost = corner(h, k)
                need(cost > 0, 'independent Gaussian corner positivity')
                return upper/cost
        h = record['largest_admitted_integer_height_in_inventory_range']
        if h is None:
            need(ratio(5419) >= 1, 'no admitted base height')
        else:
            accepted, following = ratio(h), ratio(h+1)
            need(accepted == Q(record['accepted_ratio_exact']) < 1, 'exact strict accepted guard')
            need(following == Q(record['next_integer_ratio_exact']) and (h == 8192 or following >= 1), 'exact next-integer predicate failure')
            need(all(b < h or a > h for a, b in selected), 'boundary avoids every selected interval')
            need(sum(b < h for a, b in selected) == record['complete_simple_positive_zero_count'], 'derived exact finite zero count')
            need(record['maximum_column_derivative_order'] == 2*h-3, 'complete column domain')
        guards.append({'kind':record['kind'], 'order':k, 'height':h,
                       'positive_zero_count':record.get('complete_simple_positive_zero_count'),
                       'accepted_ratio_decimal':None if h is None else float(ratio(h))})

    intervals = [tuple(map(Q, value)) for value in native['complete_shifted_moment_intervals']]
    need(len(intervals) == 32 and all(0 < a <= b for a, b in intervals), 'complete coefficient interval inventory')
    c = Q(512**2)-Q(1, 4)
    mixed = native['finite_hausdorff_mixed_moments']
    need(len(mixed) == 528 and {(r['n'], r['difference_degree']) for r in mixed} == {(n, j) for n in range(32) for j in range(32-n)}, 'complete triangular mixed-index coverage')
    least_relative_lower = Q(1)
    for record in mixed:
        n, degree = record['n'], record['difference_degree']
        low, high = Q(0), Q(0)
        for j in range(degree+1):
            a, b = intervals[n+j]
            factor = (-1)**j*comb(degree, j)*c**(n+j)
            if factor >= 0:
                low += factor*a
                high += factor*b
            else:
                low += factor*b
                high += factor*a
        native_low, native_high = map(Q, record['interval'])
        need(0 < low <= high and 0 < native_low <= native_high and record['classification'] == 'strict_positive', 'independent exact complete mixed positivity')
        need(max(low, native_low) <= min(high, native_high), 'exact and directed derived intervals overlap')
        least_relative_lower = min(least_relative_lower, low/high)
    first, second = Q(8001, 5419), Q(235929375000, 159131975059)
    need(first < Q(3, 2) and second < Q(3, 2), 'analytic full finite rectangle phase bounds')
    need(Q(cone['first_phase_extreme']) == first and Q(cone['second_phase_extreme']) == second, 'rectangle receipt fractions')
    bound[str(Path(__file__).resolve().relative_to(EXPLORATORY))] = sha(Path(__file__).resolve())
    bound[str(source.relative_to(EXPLORATORY))] = sha(source)
    bound[str(cone_source.relative_to(EXPLORATORY))] = sha(cone_source)
    result = {'status':'PASS_INDEPENDENT_EXACT_DERIVED_V2_SHIFTED_MIXED_AUDIT',
              'normalization':'Xi(z)=xi(1/2+i*z)', 'native_primitive_replay_by_this_checker':False,
              'new_hardy_signs_replayed_by_this_checker':0, 'native_coefficient_source_imported':str(source.relative_to(EXPLORATORY)),
              'all_selected_bracket_geometries_audited':8049, 'strictly_refined_geometries_audited':5756,
              'exact_guard_records_audited':guards, 'complete_native_mixed_indices_audited':528,
              'finite_mixed_minimum_relative_interval_lower':float(least_relative_lower),
              'analytic_rectangle_extreme_bounds':[str(first), str(second)],
              'cofinal_census_or_all_order_positivity_claimed':False, 'rh_proved':False,
              'source_sha256':bound}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(result['status'])


if __name__ == '__main__':
    main()

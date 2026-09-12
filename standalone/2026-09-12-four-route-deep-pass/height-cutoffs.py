"""Exact comparison of two sufficient cutoff recipes, not observed zero heights.

Reconstructs #860's full rational recurrence from authenticated vendored bytes
and retains all E0/E1/L terms in the new alternative. Does not prove analytic
statements. No Git installation or historical repository objects are needed.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

HERE = Path(__file__).resolve().parent
COMMIT = 'e1a782cffaafbc9cc228273ed94ce63ae0407632'
SOURCE = 'standalone/2026-09-10-astra-branching-high-height/check.py'
SOURCE_SHA256 = 'c50a582fcb298dd17971e4f8969bdf39b78d3edc2862321c22faf8ce7fecb97d'
FROZEN_SOURCE = HERE / 'predecessor' / 'bhh26-check.py'


def require(value, message):
    if not value:
        raise ArithmeticError(message)


def load_predecessor():
    require(FROZEN_SOURCE.is_file() and not FROZEN_SOURCE.is_symlink(),
            'frozen predecessor must be a regular nonsymlink file')
    data = FROZEN_SOURCE.read_bytes()
    require(hashlib.sha256(data).hexdigest() == SOURCE_SHA256,
            'frozen predecessor SHA256 mismatch; no source executed')
    scope = {'__file__': str(FROZEN_SOURCE), '__name__': 'frozen_bhh'}
    exec(compile(data, SOURCE, 'exec'), scope)
    return data, scope


def main():
    data, scope = load_predecessor()
    rows = []
    for old in scope['threshold_records'](8):
        n = old['depth']
        e0, e1, lower = (F(old[key]) for key in ('error_E0', 'error_E1', 'polynomial_lower_bound'))
        floor = 2**21 * 4**n
        new = scope['ceilq'](max(F(2), 2*e0/lower, 4*(e1+(n+7)*e0)/lower, F(floor)))
        original = int(old['threshold'])
        require(e0/new <= lower/2, 'complete remainder must stay below half leading term')
        require(2*(e1+(n+7)*e0)/(lower*new) <= F(1, 2), 'complete logarithmic remainder')
        require(new >= floor, 'phase floor retained')
        require(F(2**21, 10) > 2**17 and 3*F(2, 3)-F(19, 12)>0, 'rational phase slack')
        rows.append({'depth': n, 'old_threshold': str(original),
                     'alternative_threshold': str(new), 'usable_minimum': str(min(original,new)),
                     'alternative_over_old': str(F(new,original)),
                     'old_decimal_digits': len(str(original)),
                     'alternative_is_smaller': new<original,
                     'old_phase_floor': str(320*16**n), 'new_phase_floor': str(floor)})
    result={'scope': 'exact finite recurrence comparison; no zero census or optimal cutoff',
            'source_commit': COMMIT, 'source_path': SOURCE,
            'source_sha256': hashlib.sha256(data).hexdigest(), 'rows': rows}
    (HERE/'height-cutoffs.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    for row in rows:
        print('n=',row['depth'],'old_digits=',row['old_decimal_digits'],
              'alternative_smaller=',row['alternative_is_smaller'],
              'ratio=',float(F(row['alternative_over_old'])))
    print('PASS: complete rational recurrences reconstructed for depths 0..8; displayed ratios are approximate.')


if __name__ == '__main__':
    main()

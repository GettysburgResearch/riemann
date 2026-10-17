#!/usr/bin/env python3
"""Run six deliberately false models in isolated optimized Python processes."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
CASES = [
    ('diagonal-fourth-moment', 'MOMENT4 = Q(7,6)', 'MOMENT4 = Q(1)', 'unpaid fourth-moment exponent'),
    ('missing-self-selection-power', 'ELIMINATION = Q(4,3)', 'ELIMINATION = Q(1)', 'wrong self-selected Holder elimination'),
    ('old-small-cutoff', 'Q(1,200)', 'Q(1,100)', 'incorrect small-frequency threshold'),
    ('old-Mellin-shift', 'CLAIM_B = Q(41,60)', 'CLAIM_B = Q(2,3)', 'wrong principal Mellin normalization'),
    ('missing-stratum', None, None, 'missing row class'),
    ('upper-threshold-count', None, None, 'unproved exceptional-count exponent'),
]

def main():
    source = (HERE/'verify.py').read_text()
    original = json.loads((HERE/'strata.json').read_text())
    records = []
    for name, before, after, expected in CASES:
        with tempfile.TemporaryDirectory(prefix='density-negative-control-') as temp:
            root = Path(temp)
            data = json.loads(json.dumps(original))
            changed = source
            if before is not None:
                if source.count(before) != 1:
                    raise ValueError('mutation anchor must occur exactly once: '+name)
                changed = source.replace(before, after)
            elif name == 'missing-stratum':
                del data[9]
            else:
                # Improperly charge the first exceptional bin at a stronger,
                # upper-threshold count instead of its actual lower threshold.
                data[1]['nu'] = '43/60'
            (root/'verify.py').write_text(changed)
            (root/'strata.json').write_text(json.dumps(data))
            p = subprocess.run([sys.executable, '-O', 'verify.py'], cwd=root,
                               capture_output=True, text=True, timeout=30)
            error = p.stderr.strip()
            if p.returncode == 0 or expected not in error:
                raise ValueError('negative control not rejected as intended: '+name+' '+error)
            records.append({'name':name,'exit_code':p.returncode,'error':error})
    print(json.dumps({'status':'PASS','executed_optimized_processes':len(records),
                      'scope':'deliberately corrupted finite models, not analytic refutations',
                      'cases':records}, indent=2, sort_keys=True))

if __name__ == '__main__': main()

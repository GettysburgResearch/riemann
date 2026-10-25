#!/usr/bin/env python3
"""Replay this pass's exact checks in isolated optimized Python processes.

No output here certifies the imported analytic framework or an open
arithmetic estimate. This runner preserves all earlier-pass bytes.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CHECKERS = (
    'check_middle_joint.py',
    'check_coherent_identity.py',
    'check_detector_localization.py',
    'check_hlc_path_cancellation.py',
    'check_hlc_root_averaging.py',
    'check_three_edge_integer_bridge.py',
    'check_off_diagonal_transfer.py',
    'check_closed_triangle_weight.py',
    'check_common_d_triangle_extension.py',
    'check_root_count_refinement.py',
)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    missing = [name for name in CHECKERS if not (HERE/name).is_file()]
    if missing:
        raise RuntimeError('Required checker files missing: ' + ', '.join(missing))
    previous_root = HERE.parent/'third-pass'
    before = {str(p.relative_to(previous_root)): digest(p)
              for p in previous_root.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts}
    runs = []
    for name in CHECKERS:
        completed = subprocess.run(
            [sys.executable,'-I','-S','-B','-O',str(HERE/name)],
            cwd=HERE, text=True, capture_output=True, check=False,
            timeout=180)
        record = {
            'checker': name,
            'checker_sha256': digest(HERE/name),
            'arguments': ['-I','-S','-B','-O',name],
            'returncode': completed.returncode,
            'stdout': completed.stdout,
            'stderr': completed.stderr,
        }
        runs.append(record)
        if completed.returncode != 0:
            raise RuntimeError(json.dumps(record,indent=2))
        print(name + ': PASS',flush=True)
    after = {str(p.relative_to(previous_root)): digest(p)
             for p in previous_root.rglob('*') if p.is_file()
             and '__pycache__' not in p.parts}
    if before != after:
        raise RuntimeError('An earlier-pass file changed during replay')
    report = {
        'status': 'PASS',
        'python_version': sys.version.split()[0],
        'optimized_predicates_retained': True,
        'third_pass_file_hashes_unchanged': True,
        'third_pass_files_compared': len(before),
        'runs': runs,
        'scope': ('Finite algebra, exact scalar certificates and regression controls. '
                  'No analytic import, residual estimate, RH proof or new '
                  'zero-free region is certified by these executions.'),
    }
    (HERE/'CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
    print('CHECKS.json written; earlier-pass bytes preserved.')


if __name__ == '__main__':
    main()

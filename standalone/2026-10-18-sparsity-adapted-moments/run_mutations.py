"""Execute each deliberately altered checker in a separate optimized process."""
import json
from pathlib import Path
import subprocess
import sys

EXPECTED = {
    'wrong_crossing': 'selected_envelope',
    'min_to_max': 'selected_envelope',
    'dual_sign': 'actual_dual_conductor',
    'erased_mask': 'literal_power_mask',
    'false_coprimality': 'literal_power_mask',
    'full_row_mollifier': 'complete_detector_budget',
    'wrong_holder': 'selected_holder_power',
    'duplicated_interval': 'prefix_disjointness',
}

def main():
    here = Path(__file__).resolve().parent
    records = []
    for name, gate in EXPECTED.items():
        p = subprocess.run([sys.executable, '-O', str(here/'verify.py'), '--mutation', name],
                           text=True, capture_output=True, timeout=20, cwd=here)
        actual = p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ''
        if p.returncode == 0 or actual != 'AssertionError: '+gate:
            raise RuntimeError(f'{name}: unexpected return {p.returncode}, {actual!r}')
        records.append({'mutation':name,'returncode':p.returncode,'rejected_at':gate})
    print(json.dumps({'status':'PASS_ALL_EIGHT_REJECTED','runs':records,
      'qualification':'The full-row-mollifier control is a valid weaker bound that fails the NEW 5/7 certificate; it is not a refutation of the old bound.'},sort_keys=True,indent=2))

if __name__ == '__main__':
    main()

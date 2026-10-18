"""Actual rejection tests for malformed degree22 proof parameters.

Each mutation is passed to the real certificate entry point. Every failure
must occur before the costly source reconstruction. Deposited certificate
status strings and solver reports are never inputs.
"""
from pathlib import Path
from contextlib import redirect_stdout
from copy import deepcopy
import hashlib
import importlib.util
import io
import json
import sys


def require(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    here = Path(__file__).resolve().parent
    theta = here.parent/'theta'
    sys.path.insert(0, str(theta))
    import certify
    original = (theta/'parameters22.json').read_text()
    p = json.loads(original)
    cases = []

    def change(name, mutate):
        q = deepcopy(p)
        mutate(q)
        cases.append((name, json.dumps(q)))

    change('missing_order22', lambda q: q.update(degree=20))
    change('lost_dimer_multiplicity', lambda q: q['counts'].__setitem__(1, 9))
    change('lost_parameter', lambda q: q['centers'].pop())
    change('duplicate_active_coordinate', lambda q: q['active'].__setitem__(1, q['active'][0]))
    change('deleted_hub_edges', lambda q: q.update(hub_correlation='0'))
    change('changed_proof_cube', lambda q: q.update(radius='1/1000'))
    change('nonpositive_dimer_coupling', lambda q: q['centers'].__setitem__(5, '1/2'))
    change('nonpositive_observable_weight', lambda q: q['centers'].__setitem__(3, '0'))
    change('floating_parameter', lambda q: q['centers'].__setitem__(3, 0.5))
    change('nonfinite_parameter', lambda q: q['centers'].__setitem__(3, float('nan')))
    key = '"schema":'
    # Work independently of whitespace in the original proof data.
    simple = json.dumps(p)
    require(key in simple, 'Missing schema key in mutation source.')
    cases.append(('duplicate_json_key', simple.replace(key, '"schema":"bad","schema":', 1)))
    scratch = here/'_scratch'
    scratch.mkdir(exist_ok=True)
    require(scratch.resolve().is_relative_to(here.resolve()), 'Scratch path escaped reviews.')
    rows = []
    for name, body in cases:
        path = scratch/(name+'.json')
        path.write_text(body, encoding='utf-8')
        captured = io.StringIO()
        try:
            with redirect_stdout(captured):
                certify.certify(path)
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            require('FRESH_COMPLETE_THETA_SOURCE' not in captured.getvalue(),
                    'Invalid parameter reached expensive source reconstruction.')
            rows.append({'mutation': name, 'rejected': True,
                         'exception': type(exc).__name__, 'reason': str(exc)})
        else:
            raise ValueError('Malformed proof parameters accepted: '+name)
    result = {'status': 'PASS', 'actual_rejections': rows,
              'degree22_parameter_sha256': hashlib.sha256(
                  (theta/'parameters22.json').read_bytes()).hexdigest(),
              'certifier_sha256': hashlib.sha256(
                  (theta/'certify.py').read_bytes()).hexdigest(),
              'fresh_source_or_model_existence_proved_by_this_check': False}
    out = here/'PARAMETER_REJECTIONS.json'
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'actual_rejections': len(rows),
                      'output': str(out)}), flush=True)


if __name__ == '__main__':
    main()

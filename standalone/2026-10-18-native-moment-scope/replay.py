"""Reproduce the packet's finite checks; analytic proofs remain separate.

Use --intervals for the two larger directed experiments and --ct-source
for a separately downloaded, hash-pinned primary TeX file. No network,
compilation, manifest resealing or source writes occur implicitly.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(args, optimized=False):
    command = [sys.executable, '-B']+(['-O'] if optimized else [])+args
    result = subprocess.run(command, cwd=HERE, text=True, capture_output=True, timeout=1800)
    if result.returncode:
        raise ValueError('Replay failed: '+str(args)+'\n'+result.stderr[-6000:])
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--intervals', action='store_true')
    parser.add_argument('--ct-source', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    executed = []
    for optimized in (False, True):
        run(['-m', 'unittest', '-q', 'test_exact'], optimized)
        executed.append({'test': 'exact and corruption suite', 'optimized': optimized, 'status': 'PASS'})
        for command, expected in ((['verify.py', '--column-cap', '4096', '--row-cap', '512'], 'EXTENDED_CHECKS.json'),):
            actual = run(command, optimized)
            if actual != (HERE/expected).read_text(encoding='utf-8'):
                raise ValueError('Finite report differed: '+expected)
            executed.append({'report': expected, 'optimized': optimized,
                             'sha256': hashlib.sha256(actual.encode()).hexdigest(), 'status': 'PASS'})
    if args.ct_source:
        for optimized in (False, True):
            actual = run(['audit_ct_source.py', '--source', str(args.ct_source.resolve())], optimized)
            if actual != (HERE/'CT_SOURCE_AUDIT.json').read_text(encoding='utf-8'):
                raise ValueError('Primary CT source audit differed.')
        executed.append({'test': 'pinned primary CT TeX source in both modes', 'status': 'PASS'})
    if args.intervals:
        for optimized in (False, True):
            run(['-m', 'unittest', '-q', 'test_gaussian'], optimized)
            executed.append({'test': 'directed primitive and corruption suite',
                             'optimized': optimized, 'status': 'PASS'})
        for command, expected in ((['replay_gaussian.py'], 'GAUSSIAN_REPLAY.json'),
                                  (['gaussian_native.py', '--replay', str(HERE/'NATIVE_GAUSSIAN.json')],
                                   'NATIVE_GAUSSIAN_REPLAY.json')):
            actual = run(command, optimized=True)
            if actual != (HERE/expected).read_text(encoding='utf-8'):
                raise ValueError('Directed replay report differed: '+expected)
            executed.append({'report': expected, 'optimized': True, 'status': 'PASS'})
        # Two different coefficient producers must agree on their common
        # original principal source, at every shared scale.
        principal = json.loads((HERE/'GAUSSIAN.json').read_text(encoding='utf-8'))
        native = json.loads((HERE/'NATIVE_GAUSSIAN.json').read_text(encoding='utf-8'))
        for a, b in zip(principal['values'], native['values']):
            if a['D'] != b['D'] or a['rows'][0]['enclosure'] != b['all_native_rows'][0]['real']:
                raise ValueError('The two primitive principal sources disagreed.')
        executed.append({'test': 'principal-source agreement between distinct local coefficient paths with a shared support sieve',
                         'common_scales': len(native['values']), 'status': 'PASS'})
    report = {'status': 'PASS: declared finite replay only', 'executed': executed,
              'boundary': 'No infinite analytic theorem, global sign, RH proof or independent referee acceptance is certified.'}
    text = json.dumps(report, sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8', newline='\n')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()

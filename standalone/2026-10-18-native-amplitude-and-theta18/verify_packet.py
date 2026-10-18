#!/usr/bin/env python3
"""Authenticate and replay the complete frozen research packet using stdlib."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def authenticate():
    raw = (ROOT / 'MANIFEST.json').read_bytes()
    manifest = json.loads(raw)
    require(manifest['schema'] == 'riemann-native-theta18.manifest.v1', 'manifest schema')
    records = manifest['files']
    names = [r['path'] for r in records]
    require(len(names) == len(set(names)), 'duplicate manifested path')
    actual = set()
    for path in ROOT.rglob('*'):
        require(not path.is_symlink(), 'symlink in packet')
        rel = path.relative_to(ROOT)
        if '__pycache__' in rel.parts:
            continue
        if path.is_file() and str(rel) != 'MANIFEST.json':
            actual.add(rel.as_posix())
    require(actual == set(names), 'complete file inventory differs from manifest')
    size = 0
    for record in records:
        rel = Path(record['path'])
        require(not rel.is_absolute() and '..' not in rel.parts, 'invalid manifested path')
        data = (ROOT / rel).read_bytes()
        require(len(data) == record['bytes'], 'byte length: ' + str(rel))
        require(sha256(data) == record['sha256'], 'SHA-256: ' + str(rel))
        require(blob(data) == record['git_blob'], 'Git blob: ' + str(rel))
        size += len(data)
    return {'payload_files': len(records), 'payload_bytes': size,
            'manifest_sha256': sha256(raw)}


def execute(label, argv, cwd=ROOT):
    print('REPLAY_START', label, flush=True)
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(label + ' failed\n' + result.stdout[-5000:] + result.stderr[-5000:])
    print('REPLAY_PASS', label, flush=True)
    return result.stdout


def replay():
    python = sys.executable
    out = []
    expected = (ROOT / 'critical/ALL_ORDER_CHECKS.json').read_text()
    for flags, label in [([], 'all-order-normal'), (['-O'], 'all-order-optimized')]:
        value = execute(label, [python, *flags, str(ROOT / 'critical/verify_all_order.py')])
        require(value == expected, label + ' must reproduce exact report bytes')
        require(json.loads(value)['explicit_checks'] == 908, 'all-order complete count')
        out.append({'name': label, 'status': 'PASS', 'explicit_checks': 908})
    require((ROOT / 'critical/ALL_ORDER_CHECKS_OPTIMIZED.json').read_text() == expected,
            'stored optimized all-order report')
    with tempfile.TemporaryDirectory(prefix='riemann-theta18-replay-') as temp:
        temp = Path(temp)
        staged = temp / 'critical'
        shutil.copytree(ROOT / 'critical', staged, ignore=shutil.ignore_patterns('__pycache__'))
        value = execute('all-order-negative-controls',
                        [python, '-O', str(staged / 'run_all_order_mutations.py')], cwd=staged)
        require(value == (ROOT / 'critical/ALL_ORDER_MUTATIONS.json').read_text(),
                'negative-control exact report')
        report = json.loads(value)
        require(len(report['mutations']) == 9 and all(r['returncode'] != 0 for r in report['mutations']),
                'all nine corrupted processes must reject')
        out.append({'name': 'all-order-negative-controls', 'status': 'PASS', 'rejected_processes': 9})
        expected_newton = (ROOT / 'newton/CHECKS.json').read_bytes()
        for flags, label in [([], 'newton-normal'), (['-O'], 'newton-optimized')]:
            dest = temp / (label + '.json')
            execute(label, [python, *flags, str(ROOT / 'newton/check_amplitude.py'), '--output', str(dest)])
            require(dest.read_bytes() == expected_newton, label + ' exact report')
            require(json.loads(dest.read_text())['total_checks'] == 10364, 'complete Newton count')
            out.append({'name': label, 'status': 'PASS', 'explicit_checks': 10364})
        require((ROOT / 'newton/CHECKS_OPTIMIZED.json').read_bytes() == expected_newton,
                'stored optimized Newton report')
        for flags, label in [([], 'theta18-full-source-normal'), (['-O'], 'theta18-full-source-optimized')]:
            value = execute(label, [python, *flags, str(ROOT / 'lee_yang/certify_chain.py'),
                                    '--check', str(ROOT / 'lee_yang/chain_certificate.json')])
            require('T18C_FULL_SOURCE_CERTIFICATE_PASS' in value, label + ' final acceptance')
            out.append({'name': label, 'status': 'PASS',
                        'certificate_sha256': sha256((ROOT / 'lee_yang/chain_certificate.json').read_bytes())})
        for flags, label in [([], 'independent-full-tree-normal'), (['-O'], 'independent-full-tree-optimized')]:
            value = execute(label, [python, *flags, str(ROOT / 'check_chain_transfer.py'),
                                    '--data', str(ROOT / 'lee_yang')])
            require(value == (ROOT / 'CHAIN_TRANSFER_CHECKS.json').read_text(),
                    label + ' exact report')
            out.append({'name': label, 'status': 'PASS', 'vertices': 281, 'raw_orders': 21,
                        'small_graph_configurations': 128})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--replay', action='store_true')
    ap.add_argument('--report', type=Path)
    args = ap.parse_args()
    before = authenticate()
    print('PACKET_MANIFEST_PASS', before['payload_files'], flush=True)
    results = replay() if args.replay else []
    after = authenticate()
    require(after == before, 'replay changed the frozen packet')
    report = {'status': 'PASS', 'manifest': before, 'replayed': args.replay,
              'stages': results,
              'scope': 'Exact payload and declared finite checks; analytic imports and RH are not certified by replay'}
    text = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if args.report:
        require(not args.report.resolve().is_relative_to(ROOT), 'write replay receipt outside frozen packet')
        args.report.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()

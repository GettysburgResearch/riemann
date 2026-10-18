#!/usr/bin/env python3
"""Authenticate this proposed research packet and optionally replay its checkers.

This is a file-integrity and finite-reproduction tool, not a mathematical
proof checker for the analytic theorems or an RH/zero-free-strip certificate.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def authenticate():
    manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
    require(manifest['schema'] == 'riemann.theta26-critical-family.manifest.v1',
            'manifest schema')
    expected = set()
    total = 0
    for item in manifest['files']:
        name = item['path']
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts,
                'relative manifest path')
        require(name not in expected and name != 'MANIFEST.json', 'unique payload path')
        expected.add(name)
        path = ROOT / name
        require(path.is_file() and not path.is_symlink(), 'regular payload file: ' + name)
        raw = path.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        require(len(raw) == item['bytes'] and digest(raw) == item['sha256']
                and blob == item['git_blob'], 'payload identity: ' + name)
        total += len(raw)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.name != 'MANIFEST.json'}
    require(actual == expected, 'complete payload inventory')
    print('PACKET_AUTHENTICATED', len(expected), 'FILES', total, 'BYTES', flush=True)
    return manifest


def replay(spec, optimized, destination):
    output = destination / (spec['name'] + ('_optimized' if optimized else '') + '.json')
    command = [sys.executable, '-S', '-B']
    if optimized:
        command.append('-O')
    command.extend([str(ROOT / spec['script']), *spec.get('args', [])])
    command.extend([spec.get('output_flag', '--output'), str(output)])
    if spec.get('complete_source') and not optimized:
        command.append('--rebuild-source')
    run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=240)
    require(run.returncode == 0,
            spec['name'] + ' failed:\n' + run.stdout[-5000:] + run.stderr[-5000:])
    require(output.is_file(), spec['name'] + ' omitted its declared receipt')
    raw = output.read_bytes()
    require(raw == (ROOT / spec['expected']).read_bytes(),
            spec['name'] + ' receipt differs from the frozen record')
    result = {'name': spec['name'], 'optimized': optimized, 'status': 'PASS',
              'sha256': digest(raw),
              'complete_source_rebuilt': bool(spec.get('complete_source') and not optimized)}
    print('REPLAY_PASS', result['name'], 'OPTIMIZED' if optimized else 'NORMAL',
          result['sha256'], flush=True)
    return result


def negative_controls(destination):
    """Reject altered provenance, an invalid node, and two false Newton claims."""
    original = json.loads((ROOT / 'theta/gaussian_parameters.json').read_text())
    cases = []
    source = json.loads((ROOT / 'theta/theta26_source.json').read_text())
    source['raw']['0'][0] += 1
    path = destination / 'changed_source.json'
    path.write_text(json.dumps(source))
    cases.append(('source_identity', '--source-json', path,
                  'authenticated complete-source digest'))
    for name, expected in [
            ('negative_node', 'every quadratic node stays strictly positive'),
            ('zero_preconditioner', 'whole-cube Newton contraction'),
            ('insufficient_radius', 'strict self mapping of full parameter cube')]:
        altered = copy.deepcopy(original)
        first = altered['models'][0]
        if name == 'negative_node':
            first['centers'][0] = '-1'
        elif name == 'zero_preconditioner':
            first['preconditioner'] = [['0' for value in row]
                                       for row in first['preconditioner']]
        else:
            first['radius'] = '1e-120'
        path = destination / (name + '.json')
        path.write_text(json.dumps(altered))
        cases.append((name, '--parameters', path, expected))
    records = []
    for name, flag, path, expected in cases:
        output = destination / (name + '_unexpected_receipt.json')
        run = subprocess.run(
            [sys.executable, '-S', '-B', '-O', str(ROOT / 'theta/check_gaussian.py'),
             flag, str(path), '--output', str(output)],
            cwd=ROOT, capture_output=True, text=True, timeout=60)
        require(run.returncode != 0 and ('ValueError: ' + expected) in run.stderr,
                'negative control did not fail at its designated gate: ' + name)
        require(not output.exists(), 'rejected input wrote an accepting receipt: ' + name)
        records.append({'name': name, 'status': 'REJECTED_AT_DESIGNATED_GATE',
                        'gate': expected, 'optimized': True})
        print('NEGATIVE_CONTROL_PASS', name, flush=True)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', action='store_true')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    manifest = authenticate()
    results = []
    controls = []
    if args.replay:
        with tempfile.TemporaryDirectory(prefix='riemann-theta26-replay-') as temporary:
            destination = Path(temporary)
            with ThreadPoolExecutor(max_workers=4) as pool:
                jobs = [pool.submit(replay, spec, optimized, destination)
                        for spec in manifest['replays'] for optimized in (False, True)]
                for job in as_completed(jobs):
                    results.append(job.result())
            controls = negative_controls(destination)
        results.sort(key=lambda item: (item['name'], item['optimized']))
    report = {'status': 'PASS',
              'manifest_sha256': digest((ROOT / 'MANIFEST.json').read_bytes()),
              'payload_files': len(manifest['files']), 'replays': results,
              'negative_controls': controls,
              'scope': 'file integrity and finite replay; no new zeta boundary or RH proof'}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print('VERIFICATION_PASS', len(results), 'FINITE_REPLAYS',
          len(controls), 'REJECTED_CORRUPTIONS', flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Actual-CLI adversarial fixtures, not a proof of the analytic theorems."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def reseal(root):
    names = sorted(p.name for p in root.iterdir() if p.is_file() and p.name != 'SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(
        sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))


def change_json(path, mutate):
    data = json.loads(path.read_text())
    mutate(data)
    path.write_text(json.dumps(data, sort_keys=True, indent=2)+'\n')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--optimized', action='store_true')
    ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--stop', type=int, default=10)
    args = ap.parse_args()
    cases = [
        ('false_rh', 'stored result mismatch'),
        ('false_external_replay', 'source-lock contract mismatch'),
        ('empty_external_scope', 'source-lock contract mismatch'),
        ('larger_finite_range', 'stored result mismatch'),
        ('numeric_alias', 'stored result mismatch'),
        ('duplicate_json_key', 'duplicate JSON key'),
        ('non_finite_json', 'non-finite JSON number'),
        ('changed_proof', 'manifest hash mismatch'),
        ('missing_manifest_row', 'manifest coverage mismatch'),
        ('changed_parent', 'parent source mismatch'),
    ]
    if not 0 <= args.start < args.stop <= len(cases):
        raise ValueError('invalid rejection coverage slice')
    reports = []
    for name, expected in cases[args.start:args.stop]:
        with tempfile.TemporaryDirectory(prefix='annular-ht-') as t:
            base = Path(t)
            dst = base/ROOT.name
            shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns('__pycache__'))
            parent = base/'annular-scalar-route'
            parent.mkdir()
            for f in ('verify.py', 'PROOF.md'):
                shutil.copy2(ROOT.parent/'annular-scalar-route'/f, parent/f)
            result = dst/'result.json'
            if name == 'false_rh':
                change_json(result, lambda d: d.update(rh_proved=True))
                reseal(dst)
            elif name == 'false_external_replay':
                change_json(dst/'SOURCE_LOCK.json', lambda d: d['external_height'].update(replayed=True))
                reseal(dst)
            elif name == 'empty_external_scope':
                change_json(dst/'SOURCE_LOCK.json', lambda d: d.update(external_height={}))
                reseal(dst)
            elif name == 'larger_finite_range':
                change_json(result, lambda d: d['finite_scalar_range'].update(real_m_max=10**15))
                reseal(dst)
            elif name == 'numeric_alias':
                # 0 must not be accepted as false even though Python equates them.
                change_json(result, lambda d: d.update(rh_proved=0))
                reseal(dst)
            elif name == 'duplicate_json_key':
                result.write_text(result.read_text().replace('{', '{"rh_proved": false,', 1))
                reseal(dst)
            elif name == 'non_finite_json':
                result.write_text(result.read_text().replace('"rh_proved": false', '"rh_proved": NaN'))
                reseal(dst)
            elif name == 'changed_proof':
                with (dst/'PROOF.md').open('a') as f:
                    f.write('\nChanged premise.\n')
            elif name == 'missing_manifest_row':
                p = dst/'SHA256SUMS'
                p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n')
            elif name == 'changed_parent':
                with (parent/'PROOF.md').open('a') as f:
                    f.write('\nChanged parent.\n')
            cmd = [sys.executable, '-B']+(['-O'] if args.optimized else [])+[str(dst/'validate.py')]
            run = subprocess.run(cmd, text=True, capture_output=True, timeout=90)
            if run.returncode == 0 or expected not in run.stderr:
                raise RuntimeError(name+' did not reject for the intended reason: '+run.stderr)
            reports.append({'case': name, 'expected_error': expected, 'rejected': True})
    print(json.dumps({'status': ('PASS_HT_REJECTIONS' if (args.start,args.stop)==(0,10)
                                 else 'PASS_HT_REJECTION_SUBSET'),
                      'optimized_target': args.optimized, 'available_cases': 10,
                      'slice': [args.start,args.stop], 'count': len(reports), 'cases': reports}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

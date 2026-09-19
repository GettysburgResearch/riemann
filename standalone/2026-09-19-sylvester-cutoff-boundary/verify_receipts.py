#!/usr/bin/env python3
"""Rebuild all exact reports and authenticate committed canonical SHA-256 receipts."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path, help='optional directory for the full JSON reports')
    args = parser.parse_args()
    expected = json.loads((ROOT / 'RESULT_DIGESTS.json').read_text(encoding='utf-8'))
    jobs = [('boundary_results.json', 'boundary', 'calculate'),
            ('harmonic_results.json', 'harmonic_adapter', 'report'),
            ('lfamily_results.json', 'lfamily', 'report')]
    if set(expected) != {name for name, _, _ in jobs}:
        raise ValueError('unexpected report receipt names')
    reports = {}
    for name, module, function in jobs:
        obj = getattr(load(module), function)()
        raw = (json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != expected[name]:
            raise ValueError(f'exact report digest mismatch: {name}')
        reports[name] = raw
        print('PASS', name, digest, flush=True)
    # Write only after every report has passed. Existing files must agree.
    if args.write:
        args.write.mkdir(parents=True, exist_ok=True)
        for name, raw in reports.items():
            path = args.write / name
            if path.exists() and path.read_bytes() != raw:
                raise ValueError(f'refusing to replace a different report: {path}')
        for name, raw in reports.items():
            (args.write / name).write_bytes(raw)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Read-only bounded source inventory. This does not execute research code."""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def git(*args: str) -> bytes:
    return subprocess.check_output(['git', '-c', 'core.hooksPath=/dev/null', *args], cwd=ROOT)

def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    freeze = json.loads((HERE / 'SOURCE_FREEZE.json').read_text(), object_pairs_hook=unique_pairs)
    expected = {'reviews/A','reviews/B','reviews/C','reviews/D','reviews/D-final','reviews/D-pass3','reviews/D-pass4'}
    require({r['path'] for r in freeze['reviews']} == expected and len(freeze['reviews']) == 7, 'exact seven-tree coverage required')
    tree_receipts = []
    for record in freeze['reviews']:
        actual = git('rev-parse', 'HEAD:' + record['path']).decode().strip()
        require(actual == record['tree'], 'frozen review tree mismatch: ' + record['path'])
        tree_receipts.append(dict(record, observed_tree=actual))
    scopes = ['reviews', 'canonical/2026-08-22', 'integration/2026-09-06',
              'research/integrated', 'README.md', 'STATUS.md', 'RESULTS.md',
              'PROOF_GRAPH.md', 'OPEN_CUTS.md', 'REFUTATIONS.md', 'COMPUTATIONS.md',
              'HISTORY.md', 'FORMALIZATION.md', 'AGENTS.md', 'CONTRIBUTING.md',
              'docs/REVIEWING.md', 'formal/FORMAL_V0_1.md', 'formal/RESULTS.md',
              'formal/OPEN_GATES.md', 'formal/TRUST.md', 'formal/registry']
    names = sorted(set(git('ls-files', '-z', '--', *scopes).decode().split('\0')) - {''})
    files, omitted, tables = [], [], {}
    total = 0
    allowed = {'.md','.tsv','.json','.py','.sh','.cpp','.h','.lean','.yml','.yaml','.txt','.tex'}
    with zipfile.ZipFile(out / 'source_bundle.zip', 'w', zipfile.ZIP_DEFLATED) as bundle:
        for name in names:
            p = ROOT / name
            if p.suffix not in allowed and p.name not in {'SHA256SUMS','lean-toolchain'}:
                omitted.append({'path': name, 'reason': 'not in declared text bundle format'})
                continue
            require(not p.is_symlink() and p.is_file(), 'unexpected source file type: ' + name)
            data = p.read_bytes()
            if len(data) > 5_000_000 or total + len(data) > 40_000_000:
                omitted.append({'path': name, 'reason': 'bounded inspection bundle size limit'})
                continue
            data.decode('utf-8')
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            index_blob = git('rev-parse', 'HEAD:' + name).decode().strip()
            require(blob == index_blob, 'working bytes differ from committed blob: ' + name)
            total += len(data)
            files.append({'path': name, 'bytes': len(data), 'blob': blob, 'sha256': hashlib.sha256(data).hexdigest()})
            bundle.writestr(name, data)
            if p.suffix == '.tsv':
                rows = list(csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t'))
                tables[name] = {'rows': len(rows), 'columns': list(rows[0]) if rows else []}
        payload = {'schema':'riemann.integration.source-inventory.v1',
                   'commit':git('rev-parse','HEAD').decode().strip(),
                   'root_tree':git('rev-parse','HEAD^{tree}').decode().strip(),
                   'frozen_reviews':tree_receipts,'files':files,'bundle_omissions':omitted,
                   'tables':tables,'research_programs_executed':False,
                   'exhaustive_scientific_review':False,'rh_proved':False}
        bundle.writestr('BUNDLE_RECEIPT.json', json.dumps(payload, indent=2) + '\n')
    (out / 'source_inventory.json').write_text(json.dumps(payload, indent=2) + '\n')
    print(json.dumps({'marker':'PASS_FROZEN_REVIEW_SOURCE_INVENTORY',
        'commit':payload['commit'],'review_trees':len(tree_receipts),
        'bundled_files':len(files),'bundled_bytes':total,'bundle_omissions':len(omitted),
        'tables':tables,'scientific_acceptance':False,'rh_proved':False}, indent=2))

if __name__ == '__main__':
    main()

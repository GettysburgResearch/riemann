#!/usr/bin/env python3
"""Verify retained bytes and packet coverage; NOT a mathematical proof checker.

Usage: python verify_packet.py [--self-test]
Only top-level reconstructed Markdown links are checked. Historical source
notes are immutable records and may contain their historical external links.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import unquote

def strict_json(text: str):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=unique)

def validate(root: Path, check_external_sibling: bool = True) -> dict:
    root = root.resolve()
    manifest = strict_json((root / 'artifacts/SOURCE_MANIFEST.json').read_text())
    source = root / manifest['retained_root']
    expected = set()
    for row in manifest['files']:
        rel = Path(row['path'])
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('unsafe source path')
        path = source / rel
        data = path.read_bytes()
        if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError(f"retained source mismatch: {rel}")
        if rel.as_posix() in expected:
            raise ValueError('duplicate manifest path')
        expected.add(rel.as_posix())
    actual = {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}
    if actual != expected or len(expected) != manifest['retained_file_count']:
        raise ValueError('retained source inventory mismatch')
    text = (root / 'ORIGINAL_QUESTIONS.md').read_text()
    if re.findall(r'^## U([1-8]) ', text, re.M) != [str(n) for n in range(1, 9)]:
        raise ValueError('question coverage must be U1 through U8 in order')
    links = 0
    for page in root.glob('*.md'):
        for href in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            if href.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            rel = unquote(href.split('#', 1)[0])
            if not rel:
                continue
            target = (page.parent / rel).resolve()
            if not target.is_relative_to(root):
                allowed = root.parent / '2026-09-18-vasyunin-support-leakage'
                if not target.is_relative_to(allowed):
                    raise ValueError(f'unexpected external relative link: {href}')
                if not check_external_sibling:
                    continue
            if not target.exists():
                raise ValueError(f'broken link in {page.name}: {href}')
            links += 1
    replay = strict_json((root / 'validation/replay.json').read_text())
    if len(replay['records']) != 7 or not all(r['passed'] and r['returncode'] == 0 for r in replay['records']):
        raise ValueError('fresh replay inventory incomplete')
    for row in replay['records']:
        for stream in ['stdout', 'stderr']:
            p = root / 'validation' / (row['name'] + '.' + stream + '.txt')
            if hashlib.sha256(p.read_bytes()).hexdigest() != row[stream + '_sha256']:
                raise ValueError('replay output hash mismatch')
    if len(re.findall(r'^\| ZIC-\d\d \|', (root/'CLAIM_LEDGER.md').read_text(), re.M)) != 46:
        raise ValueError('claim ledger incomplete')
    if len(re.findall(r'^\| C\d\d \|', (root/'CORRECTIONS.md').read_text(), re.M)) != 38:
        raise ValueError('correction ledger incomplete')
    return {'status': 'PASS: integrity and coverage only', 'retained_files': len(expected),
            'user_turns': 8, 'claim_entries': 46, 'correction_entries': 38,
            'top_level_local_links': links, 'fresh_replay_commands': 7}

def self_test(root: Path) -> list[str]:
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / 'packet'
        shutil.copytree(root, copy)
        def reject(name, relative, mutate):
            path = copy / relative
            old = path.read_bytes()
            path.write_bytes(mutate(old))
            try:
                validate(copy, check_external_sibling=False)
            except (ValueError, FileNotFoundError):
                failures.append(name)
            else:
                raise RuntimeError(f'mutation was accepted: {name}')
            finally:
                path.write_bytes(old)
        reject('altered_retained_source', 'artifacts/retained/01_arithmetic_certificate/rh_arithmetic_certificate.py', lambda x: x+b'\n# mutated\n')
        reject('missing_question', 'ORIGINAL_QUESTIONS.md', lambda x: x.replace(b'## U4 ', b'## OMITTED ', 1))
        reject('altered_replay_output', 'validation/support_normal.stdout.txt', lambda x: x+b' ')
        reject('duplicate_json_key', 'validation/replay.json', lambda x: b'{"records":[],"records":[]}')
    return failures

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    result = validate(root)
    if args.self_test:
        result['rejected_controls'] = self_test(root)
    print(json.dumps(result, indent=2, sort_keys=True))

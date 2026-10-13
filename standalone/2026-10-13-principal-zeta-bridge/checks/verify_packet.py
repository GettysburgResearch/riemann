#!/usr/bin/env python3
"""Verify publication bytes and review targets, not mathematical truth."""
from pathlib import Path
import hashlib
import json
import subprocess

PACKET = Path(__file__).resolve().parents[1]
REPO = PACKET.parents[1]
PREFIX = PACKET.relative_to(REPO).as_posix()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(['git', *args], cwd=REPO, check=True,
                          capture_output=True).stdout


def main():
    manifest = json.loads((PACKET / 'MANIFEST.json').read_text())
    actual = {p.relative_to(PACKET).as_posix()
              for p in PACKET.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts and p.name != 'MANIFEST.json'}
    expected = {row['path'] for row in manifest['files']}
    require(actual == expected, 'Publication file inventory differs')
    for row in manifest['files']:
        data = (PACKET / row['path']).read_bytes()
        require(len(data) == row['bytes'], 'Length differs: ' + row['path'])
        require(digest(data) == row['sha256'], 'Hash differs: ' + row['path'])

    reviews = json.loads((PACKET / 'REVIEW_INDEX.json').read_text())
    source = reviews['source_commit']
    tree = git('rev-parse', source + '^{tree}').decode().strip()
    parent = git('rev-parse', source + '^').decode().strip()
    require(tree == reviews['source_tree'], 'Frozen source tree differs')
    require(parent == reviews['source_parent'], 'Frozen source parent differs')
    lock_bytes = git('show', source + ':' + PREFIX + '/SOURCE_FREEZE_MANIFEST.json')
    require(lock_bytes == (PACKET / 'SOURCE_FREEZE_MANIFEST.json').read_bytes(),
            'Frozen source manifest was changed')
    lock = json.loads(lock_bytes)
    changed_after_review = set(reviews['mutable_source_paths'])
    for row in lock['files']:
        frozen = git('show', source + ':' + PREFIX + '/' + row['path'])
        require(digest(frozen) == row['sha256'], 'Frozen hash differs: ' + row['path'])
        if row['path'] not in changed_after_review:
            require(frozen == (PACKET / row['path']).read_bytes(),
                    'Reviewed source bytes changed: ' + row['path'])
    require(git('show', source + ':README.md') == (REPO / 'README.md').read_bytes(),
            'Root navigation differs from the reviewed source commit')

    ledger = json.loads((PACKET / 'SOURCES.json').read_text())
    for row in ledger['repository_sources']:
        require(digest((PACKET / row['snapshot_path']).read_bytes()) == row['sha256'],
                'Repository snapshot differs: ' + row['snapshot_path'])

    covered = {row['path']: [] for row in reviews['proof_authorship']}
    for review in reviews['reviews']:
        data = (PACKET / review['report']).read_bytes()
        require(digest(data) == review['report_sha256'], 'Review report differs')
        require(review['source_commit'] == source, 'Review targets another commit')
        for target in review['targets']:
            data = git('show', source + ':' + PREFIX + '/' + target['path'])
            require(digest(data) == target['sha256'], 'Review target differs')
            if review['verdict'] == 'PASS' and target['path'] in covered:
                covered[target['path']].append(review['reviewer'])
    for row in reviews['proof_authorship']:
        others = set(covered[row['path']]) - set(row['authors'])
        require(bool(others), 'No separate-author review: ' + row['path'])

    print(json.dumps({
        'status': 'PASS', 'source_commit': source, 'source_tree': tree,
        'publication_files_excluding_manifest': len(expected),
        'frozen_source_files': len(lock['files']),
        'repository_snapshots': len(ledger['repository_sources']),
        'review_reports': len(reviews['reviews']),
        'proof_files_with_separate_author_review': len(covered),
        'scope': 'File integrity, exact source/review binding, and disclosed authorship only; no analytic certification.',
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

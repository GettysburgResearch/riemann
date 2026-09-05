#!/usr/bin/env python3
"""Validate this inventory's syntax and declared denominator, NOT review completeness."""
from __future__ import annotations
import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

FIELDS = ['item_id', 'frozen_source', 'locator', 'reviewer', 'coverage', 'dependencies', 'disposition', 'notes']
ISSUES = {736, 737, 738, 739, 740, 741, 743, 744, 746, 763, 764}
SOURCE = re.compile(r'(?:[0-9a-f]{40}|UNRESOLVED_SHORT_SHA:[0-9a-f]{8}|issue:[0-9]+@C-observation-2026-09-05|arXiv:2609\.04176v1)\Z')


def check(data: bytes) -> dict:
    reader = csv.DictReader(io.StringIO(data.decode('utf-8')), delimiter='\t')
    if reader.fieldnames != FIELDS:
        raise ValueError('wrong census header')
    rows = list(reader)
    ids = [r['item_id'] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate census identity')
    known = set(ids)
    for row in rows:
        if set(row) != set(FIELDS) or any(v is None for v in row.values()):
            raise ValueError('wrong field count')
        if any(not row[k] for k in FIELDS[:-1]):
            raise ValueError('missing required value')
        if not SOURCE.fullmatch(row['frozen_source']):
            raise ValueError('invalid or untyped source')
        if row['reviewer'] not in {'A', 'B', 'C'}:
            raise ValueError('invalid reviewer')
        if set(row['dependencies'].split(';')) - known:
            raise ValueError('unresolved census dependency')
        if row['reviewer'] in {'A', 'B'} and row['disposition'] != 'pending integrator reconciliation':
            raise ValueError('unreconciled science promoted')
    old = [r for r in rows if r['item_id'].startswith('OLD-')]
    prs = {int(r['item_id'][3:]) for r in rows if re.fullmatch(r'PR-\d+', r['item_id'])}
    issues = {int(r['item_id'][6:]) for r in rows if re.fullmatch(r'ISSUE-\d+', r['item_id'])}
    expected_old = {337, *range(368, 708)}
    if {int(r['item_id'][4:]) for r in old} != expected_old:
        raise ValueError('historical denominator differs')
    if prs != set(range(708, 798)) - ISSUES or issues != ISSUES:
        raise ValueError('postcut denominator differs')
    matches = sum(r['coverage'] == 'B1' for r in old)
    unchecked = sum(r['coverage'] == 'B0' for r in old)
    absent = sum(r['coverage'] == 'historical-absence' for r in old)
    if (len(rows), matches, unchecked, absent) != (566, 28, 312, 1):
        raise ValueError('declared first-pass counts differ')
    return {
        'inventory_structure_valid': True,
        'review_completeness_certified': False,
        'rows': len(rows), 'historical_rows': len(old), 'real_historical_prs': len(old)-absent,
        'historical_heads_compared': matches, 'historical_heads_uncompared': unchecked,
        'historical_no_object_slots': absent, 'postcut_prs': len(prs), 'programme_issues': len(issues),
        'sha256': hashlib.sha256(data).hexdigest(),
        'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, default=Path(__file__).with_name('CENSUS.tsv'))
    args = parser.parse_args()
    print(json.dumps(check(args.path.read_bytes()), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

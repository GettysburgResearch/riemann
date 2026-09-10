#!/usr/bin/env python3
"""Authenticate the local packet inventory; not a mathematical proof checker."""
import hashlib,json,sys
from pathlib import Path
P=Path(__file__).resolve().parent
try:
    records={}
    for line in (P/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        if len(h)!=64 or any(x not in '0123456789abcdef' for x in h) or '/' in n or n in records or n=='SHA256SUMS':
            raise ValueError('invalid manifest entry')
        records[n]=h
    if any(x.is_dir() for x in P.iterdir()):raise ValueError('unexpected directory')
    files={x.name for x in P.iterdir() if x.is_file()}
    if files!=set(records)|{'SHA256SUMS'}:raise ValueError('inventory mismatch')
    for n,h in records.items():
        if hashlib.sha256((P/n).read_bytes()).hexdigest()!=h:raise ValueError('hash mismatch: '+n)
    for stem in ['checks','source']:
        if (P/(stem+'.normal.json')).read_bytes()!=(P/(stem+'.optimized.json')).read_bytes():raise ValueError('mode mismatch')
    checks=json.loads((P/'checks.normal.json').read_text());source=json.loads((P/'source.normal.json').read_text())
    if checks['RH_proved'] is not False or checks['analytic_theorems_machine_checked'] is not False:raise ValueError('mathematical scope')
    if source['RH_proved'] is not False or source['higher_rank_extrapolation'] is not False:raise ValueError('source scope')
    if source['integer_cutoff']!=4096 or source['complete_cells']!=4095:raise ValueError('source coverage')
    if checks['named_checks']!=13 or checks['fixtures']!=1004:raise ValueError('finite coverage')
    print(json.dumps({'status':'PASS_PACKET_BYTES','files':len(files),'hashes':len(records)},sort_keys=True))
except (ValueError,OSError,KeyError) as e:
    print(json.dumps({'status':'REJECTED','reason':str(e)},sort_keys=True));sys.exit(2)

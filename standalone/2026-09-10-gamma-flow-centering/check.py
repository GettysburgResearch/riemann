#!/usr/bin/env python3
"""Authenticate and freshly reconstruct the two complete GFC26 root certificates.

--emit is producer-only. A PASS requires --expect, typed equality with a complete
fresh reconstruction, and unchanged packet bytes. No parent code is imported.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
NAMES = {
    'PROOF.md','README.md','SOURCES.json','VALIDATION.md','interval.py',
    'certificate.py','check.py','test_check.py','results.json',
    'scout.py','scout.json','SHA256SUMS',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def decode(data):
    def pairs(items):
        out = {}
        for k, v in items:
            require(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    def bad(_):
        raise ValueError('floating/nonfinite JSON number')
    return json.loads(data, object_pairs_hook=pairs, parse_float=bad,
                      parse_constant=bad)


def equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(equal(x,y) for x,y in zip(a,b))
    return a == b


def shape(value):
    require(type(value) is dict, 'receipt object')
    require(value.get('schema') == 'GFC26-v1', 'schema')
    require(value.get('status') == 'PROPOSED_COMPONENTS_WITH_TWO_ROOT_CERTIFICATES','status')
    for key in ('rh_proved','actual_zeta_zero_certified','all_order_confinement_proved'):
        require(type(value.get(key)) is bool and value[key] is False, key)
    rows=value.get('zero_certificates')
    require(type(rows) is list and len(rows)==2, 'complete two-source coverage')
    for row, name, rates in zip(rows, ('N4','FLOW_u_7_over_10'),
            ([['1','1'],['4','1'],['9','1'],['16','1']],
             [['1','1'],['4','1'],['90','7']])):
        require(type(row) is dict and row.get('name')==name, 'source name')
        require(equal(row.get('rates'), rates), 'actual gamma rates')
        require(equal(row.get('radius'), ['1','1000000']), 'fixed disk radius')
        for key, n in (('bits',512),('degree',40),('cells',256)):
            require(type(row.get(key)) is int and row[key]==n, key)
        require(type(row.get('exactly_one_zero')) is bool and row['exactly_one_zero'], 'zero count flag')
        require(type(row.get('rh_proved')) is bool and row['rh_proved'] is False, 'source status')
        require(type(row.get('integral_jets')) is list and len(row['integral_jets'])==3,'three full jets')


def inventory():
    actual=set()
    for entry in ROOT.iterdir():
        require(not entry.is_symlink(), 'symbolic link in packet')
        # bytecode caches are never created by the documented -B entry point.
        require(entry.is_file(), 'nonregular packet entry')
        actual.add(entry.name)
    require(actual==NAMES, 'packet inventory mismatch')
    manifest={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest, name=line.split('  ',1)
        require(name in NAMES-{'SHA256SUMS'} and name not in manifest,'manifest path')
        require(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'digest format')
        manifest[name]=digest
    require(set(manifest)==NAMES-{'SHA256SUMS'}, 'manifest completeness')
    result={}
    for name in sorted(NAMES):
        data=(ROOT/name).read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        if name!='SHA256SUMS':
            require(digest==manifest[name], 'changed packet file: '+name)
        result[name]=digest
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--expect',type=Path)
    group.add_argument('--emit',type=Path)
    args=parser.parse_args()
    before=inventory()
    expected=None
    if args.expect:
        require(not args.expect.is_symlink(),'symlink receipt')
        expected=decode(args.expect.read_bytes())
        shape(expected)
    # Under -I the explicitly authenticated packet directory is added only here.
    sys.path.insert(0,str(ROOT))
    from certificate import build_result
    actual=build_result()
    shape(actual)
    require(inventory()==before,'packet changed during reconstruction')
    canonical=json.dumps(actual,sort_keys=True,indent=2)+'\n'
    if args.expect:
        require(equal(actual,expected),'complete numerical reconstruction mismatch')
        print('PASS_GFC_TWO_COMPLETE_ROOT_CERTIFICATES')
        print(hashlib.sha256(canonical.encode()).hexdigest())
    else:
        dest=args.emit.resolve()
        require(not dest.is_relative_to(ROOT),'producer output must be outside packet')
        dest.write_text(canonical)
        print('PRODUCED_NOT_ACCEPTED')


if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError,TypeError,ArithmeticError) as error:
        print('FAIL_GFC: '+str(error),file=sys.stderr)
        sys.exit(1)

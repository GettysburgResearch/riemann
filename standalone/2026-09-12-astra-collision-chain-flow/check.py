#!/usr/bin/env python3
"""Reconstruct every accepting finite assertion; --emit is producer-only."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json
from pathlib import Path
import native_theta,research_algebra,calibrated_chain,gamma_score

ROOT=Path(__file__).resolve().parent

def canonical(x):return (json.dumps(x,sort_keys=True,indent=2,ensure_ascii=True,allow_nan=False)+'\n').encode('utf-8')

def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('duplicate JSON key: '+k)
            out[k]=v
        return out
    def no_float(s):raise ValueError('floating JSON numbers are forbidden: '+s)
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float)

def authenticate(root=ROOT):
    manifest=root/'SHA256SUMS'
    if not manifest.is_file() or manifest.is_symlink():raise ValueError('missing regular SHA256SUMS')
    expected={}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        h,name=line.split('  ',1)
        if len(h)!=64 or any(c not in '0123456789abcdef' for c in h) or '/' in name or '\\' in name or name in ('.','..','SHA256SUMS') or name in expected:
            raise ValueError('invalid manifest record')
        expected[name]=h
    actual={p.name for p in root.iterdir()}
    if actual!=set(expected)|{'SHA256SUMS'}:raise ValueError('packet inventory mismatch')
    for name,h in expected.items():
        p=root/name
        if p.is_symlink() or not p.is_file():raise ValueError('packet entries must be regular files')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError('packet hash mismatch: '+name)
    return len(expected)+1

def reconstruct():
    theta=native_theta.report(128)
    algebra=research_algebra.report()
    return {'packet':'CCF26','date':'2026-09-12','rh_proved':False,
            'status':'PROPOSED component proofs; independent review required',
            'theta':theta,'arithmetic':algebra['arithmetic'],
            'ising':calibrated_chain.seed_certificate(theta),'chain_algebra':algebra['ising'],
            'gamma_algebra':algebra['gamma'],'gamma_positive_score':gamma_score.report(),
            'remote_publication_verified':False,'repository_wide_validation_run':False}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--check',type=Path);g.add_argument('--emit',type=Path)
    a=p.parse_args()
    if a.emit:
        result=reconstruct();a.emit.write_bytes(canonical(result))
        print('PRODUCED_ONLY '+hashlib.sha256(canonical(result)).hexdigest());return 0
    count=authenticate();received=strict_json(a.check);expected=reconstruct()
    if canonical(received)!=canonical(expected):raise ValueError('typed result differs from complete fresh reconstruction')
    print('PASS '+hashlib.sha256(canonical(expected)).hexdigest()+' files='+str(count))
    return 0
if __name__=='__main__':
    try:raise SystemExit(main())
    except (ArithmeticError,ValueError,TypeError,OSError,KeyError,IndexError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);raise SystemExit(1)

#!/usr/bin/env python3
"""Regenerate every numerical input, exhaust the continuum cover, audit constants.
Requires an LP64 Linux host, a C++17 compiler and libmpfr.so.6. The complete
10 MB table is generated outside the sealed source packet, not treated as input.
"""
from pathlib import Path
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parent

def strict_load(text):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    def bad(x):raise ValueError('nonfinite JSON')
    return json.loads(text,object_pairs_hook=pairs,parse_constant=bad)

def same(a,b):
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def authenticate():
    manifest=ROOT/'SHA256SUMS'
    records={}
    for line in manifest.read_text().splitlines():
        if not line:continue
        h,name=line.split('  ',1)
        if name in records or len(h)!=64 or '/' in name or name in ('.','..'):raise ValueError('bad manifest')
        records[name]=h
    files={p.name for p in ROOT.iterdir()}
    if files!=set(records)|{'SHA256SUMS'}:raise ValueError('unexpected packet inventory')
    for name,h in records.items():
        p=ROOT/name
        if p.is_symlink() or not p.is_file():raise ValueError('not a regular payload file')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise ValueError('payload hash mismatch: '+name)

def cmd(args):
    r=subprocess.run([str(x) for x in args],capture_output=True,text=True,check=True)
    if r.stderr:sys.stderr.write(r.stderr)
    return r.stdout

def reconstruct(work,compiler='g++',precision=160,optimization='-O2'):
    if precision not in (160,256):raise ValueError('unsupported precision')
    if optimization not in ('-O0','-O1','-O2','-O3'):raise ValueError('bad optimization')
    if not shutil.which(compiler):raise RuntimeError('C++ compiler unavailable')
    work=Path(work);work.mkdir(parents=True,exist_ok=True)
    flags=[optimization,'-std=c++17','-fno-fast-math','-ffp-contract=off']
    cmd([compiler,*flags,f'-DTABLE_PREC={precision}',ROOT/'make_table.cpp','-l:libmpfr.so.6','-o',work/'make_table'])
    cmd([compiler,*flags,ROOT/'search.cpp','-o',work/'search'])
    table=work/'kernel.txt'
    cmd([work/'make_table',table])
    rows=table.read_bytes().split(b'\n',1)
    payload_sha=hashlib.sha256(rows[1]).hexdigest()
    search=strict_load(cmd([work/'search',table,'13777','4000000','3433']))
    rational=strict_load(cmd([sys.executable,'-I','-S','-B',ROOT/'rational_audit.py','--table',table]))
    return {'status':'PROPOSED_UNCONDITIONAL_REFINEMENT_REVIEW_REQUIRED',
            'rh_proved':False,'table_payload_sha256':payload_sha,
            'search':search,'rational_audit':rational}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path,default=ROOT/'result.json')
    ap.add_argument('--compiler',default='g++');ap.add_argument('--precision',type=int,default=160)
    ap.add_argument('--optimization',default='-O2');ap.add_argument('--keep-dir',type=Path)
    ap.add_argument('--emit',type=Path,help='producer-only output; does not claim acceptance')
    args=ap.parse_args();authenticate()
    if args.keep_dir:result=reconstruct(args.keep_dir,args.compiler,args.precision,args.optimization)
    else:
        with tempfile.TemporaryDirectory(prefix='spl26-') as work:
            result=reconstruct(work,args.compiler,args.precision,args.optimization)
    if args.emit:
        args.emit.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print('PRODUCED_ONLY');return
    expected=strict_load(args.check.read_text())
    if not same(result,expected):raise RuntimeError('regenerated mathematics does not match receipt')
    print(json.dumps({'accepted':True,'semantic_sha256':hashlib.sha256(json.dumps(result,sort_keys=True,separators=(',',':')).encode()).hexdigest()},sort_keys=True))
if __name__=='__main__':
    try:main()
    except Exception as e:
        print(f'REJECT: {e}',file=sys.stderr);raise SystemExit(1)

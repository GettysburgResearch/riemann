#!/usr/bin/env python3
"""Replay exactly pinned certificate subsets, not whole research packages.

Supply roots extracted from the commits in SOURCE_HEADS.json. This script uses
no network. It authenticates all five consumed source files before compiling
any of them. The WP result must also match its published complete result blob.
The author arithmetic implementations are reused, NOT independently replaced.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import types

PINS = {
 'wp/intervals.py': '22055a6404b36c208ea891728779bd6382be7722',
 'wp/verify.py': '07f4e69a6c8216d01a6f80cf29bb9330b0bffa9a',
 'wp/certificate.json': '1f56c8940b492241be50fa7ab7aea067962b5ec5',
 'ie/interval_core.py': '92f484bc6bc7b12bf26313bd7d323c637cd834b9',
 'ie/certificate.py': '02dcfed3b2539219bc07c56411510758932b8ccf',
}
WP_RESULT = 'a94e20c9cbdb16e29fc95d5a95d6be9e660de2e5'

def require(value, message):
    if not value: raise ValueError(message)

def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def authenticate(wp, ie):
    data={}
    for key, oid in PINS.items():
        group,name=key.split('/'); p=(wp if group=='wp' else ie)/name
        require(not any(x.is_symlink() for x in [p,*p.parents]), 'symlink input: '+key)
        require(p.is_file() and p.stat().st_size<100000, 'missing/oversized source: '+key)
        value=p.read_bytes()
        require(blob(value)==oid, 'source blob mismatch: '+key)
        data[key]=value
    return data

def module(name, data, path):
    obj=types.ModuleType(name);obj.__file__=str(path)
    sys.modules[name]=obj
    exec(compile(data,str(path),'exec'),obj.__dict__)
    return obj

def load_modules(data,wp,ie):
    a=module('intervals',data['wp/intervals.py'],wp/'intervals.py')
    b=module('review_wp',data['wp/verify.py'],wp/'verify.py')
    c=module('review_ie_core',data['ie/interval_core.py'],ie/'interval_core.py')
    d=module('review_ie_certificate',data['ie/certificate.py'],ie/'certificate.py')
    return a,b,c,d

def encode(value): return (json.dumps(value,sort_keys=True,indent=2)+'\n').encode()

def contracts(data,wp,ie,mods):
    a,b,c,d=mods;counts={}
    def test(group, ok):
        require(ok,'contract failed: '+group);counts[group]=counts.get(group,0)+1
    def reject(group, fn):
        try: fn()
        except (ValueError,TypeError,ZeroDivisionError,ArithmeticError):
            counts[group]=counts.get(group,0)+1
        else: raise ValueError('corruption accepted: '+group)
    rationals=[F(-7,3),F(-1,7),F(0),F(2,9),F(5,2)]
    for core, constructor, scale in ((a,a.I,a.S),(c,c.I.of,c.SCALE)):
        contains=lambda z,x: F(z.lo,scale)<=x<=F(z.hi,scale)
        for x in rationals:
            for y in rationals:
                u,v=constructor(x),constructor(y)
                test('primitive_containment',contains(u+v,x+y))
                test('primitive_containment',contains(u-v,x-y))
                test('primitive_containment',contains(u*v,x*y))
                if y: test('primitive_containment',contains(u/v,x/y))
        for bad in (True,1.25): reject('primitive_type_refusal',lambda bad=bad:constructor(bad))
        reject('zero_division_refusal',lambda:constructor(1)/constructor(0))
    cert=json.loads(data['wp/certificate.json'])
    mutations=[lambda x:x.__setitem__('finite_modes',True),
               lambda x:x.__setitem__('finite_modes',2048.0),
               lambda x:x.__setitem__('source_interval','2'),
               lambda x:x.__setitem__('half_period','1'),
               lambda x:x.__setitem__('scaled_margin','0'),
               lambda x:x['frequencies'].pop(),
               lambda x:x['weights'].__setitem__(0,'-1'),
               lambda x:x['extension_values'].__setitem__(0,'1'),
               lambda x:x.__setitem__('unknown',0)]
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'cert.json'
        for change in mutations:
            bad=copy.deepcopy(cert);change(bad);p.write_bytes(encode(bad))
            reject('WP_input_refusal',lambda:b.load(p))
        p.write_text('{"schema":0,"schema":1}',encoding='utf-8')
        reject('WP_duplicate_refusal',lambda:b.load(p))
        for key in PINS:
            bad=bytearray(data[key]);bad[-1]^=1
            test('source_mutation_detection',blob(bad)!=PINS[key])
    test('WP_output_type_refusal',not b.strict_equal({'count':1},{'count':True}))
    test('WP_output_type_refusal',not b.strict_equal({'count':1},{'count':1.0}))
    # These are real parser/core contracts, not the authors' full CLI suites.
    return {'marker':'PASS_PINNED_SUBSET_CONTRACTS','counts':counts,
            'total':sum(counts.values()),'full_author_suites_run':False,
            'independent_arithmetic_backend':False,'rh_proved':False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wp-root',type=Path,required=True)
    parser.add_argument('--ie-root',type=Path,required=True)
    parser.add_argument('--case',choices=['wp','ie','contracts'],required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();wp=args.wp_root.absolute();ie=args.ie_root.absolute()
    require(not args.output.exists(),'output must not already exist')
    data=authenticate(wp,ie);mods=load_modules(data,wp,ie)
    if args.case=='wp':
        # run() opens this pinned JSON once more; reauthenticate afterward.
        value=mods[1].run(wp/'certificate.json')
        require(blob(encode(value))==WP_RESULT,'published WP result mismatch')
    elif args.case=='ie': value=mods[3].certify(mods[2])
    else: value=contracts(data,wp,ie,mods)
    require(authenticate(wp,ie)==data,'source changed during execution')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(encode(value))
    print(json.dumps({'case':args.case,'result_git_blob':blob(encode(value)),
          'result_sha256':hashlib.sha256(encode(value)).hexdigest(),
          'authenticated_files':len(PINS),'full_repository_checkout':False,
          'scope':'exact source subset, not complete author package or suites'},sort_keys=True))

if __name__=='__main__': main()

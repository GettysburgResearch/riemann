#!/usr/bin/env python3
"""Full source reconstruction, or explicitly weaker authenticated receipt replay."""
from pathlib import Path
import argparse
import hashlib
import json
import sys
from native_sources import gamma5, theta, power_sums
from moment_tools import derive, interval
from exact_interval import SCALE

ROOT=Path(__file__).resolve().parent

def reject_duplicates(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=reject_duplicates,
                      parse_constant=lambda v:(_ for _ in ()).throw(ValueError('nonfinite JSON')))

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False)

def verify_manifest():
    if (ROOT/'MANIFEST.json').is_symlink():raise ValueError('ordinary manifest required')
    manifest=read_json(ROOT/'MANIFEST.json')
    if set(manifest)!={'schema','files'} or manifest['schema']!='MCE26-files-v1':raise ValueError('manifest schema')
    files=manifest['files']
    if type(files) is not dict or any(type(k)is not str or type(v)is not str for k,v in files.items()):raise TypeError('manifest types')
    actual={p.name for p in ROOT.iterdir() if p.name!='__pycache__'}
    if actual!=set(files)|{'MANIFEST.json'}:raise ValueError('unexpected packet inventory')
    for name,digest in files.items():
        if '/' in name or '\\' in name or name in ('.','..'):raise ValueError('manifest path')
        p=ROOT/name
        if p.is_symlink() or not p.is_file():raise ValueError('ordinary files only')
        if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:raise ValueError('file hash mismatch: '+name)

def reconstruct(progress=False):
    a=gamma5(progress=progress)
    b=theta()
    params=read_json(ROOT/'parameters.json')
    return {'schema':'MCE26-result-v1','source_gamma':a,'source_theta':b,'derived':derive(a,b,params)}

def replay_receipt(record):
    if type(record)is not dict or set(record)!={'schema','source_gamma','source_theta','derived'} or record['schema']!='MCE26-result-v1':raise ValueError('receipt schema')
    for key,fields in [('source_gamma',{'source':'literal centered gamma N=5','N':5,'order':14,'degree':48,'cells':964}),('source_theta',{'source':'complete native theta','order':16,'mesh':256})]:
        source=record[key]
        for field,wanted in fields.items():
            if field not in source or canonical(source[field])!=canonical(wanted):raise ValueError('source scope mismatch')
        coefficients=[interval(v) for v in source['f']]
        if coefficients[0].lo!=SCALE or coefficients[0].hi!=SCALE:raise ValueError('exact unit coefficient required')
        if canonical([v.bounds() for v in power_sums(coefficients)])!=canonical(source['scaled_power_sums']):raise ValueError('cached power sums inconsistent')
    proposed=derive(record['source_gamma'],record['source_theta'],read_json(ROOT/'parameters.json'))
    if canonical(proposed)!=canonical(record['derived']):raise ValueError('finite algebra / claim mismatch')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--emit',type=Path,help='producer only; freshly reconstruct complete sources')
    mode.add_argument('--check',type=Path,help='compare complete fresh reconstruction with receipt')
    parser.add_argument('--receipt-only',action='store_true',help='NO defining-integral replay; manifest plus finite algebra only')
    parser.add_argument('--progress',action='store_true')
    args=parser.parse_args()
    if args.emit:
        if args.receipt_only:raise ValueError('receipt-only cannot produce')
        result=reconstruct(args.progress)
        args.emit.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        print('PRODUCED complete-source receipt; not an independent review')
        return
    verify_manifest()
    expected=read_json(args.check)
    replay_receipt(expected)
    if args.receipt_only:
        print('PASS authenticated receipt + finite algebra ONLY; no native integral reconstruction')
    else:
        result=reconstruct(args.progress)
        if canonical(result)!=canonical(expected):raise ValueError('complete source reconstruction differs')
        print('PASS full defining-source and finite-algebra reconstruction')
    print('semantic_sha256='+hashlib.sha256(canonical(expected).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,ArithmeticError,KeyError,OSError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)

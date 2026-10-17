#!/usr/bin/env python3
"""Authenticate this frozen research packet and optionally replay its checks.

No network or third-party packages. Mathematical analytic inputs are not
computationally verified by this program.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise ValueError(message)

def file_sha(data):return hashlib.sha256(data).hexdigest()

def authenticate():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    require(manifest['schema']=='riemann.three-route-continuation.v1','manifest schema')
    listed=set()
    for entry in manifest['files']:
        rel=Path(entry['path'])
        require(not rel.is_absolute() and '..' not in rel.parts,'unsafe manifest path')
        require(rel.as_posix() not in listed,'duplicate manifest path')
        listed.add(rel.as_posix())
        data=(ROOT/rel).read_bytes()
        require(len(data)==entry['bytes'],str(rel)+' byte length')
        require(file_sha(data)==entry['sha256'],str(rel)+' SHA256')
        header=('blob '+str(len(data))).encode()+b'\0'
        require(hashlib.sha1(header+data).hexdigest()==entry['git_blob_sha'],str(rel)+' Git blob')
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
        and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='MANIFEST.json'}
    require(actual==listed,'manifest must cover every packet file exactly')
    return manifest

def command(args,cwd=ROOT):
    p=subprocess.run([sys.executable,*args],cwd=cwd,text=True,capture_output=True)
    require(p.returncode==0,'check failed: '+repr(args)+'\n'+p.stdout+'\n'+p.stderr)
    return p.stdout

def replay():
    outcomes=[]
    reports=[
        ('critical/verify_interpolation.py','critical/INTERPOLATION_CHECKS.json'),
        ('critical/verify_diagonal.py','critical/DIAGONAL_CHECKS.json'),
        ('critical/verify_local_domain.py','critical/LOCAL_DOMAIN_CHECKS.json'),
        ('critical/review_theta_independent.py','critical/INDEPENDENT_THETA_CHECKS.json'),
        ('theta/verify_theta.py','theta/THETA_CHECKS.json'),
        ('theta/verify_fourth.py','theta/FOURTH_CHECKS.json'),
    ]
    for script,report in reports:
        generated=json.loads(command([script]))
        require(generated==json.loads((ROOT/report).read_text()),script+' report differs')
        outcomes.append({'check':script,'status':'PASS'})
    with tempfile.TemporaryDirectory(prefix='riemann-newton-replay-') as temp:
        output=Path(temp)/'audit.json'
        command(['newton/check_newton.py','--output',str(output)])
        require(json.loads(output.read_text())==json.loads((ROOT/'newton/audit.json').read_text()),'Newton audit differs')
    outcomes.append({'check':'newton/check_newton.py','status':'PASS','complete_cases':22})
    opt=subprocess.run([sys.executable,'-O','newton/check_newton.py'],cwd=ROOT,text=True,capture_output=True)
    require(opt.returncode!=0 and 'Exact replay requires assertions' in (opt.stdout+opt.stderr),'Newton optimized execution must reject disabled assertions')
    outcomes.append({'check':'Newton optimization guard','status':'EXPECTED_REJECTION'})
    for script,report in [('certify_tree.py','tree_certificate.json'),('certify_edge.py','edge_certificate.json')]:
        output=command([script,'--check',report],ROOT/'lee_yang')
        outcomes.append({'check':'lee_yang/'+script,'status':'PASS','output':output.strip().splitlines()})
    return outcomes

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay',action='store_true')
    args=parser.parse_args()
    manifest=authenticate()
    result={'status':'PASS','file_count':len(manifest['files']),
        'manifest_sha256':file_sha((ROOT/'MANIFEST.json').read_bytes()),
        'scope':'File authentication and declared finite checks only; analytic inputs require mathematical review.'}
    if args.replay:result['replays']=replay()
    print(json.dumps(result,indent=2,sort_keys=True))

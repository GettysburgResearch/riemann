#!/usr/bin/env python3
"""Real CLI adverse tests for CFC26; finite controls, not proof verification."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent

def need(value, message):
    if not value:
        raise RuntimeError(message)

def reseal(root):
    entries=[]
    for p in sorted(root.iterdir()):
        if p.name == 'SHA256SUMS':
            continue
        need(p.is_file() and not p.is_symlink(), 'reseal requires regular payload')
        entries.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (root/'SHA256SUMS').write_text('\n'.join(entries)+'\n')

def change_result(root, change):
    p=root/'result.json'; data=json.loads(p.read_text()); change(data)
    p.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    reseal(root)

def change_code(root, old, new):
    p=root/'check.py';text=p.read_text()
    need(text.count(old)==1, 'expected one producer mutation anchor')
    p.write_text(text.replace(old,new)); reseal(root)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--optimized',action='store_true')
    args=ap.parse_args()
    prefix=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])
    def run(root):
        return subprocess.run(prefix+['check.py','--check','result.json'],
                              cwd=root,capture_output=True,timeout=60)
    results=[]
    with tempfile.TemporaryDirectory(prefix='cfc26-adverse-') as td:
        base=Path(td)
        pristine=base/'pristine';shutil.copytree(ROOT,pristine)
        p=run(pristine)
        need(p.returncode==0, 'pristine CLI failed: '+p.stderr.decode())
        expected=(ROOT/'result.json').read_bytes()
        need(p.stdout==expected,'pristine result mismatch')
        def test(name, mutate, reason):
            root=base/name;shutil.copytree(ROOT,root)
            mutate(root);r=run(root)
            stderr=r.stderr.decode(errors='replace')
            need(r.returncode==1 and 'REJECT:' in stderr and reason in stderr,
                 name+' wrong refusal: '+str(r.returncode)+' '+stderr)
            results.append({'name':name,'returncode':r.returncode,'refusal':stderr.strip()})
        test('false-closure',lambda r:change_result(r,lambda d:d.__setitem__('rh_proved',True)),
             'reconstructed mathematical result mismatch')
        test('boolean-alias',lambda r:change_result(r,lambda d:d.__setitem__('rh_proved',0)),
             'reconstructed mathematical result mismatch')
        def duplicate(r):
            p=r/'result.json';p.write_text(p.read_text().replace('{','{"rh_proved":false,',1));reseal(r)
        test('duplicate-json',duplicate,'duplicate JSON key')
        def floating(r):
            p=r/'result.json'; text=p.read_text();need('"checks":18' in text,'float anchor')
            p.write_text(text.replace('"checks":18','"checks":18.0',1));reseal(r)
        test('float-alias',floating,'floating/nonfinite JSON number')
        test('drop-chain-correlation',
             lambda r:change_code(r,'p=(1+Q*old*new)/2','p=F(1,2)'),
             'independent transfer/derivative enumeration mismatch')
        test('drop-cloud-compensation',
             lambda r:change_code(r,'ds=[-F(1,cloud)]*cloud+[F(0)]*tail','ds=[F(0)]*(cloud+tail)'),
             'calibration head sum derivative')
        def source_drift(r):
            p=r/'ICR_RECEIPT.json';p.write_bytes(p.read_bytes()+b' ');reseal(r)
        test('resealed-import-drift',source_drift,'imported primitive changed')
        def proof_edit(r):
            p=r/'PROOF.md';p.write_text(p.read_text()+'\nunauthenticated edit\n')
        test('unsealed-proof',proof_edit,'payload hash PROOF.md')
        test('extra-file',lambda r:(r/'unlisted.txt').write_text('unlisted\n'),
             'exact package inventory')
        def linked(r):
            p=r/'PROOF.md';target=base/'outside-proof.md';target.write_bytes(p.read_bytes())
            p.unlink();p.symlink_to(target)
        test('symlink-core',linked,'missing/nonregular payload PROOF.md')
    print(json.dumps({'schema':'CFC26.adverse.v1','optimized':args.optimized,
                      'pristine_acceptances':1,'actual_refusals':len(results),
                      'cases':results},sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()

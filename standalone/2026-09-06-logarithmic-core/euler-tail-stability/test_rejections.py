#!/usr/bin/env python3
"""Run actual CLI rejection tests in isolated, unprivileged temporary folders."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
CASES = [
    'rh_flag', 'claimed_native_sign', 'fake_parameter_certificate', 'boolean_count',
    'missing_scope', 'duplicate_json_key', 'changed_proof', 'missing_lock',
    'wrong_parent_head', 'changed_parent_proof',
]

def reseal(root):
    names = sorted(p.name for p in root.iterdir() if p.is_file() and p.name != 'SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def run_case(name, optimized, parent_root):
    with tempfile.TemporaryDirectory(prefix='riemann-euler-refusal-') as tmp:
        root = Path(tmp)/'tree'
        packet = root/HERE.name
        shutil.copytree(HERE, packet, ignore=shutil.ignore_patterns('__pycache__'))
        for sub in ['annular-scalar-route', 'height-transfer-and-prime-squares']:
            (root/sub).mkdir()
            shutil.copy2(parent_root/sub/'PROOF.md', root/sub/'PROOF.md')
        result = packet/'result.json'
        data = json.loads(result.read_text())
        expected = 'RESULT_MISMATCH'
        if name == 'rh_flag': data['scope']['rh_proved'] = True
        elif name == 'claimed_native_sign': data['scope']['native_unbounded_sign_proved'] = True
        elif name == 'fake_parameter_certificate': data['global_parameter_certificate'] = {'eta':'1/3','tau':'1'}
        elif name == 'boolean_count': data['groups']['native_identity_separation'] = True
        elif name == 'missing_scope': data['scope'] = {}
        elif name == 'duplicate_json_key':
            result.write_text('{"schema":"duplicate",'+result.read_text()[1:])
            expected = 'DUPLICATE_JSON_KEY'
        elif name == 'changed_proof':
            with (packet/'PROOF.md').open('a') as out: out.write('\nCORRUPTED\n')
            expected = 'MANIFEST_HASH:PROOF.md'
        elif name == 'missing_lock':
            (packet/'SOURCE_LOCK.json').unlink()
            expected = 'DELIVERY_COVERAGE'
        elif name == 'wrong_parent_head':
            lock=json.loads((packet/'SOURCE_LOCK.json').read_text())
            lock['parent_head']='0'*40
            (packet/'SOURCE_LOCK.json').write_text(json.dumps(lock))
            expected = 'SOURCE_HEAD'
        elif name == 'changed_parent_proof':
            with (root/'annular-scalar-route/PROOF.md').open('a') as out: out.write('\nCHANGED PARENT\n')
            expected = 'PARENT_BLOB:'
        else: raise RuntimeError(name)
        if name in CASES[:5]: result.write_text(json.dumps(data))
        if name not in ['changed_proof','missing_lock','changed_parent_proof']: reseal(packet)
        command=[sys.executable,'-B']+(['-O'] if optimized else [])+[str(packet/'verify.py'),'--check',str(result)]
        proc=subprocess.run(command, capture_output=True, text=True, timeout=20)
        if proc.returncode!=2 or expected not in proc.stderr:
            raise RuntimeError({'case':name,'returncode':proc.returncode,'expected':expected,'stderr':proc.stderr[-2000:]})
        return {'case':name,'target_optimized':optimized,'returncode':proc.returncode,'expected_error':expected}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--optimized',action='store_true')
    parser.add_argument('--parent-root',type=Path,default=HERE.parent)
    args=parser.parse_args()
    rows=[run_case(c,args.optimized,args.parent_root) for c in CASES]
    print(json.dumps({'status':'PASS_INTENDED_REJECTIONS','cases':rows,'count':len(rows)},indent=2,sort_keys=True))

if __name__=='__main__':main()

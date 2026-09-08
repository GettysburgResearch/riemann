#!/usr/bin/env python3
"""Actual-CLI pristine/rejection controls for the reviewer replay boundary.

Run normally and with -O. The retained result omits interpreter mode so both
complete test outputs can be compared byte-for-byte. Every pristine control
recomputes its full numerical result; malformed receipts may reject early.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
PREFIX=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])

def need(ok,msg):
    if not ok:raise ValueError(msg)

def run():
    rows=[]
    def invoke(packet,receipt,source_root=None,expect=2,name=''):
        cmd=PREFIX+[str(ROOT/'replay.py'),'--packet',packet,'--expect',str(receipt)]
        if source_root is not None:cmd+=['--source-root',str(source_root)]
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=75)
        need(r.returncode==expect,'unexpected CLI result: '+name+' '+r.stderr)
        rows.append({'case':name,'packet':packet,'returncode':r.returncode,
                     'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),
                     'stderr':r.stderr})
    for packet in ('FR','CD','MW','SSQ'):
        invoke(packet,ROOT/f'evidence/{packet.lower()}-normal.json',expect=0,name='pristine_full_'+packet)
    with tempfile.TemporaryDirectory() as temp:
        d=Path(temp);raw=(ROOT/'evidence/mw-normal.json').read_text();base=json.loads(raw)
        def altered(name,mutate):
            obj=json.loads(raw);mutate(obj)
            p=d/(name+'.json');p.write_text(json.dumps(obj,sort_keys=True,indent=2)+'\n')
            invoke('MW',p,name=name)
        altered('float_event_count',lambda x:x.__setitem__('integer_events',65536.0))
        altered('boolean_checkpoint',lambda x:x['checkpoints'].__setitem__(0,True))
        altered('missing_checkpoint',lambda x:x['results'].pop())
        altered('changed_numeric_endpoint',lambda x:x['results'][-1]['J'].__setitem__('hi',str(int(x['results'][-1]['J']['hi'])+1)))
        altered('false_RH_status',lambda x:x.__setitem__('rh_proved',True))
        altered('extra_key',lambda x:x.__setitem__('unpriced_tail',False))
        texts={
            'duplicate_last_wins':raw.replace('"integer_events": 65536,','"integer_events": 1,\n  "integer_events": 65536,'),
            'nonfinite_json':raw.replace('"integer_events": 65536,','"integer_events": NaN,'),
            'empty_object':'{}',
            'truncated_json':'{"integer_events":',
            'nonobject':'[]',
        }
        for name,text in texts.items():
            p=d/(name+'.json');p.write_text(text);invoke('MW',p,name=name)
        alias=d/'receipt-alias.json';alias.symlink_to(ROOT/'evidence/mw-normal.json')
        invoke('MW',alias,name='symlink_receipt')
        huge=d/'oversized.json';huge.write_bytes(b' '*1048577)
        invoke('MW',huge,name='oversized_receipt')
        # Each source mutation is tested through the actual authenticated CLI.
        for name in ('changed_source','missing_source','extra_source','source_symlink','root_symlink'):
            p=d/name;shutil.copytree(ROOT/'sources',p)
            if name=='changed_source':
                (p/'MW/certify.py').write_text("raise RuntimeError('must not execute')\n")
            elif name=='missing_source':(p/'MW/certify.py').unlink()
            elif name=='extra_source':(p/'MW/extra.py').write_text('pass\n')
            elif name=='source_symlink':
                (p/'MW/certify.py').unlink();(p/'MW/certify.py').symlink_to(ROOT/'sources/MW/certify.py')
            else:
                q=d/'linked-root';q.symlink_to(p,target_is_directory=True);p=q
            invoke('MW',ROOT/'evidence/mw-normal.json',source_root=p,name=name)
    return {'schema':'riemann-final-review-replay-cli-tests-v1','pristine_full_replays':4,
            'actual_refusals':len(rows)-4,'skips':0,
            'scope':'Malformed/type-aliased/hash-mismatched receipts and altered source inventories are rejected. Four pristine paths execute complete producer reconstruction.',
            'rows':rows}

if __name__=='__main__':print(json.dumps(run(),sort_keys=True,indent=2)+'\n',end='')

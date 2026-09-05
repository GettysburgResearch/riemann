#!/usr/bin/env python3
"""Run the unmodified manifest-closure CLI on deterministic local Git fixtures.

This tests the scanner's contract, not the actual 37-root scientific graph.
All writes are to a temporary, remote-less repository; no GitHub action is run.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'references'/'sixhour_complete_source_closure.py'
BLOB = '106e1a300872c78659ba2796b7fb98e08df84ef7'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(command: list[str], root: Path, env: dict[str,str], check: bool=True) -> subprocess.CompletedProcess:
    result = subprocess.run(command,cwd=root,env=env,text=True,capture_output=True,timeout=15)
    if check and result.returncode != 0:
        raise ValueError('fixture command failed: '+result.stderr[-500:])
    return result


def build() -> dict:
    raw=SOURCE.read_bytes()
    actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    need(actual==BLOB,'source authentication failed')
    rows=[]
    names=['valid_explicit','valid_inherited','bad_blob','bad_hash','missing_target',
           'duplicate_key','float_primitive','unknown_implicit','zero_roots',
           'empty_bindings','unrecognized_seal_key']
    expected_accept={'valid_explicit':1,'valid_inherited':1,'zero_roots':0,
                     'empty_bindings':0,'unrecognized_seal_key':0}
    for name in names:
        with tempfile.TemporaryDirectory(prefix='C3-manifest-') as d:
            root=Path(d)
            env={'PATH':os.defpath,'LANG':'C.UTF-8','HOME':d,'GIT_CONFIG_NOSYSTEM':'1',
                 'GIT_CONFIG_GLOBAL':os.devnull,'GIT_AUTHOR_NAME':'C synthetic fixture',
                 'GIT_COMMITTER_NAME':'C synthetic fixture','GIT_AUTHOR_EMAIL':'fixture@example.invalid',
                 'GIT_COMMITTER_EMAIL':'fixture@example.invalid','GIT_AUTHOR_DATE':'2000-01-01T00:00:00Z',
                 'GIT_COMMITTER_DATE':'2000-01-01T00:00:00Z'}
            def git(*args: str) -> str:
                return run(['git','-c','core.hooksPath=/dev/null',*args],root,env).stdout.strip()
            git('init','-q','--initial-branch=fixture')
            script=root/'research'/'exploratory'/'closure.py'
            script.parent.mkdir(parents=True)
            script.write_bytes(raw)
            target=root/'arithmetic.txt'; target.write_text('1 + 1 = 2\n',encoding='utf-8')
            git('add','--','research/exploratory/closure.py','arithmetic.txt')
            git('commit','-q','--no-gpg-sign','-m','deterministic base')
            base=git('rev-parse','HEAD')
            target_blob=git('rev-parse',base+':arithmetic.txt')
            row={'path':'arithmetic.txt','commit':base,'git_blob':target_blob,'sha256_lf':sha(target.read_bytes())}
            doc={'schema':'audit-explicit-v1','sources':[row]}
            text=None
            if name=='valid_inherited':
                row.pop('commit');doc['schema']='riemann.atlas.generalized.audit';doc['base_commit']=base
            elif name=='bad_blob': row['git_blob']='0'*40
            elif name=='bad_hash': row['sha256_lf']='0'*64
            elif name=='missing_target': row['path']='absent.txt'
            elif name=='duplicate_key': text='{"schema":"x","schema":"y"}\n'
            elif name=='float_primitive': doc['unrelated_number']=1.0
            elif name=='unknown_implicit': row.pop('commit');doc['base_commit']=base
            elif name=='empty_bindings': doc={'schema':'riemann.atlas.generalized.audit','base_commit':base,'sources':[]}
            elif name=='unrecognized_seal_key':
                doc={'schema':'riemann.atlas.generalized.audit','base_commit':base,
                     'sources':[{'path':'absent.txt','sha256':'0'*64}]}
            if name=='zero_roots':
                (root/'README.md').write_text('No manifest root.\n',encoding='utf-8')
                git('add','--','README.md')
            else:
                (root/'packet.sources.json').write_text(text or json.dumps(doc,sort_keys=True)+'\n',encoding='utf-8')
                git('add','--','packet.sources.json')
            git('commit','-q','--no-gpg-sign','-m',name)
            head=git('rev-parse','HEAD')
            outputs=[]
            roundtrips=[]
            for optimized in (False,True):
                command=[sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])+[str(script),
                         '--head',head,'--base',base,'--programme','G']
                result=run(command,root,env,check=False)
                accepted=result.returncode==0
                need(accepted==(name in expected_accept),'unexpected accept/reject for '+name)
                if accepted:
                    payload=json.loads(result.stdout)
                    need(payload['counts']['edges']==expected_accept[name],'unexpected edge census')
                    need(payload['all_local_objects_present'] is True and payload['all_declared_seals_match'] is True,
                         'declared flags changed')
                    receipt=root/'receipt.json';receipt.write_text(result.stdout,encoding='utf-8')
                    again=run(command+['--check-report',str(receipt)],root,env)
                    check=json.loads(again.stdout)
                    need(check['status']=='PASS','check-report did not accept its generated report')
                    roundtrips.append(True)
                    outputs.append({'accepted':True,'counts':payload['counts'],
                                    'payload_sha256':payload['payload_sha256'],
                                    'all_local_objects_present':payload['all_local_objects_present'],
                                    'all_declared_seals_match':payload['all_declared_seals_match']})
                else:
                    # Keep only the stable final exception, not temporary absolute paths.
                    outputs.append({'accepted':False,'final_exception':result.stderr.strip().splitlines()[-1].split('Command ')[0]})
            need(outputs[0]==outputs[1],'ordinary and optimized results differ: '+name)
            rows.append({'case':name,'base':base,'head':head,'modes':['normal','optimized'],
                         'result':outputs[0],'roundtrip_PASS_modes':len(roundtrips)})
    return {'schema':'C3-manifest-contract-replay-v1','status':'PASS_CONTRACT_BOUNDARY_REPRODUCTION',
            'source_git_blob':BLOB,'source_sha256':sha(raw),'fixture_cases':len(rows),'cli_mode_runs':2*len(rows),
            'roundtrip_mode_runs':sum(r['roundtrip_PASS_modes'] for r in rows),'cases':rows,
            'interpretation':'Recognized-binding integrity is not root/schema completeness. Empty closures can be valid vacuous reports.',
            'actual_scientific_graph_replayed':False,'earlier_expected_count_regressions_refuted':False,
            'source_authentication_does_not_authenticate_mathematics':True,'RH_proved':False}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    args=ap.parse_args();text=json.dumps(build(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')


if __name__=='__main__': main()

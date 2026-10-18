#!/usr/bin/env python3
"""Authenticate the complete packet and optionally replay every accepting check.

No report supplies a mathematical input to an accepting calculation. The
independent checks recompute their results and compare exact stored receipts.
Component runners execute their own normal/optimized and corruption processes.
"""
from concurrent.futures import ThreadPoolExecutor
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent

def need(ok, message):
    if not ok:
        raise RuntimeError(message)

def read_json(path):
    def pairs(items):
        out = {}
        for key,value in items:
            need(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=pairs)

def manifest_check():
    data = read_json(HERE/'MANIFEST.json')
    need(data['schema'] == 'theta20-native-signed.manifest.v1', 'manifest schema')
    entries = data['files']
    names = [entry['path'] for entry in entries]
    need(len(set(names)) == len(names), 'duplicate manifest path')
    actual = sorted(p.relative_to(HERE).as_posix() for p in HERE.rglob('*')
                    if p.is_file() and '__pycache__' not in p.parts
                    and p.relative_to(HERE).as_posix() != 'MANIFEST.json')
    need(sorted(names) == actual, 'complete payload inventory')
    for entry in entries:
        path = Path(entry['path'])
        need(not path.is_absolute() and '..' not in path.parts, 'relative payload path')
        raw = (HERE/path).read_bytes()
        need(len(raw) == entry['bytes'], 'byte count: '+str(path))
        need(hashlib.sha256(raw).hexdigest() == entry['sha256'], 'SHA256: '+str(path))
        git_blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        need(git_blob == entry['git_blob'], 'Git blob: '+str(path))
    return {'manifest_sha256':hashlib.sha256((HERE/'MANIFEST.json').read_bytes()).hexdigest(),
            'manifested_payloads':len(entries),
            'files_including_manifest':len(entries)+1,
            'bytes_including_manifest':sum(x['bytes'] for x in entries)+(HERE/'MANIFEST.json').stat().st_size}

def process(arguments, directory=HERE):
    return subprocess.run([sys.executable,'-B',*arguments], cwd=directory,
                          capture_output=True,text=True)

def component(name):
    print('REPLAY '+name, file=sys.stderr, flush=True)
    proc = process(['replay.py'], HERE/name)
    need(proc.returncode == 0, name+' replay failed:\n'+proc.stdout+proc.stderr)
    return {'component':name,'exit_code':proc.returncode,
            'stdout_sha256':hashlib.sha256(proc.stdout.encode()).hexdigest()}

def independent(script, report):
    print('REPLAY '+script, file=sys.stderr, flush=True)
    ordinary = process(['root/'+script])
    optimized = process(['-O','root/'+script])
    need(ordinary.returncode == 0, script+' ordinary:\n'+ordinary.stderr)
    need(optimized.returncode == 0, script+' optimized:\n'+optimized.stderr)
    need(ordinary.stdout == optimized.stdout, script+' mode mismatch')
    need(ordinary.stdout == (HERE/'root'/report).read_text(), script+' receipt mismatch')
    return {'script':script,'normal_optimized_identical':True,
            'report_sha256':hashlib.sha256(ordinary.stdout.encode()).hexdigest()}

def independent_corruptions():
    results = []
    for mutation,gate in [('permute_derivative','independent complete Jacobian'),
                          ('erase_hub','independent full graph moment map')]:
        proc = process(['-O','root/check_theta_product_independent.py','--mutation',mutation])
        need(proc.returncode != 0, 'accepted independent corruption: '+mutation)
        need(gate in proc.stderr, 'wrong independent corruption gate: '+mutation)
        results.append({'mutation':mutation,'exit_code':proc.returncode,
                        'expected_gate':gate,'rejected':True})
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--replay',action='store_true')
    args = parser.parse_args()
    before = manifest_check()
    result = {'status':'MANIFEST_PASS',**before,'replayed':False}
    if args.replay:
        # Independent components own disjoint directories. Each runner executes
        # its dependent stages sequentially; all futures are awaited and checked.
        with ThreadPoolExecutor(max_workers=3) as pool:
            futures = [pool.submit(component,name) for name in ('critical','native','theta')]
            stages = [future.result() for future in futures]
        checks = [independent('check_divisibility_independent.py','DIVISIBILITY_INDEPENDENT.json'),
                  independent('check_theta_product_independent.py','THETA_PRODUCT_INDEPENDENT.json')]
        mutations = independent_corruptions()
        need(manifest_check() == before, 'payload changed during full replay')
        result.update(status='FULL_REPLAY_PASS',replayed=True,components=stages,
                      independent_checks=checks,
                      independent_optimized_corruptions=mutations,
                      component_corruptions={'critical':3,'native':9,'theta':4},
                      total_separately_executed_optimized_corruptions=18)
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()

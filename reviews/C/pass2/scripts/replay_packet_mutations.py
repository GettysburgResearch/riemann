#!/usr/bin/env python3
"""Synthetic faults in authenticated copies, never edits upstream source."""
from __future__ import annotations
import hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def main():
    cases=[]
    specs=[
      ('wrong_owner_telescope','pr599','121a2767b0e9fe8ed0d76d6146f11807b9a4b587','return current-debt','return current+debt'),
      ('wrong_product_boundary','pr599','121a2767b0e9fe8ed0d76d6146f11807b9a4b587','return main,bulk,boundary','return main+1,bulk,boundary'),
      ('invalid_negative_threshold','pr568_current','f0e8f85e195162d745477cfb69e68b9b24443289','threshold = Decimal("-62.7181678185658877324")','threshold = Decimal("-100")'),
    ]
    for name, target, sha, before, after in specs:
        raw=(ROOT/'replay/references'/target/'verify.py').read_bytes()
        if blob(raw)!=sha: raise ValueError('source hash mismatch')
        text=raw.decode()
        if text.count(before)!=1: raise ValueError('mutation must have one exact site')
        mutant=text.replace(before,after).encode()
        for opt in (False,True):
            with tempfile.TemporaryDirectory(prefix='review-c-mutant-') as tmp:
                p=Path(tmp);(p/'verify.py').write_bytes(mutant)
                cmd=[sys.executable,'-I']+(['-O'] if opt else [])+['verify.py']
                proc=subprocess.run(cmd,cwd=p,env={'PATH':os.defpath,'LC_ALL':'C.UTF-8'},text=True,capture_output=True,timeout=5)
                out=p/'results/verification.json'
                result=json.loads(out.read_text()) if out.exists() else {}
                emitted=proc.returncode==0 and result.get('verdict','').startswith('PASS_')
                if emitted!=opt: raise ValueError('unexpected mutant outcome '+name)
                cases.append({'case':name,'source_git_blob':sha,'mutant_sha256':hashlib.sha256(mutant).hexdigest(),
                              'before':before,'after':after,'optimized':opt,'returncode':proc.returncode,
                              'emitted_PASS':emitted,'stdout':proc.stdout,'stderr':proc.stderr,
                              'command':['python','-I']+(['-O'] if opt else [])+['verify.py'],
                              'stderr_classification':'AssertionError' if 'AssertionError' in proc.stderr else proc.stderr,
                              'telescope_values_equal':result.get('toy_full_euler')==result.get('toy_largest_prime_telescope') if target=='pr599' and result else None})
    report={'synthetic_mutations':3,'subprocesses':6,'cases':cases,
            'classification':'synthetic producer guard bypass under optimization; not a deployed pipeline exploit',
            'unmodified_target_sources_preserved':True,'rh_established':False}
    (ROOT/'reports/packet_mutations.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'synthetic_mutations':3,'normal_rejections':3,'optimized_PASS_emissions':3,'deployed_pipeline_bypass_claimed':False}))
if __name__=='__main__': main()

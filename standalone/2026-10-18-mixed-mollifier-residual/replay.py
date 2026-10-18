#!/usr/bin/env python3
"""Replay exact diagnostics and byte manifests. This is not a proof assistant."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
MUTANTS={
 'pointwise_mollifier':'three_quarters_exact',
 'floor_order':'nearline_ceiling',
 'erase_masks':'literal_nonunit_zero',
 'same_character_dual':'mixed_character_ratio_identity',
 'extra_coprimality':'power_removal_shared_primes',
 'retain_unit_error':'full_flat_convolution',
 'replace_negative_conductor':'negative_conductor_identity',
 'principal_in_dual':'principal_polar_term_separate',
 'omit_fourth_moment':'mixed_holder_fourth_factor',
 'delete_zero_member':'zero_member_cost_not_deleted',
}

def main()->None:
    manifest=ROOT/'MANIFEST.json'
    if manifest.exists():
        for name,item in json.loads(manifest.read_text())['files'].items():
            data=(ROOT/name).read_bytes()
            if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
                raise RuntimeError('payload mismatch: '+name)
    expected=(ROOT/'CHECKS.json').read_bytes()
    for flags in ([],['-O']):
        result=subprocess.run([sys.executable,*flags,str(ROOT/'verify.py')],capture_output=True,timeout=45)
        if result.returncode or result.stdout!=expected:
            raise RuntimeError('accepting replay failed: '+str(flags))
    record=[]
    for mutation,gate in MUTANTS.items():
        result=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py'),'--mutate',mutation],capture_output=True,timeout=45)
        marker='failed gate: '+gate
        if result.returncode==0 or marker not in result.stderr.decode():
            raise RuntimeError('mutation not rejected at intended gate: '+mutation)
        record.append({'mutation':mutation,'rejected':True,'gate':gate})
    archived=ROOT/'MUTATIONS.json'
    payload=(json.dumps(record,indent=2,sort_keys=True)+'\n').encode()
    if archived.exists() and archived.read_bytes()!=payload:
        raise RuntimeError('mutation report changed')
    if not archived.exists(): archived.write_bytes(payload)
    print('PASS: 2 exact replays; 10 executed negative controls; existing manifest checked.')

if __name__=='__main__': main()

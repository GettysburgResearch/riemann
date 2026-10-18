"""Authenticate this packet, replay finite checks, and execute corruption controls."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
CASES={
 'inert_norm':'all_ideal_HNF_norm_fibers',
 'shared_radical':'complete_critical_weighted_Gram',
 'erase_mask':'complete_native_mask_convolution',
 'wrong_inverse':'complete_limit_inverse',
 'drop_powers':'complete_native_mask_convolution',
 'wrong_population':'complete_limit_inverse',
 'drop_horizon':'finite_horizon_tail_retained',
}

def main():
    if len(sys.argv)>1:raise ValueError('No arguments supported.')
    man=json.loads((HERE/'MANIFEST.json').read_text())
    expected=set(man)|{'MANIFEST.json'}
    actual={p.name for p in HERE.iterdir() if p.is_file()}
    if actual!=expected:raise ValueError('Unexpected or missing packet files.')
    for n,entry in man.items():
        raw=(HERE/n).read_bytes()
        if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
            raise ValueError('Manifest mismatch: '+n)
    for opts in [[],['-O']]:
        raw=subprocess.check_output([sys.executable,'-B',*opts,str(HERE/'verify.py')],cwd=HERE,timeout=35)
        if raw!=(HERE/'CHECKS.json').read_bytes():raise ValueError('Checker report mismatch.')
    records=[]
    for mut,gate in CASES.items():
        p=subprocess.run([sys.executable,'-B','-O',str(HERE/'verify.py'),'--mutate',mut],cwd=HERE,capture_output=True,timeout=35)
        if not p.returncode or ('ValueError: '+gate).encode() not in p.stderr:
            raise ValueError('Mutation did not fail at expected gate: '+mut)
        records.append({'mutation':mut,'rejected_at':gate,'returncode':p.returncode})
    if records!=json.loads((HERE/'MUTATIONS.json').read_text()):raise ValueError('Mutation receipt mismatch.')
    print(json.dumps({'status':'PASS','manifested_files':len(man),'modes':['normal','optimized'],
     'separately_executed_mutations':len(records),'scope':'finite algebra and bytes, not analytic verification','rh_proved':False},sort_keys=True))
if __name__=='__main__':main()

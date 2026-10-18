"""Run actual corrupted checker processes; no precomputed verdict is accepted."""
import json
from pathlib import Path
import subprocess
import sys

CASES = {
 'dual_sign':'actual_conductor_dual',
 'large_cap':'bad_capped_mass',
 'equality_diagonal':'finite_field_root_and_zero_moment',
 'replace_omega':'finite_field_root_and_zero_moment',
 'no_unit_subtraction':'literal_flat_cutoff_highpass',
 'impose_coprimality':'false_coprimality_gate',
 'erase_mask':'power_removal_nonunit_mask',
 'collapse_conjugates':'split_conjugates_must_not_collapse',
}

def main():
    here=Path(__file__).resolve().parent
    result={}
    for mutation,gate in CASES.items():
        p=subprocess.run([sys.executable,'-O','verify.py','--mutate',mutation],cwd=here,capture_output=True,text=True,timeout=40)
        if p.returncode==0 or 'FAILED: '+gate not in p.stderr:
            raise ValueError('Mutation did not fail at intended gate: '+mutation+'\n'+p.stderr)
        result[mutation]={'returncode':p.returncode,'rejected_at':gate}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()

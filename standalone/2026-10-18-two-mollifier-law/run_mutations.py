#!/usr/bin/env python3
"""Run separately corrupted finite checkers; not mathematical refereeing."""
import json
from pathlib import Path
import subprocess
import sys

CASES={
 'erase_zero_cap':'zero_receives_cap',
 'omit_bad_cap_cost':'explicit_large_cap_error',
 'unsquared_cauchy_gain':'cauchy_half_saving',
 'use_short_for_bad_count':'long_and_short_roles',
 'cap_inactive_on_good':'cap_can_be_active_on_good_row',
 'wrong_nfree_probability':'nfree_local_probability',
 'drop_sextic_aliases':'complete_cyclotomic_euler_moment',
 'lost_zero_multiplicity':'vertical_monomial_full_tail',
}

def main():
    here=Path(__file__).resolve().parent
    rows=[]
    for mutation,gate in CASES.items():
        result=subprocess.run([sys.executable,'-O',str(here/'verify.py'),
                 '--mutation',mutation],capture_output=True,text=True,timeout=30)
        if result.returncode==0 or result.stderr.strip()!='REJECT:'+gate:
            raise RuntimeError('Unexpected mutation outcome: '+mutation+' '+result.stderr)
        rows.append({'mutation':mutation,'rejected_at':gate,'returncode':result.returncode})
    print(json.dumps({'separate_optimized_processes':len(rows),'results':rows},indent=2,sort_keys=True))

if __name__=='__main__': main()

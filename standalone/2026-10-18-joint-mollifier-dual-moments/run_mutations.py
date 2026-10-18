#!/usr/bin/env python3
"""Execute corrupted optimized checkers; no analytic certification is implied."""
import json
from pathlib import Path
import subprocess
import sys

CASES={
 'erased_mask':'literal_nonunit_zero',
 'same_character_dual':'dual_conjugation',
 'false_shared_coprimality':'shared_power_mask',
 'wrong_cutoff_dilation':'complete_cutoff_convolution',
 'pointwise_mollifier':'joint_dual_budget',
 'lost_actual_conductor':'actual_conductor_cancellation',
 'erased_zero_cap':'actual_zero_keeps_cap',
}

def main():
    here=Path(__file__).resolve().parent
    results=[]
    for name,gate in CASES.items():
        run=subprocess.run([sys.executable,'-O',str(here/'verify.py'),'--mutation',name],text=True,capture_output=True,timeout=25)
        if run.returncode==0 or run.stderr.strip()!='REJECT:'+gate:
            raise RuntimeError('Unexpected result: '+name+' '+run.stderr)
        results.append({'mutation':name,'returncode':run.returncode,'rejected_at':gate})
    print(json.dumps({'executed_separate_processes':len(results),'results':results},indent=2,sort_keys=True))

if __name__=='__main__':main()

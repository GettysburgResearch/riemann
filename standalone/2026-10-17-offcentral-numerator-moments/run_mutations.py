#!/usr/bin/env python3
"""Execute deliberately corrupted finite models; require their specific failures."""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path
EXPECTED={
 'wrong_dual_weight':'afe_dual:2_2',
 'erase_mask':'column_mask:sixth_power_identity',
 'impose_coprimality':'column_factor:retain_shared_prime',
 'fourth_to_second':'class_budget:middle_0',
 'eighth_to_second':'class_budget:middle_2',
 'wrong_lower_count':'partition:lower_count',
 'old_small_line':'small_budget:separate_line',
 'drop_diagonal':'theta:diagonal_retained',
 'zero_tail_gap':'large_tail:positive_gap',
 'old_mellin_shift':'mellin:new_shift'}

def main():
    report=[]
    for name,gate in EXPECTED.items():
        p=subprocess.run([sys.executable,'-O','verify.py','--mutation',name],
                         cwd=Path(__file__).resolve().parent,text=True,
                         capture_output=True,timeout=30)
        if p.returncode==0 or ('ValueError: '+gate) not in p.stderr:
            raise RuntimeError(f'{name}: did not fail at {gate}: {p.stderr}')
        report.append(dict(mutation=name,returncode=p.returncode,rejected_at=gate))
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__': main()

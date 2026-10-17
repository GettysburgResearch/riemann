#!/usr/bin/env python3
"""Run separate optimized processes with deliberate finite-model defects."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
CASES={
    'full_family':'constant_margins:',
    'lost_dual':'mutation_gate:',
    'upper_count':'lower_count_upper_contour:',
    'omit_class':'coverage:',
    'old_shift':'normalization:',
    'wrong_block_weight':'mutation_gate:',
    'full_mollifier':'mutation_gate:',
    'zero_tail_gap':'large_tail:',
    'erased_mask':'sixth_power_masks:',
}

def main() -> None:
    reports=[]
    for mode,gate in CASES.items():
        run=subprocess.run([sys.executable,'-O',str(ROOT/'verify.py'),'--mutation',mode],
                           cwd=ROOT,capture_output=True,text=True,timeout=40,check=False)
        last=run.stderr.strip().splitlines()[-1] if run.stderr.strip() else ''
        if run.returncode==0 or not last.startswith('ValueError: '+gate):
            raise RuntimeError(f'{mode}: unexpected result {run.returncode}: {last}')
        reports.append({'mutation':mode,'returncode':run.returncode,'failure':last})
    print(json.dumps({'separate_optimized_processes':len(reports),'rejected':reports,
                      'analytic_proof_perturbed':False},indent=2,sort_keys=True))

if __name__=='__main__':
    main()

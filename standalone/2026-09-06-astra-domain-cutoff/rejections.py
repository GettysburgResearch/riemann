#!/usr/bin/env python3
"""Reject altered result records through the actual checker's CLI."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent

def main() -> int:
    baseline=json.loads((ROOT/'checks.normal.json').read_text())
    cases=[]
    x=copy.deepcopy(baseline);x['status']='RH_PROVED';cases.append(('status_promotion',x))
    x=copy.deepcopy(baseline);x['details']['directed_source']['complete_cells']=62;cases.append(('coverage_loss',x))
    x=copy.deepcopy(baseline);x['details']['directed_source']['H_log64']['upper_numerator']='1';cases.append(('false_endpoint',x))
    x=copy.deepcopy(baseline);x['details']['Cauchy_jet_cases']=0;cases.append(('multiplicity_coverage_loss',x))
    report=[]
    with tempfile.TemporaryDirectory() as td:
        for optimized in (False,True):
            for name,data in cases:
                p=Path(td)/'mutated.json';p.write_text(json.dumps(data))
                cmd=[sys.executable]+(['-O'] if optimized else [])+[str(ROOT/'checks.py'),'--check',str(p)]
                r=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
                ok=r.returncode==2 and 'retained record mismatch' in r.stderr
                if not ok:raise RuntimeError((name,r.returncode,r.stderr))
                report.append({'mode':'optimized' if optimized else 'normal','mutation':name,'rejected':True})
    (ROOT/'rejections.json').write_text(json.dumps({'executed':report,'scope':'Strict record replay only; not a proof of the analytic theorems.'},indent=2,sort_keys=True)+'\n')
    return 0

if __name__=='__main__':raise SystemExit(main())

#!/usr/bin/env python3
"""Mutate retained outputs; rerun the actual generating CLI in each case."""
import argparse,copy,json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def run(mode):
    prefix=[sys.executable]+(['-O'] if mode=='optimized' else [])
    jobs=[]
    data=json.loads((ROOT/'checks.normal.json').read_text())
    for name,edit in [
      ('negative_Gram_pivot',lambda x:x['Q_LDL_pivots'].__setitem__(0,'-385/2048')),
      ('missing_check_group',lambda x:x['groups'].pop()),
      ('false_fixture_count',lambda x:x.__setitem__('bounded_cases',0))]:
        o=copy.deepcopy(data);edit(o);jobs.append((name,'checks.py',o))
    cert=json.loads((ROOT/'certificate.normal.json').read_text())
    for name,edit in [
      ('missing_last_checkpoint',lambda x:x['results'].pop()),
      ('false_N3_signed_work',lambda x:x['results'][2]['W'].__setitem__('lo','-1'))]:
        o=copy.deepcopy(cert);edit(o);jobs.append((name,'certify.py',o))
    out=[]
    with tempfile.TemporaryDirectory() as tmp:
        for name,script,data in jobs:
            p=Path(tmp)/(name+'.json');p.write_text(json.dumps(data))
            cp=subprocess.run(prefix+[str(ROOT/script),'--expect',str(p)],capture_output=True,text=True,timeout=35)
            if cp.returncode!=2:raise RuntimeError('mutation was not rejected: '+name)
            out.append({'mutation':name,'script':script,'return_code':cp.returncode,'stderr':cp.stderr.strip()})
    return {'mode':mode,'actual_CLI_refusals':len(out),'results':out}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['normal','optimized'],required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    a.output.write_text(json.dumps(run(a.mode),sort_keys=True,indent=2)+'\n')

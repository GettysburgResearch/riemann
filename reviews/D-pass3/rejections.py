#!/usr/bin/env python3
"""Mutate records through the actual comparator and packages through validate.py."""
import argparse,copy,importlib.util,json,shutil,subprocess,sys,tempfile
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reviewer_d3_checks',ROOT/'checks.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def main():
    expected=mod.run();outs=[]
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        for kind in ['fixture_total','schema','drop_check','change_claimed_precision','change_source_blob','erase_core_counterexample','alter_P61_interval','duplicate_check']:
            x=copy.deepcopy(expected)
            if kind=='fixture_total':x['fixtures']+=1
            elif kind=='schema':x['schema']='wrong'
            elif kind=='drop_check':x['checks'].pop()
            elif kind=='duplicate_check':x['checks'].append(copy.deepcopy(x['checks'][0]))
            else:
                name={'change_claimed_precision':'P61_X184_independent_directed_regeneration',
                      'change_source_blob':'annular_certificate_all_coefficients',
                      'erase_core_counterexample':'annular_core_inequivalence',
                      'alter_P61_interval':'P61_X184_independent_directed_regeneration'}[kind]
                c=next(c for c in x['checks'] if c['name']==name)
                if kind=='change_claimed_precision':c['details']['precision_bits']=1
                elif kind=='change_source_blob':c['details']['source_blob']='0'*40
                elif kind=='erase_core_counterexample':c['details']['m']=17
                else:c['details']['40F-M']=['0','1']
            p=td/'mutated.json';p.write_text(json.dumps(x,sort_keys=True,indent=2)+'\n')
            try:mod.check_saved(p,expected)
            except (ValueError,TypeError,KeyError):outs.append({'mutation':kind,'rejected':True})
            else:raise RuntimeError('accepted mutated result '+kind)
        packages=[]
        for kind in ['modify_report','missing_source_ledger','extra_file','forged_hash']:
            d=td/kind;shutil.copytree(ROOT,d,ignore=shutil.ignore_patterns('__pycache__'))
            if kind=='modify_report':(d/'REPORT.md').write_text('corrupted\n')
            elif kind=='missing_source_ledger':(d/'SOURCES.tsv').unlink()
            elif kind=='extra_file':(d/'UNDECLARED').write_text('extra')
            else:
                s=(d/'SHA256SUMS').read_text();(d/'SHA256SUMS').write_text('0'*64+s[64:])
            cmd=[sys.executable,'-B']+(['-O'] if sys.flags.optimize else [])+[str(d/'validate.py'),'--directory',str(d)]
            p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=20)
            if p.returncode==0:raise RuntimeError('accepted corrupted package '+kind)
            packages.append({'mutation':kind,'rejected':True})
    return {'schema':'reviewer-D-pass3-rejections-v1','result_mutations':outs,'package_mutations':packages,
            'scope':'result parser/comparator and file/package contracts; not mathematical theorem validation'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);a=ap.parse_args()
    text=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    else:print(text,end='')

#!/usr/bin/env python3
"""Execute genuine altered-result and altered-package CLI refusals."""
import argparse,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--optimized',action='store_true');args=ap.parse_args()
    py=[sys.executable,'-I','-S','-B']+(['-O'] if args.optimized else [])
    records=[]
    def run(cmd,want_ok):
        r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        if (r.returncode==0)!=want_ok:raise RuntimeError('unexpected exit: '+r.stderr.decode()[:500])
    run(py+[str(ROOT/'validate.py')],True)
    run(py+[str(ROOT/'check.py'),'--check',str(ROOT/'result.json')],True)
    original=json.loads((ROOT/'result.json').read_text())
    with tempfile.TemporaryDirectory() as d:
        d=Path(d)
        for name in ['rh_flag','prime_count_alias','root_bound','missing_field','duplicate_key','float_alias']:
            r=json.loads(json.dumps(original))
            if name=='rh_flag':r['rh_proved']=True
            elif name=='prime_count_alias':r['prime_count']=True
            elif name=='root_bound':r['actual_root_certificates']['sf']['C_readable_bracket'][0]='1'
            elif name=='missing_field':del r['scope']
            text=json.dumps(r)
            if name=='duplicate_key':text=text[:-1]+',"rh_proved":false}'
            if name=='float_alias':text=text.replace('"prime_count": 55','"prime_count": 55.0')
            p=d/(name+'.json');p.write_text(text)
            run(py+[str(ROOT/'check.py'),'--check',str(p)],False);records.append(name)
        for name in ['changed_proof','extra_file','missing_manifest','symlink_proof']:
            out=d/name;shutil.copytree(ROOT,out)
            if name=='changed_proof':(out/'PROOF.md').write_text((out/'PROOF.md').read_text()+'\nfalse appendix\n')
            elif name=='extra_file':(out/'extra.txt').write_text('not declared')
            elif name=='missing_manifest':(out/'SHA256SUMS').unlink()
            else:
                (out/'PROOF.md').unlink();(out/'PROOF.md').symlink_to(ROOT/'PROOF.md')
            run(py+[str(out/'validate.py')],False);records.append(name)
    print(json.dumps({'mode':'optimized' if args.optimized else 'normal',
                      'pristine_controls':2,'actual_refusals':records},sort_keys=True))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Actual CLI refusal tests. Integrity checks are not mathematical acceptance."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def seal(root):
    files=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS' and p.is_file())
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))

def run(root):
    flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    return subprocess.run([sys.executable,*flags,str(root/'verify.py'),'--check',str(root/'result.json')],
                          capture_output=True,text=True,timeout=40)

def mutate(root,key,value):
    p=root/'result.json';d=json.loads(p.read_text());d[key]=value;p.write_text(json.dumps(d));seal(root)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--part',choices=('1','2'))
    part=parser.parse_args().part
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp)/'packet';shutil.copytree(ROOT,root)
        good=run(root)
        if good.returncode:raise RuntimeError('pristine failed: '+good.stderr)
    names=['false_RH','false_subpower','numeric_alias','altered_minimum','duplicate_JSON',
           'changed_proof','missing_hash','extra_file','wrong_parent']
    if part=='1':names=names[:3]
    elif part=='2':names=names[3:]
    for name in names:
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'packet';shutil.copytree(ROOT,root)
            if name=='false_RH':mutate(root,'RH_proved',True)
            elif name=='false_subpower':mutate(root,'subpower_upper_bound_proved',True)
            elif name=='numeric_alias':mutate(root,'RH_proved',0)
            elif name=='altered_minimum':
                p=root/'result.json';d=json.loads(p.read_text());d['certificates'][0]['full_min_upper']='0.000000000001';p.write_text(json.dumps(d));seal(root)
            elif name=='duplicate_JSON':
                p=root/'result.json';s=p.read_text();p.write_text('{"RH_proved":false,'+s[1:]);seal(root)
            elif name=='changed_proof':
                p=root/'PROOF.md';p.write_text(p.read_text()+'\nmodified\n')
            elif name=='missing_hash':
                p=root/'SHA256SUMS';p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n')
            elif name=='extra_file':(root/'extra.txt').write_text('extra');seal(root)
            elif name=='wrong_parent':
                p=root/'SOURCES.json';d=json.loads(p.read_text());d['parent_head']='0'*40;p.write_text(json.dumps(d));seal(root)
            out=run(root)
            if out.returncode==0:raise RuntimeError('corruption accepted: '+name)
            print('REJECTED',name,flush=True)
    print('PASS',len(names),'refusals; one pristine control; optimized='+str(bool(sys.flags.optimize)))
if __name__=='__main__':main()

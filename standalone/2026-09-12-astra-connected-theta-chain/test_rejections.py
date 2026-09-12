#!/usr/bin/env python3
"""Actual changed-copy CLI tests. Finite checking is not a formal RH proof."""
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def require(x,msg):
    if not x:raise ValueError(msg)

def seal(p):
    names=sorted(x.name for x in p.iterdir() if x.name!='SHA256SUMS')
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256((p/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def run(p):
    flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    return subprocess.run([sys.executable,*flags,str(p/'verify.py'),'--check',str(p/'result.json')],capture_output=True,text=True,timeout=35)

def changed_result(p,fn):
    f=p/'result.json';d=json.loads(f.read_text());fn(d);f.write_text(json.dumps(d,sort_keys=True)+'\n');seal(p)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--part',type=int,choices=[1,2],required=True);a=ap.parse_args()
    names1=['duplicate-json','float-alias','boolean-alias','false-RH','unsealed-proof','extra-file','symlink-proof','resealed-source-drift']
    names2=['resealed-chain-rate','resealed-theta-coefficient','resealed-numerical-endpoint']
    results=[]
    with tempfile.TemporaryDirectory(prefix='ctc-reject-') as td:
        base=Path(td)/'base';shutil.copytree(ROOT,base)
        r=run(base);require(r.returncode==0,'pristine reconstruction failed: '+r.stderr[-1000:])
        for name in names1 if a.part==1 else names2:
            p=Path(td)/name;shutil.copytree(ROOT,p)
            if name=='duplicate-json':
                f=p/'result.json';f.write_text('{"bits":192,'+f.read_text().lstrip()[1:]);seal(p)
            elif name=='float-alias':changed_result(p,lambda d:d.__setitem__('bits',192.0))
            elif name=='boolean-alias':changed_result(p,lambda d:d.__setitem__('bits',True))
            elif name=='false-RH':changed_result(p,lambda d:d.__setitem__('rh_proved',True))
            elif name=='unsealed-proof':
                with (p/'PROOF.md').open('a') as f:f.write('\nChanged proof.\n')
            elif name=='extra-file':(p/'unexpected.txt').write_text('extra')
            elif name=='symlink-proof':
                target=Path(td)/'outside-proof.md';target.write_bytes((p/'PROOF.md').read_bytes())
                (p/'PROOF.md').unlink();(p/'PROOF.md').symlink_to(target)
            elif name=='resealed-source-drift':
                f=p/'SOURCES.json';d=json.loads(f.read_text());d['parent']['head']='0'*40;f.write_text(json.dumps(d));seal(p)
            elif name=='resealed-chain-rate':
                f=p/'verify.py';text=f.read_text();old='s1,s3,s5,l2,l4,l6=state;q=I.rat(1,5)'
                require(text.count(old)==1,'mutation locator');f.write_text(text.replace(old,old.replace('1,5','1,4')));seal(p)
            elif name=='resealed-theta-coefficient':
                f=p/'verify.py';text=f.read_text();old='pref=[4*q*q*x-6*q*y for x,y in zip(e9,e5)]'
                require(text.count(old)==1,'theta locator');f.write_text(text.replace(old,old.replace('4*q*q','5*q*q')));seal(p)
            elif name=='resealed-numerical-endpoint':
                changed_result(p,lambda d:d['standardized_sixth_defect'].__setitem__(0,d['standardized_sixth_defect'][0]+1))
            r=run(p);require(r.returncode!=0,'altered copy accepted: '+name)
            require('ValueError' in r.stderr,'unexpected infrastructure failure: '+name+': '+r.stderr[-1000:])
            results.append({'case':name,'rejected':True,'reason':r.stderr.strip().splitlines()[-1]})
    print(json.dumps({'part':a.part,'optimized':bool(sys.flags.optimize),'pristine_reconstruction':True,'cases':results},sort_keys=True))
if __name__=='__main__':main()

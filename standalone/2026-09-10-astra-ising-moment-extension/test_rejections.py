#!/usr/bin/env python3
"""Run real changed-copy CLI checks, separated from analytic proof claims."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent

def seal(p):
    rows=[]
    for f in sorted(p.iterdir()):
        if f.name=='SHA256SUMS':continue
        rows.append(hashlib.sha256(f.read_bytes()).hexdigest()+'  '+f.name)
    (p/'SHA256SUMS').write_text('\n'.join(rows)+'\n')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--part',type=int,choices=(1,2),required=True)
    ap.add_argument('--optimized',action='store_true');a=ap.parse_args()
    names=(['wrong_status','wrong_weights','duplicate','float','boolean'] if a.part==1 else
           ['density_primitive','compensation_sign','proof_hash','extra','symlink'])
    with tempfile.TemporaryDirectory() as td:
        for name in ['pristine']+names:
            p=Path(td)/name;shutil.copytree(ROOT,p)
            res=p/'result.json'
            if name in ('wrong_status','wrong_weights','float','boolean'):
                d=json.loads(res.read_text())
                if name=='wrong_status':d['rh_proved']=True
                if name=='wrong_weights':d['model']['multiplicities'][0]=255
                if name=='float':d['coverage']['cells']=84.0
                if name=='boolean':d['coverage']['cells']=True
                res.write_text(json.dumps(d));seal(p)
            elif name=='duplicate':
                s=res.read_text();res.write_text('{"schema":"IME26-1",'+s[1:]);seal(p)
            elif name=='density_primitive':
                f=p/'core.py';s=f.read_text();t=s.replace('pref=[4*q*q*x-6*q*y','pref=[5*q*q*x-6*q*y')
                if s==t:raise ValueError('mutation did not change source')
                f.write_text(t);seal(p)
            elif name=='compensation_sign':
                f=p/'verify.py';s=f.read_text();t=s.replace('((-1)**(4-k))','((-1)**(5-k))')
                if s==t:raise ValueError('mutation did not change sign')
                f.write_text(t);seal(p)
            elif name=='proof_hash':(p/'PROOF.md').write_text('altered\n')
            elif name=='extra':(p/'EXTRA').write_text('not in manifest')
            elif name=='symlink':
                f=p/'core.py';f.unlink();f.symlink_to(ROOT/'core.py')
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if a.optimized else [])+[str(p/'verify.py'),'--check',str(res)]
            v=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
            if name=='pristine':
                if v.returncode!=0:raise ValueError('pristine failed: '+v.stderr.decode())
                print('PASS pristine')
            else:
                if v.returncode!=2 or b'REFUSED:' not in v.stderr:raise ValueError('mutation not refused: '+name+' '+v.stderr.decode())
                print('PASS refusal',name)
if __name__=='__main__':main()

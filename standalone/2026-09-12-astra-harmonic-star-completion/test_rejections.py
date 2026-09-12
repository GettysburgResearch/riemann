#!/usr/bin/env python3
"""Execute actual malformed/altered-packet controls, with a pristine replay."""
import hashlib,json,subprocess,sys,tempfile,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def seal(root):
    files=sorted(p for p in root.iterdir() if p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files))


def run(root):
    cmd=[sys.executable,'-I','-S','-B']
    if sys.flags.optimize:cmd+=['-O']
    return subprocess.run(cmd+[str(root/'check.py'),'--check',str(root/'result.json')],capture_output=True)


def main():
    result=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td)
        for kind in ['pristine','false_RH','bool_alias','duplicate','wrong_harmonic','negative_leaf','wrong_seed','proof_edit','extra_file']:
            root=base/kind;shutil.copytree(ROOT,root)
            f=root/'result.json'
            if kind=='false_RH':
                d=json.loads(f.read_text());d['rh_proved']=True;f.write_text(json.dumps(d));seal(root)
            elif kind=='bool_alias':
                d=json.loads(f.read_text());d['rh_proved']=0;f.write_text(json.dumps(d));seal(root)
            elif kind=='duplicate':
                text=f.read_text();f.write_text('{"rh_proved":false,'+text[1:]);seal(root)
            elif kind=='wrong_harmonic':
                p=root/'check.py';s=p.read_text();old='a=F(1,2*n);r=F(7,4*n)'
                if old not in s:raise RuntimeError('mutation anchor missing')
                p.write_text(s.replace(old,'a=F(1,3*n);r=F(7,4*n)',1));seal(root)
            elif kind=='negative_leaf':
                p=root/'check.py';s=p.read_text();old='require(a>0 and 0<=r<1,'
                if old not in s:raise RuntimeError('mutation anchor missing')
                p.write_text(s.replace(old,'require(a>0 and -1<r<1,',1));seal(root)
            elif kind=='wrong_seed':
                p=root/'seed_parameters.json';s=p.read_text();p.write_text(s.replace('256','255',1));seal(root)
            elif kind=='proof_edit':
                p=root/'PROOF.md';p.write_text(p.read_text()+'\nUNSEALED EDIT\n')
            elif kind=='extra_file':(root/'EXTRA').write_text('unexpected')
            process=run(root)
            expected=(kind=='pristine')
            if (process.returncode==0)!=expected:
                raise RuntimeError(kind+' unexpected outcome: '+process.stderr.decode())
            result.append({'case':kind,'accepted':process.returncode==0})
    print(json.dumps({'mode':'optimized' if sys.flags.optimize else 'normal','cases':result},sort_keys=True))

if __name__=='__main__':main()

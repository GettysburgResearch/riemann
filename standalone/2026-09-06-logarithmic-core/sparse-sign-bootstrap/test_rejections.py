#!/usr/bin/env python3
"""Exercise actual command-line refusal paths in the active interpreter mode."""
import hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
CONTEXT=('annular-scalar-route/PROOF.md','height-transfer-and-prime-squares/PROOF.md','prime-curvature-and-failure-count/PROOF.md')

def seal(root):
    paths=sorted(p for p in root.iterdir() if p.is_file() and p.name!='SHA256SUMS')
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in paths))

def run(root):
    flags=['-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    return subprocess.run([sys.executable,*flags,str(root/'verify.py'),'--check',str(root/'result.json')],capture_output=True,text=True,timeout=30)

def main():
    cases=('false_RH','false_power_saving','boolean_count','duplicate_JSON','changed_proof','changed_parent','omitted_manifest_entry','extra_file')
    receipts=[]
    with tempfile.TemporaryDirectory(prefix='ssb-refusal-') as td:
        top=Path(td)
        for name in ('pristine',*cases):
            base=top/name; r=base/'sparse-sign-bootstrap'
            shutil.copytree(ROOT,r)
            for rel in CONTEXT:
                p=base/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT.parent/rel,p)
            if name in ('false_RH','false_power_saving','boolean_count'):
                p=r/'result.json';d=json.loads(p.read_text())
                if name=='false_RH':d['RH_proved']=True
                elif name=='false_power_saving':d['native_power_saving_proved']=True
                else:d['finite_fixture_total']=True
                p.write_text(json.dumps(d,indent=2)+'\n');seal(r)
            elif name=='duplicate_JSON':
                p=r/'result.json';p.write_text(p.read_text().replace('{','{"status":"alias",',1));seal(r)
            elif name=='changed_proof':
                p=r/'PROOF.md';p.write_text(p.read_text()+'\nUnreviewed altered text.\n');seal(r)
            elif name=='changed_parent':
                p=base/CONTEXT[0];p.write_text(p.read_text()+'\nChanged.\n')
            elif name=='omitted_manifest_entry':
                p=r/'SHA256SUMS';p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n')
            elif name=='extra_file':(r/'unexpected.txt').write_text('not allowed\n')
            cp=run(r)
            if name=='pristine':
                if cp.returncode!=0:raise RuntimeError('pristine failed: '+cp.stderr)
            else:
                if cp.returncode==0 or 'REJECT:' not in cp.stderr:raise RuntimeError('unexpected mutation result: '+name+' '+cp.stderr)
            receipts.append({'case':name,'exit_code':cp.returncode,'outcome':'PASS' if name=='pristine' else 'REJECTED','message':cp.stderr.strip()})
    print(json.dumps({'optimized':bool(sys.flags.optimize),'cases':receipts},indent=2))
if __name__=='__main__':main()

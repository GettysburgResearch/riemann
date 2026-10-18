"""Authenticate and replay the full degree20 certificate and finite controls."""
from pathlib import Path
import hashlib,json,subprocess,sys,argparse
ROOT=Path(__file__).resolve().parent

def need(x,message):
    if not x:raise ValueError(message)

def run():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    records=manifest['files']
    for name,rec in records.items():
        need(Path(name).name==name,'plain payload name')
        data=(ROOT/name).read_bytes()
        need(len(data)==rec['bytes'] and hashlib.sha256(data).hexdigest()==rec['sha256'],'manifest identity: '+name)
    outputs={};stages=[]
    for optimized in (False,True):
        for script,receipt in [('certify20.py','certificate20.json'),('check_connected.py','finite_checks20.json')]:
            cmd=[sys.executable]+(['-O'] if optimized else [])+[str(ROOT/script),'--check',str(ROOT/receipt)]
            result=subprocess.run(cmd,capture_output=True,text=True,cwd=ROOT,check=False)
            need(result.returncode==0,'accepting replay failed: '+script+' '+result.stderr)
            if optimized:need(result.stdout==outputs[script],'normal/optimized output differs: '+script)
            else:outputs[script]=result.stdout
            stages.append({'script':script,'optimized':optimized,'returncode':result.returncode,'stdout_sha256':hashlib.sha256(result.stdout.encode()).hexdigest()})
            print('PASS',script,'optimized' if optimized else 'ordinary',flush=True)
    negative=[]
    expected={'erase_hub':'complete seven-spin assembly mismatch','reverse_inner':'complete seven-spin assembly mismatch',
              'reduce_count':'complete seven-spin assembly mismatch','omit_top':'all raw moment orders0through20 required'}
    for mutation,message in expected.items():
        cmd=[sys.executable,'-O',str(ROOT/'check_connected.py'),'--corrupt',mutation]
        result=subprocess.run(cmd,capture_output=True,text=True,cwd=ROOT,check=False)
        need(result.returncode!=0 and message in result.stderr,'corrupt optimized control escaped: '+mutation)
        negative.append({'mutation':mutation,'optimized':True,'returncode':result.returncode,'required_failure':message})
        print('REJECTED',mutation,flush=True)
    return {'status':'T20D_COMPLETE_REPLAY_PASS','payloads_authenticated':len(records),'manifest_sha256':hashlib.sha256((ROOT/'MANIFEST.json').read_bytes()).hexdigest(),
            'accepting_stages':stages,'separately_executed_negative_controls':negative,
            'scope':'complete finite source/root certificate and finite assembly; not RH or an unbounded-order theorem'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);a=p.parse_args();out=run()
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    print(txt,end='')

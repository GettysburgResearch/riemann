"""Byte checks and isolated exact finite replays; not an analytic verifier."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile

root=Path(__file__).resolve().parent
manifest=json.loads((root/'COMPONENT_MANIFEST.json').read_text(encoding='utf-8'))
for item in manifest['components']:
    p=root/item['path']
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:
        raise RuntimeError('component identity mismatch: '+item['path'])
checks=['verify_label_exponents.py','verify_structural_exponents.py',
        'verify_quartic_orientation.py','verify_signed_completion_exponents.py']
results=[]
for checker in checks:
    outputs=[]
    for optimized in (False,True):
        with tempfile.TemporaryDirectory(prefix='riemann-structural-') as tmp:
            p=Path(tmp)/checker
            shutil.copyfile(root/checker,p)
            command=[sys.executable]+(['-O'] if optimized else [])+[str(p)]
            run=subprocess.run(command,cwd=tmp,capture_output=True,text=True,check=True)
            result=json.loads(run.stdout)
            outputs.append(result)
    if outputs[0]!=outputs[1]:raise RuntimeError('normal/optimized mismatch: '+checker)
    results.append({'checker':checker,'normal_equals_optimized':True,'result':outputs[0]})
record={'status':'PASS','manifest_components':len(manifest['components']),
        'scope':'finite algebra only; no analytic theorem or zero-free bound certified',
        'checkers':results}
(root/'REPLAY_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))

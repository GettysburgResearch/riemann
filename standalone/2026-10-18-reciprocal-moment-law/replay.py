"""Authenticate all payloads, rerun both checker modes, and rerun actual mutations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

def main():
    here=Path(__file__).resolve().parent
    manifest=json.loads((here/'MANIFEST.json').read_text())
    for name,expected in manifest.items():
        p=here/name
        if p.parent!=here or not p.is_file(): raise ValueError('Unsafe/missing payload')
        data=p.read_bytes()
        if len(data)!=expected['bytes'] or hashlib.sha256(data).hexdigest()!=expected['sha256']:
            raise ValueError('Payload differs: '+name)
    expected=(here/'CHECKS.json').read_bytes()
    for flags in ([],['-O']):
        got=subprocess.check_output([sys.executable,*flags,'verify.py'],cwd=here,timeout=45)
        if got!=expected: raise ValueError('Checker report differs')
    got=subprocess.check_output([sys.executable,'run_mutations.py'],cwd=here,timeout=120)
    if got!=(here/'MUTATIONS.json').read_bytes(): raise ValueError('Mutation report differs')
    print(json.dumps({'manifested_payloads':len(manifest),'normal_and_optimized':'MATCH','actual_negative_controls':8,'analytic_certification':False},sort_keys=True))

if __name__=='__main__': main()

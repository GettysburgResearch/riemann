#!/usr/bin/env python3
"""Execute corrupted finite models. Success here means every corruption failed."""
from pathlib import Path
import json
import subprocess
import sys
from verify import MUTATIONS
root=Path(__file__).resolve().parent
out=[]
for name in MUTATIONS:
    proc=subprocess.run([sys.executable,'-O',str(root/'verify.py'),'--mutation',name],
                        capture_output=True,text=True,timeout=20)
    if proc.returncode==0:
        raise RuntimeError(f'Corrupted model unexpectedly passed: {name}')
    diagnostic=next((x for x in reversed(proc.stderr.splitlines()) if x.startswith('ValueError:')),None)
    if diagnostic is None:
        raise RuntimeError(f'Unexpected failure rather than a model guard: {name}: {proc.stderr}')
    out.append({'mutation':name,'returncode':proc.returncode,'failure':diagnostic})
print(json.dumps({'status':'ALL_CORRUPTED_MODELS_REJECTED','optimized':True,'results':out},indent=2,sort_keys=True))

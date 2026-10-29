#!/usr/bin/env python3
"""Static source-path audit only; no Lean elaboration or olean validation."""
from pathlib import Path
import re,hashlib
root=Path('/workspace/scratch/chain131-candidate');base=Path('/workspace/scratch/pr94-prepared/submission/src')
qproject=Path('/workspace/scratch/qproject/src')
def locate(mod):
 rel=Path(*mod.split('.')).with_suffix('.lean')
 opts=[]
 if mod.startswith('Candidate.'):opts=[root/'src'/rel]
 elif mod.startswith('Submissions.arvi_density.Return.'):
  opts=[root/'return-overlay'/Path(*mod.split('.')[3:]).with_suffix('.lean'),base/rel,qproject/rel]
 elif mod.startswith('Submissions.arvi_density.ReturnD.'):
  opts=[root/'returnd-overlay'/Path(*mod.split('.')[3:]).with_suffix('.lean'),base/rel,qproject/rel]
 elif mod.startswith('Submissions.'):opts=[base/rel,qproject/rel]
 else:return None
 for p in opts:
  if p.is_file():return p
 raise FileNotFoundError(mod)
files=sorted((root/'src/Candidate/ChainExtension').glob('*.lean'))+sorted((root/'return-overlay').rglob('*.lean'))+sorted((root/'returnd-overlay').rglob('*.lean'))
imports=[]
for f in files:
 for line in f.read_text().splitlines():
  m=re.match(r'^import\s+([A-Za-z0-9_\.]+)',line)
  if not m:continue
  p=locate(m.group(1))
  if p is not None:imports.append((str(f),m.group(1),str(p)))
for f in ('Source/HybridGates.lean','Source/HybridGatesMarked.lean','Cert/Reflect.lean','ChainF50/Chain.lean'):
 a=base/'Submissions/arvi_density'/f;b=qproject/'Submissions/arvi_density'/f
 assert hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest(),f
print('Checked',len(files),'staged source files and',len(imports),'direct staged imports')
print('Candidate.ChainExtension.Wiring resolves to',locate('Candidate.ChainExtension.Wiring'))
print('Return.Endpoint resolves to',locate('Submissions.arvi_density.Return.Endpoint'))
print('Four pinned source modules match qproject by SHA-256')
print('Not checked: imports nested under untouched files, Lean module elaboration, or build artifacts.')

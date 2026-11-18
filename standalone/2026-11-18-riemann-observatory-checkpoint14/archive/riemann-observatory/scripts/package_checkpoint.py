#!/usr/bin/env python3
"""Package current checkpoint without rerendering or changing already delivered PDF bytes."""
import hashlib,json,shutil,zipfile
from pathlib import Path
from distribution_policy import is_distributable
R=Path(__file__).resolve().parents[1]
files=[]
for p in sorted(R.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(R)
 if not is_distributable(rel):continue
 if str(rel)=='quality/distribution_manifest.json':continue
 files.append(p)
payloads={str(p.relative_to(R)):p.read_bytes() for p in files}
manifest={'included_files':len(files)+1,'excluded':['sources/ and raw source staging directories','corpus/raw_discovery/ raw API payload cache','bytecode, build caches and unapproved source PDFs'],'scope':'File-byte checkpoint during active research; hashes describe exact distributed bytes. Original PDF allowlist: scripts/distribution_policy.py.','files':[{'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in payloads.items()]}
manifest_bytes=(json.dumps(manifest,indent=2)+'\n').encode()
(R/'quality/distribution_manifest.json').write_bytes(manifest_bytes)
payloads['quality/distribution_manifest.json']=manifest_bytes
out=R.parent/'riemann-observatory.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,data in payloads.items():z.writestr('riemann-observatory/'+name,data)
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert not any('/sources/' in n or '/raw_discovery/' in n for n in z.namelist())
 assert 'riemann-observatory/final_synthesis/synthesis.pdf' in z.namelist()
 # Original research figures may accompany the original synthesis. Source PDFs
 # are excluded by the directory rule; every remaining PDF needs a known scope.
 assert all(is_distributable(n.removeprefix('riemann-observatory/')) for n in z.namelist())
 for row in manifest['files']:assert hashlib.sha256(z.read('riemann-observatory/'+row['path'])).hexdigest()==row['sha256']
sha=hashlib.sha256(out.read_bytes()).hexdigest();out.with_suffix('.zip.sha256').write_text(sha+'  '+out.name+'\n')
a=R.parent/'artifacts';a.mkdir(exist_ok=True)
for p in [out,out.with_suffix('.zip.sha256'),R/'final_synthesis/synthesis.pdf',R/'final_synthesis/synthesis.html']:shutil.copy2(p,a/p.name)
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'included_files':len(files),'sha256':sha},indent=2))

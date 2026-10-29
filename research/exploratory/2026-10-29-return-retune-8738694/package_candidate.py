"""Create a source manifest and unified patch against the pristine PR94 submission."""
import argparse, difflib, hashlib, json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--pristine-src',required=True);p.add_argument('--candidate-src',required=True);p.add_argument('--out',required=True);a=p.parse_args()
old=Path(a.pristine_src);new=Path(a.candidate_src);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
prefix='submissions/2026-10-29-arvi-density/src/'
changed=[];patch=[]
for f in sorted(new.rglob('*.lean')):
 rel=f.relative_to(new);base=old/rel;after=f.read_bytes();before=base.read_bytes() if base.exists() else None
 if before==after:continue
 path=prefix+str(rel); h=lambda b:hashlib.sha256(b).hexdigest() if b is not None else None
 changed.append({'path':path,'original_sha256':h(before),'candidate_sha256':h(after)})
 patch.extend(difflib.unified_diff(before.decode().splitlines(keepends=True) if before is not None else [],after.decode().splitlines(keepends=True),fromfile='a/'+path if before is not None else '/dev/null',tofile='b/'+path))
assert len(changed)==20,len(changed)
manifest={'status':'experimental, uncompiled','source_repository':'https://github.com/GTimG/QuasiRiemannTracker','source_commit':'e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4','target':'4369347/5000000','files':changed}
(out/'candidate-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(out/'candidate-lean.patch').write_text(''.join(patch))
print('packaged',len(changed),'modules')

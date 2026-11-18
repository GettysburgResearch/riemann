#!/usr/bin/env python3
"""List or restore reversible private compiler setup-cache compression."""
import argparse
import gzip
import hashlib
import json
import shutil
from pathlib import Path

R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--restore',action='store_true',help='Restore missing originals after verifying their gzip and SHA256')
p.add_argument('--prefix',default='',help='Restore only matching archive-relative source paths')
a=p.parse_args()
manifest=R/'sources/cache_maintenance/packed_setup_json.jsonl'
if not manifest.exists():
 p.exit(0,'Private cache manifest is not distributed. This operation applies only to the original research workspace.\n')
rows=[json.loads(x) for x in manifest.read_text().splitlines() if x.strip()]
rows=[x for x in rows if x['path'].startswith(a.prefix)]
pending=[]
for x in rows:
 target=R/x['path'];packed=R/x['packed_path']
 assert target.resolve().is_relative_to(R) and packed.resolve().is_relative_to(R)
 if not target.exists():pending.append(x)
required=sum(x['bytes'] for x in pending)
print(json.dumps({'matched_files':len(rows),'missing_originals':len(pending),'restore_bytes':required,'restoring':a.restore}))
if a.restore:
 if shutil.disk_usage(R).free<required+50_000_000:
  p.exit(1,'Insufficient free space for this selection; use a narrower --prefix.\n')
 for x in pending:
  target=R/x['path'];data=gzip.decompress((R/x['packed_path']).read_bytes())
  assert len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256']
  temporary=target.with_suffix(target.suffix+'.restoring')
  temporary.write_bytes(data);temporary.replace(target)
 print('Restored exact original setup JSON bytes; packed copies remain.')

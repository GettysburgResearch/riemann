"""Authenticate bytes, not mathematical assertions."""
import hashlib
import json
from pathlib import Path

here=Path(__file__).resolve().parent
items=json.loads((here/'MANIFEST.json').read_text())['files']
for name,item in items.items():
    if Path(name).name!=name: raise ValueError('non-flat manifest path')
    data=(here/name).read_bytes()
    if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
        raise ValueError('manifest mismatch: '+name)
print('PASS_MANIFEST',len(items))

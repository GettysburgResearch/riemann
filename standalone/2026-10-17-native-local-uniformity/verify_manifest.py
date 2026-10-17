from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent
m=json.loads((p/'MANIFEST.json').read_text())
for name,expected in m.items():
    data=(p/name).read_bytes()
    got={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
         'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
    if got!=expected:
        raise RuntimeError('Manifest mismatch: '+name)
print('PASS manifest; byte identity only, not theorem validity')

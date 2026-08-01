#!/usr/bin/env python3
from pathlib import Path
import base64, hashlib
root=Path(__file__).resolve().parent
parts=sorted((root/'source_chunks_b64').glob('cpart.*.b64'))
data=b''.join(base64.b64decode(''.join(p.read_text().split())) for p in parts)
expected='be431ad0011bcafa482836cc9116bb82ea5dc926914b2ab642a0eb98678e4afb'
actual=hashlib.sha256(data).hexdigest()
if actual!=expected:
    raise SystemExit(f'materialized source hash mismatch: {actual}')
(root/'directed_producer.c').write_bytes(data)
print(actual)

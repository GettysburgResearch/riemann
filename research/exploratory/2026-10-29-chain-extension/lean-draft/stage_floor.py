#!/usr/bin/env python3
"""Stage the independently developed 1/250 floor patch as an exact snapshot.
This copies source files, not compiled artifacts; no new Lean check is implied.
"""
from pathlib import Path
from hashlib import sha256
from shutil import copyfile
src=Path('/workspace/scratch/retune_project/src/Submissions/arvi_density/ReturnD')
dst=Path('/workspace/scratch/chain131-candidate/returnd-overlay')
expected={
'Transport/Transport/CubeFloorCollected.lean':'c3b4bb57e1f5b10d4235f602f614d4cc95b720902f42550a898e50a07d894b92',
'Transport/Transport/CubeFloorSaving.lean':'38a4e08fe4010e4d5d8c21fa030a064a4b24089be8d3d7fb67b255728df175f1',
'Transport/Transport/FloorExponent.lean':'5fb9b65a7d8d86b8dd17207dc78adb6b729e2f3af1ef085e8e09daaea056cc54',
'Transport/Transport/HighApproximation.lean':'fb841ca0eee438d9769cda80d393d82ec3bfcb2e70e5e933c28f7738527b2581',
'Transport/Transport/NonfloorTransport.lean':'d44de7ade5205fac262d31a34f105527ef76afcc79dacd22a187f800c912946d',
'Transport/Transport/SharedNonfloor.lean':'0959bf5e54b7ad9dada36d98144889bd70a14efbacda672ab82abec0e531a19e',
'Transport/TransportParameters.lean':'f34941798c16e48b49facc6e8ebe3bd393cce1dd71a927af5c1adb96c4af1ba9',
'TransportGeometry.lean':'8764b0ae2b9a05d8c82ed0a04c4878a83d64690b4c73e5a86d62ec8063ef168d'}
for rel,digest in expected.items():
 p=src/rel;assert sha256(p.read_bytes()).hexdigest()==digest,rel
for rel in expected:
 p=dst/rel;p.parent.mkdir(parents=True,exist_ok=True);copyfile(src/rel,p)
print('Staged',len(expected),'hash-matched floor-patch source files to',dst)

#!/usr/bin/env python3
"""Stage uncompiled generated source modules; never overwrite the PR94 checkout."""
from pathlib import Path
from shutil import copyfile
here=Path(__file__).parent
base=Path('/workspace/scratch/chain131-candidate')
modules=base/'src/Candidate/ChainExtension'
rows=base/'return-overlay/Rows'
modules.mkdir(parents=True,exist_ok=True);rows.mkdir(parents=True,exist_ok=True)
for name in ('Low130.lean','Low131.lean','High130.lean','High131.lean','Step_130.lean','Step_131.lean','Main131.lean'):
 copyfile(here/name,modules/name)
copyfile(here/'ChainExtension.lean',modules/'Wiring.lean')
copyfile(here/'Edges131.lean',rows/'Edges131.lean')
copyfile(here/'EdgeCertificates131.lean',base/'return-overlay/EdgeCertificates.lean')
print('Staged eight candidate modules, edge leaves and edge cover; not compiled.')

#!/usr/bin/env python3
from pathlib import Path
import subprocess, json, hashlib
root=Path(__file__).resolve().parents[2]
experiments=[
 ('X-91686-rough-coaction-ownership','PASS_ROUGH_COACTION_ONE_OWNER_LEDGER'),
 ('X-91687-p61-causal-coalesced-hall','PASS_P61_CAUSAL_COALESCED_TARGET_SCORE_HALL'),
 ('X-91688-decomposition-blind-endpoint-bridge','PASS_DECOMPOSITION_BLIND_ENDPOINT_BRIDGE'),
]
for name, verdict in experiments:
 d=root/'experiments'/name
 subprocess.run(['python3','verify.py'],cwd=d,check=True,stdout=subprocess.DEVNULL)
 data=json.loads((d/'results/verification.json').read_text())
 assert data['classification']==verdict
 subprocess.run(['sha256sum','-c','SHA256SUMS'],cwd=d,check=True,stdout=subprocess.DEVNULL)
print('PASS_T91659_THREE_ROUTE_PACKET')

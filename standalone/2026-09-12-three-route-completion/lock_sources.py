"""Bind the exact primary research proofs used by the joint packet.

Requires the recorded historical Git objects locally; a later PR head is not
a replacement for the frozen commit. This is provenance, not proof review.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

BASE='f99d9e3908dde4865377c75d9ca051c1f545bf4f'
SOURCES=[
    (848,'99101457b32b6f10f4eda88ca998048404b860ea','2026-09-12-astra-crossing-cofinal','native crossing energy; complete proof read'),
    (866,'14b20cc85aec1dc1909990d2d8a517740f2dd536','2026-09-12-astra-polynomial-degree-growth','degree-growth trace; complete proof read'),
    (863,'0640c9c59be0bf20c18258460a7517fb09728e82','2026-09-12-astra-interacting-cluster-realization','native degree-14 root premise; complete proof read, primitive integration not replayed'),
    (842,'4558dce9cb981a2e8c0e3e058b21a5b17f6a1cf5','2026-09-12-theta-cumulant-spectral-index','cumulant spectral criterion; complete proof read, theta certificate not replayed'),
    (867,'4c7898432546814812b2be8c72fc199e294354d1','2026-09-12-astra-weight-adapted-star','new during pass: opposite-sign degree-16 seed; complete proof read, root theorem imported'),
    (862,'67d5d6a5f588642f4c451fe35d2369b5ddac9346','2026-09-10-gamma-finite-defect','full defect consumer and budgets; complete proof read'),
    (865,'03cb3cb0b14922b839d0a6a64a59236377b1848d','2026-09-12-positive-gamma-tail-compression','positive compressed source; complete proof read, primitive campaign not replayed'),
    (858,'72ccb357e774db1189e82f4f1b83459f00638c7e','2026-09-10-gamma-endpoint-index','native N5 disk; proof/certificate specification read, defining integral not replayed'),
    (868,'8ae3ea4855fd89882f4b5d782bbd72b721ebf47b','2026-09-12-native-gamma-collision','new during pass: martingale/collision; gamma author read complete proof, local certificate imported'),
]


def reconstruct():
    rows=[]
    for number,commit,folder,scope in SOURCES:
        path='standalone/'+folder+'/PROOF.md'
        data=subprocess.check_output(['git','show',commit+':'+path])
        blob=subprocess.check_output(['git','rev-parse',commit+':'+path],text=True).strip()
        rows.append({'pr':number,'commit':commit,'path':path,'git_blob':blob,
                     'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                     'url':'https://github.com/GettysburgResearch/riemann/blob/'+commit+'/'+path,
                     'reading_and_dependency_scope':scope,
                     'status':'proposed predecessor, not promoted by this packet'})
    return {'main_base':BASE,'review_date':'2026-09-12',
            'scope':'source identity and reading boundaries; no inherited checker acceptance',
            'new_during_pass':[867,868],'sources':rows}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    content=json.dumps(reconstruct(),indent=2)+'\n'
    target=Path(__file__).with_name('SOURCE_LOCK.json')
    if args.write:
        target.write_text(content,encoding='utf-8',newline='\n')
    elif target.read_text(encoding='utf-8')!=content:
        raise ValueError('source lock mismatch')
    print('PASS nine frozen proof identities; no mathematical status promotion')

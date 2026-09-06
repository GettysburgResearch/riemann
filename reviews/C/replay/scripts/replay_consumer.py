#!/usr/bin/env python3
"""Bounded adversarial fixtures for the frozen repository validator; not a proof replay."""
import csv,hashlib,json,pathlib,subprocess,sys,tempfile
root=pathlib.Path(__file__).resolve().parents[1]
src=root/'references/consumer/validate_consumer.py';data=src.read_bytes()
sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
if sha!='950d5f1193724bd975111a1b37d55e19c9270a35':raise SystemExit('wrong source')
ids=['CONSUMER.MELLIN.TWO_ROW','CONSUMER.MELLIN.FIVE_THREE','CONSUMER.MELLIN.SPECIALIZED_LANDAU','API.MELLIN.SUBPOWER_NEGATIVE_MASS','OPEN.ARITH.ROWS23_NATIVE','OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS','OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS']
base=[{'semantic_id':i,'final_verdict':'OPEN_SUFFICIENT_FOR_RH' if i.startswith('OPEN.') else 'VERIFIED','source_head_sha':'0'*40} for i in ids]
edge={'edge_id':'SYNTHETIC_EDGE','conclusion_id':'RH','final_verdict':'CONDITIONAL_EXACT','premise_ids':json.dumps([ids[0],ids[-1]])}
fixtures={
 'minimal_valid_shape':(base,[edge]),
 'empty_census':([],[]),
 'false_verified_open_claims':([{**r,'final_verdict':'VERIFIED'} for r in base],[edge]),
 'duplicate_semantic_id':(base+[base[0].copy()],[edge]),
 'no_open_premise':(base,[{**edge,'premise_ids':json.dumps([ids[0]])}]),
 'malformed_source_identity':([{**r,'source_head_sha':'not-a-git-sha'} for r in base],[edge]),
}
runs=[]
for name,(claims,edges) in fixtures.items():
 for opt in (False,True):
  with tempfile.TemporaryDirectory(prefix='reviewC-consumer-') as td:
   p=pathlib.Path(td);(p/src.name).write_bytes(data)
   for fn,rows,keys in [('CLAIMS.tsv',claims,['semantic_id','final_verdict','source_head_sha']),('EDGES.tsv',edges,['edge_id','conclusion_id','final_verdict','premise_ids'])]:
    with (p/fn).open('w',newline='') as f:
     w=csv.DictWriter(f,fieldnames=keys,delimiter='\t');w.writeheader();w.writerows(rows)
   cmd=[sys.executable]+(['-O'] if opt else [])+[src.name]
   r=subprocess.run(cmd,cwd=p,capture_output=True,text=True,timeout=5,env={'PATH':'/usr/bin:/bin','PYTHONHASHSEED':'0'})
   runs.append({'fixture':name,'optimized':opt,'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'writes_validation_json':(p/'validation.json').exists(),'data_class':'reviewer-created structural/adversarial fixture; not original CLAIMS.tsv'})
for r in runs:
 print(r['fixture'],r['optimized'],r['exit_code'])
(root/'reports/consumer_replay.json').write_text(json.dumps({'source_commit':'8d16f8d9c475db290bc85e53d775b93b9bcdb336','source_path':'canonical/consumers/mellin-landau/validate_consumer.py','source_blob':sha,'runs':runs},indent=2)+'\n')

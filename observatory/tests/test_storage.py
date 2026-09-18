import copy
import hashlib
import json
import math
import shutil
import sqlite3
import subprocess
from decimal import Decimal
import pytest
from artifacts import ArtifactStore, verify_result
from engine import compute
from identity import content_id, result_id, strict_loads
from series_store import SeriesStore


def fixture_result():
    return compute({'module':'cancellation','n':16,'split':7})


def test_identity_survives_browser_number_spelling():
    value={'one':1.0,'minus_zero':-0.0,'decimal':.1,'small':1e-35,'unicode':'ζ','coordinate':'763173730199776587433631628770.000001'}
    if not shutil.which('node'): pytest.skip('Node needed for genuine JavaScript JSON round-trip')
    out=subprocess.check_output(['node','-e','let s="";process.stdin.on("data",x=>s+=x);process.stdin.on("end",()=>console.log(JSON.stringify(JSON.parse(s))));'],input=json.dumps(value).encode())
    assert content_id(value)==content_id(json.loads(out))
    r=fixture_result()
    out=subprocess.check_output(['node','-e','let s="";process.stdin.on("data",x=>s+=x);process.stdin.on("end",()=>console.log(JSON.stringify(JSON.parse(s))));'],input=json.dumps(r).encode())
    assert result_id(json.loads(out))==r['result_id']


@pytest.mark.parametrize('raw',['{"a":1,"a":2}','{"x":NaN}','{"x":Infinity}'])
def test_strict_json(raw):
    with pytest.raises(ValueError): strict_loads(raw)


def test_immutable_both_artifacts_restart_and_refinement(tmp_path):
    a=fixture_result();b=compute({**a['request'],'width':1.2})
    point=compute({'module':'refine','real':'2','imag':'0'})
    request=dict(name='full comparison',notes='keep the cross terms',result=b,comparison=a,refinements=[point],selection={'kind':'term','m':4,'n':7},viewports=[{'id':'prefix','x_range':[2,12]}])
    store=ArtifactStore(tmp_path);receipt=store.save(request)
    assert store.save(request)==receipt
    saved=ArtifactStore(tmp_path).load(receipt['investigation_id'])['experiment']
    assert saved['result']==b and saved['comparison']==a and saved['refinements']==[point]
    assert saved['selection']==request['selection'] and saved['viewports']==request['viewports']
    assert len(store.list())==1


def test_corruption_unknown_schema_and_shape_refused(tmp_path):
    store=ArtifactStore(tmp_path);a=fixture_result();receipt=store.save({'result':a})
    path=store.path(a['result_id']);data=json.loads(path.read_text());data['metrics']['A_energy']+=1;path.write_text(json.dumps(data))
    with pytest.raises(ValueError,match='integrity'): store.load(receipt['investigation_id'])
    with pytest.raises(ValueError,match='corrupted'): store.save({'result':a})
    bad=copy.deepcopy(a);bad['schema_version']=99
    with pytest.raises(ValueError,match='Unknown'): verify_result(bad)
    bad=copy.deepcopy(a);bad['grid']['n']=10000000;bad['result_id']=result_id(bad)
    with pytest.raises(ValueError,match='grid'): verify_result(bad)
    with pytest.raises(ValueError): store.load('../../etc/passwd')


def sample_data(n=8192):
    data={'name':'adversarial','provenance':'synthetic deterministic fixture','anchor':'763173730199776587433631628770',
          'samples':[{'offset':format(Decimal(i)/Decimal(1000000),'f'),'value':None if 1023<=i<1051 else 12345 if i==6003 else (-1)**i} for i in range(n)],
          'events':[{'index':6003,'label':'spike','status':'synthetic'},{'index':1030,'label':'in gap','status':'missing'}]}
    return data


def test_indexed_viewport_spikes_gaps_signed_sums_and_events(tmp_path):
    store=SeriesStore(tmp_path);q=sample_data();info=store.ingest(q);key=info['dataset_id']
    view=store.viewport(key,0,8192,32)
    assert [6003,12345.0] in view['points']
    assert view['gaps']==[[1023,1051]] and [1023,None] in view['points']
    assert len(view['events'])==2 and view['missing_count']==28
    assert view['finite_count']==8192-28
    assert view['signed_sum']==math.fsum(v['value'] for v in q['samples'] if v['value'] is not None)
    assert view['absolute_sum']==sum(abs(v['value']) for v in q['samples'] if v['value'] is not None)
    assert view['raw_rows_read']==0
    assert len(view['points'])<200
    narrow=store.viewport(key,1001,1080,16)
    assert narrow['missing_count']==28 and narrow['raw_rows_read']<79
    assert narrow['gaps']==[[1023,1051]] and len(narrow['events'])==1
    sample=store.sample(key,6003)
    assert sample['exact_decimal']=='763173730199776587433631628770.006003'
    assert SeriesStore(tmp_path).viewport(key,0,8192,32)==view


def test_import_boundaries_and_duplicate_offsets(tmp_path):
    store=SeriesStore(tmp_path);q=sample_data();q['samples'][1]['offset']=q['samples'][0]['offset']
    with pytest.raises(ValueError): store.ingest(q)
    q=sample_data();q['samples'][0]['value']=float('nan')
    with pytest.raises(ValueError): store.ingest(q)
    key=store.ingest(sample_data())['dataset_id']
    for args in [(-1,10,20),(10,9,20),(0,99999,20),(0,100,2)]:
        with pytest.raises(ValueError): store.viewport(key,*args)


@pytest.mark.parametrize('table,sql,args',[
 ('samples','UPDATE samples SET value=888 WHERE i=3',None),
 ('nodes','UPDATE nodes SET payload=? WHERE level=0 AND slot=0',('{"tampered":true}',)),
 ('events','UPDATE events SET payload=? WHERE id=0',('{"tampered":true}',)),
 ('gaps','UPDATE gaps SET hi=1052',None),
 ('meta','UPDATE meta SET payload=?',('{"tampered":true}',)),
])
def test_accessed_storage_corruption(table,sql,args,tmp_path):
    store=SeriesStore(tmp_path);key=store.ingest(sample_data())['dataset_id']
    with sqlite3.connect(store.path(key)) as db: db.execute(sql,args or ())
    with pytest.raises(ValueError):
        if table=='samples': store.sample(key,3)
        elif table=='nodes': store.viewport(key,0,32,8)
        else: store.viewport(key,0,8192,32)


def test_legacy_hash_is_not_silently_repaired():
    old={'schema_version':1,'a':1.0}
    old['result_id']=hashlib.sha256(json.dumps(old,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert result_id(old)==old['result_id']
    old['a']=1
    assert result_id(old)!=old['result_id']

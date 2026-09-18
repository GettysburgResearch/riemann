import time
import pytest
from fastapi.testclient import TestClient
import server

HEADERS={'X-Observatory-Client':'v0.1'}
@pytest.fixture
def client(monkeypatch,tmp_path):
    monkeypatch.setenv("OBSERVATORY_DATA_DIR",str(tmp_path))
    monkeypatch.setattr(server,"_store",None)
    monkeypatch.setattr(server,"_series",None)
    monkeypatch.setattr(server,'jobs',server.Jobs(capacity=2,deadline=30))
    with TestClient(server.app) as client:
        yield client

def terminal(client,key):
    for _ in range(150):
        r=client.get('/api/jobs/'+key).json()
        if r['status']!='running':return r
        time.sleep(.05)
    pytest.fail('Worker did not finish')

def test_health_static_and_schema(client):
    assert client.get('/api/health').json()['certified'] is False
    r=client.get('/');assert r.status_code==200
    assert 'frame-ancestors' in r.headers['content-security-policy']
    assert "script-src 'self'" in r.headers['content-security-policy']
    assert client.get('/app.js').status_code==200
    assert client.get('/api/capabilities').json()['huge_height_live_evaluation'] is False
    assert client.get('/api/openapi.json').status_code==200

def test_csrf_host_and_payload_guards(client):
    assert client.post('/api/jobs',json={}).status_code==403
    assert client.post('/api/jobs',headers={**HEADERS,'Origin':'https://attacker.invalid'},json={}).status_code==403
    assert client.get('/api/health',headers={'Host':'attacker.invalid'}).status_code==403
    assert client.post('/api/jobs',headers=HEADERS,content='x'*17000).status_code==413
    assert client.post('/api/jobs',headers=HEADERS,json={'t':1e30}).status_code==422
    assert client.post('/api/jobs',headers=HEADERS,json={'module':'python'}).status_code==422

def test_real_process_job(client):
    r=client.post('/api/jobs',headers=HEADERS,json={'module':'primes','limit':100})
    assert r.status_code==202
    end=terminal(client,r.json()['job_id'])
    assert end['status']=='done' and end['result']['metrics']['π(limit)']==25

def test_cancel_capacity_and_missing_job(client):
    server.jobs.capacity=1
    job=client.post('/api/jobs',headers=HEADERS,json={'module':'geometry','grid':80,'samples':2048}).json()['job_id']
    assert client.post('/api/jobs',headers=HEADERS,json={'module':'height'}).status_code==429
    assert client.delete('/api/jobs/'+job,headers=HEADERS).json()['status']=='cancelled'
    assert client.get('/api/jobs/'+'0'*32).status_code==404
    assert not server.jobs.entries[job]['process'].is_alive()

def test_deadline_kills_worker(client):
    server.jobs.deadline=.001
    key=client.post('/api/jobs',headers=HEADERS,json={'module':'geometry','grid':80}).json()['job_id']
    time.sleep(.02)
    assert terminal(client,key)['status']=='timeout'
    assert not server.jobs.entries[key]['process'].is_alive()

def test_exact_coordinate_api(client):
    payload={'anchor':'201016554543249943627430143193','offset':'0.078428'}
    r=client.post('/api/coordinates',headers=HEADERS,json=payload)
    assert r.json()['exact_decimal']=='201016554543249943627430143193.078428'

@pytest.mark.parametrize('module,options',[
 ('cancellation',{'n':16,'split':7}),('sweep',{'n':16,'width_steps':3,'split_steps':3}),
 ('explicit',{'samples':8,'zero_count':8}),('refine',{'real':'2','imag':'0'}),
 ('family',{'samples':16,'discriminants':[-4]}),('hierarchy',{'limit':100}),
])
def test_new_modules_real_worker(client,module,options):
    r=client.post('/api/jobs',headers=HEADERS,json={'module':module,**options})
    assert r.status_code==202
    end=terminal(client,r.json()['job_id'])
    assert end['status']=='done',end
    assert end['result']['request']['module']==module


def test_new_schemas_duplicate_json_and_origin(client):
    schema=client.get('/api/capabilities').json()
    assert schema['provider_schemas']['cancellation']['additionalProperties'] is False
    assert client.post('/api/jobs',headers=HEADERS,content='{"module":"height","module":"geometry"}').status_code==422
    assert client.post('/api/jobs',headers={**HEADERS,'Origin':'http://['},json={}).status_code==403
    assert client.get('/api/health',headers={'Host':'['}).status_code==403


def test_persist_and_reopen_api(client):
    from engine import compute
    result=compute({'module':'cancellation','n':16,'split':7})
    data={'schema_version':2,'name':'API save','result':result,'comparison':result}
    saved=client.post('/api/investigations',headers=HEADERS,json=data)
    assert saved.status_code==201,saved.text
    key=saved.json()['investigation_id']
    got=client.get('/api/investigations/'+key).json()['experiment']
    assert got['result']==result and got['comparison']==result
    assert client.get('/api/investigations').json()['items'][0]['investigation_id']==key
    result['metrics']['A_energy']+=10
    assert client.post('/api/investigations',headers=HEADERS,json=data).status_code==422


def test_stored_series_api(client):
    data={'name':'API fixture','provenance':'synthetic','anchor':'999999999999999999999999',
          'samples':[{'offset':'0','value':1},{'offset':'0.000001','value':None},{'offset':'0.000002','value':-1}],
          'events':[{'index':1,'label':'missing'}]}
    reply=client.post('/api/datasets',headers=HEADERS,json=data)
    assert reply.status_code==201,reply.text
    key=reply.json()['dataset_id']
    view=client.get(f'/api/datasets/{key}/view?start=0&stop=3&buckets=8').json()
    assert view['signed_sum']==0 and view['missing_count']==1
    assert client.get(f'/api/datasets/{key}/sample/2').json()['exact_decimal']=='999999999999999999999999.000002'
    assert client.get(f'/api/datasets/{key}/view?stop=4').status_code==422

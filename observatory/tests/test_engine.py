import hashlib
import json
import math
import mpmath
import pytest
from pydantic import ValidationError
from engine import Spec, Coordinate, compute, sieve, evaluator, li_r, reduce_series, finite

@pytest.mark.parametrize('payload',[{'dps':1000},{'limit':200001},{'grid':100},{'samples':10000},{'t':1e30},{'t_min':5,'t_max':4},{'re_min':2,'re_max':1},{'module':'euler','limit':10001},{'sigma':float('nan')},{'sigma':float('inf')},{'module':'__import__'},{'execute':'rm -rf /'},{'kernel_n':1000},{'width':0},{'zero_count':65}])
def test_refuses_outside_capabilities(payload):
    with pytest.raises(ValidationError):
        Spec.model_validate(payload)

def test_exact_anchor_is_not_a_float():
    a='763173730199776587433631628770'
    assert Coordinate(anchor=a,offset='-0.068203').exact()=='763173730199776587433631628769.931797'
    assert Coordinate(anchor=a,offset='-0.068103').exact()=='763173730199776587433631628769.931897'
    assert float(a)==float(Coordinate(anchor=a,offset='-0.068203').exact())

@pytest.mark.parametrize('offset',['nan','inf','1e400','1/0','__import__("os")','0.'+'1'*61])
def test_coordinate_rejection(offset):
    with pytest.raises(ValidationError):
        Coordinate(anchor='100',offset=offset)

def test_linear_sieve():
    p,mu=sieve(100)
    assert len(p)==25 and p[-1]==97
    assert mu[:11]==[0,1,-1,-1,0,-1,1,-1,0,0,1]
    for n in range(1,101):
        assert sum(mu[d] for d in range(1,n+1) if n%d==0)==(n==1)

def test_pole_removal_and_functions():
    c=mpmath.mp.clone();c.dps=45
    assert abs(evaluator(c,'zeta',c.mpf(2))-c.pi**2/6)<c.mpf('1e-40')
    assert abs(evaluator(c,'eta',c.mpf(1))-c.log(2))<c.mpf('1e-40')
    assert evaluator(c,'xi',c.mpf(0))==c.mpf('.5')
    assert evaluator(c,'xi',c.mpf(1))==c.mpf('.5')
    assert abs(evaluator(c,'xi',c.mpf(-2))-evaluator(c,'xi',c.mpf(3)))<c.mpf('1e-40')
    assert abs(evaluator(c,'beta',c.mpf(2))-c.catalan)<c.mpf('1e-40')
    assert abs(evaluator(c,'chi3',c.mpf(1))-c.pi/(3*c.sqrt(3)))<c.mpf('1e-40')

@pytest.mark.parametrize('x',[2,3,10,100,1000,10000,200000])
def test_main_terms_against_independent_library_calls(x):
    a,b=li_r(x)
    assert math.isclose(a,float(mpmath.li(x)),rel_tol=3e-14,abs_tol=2e-13)
    assert math.isclose(b,float(mpmath.riemannr(x)),rel_tol=3e-14,abs_tol=2e-13)

def test_spike_extrema_and_sums_survive_reduction():
    xs=list(range(10001));ys=[0]*len(xs);ys[5003]=10**8;ys[8001]=-7
    result=reduce_series(xs,ys,50)
    assert [5003,10**8] in result['points'] and [8001,-7] in result['points']
    assert sum(e['sum'] for e in result['envelopes'])==10**8-7
    assert sum(e['absolute_sum'] for e in result['envelopes'])==10**8+7
    assert len(result['points'])<=4*50

def test_alternation_and_missing_region():
    xs=list(range(101));ys=[(-1)**i for i in xs];ys[35:41]=[None]*6
    r=reduce_series(xs,ys,10)
    assert r['missing_count']==6
    assert all([k,None] in r['points'] for k in range(35,41))
    assert not any(e['x0']<35 and e['x1']>40 for e in r['envelopes'])
    assert all(e['min']==-1 and e['max']==1 for e in r['envelopes'] if e['count']>1)

def test_event_layer_does_not_follow_display_decimation():
    a=compute({'module':'geometry','grid':16,'samples':64,'buckets':16})
    b=compute({'module':'geometry','grid':16,'samples':64,'buckets':64})
    assert a['events']==b['events']
    assert len(a['events'])>=3

def test_full_source_energy_identity():
    r=compute({'module':'mobius','limit':100,'kernel_n':32})
    v=r['metrics'];assert v['kernel_prefix']==32
    assert abs(v['full_energy']-v['energy_A']-v['energy_B']-v['cross_term'])<1e-12
    assert v['M(limit)']==1
    assert len(r['grid']['values'])==32**2
    assert v['full_energy']>=-1e-12

def test_finite_euler_identity_and_omission():
    r=compute({'module':'euler','sigma':2,'t':0,'limit':10})
    z=1
    for p in [2,3,5,7]:z/=1-p**-2
    assert math.isclose(r['series'][0]['points'][-1][1],z,rel_tol=1e-14)
    omitted=compute({'module':'euler','sigma':2,'t':0,'limit':10,'omit_prime':2})
    assert math.isclose(omitted['series'][0]['points'][-1][1],z*.75,rel_tol=1e-14)
    bad=compute({'module':'euler','sigma':.5,'limit':10})
    assert any('NOT analytic continuation' in w for w in bad['warnings'])

def test_nonfinite_display_values_are_masked():
    assert finite(float('inf')) is None
    assert finite(mpmath.mpf('1e-500')) is None
    assert finite(0)==0

def test_zeros_are_approximate_and_gaps_use_original_data():
    r=compute({'module':'zeros','zero_count':3})
    assert abs(float(r['events'][0]['decimal'])-14.134725141734694)<1e-13
    assert r['events'][0]['status']=='approximate'
    assert r['series'][0]['input_count']==2
    assert math.isclose(r['series'][0]['points'][0][1],21.022039638771556-14.134725141734694)

@pytest.mark.parametrize('module',['geometry','primes','euler','mobius','zeros','height'])
def test_serializable_identified_scoped_result(module):
    payload={'module':module,'grid':16,'samples':32,'limit':30,'kernel_n':8,'zero_count':2}
    r=compute(payload);encoded=json.dumps({k:v for k,v in r.items() if k!='result_id'},sort_keys=True,separators=(',',':'),allow_nan=False).encode()
    from identity import result_id
    assert result_id(r)==r['result_id']
    assert compute(payload)['result_id']==r['result_id']
    assert r['schema_version']==2
    assert 'certified' in r['evidence'] or 'pending' in r['evidence']
    assert r['warnings']

def test_huge_height_is_not_a_fake_z_plot():
    r=compute({'module':'height'})
    assert r['series']==[]
    assert r['metrics']['primitive_Z_replayed'] is False
    assert r['metrics']['width_exact']=='0.000100'
    assert 'd5d55b7950a4cc8a850e99c82b8f40e1699c7a3e' in r['sources'][0]

import copy
import math
import numpy as np
import mpmath as mp
import pytest
from pydantic import ValidationError
from engine import compute, parse_spec
from providers.cancellation import source
from providers.explicit import transform, gamma_integral, prime_powers
from providers.explorations import character_table, kronecker_positive_n


def cancel(**changes):
    return compute(dict(module='cancellation', n=24, split=9, **changes))


def test_full_comparison_trace_and_spectrum():
    r = cancel()
    a, b = r['experiments'].values()
    delta = np.array(r['grid']['values']).reshape(24,24)
    for data in (a,b):
        energy=data['energy']; m=np.array(data['matrix']).reshape(24,24)
        assert abs(energy['total']-energy['A']-energy['B']-energy['cross']) < 1e-12
        assert np.allclose(m, m.T)
        assert abs(math.fsum(data['rows'])-energy['total']) < 1e-12
        assert abs(data['prefix_energy'][-1]-energy['total']) < 1e-12
    assert np.allclose(delta.ravel(), np.array(b['matrix'])-a['matrix'])
    assert abs(delta.sum()-(b['energy']['total']-a['energy']['total'])) < 1e-12
    spec = r['spectrum']
    assert abs(sum(spec['mode_energy_a'])-a['energy']['total']) < 1e-11
    assert abs(sum(spec['mode_energy_b'])-b['energy']['total']) < 1e-11
    assert np.allclose(np.array(spec['vectors'])@np.array(spec['vectors']).T, np.eye(24))
    assert spec['residual_frobenius'] < 1e-10


def test_block_split_changes_ledger_not_full_source():
    a=cancel()
    b=compute({**a['request'],'split':19})
    for side in 'ab':
        assert a['experiments'][side]['matrix']==b['experiments'][side]['matrix']
        assert a['experiments'][side]['energy']['total']==b['experiments'][side]['energy']['total']
        assert a['experiments'][side]['energy']['A']!=b['experiments'][side]['energy']['A']
        assert a['experiments'][side]['experiment_id']!=b['experiments'][side]['experiment_id']


@pytest.mark.parametrize('control',['mobius','magnitude','random_signs','shuffled','liouville','alternating'])
def test_controls_are_actual_source_changes(control):
    r=cancel(source_b=control)
    a,b=r['experiments'].values()
    assert b['definition']
    if control=='mobius':
        assert a['matrix']==b['matrix']
        assert max(abs(v) for v in r['grid']['values'])==0
    if control in ['magnitude','random_signs','alternating']:
        assert [abs(v) for v in a['coefficients']]==[abs(v) for v in b['coefficients']]
    if control=='shuffled':
        assert sorted(a['coefficients'])==sorted(b['coefficients'])
    if control=='liouville':
        assert all(abs(v)==1 for v in b['coefficients'])
    assert np.array_equal(source(control,1,24,29), b['coefficients'])


def test_sweep_frozen_before_holdout():
    q=dict(module='sweep',n=16,width_steps=4,split_steps=4,holdout_start=501)
    r=compute(q); other=compute({**q,'holdout_start':1501})
    assert r['trials']==other['trials']
    assert r['detector']==other['detector']
    assert r['holdout']['request']['width']==r['detector']['width']
    assert r['holdout']['request']['split']==r['detector']['split']
    assert len(r['trials'])==16
    assert r['metrics']['holdout_evaluations']==1
    assert r['holdout']['experiments']!=other['holdout']['experiments']


@pytest.mark.parametrize('q',[
 {'module':'cancellation','n':12,'split':12}, {'module':'cancellation','n':193},
 {'module':'cancellation','width':0}, {'module':'cancellation','source_a':'untrusted'},
 {'module':'sweep','n':32,'train_start':1,'holdout_start':20},
 {'module':'sweep','width_min':2,'width_max':1},
 {'module':'explicit','band_first':10,'band_last':3},
 {'module':'explicit','band_last':50,'zero_count':20},
 {'module':'explicit','focus_b':6}, {'module':'refine','real':0.5},
 {'module':'refine','imag':'1e30'}, {'module':'family','discriminants':[4]},
 {'module':'family','discriminants':[-4,-4]}, {'module':'hierarchy','limit':500000},
 {'module':'hierarchy','run_arbitrary_python':'no'},
])
def test_new_provider_bounds(q):
    with pytest.raises(ValidationError):
        parse_spec(q)


def test_transform_independent_fourier_quadrature():
    with mp.workdps(35):
        for a,b,u in [(.04,0.,0.),(.1,2.,.8),(.2,1.,2.)]:
            # Independent half-line cosine integral, not provider's closed form.
            value=2*mp.quad(lambda t:mp.exp(-a*t*t)*mp.cos(b*t)*mp.cos(u*t),[0,5,10,20,40,mp.inf])
            assert math.isclose(float(transform(a,b,u)),float(value),rel_tol=1e-11,abs_tol=1e-12)


@pytest.mark.parametrize('b',[0., math.log(2), math.log(10)])
def test_archimedean_term_independent_mpmath(b):
    with mp.workdps(30):
        a=.04; T=12
        reference=mp.quad(lambda t:mp.exp(-a*t*t)*mp.cos(b*t)*mp.re(mp.digamma(mp.mpf('0.25')+mp.j*t/2)),list(range(T+1)))/mp.pi
        value=gamma_integral(a,[b],T,24)[0]
        assert math.isclose(value,float(reference),rel_tol=2e-12,abs_tol=2e-13)


def test_prime_powers_include_multiplicity_but_no_composites():
    pp={n:(p,k,v) for n,p,k,v in prime_powers(30)}
    assert pp[8][:2]==(2,3) and pp[9][:2]==(3,2) and pp[25][:2]==(5,2)
    assert pp[8][2]==math.log(2)
    assert 6 not in pp and 12 not in pp


def test_explicit_complete_ledger_and_deliberate_truncation():
    r=compute({'module':'explicit','samples':8})
    f=r['focus']
    assert abs(math.fsum(p['contribution'] for p in f['prime_terms'])-f['prime'])<1e-14
    assert abs(math.fsum(z['contribution'] for z in f['zero_terms'])-f['zeros'])<1e-14
    assert math.isclose(f['rhs'],math.fsum(f[k] for k in ['pole','logpi','gamma','prime']),abs_tol=1e-14)
    assert abs(f['discrepancy'])<1e-9
    assert all(r['boundaries'][k] is None for k in ['prime_tail_bound','zero_tail_bound','gamma_tail_bound','rounding_bound','quadrature_error_bound'])
    short=compute({**r['request'],'prime_cutoff':10,'focus_b':4})
    assert abs(short['focus']['discrepancy'])>.1
    assert 'DO NOT' in r['boundaries']['trivial_zeros']


def test_zero_band_is_literal_subset():
    r=compute({'module':'explicit','samples':8,'zero_count':8,'band_first':2,'band_last':3})
    gs=[float(v['gamma']) for v in r['focus']['zero_terms']][1:3]
    for b,y in r['series'][3]['points']:
        expected=sum(2*math.exp(-r['request']['a']*t*t)*math.cos(b*t) for t in gs)
        assert math.isclose(y,expected,abs_tol=1e-14)


def test_character_tables_and_induction():
    assert character_table(-4)==[0,1,0,-1]
    assert character_table(-3)==[0,1,-1]
    for D in [-4,-3,5,8,-7,-8,12,13,-11,17]:
        table=character_table(D)
        for m in range(1,20):
            assert kronecker_positive_n(D,m)==table[m%abs(D)]
            for n in range(1,20):
                assert kronecker_positive_n(D,m*n)==kronecker_positive_n(D,m)*kronecker_positive_n(D,n)
    r=compute({'module':'family','discriminants':[-4,5],'multiplier':3,'samples':16})
    assert all(abs(float(m['induction_residual_at_midpoint']))<1e-20 for m in r['members'])
    assert r['members'][0]['conductor']==4 and r['members'][0]['modulus']==12
    assert r['members'][0]['removed_euler_primes']==[3]


def test_sequence_membership_and_separate_fractional_coordinate():
    r=compute({'module':'hierarchy','limit':100,'depth':3,'alpha':.5})
    assert r['families'][1]['initial_members'][:6]==[2,3,5,7,11,13]
    assert r['families'][2]['initial_members'][:6]==[3,5,11,17,31,41]
    assert r['families'][3]['initial_members'][:3]==[5,11,31]
    assert r['fractional']['last_value_a_N']==10
    assert math.isclose(r['metrics']['fractional_index_sum'],sum(n**-.5 for n in range(1,101)))


def test_point_refinement_retains_decimal_input_and_fails_pole():
    r=compute({'module':'refine','real':'2','imag':'0','dps':80})
    with mp.workdps(85):
        assert abs(mp.mpf(r['point']['real'])-mp.pi**2/6)<mp.mpf('1e-79')
    assert 'NOT an error bound' in r['warnings'][0]
    with pytest.raises(ValueError):
        compute({'module':'refine','real':'1','imag':'0'})


def test_optional_flint_serialization():
    pytest.importorskip('flint')
    r=compute({'module':'refine','real':'2','imag':'0','backend':'flint'})
    assert r['point']['roundtrip_containment_checked'] is True

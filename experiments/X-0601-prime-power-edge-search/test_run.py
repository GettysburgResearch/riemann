import importlib.util
from pathlib import Path
import mpmath as mp

spec=importlib.util.spec_from_file_location('edge',Path(__file__).with_name('run.py'))
edge=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=edge
spec.loader.exec_module(edge)


def maxabs(A):
    return max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))

def test_prime_power_identity():
    x=edge.identify_prime_power(64)
    assert (x.p,x.exponent)==(2,6)
    assert [z.q for z in edge.prime_powers_up_to(10)]==[2,3,4,5,7,8,9]

def test_threshold_block_zero():
    with mp.workdps(60):
        item=edge.identify_prime_power(9)
        assert maxabs(edge.prime_power_even_block(9,item,4))==0

def test_edge_derivative_jump():
    with mp.workdps(90):
        item=edge.identify_prime_power(8);N=3;h=mp.mpf('1e-8')
        numerical=edge.prime_power_even_block(mp.mpf(8)*mp.exp(h),item,N)/h
        exact=edge.edge_derivative_jump_even(item,N)
        assert maxabs(numerical-exact)<mp.mpf('2e-7')

def test_m0_neutral_annihilates_jump():
    with mp.workdps(60):
        item=edge.identify_prime_power(5);N=2
        v=mp.matrix([-mp.sqrt(2),1,0])
        assert abs(edge.even_moment(v,0))<mp.mpf('1e-55')
        J=edge.edge_derivative_jump_even(item,N)
        assert abs((v.T*J*v)[0])<mp.mpf('1e-55')

def test_fifth_order_asymptotic():
    with mp.workdps(100):
        item=edge.identify_prime_power(5);N=2
        v=mp.matrix([-mp.sqrt(2),1,0])
        for eps in [mp.mpf('1e-2'),mp.mpf('3e-3')]:
            L=mp.log(item.q)/(1-eps);c=mp.exp(L)
            exact=(v.T*edge.prime_power_even_block(c,item,N)*v)[0]
            leading=edge.leading_moment_edge_term(v,item,eps,0)
            assert abs(exact/leading-1)<20*eps**2

def test_full_matrix_small_positive_and_symmetric():
    with mp.workdps(80):
        A=edge.build_cutoff_free_even_matrix('13',4,dps=80)
        assert maxabs(A-A.T)==0
        vals,_=mp.eigsy(A)
        assert vals[0]>0
        assert abs(vals[0]-mp.mpf('9.6792618605069722168465e-15'))<mp.mpf('1e-35')

def test_small_scan_has_no_negative():
    with mp.workdps(70):
        result=edge.scan_edges(limit=5,bands=[2],fractions=['0','0.5','0.98'],dps=70)
        assert result['summary']=={'cells':12,'empirical_negative_cells':0}

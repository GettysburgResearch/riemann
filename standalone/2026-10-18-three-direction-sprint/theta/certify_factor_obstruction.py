"""Fresh source14 obstruction to independent quadratic Gaussian factors."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,hashlib,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import source_extended
from certify_nonnegative_obstruction import load
I=b.I

def certify():
    primitive='inherited/pr886_primitive.py'
    b.require(hashlib.sha256((ROOT/primitive).read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned outward primitive identity')
    source=source_extended.reconstruct(14)
    unit=b.cumulants([F(int(j%2==0)) for j in range(15)])
    power={r:F((-1)**(r+1)*unit[2*r],2*factorial(2*r-1))*I(*source['standardized_cumulant_ratios'][r-1]) for r in range(2,8)}
    weights=[116,-2913,17762]
    bound=sum((2*weights[i]*power[i+2] for i in range(3)),I.coerce(0))-sum((weights[i]*weights[j]*power[i+j+3] for i in range(3) for j in range(3)),I.coerce(0))
    b.require(bound.lo>I.rat(35,100).hi,'strict power-sum lower bound above.35')
    b.require(bound.lo>I.rat(1,3).hi,'incompatible with variance1 independent positive factors')
    return {'schema':'T14S.quadratic-factor-obstruction.v1','status':'PROPOSED_COMPUTER_ASSISTED_FINITE_OBSTRUCTION','rh_proved':False,
        'moment_degree':14,'polynomial_weights':weights,'power_sum_intervals':{str(r):x.record() for r,x in power.items()},
        'sum_a_lower_interval':bound.record(),'excluded_sum_a_upper':'1/3','complete_theta_source':source,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [primitive,'source_extended.py','certify_nonnegative_obstruction.py','certify_factor_obstruction.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    start=time.time();out=certify();txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'fresh obstruction certificate equality')
    print('T14S_FACTOR_OBSTRUCTION_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,'lower',float(F(out['sum_a_lower_interval'][0],b.SCALE)),flush=True)

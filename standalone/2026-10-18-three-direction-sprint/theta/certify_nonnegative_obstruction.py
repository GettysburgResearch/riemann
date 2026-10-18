"""Fresh full-source finite obstruction to nonnegative Fourier models.

The saved certificate is an output, never a source of target intervals.
The analytic consumer is the global inequality cos(u) <= P_28(u).
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse, hashlib, json, sys, time

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import source_extended
I=b.I

def load(path):
    def pairs(items):
        out={}
        for k,v in items:
            b.require(k not in out,'duplicate JSON key');out[k]=v
        return out
    def no_float(x):raise ValueError('floating or nonfinite proof input')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=no_float,parse_constant=no_float)

def certify():
    primitive='inherited/pr886_primitive.py'
    b.require(hashlib.sha256((ROOT/primitive).read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned outward primitive identity')
    source=source_extended.reconstruct(28)
    raw={int(k):I(*v) for k,v in source['raw'].items()}
    terms=[I.coerce(1)]
    for j in range(2,29,2):
        terms.append(F((-1)**(j//2)*15**j,factorial(j))*(raw[j]/raw[0]))
    upper=sum(terms,I.coerce(0))
    b.require(upper.hi<I.rat(-1,1000).lo,'strict negative full-source cosine upper expectation below -1/1000')
    return {'schema':'T28S.nonnegative-obstruction.v1',
        'status':'PROPOSED_COMPUTER_ASSISTED_FINITE_OBSTRUCTION',
        'rh_proved':False,'moment_degree':28,'original_theta_frequency':15,
        'cosine_upper_expectation':upper.record(),
        'negative_margin_lower':str(F(-upper.hi,b.SCALE)),
        'term_intervals':[x.record() for x in terms],
        'excluded_class':'all symmetric probability laws with everywhere nonnegative real Fourier transform and matching original theta moments through28',
        'complete_theta_source':source,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [primitive,'source_extended.py','certify_nonnegative_obstruction.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    start=time.time();out=certify();txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'fresh obstruction certificate equality')
    print('T28S_NONNEGATIVE_OBSTRUCTION_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,'upper',float(F(out['cosine_upper_expectation'][1],b.SCALE)),flush=True)

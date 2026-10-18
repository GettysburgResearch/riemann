"""Fresh finite complexity obstructions for Hermite-square block products."""
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
WITNESSES={1:[116,-2913,17762],2:[375,-35859,1305830,-19223562,91738523],3:[929,-232857,24361269,-1233811672,31243955787,-370336951380,1564944275303]}

def certify():
    primitive='inherited/pr886_primitive.py'
    b.require(hashlib.sha256((ROOT/primitive).read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned outward primitive identity')
    source=source_extended.reconstruct(30);unit=b.cumulants([F(int(j%2==0)) for j in range(31)])
    power={r:F((-1)**(r+1)*unit[2*r],2*factorial(2*r-1))*I(*source['standardized_cumulant_ratios'][r-1]) for r in range(2,16)}
    results=[]
    for degree_cap,weights in WITNESSES.items():
        dim=len(weights);bound=sum((2*weights[i]*power[i+2] for i in range(dim)),I.coerce(0))-sum((weights[i]*weights[j]*power[i+j+3] for i in range(dim) for j in range(dim)),I.coerce(0))
        threshold=F(degree_cap,2*degree_cap+1)
        b.require(bound.lo>I.coerce(threshold+F(1,1000)).hi,'strict finite Hermite-complexity obstruction margin above.001')
        results.append({'maximum_hermite_degree':degree_cap,'theta_moment_degree_needed':4*dim+2,'weights':weights,'S1_lower_interval':bound.record(),'excluded_upper':str(threshold)})
    return {'schema':'T30S.hermite-complexity-obstruction.v1','status':'PROPOSED_COMPUTER_ASSISTED_FINITE_OBSTRUCTION','rh_proved':False,'complete_theta_source':source,
        'power_sum_intervals':{str(r):x.record() for r,x in power.items()},'obstructions':results,
        'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in [primitive,'source_extended.py','certify_nonnegative_obstruction.py','certify_hermite_obstruction.py']}}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args();b.require(bool(a.emit)!=bool(a.check),'choose emit or check')
    start=time.time();out=certify();txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:b.require(load(a.check)==out,'fresh full-source Hermite obstruction certificate equality')
    print('T30S_HERMITE_OBSTRUCTION_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)

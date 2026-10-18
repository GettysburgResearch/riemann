"""Independent finite assembly and adversarial directed-source controls."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import itertools,json,hashlib,argparse,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import model

def require(ok,message):
    if not ok:raise ValueError(message)

def fixture(degree=22):
    z=[F(3,7),F(0),F(1),F(7,9),F(-1,5),F(4,5),F(5,8),F(1,8),F(3,5)]
    counts=[2,1,1];eta=F(1,11)
    weights=[F(0),F(3,7),F(3,7),(z[3]+z[4])/2,(z[3]-z[4])/2,(z[6]+z[7])/2,(z[6]-z[7])/2]
    edges=[(0,1,eta),(0,2,eta),(0,3,eta),(3,4,2*z[5]-1),(0,5,eta),(5,6,2*z[8]-1)]
    raw=[F(0)]*(degree+1);mass=F(0)
    for spins in itertools.product((-1,1),repeat=7):
        probability=F(1,128)
        for a,c,q in edges:probability*=1+q*spins[a]*spins[c]
        value=sum(w*s for w,s in zip(weights,spins));mass+=probability
        for n in range(degree+1):raw[n]+=probability*value**n
    require(mass==1,'fixture normalization')
    require(all(raw[j]==0 for j in range(1,degree+1,2)),'fixture odd moments')
    _,got=model.evaluate(z,counts,eta,degree)
    require(raw==got,'all128fixture configurations versus complete cumulants')
    direct=model.direct_assembly(z,counts,eta,degree);require(direct==raw,'fixture direct-series assembly')
    changed=list(z);changed[4]=abs(changed[4])
    require(model.evaluate(changed,counts,eta,degree)[1]!=raw,'inner orientation is load-bearing')
    require(model.evaluate(z,counts,F(0),degree)[1]!=raw,'hub deletion must change finite law')
    return {'configurations':128,'degree':degree,'all_orders_compared':degree+1,'negative_inner_amplitude_test':True,'hub_deletion_test':True}

def strip_factor_grid():
    tests=0
    for delta,y in [(F(1,3),F(1)),(F(1,3),F(1,2)),(F(1,3),F(12,25)),(F(0),F(1))]:
        require(y*y>2*delta*delta,'strict one-point threshold')
        c=2*y*y if delta==0 else y*y*min(F(2),y*y/(delta*delta)-2)
        for x in [F(1,1000),F(1,10),F(1),F(10),F(1000)]:
            for u in [F(0),delta/4,delta/2,delta]:
                r2=x*x+u*u;q=1+y*y*(2*r2+y*y-4*u*u)/(r2*r2)
                require(q-1>=c/r2,'exact one-point factor inequality');tests+=1
    delta=F(1,3);y=F(9,20);x=F(1,1000);u=delta;r2=x*x+u*u
    q=1+y*y*(2*r2+y*y-4*u*u)/(r2*r2)
    require(delta<y and y*y<2*delta*delta and q<1,'factor positivity proof gate below sqrt2delta')
    return {'exact_rational_factor_cases':tests,'below_threshold_factor_counterexample':True}

def main(emit=None):
    start=time.time();small=fixture();p=json.loads((ROOT/'parameters22.json').read_text());z=list(map(F,p['centers']));eta=F(p['hub_correlation']);counts=p['counts'];degree=p['degree']
    _,raw=model.evaluate(z,counts,eta,degree);direct=model.direct_assembly(z,counts,eta,degree)
    require(raw==direct,'complete307vertex direct-series equality through22')
    changed=list(counts);changed[1]-=1
    require(model.direct_assembly(z,changed,eta,degree)!=raw,'multiplicity deletion must change full model')
    require(len(raw)==23 and degree==22,'full endpoint order22 retained')
    require(len(raw[:-1])!=23,'omitted highest order rejected')
    require(sum(F(24**j,factorial(j)) for j in range(25))>2*10**9,'elementary upper coupling bound')
    zero=model.Dual(F(0),[F(1)]);require((zero**1).d==(F(1),) and (zero**2).d==(F(0),),'zero-amplitude polynomial differentiation')
    factors=strip_factor_grid()
    out={'status':'FINITE_CONTROLS_PASS','fixture':small,'complete_model_raw_orders':23,'complete_model_vertices':307,'full_series_matches':True,
         'multiplicity_mutation_rejected':True,'missing_order22_rejected':True,'zero_amplitude_derivative':True,'couplings_below12':True,'strip_factor_controls':factors,
         'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['model.py','parameters22.json','finite_controls.py']}}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if emit:emit.write_text(txt)
    print('T22S_FINITE_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest(),'seconds',time.time()-start,flush=True)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path,default=ROOT/'finite_controls22.json');a=p.parse_args();main(a.emit)

"""Exact rational global obstruction for an observed-hub harmonic star.

No optimizer, floating fit, special-function library or saved theta moment
is an acceptance dependency. The theta variance is reconstructed completely.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'inherited'))
import pr886_primitive as b
import source_extended

def log_bounds(x,terms=100):
    x=F(x);b.require(x>0,'positive logarithm argument');k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def core(y):
        z=(y-1)/(y+1);power=z;total=F(0)
        for n in range(terms):total+=2*power/(2*n+1);power*=z*z
        tail=2*power/((2*terms+1)*(1-z*z))
        return total,total+tail
    l,u=core(x);l2,u2=core(F(2))
    return (l+k*l2,u+k*u2) if k>=0 else (l+k*u2,u+k*l2)

def main(emit):
    began=time.monotonic();N=100;H=sum((F(1,n) for n in range(1,N+1)),F(0));lnlo,lnhi=log_bounds(N)
    # Alternating Euler--Maclaurin remainder for Euler's constant.
    gamma_lo=H-lnhi-F(1,2*N)+F(1,12*N*N)-F(1,120*N**4)
    gamma_hi=H-lnlo-F(1,2*N)+F(1,12*N*N)
    l4,u4=log_bounds(4);Klo,Khi=gamma_lo+l4,gamma_hi+u4
    b.require(Klo>F(1963,1000) and Khi<F(1964,1000),'rigorous coarse gamma+log4 bounds')
    b.require(log_bounds(F(38,5))[1]-F(5,76)<F(1963,1000),'a<=7.6 impossible by the digamma upper bound')
    h=F(7,2);records=[]
    for k in range(76,120):
        low,up=F(k,10),F(k+1,10)
        S2=F(1,4)/up+F(1,8)/(up*up)
        S4=F(1,48)/low**3+F(1,16)/low**4
        B=max(F(0),(log_bounds(low-F(1,2))[0]-F(1964,1000))/2)
        m=h*S2-h**3*S4/3
        b.require(m>0,'positive conditional-mean lower bound')
        lower=S2-h*h*S4+(B+m)**2
        b.require(lower>F(48,1000),'uniform observed-star variance above .048 on each entire cell')
        records.append({'a_interval':[str(low),str(up)],'variance_lower':str(lower)})
    B12=(log_bounds(F(23,2))[0]-F(1964,1000))/2
    b.require(B12>0 and B12*B12>F(47,1000),'a>=12 impossible by hub variance alone')
    primitive=ROOT/'inherited/pr886_primitive.py'
    b.require(hashlib.sha256(primitive.read_bytes()).hexdigest()=='2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55','pinned directed backend')
    source=source_extended.reconstruct(2)
    b.require(F(source['variance'][1],b.SCALE)<F(47,1000),'fresh full-theta variance below .047')
    result={'status':'PROPOSED_CERTIFIED_HARMONIC_OBSERVED_OBSTRUCTION','rh_proved':False,'class':'w_n=1/(2(n+a)), B>=0, J_n>=7w_n/2, J_n=7w_n/2+O(w_n^2); no finite weight changes','gamma_log4_interval':[str(Klo),str(Khi)],'grid':records,'uniform_grid_variance_lower':'6/125','full_theta_source':source,'input_hashes':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['certify_harmonic_observed_obstruction.py','source_extended.py','inherited/pr886_primitive.py']}}
    text=json.dumps(result,sort_keys=True,separators=(',',':'))+'\n';emit.write_text(text)
    print('HARMONIC_OBSERVED_OBSTRUCTION_PASS',hashlib.sha256(text.encode()).hexdigest(),'seconds',time.monotonic()-began,'minimum_grid_lower',float(min(F(r['variance_lower']) for r in records)),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--emit',type=Path,default=ROOT/'harmonic_observed_obstruction.json');a=ap.parse_args();main(a.emit)

"""Independent complete Gibbs enumeration and full finite-product assembly."""
from fractions import Fraction as F
from math import factorial
from itertools import product
from pathlib import Path
import json,argparse
from connected_blocks import evaluate,COUNTS,ETA
ROOT=Path(__file__).resolve().parent

def need(x,message):
    if not x:raise ValueError(message)

def fixture(corrupt=None):
    degree=20;eta=F(1,11);counts=(2,1,1)
    z=[F(1,5),F(0),F(1),F(7,10),F(1,10),F(3,4),F(4,5),F(1,5),F(2,3)]
    # hub 0; two fair leaves 1,2; two dimers (3,4) and(5,6).
    weights=[F(0),z[0],z[0],(z[3]+z[4])/2,(z[3]-z[4])/2,(z[6]+z[7])/2,(z[6]-z[7])/2]
    edges=[(0,1,eta),(0,2,eta),(0,3,eta),(3,4,2*z[5]-1),(0,5,eta),(5,6,2*z[8]-1)]
    raw=[F(0)]*(degree+1)
    for spins in product((-1,1),repeat=7):
        prob=F(1,2**7)
        for i,j,q in edges:prob*=1+q*spins[i]*spins[j]
        y=sum(a*s for a,s in zip(weights,spins));power=F(1)
        for k in range(degree+1):raw[k]+=prob*power;power*=y
    need(raw[0]==1,'complete Gibbs probability normalization')
    need(all(raw[k]==0 for k in range(1,degree+1,2)),'global spin reversal')
    zz=z[:];cc=counts;ee=eta;top=degree
    if corrupt=='erase_hub':ee=F(0)
    elif corrupt=='reverse_inner':zz[4]=-zz[4]
    elif corrupt=='reduce_count':cc=(1,1,1)
    elif corrupt=='omit_top':top=18
    elif corrupt is not None:raise ValueError('unknown corruption')
    _,model=evaluate(zz,degree=top,counts=cc,eta=ee)
    need(len(model)==21,'all raw moment orders0through20 required')
    need(all(a==b for a,b in zip(raw,model)),'complete seven-spin assembly mismatch')
    # An independent modification of a real internal edge changes the law.
    altered=z[:];altered[5]=F(1,2)
    _,new=evaluate(altered,counts=counts,eta=eta)
    need(new[2]!=raw[2],'positive internal edge is observable')
    return {'states':128,'moments_checked':list(range(21)),'mass':'1','edge_deletion_changes_variance':True}

def conv(a,b,degree):
    return [sum((a[j]*b[k-j] for j in range(k+1)),F(0)) for k in range(degree+1)]
def power(p,n,degree):
    out=[F(1)]+[F(0)]*degree
    while n:
        if n&1:out=conv(out,p,degree)
        n//=2
        if n:p=conv(p,p,degree)
    return out

def full_product(z,degree=20):
    poly=[F(1)]+[F(0)]*degree
    for i,count in enumerate(COUNTS):
        A,B,p=z[3*i:3*i+3]
        base=[F(1)]+[(A**r if i==0 else p*A**r+(1-p)*B**r)*(1 if r%2==0 else ETA)/factorial(r) for r in range(1,degree+1)]
        poly=conv(poly,power(base,count,degree),degree)
    raw=[x*factorial(k) if k%2==0 else F(0) for k,x in enumerate(poly)]
    _,model=evaluate(z,degree)
    need(raw==model,'full305-spin generating-product identity')
    return {'vertices':305,'observed_vertices':304,'edges':304,'raw_orders':list(range(degree+1)),
            'arithmetic':'exact Fraction at rational center','scope':'finite assembly; not root or theta-source proof'}

def run(corrupt=None):
    small=fixture(corrupt)
    if corrupt is not None:raise ValueError('a corruption unexpectedly passed')
    params=json.loads((ROOT/'parameters20.json').read_text());z=[F(x) for x in params['centers']]
    large=full_product(z)
    return {'status':'EXACT_FINITE_ASSEMBLY_PASS','small':small,'whole_model':large}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--corrupt');p.add_argument('--emit',type=Path);p.add_argument('--check',type=Path);a=p.parse_args()
    out=run(a.corrupt);txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    if a.emit:a.emit.write_text(txt)
    if a.check:need(json.loads(a.check.read_text())==out,'finite receipt differs')
    print('T20D_FINITE_ASSEMBLY_PASS',flush=True)

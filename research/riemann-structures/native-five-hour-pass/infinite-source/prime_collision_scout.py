#!/usr/bin/env python3
"""Directed two-prime physical-frame reconnaissance for the proved scaling law."""
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
from pathlib import Path
import argparse
import importlib.util
import json
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
FREEZE='a454106bd685d618f61231549e6fd99bf5b5a1ad'
CORE_PATH='research/riemann-structures/native-five-hour-pass/infinite-source/physical_infinity.py'
CORE_BLOB='36ddede447e6190e7712d3afbdae04f50b7ab1d9'
PAIRS=((101,103),(1009,1013),(10007,10009),(1000003,1000033))
L=32;PRECISION=192
BITS=tuple(product((0,1),repeat=2));TRITS=tuple(product(range(3),repeat=2))
BASIS=((0,(0,1)),(0,(0,2)),(1,(2,0)))
INDEX={(tuple(p[k]+int(k==i) for k in range(2)),i):j for j,(i,p) in enumerate(BASIS)}
OUTPUT=HERE/'prime_collision_scout.verification.json'

def need(ok,why):
    if not ok:raise ValueError(why)

def source_bytes():
    raw=subprocess.check_output(['git','cat-file','blob',f'{FREEZE}:{CORE_PATH}'],cwd=ROOT)
    actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    need(actual==CORE_BLOB,'frozen physical core blob')
    return raw

def load_core():
    raw=source_bytes();module_path=HERE/'physical_infinity.py'
    need(sha256(module_path.read_text(encoding='utf8').encode()).hexdigest()==
         '9eaad7aac963f0ad13d2d4a2656258bf172e61fc51fbb5af74a0aff7f1b13207',
         'current physical core LF binding')
    spec=importlib.util.spec_from_file_location('prime_collision_core',module_path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    need(sha256(raw).hexdigest()==sha256(module_path.read_text(encoding='utf8').encode()).hexdigest(),
         'frozen versus working core LF bytes')
    return module,sha256(raw).hexdigest()

def decoder(a,b):
    total=tuple(x+y for x,y in zip(a,b));row=[0]*4
    if total==(0,0):return row
    row[0]=1;active=[i for i in range(2) if total[i]==1]
    sign=[a[i]-b[i] for i in range(2)]
    if 2 in total:
        for i in active:row[1+INDEX[total,i]]+=sign[i]
    elif active:
        anchor=active[-1];row[0]+=sign[anchor]
        for i in active[:-1]:row[1+INDEX[total,i]]+=sign[i]-sign[anchor]
    return row

def endpoints(core,x):return core.endpoints(x)

def panel(core,p,q,arb,arb_mat,arb_poly):
    local=[core.local_arb(prime,L,arb,arb_mat,arb_poly) for prime in (p,q)]
    exponents=list(range(-L,L+1));N=len(exponents);slab=arb_mat(N,N);cache={}
    for i,a in enumerate(exponents):
        for j,b in enumerate(exponents):
            n=p**max(a,0)*q**max(b,0);d=p**max(-a,0)*q**max(-b,0)
            if n>=8*d or d>=8*n:continue
            key=(max(n,d),min(n,d))
            if key not in cache:cache[key]=core.gamma_arb(*key,arb)
            slab[i,j]=cache[key]
    need(len(cache)<=16000,'registered kernel-frequency cap')
    tensor=local[0][0]*slab*local[1][0].transpose()
    nu0=128*(3+arb(2).sqrt())*arb(2).log()-288
    masses=[];tails=[]
    for a in TRITS:
        mass=arb(1);eta=arb(0)
        for i in range(2):mass*=local[i][3][a[i]]
        for i in range(2):
            term=local[i][2][a[i]]
            for j in range(2):
                if i!=j:term*=local[j][3][a[j]]
            eta+=term
        masses.append(mass);tails.append(eta)
    pos={a:i for i,a in enumerate(TRITS)};H=arb_mat(9,9)
    for i,a in enumerate(TRITS):
        for j,b in enumerate(TRITS):
            error=nu0*(tails[i]*masses[j]+tails[j]*masses[i])
            H[i,j]=tensor[3*a[0]+b[0],3*a[1]+b[1]]+arb(0,error.upper())
    pairs=tuple(product(BITS,repeat=2));K=arb_mat(16,16)
    for i,(a,b) in enumerate(pairs):
        for j,(c,d) in enumerate(pairs):
            K[i,j]=H[pos[tuple(x+y for x,y in zip(a,d))],
                     pos[tuple(x+y for x,y in zip(b,c))]]
    D=arb_mat([decoder(a,b) for a,b in pairs]).transpose();raw=D*K*D.transpose()
    scales=(-arb(p*q).sqrt(),4*q*arb(p).sqrt(),4*p*arb(q).sqrt())
    G=arb_mat([[raw[i+1,j+1]*scales[i]*scales[j] for j in range(3)] for i in range(3)])
    piv=[];ell=[[arb(int(i==j)) for j in range(3)] for i in range(3)]
    for i in range(3):
        value=G[i,i]-sum((ell[i][k]**2*piv[k] for k in range(i)),arb(0))
        need(value>0,'directed positive collision Gram pivot');piv.append(value)
        for j in range(i+1,3):
            ell[j][i]=(G[j,i]-sum((ell[j][k]*ell[i][k]*piv[k]
                                   for k in range(i)),arb(0)))/value
    inverse=G.inv();lower=1/max(sum(abs(inverse[i,j]).upper() for j in range(3))
                                for i in range(3))
    upper=max(sum(abs(G[i,j]).upper() for j in range(3)) for i in range(3))
    gh=core.gamma_arb(q,p,arb);g2h=core.gamma_arb(q*q,p*p,arb)
    limit=arb_mat([[ (nu0-g2h)/2,0,0],[0,nu0/2,gh/2],[0,gh/2,nu0/2]])
    correlation=G[1,2]/(G[1,1]*G[2,2]).sqrt()
    return {'primes':[p,q],'log_ratio_interval':endpoints(core,(arb(q)/p).log()),
            'normalized_Gram_intervals':[[endpoints(core,G[i,j]) for j in range(3)]
                                         for i in range(3)],
            'ratio_limit_matrix_at_current_ratio':[[endpoints(core,limit[i,j]) for j in range(3)]
                                                    for i in range(3)],
            'EC_ED_correlation_interval':endpoints(core,correlation),
            'predicted_correlation_at_current_ratio':endpoints(core,gh/nu0),
            'frame_lower_interval':endpoints(core,lower),'frame_upper_interval':endpoints(core,upper),
            'LDL_pivot_intervals':list(map(lambda x:endpoints(core,x),piv)),
            'kernel_values':len(cache)}

def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)

def build():
    core,core_sha=load_core();core.authenticate();arb,arb_mat,arb_poly,ctx=core.arb_import();ctx.prec=PRECISION
    result={'schema':'native-prime-collision-directed-scout/v1',
            'status':'DIRECTED FINITE RECONNAISSANCE; theorem is proved separately',
            'cutoff':L,'precision_bits':PRECISION,'core_freeze':FREEZE,
            'core_blob':CORE_BLOB,'core_sha256':core_sha,
            'panels':[panel(core,p,q,arb,arb_mat,arb_poly) for p,q in PAIRS],
            'scope':{'finite_panels_prove_limit':False,'fixed_prime_injectivity_reproved':False,
                     'physical_measure':True,'coefficient_norm_substituted':False}}
    result['producer_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    result['proof_sha256']=sha256((HERE/'PRIME_COLLISION_PHYSICAL_FRAME.md').read_bytes()).hexdigest()
    result['preregistration_sha256']=sha256((HERE/'PRIME_COLLISION_PREREGISTRATION.md').read_bytes()).hexdigest()
    return result

def main():
    parser=argparse.ArgumentParser();mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write',action='store_true');mode.add_argument('--check',action='store_true')
    args=parser.parse_args();data=build()
    if args.write:OUTPUT.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n',encoding='utf8')
    else:need(canonical(json.loads(OUTPUT.read_text()))==canonical(data),'fresh complete scout replay')
    print(canonical({'status':'PASS','panels':len(data['panels']),
                     'correlations':[x['EC_ED_correlation_interval'] for x in data['panels']]}))

if __name__=='__main__':main()

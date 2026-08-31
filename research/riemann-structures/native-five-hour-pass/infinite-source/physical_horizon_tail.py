#!/usr/bin/env python3
"""Certified complete positive coefficient tail at original product horizons."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json

HERE=Path(__file__).resolve().parent
PANEL=(32,40,48,56,61)
CORE_SHA='9eaad7aac963f0ad13d2d4a2656258bf172e61fc51fbb5af74a0aff7f1b13207'
GRAM_NAME='physical_infinity_L96_p192.acquisition.json'
GRAM_SHA='e828069e8898a464741553a44f53a13bb11d93c5c27ed5475130656a99749757'

def require(ok,why):
    if not ok:raise ValueError(why)

def unique_object(pairs):
    out={}
    for key,value in pairs:
        require(key not in out,'duplicate JSON key')
        out[key]=value
    return out

def strict_load(raw):
    def bad_constant(value):raise ValueError('nonfinite JSON constant: '+value)
    return json.loads(raw,object_pairs_hook=unique_object,parse_constant=bad_constant)

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)

def load_core():
    path=HERE/'physical_infinity.py'
    require(sha256(path.read_text(encoding='utf8').encode()).hexdigest()==CORE_SHA,
            'pinned core before import')
    spec=importlib.util.spec_from_file_location('physical_horizon_pinned_core',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

core=load_core()

def authenticate_gram(manifest):
    raw=(HERE/GRAM_NAME).read_bytes()
    require(len(raw)<=2000000,'bounded physical Gram capture')
    require(sha256(raw).hexdigest()==GRAM_SHA,'pinned infinite physical Gram capture')
    data=strict_load(raw)
    require(data['producer_sha256']==CORE_SHA,'infinite Gram producer binding')
    require(type(data['L']) is int and data['L']==96,'fixed Gram cutoff')
    require(type(data['precision_bits']) is int and data['precision_bits']==192,
            'fixed Gram precision')
    require(data['local_product_truncation'] is True,'Gram cutoff interface')
    require(canonical(data['primitive_sources'])==canonical(manifest),'same original source')
    require(data['source_norm']=='Euclidean norm of twenty declared occupation coordinates',
            'same source coordinate normalization')
    lower=data['frame_lower_interval']
    require(type(lower) is list and len(lower)==2 and all(type(x) is str for x in lower),
            'exact rational frame endpoints')
    require(F(lower[0])<=F(lower[1]) and F(lower[0])>F(1,12000000),
            'strict independently replayable infinity frame bound')
    require(len(data['ldl_pivot_intervals'])==20 and
            all(F(pair[0])>0 for pair in data['ldl_pivot_intervals']),
            'all twenty positive directed LDL pivots')
    return {'file':GRAM_NAME,'sha256':GRAM_SHA,'producer_sha256_lf':CORE_SHA,
            'certified_frame_lower_interval':lower,
            'complete_Gram_recomputed_here':False}

def weights(N):
    require(type(N) is int and 0<=N<=61,'bounded exact coefficient degree')
    b=[F(1)]
    for k in range(1,N+1):b.append(-b[-1]*(F(1,2)-k+1)/k)
    w=[]
    for e in range(N+1):
        a=b[e//2] if e%2==0 else F(0)
        w.append(abs(a)+abs(b[e]-a))
    u=[sum(w[i]*w[k-i] for i in range(k+1)) for k in range(N+1)]
    return w,u

def smooth_products(H):
    require(type(H) is int and 1<=H<=2**61,'bounded positive integer horizon')
    count=0;a=0;n2=1
    while n2<=H:
        b=0;n3=n2
        while n3<=H:
            c=0;n=n3
            while n<=H:
                count+=1
                core.require(count<=100000,'complete smooth-product cap')
                yield n,a,b,c
                c+=1;n*=5
            b+=1;n3*=3
        a+=1;n2*=2

def prefix(H,arb):
    N=H.bit_length()-1
    w,u=weights(N)
    exact=[arb(x.numerator)/x.denominator for x in u]
    total=arb(0);count=0;digest=sha256()
    for n,a,b,c in smooth_products(H):
        coefficient=u[a]*u[b]*u[c]
        digest.update(f'{n},{a},{b},{c}:{coefficient}\n'.encode())
        total+=exact[a]*exact[b]*exact[c]/arb(n).sqrt()
        count+=1
    return total,count,digest.hexdigest()

def build():
    manifest=core.authenticate()
    gram_binding=authenticate_gram(manifest)
    arb,_,_,ctx=core.arb_import();ctx.prec=192
    complete=arb(1)
    for p in core.PRIMES:
        q=1/arb(p).sqrt()
        W=2+(1+q).sqrt()-2*(1-q*q).sqrt()
        complete*=W*W
    nu0=128*(3+arb(2).sqrt())*arb(2).log()-288
    rows=[]
    for k in PANEL:
        H=2**k;part,count,digest=prefix(H,arb)
        tail=2*(complete-part)
        core.require(tail>0,'strict positive omitted coefficient mass')
        delta2=20*nu0*tail*tail
        margin=arb(1)/48000000-delta2
        rows.append({'H':str(H),'power_of_two':k,'prefix_count':count,
                     'prefix_sha256':digest,'field_tail_interval':core.endpoints(tail),
                     'operator_tail_squared_interval':core.endpoints(delta2),
                     'frame_margin_interval':core.endpoints(margin),
                     'uniform_physical_frame_pass':bool(margin>0)})
    return {'schema':'native-original-horizon-positive-tail/v1',
            'status':'directed tail acquisition; independent review pending',
            'primitive_sources':manifest,'precision_bits':192,'rows':rows,
            'infinite_physical_Gram':gram_binding,
            'producer_sha256_lf':sha256(Path(__file__).read_text().encode()).hexdigest(),
            'core_sha256_lf':sha256(Path(core.__file__).read_text().encode()).hexdigest(),
            'source_infinity_lower':'1/12000000','result_uniform_lower':'1/48000000'}

def main():
    parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--write',action='store_true');modes.add_argument('--check',action='store_true')
    args=parser.parse_args();data=build();path=HERE/'physical_horizon_tail.verification.json'
    if args.write:path.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    else:core.require(canonical(strict_load(path.read_text()))==canonical(data),
                      'complete fresh typed tail replay')
    print(json.dumps([{'H':r['H'],'prefix_count':r['prefix_count'],
                       'tail_upper':float(F(r['field_tail_interval'][1])),
                       'PASS':r['uniform_physical_frame_pass']} for r in data['rows']],indent=2))

if __name__=='__main__':main()

#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any
import numpy as np
from scipy.linalg import toeplitz

VECTOR_SCHEMA='riemann.piecewise-carrier-vector.v1'
BOX_SCHEMA='riemann.toeplitz-coefficient-box.v1'
FINAL_SCHEMA='riemann.piecewise-carrier-final-interval.v1'

def fhex(x:str)->Fraction:
    return Fraction.from_float(float.fromhex(x))

def fj(x:Fraction)->dict[str,int]:
    return {'numerator':x.numerator,'denominator':x.denominator}

def ij(lo:Fraction,hi:Fraction)->dict[str,dict[str,int]]:
    if lo>hi: raise ValueError('reversed interval')
    return {'lower':fj(lo),'upper':fj(hi)}

def canonical_sha(v:Any)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')).hexdigest()

def mul_interval_scalar(a:tuple[Fraction,Fraction],x:Fraction):
    u=a[0]*x;v=a[1]*x
    return min(u,v),max(u,v)

def merge_shards(paths:list[Path]):
    items=[json.loads(p.read_text()) for p in paths]
    if not items: raise ValueError('no shards')
    ref=items[0]
    keys=('cutoff','carrier','cells','precision_bits','segment_size','total_segments')
    for item in items:
        if item.get('schema')!='riemann.mpfr-toeplitz-box-shard.v1': raise ValueError('bad shard schema')
        for key in keys:
            if item.get(key)!=ref.get(key): raise ValueError(f'parameter mismatch: {key}')
        if item.get('ambiguous_lags')!=0: raise ValueError('ambiguous support lag')
    items.sort(key=lambda x:x['segment_start'])
    cursor=0; hpstreams=0; pc=hc=tc=0; K=ref['cells']
    lr=[Fraction(0) for _ in range(K)]; ur=[Fraction(0) for _ in range(K)]
    li=[Fraction(0) for _ in range(K)]; ui=[Fraction(0) for _ in range(K)]
    for item in items:
        if item['segment_start']!=cursor: raise ValueError(f'coverage gap or overlap at {cursor}')
        cursor=item['segment_end']; hpstreams+=int(item['include_higher_powers'])
        pc+=item['prime_count']; hc+=item['higher_prime_power_count']; tc+=item['total_terms']
        if item['total_terms']!=item['prime_count']+item['higher_prime_power_count']: raise ValueError('term-count mismatch')
        if len(item['lags'])!=K: raise ValueError('wrong lag count')
        for d,row in enumerate(item['lags']):
            if row['lag']!=d: raise ValueError('lag order mismatch')
            lr[d]+=fhex(row['real_lower_hex']); ur[d]+=fhex(row['real_upper_hex'])
            li[d]+=fhex(row['imag_lower_hex']); ui[d]+=fhex(row['imag_upper_hex'])
    if cursor!=ref['total_segments']: raise ValueError('incomplete coverage')
    if hpstreams!=1: raise ValueError('exactly one higher-power stream is required')
    if tc!=pc+hc: raise ValueError('global term-count mismatch')
    return ref,(lr,ur,li,ui),{'prime_count':pc,'higher_prime_power_count':hc,'total_terms':tc,'shards':len(items),'total_segments':cursor}

def freeze_from_boxes(coeff,bits:int):
    lr,ur,li,ui=coeff;K=len(lr)
    mid=np.array([complex(float((lr[d]+ur[d])/2),float((li[d]+ui[d])/2)) for d in range(K)],dtype=np.complex128)
    mid[0]=mid[0].real
    row=np.empty(K,dtype=np.complex128); row[0]=mid[0].real; row[1:]=0.5*mid[1:]
    matrix=toeplitz(np.conj(row),row); matrix=(matrix+matrix.conj().T)/2
    values,vectors=np.linalg.eigh(matrix); v=vectors[:,-1]
    pivot=int(np.argmax(np.abs(v))); v*=np.exp(-1j*np.angle(v[pivot]))
    if v[pivot].real<0: v=-v
    scale=1<<bits
    real=[int(round(float(z.real)*scale)) for z in v]
    imag=[int(round(float(z.imag)*scale)) for z in v]
    canonical={'imag_numerators':imag,'real_numerators':real,'scale_bits':bits}
    digest=canonical_sha(canonical)
    residual=float(np.max(np.abs(matrix@v-values[-1]*v)))
    return canonical,digest,float(values[-1]),residual,pivot

def autocorrelation(real:list[int],imag:list[int]):
    K=len(real); ar=[]; ai=[]
    for d in range(K):
        rr=ii=0
        for j in range(K-d):
            rr+=real[j+d]*real[j]+imag[j+d]*imag[j]
            ii+=imag[j+d]*real[j]-real[j+d]*imag[j]
        ar.append(rr); ai.append(ii)
    return ar,ai

def contract(coeff,vector):
    lr,ur,li,ui=coeff
    real=vector['real_numerators']; imag=vector['imag_numerators']; bits=vector['scale_bits']
    ar,ai=autocorrelation(real,imag); scale=Fraction(1,1<<(2*bits))
    lower=upper=Fraction(0)
    for d in range(len(real)):
        for box,value in [((lr[d],ur[d]),Fraction(ar[d])*scale),((li[d],ui[d]),-Fraction(ai[d])*scale)]:
            lo,hi=mul_interval_scalar(box,value); lower+=lo; upper+=hi
    return (lower,upper),ar,ai

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('shards',nargs='+',type=Path)
    parser.add_argument('--bits',type=int,default=96)
    parser.add_argument('--outdir',type=Path,required=True)
    args=parser.parse_args(); args.outdir.mkdir(parents=True,exist_ok=True)
    ref,coeff,counts=merge_shards(args.shards)
    if ref['cutoff']!=100000000000 or ref['carrier']!='4709203636353.65' or ref['cells']!=1024:
        raise ValueError('target parameter mismatch')
    expected={'prime_count':4118054813,'higher_prime_power_count':28156,'total_terms':4118082969}
    for key,value in expected.items():
        if counts[key]!=value: raise ValueError(f'{key} mismatch: {counts[key]} != {value}')
    vector,vector_digest,eigenvalue,residual,pivot=freeze_from_boxes(coeff,args.bits)
    prime,_,_=contract(coeff,vector)
    denominator=1<<args.bits
    norm=sum(Fraction(r,denominator)**2+Fraction(i,denominator)**2 for r,i in zip(vector['real_numerators'],vector['imag_numerators']))
    alpha=(
      Fraction(27316188863170422972141786876274838781565257086415513364963,1<<192),
      Fraction(27316188863170422972141786876274838781565257086415513364964,1<<192),
    )
    leading=(norm*alpha[0]-prime[1],norm*alpha[1]-prime[0])
    correction_per_unit=Fraction(136091541158257193750,292731105330133011007855861857)
    correction=norm*correction_per_unit
    full=(leading[0]-correction,leading[1]+correction)
    vector_doc={'schema':VECTOR_SCHEMA,'cells':1024,'cutoff':ref['cutoff'],'carrier':ref['carrier'],'vector':vector,'vector_sha256':vector_digest,'discovery':{'largest_midpoint_prime_eigenvalue':eigenvalue,'residual_inf_norm':residual,'pivot':pivot,'postselected_from_simultaneous_directed_boxes':True},'counts':counts}
    (args.outdir/'target-vector-b96.json').write_text(json.dumps(vector_doc,indent=2,sort_keys=True)+'\n')
    lags=[]
    for d in range(1024):
        lags.append({'lag':d,'real_interval':ij(coeff[0][d],coeff[1][d]),'imag_interval':ij(Fraction(0),Fraction(0)) if d==0 else ij(coeff[2][d],coeff[3][d])})
    boxes={'schema':BOX_SCHEMA,'cells':1024,'vector_sha256':vector_digest,'lags':lags,'counts':counts}
    (args.outdir/'target-merged-lag-boxes.json').write_text(json.dumps(boxes,indent=2,sort_keys=True)+'\n')
    verdict='CERTIFIED_POSITIVE_FIXED_VECTOR' if full[0]>0 else 'CERTIFIED_NEGATIVE_FIXED_VECTOR' if full[1]<0 else 'UNRESOLVED'
    certificate={'schema':FINAL_SCHEMA,'status':'DIRECTED_FIXED_VECTOR_INTERVAL','cutoff':ref['cutoff'],'carrier_exact':{'numerator':94184072727073,'denominator':20},'cells':1024,'precision_bits':ref['precision_bits'],'vector_sha256':vector_digest,'vector_norm_squared':fj(norm),'coverage':counts,'alpha_interval':ij(*alpha),'prime_rayleigh_interval':ij(*prime),'leading_interval':ij(*leading),'correction_radius_per_unit':fj(correction_per_unit),'correction_quadratic_radius':fj(correction),'full_interval':ij(*full),'certified_positive_fixed_vector':full[0]>0,'certified_negative_fixed_vector':full[1]<0,'verdict':verdict,'logical_boundary':'Exact finite interval composition. The RH implication of a negative value remains subject to independent D-0801 admissibility and Guinand-Weil normalization review.'}
    (args.outdir/'target-final-interval.json').write_text(json.dumps(certificate,indent=2,sort_keys=True)+'\n')
    summary={'vector_sha256':vector_digest,'largest_midpoint_prime_eigenvalue':eigenvalue,'residual_inf_norm':residual,'prime_interval_float':[float(prime[0]),float(prime[1])],'prime_interval_width':float(prime[1]-prime[0]),'alpha_interval_float':[float(alpha[0]),float(alpha[1])],'norm_squared_float':float(norm),'leading_interval_float':[float(leading[0]),float(leading[1])],'correction_radius_float':float(correction),'full_interval_float':[float(full[0]),float(full[1])],'verdict':verdict,'counts':counts}
    (args.outdir/'target-summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))
    if verdict=='UNRESOLVED': raise SystemExit(2)
if __name__=='__main__': main()

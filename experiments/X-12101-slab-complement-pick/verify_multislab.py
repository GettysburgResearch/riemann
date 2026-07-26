#!/usr/bin/env python3
"""Exact rational checker for polynomial multi-slab Pick localizers."""
from __future__ import annotations
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction
from typing import Any
from verify_slab_complement import (
    CertificateError,q,integer,text,Interval,QComplex,CInterval,ZERO,ONE,
    parse_points,parse_vector,parse_gates,ordinary_coefficients,contract_f,
    reciprocal_rectangle,phi_rectangle,classify,canonical_digest
)
SCHEMA='riemann.multislab-pick.v1'
VERIFY_SCHEMA='riemann.multislab-pick.verification.v1'

def poly_eval_complex(value:QComplex, slabs:list[tuple[Fraction,Fraction]])->QComplex:
    out=ONE
    for a,b in slabs:
        out=out.mul(value.add(QComplex(-a,0))).mul(value.add(QComplex(-b,0)))
    return out

def poly_interval(gamma:Interval, slabs:list[tuple[Fraction,Fraction]])->Interval:
    out=Interval.exact(Fraction(1))
    for a,b in slabs:
        out=out.mul(Interval(gamma.lo-a,gamma.hi-a))
        out=out.mul(Interval(gamma.lo-b,gamma.hi-b))
    return out

def complex_pow(value:QComplex,k:int)->QComplex:
    out=ONE
    for _ in range(k): out=out.mul(value)
    return out

def parse_slabs(payload:dict[str,Any]):
    raw=payload.get('slabs')
    if not isinstance(raw,list) or not raw: raise CertificateError('slabs must be a nonempty list')
    slabs=[]; gates=set(); ids=set(); expected={}
    for i,row in enumerate(raw):
        if not isinstance(row,dict): raise CertificateError(f'slabs[{i}] must be an object')
        sid=row.get('id'); cg=row.get('complete_gate_id'); eg=row.get('endpoint_gate_id')
        if not isinstance(sid,str) or not sid or sid in ids: raise CertificateError('invalid or duplicate slab id')
        if not isinstance(cg,str) or not cg or not isinstance(eg,str) or not eg: raise CertificateError(f'slab {sid!r} lacks gates')
        a=q(row.get('lower'),f'slabs[{i}].lower'); b=q(row.get('upper'),f'slabs[{i}].upper')
        count=integer(row.get('exact_zero_count'),f'slabs[{i}].exact_zero_count')
        if a>=b or count<=0: raise CertificateError(f'slab {sid!r} is invalid')
        slabs.append((sid,a,b,count,cg,eg)); gates|={cg,eg};ids.add(sid);expected[sid]=0
    slabs.sort(key=lambda x:(x[1],x[2],x[0]))
    for left,right in zip(slabs,slabs[1:]):
        if left[2]>=right[1]: raise CertificateError('slabs overlap or share an endpoint')
    raw_bins=payload.get('zero_bins')
    if not isinstance(raw_bins,list) or not raw_bins: raise CertificateError('zero_bins must be a nonempty list')
    bins=[]; bidset=set(); slabmap={s[0]:s for s in slabs}
    for i,row in enumerate(raw_bins):
        if not isinstance(row,dict): raise CertificateError(f'zero_bins[{i}] must be an object')
        bid=row.get('id'); sid=row.get('slab_id'); gid=row.get('gate_id')
        if not isinstance(bid,str) or not bid or bid in bidset: raise CertificateError('invalid or duplicate zero-bin id')
        if sid not in slabmap: raise CertificateError(f'zero bin {bid!r} uses unknown slab')
        if not isinstance(gid,str) or not gid: raise CertificateError(f'zero bin {bid!r} lacks gate')
        lo=q(row.get('lower'),f'zero_bins[{i}].lower'); hi=q(row.get('upper'),f'zero_bins[{i}].upper')
        count=integer(row.get('count'),f'zero_bins[{i}].count'); _,a,b,_,_,_=slabmap[sid]
        if count<=0 or not a<lo<=hi<b: raise CertificateError(f'zero bin {bid!r} is invalid or not strictly inside its slab')
        bins.append((bid,sid,Interval(lo,hi),count,gid)); bidset.add(bid);gates.add(gid);expected[sid]+=count
    for sid,a,b,count,_,_ in slabs:
        local=sorted([x for x in bins if x[1]==sid],key=lambda x:(x[2].lo,x[2].hi,x[0]))
        for left,right in zip(local,local[1:]):
            if left[2].hi>=right[2].lo: raise CertificateError(f'zero bins overlap in slab {sid!r}')
        if expected[sid]!=count: raise CertificateError(f'zero-bin multiplicities do not saturate slab {sid!r}')
    return slabs,bins,gates

def weighted_coefficients(points,vector,slab_pairs,origin):
    ws=[QComplex(p.z.re,p.z.im-origin) for p in points]
    shifted=[(a-origin,b-origin) for a,b in slab_pairs]; out=[]
    for point_i,value_i,w_i in zip(points,vector,ws):
        pminus=poly_eval_complex(QComplex(w_i.im,-w_i.re),shifted); inner=ZERO
        for value_j,w_j in zip(vector,ws): inner=inner.add(value_j.div(w_i.add(w_j.conj())))
        out.append(value_i.conj().mul(pminus).mul(inner))
    return out,ws

def check_moments(vector,ws,order):
    vals=[]
    for k in range(order):
        total=ZERO
        for value,w in zip(vector,ws): total=total.add(value.conj().mul(complex_pow(w,k)))
        vals.append(total)
        if total!=ZERO: raise CertificateError(f'vector moment k={k} does not vanish exactly')
    return vals

def claim(payload,key,interval):
    raw=payload.get(key)
    if raw is not None and Interval.parse(raw,key)!=interval: raise CertificateError(f'{key} mismatch')

def verify(payload):
    if not isinstance(payload,dict) or payload.get('schema')!=SCHEMA: raise CertificateError(f'schema must be {SCHEMA!r}')
    origin=q(payload.get('origin',0),'origin'); parent=payload.get('parent_gate_id')
    if not isinstance(parent,str) or not parent: raise CertificateError('parent_gate_id required')
    points,point_gates=parse_points(payload); vector=parse_vector(payload,len(points))
    slabs,bins,slab_gates=parse_slabs(payload); pairs=[(x[1],x[2]) for x in slabs]
    coeff,ws=weighted_coefficients(points,vector,pairs,origin); moments=check_moments(vector,ws,len(slabs))
    ordinary=contract_f(ordinary_coefficients(points,vector),points); weighted=contract_f(coeff,points)
    inside=Interval.exact(Fraction(0)); details=[]
    for bid,sid,gamma,count,_ in bins:
        p=poly_interval(gamma,pairs)
        if p.hi>0: raise CertificateError(f'bin {bid!r} does not lie in the nonpositive polynomial region')
        phi2=phi_rectangle(points,vector,gamma).modulus2(); contribution=p.mul(phi2).scale(Fraction(count)); inside=inside.add(contribution)
        details.append({'id':bid,'slab_id':sid,'count':count,'gamma':gamma.to_json(),'polynomial_weight':p.to_json(),'phi_modulus_squared':phi2.to_json(),'weighted_contribution':contribution.to_json()})
    residual=weighted.sub(inside); status,moat=classify(residual)
    claim(payload,'claimed_ordinary_pick',ordinary); claim(payload,'claimed_weighted_full',weighted); claim(payload,'claimed_inside_contribution',inside); claim(payload,'claimed_residual',residual)
    if payload.get('claimed_status') is not None and payload['claimed_status']!=status: raise CertificateError('claimed_status mismatch')
    used=point_gates|slab_gates|{parent}
    result={'schema':VERIFY_SCHEMA,'verified':True,'status':status,'strict_moat':text(moat),'origin':text(origin),'moment_order':len(slabs),'moments':[x.to_json() for x in moments],
    'ordinary_pick_interval':ordinary.to_json(),'weighted_full_interval':weighted.to_json(),'inside_contribution_interval':inside.to_json(),'multislab_residual_interval':residual.to_json(),
    'slabs':[{'id':sid,'lower':text(a),'upper':text(b),'exact_zero_count':count} for sid,a,b,count,_,_ in slabs],
    'point_count':len(points),'zero_bin_count':len(bins),'weighted_contracted_coefficients':[x.to_json() for x in coeff],'zero_bins':details,'manifest':parse_gates(payload,used),
    'interpretation':'Exact finite multi-slab contraction only; primitive F rectangles, complete slab counts, critical-line bins, and parent RH implication remain external gates.'}
    result['verification_sha256']=canonical_digest(result); return result

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('certificate',type=Path); ap.add_argument('--output',type=Path); args=ap.parse_args()
    try: data=json.loads(args.certificate.read_text()); result=verify(data); code=0
    except (OSError,json.JSONDecodeError,CertificateError) as exc: result={'schema':VERIFY_SCHEMA,'verified':False,'status':'REJECTED','reason':str(exc)}; code=2
    rendered=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: args.output.write_text(rendered)
    else: print(rendered,end='')
    return code
if __name__=='__main__': raise SystemExit(main())

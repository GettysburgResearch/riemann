#!/usr/bin/env python3
"""Convert a proof-grade X-9301 certificate into an X-9302 selected-factor certificate."""
from __future__ import annotations
import argparse, hashlib, json, string, sys
from fractions import Fraction
from pathlib import Path
from typing import Any
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)

INPUT_SCHEMA='riemann.xi-modulus-zero-deflation.v1'
OUTPUT_SCHEMA='riemann.xi-modulus-selected-factor-deflation.v1'
NORMALIZATION='riemann-xi-standard-half-s-sminus1-v1'

class AdapterError(ValueError): pass

def integer(x:Any,name:str)->int:
    if isinstance(x,bool) or not isinstance(x,int): raise AdapterError(f'{name} must be integer')
    return x

def rat(x:Any,name:str)->Fraction:
    if not isinstance(x,dict): raise AdapterError(f'{name} must be object')
    n=integer(x.get('numerator'),name+'.numerator'); d=integer(x.get('denominator'),name+'.denominator')
    if d<=0: raise AdapterError(f'{name}.denominator must be positive')
    return Fraction(n,d)

def fj(x:Fraction)->dict[str,int]: return {'numerator':x.numerator,'denominator':x.denominator}
def ij(lo:Fraction,hi:Fraction):
    if lo>hi: raise AdapterError('reversed interval')
    return {'lower':fj(lo),'upper':fj(hi)}
def sha(v:Any)->str: return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')).hexdigest()
def validate_sha(v:Any,name:str)->str:
    if not isinstance(v,str) or len(v)!=64 or any(c not in string.hexdigits for c in v): raise AdapterError(f'{name} bad sha')
    return v.lower()

def interval(x:Any,name:str)->tuple[Fraction,Fraction]:
    if not isinstance(x,dict): raise AdapterError(f'{name} must be object')
    lo=rat(x.get('lower'),name+'.lower'); hi=rat(x.get('upper'),name+'.upper')
    if lo>hi: raise AdapterError(f'{name} reversed')
    return lo,hi

def square_interval(lo:Fraction,hi:Fraction)->tuple[Fraction,Fraction]:
    upper=max(lo*lo,hi*hi)
    lower=Fraction(0) if lo<=0<=hi else min(lo*lo,hi*hi)
    return lower,upper

def modulus_square(rect:Any,name:str)->dict[str,dict[str,int]]:
    if not isinstance(rect,dict): raise AdapterError(f'{name} must be object')
    rlo,rhi=interval(rect.get('real'),name+'.real'); ilo,ihi=interval(rect.get('imag'),name+'.imag')
    rl,rh=square_interval(rlo,rhi); il,ih=square_interval(ilo,ihi)
    return ij(rl+il,rh+ih)

def adapt(data:dict[str,Any])->dict[str,Any]:
    if data.get('schema')!=INPUT_SCHEMA: raise AdapterError('input schema mismatch')
    if data.get('normalization_id')!=NORMALIZATION: raise AdapterError('normalization mismatch')
    classification=data.get('classification')
    if classification not in ('RIEMANN_XI_DIRECTED','SYNTHETIC_MODEL'): raise AdapterError('classification mismatch')
    ordinate=fj(rat(data.get('ordinate'),'ordinate'))
    log_terms=integer(data.get('log_terms',256),'log_terms')
    raw_points=data.get('points')
    if not isinstance(raw_points,list) or not raw_points: raise AdapterError('points missing')
    points=[]; ids=set()
    for k,p in enumerate(raw_points):
        if not isinstance(p,dict) or not isinstance(p.get('id'),str) or not p['id'] or p['id'] in ids: raise AdapterError('bad point')
        ids.add(p['id']); u=fj(rat(p.get('u'),f'point[{k}].u'))
        h=modulus_square(p.get('xi_rectangle'),f'point[{k}].xi_rectangle')
        canon={'id':p['id'],'u':u,'modulus_square_interval':h}
        points.append({**canon,'point_sha256':sha(canon)})
    raw_bins=data.get('zero_bins')
    if not isinstance(raw_bins,list) or not raw_bins: raise AdapterError('zero_bins missing')
    bins=[]
    for k,z in enumerate(raw_bins):
        if not isinstance(z,dict) or not isinstance(z.get('id'),str) or not z['id']: raise AdapterError('bad zero bin')
        gate=z.get('gate')
        if not isinstance(gate,dict):
            gate={'status':'CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND','sha256':z.get('gate_sha256')}
        validate_sha(gate.get('sha256'),f'zero[{k}].gate.sha256')
        bins.append({
            'id':z['id'],
            'lower_ordinate':fj(rat(z.get('lower_ordinate'),f'zero[{k}].lower')),
            'upper_ordinate':fj(rat(z.get('upper_ordinate'),f'zero[{k}].upper')),
            'count_lower':integer(z.get('count_lower'),f'zero[{k}].count'),
            'gate':{'status':gate.get('status'),'sha256':gate.get('sha256').lower()},
        })
    raw_rows=data.get('rows')
    if not isinstance(raw_rows,list) or not raw_rows: raise AdapterError('rows missing')
    rows=[]
    for k,r in enumerate(raw_rows):
        if not isinstance(r,dict) or not isinstance(r.get('id'),str) or not r['id']: raise AdapterError('bad row')
        kind=r.get('kind')
        if kind=='deflated-monotonicity':
            rows.append({'id':r['id'],'kind':'selected-factor-monotonicity','left':r.get('left'),'right':r.get('right')})
        elif kind=='deflated-cross-loewner-determinant':
            rows.append({'id':r['id'],'kind':'selected-factor-cross-loewner-determinant','rows':r.get('rows'),'columns':r.get('columns')})
        else: raise AdapterError(f'unsupported row kind at {k}')
    output={
        'schema':OUTPUT_SCHEMA,
        'classification':classification,
        'normalization_id':NORMALIZATION,
        'ordinate':ordinate,
        'log_terms':log_terms,
        'points':points,
        'selected_zero_bins':bins,
        'rows':rows,
        'source':{'x9301_certificate_sha256':sha(data),'adapter':'adapt_x9301_selected_factor.py'},
    }
    output['certificate_sha256']=sha(output)
    return output

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    try:
        data=json.loads(a.input.read_text()); result=adapt(data)
    except (OSError,json.JSONDecodeError,AdapterError) as e:
        print(json.dumps({'adapted':False,'error':str(e)},indent=2),file=sys.stderr);return 2
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'schema':result['schema'],'point_count':len(result['points']),'zero_bin_count':len(result['selected_zero_bins']),'row_count':len(result['rows']),'certificate_sha256':result['certificate_sha256']},indent=2,sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())

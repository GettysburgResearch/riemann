#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, itertools, json, math, string, sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any
if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)

SCHEMA='riemann.xi-modulus-selected-factor-deflation.v1'
NORMALIZATION='riemann-xi-standard-half-s-sminus1-v1'
PRODUCTION_GATE='CERTIFIED_CRITICAL_LINE_ZERO_LOWER_BOUND'
SYNTHETIC_GATE='SYNTHETIC_CRITICAL_LINE_ZERO_COUNT'

class CertificateError(ValueError): pass
@dataclass(frozen=True)
class Interval:
    lower: Fraction; upper: Fraction
    def __post_init__(self):
        if self.lower>self.upper: raise CertificateError('reversed interval')
    def add(self,o): return Interval(self.lower+o.lower,self.upper+o.upper)
    def sub(self,o): return Interval(self.lower-o.upper,self.upper-o.lower)
    def scale(self,c):
        a,b=self.lower*c,self.upper*c; return Interval(min(a,b),max(a,b))
    def mul(self,o):
        x=[self.lower*o.lower,self.lower*o.upper,self.upper*o.lower,self.upper*o.upper]
        return Interval(min(x),max(x))
    def pow_nonnegative(self,n):
        if n<0 or self.lower<0: raise CertificateError('bad nonnegative power')
        return Interval(self.lower**n,self.upper**n)

def exact_int(x,name):
    if isinstance(x,bool) or not isinstance(x,int): raise CertificateError(f'{name} must be integer')
    return x
def rat(x,name):
    if not isinstance(x,dict): raise CertificateError(f'{name} must be object')
    n=exact_int(x.get('numerator'),name+'.numerator'); d=exact_int(x.get('denominator'),name+'.denominator')
    if d<=0: raise CertificateError('nonpositive denominator')
    return Fraction(n,d)
def iv(x,name):
    if not isinstance(x,dict): raise CertificateError(f'{name} must be object')
    return Interval(rat(x.get('lower'),name+'.lower'),rat(x.get('upper'),name+'.upper'))
def fj(x): return {'numerator':x.numerator,'denominator':x.denominator}
def ij(x): return {'lower':fj(x.lower),'upper':fj(x.upper)}
def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode('ascii')).hexdigest()
def valid_sha(x,name):
    if not isinstance(x,str) or len(x)!=64 or any(c not in string.hexdigits for c in x): raise CertificateError(f'{name} bad sha')
    return x.lower()
def square(x:Interval):
    hi=max(x.lower*x.lower,x.upper*x.upper)
    lo=Fraction(0) if x.lower<=0<=x.upper else min(x.lower*x.lower,x.upper*x.upper)
    return Interval(lo,hi)

def _atanh_log(y:Fraction,terms:int):
    if not Fraction(1)<=y<=Fraction(2) or terms<8: raise CertificateError('log reduction')
    z=(y-1)/(y+1); z2=z*z; p=z; s=Fraction(0)
    for j in range(terms): s+=p/(2*j+1); p*=z2
    lo=2*s; tail=2*p/((2*terms+1)*(1-z2)); return Interval(lo,lo+tail)
def log_frac(x:Fraction,terms:int):
    if x<=0: raise CertificateError('log nonpositive')
    e=x.numerator.bit_length()-x.denominator.bit_length()
    pow2=lambda k: Fraction(1<<k,1) if k>=0 else Fraction(1,1<<(-k))
    y=x/pow2(e)
    while y<1: e-=1;y*=2
    while y>=2: e+=1;y/=2
    return _atanh_log(y,terms).add(_atanh_log(Fraction(2),terms).scale(Fraction(e)))
def log_iv(x:Interval,terms:int):
    if x.lower<=0: raise CertificateError('log interval touches zero')
    return Interval(log_frac(x.lower,terms).lower,log_frac(x.upper,terms).upper)
def det_iv(A):
    n=len(A)
    if n<1 or any(len(r)!=n for r in A): raise CertificateError('bad determinant')
    out=Interval(Fraction(0),Fraction(0))
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)); t=Interval(Fraction(1),Fraction(1))
        for i,j in enumerate(p): t=t.mul(A[i][j])
        out=out.add(t.scale(Fraction(-1 if inv%2 else 1)))
    return out
def status(x):
    if x.upper<0:return 'CERTIFIED_NEGATIVE'
    if x.lower>=0:return 'CERTIFIED_NONNEGATIVE'
    return 'UNRESOLVED'

def parse_points(data):
    out={}
    raw=data.get('points')
    if not isinstance(raw,list) or not raw: raise CertificateError('points missing')
    for k,p in enumerate(raw):
        if not isinstance(p,dict): raise CertificateError('bad point')
        i=p.get('id')
        if not isinstance(i,str) or not i or i in out: raise CertificateError('bad point id')
        u=rat(p.get('u'),f'point[{k}].u')
        h=iv(p.get('modulus_square_interval'),f'point[{k}].h')
        if u<=0 or h.lower<=0: raise CertificateError('point must be positive')
        canon={'id':i,'u':fj(u),'modulus_square_interval':ij(h)}; d=sha(canon)
        if p.get('point_sha256') is not None and valid_sha(p['point_sha256'],'point sha')!=d: raise CertificateError('point digest mismatch')
        out[i]={'u':u,'h':h,'sha':d}
    return out

def parse_factors(data,T,classification):
    raw=data.get('selected_zero_bins')
    if not isinstance(raw,list) or not raw: raise CertificateError('selected_zero_bins missing')
    out=[]
    expected=SYNTHETIC_GATE if classification=='SYNTHETIC_MODEL' else PRODUCTION_GATE
    for k,z in enumerate(raw):
        if not isinstance(z,dict): raise CertificateError('bad zero bin')
        i=z.get('id'); a=rat(z.get('lower_ordinate'),f'zero[{k}].lower'); b=rat(z.get('upper_ordinate'),f'zero[{k}].upper')
        m=exact_int(z.get('count_lower'),f'zero[{k}].count')
        if not isinstance(i,str) or not i or a>b or m<=0: raise CertificateError('bad zero bin fields')
        gate=z.get('gate')
        if not isinstance(gate,dict) or gate.get('status')!=expected: raise CertificateError('bad zero gate')
        gs=valid_sha(gate.get('sha256'),'gate sha')
        Y=square(Interval(T-b,T-a))
        out.append({'id':i,'a':a,'b':b,'m':m,'Y':Y,'gate_sha':gs})
    out.sort(key=lambda z:(z['a'],z['b'],z['id']))
    if len({z['id'] for z in out})!=len(out): raise CertificateError('duplicate zero id')
    for a,b in zip(out,out[1:]):
        if a['b']>=b['a']: raise CertificateError('zero bins overlap or touch')
    return out

def selected_log(point,factors,terms):
    g=log_iv(point['h'],terms); u=point['u']
    for z in factors:
        g=g.sub(log_iv(Interval(u+z['Y'].lower,u+z['Y'].upper),terms).scale(Fraction(z['m'])))
    return g

def factor_product(u,factors):
    p=Interval(Fraction(1),Fraction(1))
    for z in factors:
        p=p.mul(Interval(u+z['Y'].lower,u+z['Y'].upper).pow_nonnegative(z['m']))
    return p

def vand(nodes):
    p=Fraction(1)
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)): p*=nodes[j]-nodes[i]
    if p<=0: raise CertificateError('nodes not increasing')
    return p

def loewner(row_ids,col_ids,points,factors,terms):
    n=len(row_ids)
    if n<1 or n>4 or len(col_ids)!=n: raise CertificateError('order 1..4')
    if len(set(row_ids))!=n or len(set(col_ids))!=n or set(row_ids)&set(col_ids): raise CertificateError('Loewner node collision')
    try: rn=[points[i]['u'] for i in row_ids]; cn=[points[i]['u'] for i in col_ids]
    except KeyError as e: raise CertificateError('unknown point') from e
    rv=vand(rn); cv=vand(cn)
    vals={i:selected_log(points[i],factors,terms) for i in row_ids+col_ids}
    A=[]
    for i in row_ids:
        row=[]
        for j in col_ids:
            row.append(vals[i].sub(vals[j]).scale(Fraction(1,1)/(points[i]['u']-points[j]['u'])))
        A.append(row)
    raw=det_iv(A); normal=raw.scale(Fraction(1,1)/(rv*cv))
    return raw,normal,rv,cv

def verify(data):
    if data.get('schema')!=SCHEMA or data.get('normalization_id')!=NORMALIZATION: raise CertificateError('schema/normalization')
    classification=data.get('classification')
    if classification not in ('SYNTHETIC_MODEL','RIEMANN_XI_DIRECTED'): raise CertificateError('classification')
    T=rat(data.get('ordinate'),'ordinate'); terms=exact_int(data.get('log_terms',256),'log_terms')
    if not 32<=terms<=4096: raise CertificateError('log_terms')
    points=parse_points(data); factors=parse_factors(data,T,classification)
    rows=data.get('rows')
    if not isinstance(rows,list) or not rows: raise CertificateError('rows missing')
    out=[]; seen=set()
    for r in rows:
        if not isinstance(r,dict): raise CertificateError('bad row')
        i=r.get('id'); kind=r.get('kind')
        if not isinstance(i,str) or not i or i in seen: raise CertificateError('bad row id')
        seen.add(i)
        if kind=='selected-factor-monotonicity':
            l,rid=r.get('left'),r.get('right')
            if l not in points or rid not in points or not points[l]['u']<points[rid]['u']: raise CertificateError('bad monotonicity')
            lp=factor_product(points[l]['u'],factors); rp=factor_product(points[rid]['u'],factors)
            value=points[rid]['h'].mul(lp).sub(points[l]['h'].mul(rp))
            rec={'id':i,'kind':kind,'left':l,'right':rid,'interval':ij(value),'status':status(value)}
        elif kind=='selected-factor-cross-loewner-determinant':
            rr,cc=r.get('rows'),r.get('columns')
            if not isinstance(rr,list) or not isinstance(cc,list): raise CertificateError('bad Loewner lists')
            raw,norm,rv,cv=loewner(rr,cc,points,factors,terms)
            rec={'id':i,'kind':kind,'rows':rr,'columns':cc,'order':len(rr),'raw_interval':ij(raw),'vandermonde_normalized_interval':ij(norm),'row_vandermonde':fj(rv),'column_vandermonde':fj(cv),'status':status(norm)}
        else: raise CertificateError('unsupported row kind')
        out.append(rec)
    neg=[r for r in out if r['status']=='CERTIFIED_NEGATIVE']; unresolved=[r for r in out if r['status']=='UNRESOLVED']
    verdict='NEGATIVE_SELECTED_FACTOR_XI_MODULUS_WITNESS_PENDING_REVIEW' if classification=='RIEMANN_XI_DIRECTED' and neg else 'SYNTHETIC_SELECTED_FACTOR_SEPARATION' if classification=='SYNTHETIC_MODEL' and neg else 'UNRESOLVED' if unresolved else 'NO_NEGATIVE_IN_DECLARED_ROWS'
    return {'schema':SCHEMA,'classification':classification,'normalization_id':NORMALIZATION,'ordinate':fj(T),'point_count':len(points),'selected_factor_count_lower':sum(z['m'] for z in factors),'selected_zero_bins':[{'id':z['id'],'lower_ordinate':fj(z['a']),'upper_ordinate':fj(z['b']),'count_lower':z['m'],'distance_square_interval':ij(z['Y']),'gate_sha256':z['gate_sha']} for z in factors],'rows':out,'certified_negative_rows':len(neg),'unresolved_rows':len(unresolved),'verdict':verdict,'scope_warning':'Exact rational interval contraction only; production acceptance additionally requires proof-grade completed-xi rectangles, valid critical-line zero gates, and independent review of L-9304/L-9305.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
    try: result=verify(json.loads(a.certificate.read_text()))
    except (OSError,json.JSONDecodeError,CertificateError,ZeroDivisionError) as e:
        print(json.dumps({'verified':False,'error':str(e)},indent=2),file=sys.stderr);return 2
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text)
    print(text,end='');return 1 if result['verdict']=='UNRESOLVED' else 0
if __name__=='__main__':raise SystemExit(main())

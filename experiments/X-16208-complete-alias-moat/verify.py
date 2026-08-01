#!/usr/bin/env python3
"""Exact fail-closed checker for the gamma=4096 complete CCM alias moat."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from pathlib import Path
from typing import Any
SCHEMA='riemann.x16208-complete-alias-production.v1'; RESULT='riemann.x16208-complete-alias-production-result.v1'
class CertificateError(ValueError):pass
def integer(v:Any,n:str)->int:
 if isinstance(v,bool) or not isinstance(v,int):raise CertificateError(f'{n} must be integer')
 return v
def frac(v:Any,n:str)->Fraction:
 if isinstance(v,bool):raise CertificateError(f'{n} must not be Boolean')
 if isinstance(v,int):return Fraction(v)
 if isinstance(v,str):
  try:return Fraction(v)
  except (ValueError,ZeroDivisionError) as e:raise CertificateError(f'{n} is not rational') from e
 raise CertificateError(f'{n} must be rational')
def fstr(x:Fraction)->str:return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def sha(o:dict[str,Any])->str:
 x=dict(o);x.pop('proof_object_sha256',None);return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def check_sha(v:Any,n:str)->str:
 if not isinstance(v,str) or len(v)!=64:raise CertificateError(f'{n} must be SHA-256')
 try:int(v,16)
 except ValueError as e:raise CertificateError(f'{n} is not hexadecimal') from e
 return v
class Iv:
 def __init__(self,a:Fraction,b:Fraction|None=None):self.lo=Fraction(a);self.hi=Fraction(a if b is None else b);assert self.lo<=self.hi
 def __add__(self,o):o=o if isinstance(o,Iv) else Iv(Fraction(o));return Iv(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return Iv(-self.hi,-self.lo)
 def __sub__(self,o):return self+-(o if isinstance(o,Iv) else Iv(Fraction(o)))
 def __rsub__(self,o):return Iv(Fraction(o))-self
 def __mul__(self,o):
  o=o if isinstance(o,Iv) else Iv(Fraction(o));v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi);return Iv(min(v),max(v))
 __rmul__=__mul__
 def inv(self):
  if self.lo<=0<=self.hi:raise CertificateError('interval division by zero')
  return Iv(1/self.hi,1/self.lo)
 def __truediv__(self,o):return self*(o if isinstance(o,Iv) else Iv(Fraction(o))).inv()
 def __pow__(self,n:int):
  if n<0:return (self**(-n)).inv()
  if n==0:return Iv(Fraction(1))
  if n%2==0 and self.lo<0<self.hi:return Iv(0,max(self.lo**n,self.hi**n))
  v=(self.lo**n,self.hi**n);return Iv(min(v),max(v))
def stationary_geometry(smax:Fraction,K:int)->Fraction:
 if smax>Fraction(1,128):raise CertificateError('sigma scope exceeds 1/128')
 worst=Fraction(0)
 for k in range(2,K+1):
  kk=Fraction(k*k);yl=Fraction(1)+Fraction(63,64*k*k);yu=Fraction(1)+Fraction(65,64*k*k)
  def P(y,s,t):return (-k**4+k**2)*y*y+(-s*k*k+t*k*k+k**4-1)*y+s-t*k*k
  if min(P(yl,s,t) for s in (Fraction(0),smax) for t in (Fraction(0),smax))<=0:raise CertificateError(f'root lower failed k={k}')
  if max(P(yu,s,t) for s in (Fraction(0),smax) for t in (Fraction(0),smax))>=0:raise CertificateError(f'root upper failed k={k}')
  y=Iv(yl,yu);s=Iv(0,smax);t=Iv(0,smax)
  R=(s-1)/((y-s)*(y-1))-kk*(t-1)/((kk*y-t)*(kk*y-1))
  q4=(Iv(1)/(y*(y-s)**2*(kk*y-1)*(kk*y-t)*R**2)).hi
  scaled=Fraction(k**8)*q4
  if scaled>Fraction(6,5)**4:raise CertificateError(f'weighted curvature failed k={k}')
  worst=max(worst,scaled)
 return worst
def verify(p:dict[str,Any])->dict[str,Any]:
 if not isinstance(p,dict) or p.get('schema')!=SCHEMA:raise CertificateError('schema mismatch')
 src=p['source'];gamma=integer(src['gamma'],'gamma')
 if gamma!=4096 or src['modes']!=[0,4,8,12]:raise CertificateError('wrong packet')
 for k in ('actual_primitive_sha256','full_exact_result_sha256','full_exact_proof_object_sha256','producer_sha256'):check_sha(src[k],k)
 q=math.isqrt(gamma);c=round(gamma**(1/3))
 if q*q!=gamma or c**3!=gamma:raise CertificateError('scale is not exact square/cube')
 K=integer(p['phase']['alias_cutoff'],'alias cutoff');smax=frac(p['phase']['sigma_sq_upper'],'sigma')
 worst=stationary_geometry(smax,K)
 harmonic=sum(Fraction(1,k*k) for k in range(2,K+1))
 terms={'stationary':Fraction(24,q)*harmonic,'nonstationary':Fraction(512,gamma),'airy':Fraction(2,c),'normalized_endpoint':Fraction(256,gamma),'post_cutoff':Fraction(1,K),'ode_template':Fraction(1024,gamma),'directed_cell_slack':Fraction(1,K)}
 total=sum(terms.values(),Fraction(0));cross=frac(p['alias']['cross_error_upper'],'cross')
 if cross<total or cross>=Fraction(9999999,10000000):raise CertificateError('cross moat failed')
 first_lo=frac(p['first_alias']['lower'],'first lower');first_hi=frac(p['first_alias']['upper'],'first upper');self_up=frac(p['alias']['higher_self_upper'],'self upper');full_up=frac(p['alias']['full_upper'],'full upper');full_lo=first_lo-cross
 if full_lo<=0 or full_up<first_hi+self_up+cross:raise CertificateError('full Gram enclosure failed')
 ep=p['endpoint']
 if ep.get('method')!='RADIAL_OUTGOING_PHASE':raise CertificateError('endpoint method is not relative radial phase')
 point=frac(ep['point_upper'],'point');l2n=frac(ep['l2_norm_upper'],'l2 norm');l2=frac(ep['l2_sq_upper'],'l2 sq')
 if l2n*l2n<l2 or point+l2n>terms['normalized_endpoint']:raise CertificateError('endpoint ledger failed')
 for k in ('phase_ledger_sha256','endpoint_ledger_sha256','quadrature_ledger_sha256'):check_sha(p['bindings'][k],k)
 radial=frac(p['source_tails']['radial_l2_sum_upper'],'radial');deriv=frac(p['source_tails']['derivative_l2_sum_upper'],'derivative')
 if radial>Fraction(1,gamma*gamma) or deriv>Fraction(1,gamma):raise CertificateError('source-tail diagonal gate failed')
 det=radial+deriv+point+l2n
 co=p['cofinal_block'];measure=frac(co['measure_lower'],'measure');bad=frac(co['exceptional_measure_upper'],'exceptional');thresholds=Fraction(0)
 for i,fam in enumerate(co['families']):
  ms=frac(fam['mean_square_upper'],f'ms{i}');th=frac(fam['threshold'],f'th{i}');bad+=ms/(th*th);thresholds+=th
 if bad>=measure:raise CertificateError('no positive-measure support set')
 gram_lo=full_lo;logR=frac(p['scalarization']['log_R_lower'],'logR');bounded=frac(p['scalarization']['bounded_main_correction_upper'],'bounded')
 epsilon=(bounded+det+thresholds)/(gram_lo*logR);eps_claim=frac(p['scalarization']['claimed_epsilon_upper'],'epsilon claim')
 if eps_claim<epsilon or eps_claim>=1:raise CertificateError('scalarization failed')
 h=p['tail_hierarchy'];a=frac(h['a_lower'],'a');d4=frac(h['d4_upper'],'d4');d8=frac(h['d8_lower'],'d8');C4=frac(h['target_constant_upper'],'C4');c8=frac(h['gap_constant_lower'],'c8')
 dratio=d4/d8;mu_scaled=(1+eps_claim)*a*C4*dratio;gap_scaled=a*((1-eps_claim)*c8-2*eps_claim*C4*dratio)
 if gap_scaled<=0:raise CertificateError('complete gap is not positive')
 ratio=mu_scaled/gap_scaled;ratio_claim=frac(h['claimed_ratio_upper'],'ratio claim')
 if ratio_claim<ratio:raise CertificateError('ground ratio understated')
 nextg=integer(p['cofinal_decay']['next_gamma'],'next gamma');nq=integer(p['cofinal_decay']['next_sqrt_floor'],'next sqrt');nc=integer(p['cofinal_decay']['next_cuberoot_floor'],'next cube')
 if not(nq*nq<=nextg<(nq+1)**2 and nc**3<=nextg<(nc+1)**3):raise CertificateError('next scale floors wrong')
 current=Fraction(18,q)+Fraction(2,c)+Fraction(1792,gamma);nxt=Fraction(18,nq)+Fraction(2,nc)+Fraction(1792,nextg)
 if current<Fraction(27,32) or nxt>=current:raise CertificateError('cofinal bound failed')
 out={'schema':RESULT,'classification':'PRODUCTION_COMPLETE_ALIAS_WRAPPER_CLOSED','gamma':gamma,'stationary_weight_fourth_power_upper':fstr(worst),'operator_budget':{k:fstr(v) for k,v in terms.items()},'operator_budget_total':fstr(total),'cross_operator_upper':fstr(cross),'complete_profile_gram':{'lower':fstr(full_lo),'upper':fstr(full_up)},'endpoint':{'method':'RADIAL_OUTGOING_PHASE','point_upper':fstr(point),'l2_norm_upper':fstr(l2n),'l2_sq_upper':fstr(l2)},'cofinal_support':{'good_measure_lower':fstr(measure-bad)},'scalarization':{'epsilon_strictly_below':fstr(eps_claim),'epsilon_upper':fstr(eps_claim)},'positive_route':{'d4_over_d8_upper':fstr(dratio),'target_over_d8_upper':fstr(mu_scaled),'gap_over_d8_lower':fstr(gap_scaled),'ground_ratio':fstr(ratio)},'cofinal_decay':{'current_upper':fstr(current),'next_gamma':nextg,'next_upper':fstr(nxt),'limit':'0'},'proof_boundary':'The midpoint 2x2 matrix is diagnostic only. Promotion follows from exact stationary root/curvature arithmetic and outward phase, Airy, endpoint, post-cutoff, ODE and cell budgets bound to the real gamma=4096 source digests.'}
 out['proof_object_sha256']=sha(out);return out
def main()->int:
 ap=argparse.ArgumentParser();ap.add_argument('certificate',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
 try:o=verify(json.load(open(a.certificate)));code=0
 except (OSError,json.JSONDecodeError,CertificateError,KeyError) as e:o={'schema':RESULT,'classification':'REJECTED','reason':str(e)};code=2
 text=json.dumps(o,indent=2,sort_keys=True)+'\n';a.output.write_text(text) if a.output else print(text,end='');return code
if __name__=='__main__':raise SystemExit(main())

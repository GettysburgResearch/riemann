#!/usr/bin/env python3
"""Authenticate this packet; reconstruct bounded algebra and optional whole phase.
--full is the actual primitive phase replay. Without it, no new phase is computed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
import argparse,copy,hashlib,json,sys
import ball_core as bc
import certify
ROOT=Path(__file__).resolve().parent

def require(ok,message):
 if not ok:raise ValueError(message)

def pairs(p):
 out={}
 for k,v in p:
  require(k not in out,'duplicate JSON key: '+k);out[k]=v
 return out

def read_json(p):return json.loads(Path(p).read_text(),object_pairs_hook=pairs,parse_constant=lambda v:(_ for _ in ()).throw(ValueError('nonfinite JSON')))
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def compare(actual,expected):require(canon(actual)==canon(expected),'receipt differs from reconstruction')

def authenticate():
 entries=read_json(ROOT/'SHA256.json')
 actual=set()
 for p in ROOT.iterdir():
  if p.name=='__pycache__':continue
  require(not p.is_symlink() and p.is_file(),'nonregular packet member: '+p.name)
  actual.add(p.name)
 require(actual==set(entries)|{'SHA256.json'},'packet file inventory mismatch')
 for name,digest in entries.items():
  require('/' not in name and '\\' not in name,'manifest path contract')
  require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'hash mismatch: '+name)
 return len(entries)

def contains(b,z):
 return abs(F(b.a,bc.Q)-z[0])+abs(F(b.b,bc.Q)-z[1])<=F(b.e,bc.Q)
def gauss_mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def gauss_inv(z):
 den=z[0]*z[0]+z[1]*z[1];return (z[0]/den,-z[1]/den)
def a(n):return F(1) if n==0 else F(1-F(1,2**(2*n-1)),2*n-1)

def controls():
 counts={};operations=0
 for k in range(1,21):
  z=(F(k,7),F(3-k,11));w=(F(2*k+1,13),F(k+2,17));dz=F(1,1000);dw=F(1,1300)
  zb=bc.B.complex(*z).grow(bc.rad(dz));wb=bc.B.complex(*w).grow(bc.rad(dw))
  zv=[(z[0]+dx,z[1]+dy) for dx,dy in [(dz,0),(-dz,0),(0,dz),(0,-dz)]]
  wv=[(w[0]+dx,w[1]+dy) for dx,dy in [(dw,0),(-dw,0),(0,dw),(0,-dw)]]
  for zz in zv:
   require(contains(zb.inv(),gauss_inv(zz)),'reciprocal enclosure');operations+=1
   for ww in wv:
    require(contains(zb*wb,gauss_mul(zz,ww)),'product enclosure');operations+=1
    require(contains(zb+wb,(zz[0]+ww[0],zz[1]+ww[1])),'sum enclosure');operations+=1
 counts['Gaussian_rational_enclosures']=operations
 N=24
 ff=[F((-6)**k,factorial(2*k+1)) for k in range(N+2)];x=[F(1)]
 for n in range(1,N+2):x.append(-sum((ff[k]*x[n-k] for k in range(1,n+1)),F(0)))
 bb=bc.bernoulli(2*(N+1))
 for n in range(N+2):
  alt=(-1)**n*2*(1-F(2)**(2*n-1))*bb[2*n]*6**n/factorial(2*n)
  require(x[n]==alt,'independent Bernoulli/source identity')
 counts['source_moments_two_formulas']=N+2
 mode_cases=0;mode_coeff=[]
 for m in range(13):
  pp=[F(1)]
  for j in range(1,N+1):
   b=a(m+j)/a(m)
   pp.append(b/(1-b)*sum((pp[k]*x[j-k] for k in range(j)),F(0)))
  for j in range(N-m+1):
   left=2*a(m+j)*sum((pp[k]*x[j-k] for k in range(j+1)),F(0))
   require(left==2*a(m)*pp[j],'renormalization eigenmode identity');mode_cases+=1
  if m==0:require(pp==x[:N+1],'zeroth mode')
  if m==1:
   for j in range(N+1):require(pp[j]==(j+1)*x[j+1],'neutral size-bias identity')
  if m==2:
   for j in range(N+1):
    hh=sum((pp[k]*x[j-k] for k in range(j+1)),F(0))
    require((2*j+3)*pp[j]==F(24,7)*(1-F(1,8*4**j))*hh,'delay identity')
    require(pp[j]<=j+1 and hh<=F((j+1)*(j+2),2),'majorants')
  mode_coeff.append([str(v) for v in pp])
 counts['native_mode_coefficients']=mode_cases;counts['neutral_coefficients']=N+1;counts['delay_coefficients']=N+1;counts['majorant_checks']=2*(N+1)
 special=0
 for z,target in [(bc.B.real(1),bc.ZERO),(bc.B.real(5),bc.logpos(F(24))),(bc.B.real(F(1,2)),bc.clog(bc.PI)/2)]:
  diff=bc.loggamma(z)-target
  require(abs(diff.a)+abs(diff.b)<=diff.e,'gamma exact special value');special+=1
 for z in [bc.B.complex(F(17,20),F(-119,4)),bc.B.complex(F(13,20),F(-119,4)),bc.B.complex(3,2)]:
  diff=bc.loggamma(z+1)-bc.loggamma(z)-bc.clog(z)
  require(abs(diff.a)+abs(diff.b)<=diff.e,'gamma recurrence');special+=1
  diff=bc.exp(bc.clog(z))-z
  require(abs(diff.a)+abs(diff.b)<=diff.e,'exp-log identity');special+=1
 counts['elementary_function_identity_controls']=special
 counts['mode_coefficient_digest']=hashlib.sha256(canon(mode_coeff)).hexdigest()
 return counts

def check_contract(d):
 require(type(d) is dict,'receipt object')
 require(d['status']=='PROPOSED_DIRECTED_NATIVE_PHASE_REFUTATION','status')
 require(d['rh_proved'] is False and d['off_line_zeta_zero_claimed'] is False,'claim boundary')
 for key,value in {'bits':512,'degree':80,'origin_degree':384,'endpoint':512,'cells':4092}.items():require(type(d[key]) is int and d[key]==value,key)
 require(d['point']=={'x':'119/2','y':'1/5'} and d['step']=='1/8','source point/coverage')
 require(d['positive_scale']=='exp(119*pi/8) for A and B','scale')
 p=d['phase_scaled'];require(type(p['im_num']) is str and type(p['radius_num']) is str,'integer serialization')
 b,e=int(p['im_num']),int(p['radius_num']);require(e>=0,'negative radius')
 require(-4700000*bc.Q<b-e and b+e<-4600000*bc.Q,'strict complete phase bound')
 require(d['strict_negative'] is True and d['coarse_phase_interval']==['-4700000','-4600000'],'verdict')

def mutation_tests(expected):
 variants=[]
 def add(fn):
  d=copy.deepcopy(expected);fn(d);variants.append(d)
 add(lambda d:d.update(rh_proved=True));add(lambda d:d.update(off_line_zeta_zero_claimed=True))
 add(lambda d:d.update(cells=4091));add(lambda d:d.update(bits=True));add(lambda d:d.update(tail_K='0'))
 add(lambda d:d['phase_scaled'].update(im_num=str(-int(d['phase_scaled']['im_num']))))
 add(lambda d:d['A_scaled'].update(re_num=str(int(d['A_scaled']['re_num'])+1)))
 add(lambda d:d['point'].update(y='0'))
 count=0
 for d in variants:
  try:check_contract(d);compare(d,expected)
  except (ValueError,KeyError):count+=1
  else:raise ValueError('accepted altered receipt')
 try:json.loads('{"a":1,"a":2}',object_pairs_hook=pairs)
 except ValueError:count+=1
 else:raise ValueError('accepted duplicate JSON key')
 return count

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--full',action='store_true');ap.add_argument('--self-test',action='store_true');ap.add_argument('--receipt',type=Path,default=ROOT/'result.json');args=ap.parse_args()
 files=authenticate();expected=read_json(args.receipt);check_contract(expected);bounded=controls()
 if args.full:
  computed=certify.compute(progress=0);check_contract(computed);compare(computed,expected)
  print('PASS_COMPLETE_NATIVE_PHASE_REPLAY',hashlib.sha256(canon(computed)).hexdigest(),flush=True)
 else:print('BOUNDED_CHECK_ONLY_NO_NEW_PHASE_REPLAY',flush=True)
 refused=mutation_tests(expected) if args.self_test else 0
 print(json.dumps({'authenticated_hashes':files,'controls':bounded,'altered_receipts_refused':refused,'full_replay':args.full},sort_keys=True),flush=True)
if __name__=='__main__':
 try:main()
 except (ValueError,KeyError,ArithmeticError,OSError) as e:print('REJECT',str(e),file=sys.stderr);raise SystemExit(1)

"""Independent exact-rational first-window majorant/close-pair component check.
Uses stronger Taylor orders and Machin pi bounds, not author verifier helpers.
Ordinary analytic justification is in audits/adversarial_reviews/839_majorant_reconstruction.md.
"""
from pathlib import Path
from fractions import Fraction as F
import json,math,hashlib,struct,time
B=Path(__file__).resolve().parents[2];start=time.monotonic();D=B/'experiments/inputs/839_first_window'
raw=(D/'inputs.json').read_bytes();p=json.loads(raw);aa=[193305,-23105,29166,13952,-21009,41052];assert p['window_coefficients']==aa and p['denominator']==10**6
coef=[F(a,10**6) for a in aa];theta=F(17,20);gamma=F(607,1000);assert F(p['separation'])==theta and F(p['majorant_gamma'])==gamma
break_text='1/128,1/64,3/128,1/32,3/64,1/16,5/64,3/32,1/8,9/64,5/32,11/64,3/16,7/32,1/4,9/32,19/64,5/16,41/128,21/64,11/32,23/64,3/8,13/32,7/16,29/64,15/32,61/128,31/64,125/256,63/128,253/512,127/256,509/1024,255/512,1021/2048,511/1024,2045/4096,1023/2048,2047/4096,4095/8192,1/2'
breaks=[F(0)]+[F(x) for x in break_text.split(',')];assert len(breaks)==43 and all(x<y for x,y in zip(breaks,breaks[1:]))
def atan(q,n):
 s=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));t=s+F((-1)**n,(2*n+1)*q**(2*n+1));return min(s,t),max(s,t)
a,b=atan(5,100);c,d=atan(239,40);lo,hi=16*a-4*d,16*b-4*c;P=10**55;piL=F((P*lo).__floor__(),P);piU=F((P*hi).__floor__()+1,P);piQ=F(355,113);pe=max(abs(piQ-piL),abs(piQ-piU))
def poly(x,n,sinc=False):
 term=F(1);s=term
 for k in range(1,n):
  term=-term*x*x/F((2*k)*(2*k+1) if sinc else (2*k-1)*(2*k));s+=term
 return s
cells=[]
for l,r in zip(breaks,breaks[1:]):
 mid=(l+r)/2;delta=(r-l)/2;fup=F(1)
 for j,a in enumerate(coef,1):
  v=j*mid;k=(v+F(1,2)).__floor__();red=v-k;z=2*piQ*red;err=2*piU*j*delta+2*pe*abs(red)
  fup+=a*(poly(z,19)+err if a>=0 else poly(z,18)-err)
 slow=F(0)
 for shift in [F(-1,2),F(1,2)]:
  z=piQ*theta*(mid+shift);assert abs(z)<3
  err=(piU*theta*delta+pe*theta*abs(mid+shift))/2
  slow+=poly(z,18,True)-err
 assert slow>0;slack=gamma*slow*slow-fup;assert slack>=0
 cells.append({'left':str(l),'right':str(r),'slack':str(slack)})
sinc_upper=poly(piQ*theta,19,True)+pe*theta/2;lam_upper=2*gamma/theta*(1+sinc_upper);assert lam_upper<=F(16711,10000)<F(67,40)
rawtab=(D/'kernel_lower.bin').read_bytes();table_hash=hashlib.sha256(rawtab).hexdigest();assert table_hash=='b80e5a8c70e4beb3b872dada426016bc97b0954c1a8a5eabaeb40fba49cded36';assert len(rawtab)==4*209010;assert(p['grid'],p['scale'],p['R'])==(16384,2**28,209009);assert F(p['clip_c'])==F(67,20);tab=struct.unpack('<'+'I'*(len(rawtab)//4),rawtab);H=p['grid'];V=p['scale'];last=(theta*H).__floor__();minimum=min(tab[:last+1]);beta=F(8824337,134217728);assert F(minimum,V)>=beta
# 2+2sqrt(beta)<c is equivalent to4beta<(c-2)^2 withc>2.
cclip=F(67,20);assert cclip>2 and 4*beta<(cclip-2)**2
x,y=F(p['x']),F(p['y']);assert 2*beta>2*x and 4*beta>x+y and 8*beta>2*y
cache=B/'sources/formal_round2/839-v1/lean/Distinct839/Majorant/Pointwise.lean'
source_hash=None
if cache.exists():
 import re
 text=cache.read_text();m=re.search(r'def majorantBreaks[^=]*:=\s*\[([^\]]+)\]',text,re.S);assert m
 assert [F(v.strip()) for v in m.group(1).split(',')]==breaks[1:];source_hash=hashlib.sha256(cache.read_bytes()).hexdigest()
out={'kind':'independent_exact_first_window_majorant_closepair_components','source_commit':'0e961ea199b425010843bc8044676d4ad29fe031','input_sha256':hashlib.sha256(raw).hexdigest(),'kernel_table_sha256':table_hash,'source_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_pointwise_lean_sha256':source_hash,'majorant_closed_intervals':len(cells),'all_cells_pass':True,'minimum_certificate_slack':str(min(F(r['slack']) for r in cells)),'breakpoints':[str(t) for t in breaks],'lambda_upper':str(lam_upper),'lambda_upper_below_c_half':True,'source_LMajBound':'16711/10000','lambda_upper_below_source_LMajBound':True,'c_half':'67/40','closepair_cells':last+1,'minimum_table_integer':minimum,'table_scale':V,'beta':str(beta),'closepair_beta_pass':True,'clip_condition_pass':True,'reward_conditions_pass':True,'elapsed_seconds':time.monotonic()-start,'scope':'Component validation of f<=g on[-1/2,1/2], majorant integral bound, and close-pair constants conditional on previously independently validated kernel-table cells; not a full zeta theorem or Lean build.'}
(B/'experiments/results/839_majorant_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['breakpoints','lambda_upper','minimum_certificate_slack']},indent=2))

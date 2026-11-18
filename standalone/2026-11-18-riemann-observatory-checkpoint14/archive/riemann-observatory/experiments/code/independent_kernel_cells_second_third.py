"""Independent second/third-window exact kernel checks; shares trig enclosures.
Uses the same parent-reviewed analytic bounds as independent_kernel_cells.py.
No first-window rerun. Defaults to bundled MIT-licensed frozen data; no network.
"""
from fractions import Fraction as F
from pathlib import Path
import sys,math,struct,json,time,hashlib
start=time.monotonic();archive_root=Path(__file__).resolve().parents[2];H=16384;V=2**28
# Machin: pi=16 atan(1/5)-4 atan(1/239); alternating next-term enclosures.
def atan_interval(q,n):
 a=sum((F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(n)),F(0));b=a+F((-1)**n,(2*n+1)*q**(2*n+1));return min(a,b),max(a,b)
a,b=atan_interval(5,100);c,d=atan_interval(239,40);piL,piU=16*a-4*d,16*b-4*c
unit=10**55;piL=F((piL*unit).__floor__(),unit);piU=F((piU*unit).__floor__()+1,unit)
assert F(3)<piL<piU<F(22,7)
Q=2**100
def down(x):return F((x*Q).__floor__(),Q)
def up(x):return F((x*Q).__floor__()+1,Q)
# Alternate Taylor truncations; omitted tails after term18 decrease on[0,pi/2].
# The first two cosine terms need not decrease, which does not affect the tail bound.
# Even n truncation ends negative; odd n ends positive.
def sincos_sum(x,n,sin):
 first=x if sin else F(1);total=first;term=first
 for k in range(1,n):
  den=(2*k)*(2*k+1) if sin else (2*k-1)*(2*k)
  term=-term*x*x/den;total+=term
 return total
trig=[]
for j in range(H//2):
 a=F(2*j+1,2*H);xl,xu=piL*a,piU*a;assert xu<piL/2
 sl=sincos_sum(xl,18,True)/piU;su=sincos_sum(xu,19,True)/piL
 cl=sincos_sum(xu,18,False);cu=sincos_sum(xl,19,False)
 assert 0<sl<su and 0<cl<cu;trig.append((down(sl),up(su),down(cl),up(cu)))
def check_data(label,expected_coeffs,expected_sha):
 data=archive_root/f'experiments/inputs/839_{label}_window';meta=json.loads((data/'inputs.json').read_text());case_start=time.monotonic()
 assert isinstance(meta['grid'],int) and meta['grid']==H and H>0 and H%2==0
 assert isinstance(meta['scale'],int) and meta['scale']==V and V>0
 R=meta['R'];assert isinstance(R,int) and R==262143 and R>=0
 assert meta['window_coefficients']==expected_coeffs and meta['denominator']==1000000
 coef=[F(a,meta['denominator']) for a in expected_coeffs];margin=1-sum(map(abs,coef));assert margin>0
 assert hashlib.sha256((data/'kernel_lower.bin').read_bytes()).hexdigest()==expected_sha
 p=data/'kernel_lower.bin';raw=p.read_bytes();assert len(raw)==4*(R+1);tab=struct.unpack('<'+'I'*(R+1),raw)
 half=F(1,2*H);mismatch=[];min_slack=None
 for k,claimed in enumerate(tab):
  t=F(2*k+1,2*H);j=k%H;idx=min(j,H-1-j);sl,su,cl,cu=trig[idx]
  if j>=H//2:cl,cu=-cu,-cl
  rr=1/t;dd=-1/(t*t)
  for n,a in enumerate(coef,1):
   rr+=a*(-1)**n*t/(t*t-n*n)
   dd-=a*(-1)**n*(t*t+n*n)/(t*t-n*n)**2
  dl=min(rr*cl,rr*cu)+min(dd*sl,dd*su);du=max(rr*cl,rr*cu)+max(dd*sl,dd*su)
  local=min(piU,max(abs(dl),abs(du))+piU*piU*half)
  lower=max(F(0),abs(rr)*sl-local*half)
  certified=(V*lower*lower).__floor__()
  if certified<claimed:mismatch.append({'cell':k,'claimed':claimed,'certified':certified})
  if k%40000==0:print(json.dumps({'progress_cells':k,'elapsed_seconds':time.monotonic()-start}),flush=True)
 base=F(4,3)+sum((a*a/2 for a in coef),F(0));S=sum(((-1)**j*a/F(j*j)-a*a/F(4*j*j) for j,a in enumerate(coef,1)),F(0))
 lowC,highC=sorted([base+S/(piL*piL),base+S/(piU*piU)]);cap=F(meta['energy_cap']);assert highC<cap
 return {'label':label,'source_commit':'0e961ea199b425010843bc8044676d4ad29fe031','cells':len(tab),'table_sha256':hashlib.sha256(raw).hexdigest(),'input_sha256':hashlib.sha256((data/'inputs.json').read_bytes()).hexdigest(),'coefficients':expected_coeffs,'coefficient_denominator':1000000,'positive_density_lower_bound':str(margin),'integral_density':1,'all_table_lower_bounds_certified':not mismatch,'mismatches':mismatch[:50],'energy_upper_cap':str(cap),'energy_cap_independently_checked':True,'case_seconds':time.monotonic()-case_start}
results=[check_data('second',[122290,-45012,16241,1887,2711,3731,-5307,2982,-5153,5358],'e32c430de69dd92adbfbdb9935a9983eb7e033113c2c87c2a763f549e4401e0a'),check_data('third',[200566,19,-9358,9283,-6746,8170],'698cd6a9e691e1ed132a8990967c63694cb64f2f614090ba0d6ff9d31eb2da6d')]
out={'kind':'independent_exact_rational_second_third_cell_checks','arithmetic':'Python Fraction exact; no floats in inequalities','shared_trig':True,'total_elapsed_seconds':time.monotonic()-start,'results':results,'scope':'Kernel-table soundness and energy caps only. Does not check second/third branch searches or analytic zeta transfer; not Lean execution.'}
print(json.dumps(out,indent=2));(archive_root/'experiments/results/independent_kernel_cells_second_third.json').write_text(json.dumps(out,indent=2))

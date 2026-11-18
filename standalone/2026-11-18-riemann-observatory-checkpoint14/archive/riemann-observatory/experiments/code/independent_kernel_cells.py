"""Independent exact-rational verification of EVERY first-window kernel-table cell.
No numpy, floating point, or author helper routines. Stronger Taylor enclosures than builder.
Analytic lemmas: K=Fourier(f), f>=0,int f=1,supp f in[-1/2,1/2];
|K'|<=pi,|K''|<=pi^2. Closed sinc-sum expression gives midpoint K,K'.
All binary lower bounds are checked by mean value theorem over the WHOLE cell.
Usage: python experiments/code/independent_kernel_cells.py [path/to/839-v1_OR_data_folder]
Default uses the bundled MIT-licensed experiments/inputs/839_first_window data.
"""
from fractions import Fraction as F
from pathlib import Path
import sys,math,struct,json,time,hashlib
start=time.monotonic();archive_root=Path(__file__).resolve().parents[2]
root=Path(sys.argv[1]) if len(sys.argv)>1 else archive_root/'experiments/inputs/839_first_window'
data=root/'certificate' if (root/'certificate/inputs.json').exists() else root
meta=json.loads((data/'inputs.json').read_text());H,V,R=meta['grid'],meta['scale'],meta['R']
assert isinstance(H,int) and H>0 and H%2==0 and isinstance(V,int) and V>0 and isinstance(R,int) and R>=0
assert meta['window_coefficients']==[193305,-23105,29166,13952,-21009,41052] and meta['denominator']==1000000
assert (H,V,R)==(16384,268435456,209009)
coef=list(map(lambda n:F(n,10**6),[193305,-23105,29166,13952,-21009,41052]));assert sum(map(abs,coef))<1
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
res={'kind':'independent_exact_rational_all_cell_check_with_classical_analytic_bounds','source_commit':'0e961ea199b425010843bc8044676d4ad29fe031','table_sha256':hashlib.sha256(raw).hexdigest(),'cells':len(tab),'all_table_lower_bounds_certified':not mismatch,'mismatches':mismatch[:50],'elapsed_seconds':time.monotonic()-start,'pi_interval_width':str(piU-piL),'arithmetic':'Python Fraction exact; no floating point in inequalities','scope':'Full first-window table only; mathematical justification of Taylor, Fourier derivative bounds and mean-value estimate is a short external proof, not Lean-checked here.'}
print(json.dumps(res,indent=2));out=Path(__file__).resolve().parents[2]/'experiments/results/independent_kernel_cells.json';out.write_text(json.dumps(res,indent=2))

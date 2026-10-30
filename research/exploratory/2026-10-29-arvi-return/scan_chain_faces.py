"""Floating-point reconnaissance of PR94 chain faces; not a proof.

New faces are tested wherever all 15 transcribed admission guards are strictly
positive; current branches are restricted to the existing 31 windows. This
does not prove the generalized Lean branch interface exists.
"""
from pathlib import Path
import re
from collections import Counter
import numpy as np

root = Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density')
source = (root/'ChainF50/Chain.lean').read_text()
pattern = r'theorem (boot|source_\d+) \(hβ[^\n]*\) :\s*QRH\.Record1252270103Source\.GlobalSource \((\d+) / (\d+) : ℝ\) \((\d+) / (\d+) : ℝ\) \((\d+) / (\d+) : ℝ\)'
raw = re.findall(pattern, source)
assert len(raw)==130
faces=[(v[0],int(v[1])/int(v[2]),int(v[3])/int(v[4]),int(v[5])/int(v[6])-1e-5) for v in raw]
ns={}
exec(Path(__file__).with_name('check_rows.py').read_text().split('assert len(windows) == 31')[0],ns)
windows=[(n,float(a),float(b),float(c)) for n,a,b,c in ns['windows']]
assert len(windows)==31
B,L,cap=faces[-1][1:]
PB,PL,PC=49283557/50000000,4503/2000,31/500
theta=8738702/10**7
k=2*theta-1
EPS=1e-7; natural=(1-4.5*.03)/2

def counts(d,p,b,l,cp,ic,guard_list=False):
 v=5/6-d; z=cp-EPS
 dd=3-p if ic else 3-p-4*p/l
 aa=2+0*p if ic else 2-4*p/l
 c0=1-2*p*z if ic else 1-2*p*b/l
 zz=2*p*z if ic else 2*p*b/l
 u=(1-p)*c0; j=v*dd+d*(1-p)*aa
 t=j+d*u; rn=aa*t+(zz-p)*j; dj=dd*j; mn=dd*t-rn
 low=.377+EPS if ic else max(.377+EPS,(b-l*z)/2+EPS)
 high=np.minimum(np.minimum(.44-EPS,natural-EPS),(b-l*(z if ic else .03+EPS))/2-EPS)
 derd=-1 if ic else -1-4/l; dera=0 if ic else -4/l
 derc=-2*z if ic else -2*b/l
 deru=-c0+(1-p)*derc; derj=v*derd+d*(-aa+(1-p)*dera)
 nn=(1-d)*j+v*d*u
 guards=[dd,aa,c0,j,t-j,1.2499*j-t,rn-23/37*dj,dj-rn,
         mn-low*dj,high*dj-mn,nn-(1-2*d*natural-2*d*p*.03)*j,
         u*derj-deru*j,0*d+.44-natural-EPS,
         0*d+b-2*natural-l*(.03+EPS)-2*EPS,
         (z-.03-EPS)*dj if ic else 0*d+1]
 if guard_list:
  # Separate the minimum into its three affine inequalities.
  guards[9:10]=[(.44-EPS)*dj-mn,(natural-EPS)*dj-mn,
                 ((b-l*(z if ic else .03+EPS))/2-EPS)*dj-mn]
  return nn/j, [np.broadcast_to(g,np.shape(d)) for g in guards]
 return nn/j, np.minimum.reduce(guards)

def optimize_cap(d,p,b,l,cpmax):
 # Capped count and its guard polynomials are affine in cp. Intersect all
 # pointwise half intervals numerically and approach the largest feasible cp.
 cpmin=.03+2*EPS+1e-12
 if cpmax<=cpmin:return np.full(d.shape,np.inf)
 _,g0=counts(d,p,b,l,cpmin,True,True)
 _,g1=counts(d,p,b,l,cpmax,True,True)
 lo=np.full(d.shape,cpmin);hi=np.full(d.shape,cpmax);possible=np.ones(d.shape,bool)
 for a,c in zip(g0,g1):
  slope=(c-a)/(cpmax-cpmin)
  possible &= (np.abs(slope)>1e-15) | (a>1e-12)
  cross=cpmin-np.divide(a,slope,out=np.zeros_like(a),where=np.abs(slope)>1e-15)
  hi=np.where(slope < -1e-15,np.minimum(hi,cross),hi)
  lo=np.where(slope > 1e-15,np.maximum(lo,cross),lo)
 cp=hi-1e-12
 possible &= cp>lo+1e-12
 val,guard=counts(d,p,b,l,cp,True)
 return np.where(possible & (guard>0),val,np.inf)

def evaluate(d,p):
 d,p=np.broadcast_arrays(np.asarray(d),np.asarray(p))
 v=5/6-d; od=3-p-2*p/(3*k); oc=2*(1-p)*(1-p/(3*k)); oj=v*od+d*oc
 base=((1-d)*oj+d*oc*v/2)/oj
 label=np.full(d.shape,'old',dtype='<U16')
 current=[('C',B,L,cap,False),('capC',B,L,cap,True),('weakC7',B-7/4000,L,cap,False),('capP',PB,PL,PC,True)]
 for name,b,l,cp,ic in current:
  count,guard=counts(d,p,b,l,cp,ic)
  admitted=np.zeros(d.shape,bool)
  for n,lo,hi,pl in windows:
   if name==n: admitted|=(d>=lo)&(d<=hi)&(p>=pl)&(p<=.5)
  admitted &= guard>=-1e-12
  use=admitted & (count<base);base=np.where(use,count,base);label=np.where(use,name,label)
 best=base.copy(); which=np.full(d.shape,'baseline',dtype='<U20')
 for name,b,l,cp in faces:
  for ic in (False,True):
   if ic:
    val=optimize_cap(d,p,b,l,cp);guard=np.ones(d.shape)
   else:
    val,guard=counts(d,p,b,l,cp,ic)
   use=(guard>1e-12)&(val<best-1e-12)
   best=np.where(use,val,best);which=np.where(use,name+('_cap' if ic else '_C'),which)
 return base,best,label,which

if __name__=='__main__':
 d,p=np.meshgrid(np.linspace(0,.75,301),np.linspace(0,.5,201),indexing='ij')
 base,best,label,which=evaluate(d,p);gain=base-best
 good=gain>1e-10
 print('faces',len(faces),'grid',d.size,'improved',int(good.sum()),'fraction',np.mean(good))
 print('best case',float(gain.max()),'at',float(d.flat[gain.argmax()]),float(p.flat[gain.argmax()]),'branch',which.flat[gain.argmax()],'base',float(base.flat[gain.argmax()]),'new',float(best.flat[gain.argmax()]))
 print('improved domain', (float(d[good].min()),float(d[good].max()),float(p[good].min()),float(p[good].max())) if good.any() else None)
 print('top winning branches',Counter(which[good]).most_common(15))
 for x,y in [(223/500,.5),(.446,.499),(.446,.49),(.445,.5),(.45,.5),(.43,.45),(.4,.48),(.5,.5),(.52,.49),(.3,.45)]:
  b,z,l,w=evaluate(x,y);print('point',x,y,'baseline',b.item(),l.item(),'new',z.item(),w.item(),'gain',(b-z).item())

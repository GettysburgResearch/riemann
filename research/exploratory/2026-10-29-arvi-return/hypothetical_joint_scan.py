import numpy as np
from scipy.optimize import differential_evolution, minimize
B=.96232839; L=1.9265; cap=.09999; PB=.98567114; PL=2.2515; PC=.062
branches=[('old',0,1,.04),('C',B,L,cap),('capC',B,L,cap),('weakC7',B-.00175,L,cap),('capP',PB,PL,PC)]
ns={}
exec((__import__('pathlib').Path(__file__).with_name('check_rows.py')).read_text().split('assert len(windows) == 31')[0],ns)
windows=[(n,float(a),float(b),float(c)) for n,a,b,c in ns['windows']]
def make(theta,h,combine=False):
 c=1-theta; ell=4*c-1/3;x=1+ell-h;y=h-2*ell; k=1-2*c
 def f(v, show=False):
  de,p=v
  edges=[(.005,min(.005,2*y-.005)/(6*k)),(.76,min(.76,2*y-.76)/(6*k))]
  phys93b=3945996453113/4000000000000;phys93l=4603201/2000000
  lines=[(0,.0619),(2*y/PL,-(2-PB)/PL)]
  if combine: lines += [(0,1/16),(2*y/phys93l,-(2-phys93b)/phys93l)]
  ds=[.76,h+1e-10]
  for i,(a,b) in enumerate(lines):
   for c0,d0 in lines[i+1:]:
    if b!=d0:
     z=(c0-a)/(b-d0)
     if .76<z<h+1e-10:ds.append(z)
  for dd in ds:
   a=min(lines[0][0]+lines[0][1]*dd,lines[1][0]+lines[1][1]*dd)
   if combine: a=max(a,min(lines[2][0]+lines[2][1]*dd,lines[3][0]+lines[3][1]*dd))
   edges.append((dd,a))
  out=[]
  for d,C in edges:
   vals=[]
   for name,b,l,capb in branches:
    V=5/6-de
    if name != 'old' and not any(name==n and lo<=de<=hi and low<=p<=.5 for n,lo,hi,low in windows): continue
    if name=='old':
     dd=3-p-2*p/(3*k);aa=2*(1-p)*(1-p/(3*k)); J=V*dd+de*aa; N=(1-de)*J+de*aa*V/2
    else:
     ic=name.startswith('cap'); z=capb-1e-7; dd=3-p if ic else 3-p-4*p/l; aa=2 if ic else 2-4*p/l; c0=1-2*p*z if ic else 1-2*p*b/l;zz=2*p*z if ic else 2*p*b/l; U=(1-p)*c0; J=V*dd+de*(1-p)*aa;T=J+de*U; rn=aa*T+(zz-p)*J; mn=dd*T-rn; dj=dd*J; nm=(1-4.5*.03)/2; low=.377+1e-7 if ic else max(.377+1e-7,(b-l*(capb-1e-7))/2+1e-7); high=min(.44-1e-7,nm-1e-7, (b-l*(z if ic else .03+1e-7))/2-1e-7); derd=-1 if ic else -1-4/l; dera=0 if ic else -4/l; derc=-2*z if ic else -2*b/l;deru=-c0+(1-p)*derc;derj=V*derd+de*(-aa+(1-p)*dera)
     g=[dd,aa,c0,J,T-J,1.2499*J-T,rn-23/37*dj,dj-rn,mn-low*dj,high*dj-mn, U*derj-deru*J, .44-nm-1e-7,b-2*nm-l*(.03+1e-7)-2e-7,(z-.03-1e-7)*dj if ic else 1]
     N=(1-de)*J+V*de*U;g.append(N-(1-2*de*nm-2*de*p*.03)*J)
     if min(g)<-1e-12: continue
    vals.append((N/J,name))
   sigma=2*de*p
   vals.append((3*(1-sigma)*(1-de)/(3-de-2*sigma),'hyp_joint'))
   R,name=min(vals); base=.5+13*h/75-y/2-ell/2-.09*d+de/2+de*p*(ell-C/2)
   out.append((base+.75*d*R,name))
  idx=np.argmax([q[0] for q in out]);return out[idx][0]-theta,(idx,out[idx],out) if show else None
 return f
if __name__=='__main__':
 from scipy.optimize import differential_evolution
 for theta,h in [(0.87387234,0.8),(0.87287234,0.8),(0.872,0.8),(0.8717357911022081,0.7994470045156682)]:
  f=make(theta,h)
  for seed in (1,2,3):
   out=differential_evolution(lambda v:-f(v)[0],[(0,.75),(0,.5)],popsize=16,tol=1e-8,seed=seed)
   print('theta',theta,'h',h,'seed',seed,'worst gap',-out.fun,'delta,p',out.x,'edge,branch',f(out.x,True)[1][0:2],flush=True)
 # Exact geometric lower limit from positive floor saving and y>11/25.
 from fractions import Fraction as F
 limit=F(45400000000603,52080000000000)
 hcorner=F(11,25)+2*(F(11,3)-4*limit)
 assert (9360000000000*limit-1000000000000*hcorner-7360000000201)==0
 print('exact retained geometry limit theta >',limit,'≈',float(limit),'limiting h',hcorner)

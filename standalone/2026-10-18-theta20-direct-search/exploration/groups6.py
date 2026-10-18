import numpy as np,json,math,itertools,time,sys
from pathlib import Path
from scipy.optimize import least_squares
from scipy.special import logsumexp,gammaln
ROOT=Path(__file__).parent
an=np.array(list(map(float,json.load(open(ROOT/'target.json'))['an'])))
N=np.array([32,6,2,2,1,1]);G=len(N)
M=np.array(list(itertools.product(*[np.arange(-n,n+1,2) for n in N])),float)
logbase=sum(gammaln(n+1)-gammaln((M[:,j]+n)/2+1)-gammaln((n-M[:,j])/2+1) for j,n in enumerate(N))
pairs=list(itertools.combinations_with_replacement(range(G),2))
V=np.column_stack([(M[:,i]**2-N[i])/2 if i==j else M[:,i]*M[:,j] for i,j in pairs])
last=[None,None,None]

def ev(z):
 if last[0] is not None and np.array_equal(z,last[0]):return last[1],last[2]
 y=M@z[:G];ew=logbase+V@z[G:];pr=np.exp(ew-logsumexp(ew))
 p0=np.ones(len(y));p1=y/an[1];d0=np.zeros(len(y));d1=np.ones(len(y))/an[1]
 polys=[];der=[]
 for k in range(1,20):
  p2=(y*p1-an[k]*p0)/an[k+1];d2=(p1+y*d1-an[k]*d0)/an[k+1]
  if(k+1)%2==0:polys.append(p2);der.append(d2)
  p0,p1=p1,p2;d0,d1=d1,d2
 P=np.array(polys);D=np.array(der)
 f=P@pr
 J=np.c_[(D*pr)@M,(P*pr)@V-f[:,None]*(pr@V)[None,:]]
 last[:]=[z.copy(),f,J];return f,J

def fun(z):return ev(z)[0]
def jac(z):return ev(z)[1]
bl=np.r_[np.ones(G)*.0001,np.ones(len(pairs))*1e-8];bh=np.r_[np.ones(G)*1,np.ones(len(pairs))*.5]
mode=int(sys.argv[1]) if len(sys.argv)>1 else 0
rng=np.random.default_rng(7853+mode)
best=1.;start=time.monotonic()
for t in range(12):
 z=np.r_[np.linspace(.06,.24,G)*np.exp(rng.normal(0,.15,G)),[rng.uniform(.05,.7)/N[i] if i==j else rng.uniform(.00001,.002) for i,j in pairs]]
 if t==0 and (ROOT/f'groups6_best{mode}.json').exists():z=np.array(json.load(open(ROOT/f'groups6_best{mode}.json'))['z'])
 else:
  prob=np.exp(logbase+V@z[G:]-logsumexp(logbase+V@z[G:]));v=prob@((M@z[:G])**2);z[:G]/=np.sqrt(v)
 z=np.clip(z,bl+1e-12,bh-1e-12)
 out=least_squares(fun,z,jac=jac,bounds=(bl,bh),max_nfev=400,gtol=1e-14,ftol=1e-14,xtol=1e-14,x_scale='jac')
 err=np.linalg.norm(out.fun)
 if err<best:
  best=err;json.dump({'err':err,'N':N.tolist(),'pairs':pairs,'z':out.x.tolist(),'f':out.fun.tolist(),'states':len(M),'status':'NUMERICAL EXPLORATION ONLY'},open(ROOT/f'groups6_best{mode}.json','w'),indent=2)
  print('trial',t,'err',err,'nfev',out.nfev,'minJ',min(out.x[G:]),flush=True)
 if err<1e-11:break
 if time.monotonic()-start>28:break

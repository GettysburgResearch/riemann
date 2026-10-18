import numpy as np,json,math,itertools,time,sys
from pathlib import Path
from scipy.optimize import least_squares
from scipy.special import logsumexp,gammaln,roots_hermitenorm
ROOT=Path(__file__).parent
an=np.array(list(map(float,json.load(open(ROOT/'target.json'))['an'])))
N=np.array([6,2,2,1,1]);G=len(N)
M=np.array(list(itertools.product(*[np.arange(-n,n+1,2) for n in N])),float)
logbase=sum(gammaln(n+1)-gammaln((M[:,j]+n)/2+1)-gammaln((n-M[:,j])/2+1) for j,n in enumerate(N))
pairs=[(i,j) for i,j in itertools.combinations_with_replacement(range(G),2) if i!=j or N[i]>1]
V=np.column_stack([(M[:,i]**2-N[i])/2 if i==j else M[:,i]*M[:,j] for i,j in pairs])
gn,gw=roots_hermitenorm(11);gw/=np.sqrt(2*np.pi)
last=[None,None,None]
def ev(z):
 if last[0] is not None and np.array_equal(z,last[0]):return last[1],last[2]
 y=(M@z[:G])[None,:]+z[G]*gn[:,None];ew=logbase+V@z[G+1:];pr=np.exp(ew-logsumexp(ew))
 p0=np.ones_like(y);p1=y/an[1];d0=np.zeros_like(y);d1=np.ones_like(y)/an[1];ps=[];ds=[];gs=[]
 for k in range(1,20):
  p2=(y*p1-an[k]*p0)/an[k+1];d2=(p1+y*d1-an[k]*d0)/an[k+1]
  if(k+1)%2==0:ps.append(gw@p2);ds.append(gw@d2);gs.append((gw*gn)@d2)
  p0,p1=p1,p2;d0,d1=d1,d2
 P=np.array(ps);D=np.array(ds);gg=np.array(gs)@pr;f=P@pr
 J=np.c_[(D*pr)@M,gg,(P*pr)@V-f[:,None]*(pr@V)[None,:]]
 last[:]=[z.copy(),f,J];return f,J
fun=lambda z:ev(z)[0];jac=lambda z:ev(z)[1]
bl=np.r_[np.ones(G+1)*.00001,np.ones(len(pairs))*1e-9];bh=np.r_[np.ones(G+1)*1.5,np.ones(len(pairs))*2]
mode=int(sys.argv[1]) if len(sys.argv)>1 else 0
rng=np.random.default_rng(7943+mode);best=1.;start=time.monotonic()
for t in range(20):
 z=np.r_[np.linspace(.1,.3,G)*np.exp(rng.normal(0,.2,G)),.3,[rng.uniform(.001,.5) if i==j else rng.uniform(.00001,.02) for i,j in pairs]]
 path=ROOT/f'gaussian_groups{mode}.json'
 if t==0 and path.exists():z=np.array(json.load(open(path))['z'])
 else:
  prob=np.exp(logbase+V@z[G+1:]-logsumexp(logbase+V@z[G+1:]));v=prob@((M@z[:G])**2)+z[G]**2;z[:G+1]/=np.sqrt(v)
 out=least_squares(fun,z,jac=jac,bounds=(bl,bh),max_nfev=1000,gtol=1e-14,ftol=1e-14,xtol=1e-14,x_scale='jac')
 err=np.linalg.norm(out.fun)
 if err<best:
  best=err;json.dump({'err':err,'N':N.tolist(),'pairs':pairs,'z':out.x.tolist(),'f':out.fun.tolist(),'states':len(M),'status':'NUMERICAL EXPLORATION ONLY'},open(path,'w'),indent=2)
  print('trial',t,'err',err,'nfev',out.nfev,'minJ',min(out.x[G+1:]),flush=True)
 if err<5e-12:break
 if time.monotonic()-start>30:break

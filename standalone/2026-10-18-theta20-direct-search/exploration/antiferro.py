import numpy as np,json,itertools,time,sys
from pathlib import Path
from scipy.optimize import least_squares
from scipy.special import logsumexp,roots_hermitenorm
ROOT=Path(__file__).parent
an=np.array(list(map(float,json.load(open(ROOT/'target.json'))['an'])))
N=12;H=3
pairs=list(itertools.combinations(range(N),2))
M=np.array(list(itertools.product([-1.,1.],repeat=N)))
V=np.column_stack([M[:,i]*M[:,j] for i,j in pairs])
gn,gw=roots_hermitenorm(11);gw/=np.sqrt(2*np.pi)
cache=[None,None,None]
def ev(z):
 if cache[0] is not None and np.array_equal(z,cache[0]):return cache[1],cache[2]
 a=z[:N];ga=z[N];lw=V@z[N+1:];pr=np.exp(lw-logsumexp(lw))
 score=V
 y=(M@a)[None,:]+ga*gn[:,None]
 p0=np.ones_like(y);p1=y;d0=np.zeros_like(y);d1=np.ones_like(y);ps=[];ds=[];gs=[]
 for k in range(1,20):
  p2=(y*p1-an[k]*p0)/an[k+1];d2=(p1+y*d1-an[k]*d0)/an[k+1]
  if(k+1)%2==0:ps.append(gw@p2);ds.append(gw@d2);gs.append((gw*gn)@d2)
  p0,p1=p1,p2;d0,d1=d1,d2
 P=np.array(ps);D=np.array(ds);gg=np.array(gs)@pr;f=P@pr
 J=np.c_[(D*pr)@M,gg,(P*pr)@score-f[:,None]*(pr@score)[None,:]]
 cache[:]=[z.copy(),f,J];return f,J
fun=lambda z:ev(z)[0];jac=lambda z:ev(z)[1]
mode=int(sys.argv[1]) if len(sys.argv)>1 else 0
rng=np.random.default_rng(4294+mode);path=ROOT/f'antiferro{mode}.json'
z=np.r_[np.linspace(.05,.4,N)*np.exp(rng.normal(0,.3,N)),.35,rng.uniform(.00001,.015,len(pairs))]
if path.exists():z=np.array(json.load(open(path))['z'])
elif (ROOT/f'complete{mode}.json').exists():z=np.array(json.load(open(ROOT/f'complete{mode}.json'))['z'])
else:
 lp=V@z[N+1:];p=np.exp(lp-logsumexp(lp));var=p@((M@z[:N])**2)+z[N]**2;z[:N+1]/=np.sqrt(var)
lo=np.r_[np.ones(N+1)*1e-5,np.ones(len(pairs))*(-.2)];hi=np.r_[np.ones(N+1)*1.5,np.ones(len(pairs))*3]
count=0;best=1.
def fsave(z):
 global count,best
 f=fun(z);err=np.linalg.norm(f);count+=1
 if err<best:
  best=err;json.dump({'err':err,'N':N,'H':H,'z':z.tolist(),'f':f.tolist(),'calls':count,'status':'EXPLORATORY, NOT CERTIFIED'},open(path,'w'),indent=2)
 return f
out=least_squares(fsave,z,jac=jac,bounds=(lo,hi),max_nfev=500,gtol=1e-14,ftol=1e-14,xtol=1e-14,x_scale='jac')
print('err',np.linalg.norm(out.fun),'calls',out.nfev,'minw',out.x[N+1:].min(),flush=True)

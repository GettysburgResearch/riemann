import numpy as np
from scipy.optimize import minimize
B0=0.96232839;L0=1.9265;L=L0-.005;c0=c=.1
vgrid=np.linspace(0,1,13);pgrid=np.linspace(0,.5,17);tgrid=np.linspace(0,1,13)

def vals(x,grid=(vgrid,pgrid,tgrid)):
 cross,A,D=x;vg,pg,tg=grid
 v=vg*(c-cross);w=cross+v;u=A*v/(1+D*v);H=1-6*u
 dens=.999*L0*A/(.005*(1+D*v)+(6*B0-L0)*A)
 out=[cross, c-cross, A,D,*list(1+D*v),*list(dens-.5),*list(.75-dens),*list(H-.9),*list(c0*H-(w-u)),*list(w-u),*list(1/3-2*w-3*u),*list(1-(B0-.005*cross)+(L-2)*w-4.5*u),*list(.05+1.5*(1-(B0-.005*cross))+(1.5*L-2.5)*w-4.5*u),*list(1-(B0-.005*cross)+(L-1)*w-4*u)]
 v=v[:,None,None];w=w[:,None,None];u=u[:,None,None];H=H[:,None,None];dens=dens[:,None,None]
 p=pg[None,:,None];nu=dens+(0.75-dens)*tg[None,None,:]
 base=10/(15-6*nu);ww=5-6*nu;B=B0-.005*cross;S=w-u
 j=base*nu -nu*B+nu*(L-1)*w-(6*base*nu-nu-1)*u
 for i in (0,1):
  invs=1 if i==0 else 1/(1-p)
  invo=-2*p*8*S if i==0 else -p*H/(1-p)
  for k in (0,1,2):
   ps=1 if k<2 else 1/(1-2*p/L0)
   po= -2*p*S if k==0 else (-2*p*c0*H if k==1 else -(2*p*B0*H/L0)/(1-2*p/L0))
   root=(5*H-ww*(invo+po/2))/(6*nu+ww*(invs+ps/2))
   gain=(1-2*p)*nu*S+nu*(root-base*H)
   out.extend((j+gain).ravel().tolist())
 return np.array(out)

if __name__=='__main__':
 margin=1e-9
 for guess in [(.099,4,500),(.0995,6,1200),(.0999,10,10000)]:
  res=minimize(lambda x:-x[0],guess,method='SLSQP',bounds=[(.001,.099999),(.05,30),(.01,100000)],constraints=[{'type':'ineq','fun':lambda x:vals(x)-margin}],options={'maxiter':300,'ftol':1e-11})
  print('success',res.success,'x',res.x,'sample min',min(vals(res.x)),'message',res.message,flush=True)
  if res.success:
   fine=vals(res.x,(np.linspace(0,1,121),np.linspace(0,.5,121),np.linspace(0,1,41)))
   print('fine minimum',min(fine),'child B',B0-.005*res.x[0],flush=True)

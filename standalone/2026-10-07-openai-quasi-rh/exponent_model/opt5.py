import sys; sys.path.insert(0,'.')
from model2 import *
import numpy as np, time
mode=sys.argv[1]
def obj(g,nd=16):
    lx,b,ell=g
    if lx<=ell or b<0 or ell<0: return 9,9
    s=sigma_low2(g)
    w=max(worst(beta,g,mode,nd=nd,xs=(0.25,0.5))[0] for beta in [s+1e-6,min(11/12,s+0.03)])
    return s,w
best=((17/48,1/8,1/6),obj((17/48,1/8,1/6))[0])
print('start',best,obj(best[0]),flush=True)
rng=np.random.default_rng(int(sys.argv[2]))
t0=time.time(); step=float(sys.argv[4])
while time.time()-t0<float(sys.argv[3]):
    g=tuple(np.array(best[0])+rng.normal(0,step,3))
    s,w=obj(g)
    if w<0 and s<best[1]-1e-6:
        best=(g,s); print(round(s,5),round(w,6),[round(v,4) for v in g],'M+ell',round(2*g[0]+g[1]+g[2],4),flush=True)
print('best',best)

import numpy as np, math
from mpmath import mp, mpf
mp.dps=40
R4=2+math.sqrt(3)
def funcs(reals,pairs):
    r=np.array(reals,float)
    def h(t):
        v=np.sum(1.0/(t[:,None]-r[None,:]),axis=1)
        for (x,y,m) in pairs: v+=m*2*(t-x)/((t-x)**2+y**2)
        return v
    def hp(t):
        v=-np.sum(1.0/(t[:,None]-r[None,:])**2,axis=1)
        for (x,y,m) in pairs:
            s=t-x; v+=m*2*(y**2-s**2)/(s**2+y**2)**2
        return v
    return h,hp
def fcount(fn,a,b,N=60000):
    e=(b-a)*1e-10
    t=np.linspace(a+e,b-e,N)
    v=fn(t); s=np.sign(v)
    return int(np.sum(s[:-1]*s[1:]<0))
def mpcount(reals,pairs,a,b,deriv=False,N=30001):
    a,b=mpf(a),mpf(b); e=(b-a)/mpf(10)**14
    def f(t):
        if deriv:
            v=-sum(1/(t-mpf(r))**2 for r in reals)
            for (x,y,m) in pairs:
                s=t-x; v+=m*2*(mpf(y)**2-s**2)/(s**2+mpf(y)**2)**2
        else:
            v=sum(1/(t-mpf(r)) for r in reals)
            for (x,y,m) in pairs: v+=m*2*(t-x)/((t-x)**2+mpf(y)**2)
        return v
    prev=None; sc=0
    for i in range(N):
        t=a+e+(b-a-2*e)*mpf(i)/(N-1)
        v=f(t)
        if prev is not None and v*prev<0: sc+=1
        prev=v
    return sc
mxe=-1; mxhp=0; cand=[]; total=0
gaps=[0.1,0.5,1.0,2.0]
for g in gaps:
    a,b=0.0,g
    bgs=[[a,b],[a,b,b+0.3*g,b+0.9*g,b+2*g],[a-0.5*g,a,b],[a,a,b],[a,a,a,b,b],
         [a-0.1*g,a,b,b,b+0.1*g],[a-3*g,a-0.2*g,a,b,b+0.2*g,b+3*g]]
    for reals in bgs:
        # optional far pair, R4-far from G: at x=b+10*g, y=0.4 => Itilde=(x-1.49,x+1.49) misses (a,b) if 10g-1.5>0
        farsets=[[],[(b+10*g+2.0,0.4,1)],[(a-10*g-2.0,0.3,2)]]
        for far in farsets:
            for y in [0.01,0.03,0.05,0.1,0.25,0.5]:
                for xf in [-0.3,-0.05,0.0,0.1,0.25,0.4,0.5,0.6,0.75,0.9,1.05,1.3]:
                    x=a+xf*g
                    for m1 in [1,2,5]:
                        pairs=[(x,y,m1)]+far
                        h,hp=funcs(reals,pairs)
                        zh=fcount(h,a,b); zhp=fcount(hp,a,b); total+=1
                        if zh-1>=2 or zhp>=3: cand.append((g,tuple(reals),tuple(far),x,y,m1,zh,zhp))
                        else:
                            mxe=max(mxe,zh-1); mxhp=max(mxhp,zhp)
print("total configs:",total,"float-clean max extra:",mxe,"max zhp:",mxhp,"candidates:",len(cand))
vm=-1; vhp=0; vio=[]
for (g,reals,far,x,y,m1,zh,zhp) in cand:
    pairs=[(x,y,m1)]+list(far)
    Zh=mpcount(list(reals),pairs,0.0,g); Zhp=mpcount(list(reals),pairs,0.0,g,deriv=True)
    vm=max(vm,Zh-1); vhp=max(vhp,Zhp)
    if Zh-1>6 or Zhp>6: vio.append((g,reals,far,x,y,m1,Zh,Zhp))
print("verified candidates: max extra:",vm,"max zhp:",vhp,"violations of C_A=6:",len(vio))
for v in vio: print(v)

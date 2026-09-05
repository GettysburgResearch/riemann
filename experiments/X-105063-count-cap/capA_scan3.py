import numpy as np, math
from mpmath import mp, mpf
mp.dps=30
def vals(reals,pairs,t,deriv):
    r=np.array(reals,float)
    if deriv:
        terms=[-1.0/(t[:,None]-r[None,:])**2]
        tp=[]
        for (x,y,m) in pairs:
            s=t-x; tp.append(m*2*(y**2-s**2)/(s**2+y**2)**2)
    else:
        terms=[1.0/(t[:,None]-r[None,:])]
        tp=[]
        for (x,y,m) in pairs: tp.append(m*2*(t-x)/((t-x)**2+y**2))
    v=terms[0].sum(axis=1)+ (np.sum(tp,axis=0) if tp else 0)
    scale=np.abs(terms[0]).sum(axis=1)+(np.sum(np.abs(tp),axis=0) if tp else 0)
    return v,scale
def rcount(reals,pairs,a,b,deriv=False,N=60000):
    e=(b-a)*1e-9
    t=np.linspace(a+e,b-e,N)
    v,sc=vals(reals,pairs,t,deriv)
    solid=np.abs(v)>1e-11*sc
    s=np.sign(v[solid])
    if len(s)==0: return 0
    return int(np.sum(s[:-1]*s[1:]<0))
def mpcount(reals,pairs,a,b,deriv=False,N=8001):
    a,b=mpf(a),mpf(b); e=(b-a)/mpf(10)**13; prev=None; sc=0
    for i in range(N):
        t=a+e+(b-a-2*e)*mpf(i)/(N-1)
        if deriv:
            v=-sum(1/(t-mpf(r))**2 for r in reals)
            for (x,y,m) in pairs:
                s=t-x; v+=m*2*(mpf(y)**2-s**2)/(s**2+mpf(y)**2)**2
        else:
            v=sum(1/(t-mpf(r)) for r in reals)
            for (x,y,m) in pairs: v+=m*2*(t-x)/((t-x)**2+mpf(y)**2)
        if prev is not None and v*prev<0: sc+=1
        prev=v
    return sc
mxe=-1; mxhp=0; cand=[]; total=0; best=None
gaps=[0.1,0.5,1.0,2.0]
for g in gaps:
    a,b=0.0,g
    bgs=[[a,b],[a,b,b+0.3*g,b+0.9*g,b+2*g],[a-0.5*g,a,b],[a,a,b],[a,a,a,b,b],
         [a-0.1*g,a,b,b,b+0.1*g],[a-3*g,a-0.2*g,a,b,b+0.2*g,b+3*g]]
    for reals in bgs:
        farsets=[[],[(b+10*g+2.0,0.4,1)],[(a-10*g-2.0,0.3,2)]]
        for far in farsets:
            for y in [0.01,0.03,0.05,0.1,0.25,0.5]:
                for xf in [-0.3,-0.05,0.0,0.1,0.25,0.4,0.5,0.6,0.75,0.9,1.05,1.3]:
                    x=a+xf*g
                    for m1 in [1,2,5]:
                        pairs=[(x,y,m1)]+far
                        zh=rcount(reals,pairs,a,b); zhp=rcount(reals,pairs,a,b,deriv=True); total+=1
                        if zh-1>mxe or (zh-1==mxe and zhp>mxhp):
                            best=(g,tuple(reals),tuple(far),x,y,m1,zh,zhp)
                        mxe=max(mxe,zh-1); mxhp=max(mxhp,zhp)
                        if zh-1>2 or zhp>6: cand.append((g,tuple(reals),tuple(far),x,y,m1,zh,zhp))
print("total:",total,"float max extra:",mxe,"max zhp:",mxhp,"cands(>2 or >6):",len(cand))
print("best:",best)
# mpmath-verify best + all candidates
ver=[best]+cand
seen=set()
for (g,reals,far,x,y,m1,zh,zhp) in ver:
    key=(g,reals,far,x,y,m1)
    if key in seen: continue
    seen.add(key)
    pairs=[(x,y,m1)]+list(far)
    Zh=mpcount(list(reals),pairs,0.0,g); Zhp=mpcount(list(reals),pairs,0.0,g,deriv=True)
    print("VERIFY",key,"-> extra:",Zh-1,"zhp:",Zhp,"(float said",zh-1,zhp,")")

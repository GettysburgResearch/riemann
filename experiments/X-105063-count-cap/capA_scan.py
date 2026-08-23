import numpy as np, itertools, math
R4 = 2+math.sqrt(3)
def make_funcs(reals, pairs):
    reals=np.array(reals,float)
    def h(t):
        v=np.sum(1.0/(t[:,None]-reals[None,:]),axis=1)
        for (x,y,m) in pairs: v+=m*2*(t-x)/((t-x)**2+y**2)
        return v
    def hp(t):
        v=-np.sum(1.0/(t[:,None]-reals[None,:])**2,axis=1)
        for (x,y,m) in pairs:
            s=t-x; v+=m*2*(y**2-s**2)/(s**2+y**2)**2
        return v
    return h,hp
def count_zeros(fn,a,b,N=200000):
    # grid clustered near endpoints via tanh-like map
    u=np.linspace(-1,1,N); u=np.sign(u)*np.abs(u)**1.5  # cluster near ends? this clusters near center; invert
    u=np.sin(u*np.pi/2)  # clusters near +-1? sin flattens near ends -> clusters points near ends
    t=a+(b-a)*(u+1)/2
    t=t[(t>a)&(t<b)]
    v=fn(t); sgn=np.sign(v)
    sc=np.sum(sgn[:-1]*sgn[1:]<0)
    return int(sc)
results=[]; mx_extra=-10; mx_hp=0; worst=None
gaps=[0.1,0.5,1.0,2.0]
for g in gaps:
    a,b=0.0,g
    bgs=[[a,b],[a,b,b+0.3*g,b+0.9*g,b+2*g],[a-0.5*g,a,b],[a,a,b],[a,a,a,b,b],[a-0.1*g,a,b,b,b+0.1*g],
         [a-3*g,a-0.2*g,a,b,b+0.2*g,b+3*g]]
    for reals in bgs:
        for y in [0.01,0.05,0.1,0.25,0.5]:
            if y>0.5: continue
            for xf in [-0.3,-0.05,0.0,0.1,0.25,0.5,0.75,0.9,1.05,1.3]:
                x=a+xf*g
                for m1 in [1,2,5]:
                    pairs=[(x,y,m1)]
                    # H1 check trivially true (no other pairs)
                    h,hp=make_funcs(reals,pairs)
                    zh=count_zeros(h,a,b); zhp=count_zeros(hp,a,b)
                    extra=zh-1
                    if extra>mx_extra or (extra==mx_extra and zhp>mx_hp):
                        mx_extra=max(mx_extra,extra); worst=(g,tuple(reals),x,y,m1,zh,zhp)
                    mx_hp=max(mx_hp,zhp)
                    if extra>2 or zhp>6:
                        results.append(("FLAG",g,tuple(reals),x,y,m1,zh,zhp))
print("max extra:",mx_extra,"max Z(h'):",mx_hp)
print("worst:",worst)
print("flags:",len(results))
for r in results[:20]: print(r)

import numpy as np, random, math
exec(open('scan3.py').read().split('mxe=-1')[0])  # reuse rcount, mpcount
random.seed(7)
mxe=-1;mxhp=0;best=None;cand=[]
# adversarial: pair hugging endpoint, tiny y, high m1
for g in [0.05,0.2,1.0]:
    a,b=0.0,g
    for reals in [[a,b],[a,a,a,b],[a-0.01*g,a,b,b+0.01*g],[a,b,b,b,b]]:
        for y in [0.001,0.005,0.02,0.08]:
            for xf in [0.001,0.01,0.03,0.06,0.12,0.5,0.88,0.94,0.97,0.99,0.999,1.001,1.01]:
                for m1 in [1,3,10,50]:
                    pairs=[(a+xf*g,y,m1)]
                    zh=rcount(reals,pairs,a,b,N=120000);zhp=rcount(reals,pairs,a,b,deriv=True,N=120000)
                    if zh-1>mxe:best=(g,tuple(reals),xf,y,m1,zh,zhp)
                    mxe=max(mxe,zh-1);mxhp=max(mxhp,zhp)
                    if zh-1>2 or zhp>6:cand.append((g,tuple(reals),xf,y,m1,zh,zhp))
# random configs
for trial in range(3000):
    g=10**random.uniform(-2,1); a,b=0.0,g
    nl=random.randint(0,3); nr=random.randint(0,3)
    reals=[a,b]+[a-10**random.uniform(-2,1)*g for _ in range(nl)]+[b+10**random.uniform(-2,1)*g for _ in range(nr)]
    reals+= [a]*random.randint(0,2)+[b]*random.randint(0,2)
    y=min(0.5,10**random.uniform(-3,-0.301))
    x=a+random.uniform(-0.5,1.5)*g; m1=random.choice([1,1,1,2,3,7])
    pairs=[(x,y,m1)]
    zh=rcount(reals,pairs,a,b);zhp=rcount(reals,pairs,a,b,deriv=True)
    if zh-1>mxe:best=(round(g,4),tuple(round(r,4) for r in reals),round(x,4),y,m1,zh,zhp)
    mxe=max(mxe,zh-1);mxhp=max(mxhp,zhp)
    if zh-1>2 or zhp>6:cand.append((g,tuple(reals),x,y,m1,zh,zhp))
print("adversarial+random: max extra:",mxe,"max zhp:",mxhp,"cands:",len(cand))
print("best:",best)
for c in cand[:10]:
    (g,reals,x,y,m1,zh,zhp)=c
    if x<1.5: xx=x if x>0.002 else x*g
    pairs=[(x if abs(x)<100 else x,y,m1)]
    Zh=mpcount(list(reals),[(x,y,m1)],0.0,g);Zhp=mpcount(list(reals),[(x,y,m1)],0.0,g,deriv=True)
    print("VERIFY",c,"->",Zh-1,Zhp)

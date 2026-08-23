# Residual-boundary scans: (i) deep clusters (Sep violated); (ii) supercritical shallow + deep.
import numpy as np, math, random
exec(open('scanC.py').read().split("random.seed(7)")[0])  # reuse builders
random.seed(11)
print("== (i) deep clusters: k pairs crammed within one R4-fattened neighborhood ==")
maxratio=0; rec=None
for trial in range(300):
    g=1.0; reals=[(0.0,1),(g,1)]
    k = random.choice([2,2,3,4])
    xc = random.uniform(0.2,0.8); yb = 10**random.uniform(-3,-1.2)
    cl=[]
    for i in range(k):
        y = yb*random.uniform(0.5,2); x = xc + random.uniform(-1,1)*R4*yb*1.5
        cl.append((x,y,random.choice([1,1,2])))
    q,ex,nzp,per,outside = run_config(g, reals, cl)
    if q['sep']: continue   # want genuine clusters
    ratio = ex/ k
    if ex > maxratio*k or rec is None:
        if ratio>maxratio: maxratio=ratio; rec=(k,ex,nzp,cl)
print("max extra per clustered pair:", maxratio, " record:", rec[:3])
print("== (ii) supercritical shallow (Wsh>=1) + deep pairs (outside all hypotheses) ==")
maxex=0; rec2=None
for trial in range(300):
    g=0.5; reals=[(0.0,1),(g,1)]
    pairs=[]
    for _ in range(random.randint(2,8)):
        y=random.uniform(g/2,0.5); x=random.uniform(-0.1,0.6)
        pairs.append((x,y,random.randint(1,4)))
    D=random.choice([0,1,2,3])
    deep=[]
    att=0
    while len(deep)<D and att<100:
        att+=1
        y=10**random.uniform(-3,math.log10(0.2)); x=random.uniform(0.02,0.48)
        if all(abs(x-x2)>=R4*(y+y2)*1.02 for x2,y2,_ in deep): deep.append((x,y,random.choice([1,2,5])))
    pairs+=deep
    q,ex,nzp,per,outside = run_config(g, reals, pairs)
    if q['Wsh'] < 1: continue
    tot = ex
    if tot>maxex: maxex=tot; rec2=(q['Wsh'],q['D'],ex,nzp,per)
print("max extra:", maxex, " record (Wsh,D,extra,nzp,per):", rec2)

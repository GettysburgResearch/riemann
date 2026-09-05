import numpy as np, math, random
R4 = 2+math.sqrt(3); KAP=(11+5*math.sqrt(5))/64; G4=0.0225425; G6=0.0463163
COT8 = 1+math.sqrt(2); COT12 = 2+math.sqrt(3)
def build(reals, pairs):
    ra = np.array([r for r,_ in reals]); rm = np.array([m for _,m in reals], float)
    px = np.array([x for x,_,_ in pairs]); py = np.array([y for _,y,_ in pairs]); pm = np.array([m for _,_,m in pairs], float)
    def h(t):
        t = np.atleast_1d(t)[:,None]
        A = rm/(t-ra); B = pm*2*(t-px)/((t-px)**2+py**2)
        v = A.sum(1)+B.sum(1); mag = np.abs(A).sum(1)+np.abs(B).sum(1)
        return v, mag
    def hp(t):
        t = np.atleast_1d(t)[:,None]
        A = -rm/(t-ra)**2
        u = t-px; r2 = u**2+py**2
        B = pm*2*(py**2-u**2)/r2**2
        v = A.sum(1)+B.sum(1); mag = np.abs(A).sum(1)+np.abs(B).sum(1)
        return v, mag
    return h, hp
def count_zeros(fn, a, b, N=400000, tol=1e-11):
    t = np.linspace(a,b,N+2)[1:-1]
    v, mag = fn(t)
    good = np.abs(v) > tol*mag
    tg, vg = t[good], v[good]
    s = np.sign(vg)
    idx = np.nonzero(s[1:]*s[:-1] < 0)[0]
    return len(idx), tg, vg, idx
def hyp_quantities(g, pairs):
    # gap (0,g). classify
    Wsh=V1=V2=0.0; deep=[]; M4L=M4R=M6L=M6R=0.0
    ok_sep=True
    ov=[]
    for (x,y,m) in pairs:
        if x+y>0 and x-y<g: ov.append((x,y,m))
        else:
            if x+y<=0:  # left non-ov
                if -x < COT8*y: M4L+=m
                if -x < COT12*y: M6L+=m
            else:
                if x-g < COT8*y: M4R+=m
                if x-g < COT12*y: M6R+=m
    for (x,y,m) in ov:
        if y >= g/2:
            w=(g/(2*y))**2; Wsh+=m*w; V1+=m*w*w; V2+=m*w**3
        else: deep.append((x,y,m))
    for i in range(len(deep)):
        for j in range(i+1,len(deep)):
            xi,yi,_=deep[i]; xj,yj,_=deep[j]
            if abs(xi-xj) < R4*(yi+yj): ok_sep=False
    L2 = Wsh < 1
    L4 = KAP*V1 + G4*(M4L+M4R) < 1
    L6 = V2 + G6*(M6L+M6R) < 1
    return dict(Wsh=Wsh,V1=V1,V2=V2,deep=deep,D=len(deep),sep=ok_sep,L2=L2,L4=L4,L6=L6,
                M4=M4L+M4R,M6=M6L+M6R)
def run_config(g, reals, pairs, N=400000):
    q = hyp_quantities(g, pairs)
    h, hp = build(reals, pairs)
    nz,_,_,_ = count_zeros(h, 0, g, N)
    nzp, tg, vg, idx = count_zeros(hp, 0, g, N)
    # confinement + per-interval count of h' zeros
    dx = g/(N+1)
    zbr = [(tg[i]-dx, tg[i+1]+dx) for i in idx]
    per=[0]*q['D']; outside=0
    for lo,hi in zbr:
        placed=False
        for k,(x,y,m) in enumerate(q['deep']):
            if hi > x-y and lo < x+y: per[k]+=1; placed=True; break
        if not placed: outside+=1
    return q, nz-1, nzp, per, outside
random.seed(7); rng = np.random.default_rng(7)
viol=[]; maxex=-9; maxper=0; results=[]; nconf=0
for trial in range(700):
    g = random.choice([0.5,1.0])
    reals=[(0.0,1),(g,1)]
    if random.random()<0.4: reals.append((round(-random.uniform(0.05,0.5)*g,4),random.randint(1,3)))
    if random.random()<0.4: reals.append((round(g+random.uniform(0.05,0.5)*g,4),random.randint(1,3)))
    D = random.choice([1,1,2,2,3,5,8])
    # place deep pairs R4-separated: sequential greedy
    deep=[]; attempts=0
    while len(deep)<D and attempts<200:
        attempts+=1
        y = 10**random.uniform(-3, math.log10(0.45*g/2)); x = random.uniform(0.02*g, 0.98*g)
        if all(abs(x-x2)>=R4*(y+y2)*1.02 for x2,y2,_ in deep):
            deep.append((round(x,6), round(y,6), random.choice([1,1,2,5])))
    pairs=list(deep)
    # shallow background
    for _ in range(random.randint(0,4)):
        y = random.uniform(g/2, 0.5); x = random.uniform(-0.2*g, 1.2*g)
        pairs.append((round(x,4), round(y,4), 1))
    # trim shallow mult so Wsh<1: compute then adjust
    q0 = hyp_quantities(g, pairs)
    if q0['Wsh'] >= 1:
        # drop shallow pairs until <1
        pairs2=list(deep); ws=0
        for p in pairs[len(deep):]:
            x,y,m=p; w=(g/(2*y))**2 if (x+y>0 and x-y<g and y>=g/2) else 0
            if ws+w<0.99: pairs2.append(p); ws+=w
        pairs=pairs2
    # occasional band-adjacent non-ov pairs within budget
    if random.random()<0.35:
        y=random.uniform(0.05,0.5); pairs.append((round(-random.uniform(0.1,1.0)*y,4), round(y,4), random.randint(1,4)))
    q,ex,nzp,per,outside = run_config(g, reals, pairs)
    if not (q['sep'] and q['L2'] and q['L4'] and q['L6']): continue
    nconf+=1
    ok = ex <= 6*q['D'] and outside==0 and all(p<=6 for p in per)
    if ex>maxex: maxex=ex; best=(g,reals,pairs,q,ex,nzp,per)
    maxper=max(maxper,max(per) if per else 0)
    if not ok: viol.append((g,reals,pairs,q,ex,nzp,per,outside))
print("configs passing hypotheses:", nconf)
print("violations:", len(viol))
print("max extra:", maxex, " max per-interval Z(h'):", maxper)
g,reals,pairs,q,ex,nzp,per = best
print("best: g=%s D=%d Wsh=%.3f extra=%d nzp=%d per=%s bound=%d" % (g,q['D'],q['Wsh'],ex,nzp,per,6*q['D']))
for v in viol[:3]: print("VIOL:", v)

import numpy as np, math
rng = np.random.default_rng(7)

def make_h(reals, pairs):
    R = np.array(reals); P = np.array(pairs) if pairs else np.zeros((0,2))
    def h(t):
        s = np.sum(1.0/(t[:,None]-R[None,:]),axis=1)
        if len(P):
            u = t[:,None]-P[None,:,0]; y2 = P[None,:,1]**2
            s += np.sum(2*u/(u*u+y2),axis=1)
        return s
    return h

def count_zeros(h, a, b, n=400001):
    t = np.linspace(a,b,n)[1:-1]
    v = h(t); sc = np.sum(np.abs(np.diff(np.sign(v)))>1)
    return int(sc)

def base_reals(g, K=8):
    return [0.0,g]+[-1.0-i for i in range(K)]+[g+1.0+i for i in range(K)]

results = []
worst = (0,None)
for trial in range(600):
    g = rng.choice([0.3,0.6,1.0])
    m = rng.integers(2,31)
    mode = rng.integers(0,3)
    ymin, ymax = g/2, 0.5
    if mode==0:   # random overhang
        ys = rng.uniform(ymin,ymax,m)
        xs = rng.uniform(-ys*0.9, g+ys*0.9)
    elif mode==1: # clustered at center
        ys = rng.uniform(ymin,min(ymax,ymin*1.2),m)
        xs = g/2 + rng.normal(0,0.02*g,m)
    else:         # spread evenly, near-critical y
        ys = np.full(m, ymin*rng.uniform(1.0,1.1))
        xs = np.linspace(-0.3*g,1.3*g,m)
    pairs=[(x,y) for x,y in zip(xs,ys)]
    # keep only overhanging (all are, roughly) - compute weights over ov pairs
    ov=[(x,y) for x,y in pairs if x+y>0 and x-y<g]
    W  = sum(min(1,(g/(2*y))**2) for x,y in ov)
    W2 = sum(min(1,(g/(2*y))**2)**2 for x,y in ov)
    h = make_h(base_reals(g), pairs)
    z = count_zeros(h,0,g)
    extra = z-1
    wmax = max(((g/(2*y))**2 for x,y in ov), default=0)
    if extra > worst[0]: worst=(extra,(g,m,mode,W,W2,wmax))
    results.append((extra,W,W2,wmax,g,m,mode))
    if extra>2:
        print("EXTRA>2:",extra,g,m,mode,"W=%.3f W2=%.3f wmax=%.3f"%(W,W2,wmax))
ex = [r[0] for r in results]
print("max extra:",max(ex),"counts:",{k:ex.count(k) for k in sorted(set(ex))})
print("worst:",worst)
# check ladder prediction on each: k minimal with sum w^{k+1}<1 => extra<=2k
viol=0
for extra,W,W2,wmax,g,m,mode in results:
    if wmax<1 and W2>0:
        k=1
        while True:
            s=W2*(wmax**(k-1))  # upper bound of sum w^{k+1}
            if s<1 or k>200: break
            k+=1
        if extra>2*k: viol+=1; print("LADDER VIOLATION", extra, k)
print("ladder violations:",viol)

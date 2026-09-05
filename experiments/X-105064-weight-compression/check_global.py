import random
random.seed(64)

def run_config(trial):
    # symmetric zero set (parity), pairs at +-x
    n = random.randint(6, 30)
    pos = sorted(random.uniform(0.2, 20) for _ in range(n))
    zeros = sorted([-z for z in pos] + pos)   # k even model, Xi_k(0)!=0
    npairs = random.randint(0, 8)
    pairs = []
    for _ in range(npairs):
        x = random.uniform(0, 22); y = random.uniform(0.01, 0.5)
        m = random.randint(1, 3)
        pairs += [(x, y, m), (-x, y, m)]
    T = random.uniform(1, pos[-1])  # hostile-review fix: T beyond the finite synthetic zero set made b_T undefined
    # gap list: gaps meeting (0,T]
    gaps = [(zeros[i], zeros[i+1]) for i in range(len(zeros)-1)]
    gcalT = [(a,b) for (a,b) in gaps if b > 0 and a < min(b,T) and any(0 < u <= T for u in [(max(a,0)+min(b,T))/2]) ]
    gcalT = [(a,b) for (a,b) in gaps if b > 0 and a <= T]  # meets (0,T] iff b>0 and a<T (open gap)
    gcalT = [(a,b) for (a,b) in gaps if b > 0 and a < T]
    # W by definition (double sum)
    W = 0.0
    for (a,b) in gcalT:
        g = b - a
        for (x,y,m) in pairs:
            if x - y < b and x + y > a:
                W += m*min(1.0, g*g/(4*y*y))
    # per-pair bound side
    t1 = pos[0]; bT = min([z for z in zeros if z > T], default=None)
    S1 = 0.0; count = 0
    for (x,y,m) in pairs:
        om = 0.0; gmax = 0.0
        for (a,b) in gaps:
            if x - y < b and x + y > a:
                g = b - a; om += min(1.0,g*g/(4*y*y)); gmax = max(gmax,g)
        mu = min(1.0, gmax/(2*y))
        charged = (x > -t1 - 0.5) and (bT is not None and x < bT + 0.5)
        if charged:
            S1 += m*(mu + 2*mu*mu); count += m
        # sanity: if pair overhangs a gap in gcalT it must be charged
        for (a,b) in gcalT:
            if x - y < b and x + y > a:
                assert charged, (trial, x, y, t1, bT)
    return W, S1, 3*count, bT, T

bad = 0
for tr in range(20000):
    W, S1, S3, bT, T = run_config(tr)
    if W > S1 + 1e-9 or S1 > S3 + 1e-9: bad += 1
print("global configs: 20000, violations of W<=Sum m(mu+2mu^2)<=3*mult:", bad)

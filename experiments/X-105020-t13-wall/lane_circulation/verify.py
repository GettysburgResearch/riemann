"""Validation: (1) brute max-flow on truncated instance vs cut-family prediction,
(2) interval closed form, (3) global argmin of A_t, (4) canonical prefix min at terminal bases."""
from fractions import Fraction
from mpmath import mp, mpf, sqrt, nstr, iv

PRIMES61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def smooth_divisors(bound):
    out = [(1,1)]
    for p in PRIMES61:
        new = []
        for d,mu in out:
            nd = d*p
            if nd <= bound: new.append((nd,-mu))
        out += new
    out.sort(); return out

# ---------- (1) brute max-flow on truncated model, float ----------
mp.dps = 30
def T(u): return 4*sqrt(u)-3 if u >= 1 else mpf(0)

def build_truncated(q, y, cap):
    X = 67*q*y; B1 = q*y
    nodes = []  # (leaf, d, mass, is_even)
    for d,mu in smooth_divisors(min(cap,X)):
        nodes.append((0,d, T(mpf(X)/d)/sqrt(mpf(d)), mu==1))
    for d,mu in smooth_divisors(min(cap,B1)):
        nodes.append((1,d, T(mpf(B1)/d)/sqrt(mpf(67*d)), mu==-1))
    for d,mu in smooth_divisors(min(cap,y)):
        nodes.append((2,d, T(mpf(y)/d)/sqrt(mpf(67*q*d)), mu==1))
    return X,B1,nodes

def mobius(d):
    m=1
    for p in PRIMES61:
        if d%p==0: m=-m
    return m

def edges_licensed(nodes):
    E=[]
    for i,(l1,d1,m1,e1) in enumerate(nodes):
        if not e1: continue
        for j,(l2,d2,m2,e2) in enumerate(nodes):
            if e2: continue
            if l1==l2 and d1<=d2: E.append((i,j))
            elif l2==l1+1 and d1==d2: E.append((i,j))  # parent->child same d
    return E

def maxflow(nodes, E):
    # simple successive shortest augmentation via BFS (Edmonds-Karp), float
    import collections
    n=len(nodes); S=n; Tk=n+1; N=n+2
    capm=collections.defaultdict(mpf)
    adj=collections.defaultdict(set)
    INF=mpf(10)**9
    for i,(l,d,m,ev) in enumerate(nodes):
        if ev: capm[(S,i)]=m; adj[S].add(i); adj[i].add(S)
        else: capm[(i,Tk)]=m; adj[i].add(Tk); adj[Tk].add(i)
    for i,j in E:
        capm[(i,j)]=INF; adj[i].add(j); adj[j].add(i)
    flow=mpf(0)
    while True:
        # BFS
        par={S:None}; qq=[S]
        while qq:
            u=qq.pop(0)
            if u==Tk: break
            for v in adj[u]:
                if v not in par and capm[(u,v)]>mpf(10)**-25:
                    par[v]=u; qq.append(v)
        if Tk not in par: break
        # bottleneck
        b=INF; v=Tk
        while par[v] is not None:
            b=min(b,capm[(par[v],v)]); v=par[v]
        v=Tk
        while par[v] is not None:
            u=par[v]; capm[(u,v)]-=b; capm[(v,u)]+=b; v=u
        flow+=b
    return flow

def predicted_violation(q,y,cap):
    X,B1,nodes=build_truncated(q,y,cap)
    l0=[(d,m,ev) for l,d,m,ev in nodes if l==0]
    l1=[(d,m,ev) for l,d,m,ev in nodes if l==1]
    l2=[(d,m,ev) for l,d,m,ev in nodes if l==2]
    def prefix_DC(lst):
        out=[]; run=mpf(0)
        for d,m,ev in lst:
            run += (-m if ev else m)
            out.append((d,run))
        return out  # D-C prefix
    P0=prefix_DC(l0); P1=prefix_DC(l1); P2=prefix_DC(l2)
    best=mpf(0)
    # V = P0(t0)+P1(t1)+P2(t2), t2<=t1<=t0, each threshold in coords or 0
    cand2=[(0,mpf(0))]+P2; cand1=[(0,mpf(0))]+P1; cand0=P0
    for t0,v0 in cand0:
        for t1,v1 in cand1:
            if t1>t0: break
            for t2,v2 in cand2:
                if t2>t1: break
                best=max(best,v0+v1+v2)
    # also pure leaf-1/leaf-2 cuts (t0=0)
    for t1,v1 in cand1:
        if t1==0: continue
        # need cross-pulled even R_d for odd A_d in S: all d<=t1 mu+ root evens
        # V = v1 + P2 - C0pull(t1)
        c0pull=sum(m for d,m,ev in l0 if ev and d<=t1)
        for t2,v2 in cand2:
            if t2>t1: break
            best=max(best,v1+v2-c0pull)
    return best

for cap in [10, 30, 100]:
    X,B1,nodes=build_truncated(71,13,cap)
    E=edges_licensed(nodes)
    tot_dem=sum(m for l,d,m,ev in nodes if not ev)
    fl=maxflow(nodes,E)
    deficit=tot_dem-fl
    pred=predicted_violation(71,13,cap)
    print(f"cap={cap}: nodes={len(nodes)} maxflow deficit={nstr(deficit,12)}  predicted max-violation={nstr(pred,12)}  match={abs(deficit-pred)<mpf(10)**-15}")

# ---------- (2) interval closed form ----------
iv.prec=250
A13 = Fraction(0)
B13v = iv.mpf(0)
for d,mu in smooth_divisors(13):
    A13 += Fraction(mu,d)
    B13v += mu/iv.sqrt(iv.mpf(d))
print("A_13 exact =", A13)
X=61841
F013 = 4*iv.sqrt(iv.mpf(X))*iv.mpf(A13.numerator)/A13.denominator - 3*B13v
print("F0(13) interval:", nstr(F013.a,20), nstr(F013.b,20))
G11 = (4*iv.sqrt(iv.mpf(923))-3)/iv.sqrt(iv.mpf(67))
V = -F013 + G11
print("V*(61841) interval:", nstr(V.a,20), nstr(V.b,20))

# ---------- (3) global argmin of A_t and of F0 for growing X ----------
mp.dps=30
divs = smooth_divisors(2*10**6)
runA=Fraction(0); Amin=Fraction(10); argA=None
prof=[]
for d,mu in divs:
    runA += Fraction(mu,d)
    prof.append((d,runA))
    if runA<Amin: Amin=runA; argA=d
print("global min of A_t over smooth squarefree t<=2e6:", Amin, float(Amin), "at t=",argA)
# second-lowest below -0.07?
lows=sorted(prof,key=lambda z:z[1])[:6]
print("lowest A_t values:", [(d,float(v)) for d,v in lows])

# ---------- (4) canonical d-prefix min at terminal base 923 (net atoms) ----------
run=mpf(0); mn=mpf(10**9); arg=None
for d,mu in smooth_divisors(923):
    td=(T(mpf(923)/d) - T(mpf(13)/d)/sqrt(mpf(71)))/sqrt(mpf(d))
    run+=mu*td
    if run<mn: mn=run; arg=d
print("canonical prefix min at base 923 (sum mu t_d):", nstr(mn,12), "at d=",arg)

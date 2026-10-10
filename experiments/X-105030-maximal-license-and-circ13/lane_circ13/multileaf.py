"""General licensed-class model for arbitrary prefix-closed history set L.
Independent Edmonds-Karp max-flow vs the S1(L) cut lower bound (and S_all variant).
Also programmatic enumeration of N(S1(L)) to verify the cut-validity lemma."""
import collections
from mpmath import mp, mpf, sqrt, nstr

mp.dps = 30
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

def T(u): return 4*sqrt(u)-3 if u >= 1 else mpf(0)

def prod(h):
    r = 1
    for p in h: r *= p
    return r

def build(X, L, cap):
    # nodes: (h, d, mass, is_even)
    nodes = []
    for h in L:
        Xh = mpf(X)/prod(h)
        if Xh < 1: continue
        sgn_h = (-1)**len(h)
        for d,mu in smooth_divisors(min(cap, int(Xh))):
            m = T(Xh/d)/sqrt(mpf(prod(h))*d)
            nodes.append((h, d, m, mu*sgn_h == 1))
    return nodes

def licensed_edges(L, nodes):
    idx = {(h,d): i for i,(h,d,m,ev) in enumerate(nodes)}
    E = []
    for i,(h1,d1,m1,e1) in enumerate(nodes):
        if not e1: continue
        for j,(h2,d2,m2,e2) in enumerate(nodes):
            if e2: continue
            if h1 == h2 and d1 <= d2: E.append((i,j))                       # within-leaf nested
            elif len(h2) == len(h1)+1 and h2[:len(h1)] == h1 and d1 == d2:  # parent->child same d
                E.append((i,j))
    return E

def maxflow(nodes, E):
    n = len(nodes); S = n; Tk = n+1
    capm = collections.defaultdict(mpf); adj = collections.defaultdict(set)
    INF = mpf(10)**9
    for i,(h,d,m,ev) in enumerate(nodes):
        if ev: capm[(S,i)] = m; adj[S].add(i); adj[i].add(S)
        else: capm[(i,Tk)] = m; adj[i].add(Tk); adj[Tk].add(i)
    for i,j in E:
        capm[(i,j)] = INF; adj[i].add(j); adj[j].add(i)
    flow = mpf(0)
    while True:
        par = {S: None}; q = [S]
        while q:
            u = q.pop(0)
            if u == Tk: break
            for v in adj[u]:
                if v not in par and capm[(u,v)] > mpf(10)**-24:
                    par[v] = u; q.append(v)
        if Tk not in par: break
        b = INF; v = Tk
        while par[v] is not None: b = min(b, capm[(par[v],v)]); v = par[v]
        v = Tk
        while par[v] is not None:
            u = par[v]; capm[(u,v)] -= b; capm[(v,u)] += b; v = u
        flow += b
    return flow

def cut_values(X, L, nodes):
    # S1(L): root odds d<=13  +  heads of depth-1 leaves
    dem = mpf(0); capv = mpf(0); dem_all_extra = mpf(0); cap_all_extra = mpf(0)
    odd_leaves = [h for h in L if len(h) % 2 == 1]
    parents_of_deep_odds = set()
    for (h,d,m,ev) in nodes:
        if h == () and not ev and d <= 13: dem += m
        if h == () and ev and d in (1,6,10): capv += m
        if len(h) == 1 and d == 1 and not ev: dem += m
        if len(h) >= 3 and len(h) % 2 == 1 and d == 1 and not ev:
            dem_all_extra += m; parents_of_deep_odds.add(h[:-1])
    for (h,d,m,ev) in nodes:
        if h in parents_of_deep_odds and d == 1 and ev: cap_all_extra += m
    V1 = dem - capv
    Vall = dem + dem_all_extra - capv - cap_all_extra
    return V1, Vall

def neighborhood_check(X, L, nodes, E):
    # enumerate in-neighbors of every node of S1(L); assert subset of root {1,6,10}
    S1 = set()
    for i,(h,d,m,ev) in enumerate(nodes):
        if h == () and not ev and d <= 13: S1.add(i)
        if len(h) == 1 and d == 1 and not ev: S1.add(i)
    N = set()
    for (i,j) in E:
        if j in S1: N.add(i)
    Nset = sorted((nodes[i][0], nodes[i][1]) for i in N)
    ok = all(h == () and d in (1,6,10) for h,d in Nset)
    return Nset, ok

def run(X, L, cap, label):
    nodes = build(X, L, cap)
    E = licensed_edges(L, nodes)
    dem_tot = sum(m for h,d,m,ev in nodes if not ev)
    fl = maxflow(nodes, E)
    deficit = dem_tot - fl
    V1, Vall = cut_values(X, L, nodes)
    Nset, ok = neighborhood_check(X, L, nodes, E)
    print(f"{label}: X={X} cap={cap} nodes={len(nodes)}")
    print(f"   N(S1) = {Nset}   subset of root x {{1,6,10}}: {ok}")
    print(f"   maxflow deficit = {nstr(deficit,15)}   V(S1) = {nstr(V1,15)}   V(S_all) = {nstr(Vall,15)}")
    print(f"   deficit >= V(S1): {deficit >= V1 - mpf(10)**-18}   deficit - V(S1) = {nstr(deficit - V1, 6)}")
    return deficit, V1, Vall

X = 61841
print("== Test 1: branch two-leaf model {(),(67),(67,71)} (reproduce validation) ==")
for cap in (10, 30, 100):
    run(X, [(), (67,), (67,71)], cap, "L2")

print("\n== Test 2: add depth-1 leaf (71): L3 = {(),(67),(67,71),(71)} ==")
h71 = T(mpf(X)/71)/sqrt(mpf(71))
print("   predicted extra head(71) =", nstr(h71, 15))
for cap in (10, 30, 100):
    d2,_,_ = run(X, [(), (67,), (67,71)], cap, "  L2")
    d3,V13,_ = run(X, [(), (67,), (67,71), (71,)], cap, "  L3")
    print(f"   cap={cap}: deficit(L3)-deficit(L2) = {nstr(d3-d2,15)}  vs head(71) = {nstr(h71,15)}")

print("\n== Test 3: depth-3 odd leaf, X=400000, L={(),(67),(67,71),(67,71,73)} ==")
for cap in (13, 30):
    run(400000, [(), (67,), (67,71), (67,71,73)], cap, "L-depth3")

print("\n== Test 4: no (67): L={(),(71)} at X=61841 ==")
for cap in (13, 30):
    run(X, [(), (71,)], cap, "L-71only")

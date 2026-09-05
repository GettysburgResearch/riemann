"""SOUND certified first-open-band GFEP, X >= X0.
Fixes vs v1: two-branch knot pokes in src_lo; symmetric parent-image widening;
zero-floor top cell; mpf-only bookkeeping. See derivation in session notes.
Claim certified: for all X >= X0=2000, all integers n with X/10 < n < ceil(X/5),
all p in [n, min(2n,X+1)):  sqrt(X)*Sigma_{X,n}(p) >= WORST > 0."""
from mpmath import iv, mp, mpf
from fractions import Fraction as Fr
iv.dps = 40

def mob(n):
    mu=[0]*(n+1); mu[1]=1
    for i in range(1,n+1):
        if mu[i]:
            for j in range(2*i,n+1,i): mu[j]-=mu[i]
    return mu
MU = mob(16)
X0 = 2000
def fr2iv(x): return iv.mpf(x.numerator)/iv.mpf(x.denominator)  # exact rational -> tight interval
IX0 = iv.mpf(1)/X0

def C_on(N, tlo, thi):
    """interval enclosure of C_N(log 1/t) for t in [tlo,thi] (Fractions), branch N fixed."""
    t = iv.mpf([fr2iv(tlo).a, fr2iv(thi).b])
    L = -iv.log(t)
    s = iv.mpf(0)
    for k in range(1, N+1):
        if MU[k]: s += MU[k]*(1 + (L - iv.log(k))/2)/iv.sqrt(k)
    return s, t

def branchN(a, b):
    mid = (a+b)/2
    return int(Fr(1,1)/mid)   # floor(1/mid) via Fraction floor div
def fr_floor_inv(x):  # floor(1/x) for Fraction
    return (x.denominator)//(x.numerator)

def src_lo(a, b, Nc, Nnext, positive_region):
    """certified mpf lower bound of sqrt(X)*m'R(m') for m'/X in [a,b], X>=X0.
    window J=[t,t+1/X] c [a, b+1/X0]; piece1=[a,b] branch Nc, piece2=[b,b+1/X0] branch Nnext.
    bound: inf_pieces(t^{-1/2}C) - (1/X0)*sup_pieces|t^{-3/2}C|; if positive_region: max(...,0),
    and if b+1/X0 > 1 return 0 (uses phi>=0 on [1/5,1])."""
    if positive_region and b + Fr(1,X0) > 1:
        return mpf(0)
    C1, t1 = C_on(Nc, a, b)
    f1 = C1/iv.sqrt(t1); g1 = C1/(t1*iv.sqrt(t1))
    b2 = b + Fr(1, X0)
    C2, t2 = C_on(Nnext, b, min(b2, Fr(1,1)))
    f2 = C2/iv.sqrt(t2); g2 = C2/(t2*iv.sqrt(t2))
    inf_f = min(f1.a, f2.a)
    sup_g = max(abs(g1.a), abs(g1.b), abs(g2.a), abs(g2.b))
    val = iv.mpf(inf_f) - iv.mpf(sup_g)/X0
    out = val.a
    if positive_region and out < 0: out = mpf(0)
    return out

def grid(seg_knots, sub):
    edges = []
    for i in range(len(seg_knots)-1):
        a, b = seg_knots[i], seg_knots[i+1]
        for j in range(sub): edges.append(a + (b-a)*j/sub)
    edges.append(seg_knots[-1])
    return edges

SUB = 120
WID = Fr(3, X0)
q_2m  = iv.mpf(1)/2
q_2m1 = iv.mpf(1)/4 - iv.mpf(5)/(4*X0)  # ADV FIX: band child p > X/10 needs eps=5/(4X0)
q_3m  = iv.mpf(1)/6
q_b3  = iv.mpf(1)/3 - iv.mpf(5)/(9*X0)

# ---- gamma on [1/5, 1]
EG = grid([Fr(1,5), Fr(1,4), Fr(1,3), Fr(1,2), Fr(1,1)], SUB)
KG = len(EG)-1
def next_branch(edges, i, Ncur):
    return branchN(edges[i+1], edges[i+2]) if i+2 <= len(edges)-1 else Ncur  # top cell: piece capped at 1 anyway
def overlapping(edges, lo, hi):
    return [j for j in range(len(edges)-1) if edges[j+1] > lo and edges[j] < hi]

gamma = [None]*KG
for i in range(KG-1, -1, -1):
    a, b = EG[i], EG[i+1]
    Nc = branchN(a, b)
    val = iv.mpf(src_lo(a, b, Nc, next_branch(EG, i, Nc), True))
    for fac, q in [(Fr(2,1), q_2m + q_2m1), (Fr(3,1), 3*q_3m), (Fr(3,2), q_b3)]:
        lo, hi = fac*a - WID, fac*b + WID
        if fac*b + WID <= 1:
            cs = overlapping(EG, lo, hi)
            assert cs and all(gamma[j] is not None for j in cs), (i, fac)
            val += q*iv.mpf(min(gamma[j].a for j in cs))
    gamma[i] = val
gmin = min(g.a for g in gamma)
print(f"gamma: K={KG}, min = {float(gmin):.4f} (need >= 0: {'OK' if gmin >= 0 else 'FAIL'})")

# ---- band on [1/10, 1/5)
EB = grid([Fr(1,10), Fr(1,9), Fr(1,8), Fr(1,7), Fr(1,6), Fr(1,5)], SUB)
KB = len(EB)-1
worst = mpf('inf'); ok = True
for i in range(KB):
    a, b = EB[i], EB[i+1]
    Nc = branchN(a, b)
    Nnx = branchN(EB[i+1], EB[i+2]) if i+2 <= KB else 4   # cell above 1/5 is N=4
    diag = iv.mpf(src_lo(a, b, Nc, Nnx, False))
    cs2 = overlapping(EG, 2*a - WID, 2*b + WID)
    cs3 = overlapping(EG, 3*a - WID, 3*b + WID)
    flux = (q_2m + q_2m1)*iv.mpf(min(gamma[j].a for j in cs2)) + (3*q_3m)*iv.mpf(min(gamma[j].a for j in cs3))
    tot = (diag + flux).a
    if tot < worst: worst = tot
    ok = ok and (tot > 0)
print(f"band: cells={KB}, worst certified sqrt(X)*Sigma lower bound = {float(worst):.4f} -> {'CERTIFIED' if ok else 'FAIL'}")

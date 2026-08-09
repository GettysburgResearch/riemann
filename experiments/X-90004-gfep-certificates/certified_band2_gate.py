"""CERTIFIED band-2 GFEP gate (T2b deliverable 3).

Claim certified: for all X >= X0=2000, all integers n with X/20 < n <= X/10,
all p in [n, min(2n,X+1)):  sqrt(X)*Sigma_{X,n}(p) >= WORST > 0.

Method: extends X-90004/certified_band2_fixed.py.
  Stage 1: gamma_A on [1/5,1]   -- verbatim band-1 occupancy minorant (all sources >=0 there).
  Stage 2: gamma_B on [1/10,1/5) -- occupancy LOWER bound, negative sources, SIGN-AWARE flux:
           windows with possibly-negative gamma use HONEST Q UPPER bounds and count every
           potentially-present parent (2m'-1 and the second ternary-b parent included);
           windows with certified nonnegative gamma use Q lower bounds on always-present parents.
  Stage 3: targets p/X in [1/20,1/5). Parents m'' counted only if m''>=2n; since 2n>X/10 always,
           flux windows are clipped to ratio >= 1/10, and optional families (2p-1, ternary-b)
           enter only when they hurt (min(0, Q_hi * negative gamma)).

Exact parent inventory of child c (multiplicity): 2c (x2), 2c+1 (a2), 2c-1 (b2),
3c,3c-1,3c-2 (a3), and b3-parents {m: floor(2m/3)=c} = [ceil(3c/2), ceil(3(c+1)/2)-1] (1 or 2).
Q(m,c) = mult*c/(2m).  Honest bounds used (m' = child integer, ratio >= a >= a_reg):
  Q(2c,c)=1/2 exact;  Q(2c+1,c) in [1/4 - 1/(8c), 1/4);  Q(2c-1,c) in (1/4, 1/4 + 1/(8c-4)];
  Q(3c-j,c) in [1/6, 1/6 + 1/(3(3c-2))], j=0,1,2;  b3: always-present parent Q in [1/3 - 1/(9c), 1/3],
  optional second parent (c even) Q = c/(3c+2) < 1/3.  All instantiated with c >= a_reg*X0.
"""
from mpmath import iv, mp, mpf
from fractions import Fraction as Fr
iv.dps = 40

def mob(n):
    mu = [0]*(n+1); mu[1] = 1
    for i in range(1, n+1):
        if mu[i]:
            for j in range(2*i, n+1, i): mu[j] -= mu[i]
    return mu
MU = mob(24)
X0 = 2000
def fr2iv(x): return iv.mpf(x.numerator)/iv.mpf(x.denominator)

def C_on(N, tlo, thi):
    t = iv.mpf([fr2iv(tlo).a, fr2iv(thi).b])
    L = -iv.log(t)
    s = iv.mpf(0)
    for k in range(1, N+1):
        if MU[k]: s += MU[k]*(1 + (L - iv.log(k))/2)/iv.sqrt(k)
    return s, t

def branchN(a, b):
    mid = (a+b)/2
    return (mid.denominator)//(mid.numerator)

def src_lo(a, b, Nc, Nnext, positive_region):
    """certified lower bound of sqrt(X)*m'R(m') for m'/X in [a,b], X>=X0 (window widening 1/X0)."""
    if positive_region and b + Fr(1, X0) > 1:
        return mpf(0)
    C1, t1 = C_on(Nc, a, b)
    f1 = C1/iv.sqrt(t1); g1 = C1/(t1*iv.sqrt(t1))
    b2 = b + Fr(1, X0)
    C2, t2 = C_on(Nnext, b, min(b2, Fr(1, 1)))
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

# ---------------- Stage 1: gamma_A on [1/5,1] (band-1 minorant, verbatim constants) --------------
q_2m  = iv.mpf(1)/2
q_2m1_A = iv.mpf(1)/4 - iv.mpf(5)/(4*X0)      # child > X/10 (a fortiori > X/5)
q_2mm1 = iv.mpf(1)/4                          # Q(2c-1,c)=c/(2(2c-1))>=1/4 exact; parent ALWAYS present
q_3m  = iv.mpf(1)/6
q_b3_A = iv.mpf(1)/3 - iv.mpf(5)/(9*X0)       # child > X/5
EG = grid([Fr(1,5), Fr(1,4), Fr(1,3), Fr(1,2), Fr(1,1)], SUB)
KG = len(EG)-1
def next_branch(edges, i, Ncur):
    return branchN(edges[i+1], edges[i+2]) if i+2 <= len(edges)-1 else Ncur
def overlapping(edges, lo, hi):
    return [j for j in range(len(edges)-1) if edges[j+1] > lo and edges[j] < hi]

gammaA = [None]*KG
for i in range(KG-1, -1, -1):
    a, b = EG[i], EG[i+1]
    Nc = branchN(a, b)
    val = iv.mpf(src_lo(a, b, Nc, next_branch(EG, i, Nc), True))
    for fac, q in [(Fr(2,1), q_2m + q_2m1_A + q_2mm1), (Fr(3,1), 3*q_3m), (Fr(3,2), q_b3_A)]:
        lo, hi = fac*a - WID, fac*b + WID
        if fac*b + WID <= 1:
            cs = overlapping(EG, lo, hi)
            assert cs and all(gammaA[j] is not None for j in cs), (i, fac)
            val += q*iv.mpf(min(gammaA[j].a for j in cs))
    gammaA[i] = val
gAmin = min(g.a for g in gammaA)
print(f"stage1 gamma_A: K={KG}, min = {float(gAmin):.4f} (need >= 0: {'OK' if gAmin >= 0 else 'FAIL'})")
assert gAmin >= 0

# ---------------- combined lookup over A and B values --------------------------------------------
EB = grid([Fr(1,10), Fr(1,9), Fr(1,8), Fr(1,7), Fr(1,6), Fr(1,5)], SUB)
KB = len(EB)-1
gammaB = [None]*KB

def win_min(lo, hi):
    """certified min of gamma over ratio window [lo,hi]; asserts full coverage by computed cells."""
    assert lo >= Fr(1,10) - Fr(1,10**9), (lo, hi)
    vals = []
    if lo < Fr(1,5):
        cs = overlapping(EB, lo, min(hi, Fr(1,5)))
        assert cs and all(gammaB[j] is not None for j in cs), ("B cover", lo, hi, cs)
        vals += [gammaB[j].a for j in cs]
    if hi > Fr(1,5):
        cs = overlapping(EG, max(lo, Fr(1,5)), hi)
        assert cs, ("A cover", lo, hi)
        vals += [gammaA[j].a for j in cs]
    assert hi <= Fr(1,1)
    return iv.mpf(min(vals))

def sign_aware(vmin, q_lo, q_hi):
    return q_lo*vmin if vmin.a >= 0 else q_hi*vmin

# ---------------- Stage 2: gamma_B on [1/10,1/5), child integer m' > X/10 ------------------------
# region-uniform honest Q bounds for children with ratio > 1/10 (c >= X0/10 = 200):
binB_lo = iv.mpf(1)/2 + (iv.mpf(1)/4 - iv.mpf(5)/(4*X0)) + iv.mpf(1)/4   # {2c, 2c+1, 2c-1} all present
binB_hi = iv.mpf(1) + iv.mpf(1)/(iv.mpf(8*X0)/10 - 4)                    # + {2c-1} at Q_hi
ternB_lo = iv.mpf(1)/2
ternB_hi = iv.mpf(1)/2 + iv.mpf(2)/(3*(iv.mpf(3*X0)/10 - 2))
b3B_lo = iv.mpf(1)/3 - iv.mpf(10)/(9*X0)
b3B_hi = iv.mpf(2)/3

for i in range(KB-1, -1, -1):
    a, b = EB[i], EB[i+1]
    Nc = branchN(a, b)
    Nnx = branchN(EB[i+1], EB[i+2]) if i+2 <= KB else 4
    val = iv.mpf(src_lo(a, b, Nc, Nnx, False))
    val += sign_aware(win_min(2*a - WID, 2*b + WID), binB_lo, binB_hi)
    val += sign_aware(win_min(3*a - WID, 3*b + WID), ternB_lo, ternB_hi)
    val += sign_aware(win_min(Fr(3,2)*a - WID, Fr(3,2)*b + WID), b3B_lo, b3B_hi)
    gammaB[i] = val
gBmin = min(g.a for g in gammaB)
gBmax = max(g.b for g in gammaB)
print(f"stage2 gamma_B: K={KB}, certified lower bounds in [{float(gBmin):.4f}, {float(gBmax):.4f}]"
      f" (negative handling {'unused - all >=0' if gBmin >= 0 else 'ACTIVE'})")

# ---------------- Stage 3: band-2 targets ---------------------------------------------------------
# region P2a: p/X in [1/20,1/10], child p > X/20 (p >= X0/20 = 100):
binT_lo = iv.mpf(1)/2 + (iv.mpf(1)/4 - iv.mpf(5)/(2*X0))
binT_hi = iv.mpf(1) + iv.mpf(1)/(iv.mpf(8*X0)/20 - 4)
ternT_lo = iv.mpf(1)/2
ternT_hi = iv.mpf(1)/2 + iv.mpf(2)/(3*(iv.mpf(3*X0)/20 - 2))
b3T_hi = iv.mpf(2)/3
TENTH = Fr(1,10)

def clip_min(lo, hi):
    """window min with parent constraint m''>2n>X/10: clip to >=1/10; None if empty."""
    lo2 = max(lo, TENTH)
    if lo2 >= hi: return None
    return win_min(lo2, hi)

worst = mpf('inf'); ok = True; worst_where = None
EB2 = grid([Fr(1,k) for k in range(20, 9, -1)], SUB)
for i in range(len(EB2)-1):
    a, b = EB2[i], EB2[i+1]
    Nc = branchN(a, b)
    Nnx = branchN(EB2[i+1], EB2[i+2]) if i+2 <= len(EB2)-1 else 9
    tot = iv.mpf(src_lo(a, b, Nc, Nnx, False))
    v2 = clip_min(2*a - WID, 2*b + WID); assert v2 is not None
    tot += sign_aware(v2, binT_lo, binT_hi)
    v3 = win_min(3*a - WID, 3*b + WID)
    tot += sign_aware(v3, ternT_lo, ternT_hi)
    vB = clip_min(Fr(3,2)*a - WID, Fr(3,2)*b + WID)
    if vB is not None and vB.a < 0:
        tot += b3T_hi*vB
    t = tot.a
    if t < worst: worst, worst_where = t, ('P2a', float(a), float(b))
    ok = ok and (t > 0)
print(f"stage3 P2a [1/20,1/10]: cells={len(EB2)-1}, worst = {float(worst):.4f}")

# region P2b: p/X in [1/10,1/5), p > X/10 (band-1 flux constants) + b3 penalty when in negative zone
worst_b = mpf('inf'); where_b = None
for i in range(KB):
    a, b = EB[i], EB[i+1]
    Nc = branchN(a, b)
    Nnx = branchN(EB[i+1], EB[i+2]) if i+2 <= KB else 4
    tot = iv.mpf(src_lo(a, b, Nc, Nnx, False))
    tot += sign_aware(win_min(2*a - WID, 2*b + WID), binB_lo, binB_hi)
    tot += sign_aware(win_min(3*a - WID, 3*b + WID), ternB_lo, ternB_hi)
    vB = clip_min(Fr(3,2)*a - WID, Fr(3,2)*b + WID)
    if vB is not None and vB.a < 0:
        tot += b3B_hi*vB
    t = tot.a
    if t < worst_b: worst_b, where_b = t, ('P2b', float(a), float(b))
    ok = ok and (t > 0)
print(f"stage3 P2b [1/10,1/5): cells={KB}, worst = {float(worst_b):.4f}")
W = min(worst, worst_b)
print(f"\nBAND-2 CERTIFICATE (X >= {X0}): worst certified sqrt(X)*Sigma_{{X,n}}(p) = {float(W):.4f} "
      f"at {worst_where if worst < worst_b else where_b} -> {'CERTIFIED' if ok and W > 0 else 'FAIL'}")

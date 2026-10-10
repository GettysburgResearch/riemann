"""Exact checks for reviews/CUBIC_HB_ATTACK.md (adversarial attack on hypothesis (H-B), the PROPOSED
nested comparison order of proposed/CUBIC_FOURTH_MOMENT/SKETCH.md Sec. 3.3-3.6).

EXPLORATION / REVIEW AID.  Exact rational arithmetic (fractions.Fraction) and one sympy identity.
Everything is in units of log Z with M = 1 unless stated.  Nothing here proves a moment bound; it
checks affine ledgers and a finite call graph only.  Failing controls are run and must be DETECTED.

Run: python3 -I cubic_hb_checks.py
"""
from fractions import Fraction as F
from itertools import combinations
import math
import sys

results = []


def record(tag, ok, msg):
    results.append((tag, ok))
    print("[%s] %s  %s" % (tag, "PASS" if ok else "FAIL", msg))


TWO3 = F(2, 3)


def L_of(A, mu):
    """smallest admissible comparison length from (C): (5/6)L >= A - 2/3 + mu"""
    return F(6, 5) * (A - TWO3 + mu)


# ---------------------------------------------------------------------------------------------
# W: well-foundedness of the nested order.  Nodes (beta, j), j = 0 U, 1 C1, 2 C2, 3 R.
# Measure Phi(beta, j) = 4*beta + j.
# ---------------------------------------------------------------------------------------------
def build_edges(nb, k=2, allow_same_stage=False, child_drop=2):
    R = k + 1
    E = []
    for b in range(nb):
        for j in range(R + 1):
            # child calls (second transform): band drops by >= child_drop
            for b2 in range(0, b - child_drop + 1):
                for j2 in range(R + 1):
                    E.append(((b, j), (b2, j2), "child"))
            # separate comparison bound (nested): C_j -> stage j' < j at the same width
            if 1 <= j <= k:
                top = j + 1 if allow_same_stage else j
                for j2 in range(0, top):
                    E.append(((b, j), (b, j2), "comparison"))
            # reflection closure
            if j == R:
                for j2 in range(0, R):
                    E.append(((b, j), (b, j2), "reflection"))
    return E


def phi(node):
    return 4 * node[0] + node[1]


def acyclic(nodes, E):
    adj = {v: [] for v in nodes}
    indeg = {v: 0 for v in nodes}
    for a, b, _ in E:
        adj[a].append(b)
        indeg[b] += 1
    order, stack = [], [v for v in nodes if indeg[v] == 0]
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    if len(order) != len(nodes):
        return False, None
    # longest path (number of nodes) via reverse topological order
    longest = {v: 1 for v in nodes}
    for v in reversed(order):
        for w in adj[v]:
            longest[v] = max(longest[v], 1 + longest[w])
    return True, max(longest.values())


for nb in (8, 16, 32):
    E = build_edges(nb)
    nodes = [(b, j) for b in range(nb) for j in range(4)]
    dec = all(phi(b) < phi(a) for a, b, _ in E)
    ok, lp = acyclic(nodes, E)
    # a chain uses per width level at most: R -> C2 -> C1 -> U (4 nodes), and child drops >= 2 bands
    bound = 4 * ((nb - 1) // 2 + 1)
    record("W1-%d" % nb, dec and ok and lp <= bound,
           "bands=%d: Phi=4*beta+j strictly decreases on all %d edges=%s; acyclic=%s; longest chain=%s <= %d"
           % (nb, len(E), dec, ok, lp, bound))

# control: comparison allowed to land in its own stage (what happens if (R) fails) -> cycle
E = build_edges(8, allow_same_stage=True)
nodes = [(b, j) for b in range(8) for j in range(4)]
dec = all(phi(b) < phi(a) for a, b, _ in E)
ok, _ = acyclic(nodes, E)
record("W1c", (not dec) and (not ok),
       "CONTROL same-stage comparison: Phi decrease=%s, acyclic=%s (must both be False: detected)" % (dec, ok))

# control: manuscript order (k = 1 comparison only to U) is also acyclic -- sanity
E = build_edges(8, k=1)
nodes = [(b, j) for b in range(8) for j in range(3)]
ok, _ = acyclic(nodes, E)
record("W1m", ok and all(phi(b) < phi(a) for a, b, _ in E), "manuscript k=1 order acyclic=%s" % ok)


# W2: exact band drop for children: band = floor(M/(sigma/4)); child width M' = M - sigma + e,
# 0 <= e <= C_* xi <= sigma/2  =>  band(M') <= band(M) - 2.
def band(M, sigma):
    return math.floor(M / (sigma / 4))


def child_band_ok(sigma, emax, n=400):
    for t in range(n + 1):
        M = F(1, 10) + F(3, 2) * F(t, n)
        for e in (F(0), emax / 2, emax):
            Mc = M - sigma + e
            if Mc < 0:
                continue
            if not band(Mc, sigma) <= band(M, sigma) - 2:
                return False
    return True


sigma = F(1, 50)
record("W2", child_band_ok(sigma, sigma / 2),
       "child width M - sigma + C_*xi with C_*xi <= sigma/2: band drops by >= 2 (exact, 401 widths x 3)")
record("W2c", not child_band_ok(sigma, F(7, 8) * sigma),
       "CONTROL C_*xi = 7 sigma/8 (drop sigma/8 < sigma/4): band drop >= 2 fails (must be detected)")


# ---------------------------------------------------------------------------------------------
# M: closing condition and margin, recomputed as an exact 2-variable LP in (mu, b1).
# For each stage, feasibility on an interval is exact at its endpoints (lo(A) max of affine,
# hi(A) min of affine).  Endpoint constraints are affine in (mu, b1):
#   C1 top A=b1, prev 2/3 :  1 - b1 + 2 L(b1) <= 2/3 - mu ;  L(b1) <= b1/2 ;  L(b1) <= b1 - 1/2 - mu
#   C1 bottom A=2/3+     :  L <= A - 1/2 - mu  ->  (6/5) mu <= 1/6 - mu
#   C2 top A=1+d, prev b1:  1 - A + 2 L(A) <= b1 - mu ; caps
#   C2 bottom A=b1        :  1 - b1 + 2 L(b1) <= b1 - mu ; caps
# Each constraint: a*mu + b*b1 <= c.  Maximise mu by vertex enumeration.
# ---------------------------------------------------------------------------------------------
def constraints(delta, lossC=False):
    """return list of (a, b, c) meaning a*mu + b*b1 <= c.  If lossC, mu is a loss c in (C) only."""
    cons = []
    k = F(6, 5)
    m_R = 0 if lossC else 1   # margin coefficient in (R) and caps

    def stage(A_coef_b1, A_const, prev_is_b1):
        # A = A_coef_b1*b1 + A_const ;  L = (6/5)(A - 2/3 + mu)
        # (R): 1 - A + 2L <= prev - m_R*mu
        #   1 - A + (12/5)(A - 2/3) + (12/5)mu + m_R*mu - prev <= 0
        aR = F(12, 5) + m_R
        bR = (-1 + F(12, 5)) * A_coef_b1 - (1 if prev_is_b1 else 0)
        cR = -(1 + (-1 + F(12, 5)) * A_const - F(12, 5) * TWO3 - (0 if prev_is_b1 else TWO3))
        cons.append((aR, bR, cR))
        # cap1: L <= A/2  ->  (6/5)A - 4/5 + (6/5)mu - A/2 <= 0
        cons.append((k, (k - F(1, 2)) * A_coef_b1, -((k - F(1, 2)) * A_const - k * TWO3)))
        # cap2: L <= A - 1/2 - m_R*mu -> (1/5)A - 4/5 + 1/2 + (6/5 + m_R)mu <= 0
        cons.append((k + m_R, F(1, 5) * A_coef_b1, -(F(1, 5) * A_const - F(4, 5) + F(1, 2))))

    stage(1, 0, False)                 # C1 top, A = b1, prev 2/3
    stage(0, TWO3, False)              # C1 bottom limit A -> 2/3
    stage(0, 1 + delta, True)          # C2 top
    stage(1, 0, True)                  # C2 bottom A = b1
    cons.append((-1, 0, 0))            # mu >= 0
    cons.append((0, -1, -TWO3))        # b1 >= 2/3
    cons.append((0, 1, 1 + delta))     # b1 <= 1 + delta
    return cons


def lp_max_mu(cons):
    best = None
    for (a1, b1_, c1), (a2, b2, c2) in combinations(cons, 2):
        det = a1 * b2 - a2 * b1_
        if det == 0:
            continue
        mu = (c1 * b2 - c2 * b1_) / det
        bb = (a1 * c2 - a2 * c1) / det
        if all(a * mu + b * bb <= c for a, b, c in cons):
            if best is None or mu > best[0]:
                best = (mu, bb)
    return best


for delta in (F(0), F(1, 100), F(1, 50), F(1, 20)):
    mu, b1 = lp_max_mu(constraints(delta))
    claim = (11 - 147 * delta) / 612
    record("M1-%s" % delta, mu == claim,
           "delta=%s: exact LP max margin mu=%s (%.6f), claim (11-147d)/612=%s; at b1=%s"
           % (delta, mu, float(mu), claim, b1))

for delta in (F(0), F(1, 100)):
    c, b1 = lp_max_mu(constraints(delta, lossC=True))
    claim = (11 - 147 * delta) / 432
    record("M2-%s" % delta, c == claim,
           "delta=%s: (C)-only loss tolerance c*=%s (%.5f), claim (11-147d)/432=%s" % (delta, c, float(c), claim))

# control: claimed margin + 1/10^6 must be infeasible for every b1 (LP optimum is a max)
cons = constraints(F(0))
mu_bad = F(11, 612) + F(1, 10 ** 6)
feas = any(all(a * mu_bad + b * bb <= cc for a, b, cc in cons)
           for bb in [F(31, 36) + F(t, 10 ** 5) for t in range(-2000, 2001)])
record("M1c", not feas, "CONTROL mu*+1e-6 feasible for some b1 in 31/36 +- 0.02: %s (must be False)" % feas)


# ---------------------------------------------------------------------------------------------
# N: the nested chain C2 -> (reflected comparison datum D') -> C1 -> (reflected comp') -> U,
# simulated with explicit xi in every comparison call (clipping + box enlargement, l. 12797-12807),
# every sub-box scale of the rowwise supremum (l. 12780-12783), padded-core membership
# (l. 12810-12823), the lattice requirement "all four plain lengths >= L" (l. 14686), and the
# comparison's longer factor exceeding M/2 (so its reflection shortens it).
# ---------------------------------------------------------------------------------------------
def nested_chain(delta, mu, xi, b1, n=120, nsub=24):
    top = 1 + delta
    core = F(1, 2) + xi
    worst = {"R2": None, "R1": None}
    for t in range(n + 1):
        A = b1 + (top - b1) * F(t, n)
        if t == 0:
            A = b1 + F(1, 10 ** 9)
        L2 = L_of(A, mu)
        # C2 input in the padded core: lengths n1, n2 <= 1/2 + xi with n1 + n2 = A
        if not (A <= 1 + 2 * xi or A <= top):
            return False, "C2 input above padded core"
        nmin = A - core
        if not (nmin >= L2):
            return False, "C2: a core plain length below L2 at A=%s" % A
        if not (A - L2 > F(1, 2)):
            return False, "C2: comparison longer factor <= 1/2 at A=%s" % A
        if not (F(5, 6) * L2 >= A - TWO3 + mu):
            return False, "C2: (C) fails"
        # reflected comparison datum D': lengths (L2, n') with n' <= 1 - (A - L2) + xi
        nprime = 1 - (A - L2) + xi
        if not (L2 <= core and nprime <= core):
            return False, "D' not in padded core at A=%s (n'=%s)" % (A, nprime)
        Aprime = L2 + nprime
        if not (Aprime <= b1):
            return False, "D' total %s > b1 at A=%s" % (Aprime, A)
        slack = b1 - Aprime
        worst["R2"] = slack if worst["R2"] is None else min(worst["R2"], slack)
        # every sub-box scale of the rowwise supremum: n'' in [0, n']
        for s in range(nsub + 1):
            n2 = nprime * F(s, nsub)
            A2 = L2 + n2
            if A2 <= TWO3:
                continue          # stage U, no core needed
            L1 = L_of(A2, mu)
            if not (min(L2, n2) >= L1):
                return False, "C1 on D': plain length below L1 (A=%s, n''=%s)" % (A, n2)
            if not (L1 <= A2 / 2 and L1 <= A2 - F(1, 2) - mu):
                return False, "C1 caps fail"
            if not (A2 - L1 > F(1, 2)):
                return False, "C1: comparison longer factor <= 1/2"
            A3 = 1 - A2 + 2 * L1 + xi
            if not (A3 <= TWO3):
                return False, "C1 comparison of D' lands above U (A3=%s)" % A3
            sl = TWO3 - A3
            worst["R1"] = sl if worst["R1"] is None else min(worst["R1"], sl)
    return True, worst


for delta in (F(0), F(1, 100)):
    mu = (11 - 147 * delta) / 612
    b1 = (4 + 7 * delta + 17 * mu) / 5
    for xi_label, xi in (("mu/2", mu / 2), ("mu", mu)):
        ok, info = nested_chain(delta, mu, xi, b1)
        record("N1-%s-%s" % (delta, xi_label), ok,
               "delta=%s xi=%s: nested chain C2->D'->C1->U closes with every sub-box; min slacks %s"
               % (delta, xi_label, {k: (str(v) if v is not None else None) for k, v in info.items()}
                  if ok else info))

# also: C1 on ORIGINAL core data (A in (2/3, b1]) -- same checks with prev = 2/3
def c1_original(mu, xi, b1, n=200):
    core = F(1, 2) + xi
    for t in range(1, n + 1):
        A = TWO3 + (b1 - TWO3) * F(t, n)
        L1 = L_of(A, mu)
        if not (A - core >= L1 and A - L1 > F(1, 2) and 1 - A + 2 * L1 + xi <= TWO3):
            return False
    return True


mu0 = F(11, 612)
b10 = F(31, 36)
record("N2", c1_original(mu0, mu0 / 2, b10), "C1 on original core data closes (delta=0, xi=mu*/2)")

# controls: xi = 2 mu (too large for the margin) must break (R); and the manuscript's own
# choice xi <= rho/30 is NOT enough at rho = 1/2 (xi = 1/60 > mu*/... check)
ok, info = nested_chain(F(0), mu0, 2 * mu0, b10)
record("N1c", not ok, "CONTROL xi = 2 mu*: nested chain must fail; got ok=%s (%s)" % (ok, info))
ok, info = nested_chain(F(0), mu0, F(1, 30), b10)
record("N1c2", not ok, "CONTROL xi = rho/30 at rho = M = 1 (manuscript's choice, l. 12981) is too large "
       "for the nested margin: ok=%s (%s)" % (ok, info))


# ---------------------------------------------------------------------------------------------
# P: profile closure.  Reflection on the Mellin side: M W#(s) = M W(1-s) G(s), G(s)=Gamma(s)/Gamma(1-s)
# (l. 12700-12704).  Double reflection: M W##(s) = M W(s) G(1-s) G(s).  Check G(s)G(1-s) = 1.
# Control: a wrong gamma factor Gamma(s+1)/Gamma(1-s) is not involutive.
# ---------------------------------------------------------------------------------------------
try:
    import sympy as sp
    s = sp.symbols("s")
    G = lambda x: sp.gamma(x) / sp.gamma(1 - x)
    inv = sp.simplify(sp.gammasimp(G(s) * G(1 - s)))
    record("P1", inv == 1, "reflection is an involution on profiles: G(s)G(1-s) = %s" % inv)
    Gb = lambda x: sp.gamma(x + 1) / sp.gamma(1 - x)
    invb = sp.simplify(sp.gammasimp(Gb(s) * Gb(1 - s)))
    record("P1c", invb != 1, "CONTROL Gamma(s+1)/Gamma(1-s): product = %s (must differ from 1)" % invb)
except ImportError:
    record("P1", False, "sympy missing")

# P2: number of reflections a profile undergoes per width level along any branch of the nested
# order: R (entry) + one per comparison stage (C2's comp, C1's comp') = k + 1 = 3; and the total
# along a branch is <= (k+1) * (#levels).  Counted along the same-width stage chain R -> C2 -> C1 -> U
# (each comparison stage and R reflects once); this is a count, not a graph search.
refl_per_level = 0
for start_stage in range(4):
    # path inside one band: only comparison/reflection edges
    cnt, j = 0, start_stage
    if j == 3:
        cnt, j = 1, 2
    while j >= 1:
        cnt += 1
        j -= 1
    refl_per_level = max(refl_per_level, cnt)
record("P2", refl_per_level == 3, "reflections per width level along a nested branch: %d (= k+1)" % refl_per_level)


# ---------------------------------------------------------------------------------------------
# C: the conjugation device (l. 12784-12789) is load-bearing for the common-character form
# (l. 13056-13072).  Toy: the cubic character chi mod 7 on Z (values = exponents of omega mod 3).
# A product coefficient f(l1, l2) "factors on the full product" iff it depends only on l1*l2.
# psi(l1)psi(l2): yes.  psi(l1)*conj(psi(l2)) (a reflected factor NOT conjugated back): no.
# ---------------------------------------------------------------------------------------------
g = 3  # primitive root mod 7
dlog = {pow(g, e, 7): e for e in range(6)}


def chi_exp(n):
    n %= 7
    return None if n == 0 else dlog[n] % 3


def depends_only_on_product(f):
    seen = {}
    for l1 in range(1, 7):
        for l2 in range(1, 7):
            key = (l1 * l2) % 7
            v = f(l1, l2)
            if key in seen and seen[key] != v:
                return False
            seen[key] = v
    return True


same = depends_only_on_product(lambda a, b: (chi_exp(a) + chi_exp(b)) % 3)
mixed = depends_only_on_product(lambda a, b: (chi_exp(a) - chi_exp(b)) % 3)
record("C1", same, "psi(l1)psi(l2) depends only on l1 l2 (common character on the full product)")
record("C1c", not mixed, "CONTROL psi(l1)conj(psi(l2)) depends only on l1 l2: %s (must be False)" % mixed)

# ---------------------------------------------------------------------------------------------
# S: the manuscript's OWN path (sextic, L = M/4, threshold 5M/6, M = 1) already centres a reflected
# datum and then reflects its comparison: R -> C -> comparison-reflection -> U, two reflections of
# one profile lineage at one width (l. 12810-12830, 12912-12913, 12950-12985).  Example datum
# (0.45, 0.6), xi = 1/100.
# ---------------------------------------------------------------------------------------------
xi = F(1, 100)
n1, n2 = F(45, 100), F(6, 10)
A = n1 + n2
r_n2 = 1 - n2 + xi                      # R: reflect the factor longer than 1/2 (eq. centered-reflection-length)
Astar = n1 + r_n2
core = n1 <= F(1, 2) + xi and r_n2 <= F(1, 2) + xi and Astar <= 1 + 2 * xi
centred = Astar > F(5, 6)
Lm = F(1, 4)
comp_long = Astar - Lm                  # comparison lengths (L, A* - L); the long one carries profile 2
second = comp_long > F(1, 2)
Acomp = Lm + (1 - comp_long) + xi       # reflect the comparison's long factor
record("S1", A > 1 and core and centred and second and Acomp <= F(5, 6),
       "manuscript path for (0.45,0.6): A=%s not core; after R A*=%s in core, > 5/6 -> centred; comparison "
       "long factor %s > 1/2 reflected again; A_comp=%s <= 5/6 -> U.  Two reflections at one width."
       % (A, Astar, comp_long, Acomp))

npass = sum(1 for _, ok in results if ok)
print("SUMMARY %d/%d PASS (controls are the checks tagged ...c / ...c2; a PASS there means the "
      "deliberately broken variant was detected)" % (npass, len(results)))
sys.exit(0 if npass == len(results) else 1)

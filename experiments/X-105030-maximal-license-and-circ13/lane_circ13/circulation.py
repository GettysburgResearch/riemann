"""
Two-leaf (plus grandchild) occurrence-level Hoffman circulation model for the
odd-history wall, at X = 67*q*y.

Occurrences (global units), squarefree d | P_61:
  R_d : k = d        mass m0(d) = d^{-1/2} T(X/d),      sign  mu(d)     (leaf L0, empty history)
  A_d : k = 67 d     mass m1(d) = (67d)^{-1/2} T(B1/d), sign -mu(d)     (leaf L1, history (67)), B1 = X/67 = q*y
  B_d : k = 67 q d   mass m2(d) = (67qd)^{-1/2} T(y/d), sign +mu(d)     (leaf L2, history (67,q))
T(u) = 4 sqrt(u) - 3 for u >= 1 else 0.

Odd (sign -1) occurrences are demands (lower=upper=mass); even are capacities [0,mass].
Licensed edges (even -> odd):
  within leaf: same m-layer, d_e <= d_o  (nested activation / L-99020 e<=o license)
  cross-leaf : R_d -> A_d (exists iff mu(d)=+1) and A_d -> B_d (iff mu(d)=-1),
               same d = same compact-fibre coordinate; parent->child only
               (child->parent would violate k_e <= k_o).

Complete binding cut family (derived in analysis; verified vs LP for base X):
  down-sets with t2 <= t1 <= t0:
  V(t0,t1,t2) = [D0-C0](t0) + [D1-C1](t1) + [D2-C2](t2)
  plus pure-leaf-0 cuts (t1=t2=0).  Feasible iff max V over nonempty cuts <= 0.
"""
import sys
from mpmath import mp, mpf, sqrt, nstr

mp.dps = 30

PRIMES61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def smooth_divisors(bound):
    out = [(1, 1)]
    for p in PRIMES61:
        new = []
        for d, mu in out:
            nd = d * p
            if nd <= bound:
                new.append((nd, -mu))
        out += new
    out.sort()
    return out

def T(u):
    return 4*sqrt(u) - 3 if u >= 1 else mpf(0)

def analyze(q, y, verbose=True):
    X = 67*q*y
    B1 = q*y
    divs0 = smooth_divisors(X)
    divs1 = [(d,mu) for d,mu in divs0 if d <= B1]
    divs2 = [(d,mu) for d,mu in divs0 if d <= y]

    r67 = 1/sqrt(mpf(67)); rq = 1/sqrt(mpf(q))

    # leaf-1 net atoms (R-96500 convention): t_d = d^{-1/2}[T(B1/d) - q^{-1/2}T(y/d)]
    net_deficit = mpf(0); net_prof_max = mpf(-1e9); net_prof_arg = None
    run = mpf(0)
    for d, mu in divs1:
        td = (T(mpf(B1)/d) - rq*T(mpf(y)/d))/sqrt(mpf(d))
        run += mu*td
        if run > net_prof_max:
            net_prof_max = run; net_prof_arg = d
    net_deficit = run  # = E_T - O_T

    # global-unit prefix functions
    # leaf 0: F0(t) = C0-D0 prefix (root Hall margin)
    F0 = []   # list of (d, F0 value after including d)
    run = mpf(0)
    for d, mu in divs0:
        m0 = T(mpf(X)/d)/sqrt(mpf(d))
        run += mu*m0
        F0.append((d, run))
    F0_final = run
    F0_min = min(v for _, v in F0); F0_argmin = [d for d, v in F0 if v == F0_min][0]

    # leaf 1 (global units): G1(t) = D1-C1 = sum_{d<=t} mu(d) * m1(d) with demand at mu=+1
    #   D1-C1 = sum mu(d) (67d)^{-1/2} T(B1/d)
    G1 = []
    run = mpf(0)
    for d, mu in divs1:
        m1 = r67*T(mpf(B1)/d)/sqrt(mpf(d))
        run += mu*m1
        G1.append((d, run))
    G1_final = run
    G1_max = max(v for _, v in G1); G1_argmax = [d for d, v in G1 if v == G1_max][0]

    # leaf 2: G2(t) = D2-C2 = sum -mu(d) m2(d)
    G2 = []
    run = mpf(0)
    for d, mu in divs2:
        m2 = r67*rq*T(mpf(y)/d)/sqrt(mpf(d))
        run += -mu*m2
        G2.append((d, run))
    G2_prefmax = []  # prefix max of max(0, G2(t2)) for t2 <= t
    cur = mpf(0)
    for d, v in G2:
        cur = max(cur, v)
        G2_prefmax.append((d, cur))
    G2_max = cur

    # coupled subtree deficit profile: H1(t1) = G1(t1) + max_{t2<=t1} max(0,G2(t2))
    # then binding cut: V(t0) = -F0(t0) + max_{t1 <= min(t0,B1)} max(0, H1(t1))
    H1 = []
    j = 0; g2c = mpf(0)
    for d, v in G1:
        while j < len(G2_prefmax) and G2_prefmax[j][0] <= d:
            g2c = G2_prefmax[j][1]; j += 1
        H1.append((d, v + g2c))
    # prefix max of H1 (with 0 = empty leaf-1 cut)
    H1_prefmax = []
    cur = mpf(0)
    for d, v in H1:
        cur = max(cur, v)
        H1_prefmax.append((d, cur))
    H1_max = cur; H1_argmax = [d for d, v in H1 if v == H1_max][0]

    # slack(t0) = F0(t0) - H1_prefmax(min(t0,B1)); min over t0 (nonempty cuts)
    slack_min = None; slack_arg = None
    j = 0; h1c = mpf(0)
    for d, v in F0:
        while j < len(H1_prefmax) and H1_prefmax[j][0] <= d:
            h1c = H1_prefmax[j][1]; j += 1
        s = v - h1c
        if slack_min is None or s < slack_min:
            slack_min = s; slack_arg = d
    feasible = slack_min > 0

    res = dict(q=q, y=y, X=X, B1=B1,
        n0=len(divs0), n1=len(divs1), n2=len(divs2),
        net_deficit=net_deficit, net_prof_max=net_prof_max, net_prof_arg=net_prof_arg,
        F0_min=F0_min, F0_argmin=F0_argmin, F0_final=F0_final,
        G1_max=G1_max, G1_argmax=G1_argmax, G1_final=G1_final,
        G2_max=G2_max,
        H1_max=H1_max, H1_argmax=H1_argmax,
        slack_min=slack_min, slack_arg=slack_arg, feasible=feasible)
    if verbose:
        f = lambda v: nstr(v, 12)
        print(f"(q,y)=({q},{y}) X={X} B1={B1} | n0={res['n0']} n1={res['n1']} n2={res['n2']}")
        print(f"  leaf-1 net E_T-O_T = {f(net_deficit)}  profile max {f(net_prof_max)} at d={net_prof_arg}")
        print(f"  parent-layer G1max(global) = {f(G1_max)} at d={G1_argmax}; G1(B1)={f(G1_final)}; leaf-norm G1max*sqrt67 = {f(G1_max*sqrt(mpf(67)))}")
        print(f"  G2max = {f(G2_max)}  (grandchild ever in deficit: {G2_max>0})")
        print(f"  root F0: min {f(F0_min)} at d={F0_argmin}; total {f(F0_final)}")
        print(f"  subtree deficit H1max = {f(H1_max)} at d={H1_argmax}")
        print(f"  COUPLED MIN SLACK = {f(slack_min)} at t0=d={slack_arg}   FEASIBLE={feasible}")
    return res

if __name__ == "__main__":
    results = []
    fam = [(71,13),(71,11),(73,13),(79,17),(83,19),(89,23),(101,29),(151,43),(211,61),(331,53)]
    for q, y in fam:
        results.append(analyze(q, y))
        sys.stdout.flush()

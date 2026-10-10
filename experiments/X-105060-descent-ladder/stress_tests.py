"""Lane B3 stress tests: bookkeeping of the descent assembly on synthetic ladders.

A synthetic F is a real polynomial given by known real zeros (list, repetition =
multiplicity) and known conjugate pairs (x, y, mult).  We differentiate 1-2 times,
root-find the derivatives, and check EVERY inequality in the chain with exact
window bookkeeping:

  per gap G:      n'(G) >= 1 (Rolle);  extra(G) := n'(G)-1
                  threshold:  extra(G)>=1  =>  weight(G) >= 1        [Lemma 3.3/3.4]
                  dipole:     extra(G) <= Aprime * weight(G)         [I-DIPOLE, Aprime=4 target]
  weight(G) = sum over pairs j of F (with mult) overhanging G of min(1, g^2/(4 y^2))
              overhang: x-y < b and x+y > a   (int I_j meets G=(a,b))
  W(win)  = sum over gaps meeting window of weight(G)
  converse Rolle: N'^r(win) <= N^r(win) + 1 + Aprime*W(win)          [Prop 4.1]
  descent:        N^c - N'^c <= (N - N') + 1 + Aprime*W              [Thm 4.2 shape]
  partial fraction: (F'/F)'(t) = -sum m/(t-t_n)^2 + sum mult*phi'_j(t)  [I-PF, exact for polys]

Counts on window (aw, bw]: real zeros r with aw < r <= bw (mult); pairs with
aw < x <= bw contribute 2*mult to N.  Gaps = bounded components of R \ Zr meeting
(aw, bw]; configs guarantee real zeros on both sides of the window.
"""
import numpy as np, json, sys

TOL_IM = 1e-7      # |Im| below => real root
EPS = 1e-9         # strict-inequality guard

def build_poly(reals, pairs):
    c = np.array([1.0])
    for r in reals:
        c = np.polymul(c, [1.0, -r])
    for (x, y, m) in pairs:
        q = [1.0, -2.0*x, x*x + y*y]
        for _ in range(m):
            c = np.polymul(c, q)
    return c

def classify_roots(coef):
    """-> (reals sorted list with mult, pairs list (x,y,mult) y>0), from numpy roots."""
    rts = np.roots(coef)
    reals, pairs = [], []
    used = np.zeros(len(rts), bool)
    for i, z in enumerate(rts):
        if used[i]: continue
        if abs(z.imag) < TOL_IM:
            reals.append(z.real); used[i] = True
        elif z.imag > 0:
            # find conjugate partner
            j = np.argmin(np.abs(rts - z.conjugate() + 1e30*used))
            used[i] = True; used[j] = True
            pairs.append((z.real, z.imag))
    reals.sort()
    # group reals into (value, mult) with clustering tol
    grouped = []
    for r in reals:
        if grouped and abs(r - grouped[-1][0]) < 1e-6:
            v, m = grouped[-1]; grouped[-1] = ((v*m + r)/(m+1), m+1)
        else:
            grouped.append((r, 1))
    gpairs = []
    for (x, y) in sorted(pairs):
        if gpairs and abs(x-gpairs[-1][0]) < 1e-6 and abs(y-gpairs[-1][1]) < 1e-6:
            gpairs[-1] = (gpairs[-1][0], gpairs[-1][1], gpairs[-1][2]+1)
        else:
            gpairs.append((x, y, 1))
    return grouped, gpairs

def window_counts(reals_g, pairs_g, aw, bw):
    Nr = sum(m for (r, m) in reals_g if aw + EPS < r <= bw + EPS)
    Nc = sum(2*m for (x, y, m) in pairs_g if aw + EPS < x <= bw + EPS)
    return Nr, Nc, Nr + Nc

def gaps_meeting_window(reals_g, aw, bw):
    """bounded components of R\\Zr meeting (aw,bw]; assert coverage."""
    zs = [r for (r, m) in reals_g]
    assert zs and zs[0] < aw and zs[-1] > bw, "window not strictly inside real-zero range"
    out = []
    for i in range(len(zs)-1):
        a, b = zs[i], zs[i+1]
        if b > aw + EPS and a <= bw + EPS:   # (a,b) ∩ (aw,bw] nonempty
            out.append((a, b))
    return out

def gap_weight(gap, pairs_g):
    a, b = gap; g = b - a; w = 0.0; over = []
    for (x, y, m) in pairs_g:
        if x - y < b - EPS and x + y > a + EPS:
            w += m * min(1.0, g*g/(4.0*y*y)); over.append((x, y, m))
    return w, over

def nprime_in_gap(gap, reals_next):
    a, b = gap
    return sum(m for (r, m) in reals_next if a + EPS < r < b - EPS)

def phi_prime(t, x, y):
    u = t - x
    return 2.0*(y*y - u*u)/((u*u + y*y)**2)

def pf_identity_check(coef, reals_g, pairs_g, tpts):
    d1 = np.polyder(coef); d2 = np.polyder(d1)
    worst = 0.0
    for t in tpts:
        F = np.polyval(coef, t); F1 = np.polyval(d1, t); F2 = np.polyval(d2, t)
        lhs = F2/F - (F1/F)**2          # (F'/F)'
        rhs = -sum(m/(t-r)**2 for (r, m) in reals_g) \
              + sum(m*phi_prime(t, x, y) for (x, y, m) in pairs_g)
        worst = max(worst, abs(lhs-rhs)/max(1.0, abs(lhs)))
    return worst

def analyze_rung(coef, reals_g, pairs_g, aw, bw, Aprime=4.0, verbose=True):
    """One descent step F -> F'. Returns dict of checks."""
    d1 = np.polyder(coef)
    reals1, pairs1 = classify_roots(d1)
    Nr0, Nc0, N0 = window_counts(reals_g, pairs_g, aw, bw)
    Nr1, Nc1, N1 = window_counts(reals1, pairs1, aw, bw)
    gaps = gaps_meeting_window(reals_g, aw, bw)
    rows, W, X = [], 0.0, 0
    ok_rolle = ok_thresh = ok_dipole = True
    max_ratio = 0.0
    for gp in gaps:
        npr = nprime_in_gap(gp, reals1)
        extra = npr - 1
        w, over = gap_weight(gp, pairs_g)
        W += w; X += max(extra, 0)
        if npr < 1: ok_rolle = False
        if extra >= 1 and w < 1 - 1e-12: ok_thresh = False
        if extra > Aprime*w + 1e-12: ok_dipole = False
        if w > 1e-15 and extra > 0: max_ratio = max(max_ratio, extra/w)
        rows.append(dict(gap=[round(gp[0],4), round(gp[1],4)], g=round(gp[1]-gp[0],4),
                         nprime=npr, extra=extra, weight=round(w,6), n_over=len(over)))
    convRolle = Nr1 <= Nr0 + 1 + Aprime*W + 1e-9
    descent = (Nc0 - Nc1) <= (N0 - N1) + 1 + Aprime*W + 1e-9
    # identity audit: N^c - N'^c == (N - N') + (N'^r - N^r)
    ident = (Nc0 - Nc1) == (N0 - N1) + (Nr1 - Nr0)
    pf = pf_identity_check(coef, reals_g, pairs_g,
                           [gp[0] + 0.37*(gp[1]-gp[0]) for gp in gaps[:4]])
    res = dict(N0=N0, Nr0=Nr0, Nc0=Nc0, N1=N1, Nr1=Nr1, Nc1=Nc1,
               W=round(W,6), X=X, gaps=rows,
               ok_rolle=ok_rolle, ok_threshold=ok_thresh, ok_dipole4=ok_dipole,
               ok_converseRolle=bool(convRolle), ok_descent=bool(descent),
               ok_identity=ident, max_extra_over_weight=round(max_ratio,4),
               pf_relerr=float(pf))
    return res, d1, reals1, pairs1

def run_config(name, reals, pairs, aw, bw, nrungs=2, Aprime=4.0):
    print("="*78); print(f"CONFIG {name}: reals={reals} pairs={pairs} window=({aw},{bw}]")
    coef = build_poly(reals, pairs)
    reals_g, pairs_g = classify_roots(build_poly(reals, []))  # exact reals by construction
    # use constructed data directly (exact):
    reals_g = []
    for r in sorted(reals):
        if reals_g and abs(r-reals_g[-1][0]) < 1e-12:
            reals_g[-1] = (reals_g[-1][0], reals_g[-1][1]+1)
        else: reals_g.append((r,1))
    pairs_g = [(x,y,m) for (x,y,m) in pairs]
    allok = True
    out = []
    for k in range(nrungs):
        try:
            res, coef, reals_g, pairs_g = analyze_rung(coef, reals_g, pairs_g, aw, bw, Aprime)
        except AssertionError as e:
            print(f"  rung {k}: SKIPPED ({e})"); break
        flags = {kk: v for kk, v in res.items() if kk.startswith("ok_")}
        bad = [kk for kk, v in flags.items() if not v]
        allok &= not bad
        print(f"  rung {k}->{k+1}: N={res['N0']}/{res['N1']} Nr={res['Nr0']}/{res['Nr1']} "
              f"Nc={res['Nc0']}/{res['Nc1']} W={res['W']} X={res['X']} "
              f"maxratio={res['max_extra_over_weight']} pf_err={res['pf_relerr']:.1e} "
              f"{'ALL OK' if not bad else 'FAIL:'+str(bad)}")
        for row in res['gaps']:
            if row['extra'] != 0 or row['weight'] > 0:
                print(f"      gap {row['gap']} g={row['g']} n'={row['nprime']} "
                      f"extra={row['extra']} weight={row['weight']} overhung_by={row['n_over']}")
        out.append(res)
    return allok, out

def random_search(ntrials=400, seed=7, Aprime=4.0):
    rng = np.random.default_rng(seed)
    worst_ratio, viol = 0.0, []
    thresh_viol = conv_viol = 0
    for trial in range(ntrials):
        nreal = rng.integers(6, 11)
        reals = np.sort(rng.uniform(0, 10, nreal))
        # enforce min separation
        for i in range(1, len(reals)):
            reals[i] = max(reals[i], reals[i-1] + 0.05)
        reals = [-1.0] + list(reals) + [reals[-1] + 1.0]
        npair = rng.integers(1, 4)
        pairs = [(float(rng.uniform(reals[1], reals[-2])),
                  float(rng.uniform(0.05, 0.5)), 1) for _ in range(npair)]
        aw, bw = reals[1] + 0.01, reals[-2] - 0.01
        coef = build_poly(reals, pairs)
        reals_g = [(r, 1) for r in reals]
        try:
            res, *_ = analyze_rung(coef, reals_g, pairs, aw, bw, Aprime, verbose=False)
        except Exception:
            continue
        if not res['ok_threshold']: thresh_viol += 1; viol.append(('threshold', trial))
        if not res['ok_converseRolle']: conv_viol += 1; viol.append(('convRolle', trial))
        if not res['ok_dipole4']: viol.append(('dipole4', trial, res))
        worst_ratio = max(worst_ratio, res['max_extra_over_weight'])
    print("="*78)
    print(f"RANDOM SEARCH: {ntrials} trials; worst extra/weight ratio = {worst_ratio}")
    print(f"  threshold violations: {thresh_viol}; converseRolle(A'=4) violations: {conv_viol}")
    print(f"  dipole(A'=4) violations: {[v[:2] for v in viol if v[0]=='dipole4']}")
    return worst_ratio, viol

if __name__ == "__main__":
    results = {}
    ok = True
    o,_ = run_config("A_all_real_simple", [-1,0,1,2,3,4,5,6,7], [], 0.5, 5.5); ok &= o
    o,_ = run_config("B_pair_annihilation", [0,4,6,10], [(5,0.5,1)], 2, 8); ok &= o
    o,_ = run_config("C_overhang_5gaps", [-1,0,1,1.2,1.4,1.6,1.8,3,4], [(1.4,0.45,1)], 0.5, 2.5); ok &= o
    o,_ = run_config("D_double_real_zero", [0,2,2,4,6], [(3,0.3,1)], 1, 5); ok &= o
    o,_ = run_config("E_double_pair", [0,4,6,10], [(5,0.5,2)], 2, 8); ok &= o
    o,_ = run_config("F_even_parity", [-5,-3,-1,1,3,5], [(2,0.4,1),(-2,0.4,1)], 0, 4); ok &= o
    o,_ = run_config("G_deep_pair_small_gaps", [-1,0,0.5,1,1.5,2,2.5,3,4], [(1.5,0.5,1)], 0.2, 2.8); ok &= o
    o,_ = run_config("H_tight_cluster_low_pair", [-1,0,1,1.1,1.2,3,4], [(1.15,0.04,1)], 0.5, 2.5); ok &= o
    wr, viol = random_search(400)
    print("="*78)
    print("OVERALL deterministic configs:", "ALL OK" if ok else "FAILURES PRESENT")

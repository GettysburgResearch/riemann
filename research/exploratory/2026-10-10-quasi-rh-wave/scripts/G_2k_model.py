"""Row-count exponent R*(delta,x) under hypothetical moment/large-value lemmas, and the resulting
zero-free boundary B via the Section-20 exponent model of notes/stage3_closed.py (same E, Blow, side_ok)."""
import numpy as np
from math import sqrt
import sys
sys.path.insert(0, '.')
from stage3_closed import E, Blow, side_ok

ALPHA = 5/6

def Rstar_generic(delta, x, kappa, mode, tmax=1.5, nr=301, nt=61):
    """count exponent: min over t in [1,tmax] of max( max over s>=0 of max over r of min(count_M, count_S, count_mixed), L(t) )
    rows pick (r, s) adversarially: r in [t-1/2, min(t,1)]... (r up to t allowed; r>1 uses Lemma 17.6 slope), m = t+s-r in [0,1/2]."""
    best_t = np.inf
    for t in np.linspace(1.0, tmax, nt):
        worst = -np.inf
        for s in np.linspace(0, 0.5, 26):
            for r in np.linspace(max(t-0.5, 0.0), t, nr):
                m = t + s - r
                if m < -1e-12 or m > 0.5 + 1e-12: continue
                m = max(m, 0.0)
                cnts = []
                # ---- inverse witness counts ----
                # Lemma 17.6 / 17.1 (k=1): e(r) - delta r with primes capacity (1-r)/2 for r<1
                if r <= 1:
                    cnts.append(1 - delta*r - 2*x*delta*(1-r)/2)
                else:
                    cnts.append(1 - ALPHA + (ALPHA-delta)*r)
                if mode.get('inv_k', 1) >= 2:
                    for k in range(2, mode['inv_k']+1):
                        if k*r <= 1: cnts.append(1 - k*delta*r - 2*x*delta*(1-k*r)/2)
                if mode.get('huxley', False):
                    # Huxley-type large values for M_r: R << N V^-2 + N T V^-6, N=U^r, T=U, V^2=U^{delta r}
                    cnts.append(max(r - delta*r, 1 + r - 3*delta*r))
                if mode.get('inv_ideal', False):
                    cnts.append(1 - delta)
                # ---- plain witness counts ----
                # Lemma 18.1 (k=2): 1 - 2 delta m - 2 x delta (1-2m)/(6 kappa) for 2m<=1 ; k=1 copy: m+6kz<=1
                cnts.append(1 - 2*delta*m - 2*x*delta*max(0.0, 1-2*m)/(6*kappa))
                K = mode.get('plain_k', 2)
                for k in range(3, K+1):
                    if k*m <= 1: cnts.append(1 - k*delta*m - 2*x*delta*(1-k*m)/(6*kappa))
                if mode.get('plain_overshoot', False):   # MVT-type Sum|S|^{2k} << U^{max(1,km)}
                    for k in range(2, 12):
                        cnts.append(max(1, k*m) - k*delta*m)
                # ---- hybrid M_r S_m moment ----
                if mode.get('hybrid', None) is not None:
                    cap = mode['hybrid']   # Lindelof quality for r+m <= cap
                    if r + m <= cap + 1e-12: cnts.append(1 - delta*(r+m))
                if mode.get('hybrid_overshoot', False):
                    cnts.append(max(1, r+m) - delta*(r+m))
                if mode.get('ideal', False):
                    cnts.append(1 - delta)
                c = min(cnts)
                worst = max(worst, c)
        Lt = 1 - delta + (ALPHA - delta)*(t-1)
        best_t = min(best_t, max(worst, Lt))
    RN = 1 - 2*ALPHA*delta/(3*ALPHA-delta)
    return min(best_t, RN)

def best_B(kappa, dmax, mode, d0=0.02, nd=40, nx=11):
    dgrid = np.linspace(d0, dmax, nd); xgrid = np.linspace(0, 0.5, nx)
    Rtab = np.array([[Rstar_generic(d, x, kappa, mode) for x in xgrid] for d in dgrid])
    def feas(l):
        best = (np.inf, None, None)
        for b in np.linspace(0.002, 0.35, 175):
            if not side_ok(l, b, dmax, d0): continue
            w = -np.inf; arg = None
            for i, d in enumerate(dgrid):
                for j, x in enumerate(xgrid):
                    e = E(b, l, d, x, Rtab[i, j])
                    if e > w: w, arg = e, (d, x, Rtab[i, j])
            if w < best[0]: best = (w, b, arg)
        return best
    lo, hi = 0.164, 0.30
    if feas(lo)[0] > 0: return None
    for _ in range(22):
        mid = (lo+hi)/2
        if feas(mid)[0] <= 0: lo = mid
        else: hi = mid
    w, b, arg = feas(lo)
    return Blow(lo, b), lo, b, arg

if __name__ == "__main__":
    dc = (49-sqrt(921))/48
    scen = [("baseline (paper/Liu)", {}),
            ("plain 2k-th moments, k<=3 (3m<=1)", {'plain_k': 3}),
            ("plain 2k-th moments, k<=6", {'plain_k': 6}),
            ("plain moments with MVT overshoot", {'plain_overshoot': True}),
            ("inverse 2k-th moments, k<=3 (kr<=1)", {'inv_k': 3}),
            ("Huxley large values for M_r", {'huxley': True}),
            ("hybrid |M_r S_m|^2, r+m<=1", {'hybrid': 1.0}),
            ("hybrid r+m<=1.25", {'hybrid': 1.25}),
            ("hybrid r+m<=1.5 (all pairs)", {'hybrid': 1.5}),
            ("hybrid with MVT overshoot", {'hybrid_overshoot': True}),
            ("ideal counts 1-delta", {'ideal': True})]
    print("R* at critical class delta=%.4f x=1/2 kappa=3/4:" % dc)
    for name, mode in scen:
        print("  %-40s R*=%.4f" % (name, Rstar_generic(dc, 0.5, 0.75, mode)))
    print("\nBoundary B (kappa=3/4, dmax=3/4, coarse grid):")
    for name, mode in scen:
        res = best_B(0.75, 0.75, mode)
        if res: print("  %-40s B=%.6f l=%.5f b=%.4f crit(delta,x,R*)=(%.3f,%.3f,%.4f)" % ((name, res[0], res[1], res[2]) + res[3]))
        else: print("  %-40s infeasible" % name)

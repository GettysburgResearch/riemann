# floor_density.py -- note X: a Selberg/Montgomery-type zero density for the sextic family near the floor,
# fed into the Part II row bookkeeping.  Model = scripts/quick_E.py (reproduces Liu's 0.874957), unmodified
# except for the row-count function.  Run: python3 -I floor_density.py
import numpy as np, math
alpha, d0, a0 = 5/6, 1/50, 51/100

# ---- 1. the paper's own count near the floor (Prop. 19.2 / (20.8)), closed form (note A) ----
def Rstar(delta, x):
    Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x); J = (alpha - delta)*Dx + delta*Px
    t = 1 + delta*Px/(2*J)
    return 1 - delta + (alpha - delta)*(t - 1)
print("== 1. slope of the paper's own near-floor count R*(delta,x) at delta=delta0 (Prop 19.2) ==")
for x in [0.0, 0.25, 0.5]:
    eps = 1e-7; s = (Rstar(d0+eps, x) - Rstar(d0, x))/eps
    print(f"  x={x:.2f}: R*(delta0+)={Rstar(d0,x):.5f}, dR*/ddelta={s:+.4f}  (c_delta={-s:.3f}; per unit sigma: c_sigma={-2*s:.3f});"
          f" small-delta limit 1-delta(1-Px/2Dx): c={1-((2-8*x/9)*(1-x))/(2*(3-17*x/9)):.3f}")

# ---- 2. Selberg/Montgomery density from a mollified second moment of length U^theta + sextic large sieve ----
# N_U(1/2+delta/2, T) << U^{1 - theta*delta + eps} T^A   (derivation in the note, Sec. 1):  R_D(delta) = 1 - theta*delta
def R_dens(delta, theta):  return 1 - theta*delta
thetas = {"DIPP theta=1/11": 1/11, "best large-sieve theta=1/2": 1/2, "density hypothesis (theta=1)": 1.0}
print("\n== 2. density-type count 1 - theta*delta vs the paper's R* (both valid; the paper uses the smaller) ==")
for d in [d0, 0.05, 0.1, 0.2, 0.389, 0.6, alpha]:
    print(f"  delta={d:.3f}: R*(x=0)={Rstar(d,0):.4f} R*(x=1/2)={Rstar(d,.5):.4f} | " +
          "  ".join(f"{k}: {R_dens(d,t):.4f}" for k,t in thetas.items()))

# ---- 3. feed into the endpoint model (quick_E.py) ----
def make_R(theta=None, nearfloor_only=None):
    def R(delta, x):
        r = Rstar(delta, x)
        if theta is None: return r
        rd = R_dens(delta, theta)
        if nearfloor_only is not None: rd = np.where(delta <= nearfloor_only, rd, 1.0)
        return np.minimum(r, rd)
    return R
def E(b, ell, delta, x, R):
    C0 = -1/4 + 5*ell/4 + b/6; h = (1 + b + 3*ell)/2
    return C0 + delta*(1/2 + ell) + x*delta*ell - h*(1 - R(delta, x))
def Emax(b, ell, R, n=241):
    ds = np.linspace(0, alpha, n); xs = np.linspace(0, 1/2, n)
    D, X = np.meshgrid(ds, xs, indexing='ij'); v = E(b, ell, D, X, R)
    i = np.unravel_index(np.argmax(v), v.shape); return v[i], ds[i[0]], xs[i[1]]
B = lambda ell: 11/12 - ell/4
def bestB(R):
    best = None
    for b in np.linspace(0.0, 0.3, 61):
        lo, hi = 0.0, 0.4
        for _ in range(40):
            mid = (lo+hi)/2
            if Emax(b, mid, R, 121)[0] <= 0: lo = mid
            else: hi = mid
        if best is None or lo > best[1]: best = (b, lo)
    b0, l0 = best
    for b in np.linspace(b0-0.01, b0+0.01, 41):
        lo, hi = l0-0.01, l0+0.01
        for _ in range(40):
            mid = (lo+hi)/2
            if Emax(b, mid, R, 401)[0] <= 0: lo = mid
            else: hi = mid
        if lo > best[1]: best = (b, lo)
    em = Emax(best[0], best[1], R, 801)
    return best[0], best[1], B(best[1]), em
print("\n== 3. endpoint optimum (quick_E model) with the row count replaced by min(R*, 1 - theta*delta) ==")
bnew = -4/29 + 230*math.sqrt(921)/26709; lnew = (33 + 8*math.sqrt(921))/1653
print(f"  Liu's point: b={bnew:.6f} ell={lnew:.6f} B={B(lnew):.9f}")
rows = [("baseline (paper's R*)", make_R()),
        ("+DIPP density theta=1/11, all delta", make_R(1/11)),
        ("+density theta=1/2, all delta", make_R(1/2)),
        ("+density hypothesis 1-delta, all delta", make_R(1.0)),
        ("+density hypothesis, near floor only (delta<=0.1)", make_R(1.0, 0.1)),
        ("+density hypothesis, near floor only (delta<=0.3)", make_R(1.0, 0.3))]
for name, R in rows:
    b, l, Bv, em = bestB(R)
    print(f"  {name:52s}: b={b:.6f} ell={l:.6f} B={Bv:.6f} active(delta={em[1]:.3f}, x={em[2]:.3f}) Emax={em[0]:+.2e}")

# ---- 4. (N.3) floor-mechanism bookkeeping (note N) with the near-floor count improved; f = infinity ceiling ----
print("\n== 4. note N's (N.3) ceiling with the subtracted near-floor bins counted by min(R*, 1-theta*delta); f=inf ==")
def geom(b, l): return (1-b-l)/2, (1+b-l)/2, (1+b+3*l)/2
def floor_gain(b, l, R, pl=True):
    lx, ly, h = geom(b, l); C0 = -1/4 + 5*l/4 + b/6; E_floor = C0 + 3*d0/4
    ds = np.linspace(d0, alpha, 160); xs = np.linspace(0, .5, 11); D, X = np.meshgrid(ds, xs, indexing='ij')
    Ebin = E(b, l, D, X, R); numer = -h*(D-d0)/4 if pl else 0.0
    best = (-1, None)
    for r in np.concatenate([np.linspace(1.0, 2.0, 41), np.linspace(2.0, 6.0, 41)]):
        for eta in np.linspace(0.0, 0.45, 91):
            trunc = E_floor + eta - r*eta*h
            Delta = -(D-d0)*(1-ly)/2 + eta + numer + h*r*np.maximum((D-d0)/2 - eta, 0)
            new = max(trunc, (Ebin + Delta).max()); g = E_floor - new
            if g > best[0]: best = (g, (r, eta))
    return best
for (b, l) in [(1/8, 1/6), (bnew, lnew)]:
    for name, R in rows[:4]:
        g, (r, eta) = floor_gain(b, l, R)
        print(f"  (b,l)=({b:.4f},{l:.4f}) {name:40s}: max floor-exponent gain {g:+.5f} at r={r:.2f}, eta={eta:.3f}  (dB ~ {-0.26*max(g,0):+.5f})")
    # the structural cap (U.4): 1 - R(delta0+), per count
    print("   cap 1-R(delta0+): paper x=1/2 %.4f, x=0 %.4f; DIPP %.4f; theta=1/2 %.4f; ideal %.4f" %
          (1-Rstar(d0,.5), 1-Rstar(d0,0), d0/11, d0/2, d0))

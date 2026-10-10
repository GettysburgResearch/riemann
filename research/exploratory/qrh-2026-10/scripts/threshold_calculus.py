#!/usr/bin/env python3
"""Threshold calculus for the Part II architecture of the OpenAI quasi-RH manuscript.

Status: EXPLORATORY model (FLOATING_RECONNAISSANCE, with exact cross-checks).
Source: "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", OpenAI, 30 Sep 2026
        (sha256 in SOURCES.txt).  Section/equation numbers below refer to that manuscript.

The model treats every lemma of the manuscript as a black box whose *stated output exponent*
is transcribed below.  It then asks: for which scale geometry (lx, ly, ell) does the stated
machinery close the continuation criterion (Prop. 2.1), and at which boundary sigma0?

Conventions (all exponents are base Z unless said otherwise):
  X = Z^lx, Y = Z^ly, slot length ell, M = lx + ly, b = ly - lx, h = 1 - lx + ell (dual length),
  C(s) = s + lx/2 - 1 + h/6                                               (Def. 10.1, eq. 10.3)
  low estimate |I| << Z^{theta_low}; boundary sigma0 = 1 - lx/2 - h/6 + theta_low (Prop. 2.1)
  high exponent for a row bin, relative to C(beta*):                     (Lemma 10.4, eq. 10.15)
      F = a - beta* + h(z0 - 1/6) - a ly - ell/2 + q ell + d (R + delta/2 - z0),
      a = (1+delta)/2 the bin real part (a <= beta*), q = x delta the slot amplitude mean,
      U = Z^d the row norm, U^R the row count of the bin.
The architecture closes at sigma0 iff theta_low gives sigma0 and sup F < 0 for every admissible
beta* in (sigma0, beta_prev], every bin delta in [1/50, 2 beta* - 1], x in [0,1/2], d.

What is NOT modelled: the validity of each lemma outside the manuscript's own parameter ranges.
Every geometry other than the manuscript's is an extrapolation whose lemma-range obligations are
listed in THRESHOLD_CALCULUS.md.
"""
import itertools
import numpy as np

ALPHA = 5/6          # sixth-power amplification slope (Lemma 17.6, eq. 19.3)
Z0 = 17/50           # central contour Re z (Lemma 10.3; Euler region (7.14))
DELTA0 = 1/50        # floor bin delta (a = 51/100)
TMIN, TMAX = 1.0, 1.5  # detector parameter range (Prop. 8.3)


class Inputs:
    """Bundle of the lemma constants that the sensitivity study varies."""
    def __init__(self, alpha=ALPHA, plain_cap=6.0, inv_cap=2.0, tmax=TMAX, z0=Z0,
                 energy='paper', counts='paper', d_sel=0.5, kappa_floor=0.75, R_shift=0.0):
        self.alpha = alpha            # amplification slope
        self.plain_cap = plain_cap    # Lemma 18.1 width condition 2m + plain_cap*kappa*z <= 1
        self.inv_cap = inv_cap        # Lemma 17.1 width condition r + inv_cap*z <= 1
        self.tmax = tmax              # detector t in [1, tmax]
        self.z0 = z0
        self.energy = energy          # 'paper' (Lemma 14.3 sup) or 'optimal' (large-sieve diagonal only)
        self.counts = counts          # 'paper' (Prop. 19.2 machinery) or 'DH' (R = 1 - delta) or 'trivial'
        self.d_sel = d_sel            # selected prime slots used only for d >= d_sel (paper: 1/2)
        self.kappa_floor = kappa_floor  # Lemma 18.1 stated for kappa in [3/4,1]; None = extrapolate
        self.R_shift = R_shift          # demand-curve experiment: R -> max(1 - delta, R - R_shift) off the floor bin

PAPER = Inputs()

# ----------------------------------------------------------------------------------------------
# Row counts (Prop. 19.2 and its proof; Lemmas 17.1, 17.6, 18.1; detector Prop. 8.3)
# ----------------------------------------------------------------------------------------------

def _pieces(delta, x, kappa, S, t, inp):
    q = x*delta
    lo, hi = t - 0.5, t
    cands = []
    p1 = []                                              # inverse witness, amplified, no slots
    if lo < 1: p1.append((lo, min(hi, 1.0), 1.0, -delta))
    if hi > 1: p1.append((max(lo, 1.0), hi, 1 - inp.alpha, inp.alpha - delta))
    cands.append(p1)
    cands.append([(lo, hi, 1 - 2*delta*t, 2*delta)])     # plain witness (two copies), no slots
    if S > 0:
        p2 = []                                          # inverse with slots, z = min((1-r)/c, S)
        c = inp.inv_cap
        rb = 1 - c*S
        if lo < 1:
            a, b = lo, min(hi, 1.0)
            if a < min(b, rb): p2.append((a, min(b, rb), 1 - 2*q*S, -delta))
            # z = (1-r)/c : 1 - delta r - (2q/c)(1-r)
            if max(a, rb) < b: p2.append((max(a, rb), b, 1 - 2*q/c, 2*q/c - delta))
        cands.append(('partial', p2))
        p4 = []                                          # plain with slots, z = min((1-2m)/(c' kappa), S)
        cp = inp.plain_cap*kappa
        rb2 = t - (1 - cp*S)/2
        cc = 2*q/cp
        if lo < min(hi, rb2): p4.append((lo, min(hi, rb2), 1 - 2*delta*t - cc + 2*cc*t, 2*delta - 2*cc))
        if max(lo, rb2) < hi: p4.append((max(lo, rb2), hi, 1 - 2*delta*t - 2*q*S, 2*delta))
        cands.append(('partial', p4))
    return cands


def _eval(cands, r):
    vals = []
    for c in cands:
        segs = c[1] if isinstance(c, tuple) else c
        v = None
        for (lo, hi, A, B) in segs:
            if lo - 1e-11 <= r <= hi + 1e-11:
                vv = A + B*r
                v = vv if v is None else min(v, vv)
        if v is not None: vals.append(v)
    return min(vals)


def worst_split(delta, x, kappa, S, t, inp=PAPER):
    """max over the row's witness split (r, m=t-r), of the best available count: exact."""
    cands = _pieces(delta, x, kappa, S, t, inp)
    segs, pts = [], {t - 0.5, t}
    for c in cands:
        for s in (c[1] if isinstance(c, tuple) else c):
            segs.append(s); pts.update((s[0], s[1]))
    for s1, s2 in itertools.combinations(segs, 2):
        if abs(s1[3] - s2[3]) > 1e-15:
            r = (s2[2] - s1[2])/(s1[3] - s2[3])
            if max(s1[0], s2[0]) - 1e-12 <= r <= min(s1[1], s2[1]) + 1e-12:
                pts.add(r)
    return max(_eval(cands, r) for r in pts if t - 0.5 - 1e-12 <= r <= t + 1e-12)


def R_exact(delta, x, kappa, S, inp=PAPER):
    """min over detector t of worst_split; piecewise-affine in t, minimised by grid + golden search."""
    ts = np.linspace(TMIN, inp.tmax, 241)
    vals = [worst_split(delta, x, kappa, S, t, inp) for t in ts]
    i = int(np.argmin(vals))
    a, b = ts[max(i - 1, 0)], ts[min(i + 1, len(ts) - 1)]
    g = (5**0.5 - 1)/2
    c, d = b - g*(b - a), a + g*(b - a)
    fc, fd = worst_split(delta, x, kappa, S, c, inp), worst_split(delta, x, kappa, S, d, inp)
    for _ in range(60):
        if fc < fd:
            b, d, fd = d, c, fc; c = b - g*(b - a); fc = worst_split(delta, x, kappa, S, c, inp)
        else:
            a, c, fc = c, d, fd; d = a + g*(b - a); fd = worst_split(delta, x, kappa, S, d, inp)
    return min(min(vals), fc, fd)


def R_fast(delta, x, kappa, S, inp=PAPER):
    """Closed form (general kappa, capacities) of Prop. 19.2; falls back to R_exact when the
    supply S or the crossing range binds.  Agrees with R_exact to 1e-15 (see self-test)."""
    c = 1/(inp.plain_cap*kappa)
    ci = 1/inp.inv_cap
    # plain: 1 - 2 delta m - 2 x delta c (1 - 2m);  inverse: 1 - delta r - 2 x delta ci (1 - r)
    k = 2 - 4*x*c
    den = k + 1 - 2*x*ci
    if den <= 1e-12:
        return R_closed(delta, x, kappa, S, inp)
    A = 1 - 2*x*delta*ci - delta*(1 - 2*x*ci)*(2*x*c - 2*x*ci)/den
    B = -delta*(1 - 2*x*ci)*k/den
    LA, LB = 1 - inp.alpha, (inp.alpha - delta)
    t = TMIN if abs(LB - B) < 1e-14 else (A - LA)/(LB - B)
    t = min(max(t, TMIN), inp.tmax)
    R = max(A + B*t, LA + LB*t)
    rstar = (k*t + 2*x*c - 2*x*ci)/den
    ok = (t - 0.5 <= rstar <= min(t, 1.0)) and (ci*(1 - rstar) <= S + 1e-15) \
        and (c*(1 - 2*(t - rstar)) <= S + 1e-15)
    return R if ok else R_closed(delta, x, kappa, S, inp)


def _I(r, delta, q, S, inp):
    """inverse-witness count on r <= 1 (decreasing in r)."""
    v = 1 - delta*r
    if S > 0 and r < 1:
        v = min(v, 1 - delta*r - 2*q*min((1 - r)/inp.inv_cap, S))
    return v


def _P(m, delta, q, kappa, S, inp):
    """plain-witness count at length m (increasing in r = t - m)."""
    v = 1 - 2*delta*m
    if S > 0 and m < 0.5:
        v = min(v, 1 - 2*delta*m - 2*q*min((1 - 2*m)/(inp.plain_cap*kappa), S))
    return v


def _R_of_t(t, delta, x, kappa, S, inp):
    q = x*delta
    lo, hi = t - 0.5, min(t, 1.0)
    g = lambda r: _I(r, delta, q, S, inp) - _P(t - r, delta, q, kappa, S, inp)
    if g(lo) <= 0:
        val = _I(lo, delta, q, S, inp)
    elif g(hi) >= 0:
        val = _P(t - hi, delta, q, kappa, S, inp)
    else:
        a, b = lo, hi
        for _ in range(60):
            mid = (a + b)/2
            if g(mid) > 0: a = mid
            else: b = mid
        val = _I((a + b)/2, delta, q, S, inp)
    if t > 1:
        val = max(val, min(1 - inp.alpha + (inp.alpha - delta)*t, _P(0.0, delta, q, kappa, S, inp)))
    return val


def R_bisect(delta, x, kappa, S, inp=PAPER):
    """Monotone-structure evaluation: crossing by bisection in r, ternary search in t."""
    a, b = TMIN, inp.tmax
    for _ in range(80):
        m1, m2 = a + (b - a)/3, b - (b - a)/3
        if _R_of_t(m1, delta, x, kappa, S, inp) <= _R_of_t(m2, delta, x, kappa, S, inp): b = m2
        else: a = m1
    return min(_R_of_t((a + b)/2, delta, x, kappa, S, inp), _R_of_t(TMIN, delta, x, kappa, S, inp),
               _R_of_t(inp.tmax, delta, x, kappa, S, inp))


def _cross_closed(t, delta, x, kappa, S, inp):
    """max over r in [t-1/2, min(t,1)] of min(I(r), P(t-r)) in closed form (two affine pieces each)."""
    q = x*delta
    lo, hi = t - 0.5, min(t, 1.0)
    c, cp = inp.inv_cap, inp.plain_cap*kappa
    rb = 1 - c*S                       # I: r <= rb -> 1 - delta r - 2qS ; r >= rb -> 1 - 2q/c + (2q/c - delta) r
    mb = (1 - cp*S)/2                  # P: m >= mb -> 1 - 2q/cp - (2delta - 4q/cp) m ; m <= mb -> 1 - 2qS - 2 delta m
    Ipieces = [(-1e9, rb, 1 - 2*q*S, -delta), (rb, 1e9, 1 - 2*q/c, 2*q/c - delta)] if S > 0 else [(-1e9, 1e9, 1.0, -delta)]
    # P as a function of r: m = t - r
    if S > 0:
        A1, B1 = 1 - 2*q/cp - (2*delta - 4*q/cp)*t, (2*delta - 4*q/cp)     # valid for m >= mb <=> r <= t - mb
        A2, B2 = 1 - 2*q*S - 2*delta*t, 2*delta                            # valid for r >= t - mb
        Ppieces = [(-1e9, t - mb, A1, B1), (t - mb, 1e9, A2, B2)]
    else:
        Ppieces = [(-1e9, 1e9, 1 - 2*delta*t, 2*delta)]
    Iv = lambda r: max(A + B*r for (l, h_, A, B) in Ipieces if l - 1e-12 <= r <= h_ + 1e-12) if False else min(A + B*r for (l, h_, A, B) in Ipieces if l - 1e-12 <= r <= h_ + 1e-12)
    Pv = lambda r: min(A + B*r for (l, h_, A, B) in Ppieces if l - 1e-12 <= r <= h_ + 1e-12)
    if Iv(lo) <= Pv(lo): return Iv(lo)
    if Iv(hi) >= Pv(hi): return Pv(hi)
    for (l1, h1, A1_, B1_) in Ipieces:
        for (l2, h2, A2_, B2_) in Ppieces:
            if abs(B1_ - B2_) < 1e-15: continue
            r = (A2_ - A1_)/(B1_ - B2_)
            if max(l1, l2, lo) - 1e-12 <= r <= min(h1, h2, hi) + 1e-12:
                return A1_ + B1_*r
    raise RuntimeError("no crossing found")


def R_closed(delta, x, kappa, S, inp=PAPER):
    """Exact: R = min_t max(cross(t), min(L(t), P(0))) with cross decreasing and L increasing in t."""
    q = x*delta
    P0 = 1 - 2*q*min(1/(inp.plain_cap*kappa), S) if S > 0 else 1.0
    def Rt(t):
        v = _cross_closed(t, delta, x, kappa, S, inp)
        if t > 1: v = max(v, min(1 - inp.alpha + (inp.alpha - delta)*t, P0))
        return v
    a, b = TMIN, inp.tmax
    for _ in range(100):
        m1, m2 = a + (b - a)/3, b - (b - a)/3
        if Rt(m1) <= Rt(m2): b = m2
        else: a = m1
    return min(Rt((a + b)/2), Rt(TMIN), Rt(inp.tmax))


def R_bin(delta, x, d, kappa, ell, inp=PAPER):
    """Row-count exponent used for a bin at dyad U = Z^d."""
    if delta <= DELTA0 + 1e-12:
        return 1.0                                  # floor bin: trivial count, no witness
    if inp.counts == 'DH':
        return 1 - delta                            # density-hypothesis-quality benchmark
    if inp.counts == 'trivial':
        return 1.0
    if inp.counts == 'joint':
        # PR 910 eq. (6.6)-(6.7): a common-frequency joint moment sum_u |M_u S_u|^2 << U^{1+eps} for r+m >= 1
        # would give #rows << U^{1 - delta (r+m)}; the detector guarantees r + m >= t, t <= tmax (Prop. 8.3).
        # Taken at face value on the whole detector range: R = 1 - delta*tmax (better than DH).
        return 1 - delta*inp.tmax
    R_un = 1 - 2*delta/3                            # t = 1, no slots (Prop. 19.2 last clause)
    if d < inp.d_sel or ell <= 0:
        R = R_un
    else:
        R = min(R_un, R_fast(delta, x, kappa, ell/d, inp))
    if inp.R_shift:
        R = max(1 - delta, R - inp.R_shift)
    return R

# ----------------------------------------------------------------------------------------------
# Low side (Lemma 14.3 -> Lemma 15.1, Prop. 15.2, Prop. 15.3)
# ----------------------------------------------------------------------------------------------

def energy_exponent(Mp, lp, inp=PAPER):
    """sup of E_ref (eq. 14.14) over admissible dyads; closed form verified against an LP
    (energy_lp.py).  'optimal' drops the reflected-kernel branch (large-sieve diagonal only)."""
    if inp.energy == 'optimal':
        return max(Mp, 2*Mp + lp - 1)
    return max(Mp, (2*Mp + 1 + 3*lp)/4, 2*Mp + lp - 1)


def low_threshold(lx, ly, ell, inp=PAPER, nd=201):
    M = lx + ly; b = ly - lx; h = 1 - lx + ell
    worst = -9.0
    for dd in (np.linspace(0, ell, nd) if ell > 0 else [0.0]):
        Mp, lp = M - 2*dd, ell - dd
        EB = energy_exponent(Mp, lp, inp)
        gram = max(0.0, b/6, 2*b - (ly - dd))       # Prop. 15.2: (Q/Y')(1 + Pa^{1/6} + Pa^2/Y')
        sep = (-(ly - dd) + gram + EB)/2
        worst = max(worst, sep - dd/2)              # Prop. 15.3: Z^d tuples, coefficient Z^{-3d/2}
    return 1 - lx/2 - h/6 + worst

# ----------------------------------------------------------------------------------------------
# High side
# ----------------------------------------------------------------------------------------------

def F_high(delta, x, d, lx, ly, ell, beta, R, z0=Z0):
    a = (1 + delta)/2; h = 1 - lx + ell
    return a - beta + h*(z0 - 1/6) - a*ly - ell/2 + x*delta*ell + d*(R + delta/2 - z0)


def high_sup(lx, ly, ell, sigma0, beta_prev, inp=PAPER, nde=81, nx=11, nd=9):
    """sup F over bins/amplitudes/dyads at the worst admissible beta* (= max(sigma0, a)).
    Negative = the high comparison closes before adjustable losses."""
    h = 1 - lx + ell
    worst = (-9.0, None)
    dsel = list(np.linspace(inp.d_sel, h, nd)) if h > inp.d_sel else []
    for delta in np.linspace(DELTA0, 2*beta_prev - 1, nde):
        a = (1 + delta)/2
        beta = max(sigma0 + 1e-12, a)
        kappa = 2*beta - 1
        if inp.kappa_floor is not None:
            kappa = max(kappa, inp.kappa_floor)
        for x in np.linspace(0, 0.5, nx):
            for d in [0.01, min(inp.d_sel, h)] + dsel:
                R = R_bin(delta, x, d, kappa, ell, inp)
                Fv = F_high(delta, x, d, lx, ly, ell, beta, R, inp.z0)
                if Fv > worst[0]:
                    worst = (Fv, (round(delta, 5), round(x, 3), round(d, 5), round(R, 6)))
    small = h*(inp.z0 - 1/6) - ly/2                  # small rows (Sec. 20.3), O(d_min) dropped
    if small > worst[0]:
        worst = (small, ('small-rows',))
    return worst


def valid_geometry(lx, ly, ell):
    return ly >= lx - 1e-12 and lx - ell > 0.01 and ly - ell > 0.01 and ell >= 0 and lx > 0


def closes(lx, ly, ell, beta_prev, inp=PAPER, fine=False):
    s0 = low_threshold(lx, ly, ell, inp)
    kw = dict(nde=241, nx=26, nd=17) if fine else dict(nde=41, nx=6, nd=5)
    return s0, high_sup(lx, ly, ell, s0, beta_prev, inp, **kw)


def optimise(beta_prev, inp=PAPER, starts=None, penalty=200.0, slack=2e-5):
    """Nelder-Mead over (lx, ly, ell) minimising sigma0 subject to sup F < -slack."""
    from scipy.optimize import minimize
    if starts is None:
        starts = [(17/48, 23/48, 1/6), (0.3, 0.45, 0.2), (0.4, 0.45, 0.1), (0.25, 0.5, 0.25),
                  (0.45, 0.5, 0.05), (0.5, 0.5, 0.0)]
    def obj(p):
        lx, ly, ell = p
        if not valid_geometry(lx, ly, ell): return 2.0
        s0 = low_threshold(lx, ly, ell, inp, nd=41)
        if s0 >= beta_prev: return 1.5 + s0
        hs = high_sup(lx, ly, ell, s0, beta_prev, inp, nde=41, nx=6, nd=5)[0]
        return s0 + penalty*max(0.0, hs + slack)
    best = (9.0, None)
    for st in starts:
        r = minimize(obj, st, method='Nelder-Mead', options=dict(xatol=1e-6, fatol=1e-8, maxiter=2000))
        if r.fun < best[0]: best = (r.fun, tuple(r.x))
    lx, ly, ell = best[1]
    s0, hs = closes(lx, ly, ell, beta_prev, inp, fine=True)
    return dict(sigma0=s0, lx=lx, ly=ly, ell=ell, M_plus_ell=lx + ly + ell, high_sup=hs[0], arg=hs[1])


if __name__ == '__main__':
    import random
    # self-tests: (1) paper geometry reproduces 7/8 and the Lemma 20.2 margin
    s0, hs = closes(17/48, 23/48, 1/6, 11/12, fine=True)
    print(f"paper geometry: sigma0 = {s0:.6f} (expect 0.875); sup F = {hs[0]:+.3e} at {hs[1]}")
    print(f"Part I geometry: sigma0 = {low_threshold(0.5, 0.5, 0.0):.6f} (expect 11/12 = {11/12:.6f})")
    # (2) closed form R matches the paper's R* at kappa = 3/4
    for delta, x in [(0.1, 0.5), (0.3866, 0.5), (0.6, 0.25), (0.75, 0.0)]:
        Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x); J = (ALPHA - delta)*Dx + delta*Px
        Rstar = 1 - delta + (ALPHA - delta)*delta*Px/(2*J)
        print(f"  R*({delta},{x}) paper {Rstar:.9f}  model {R_fast(delta, x, 0.75, (1/6)/(13/16)):.9f}")
    # (3) fast vs exact
    random.seed(1); worst = 0
    for _ in range(200):
        dl, xx, kp, S = random.uniform(.02, .83), random.uniform(0, .5), random.uniform(.5, .85), random.choice([.05, .1, .2, .5, 2])
        worst = max(worst, abs(R_fast(dl, xx, kp, S) - R_exact(dl, xx, kp, S)))
    print(f"  max |R_fast - R_exact| over 200 random inputs: {worst:.1e}")

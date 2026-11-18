"""CRIT23 Level-2 audit, part 2, step S10 (Knausgard arXiv:2610.08965v1: local data, majorant, kernel bounds).

The certificate data are parsed directly from KN's LaTeX tables (knausgard839tab1/2/3.tex, passed as data files;
nothing from the authors' ancillary programs is executed).  Checks:
(a) the budget constraints (eq:budget), reward sums x1, x2, x, the identity sum_r B_r = 0, the oscillation bounds
    Omega = 0.015882 / 0.003882 / 0.075420, and the trivial-frame thresholds (0.001294 -> 15.975, 0.038198 -> 14.927);
(b) beta = min_{|t|<=theta} K(t)^2 >= stated dyadic rationals, by a Lipschitz grid (|d K^2/dt| <= 2 pi);
(c) f <= g on [0,1/2] with the stated margin >= 1e-4, by a Lipschitz grid; Lambda = (2 gamma0/theta)(1 + sinc theta);
(d) Lemma 2.3 (separated points) on random and lattice-like theta-separated sets: lambda_max(K(y_i-y_j)) <= Lambda;
(e) the local inequalities (eq:local) [window 1, 2^7 labellings], (eq:local8) [window 2] and the third-window one,
    by random sampling (2e6 frames each, gaps biased towards near-integer spacings) plus Nelder-Mead minimisation of
    the slack from the worst samples, with K evaluated exactly at the minimisers;
(f) the transfer Lemma 2.5 / (eq:transfer8) end-to-end on random long separated labelled sequences.
Lipschitz-grid checks are in double precision floating point (not directed rounding); (d)-(f) are sampling
evidence, not proofs.  The branch-and-bound proofs of Props 3.3, 5.3, 6.3 are NOT replayed.

Usage: python3 -I s10_kn_local.py <dir containing knausgard839tab1.tex, ...tab2.tex, ...tab3.tex>"""
import re
import sys
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261117)
TH = 17 / 20
W1 = np.array([193305, -23105, 29166, 13952, -21009, 41052]) / 1e6
W2 = np.array([122290, -45012, 16241, 1887, 2711, 3731, -5307, 2982, -5153, 5358]) / 1e6
W3 = np.array([200566, 19, -9358, 9283, -6746, 8170]) / 1e6


def sinc(t):
    t = np.asarray(t, dtype=float)
    out = np.ones_like(t)
    nz = np.abs(t) > 1e-14
    out[nz] = np.sin(np.pi * t[nz]) / (np.pi * t[nz])
    return out


def Kfun(a):
    def K(t):
        out = sinc(t)
        for j, aj in enumerate(a, start=1):
            out = out + aj / 2 * (sinc(t - j) + sinc(t + j))
        return out
    return K


# ---------------------------------------------------------------------------------------------- parsing
def rows(tex):
    body = re.findall(r'\\midrule(.*?)\\bottomrule', tex, re.S)
    out = []
    for blk in body:
        rr = []
        for line in blk.strip().split('\\\\'):
            line = line.strip()
            if line:
                rr.append([c.strip().strip('$') for c in line.split('&')])
        out.append(rr)
    return out


def parse(d):
    t1 = open(d + '/knausgard839tab1.tex').read()
    t2 = open(d + '/knausgard839tab2.tex').read()
    t3 = open(d + '/knausgard839tab3.tex').read()
    r1 = rows(t1)
    Wlab = {}
    for row in r1[0]:
        i, j = map(int, re.findall(r'\d+', row[0]))
        Wlab[(i, j)] = {(1, 1): int(row[1]) / 1e6, (1, 2): int(row[2]) / 1e6, (2, 2): int(row[3]) / 1e6}
    kap = {1: [int(v) / 1e6 for v in r1[1][0][1:]], 2: [int(v) / 1e6 for v in r1[1][1][1:]]}
    hdr = re.findall(r'j=(\d+)', t1.split('tab:knots')[1])
    jcols = [int(v) for v in hdr]
    knots1 = {}
    for row in r1[2]:
        lab = row[0]; u = row[1]
        vals = np.zeros(12)
        for jj, v in zip(jcols, row[2:]):
            vals[jj] = int(v) / 1e6
        knots1[(lab, u)] = vals
    r2 = rows(t2)
    W8 = {}
    for row in r2[0]:
        for k in range(0, len(row), 2):
            i, j = map(int, re.findall(r'\d+', row[k])); W8[(i, j)] = int(row[k + 1]) / 1e6
    knots2 = {'u0': np.zeros(12), 'u1': np.zeros(12), 'u2': np.zeros(12)}
    for row in r2[1]:
        for k in range(0, len(row), 4):
            j = int(row[k]); knots2['u0'][j], knots2['u1'][j], knots2['u2'][j] = [int(v) / 1e6 for v in row[k + 1:k + 4]]
    r3 = rows(t3)
    W7 = {}
    for row in r3[0]:
        for k in range(0, len(row), 2):
            i, j = map(int, re.findall(r'\d+', row[k])); W7[(i, j)] = int(row[k + 1]) / 1e6
    knots3 = {'u0': np.zeros(12), 'u1': np.zeros(12)}
    for row in r3[1]:
        for k in range(0, len(row), 3):
            j = int(row[k]); knots3['u0'][j], knots3['u1'][j] = [int(v) / 1e6 for v in row[k + 1:k + 3]]
    return Wlab, kap, knots1, W8, knots2, W7, knots3


KX = np.concatenate([[0.75], 7 / 8 + np.arange(12) / 8, [19 / 8]])


def pl(vals):
    """continuous piecewise-linear function through (3/4,0), (7/8 + j/8, vals[j]), (19/8, 0); zero outside."""
    yv = np.concatenate([[0.0], vals, [0.0]])
    return lambda t: np.interp(t, KX, yv, left=0.0, right=0.0)


def rng_of(fs):
    """range (max-min) over t of a list of functions (and the value 0 outside the support)."""
    tt = np.concatenate([KX, [0.0, 3.0]])
    vals = np.concatenate([f(tt) for f in fs])
    return vals.max() - vals.min()


# ---------------------------------------------------------------------------------------------- (a)
def part_a(P):
    Wlab, kap, knots1, W8, knots2, W7, knots3 = P
    print("(a) certificate data parsed from the LaTeX tables")
    for (d, dp), bud in (((1, 1), 2), ((1, 2), 4), ((2, 2), 8)):
        sums = [sum(Wlab[(i, i + s)][(d, dp)] for i in range(0, 7 - s)) for s in range(1, 7)]
        print(f"   window 1, labels {d}{dp}: budget sums by distance s=1..6: {np.round(sums, 6).tolist()} <= {bud}: {all(x <= bud + 1e-12 for x in sums)}")
    x1 = sum(kap[1]); x2 = sum(kap[2])
    print(f"   window 1: x1 = {x1:.6f} (0.054350), x2 = {x2:.6f} (0.069433), kappa_i1 <= kappa_i2: {all(a <= b for a, b in zip(kap[1], kap[2]))}")
    u = {k: pl(v) for k, v in knots1.items()}
    labs = ['11', '12', '22']
    Bcum = [lambda t, L: u[(L, 'u_0')](t), lambda t, L: u[(L, 'u_0')](t) + u[(L, 'u_1')](t),
            lambda t, L: 0 * t, lambda t, L: -u[(L, 'u_0')](t) - u[(L, 'u_1')](t), lambda t, L: -u[(L, 'u_0')](t)]
    Om1 = sum(rng_of([(lambda t, f=f, L=L: f(t, L)) for L in labs]) for f in Bcum)
    # largest value of -B_r: B = (u0,u1,-u0-u1,-u0-u1,u1,u0)
    tt = np.linspace(0, 3, 30001)
    negB1 = 0.0
    for r in range(6):
        best = 0.0
        for L in labs:
            u0 = u[(L, 'u_0')](tt); u1 = u[(L, 'u_1')](tt)
            Br = [u0, u1, -u0 - u1, -u0 - u1, u1, u0][r]
            best = max(best, np.max(-Br))
        negB1 += best
    print(f"   window 1: Omega = {Om1:.6f} (stated 0.015882); sum_r max(-B_r) = {negB1:.6f}; trivial spread >= (x2 + that)/alpha = {(x2+negB1)/0.006219:.3f}")
    sums8 = [sum(W8[(i, i + s)] for i in range(0, 8 - s)) for s in range(1, 8)]
    print(f"   window 2 (8 points): budget sums s=1..7: {np.round(sums8, 6).tolist()} <= 2: {all(x <= 2 + 1e-12 for x in sums8)}")
    v0, v1, v2 = (pl(knots2[k]) for k in ('u0', 'u1', 'u2'))
    Om2 = 2 * (rng_of([v0]) + rng_of([lambda t: v0(t) + v1(t)]) + rng_of([lambda t: v0(t) + v1(t) + v2(t)]))
    Bs2 = [v0(tt), v1(tt), v2(tt), -2 * (v0(tt) + v1(tt) + v2(tt)), v2(tt), v1(tt), v0(tt)]
    negB2 = sum(max(0.0, np.max(-B)) for B in Bs2)
    print(f"   window 2: Omega = {Om2:.6f} (stated 0.003882); sum_r max(-B_r) = {negB2:.6f} (stated 0.001294);"
          f" trivial spread = {(0.008722+negB2)/0.000627:.3f} (stated 15.975)")
    sums7 = [sum(W7[(i, i + s)] for i in range(0, 7 - s)) for s in range(1, 7)]
    print(f"   window 3: budget sums s=1..6: {np.round(sums7, 6).tolist()} <= 2: {all(x <= 2 + 1e-12 for x in sums7)}")
    w0, w1 = pl(knots3['u0']), pl(knots3['u1'])
    Om3 = 2 * (rng_of([w0]) + rng_of([lambda t: w0(t) + w1(t)]))
    Bs3 = [w0(tt), w1(tt), -w0(tt) - w1(tt), -w0(tt) - w1(tt), w1(tt), w0(tt)]
    negB3 = sum(max(0.0, np.max(-B)) for B in Bs3)
    print(f"   window 3: Omega = {Om3:.6f} (stated 0.075420); sum_r max(-B_r) = {negB3:.6f} (stated 0.038198);"
          f" trivial spread = {(0.054525+negB3)/0.006212:.3f} (stated 14.927)")
    return u, (v0, v1, v2), (w0, w1)


# ---------------------------------------------------------------------------------------------- (b),(c)
def part_bc():
    print("(b) beta = min_{0<=t<=theta} K(t)^2 by a Lipschitz grid (|dK^2/dt| <= 2 pi), h = 1e-6")
    h = 1e-6
    t = np.arange(0, TH + h / 2, h)
    for name, a, beta in (("window 1", W1, 8824337 / 134217728), ("window 2", W2, 13707941 / 2 ** 28), ("window 3", W3, 4483379 / 2 ** 26)):
        K2 = Kfun(a)(t) ** 2
        lo = K2.min() - np.pi * h
        print(f"   {name}: grid min K^2 = {K2.min():.9f} at t = {t[np.argmin(K2)]:.6f}; Lipschitz-grid lower bound (double precision, not directed rounding) {lo:.9f}"
              f" >= beta = {beta:.9f}: {lo >= beta}")
    print("(c) majorant: f <= g on [0,1/2] (Lipschitz grid, h = 1e-6) and Lambda = (2 gamma0/theta)(1 + sinc theta)")
    u = np.arange(0, 0.5 + 0.5e-6, 1e-6)
    for name, a, g0, cap in (("window 1", W1, 0.607, 3.35 / 2), ("window 2", W2, 0.65, 2.0), ("window 3", W3, 0.61, 2.0)):
        f = 1 + sum(aj * np.cos(2 * np.pi * j * u) for j, aj in enumerate(a, start=1))
        s = sinc(TH * (u - 0.5)) + sinc(TH * (u + 0.5))
        g = g0 * s ** 2
        M = 2 * np.pi * np.sum(np.arange(1, len(a) + 1) * np.abs(a)) + 4 * g0 * TH * np.pi
        marg = (g - f).min()
        Lam = 2 * g0 / TH * (1 + np.sin(np.pi * TH) / (np.pi * TH))
        print(f"   {name}: min(g-f) on grid = {marg:.6e} at u = {u[np.argmin(g-f)]:.6f}; Lipschitz const <= {M:.2f}, so min >= {marg - M*0.5e-6:.6e}"
              f" (stated margin >= 1e-4: {marg - M*0.5e-6 >= 1e-4}); Lambda = {Lam:.6f} < {cap}: {Lam < cap}; g(1/2)={g[-1]:.4f}, f(1/2)={f[-1]:.4f}")


# ---------------------------------------------------------------------------------------------- (d)
def part_d():
    print("(d) Lemma 2.3: lambda_max (K(y_i - y_j)) <= Lambda on theta-separated sets (random + near-lattice)")
    for name, a, g0 in (("window 1", W1, 0.607), ("window 2", W2, 0.65), ("window 3", W3, 0.61)):
        K = Kfun(a); Lam = 2 * g0 / TH * (1 + np.sin(np.pi * TH) / (np.pi * TH))
        best = 0.0
        for it in range(4000):
            m = rng.integers(2, 40)
            mode = it % 3
            if mode == 0:
                gaps = TH + rng.exponential(0.3, m - 1)
            elif mode == 1:
                gaps = TH + np.abs(rng.normal(0, 0.02, m - 1))
            else:
                gaps = np.where(rng.random(m - 1) < 0.5, TH, 1.0) + np.abs(rng.normal(0, 0.01, m - 1))
            y = np.concatenate([[0], np.cumsum(gaps)])
            ev = np.linalg.eigvalsh(K(y[:, None] - y[None, :]))
            best = max(best, ev[-1])
        print(f"   {name}: max lambda_max over 4000 sets = {best:.6f}  <=  Lambda = {Lam:.6f}: {best <= Lam}")


# ---------------------------------------------------------------------------------------------- (e)
def table(K, tmax=40.0, h=2e-4):
    tg = np.arange(0, tmax + h, h)
    kg = K(tg) ** 2
    return lambda d: np.interp(np.abs(d), tg, kg)


def sample_gaps(M, n, rng):
    """mixture of gap laws: near theta, near 1, near 2, near 3/2, exponential tails."""
    choice = rng.integers(0, 5, size=(M, n))
    base = np.choose(choice, [np.full((M, n), TH), np.full((M, n), 1.0), np.full((M, n), 2.0), np.full((M, n), 1.5),
                              TH + rng.exponential(0.8, size=(M, n))])
    g = base + rng.normal(0, 0.06, size=(M, n))
    return np.maximum(g, TH)


def local_window1(u, K2, gaps, labs, alpha, kap, Wlab):
    """slack of (eq:local) for frames with given gaps (M x 6) and labels (7-tuple of 1/2)."""
    y = np.concatenate([np.zeros((gaps.shape[0], 1)), np.cumsum(gaps, axis=1)], axis=1)
    lhs = alpha * y[:, 6]
    for (i, j), w in Wlab.items():
        dd = tuple(sorted((labs[i], labs[j])))
        lhs = lhs + w[dd] * K2(y[:, j] - y[:, i])
    for r in range(6):
        L = ''.join(str(v) for v in sorted((labs[r], labs[r + 1])))
        u0 = u[(L, 'u_0')](gaps[:, r]); u1 = u[(L, 'u_1')](gaps[:, r])
        lhs = lhs + [u0, u1, -u0 - u1, -u0 - u1, u1, u0][r]
    rhs = sum(kap[labs[i]][i] for i in range(7))
    return lhs - rhs


def part_e(P, u, v, w):
    Wlab, kap, knots1, W8, knots2, W7, knots3 = P
    print("(e) local inequalities: sampling (2e6 frames) + Nelder-Mead from the worst samples; slack must be >= 0")
    # window 1, labelled: K^2 of the 21 pair distances computed once, shared by all 128 labellings
    K1 = Kfun(W1); K2t = table(K1)
    K2ex = lambda d: K1(np.abs(d)) ** 2
    M = 2_000_000
    gaps = sample_gaps(M, 6, rng)
    y = np.concatenate([np.zeros((M, 1)), np.cumsum(gaps, axis=1)], axis=1)
    pairs = sorted(Wlab.keys())
    Kmat = np.stack([K2t(y[:, j] - y[:, i]) for (i, j) in pairs], axis=1)          # M x 21
    labs3 = ['11', '12', '22']
    Bval = {}
    for L in labs3:
        u0 = u[(L, 'u_0')](gaps); u1 = u[(L, 'u_1')](gaps)                       # M x 6 each
        Bl = [u0[:, 0], u1[:, 1], -u0[:, 2] - u1[:, 2], -u0[:, 3] - u1[:, 3], u1[:, 4], u0[:, 5]]
        for r in range(6):
            Bval[(r, L)] = Bl[r]
    worst_all = np.inf; worst_lab = None; worst_g = None; per_lab = []
    for code in range(128):
        labs = [1 + ((code >> i) & 1) for i in range(7)]
        wvec = np.array([Wlab[(i, j)][tuple(sorted((labs[i], labs[j])))] for (i, j) in pairs])
        sl = 0.006219 * y[:, 6] + Kmat @ wvec
        for r in range(6):
            sl = sl + Bval[(r, ''.join(str(v) for v in sorted((labs[r], labs[r + 1]))))]
        sl = sl - sum(kap[labs[i]][i] for i in range(7))
        i0 = int(np.argmin(sl))
        f = lambda z: float(local_window1(u, K2ex, (TH + z ** 2)[None, :], labs, 0.006219, kap, Wlab)[0])
        res = minimize(f, np.sqrt(np.maximum(gaps[i0] - TH, 0)), method='Nelder-Mead',
                       options={'maxiter': 1500, 'xatol': 1e-9, 'fatol': 1e-12})
        exact_at_sample = f(np.sqrt(np.maximum(gaps[i0] - TH, 0)))
        best = min(res.fun, exact_at_sample)
        per_lab.append(best)
        if best < worst_all:
            worst_all, worst_lab = best, labs
            worst_g = TH + res.x ** 2 if res.fun <= exact_at_sample else gaps[i0]
    per_lab = np.array(per_lab)
    print(f"   window 1 (7 points, 128 labellings x {M} gap samples, + 1 Nelder-Mead per labelling, exact K at the end):"
          f" min slack = {worst_all:.3e} at labels {worst_lab}, gaps {np.round(worst_g, 4).tolist()};"
          f" labellings with min slack < 1e-3: {int(np.sum(per_lab < 1e-3))}")
    # window 2, 8 points
    Kw2 = Kfun(W2); T2 = table(Kw2); E2 = lambda d: Kw2(np.abs(d)) ** 2
    v0, v1, v2 = v

    def slack8(g, K2):
        y = np.concatenate([np.zeros((g.shape[0], 1)), np.cumsum(g, axis=1)], axis=1)
        lhs = 0.000627 * y[:, 7]
        for (i, j), wt in W8.items():
            lhs = lhs + wt * K2(y[:, j] - y[:, i])
        B = [v0, v1, v2, lambda t: -2 * (v0(t) + v1(t) + v2(t)), v2, v1, v0]
        for r in range(7):
            lhs = lhs + B[r](g[:, r])
        return lhs - 0.008722
    M2 = 2_000_000
    g2 = sample_gaps(M2, 7, rng)
    sl2 = slack8(g2, T2)
    best2 = sl2.min(); bestg2 = g2[np.argmin(sl2)]
    for i0 in np.argsort(sl2)[:30]:
        f = lambda z: float(slack8((TH + z ** 2)[None, :], E2)[0])
        res = minimize(f, np.sqrt(np.maximum(g2[i0] - TH, 0)), method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-10, 'fatol': 1e-13})
        if res.fun < best2:
            best2, bestg2 = res.fun, TH + res.x ** 2
    print(f"   window 2 (8 points, {M2} samples + 30 local minimisations): min slack = {best2:.3e} at gaps {np.round(bestg2, 4).tolist()}")
    # window 3, 7 points, single data for all labels
    Kw3 = Kfun(W3); T3 = table(Kw3); E3 = lambda d: Kw3(np.abs(d)) ** 2
    w0, w1 = w

    def slack7(g, K2):
        y = np.concatenate([np.zeros((g.shape[0], 1)), np.cumsum(g, axis=1)], axis=1)
        lhs = 0.006212 * y[:, 6]
        for (i, j), wt in W7.items():
            lhs = lhs + wt * K2(y[:, j] - y[:, i])
        B = [w0, w1, lambda t: -w0(t) - w1(t), lambda t: -w0(t) - w1(t), w1, w0]
        for r in range(6):
            lhs = lhs + B[r](g[:, r])
        return lhs - 0.054525
    g3 = sample_gaps(M2, 6, rng)
    sl3 = slack7(g3, T3)
    best3 = sl3.min(); bestg3 = g3[np.argmin(sl3)]
    for i0 in np.argsort(sl3)[:30]:
        f = lambda z: float(slack7((TH + z ** 2)[None, :], E3)[0])
        res = minimize(f, np.sqrt(np.maximum(g3[i0] - TH, 0)), method='Nelder-Mead', options={'maxiter': 4000, 'xatol': 1e-10, 'fatol': 1e-13})
        if res.fun < best3:
            best3, bestg3 = res.fun, TH + res.x ** 2
    print(f"   window 3 (7 points, {M2} samples + 30 local minimisations): min slack = {best3:.3e} at gaps {np.round(bestg3, 4).tolist()}")
    return K1, local_window1, slack8, slack7, E2, E3


# ---------------------------------------------------------------------------------------------- (f)
def part_f(P, u, K1):
    Wlab, kap, *_ = P
    print("(f) transfer Lemma 2.5 end-to-end on random theta-separated labelled sequences (window 1):")
    x1, x2, alpha, Om = sum(kap[1]), sum(kap[2]), 0.006219, 0.015882
    worst = np.inf
    for it in range(3000):
        m = int(rng.integers(7, 60))
        gaps = sample_gaps(1, m - 1, rng)[0]
        y = np.concatenate([[0], np.cumsum(gaps)])
        d = rng.integers(1, 3, size=m)
        D = y[:, None] - y[None, :]
        K2 = K1(np.abs(D)) ** 2
        idx = np.abs(np.arange(m)[:, None] - np.arange(m)[None, :])
        mask = (idx > 0) & (idx <= 6)
        lhs = np.sum((d[:, None] * d[None, :] * K2)[mask])
        n1 = int(np.sum(d == 1)); n2 = m - n1
        rhs = x1 * n1 + x2 * n2 - 6 * alpha * (y[-1] - y[0]) - 6 * x2 - Om
        worst = min(worst, lhs - rhs)
    print(f"   min (lhs - rhs) over 3000 sequences (m = 7..59) = {worst:.4e}  (>= 0 expected)")


if __name__ == "__main__":
    d = sys.argv[1]
    P = parse(d)
    u, v, w = part_a(P)
    part_bc()
    part_d()
    K1, *_ = part_e(P, u, v, w)
    part_f(P, u, K1)

#!/usr/bin/env python3
"""Falsification test of the PR 910 native-height sufficient condition (reconnaissance).

Target: PR 910 (git ref pr910), standalone/2026-10-10-quasi-riemann-height-descent/NATIVE_HEIGHT.md
  G_Y(s) = sum_{a<=Y} mu(a) a^{-s},  B_Y(s) = sum_{b<=Y} b^{-s},  R_Y = G_Y B_Y - 1      (lines 156-160)
  Omega = 2 log Y, h = 1/Omega                                                           (lines 350-352)
  E_Y(sigma;T) = int_{T-h}^{T+h} |R_Y|^2 + Omega^{-2} |d_t R_Y|^2 dt                     (lines 355-358)
  D_Y(sigma)   = 2h sum_n a_n^2 (1 + (log n)^2/Omega^2),  a_n = e_Y(n) n^{-sigma}          (lines 423-424)
  O_Y(sigma;T) = E_Y - D_Y  (exact identity, lines 418-435)
  sigma_0(Y)   = 1/2 + c loglog Y / log Y, c > 2                                         (lines 464-467)
  Y = ceil(4(T+2))                                                                      (line 335)
  Sufficient condition: O_Y(sigma;T) < 1/(12 Omega) for every sigma in the interval    (lines 452-456)

Arithmetic: IEEE float64 (numpy) for Dirichlet polynomials; mpmath (30 digits) spot checks of zeta.
This is RECONNAISSANCE: ordinary floating point, finite samples, no interval arithmetic.

Since D_Y >= 0, E_Y < 1/(12 Omega) already implies O_Y < 1/(12 Omega); the reported statistic is
    ratio = 12 * Omega * E_Y(sigma;T),
and the condition can only fail where ratio >= 1 (it fails iff 12 Omega (E_Y - D_Y) >= 1).

Subcommands (each prints JSON):
  validate    exact-vs-float identity checks at small Y (R_Y two ways; E_Y = D_Y + O_Y by the (O) formula)
  dtable      exact D_Y(sigma_0(Y)) for selected Y (integer sieve of e_Y(n), n <= Y^2)
  curve       E_Y along sigma_0(Y) (c=2 boundary, which contains every c>2 region): every integer Y in
              [ylo, yhi] (3 T-values per Y), then sampled Y up to ymax
  resonance   targeted: heights where the small-prime Euler product |zeta_X(sigma_0+it)| is extreme
  mechanism   fixed-sigma diagnostic: does |R_Y| inherit the size of zeta (log-log regression)?
"""
import argparse
import json
import math
import sys
import time

import numpy as np

GL_X, GL_W = np.polynomial.legendre.leggauss(8)


def mobius_sieve(N):
    mu = np.ones(N + 1, dtype=np.int8)
    mu[0] = 0
    is_comp = np.zeros(N + 1, dtype=bool)
    for p in range(2, N + 1):
        if not is_comp[p]:
            is_comp[2 * p::p] = True
            mu[p::p] *= -1
            pp = p * p
            if pp <= N:
                mu[pp::pp] = 0
    return mu


def Y_of_T(T):
    # Y = ceil(4(T+2)); T is a float, guard the integer boundary exactly enough for our grids
    return int(math.ceil(4.0 * (T + 2.0) - 1e-9))


def T_range_of_Y(Y):
    # ceil(4(T+2)) = Y  <=>  (Y-9)/4 < T <= (Y-8)/4
    return (Y - 9) / 4.0, (Y - 8) / 4.0


def sigma0(Y, c=2.0):
    L = math.log(Y)
    return 0.5 + c * math.log(L) / L


class Native:
    """Float64 evaluation of G_Y, B_Y and their t-derivatives at sigma + i t."""

    def __init__(self, mu_full, Y):
        self.Y = Y
        n = np.arange(1, Y + 1, dtype=np.float64)
        self.logn = np.log(n)
        self.mu = mu_full[1:Y + 1].astype(np.float64)
        self.Omega = 2.0 * math.log(Y)
        self.h = 1.0 / self.Omega

    def eval(self, sigma, ts, chunk=None):
        ts = np.asarray(ts, dtype=np.float64)
        amp = np.exp(-sigma * self.logn)
        V = np.empty((self.Y, 4), dtype=np.complex128)
        V[:, 0] = amp                                # B
        V[:, 1] = amp * self.mu                      # G
        V[:, 2] = -1j * self.logn * amp              # d/dt B
        V[:, 3] = -1j * self.logn * amp * self.mu    # d/dt G
        if chunk is None:
            chunk = max(1, int(4_000_000 // self.Y))
        out = np.empty((len(ts), 4), dtype=np.complex128)
        for i in range(0, len(ts), chunk):
            tt = ts[i:i + chunk]
            Emat = np.exp(-1j * np.outer(tt, self.logn))
            out[i:i + chunk] = Emat @ V
        B, G, Bt, Gt = out[:, 0], out[:, 1], out[:, 2], out[:, 3]
        R = G * B - 1.0
        Rt = Gt * B + G * Bt
        s = sigma + 1j * ts
        zeta_approx = B + np.exp((1.0 - s) * math.log(self.Y)) / (s - 1.0)   # (E) without r_Y
        return dict(R=R, Rt=Rt, G=G, B=B, zeta=zeta_approx)

    def energy(self, sigma, Ts):
        """E_Y(sigma;T) by 8-point Gauss-Legendre on [T-h, T+h] for each T (same Y)."""
        Ts = np.asarray(Ts, dtype=np.float64)
        nodes = (Ts[:, None] + self.h * GL_X[None, :]).ravel()
        ev = self.eval(sigma, nodes)
        f = (np.abs(ev['R']) ** 2 + np.abs(ev['Rt']) ** 2 / self.Omega ** 2).reshape(len(Ts), -1)
        E = self.h * (f @ GL_W)
        # pointwise values at the centres too
        evc = self.eval(sigma, Ts)
        return E, evc


def rec(Y, T, sigma, E, evc_i, Omega):
    return dict(Y=Y, T=round(float(T), 6), sigma=round(float(sigma), 6), E=float(E),
                ratio_12OmegaE=float(12 * Omega * E), absR_T=float(abs(evc_i['R'])),
                abs_zeta_T=float(abs(evc_i['zeta'])), abs_G_T=float(abs(evc_i['G'])))


# ----------------------------------------------------------------------------------------------
def cmd_validate(args):
    out = {}
    mu = mobius_sieve(200 * 200)
    for Y in [12, 30, 60]:
        N = Y * Y
        e = np.zeros(N + 1, dtype=np.int64)
        for a in range(1, Y + 1):
            if mu[a]:
                e[a:a * Y + 1:a] += int(mu[a])
        e[1] -= 1
        assert np.all(e[1:Y + 1] == 0)
        nat = Native(mu, Y)
        for sigma, T in [(0.6, 7.3), (0.75, 40.0), (0.9, 123.4)]:
            ns = np.arange(Y + 1, N + 1)
            idx = np.nonzero(e[Y + 1:N + 1])[0]
            nn = ns[idx].astype(np.float64)
            cc = e[Y + 1:N + 1][idx].astype(np.float64)
            a = cc * nn ** (-sigma)
            Rdirect = np.sum(a * np.exp(-1j * T * np.log(nn)))
            ev = nat.eval(sigma, [T])
            errR = abs(Rdirect - ev['R'][0])
            # exact (D)+(O) formula vs quadrature
            Om = nat.Omega
            h = nat.h
            ln = np.log(nn)
            D = 2 * h * np.sum(a * a * (1 + ln ** 2 / Om ** 2))
            O = 0.0
            for i in range(len(nn)):
                dl = ln[i + 1:] - ln[i]
                O += 4 * np.sum(a[i] * a[i + 1:] * (1 + ln[i] * ln[i + 1:] / Om ** 2)
                                * np.cos(T * dl) * np.sin(h * dl) / dl)
            Eq, _ = nat.energy(sigma, [T])
            out[f"Y={Y},sigma={sigma},T={T}"] = dict(R_two_ways_abs_diff=float(errR),
                                                    E_quadrature=float(Eq[0]), D_plus_O=float(D + O),
                                                    rel_diff=float(abs(Eq[0] - D - O) / (D + O)))
    # zeta approximation (E) against mpmath at a few points
    import mpmath as mp
    mp.mp.dps = 30
    mu2 = mobius_sieve(50000)
    zchk = []
    for T in [1500.3, 7005.1, 12345.6]:
        Y = Y_of_T(T)
        nat = Native(mu2, Y)
        for sigma in [sigma0(Y), 0.6]:
            ev = nat.eval(sigma, [T])
            z = complex(mp.zeta(mp.mpc(sigma, T)))
            zchk.append(dict(T=T, Y=Y, sigma=sigma, zeta_mp=abs(z), abs_diff=abs(z - ev['zeta'][0]),
                             bound_2Y_minus_sigma=2 * Y ** (-sigma)))
    out['zeta_E_check'] = zchk
    print(json.dumps(out, indent=1))


def cmd_dtable(args):
    rows = []
    for Y in [int(v) for v in args.ys.split(',')]:
        N = Y * Y
        mu = mobius_sieve(Y)
        e = np.zeros(N + 1, dtype=np.int32)
        for a in range(1, Y + 1):
            if mu[a]:
                e[a:a * Y + 1:a] += int(mu[a])
        e[1] -= 1
        Om = 2 * math.log(Y)
        h = 1 / Om
        nz = np.nonzero(e)[0]
        nn = nz.astype(np.float64)
        c2 = e[nz].astype(np.float64) ** 2
        ln = np.log(nn)
        s0 = sigma0(Y)
        res = dict(Y=Y, sigma0_c2=s0, Omega=Om, threshold_1_over_12Omega=1 / (12 * Om),
                   mean_e2_over_window=float(np.sum(c2) / (N - Y)), max_abs_e=int(np.max(np.abs(e))))
        for sig in sorted(set([min(s0, 0.999), 0.6, 0.75, 0.9])):
            D = 2 * h * np.sum(c2 * nn ** (-2 * sig) * (1 + ln ** 2 / Om ** 2))
            LY = sum(1.0 / k for k in range(1, 2 * Y * Y + 1)) if Y <= 3000 else math.log(2 * Y * Y) + 0.5773
            Dbound = 8 * h * LY ** 3 * Y ** (1 - 2 * sig) / (1 - 2 ** (1 - 2 * sig))
            res[f"sigma={sig:.4f}"] = dict(D=float(D), twelveOmegaD=float(12 * Om * D),
                                          PR_bound_D=float(Dbound))
        rows.append(res)
        print(json.dumps(res), file=sys.stderr)
    print(json.dumps(rows, indent=1))


def cmd_curve(args):
    t0 = time.time()
    ymax = args.ymax
    mu = mobius_sieve(ymax)
    c = args.c
    recs = []
    worst = []
    # (1) every integer Y in [ylo, yhi]: 3 T values per Y (both ends and middle of its T-interval)
    Ystart = args.ylo
    while sigma0(Ystart, c) > 0.999:
        Ystart += 1
    for Y in (range(0) if args.skip_full else range(Ystart, args.yhi + 1)):
        a, b = T_range_of_Y(Y)
        Ts = np.array([a + 1e-6, (a + b) / 2, b])
        nat = Native(mu, Y)
        s = sigma0(Y, c)
        E, evc = nat.energy(s, Ts)
        for i in range(3):
            r = rec(Y, Ts[i], s, E[i], {k: v[i] for k, v in evc.items()}, nat.Omega)
            recs.append((r['ratio_12OmegaE'], r))
    full_count = len(recs)
    t1 = time.time()
    # (2) sampled Y (log-uniform) above yhi
    rng = np.random.default_rng(args.seed)
    ys = np.unique(np.exp(rng.uniform(math.log(args.yhi + 1), math.log(ymax), args.nsample)).astype(int))
    for Y in ys:
        Y = int(Y)
        a, b = T_range_of_Y(Y)
        Ts = np.array([(a + b) / 2])
        nat = Native(mu, Y)
        s = sigma0(Y, c)
        E, evc = nat.energy(s, Ts)
        r = rec(Y, Ts[0], s, E[0], {k: v[0] for k, v in evc.items()}, nat.Omega)
        recs.append((r['ratio_12OmegaE'], r))
    t2 = time.time()
    # (3) sigma-monotonicity sub-check: sigma grid in [sigma0, 0.999] for a subsample
    sub = []
    for Y in list(range(Ystart, args.yhi + 1, max(1, (args.yhi - Ystart) // 40))) + [int(v) for v in ys[::max(1, len(ys) // 20)]]:
        a, b = T_range_of_Y(Y)
        T = (a + b) / 2
        nat = Native(mu, Y)
        s0 = sigma0(Y, c)
        grid = np.linspace(s0, 0.999, 8)
        rr = []
        for s in grid:
            E, _ = nat.energy(s, [T])
            rr.append(float(12 * nat.Omega * E[0]))
        sub.append(dict(Y=Y, T=T, sigma0=s0, ratios_on_sigma_grid=rr,
                        max_ratio_on_grid=max(rr), argmax_sigma=float(grid[int(np.argmax(rr))])))
    ratios = np.array([x[0] for x in recs])
    recs.sort(key=lambda x: -x[0])
    out = dict(c=c, Y_full_range=[Ystart, args.yhi], full_points=full_count,
               sampled_Y=int(len(ys)), Ymax=ymax,
               T_full_range=[T_range_of_Y(Ystart)[0], T_range_of_Y(args.yhi)[1]],
               T_sampled_range=[T_range_of_Y(int(ys.min()))[0], T_range_of_Y(int(ys.max()))[1]],
               max_ratio=float(ratios.max()), median_ratio=float(np.median(ratios)),
               quantiles={q: float(np.quantile(ratios, q)) for q in [0.5, 0.9, 0.99, 0.999]},
               top20=[x[1] for x in recs[:20]],
               sigma_grid_subcheck=dict(n=len(sub), max_ratio=max(x['max_ratio_on_grid'] for x in sub),
                                        all_argmax_at_sigma0=all(abs(x['argmax_sigma'] - x['sigma0']) < 1e-12 for x in sub),
                                        rows=sub[:6]),
               seconds=dict(full=t1 - t0, sampled=t2 - t1, total=time.time() - t0))
    # ratio-by-decade summary
    dec = {}
    for r, d in recs:
        k = int(math.floor(math.log10(d['T'])))
        dec.setdefault(k, []).append(r)
    out['by_T_decade'] = {f"1e{k}": dict(n=len(v), max=float(max(v)), median=float(np.median(v)))
                          for k, v in sorted(dec.items())}
    print(json.dumps(out, indent=1))


def cmd_resonance(args):
    """Search heights where the Euler product over p <= P of 1/(1-p^{-s}) is extreme at sigma_0(Y(t))."""
    t0 = time.time()
    primes = [p for p in range(2, args.P + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    lp = np.log(np.array(primes, dtype=np.float64))
    mu = mobius_sieve(Y_of_T(args.thi) + 10)
    found = {'large': [], 'small': []}
    for (lo, hi) in [(args.tlo, args.thi)]:
        step = 0.02
        nblk = 200000
        cand_large, cand_small = [], []
        T = lo
        while T < hi:
            ts = np.arange(T, min(hi, T + nblk * step), step)
            # sigma0 depends on Y(t); compute per t
            Ys = np.ceil(4 * (ts + 2)).astype(np.float64)
            L = np.log(Ys)
            s0 = 0.5 + args.c * np.log(L) / L
            if args.sigma is not None:
                s0 = np.full_like(ts, args.sigma)
            logabs = np.zeros_like(ts)
            for j, p in enumerate(primes):
                pw = np.exp(-s0 * lp[j])
                z = 1 - pw * np.exp(-1j * ts * lp[j])
                logabs -= np.log(np.abs(z))
            # local extremes per window of width 5
            w = int(5 / step)
            for k in range(0, len(ts) - w, w):
                seg = logabs[k:k + w]
                i = int(np.argmax(seg)); cand_large.append((seg[i], ts[k + i]))
                i = int(np.argmin(seg)); cand_small.append((seg[i], ts[k + i]))
            T += nblk * step
        cand_large.sort(key=lambda x: -x[0])
        cand_small.sort(key=lambda x: x[0])
        for kind, cands in [('large', cand_large[:args.k]), ('small', cand_small[:args.k])]:
            for lz, tc in cands:
                # refine: scan T in [tc-0.5, tc+0.5] with the true Y(T) and full energy
                best = None
                for T in np.arange(tc - 0.5, tc + 0.5, 0.05):
                    Y = Y_of_T(T)
                    nat = Native(mu, Y)
                    s = sigma0(Y, args.c) if args.sigma is None else args.sigma
                    E, evc = nat.energy(s, [T])
                    r = rec(Y, T, s, E[0], {k: v[0] for k, v in evc.items()}, nat.Omega)
                    r['log_zetaX_euler'] = float(lz)
                    r['absR_over_abszeta'] = r['absR_T'] / r['abs_zeta_T']
                    if best is None or r['ratio_12OmegaE'] > best['ratio_12OmegaE']:
                        best = r
                found[kind].append(best)
    for kind in found:
        found[kind].sort(key=lambda r: -r['ratio_12OmegaE'])
    out = dict(P=args.P, c=args.c, fixed_sigma=args.sigma, t_range=[args.tlo, args.thi], k=args.k,
               max_ratio_large=max(r['ratio_12OmegaE'] for r in found['large']),
               max_ratio_small=max(r['ratio_12OmegaE'] for r in found['small']),
               max_abs_zeta_seen=max(r['abs_zeta_T'] for r in found['large']),
               min_abs_zeta_seen=min(r['abs_zeta_T'] for r in found['small']),
               large=found['large'][:15], small=found['small'][:15], seconds=time.time() - t0)
    print(json.dumps(out, indent=1))


def cmd_mechanism(args):
    """At fixed sigma (and at sigma0), sample t uniformly in [tlo, thi] with Y = Y(t) and regress
    log|R_Y| on log|zeta|. Slope ~ 0: G_Y mollifies the size of zeta. Slope ~ 1: |R_Y| ~ |zeta| * noise."""
    t0 = time.time()
    rng = np.random.default_rng(args.seed)
    mu = mobius_sieve(Y_of_T(args.thi) + 10)
    ts = np.sort(rng.uniform(args.tlo, args.thi, args.n))
    sigmas = [float(x) for x in args.sigmas.split(',')]
    res = {}
    data = {s: [] for s in sigmas + ['sigma0']}
    for t in ts:
        Y = Y_of_T(t)
        nat = Native(mu, Y)
        for s in sigmas + ['sigma0']:
            sg = sigma0(Y, args.c) if s == 'sigma0' else s
            ev = nat.eval(sg, [t])
            data[s].append((abs(ev['zeta'][0]), abs(ev['R'][0]), abs(ev['G'][0])))
    for s, rows in data.items():
        a = np.array(rows)
        lz, lr = np.log(a[:, 0]), np.log(a[:, 1])
        slope, icpt = np.polyfit(lz, lr, 1)
        # conditional medians by |zeta| quantile bins
        qs = np.quantile(a[:, 0], [0, 0.5, 0.9, 0.99, 1.0])
        bins = []
        for lo, hi in zip(qs[:-1], qs[1:]):
            m = (a[:, 0] >= lo) & (a[:, 0] <= hi)
            bins.append(dict(zeta_range=[float(lo), float(hi)], n=int(m.sum()),
                             median_absR=float(np.median(a[m, 1])), max_absR=float(np.max(a[m, 1])),
                             median_absR_over_zeta=float(np.median(a[m, 1] / a[m, 0]))))
        res[str(s)] = dict(n=len(rows), slope_logR_on_logzeta=float(slope), corr=float(np.corrcoef(lz, lr)[0, 1]),
                           median_absR=float(np.median(a[:, 1])), max_absR=float(a[:, 1].max()),
                           frac_absR_ge_0_354=float(np.mean(a[:, 1] >= 0.354)), bins=bins)
    print(json.dumps(dict(t_range=[args.tlo, args.thi], n=args.n, c=args.c, results=res,
                          seconds=time.time() - t0), indent=1))


def cmd_points(args):
    """E_Y on sigma_0(Y) (and given extra sigmas) at listed heights T, Y = ceil(4(T+2))."""
    Ts = [float(x) for x in args.ts.split(',')]
    mu = mobius_sieve(Y_of_T(max(Ts)) + 10)
    out = []
    for T in Ts:
        Y = Y_of_T(T)
        nat = Native(mu, Y)
        for sg in [sigma0(Y, args.c)] + [float(x) for x in args.sigmas.split(',') if x]:
            E, evc = nat.energy(sg, [T])
            out.append(rec(Y, T, sg, E[0], {k: v[0] for k, v in evc.items()}, nat.Omega))
    print(json.dumps(dict(c=args.c, rows=out), indent=1))


def e_Y_of_n(n, Y, primes):
    """e_Y(n) = sum_{d | n, n/Y <= d <= Y} mu(d) for Y < n <= Y^2 (exact integer arithmetic)."""
    ps = []
    m = n
    for p in primes:
        if p * p > m:
            break
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
    if m > 1:
        ps.append(m)
    tot = 0
    divs = [(1, 1)]
    for p in ps:
        divs += [(d * p, -s) for d, s in divs]
    for d, sg in divs:
        if d <= Y and d * Y >= n:
            tot += sg
    return tot


def cmd_dmc(args):
    """Monte Carlo estimate of D_Y(sigma) (importance sampling n ~ x^{-2 sigma} on (Y, Y^2]),
    validated against the exact sieve value at small Y."""
    rng = np.random.default_rng(args.seed)
    out = []
    for Y, sigma in json.loads(args.points):
        Y = int(Y)
        pr = np.nonzero(mobius_sieve(Y + 1) == -1)[0]          # mu=-1 includes all primes
        primes = [int(p) for p in pr if all(p % q for q in range(2, int(p ** 0.5) + 1))]
        a = 1.0 - 2.0 * sigma                                     # sampling density proportional to x^{-2 sigma} = x^{a-1}
        lo, hi = float(Y + 1), float(Y) ** 2 + 1.0
        Zint = (hi ** a - lo ** a) / a                            # int_lo^hi x^{-2 sigma} dx
        u = rng.uniform(0, 1, args.n)
        xs = (lo ** a + u * (hi ** a - lo ** a)) ** (1.0 / a)
        Om = 2 * math.log(Y)
        vals = []
        for x in xs:
            n = int(x)
            if n <= Y:
                n = Y + 1
            e = e_Y_of_n(n, Y, primes)
            # weight correction n^{-2 sigma} / x^{-2 sigma} ~ 1 ; keep exact ratio
            w = (n / x) ** (-2 * sigma) * (1 + math.log(n) ** 2 / Om ** 2)
            vals.append(e * e * w)
        vals = np.array(vals)
        S = Zint * vals.mean()
        Serr = Zint * vals.std() / math.sqrt(len(vals))
        h = 1 / Om
        D = 2 * h * S
        out.append(dict(Y=Y, sigma=sigma, n_samples=args.n, D_est=D, D_stderr=2 * h * Serr,
                        twelveOmegaD_est=12 * Om * D, twelveOmegaD_stderr=12 * Om * 2 * h * Serr,
                        sample_mean_e2w=float(vals.mean())))
        print(json.dumps(out[-1]), file=sys.stderr)
    print(json.dumps(out, indent=1))


def cmd_mpcheck(args):
    """Independent mpmath recomputation of R_Y = G_Y B_Y - 1 and zeta at listed (Y,T,sigma) points."""
    import mpmath as mp
    mp.mp.dps = args.dps
    pts = json.loads(args.points)
    mu = mobius_sieve(max(int(p[0]) for p in pts))
    out = []
    for Y, T, sigma in pts:
        Y = int(Y)
        s = mp.mpc(sigma, T)
        G = mp.mpc(0); B = mp.mpc(0)
        for n in range(1, Y + 1):
            term = mp.exp(-s * mp.log(n))
            B += term
            if mu[n]:
                G += int(mu[n]) * term
        R = G * B - 1
        z = mp.zeta(s)
        nat = Native(mu, Y)
        ev = nat.eval(sigma, [T])
        out.append(dict(Y=Y, T=T, sigma=sigma, absR_mp=float(abs(R)), absR_float=float(abs(ev['R'][0])),
                        absdiff_R=float(abs(complex(R) - ev['R'][0])), abs_zeta_mp=float(abs(z)),
                        absdiff_zeta_vs_B_plus_pole=float(abs(complex(z) - ev['zeta'][0])),
                        bound_2Y_minus_sigma=2 * Y ** (-sigma)))
        print(json.dumps(out[-1]), file=sys.stderr)
    print(json.dumps(dict(dps=args.dps, rows=out), indent=1))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('validate')
    d = sp.add_parser('dtable'); d.add_argument('--ys', default='5500,1000,2000,4000')
    c = sp.add_parser('curve')
    c.add_argument('--ylo', type=int, default=5000); c.add_argument('--yhi', type=int, default=20000)
    c.add_argument('--ymax', type=int, default=400008); c.add_argument('--nsample', type=int, default=1500)
    c.add_argument('--c', type=float, default=2.0); c.add_argument('--seed', type=int, default=910)
    c.add_argument('--skip-full', action='store_true', help='only the sampled-Y block (same seed => same Y sample)')
    r = sp.add_parser('resonance')
    r.add_argument('--tlo', type=float, default=1400); r.add_argument('--thi', type=float, default=1e5)
    r.add_argument('--P', type=int, default=31); r.add_argument('--k', type=int, default=25)
    r.add_argument('--c', type=float, default=2.0)
    r.add_argument('--sigma', type=float, default=None)
    m = sp.add_parser('mechanism')
    m.add_argument('--tlo', type=float, default=2000); m.add_argument('--thi', type=float, default=20000)
    m.add_argument('--n', type=int, default=1500); m.add_argument('--sigmas', default='0.55,0.6,0.7,0.8')
    m.add_argument('--c', type=float, default=2.0); m.add_argument('--seed', type=int, default=11)
    pt = sp.add_parser('points')
    pt.add_argument('--ts', required=True); pt.add_argument('--sigmas', default='')
    pt.add_argument('--c', type=float, default=2.0)
    dm = sp.add_parser('dmc')
    dm.add_argument('--points', required=True); dm.add_argument('--n', type=int, default=4000)
    dm.add_argument('--seed', type=int, default=5)
    q = sp.add_parser('mpcheck')
    q.add_argument('--points', required=True); q.add_argument('--dps', type=int, default=25)
    a = ap.parse_args()
    {'dmc': cmd_dmc, 'points': cmd_points, 'mpcheck': cmd_mpcheck, 'validate': cmd_validate, 'dtable': cmd_dtable, 'curve': cmd_curve,
     'resonance': cmd_resonance, 'mechanism': cmd_mechanism}[a.cmd](a)


if __name__ == '__main__':
    main()

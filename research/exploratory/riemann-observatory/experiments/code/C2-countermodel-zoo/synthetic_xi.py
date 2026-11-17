#!/usr/bin/env python3
"""C2 countermodel zoo -- synthetic xi with an injected off-line quadruple (Hadamard-product model).

Model:  xi~(s) = xi(s) P(s),  P(s) = prod_{rho in Q} (1 - s/rho),  Q = {rho0, conj rho0, 1-rho0, 1-conj rho0},
rho0 = beta + i gamma0, 1/2 < beta < 1.  Then xi~ is entire of order 1, real on R, xi~(1-s) = xi~(s), xi~(0) = 1/2,
its zeros are those of xi plus Q; it is NOT of the form (Gamma factor) x (Dirichlet series).

Computations (labels in REPORT.md):
 (L) Li coefficients lambda_n(xi~) = lambda_n(xi) + sum_{rho in Q} [1 - (1-1/rho)^n]  (exact identity, Li 1997).
     lambda_n(xi) is computed NON-RIGOROUSLY from the first 100000 (rigorous, on-line) zeros plus a smooth tail
     int_T^inf 2(1-cos(2n arctan(1/(2g)))) (1/2pi) log(g/2pi) dg; checked against lambda_1, lambda_2.
     Output: first n with lambda_n(xi~) < 0 for several (beta, gamma0).
 (J) Taylor coefficients of xi~(1/2+z) = sum_k g~(k) z^{2k}/k!  (GORZ normalisation up to a constant), in Arb;
     Turan inequalities g(k)^2 - g(k-1) g(k+1) >= 0, and hyperbolicity of Jensen polynomials
     J^{d,n}(X) = sum_j C(d,j) g(n+j) X^j for small (d, n) (roots via mpmath, NON-RIGOROUS).
Usage: python3 synthetic_xi.py OUTDIR ZEROFILE1 [ZEROFILE2 ...]
"""
import sys, os, json, time, hashlib, math
import numpy as np
import mpmath as mp
import flint
from flint import acb, arb, acb_series
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import versions


def load_zeros(files):
    g = []
    for fn in files:
        with open(fn) as fh:
            for line in fh:
                p = line.split()
                if len(p) >= 2:
                    g.append(float(p[1]))
    return np.array(sorted(g))


def lambda_xi(n_list, gam):
    """NON-RIGOROUS Li coefficients of xi from zeros 1/2 +- i gam (assumed on the line, as certified for the list)
    plus smooth tail above T = max(gam)."""
    T = gam[-1]
    phi = 2 * np.arctan(1 / (2 * gam))
    out = {}
    for n in n_list:
        s = float(np.sum(2 * (1 - np.cos(n * phi))))
        f = lambda g: 2 * (1 - mp.cos(2 * n * mp.atan(1 / (2 * g)))) * mp.log(g / (2 * mp.pi)) / (2 * mp.pi)
        tail = float(mp.quad(f, [T, 10 * T, 100 * T, mp.inf]))
        out[n] = (s + tail, tail)
    return out


def lambda_quad(n, beta, gam0):
    rho = mp.mpc(beta, gam0)
    tot = 0
    for r in (rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho)):
        tot += 1 - (1 - 1 / r) ** n
    return float(mp.re(tot))


def li_experiment(gam, cases, nmax=200000):
    # lambda_xi on a geometric-ish grid of n, interpolated in between (it is smooth ~ (n/2)log n + c n)
    grid = sorted(set([1, 2, 3, 5, 10, 20, 50, 100, 200, 500] + [int(x) for x in np.geomspace(1000, nmax, 60)]))
    lx = lambda_xi(grid, gam)
    res = dict(lambda_xi_samples={str(k): v[0] for k, v in lx.items()},
               tail_fraction={str(k): v[1] / v[0] for k, v in lx.items() if v[0] != 0})
    gx, gy = np.array(grid, float), np.array([lx[k][0] for k in grid])
    interp = lambda n: float(np.interp(n, gx, gy))
    out = []
    for beta, gam0 in cases:
        first = None
        rate = 0.5 * math.log((beta ** 2 + gam0 ** 2) / ((1 - beta) ** 2 + gam0 ** 2))
        # scan n; quadruple term is exact, lambda_xi interpolated (smooth)
        n = 1
        step = 1
        while n <= nmax:
            q = lambda_quad(n, beta, gam0)
            if interp(n) + q < 0:
                first = n
                break
            n += step
            if n > 2000:
                step = max(1, n // 2000)
        out.append(dict(beta=beta, gamma0=gam0, growth_rate_log_abs=rate,
                        predicted_scale_1_over_rate=1 / rate,
                        first_negative_n=first, scanned_up_to=nmax))
        print('li', beta, gam0, first, flush=True)
    res['cases'] = out
    return res


# ---------------- Taylor coefficients / Jensen ----------------
def xi_taylor(K, prec):
    """Arb coefficients c_j of xi(1/2+z) = sum c_j z^j, j < K."""
    flint.ctx.prec = prec
    z = acb_series([acb("0.5"), 1], prec=K)
    zeta = acb_series.zeta(z)
    gam = acb_series.gamma(z * acb("0.5"))
    pis = (z * (-acb.pi().log() / 2)).exp()
    pref = z * (z - 1) * acb("0.5")
    return (pref * pis * gam * zeta).coeffs()


def poly_mul(a, b, K):
    out = [acb(0)] * K
    for i, x in enumerate(a):
        if i >= K:
            break
        for j, y in enumerate(b):
            if i + j >= K:
                break
            out[i + j] += x * y
    return out


def jensen_experiment(cases, K=120, prec=1200, dmax=30, nmax=30):
    c = xi_taylor(K, prec)
    res = {}
    for label, beta, gam0 in [('xi', None, None)] + [(f'beta={b},gamma0={g}', b, g) for b, g in cases]:
        cc = list(c)
        if beta is not None:
            # P(1/2+z) = prod (1 - (1/2+z)/rho) = prod ((rho-1/2) - z)/rho  as polynomial in z
            P = [acb(1)]
            for r in (acb(beta, gam0), acb(beta, -gam0), acb(1 - beta, -gam0), acb(1 - beta, gam0)):
                P = poly_mul(P, [(r - acb("0.5")) / r, acb(-1) / r], 5)
            cc = poly_mul(cc, P, K)
        # g(k) = c_{2k} k!  (even part; odd coefficients vanish)
        odd_max = max(float(abs(cc[j]).upper()) for j in range(1, K, 2))
        g = [cc[2 * k].real * arb.fac_ui(k) for k in range(K // 2)]
        tur = [(g[k] ** 2 - g[k - 1] * g[k + 1]) for k in range(1, len(g) - 1)]
        tur_ok = [bool(x > 0) for x in tur]
        gm = [mp.mpf(x.mid().str(60, radius=False)) for x in g]
        mp.mp.dps = 60
        hyp = {}
        for d in range(2, dmax + 1):
            row = []
            for n in range(0, nmax + 1):
                if n + d >= len(gm):
                    break
                coeffs = [mp.binomial(d, j) * gm[n + j] for j in range(d + 1)]
                roots = mp.polyroots(coeffs[::-1], maxsteps=400, extraprec=600)
                mx = max(abs(mp.im(r)) / (1 + abs(r)) for r in roots)
                row.append(float(mx))
            hyp[d] = row
        nonhyp = [(d, n) for d, row in hyp.items() for n, v in enumerate(row) if v > 1e-12]
        res[label] = dict(odd_coeff_max=odd_max, n_g=len(g),
                          turan_all_positive=all(tur_ok), turan_first_failure=(tur_ok.index(False) + 1) if not all(tur_ok) else None,
                          turan_proven_by_arb=all(tur_ok),
                          nonhyperbolic_pairs_d_n=nonhyp[:200],
                          smallest_d_nonhyperbolic_at_n0=min([d for d, n in nonhyp if n == 0], default=None),
                          max_rel_imag_by_d_at_n0={str(d): hyp[d][0] for d in hyp})
        print('jensen', label, res[label]['turan_all_positive'], res[label]['smallest_d_nonhyperbolic_at_n0'],
              len(nonhyp), flush=True)
    return res


def main():
    outdir = sys.argv[1]
    files = sys.argv[2:]
    t0 = time.time()
    rep = dict(model='synthetic xi~ = xi * P_quadruple', versions=versions())
    gam = load_zeros(files)
    rep['n_zeros_used'] = int(len(gam)); rep['T_max_zero'] = float(gam[-1])
    chk = lambda_xi([1, 2], gam)
    rep['check_lambda1_lambda2'] = dict(computed=[chk[1][0], chk[2][0]],
                                        reference=[0.0230957089661210338, 0.0923457352280327])
    cases_li = [(0.6, 14.0), (0.75, 14.0), (0.6, 30.0), (0.75, 30.0), (0.8085, 85.7), (0.6, 100.0)]
    rep['li'] = li_experiment(gam, cases_li)
    print('li done', round(time.time() - t0, 1), flush=True)
    cases_j = [(0.6, 5.0), (0.75, 10.0), (0.6, 14.0), (0.9, 14.0), (0.75, 30.0)]
    rep['jensen'] = jensen_experiment(cases_j)
    rep['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'synthetic_xi.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn, rep['runtime_s'])


if __name__ == '__main__':
    main()

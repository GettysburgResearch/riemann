#!/usr/bin/env python3
"""SKEPTIC replay of C2-16 (Li coefficients of xi~ = xi * P_quadruple), NON-RIGOROUS:
lambda_n(xi) = sum over the first 100000 zeros (both gamma and -gamma, assumed on the line, as they are
certified) of 2(1 - cos(n theta_g)), theta_g = 2 arctan(1/(2g)), + smooth tail above T (scipy quad, density
(1/2pi) log(g/2pi)), computed EXACTLY for every n in a window (no interpolation, unlike synthetic_xi.py);
quadruple term sum_{rho in Q} [1 - (1-1/rho)^n] exact (mpmath).  Reports the first n with lambda_n(xi~)<0
inside each window and checks that lambda_n(xi~) > 0 on the rest of the window.
Usage: python3 sk_li.py OUTDIR ZEROFILE1 ZEROFILE2"""
import sys, os, json, time, math
import numpy as np
import mpmath as mp
from scipy.integrate import quad

g = []
for fn in sys.argv[2:]:
    for line in open(fn):
        p = line.split()
        if len(p) >= 2:
            g.append(float(p[1]))
g = np.array(sorted(g)); T = g[-1]
theta = 2 * np.arctan(1 / (2 * g))


def lam_xi(ns):
    ns = np.asarray(ns, float)
    out = np.zeros(ns.size)
    for k in range(0, g.size, 5000):
        th = theta[k:k + 5000]
        out += np.sum(4 * np.sin(np.outer(ns, th) / 2) ** 2, axis=1)
    tails = []
    for n in ns:
        f = lambda u: 4 * math.sin(n * math.atan(u / 2)) ** 2 * math.log(1 / (2 * math.pi * u)) / (2 * math.pi) / u ** 2
        val, err = quad(f, 0, 1 / T, limit=400, epsabs=1e-10, epsrel=1e-12)
        tails.append(val)
    return out + np.array(tails), np.array(tails)


def lam_Q(n, beta, gam):
    rho = mp.mpc(beta, gam)
    return float(mp.re(sum(1 - (1 - 1 / r) ** n for r in (rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho)))))


def main():
    t0 = time.time()
    out = {}
    lx, tl = lam_xi([1, 2, 100000])
    out['lambda_1,2,1e5'] = [float(x) for x in lx]
    out['reference_lambda_1,2 (Keiper/Li), lambda_1e5 (Johansson)'] = [0.0230957089661210, 0.0923457352280327, 462580.78]
    cases = [(0.6, 14.0, 1, 21500), (0.75, 14.0, 1, 7600), (0.6, 30.0, 105000, 113500), (0.75, 30.0, 38000, 41500)]
    res = []
    for beta, gam, n0, n1 in cases:
        ns = np.arange(n0, n1 + 1)
        lx, _ = lam_xi(ns)
        q = np.array([lam_Q(int(n), beta, gam) for n in ns])
        tot = lx + q
        neg = np.nonzero(tot < 0)[0]
        first = int(ns[neg[0]]) if neg.size else None
        rate = 0.5 * math.log((beta ** 2 + gam ** 2) / ((1 - beta) ** 2 + gam ** 2))
        r = dict(beta=beta, gamma0=gam, window=[n0, n1], first_negative_in_window=first,
                 min_margin_before_first=float(np.min(tot[:neg[0]])) if neg.size else float(np.min(tot)),
                 one_over_rate=1 / rate, gamma0_sq_over_delta=gam ** 2 / (beta - 0.5))
        res.append(r)
        print(r, round(time.time() - t0, 1), flush=True)
    out['cases'] = res
    out['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], 'sk_li.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()

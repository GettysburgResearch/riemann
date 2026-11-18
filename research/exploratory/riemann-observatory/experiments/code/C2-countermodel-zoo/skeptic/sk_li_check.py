"""SKEPTIC: accuracy check of sk_li.py near the disputed crossings: stable tail (1-cos = 2 sin^2), mpmath tail
as in synthetic_xi.py, and the investigator's interpolated lambda_xi (from synthetic_xi.json samples)."""
import sys, json, math, numpy as np, mpmath as mp
from scipy.integrate import quad
D = sys.argv[1]
g = []
for fn in [D + '/zeros_1_50000.tsv', D + '/zeros_50001_100000.tsv']:
    for line in open(fn):
        p = line.split(); g.append(float(p[1]))
g = np.array(sorted(g)); T = g[-1]; theta = 2 * np.arctan(1 / (2 * g))
def zsum(n): return float(np.sum(4 * np.sin(n * theta / 2) ** 2))
def tail_stable(n):
    f = lambda u: 4 * math.sin(n * math.atan(u / 2)) ** 2 * math.log(1 / (2 * math.pi * u)) / (2 * math.pi) / u ** 2
    return quad(f, 0, 1 / T, limit=400, epsabs=1e-10, epsrel=1e-12)[0]
def tail_mp(n):
    f = lambda gg: 2 * (1 - mp.cos(2 * n * mp.atan(1 / (2 * gg)))) * mp.log(gg / (2 * mp.pi)) / (2 * mp.pi)
    return float(mp.quad(f, [T, 10 * T, 100 * T, mp.inf]))
def lamQ(n, b, gm):
    rho = mp.mpc(b, gm)
    return float(mp.re(sum(1 - (1 - 1 / r) ** n for r in (rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho)))))
sx = json.load(open(sys.argv[2]))['li']['lambda_xi_samples']
gx = np.array(sorted(int(k) for k in sx), float); gy = np.array([sx[str(int(k))] for k in gx])
interp = lambda n: float(np.interp(n, gx, gy))
print('lambda_1 zsum+stable tail', zsum(1) + tail_stable(1), 'ref 0.0230957089661210')
for n in [7395, 7477, 20855, 20857]:
    ts, tm = tail_stable(n), tail_mp(n)
    lx = zsum(n) + ts
    for b, gm in [(0.75, 14.0), (0.6, 14.0)]:
        q = lamQ(n, b, gm)
        print(n, (b, gm), 'tail stable/mp', round(ts, 6), round(tm, 6), 'lam_xi exact', round(lx, 3), 'interp', round(interp(n), 3), 'Q', round(q, 3), 'exact total', round(lx + q, 3), 'interp total', round(interp(n) + q, 3))

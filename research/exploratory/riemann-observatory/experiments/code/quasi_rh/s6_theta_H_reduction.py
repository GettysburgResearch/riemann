# s6_theta_H_reduction.py -- App. A.2 (l.3076-3101): theta(H w) = theta(gamma_sigma w) exactly (multiplier 1) for
#   H = (1 0; lam 1) -> sigma = '-',  H = (1 0; -lam 1) -> '+',  H = (u0 -1; 1 0) with u0 = 0, omega, -omega -> '0','-','+'
# (translation by Z+3O and SL_2(Z)-invariance).  Theta from DR (5.6)-(5.8), evaluated pointwise.
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_theta import *
th = FourierSeries(tau, 3, 7.0, const=SIGMA)
lam = cv(LAM)
G = {'0': ((1, 0), (0, 1)), '+': ((1, 0), (OMEGA, 1)), '-': ((1, 0), (OMEGA ** 2, 1))}
Hs = [("(1 0; lam 1)", ((1, 0), (lam, 1)), '-'), ("(1 0; -lam 1)", ((1, 0), (-lam, 1)), '+'),
      ("(0 -1; 1 0)", ((0, -1), (1, 0)), '0'), ("(w -1; 1 0)", ((OMEGA, -1), (1, 0)), '-'), ("(-w -1; 1 0)", ((-OMEGA, -1), (1, 0)), '+'),
      ("(1+3w -1; 1 0)", ((1 + 3 * OMEGA, -1), (1, 0)), '0'), ("(2+w -1; 1 0)", ((2 + OMEGA, -1), (1, 0)), '-')]
for name, H, sig in Hs:
    worst = 0; used = 0
    cand = [(x + 1j * y, v) for x in np.linspace(-1, 1, 21) for y in np.linspace(-1, 1, 21) for v in (0.5, 0.7, 0.9)]
    for (z, v) in cand:
        z1, v1 = act(H, z, v); z2, v2 = act(G[sig], z, v)
        if min(v1, v2) < 0.3 or v < 0.3: continue
        worst = max(worst, abs(th(z1, v1) - th(z2, v2)) / abs(th(z2, v2))); used += 1
        if used >= 6: break
    # negative control: a wrong cusp
    wrong = {'0': '+', '+': '-', '-': '0'}[sig]; bad = 0
    for (z, v) in cand:
        z1, v1 = act(H, z, v); z2, v2 = act(G[wrong], z, v)
        if min(v1, v2) < 0.3: continue
        bad = max(bad, abs(th(z1, v1) - th(z2, v2)) / abs(th(z2, v2))); break
    print("H=%-15s claimed cusp %s : %d points, max rel diff %.1e   (control vs cusp %s: %.1e)" % (name, sig, used, worst, wrong, bad))

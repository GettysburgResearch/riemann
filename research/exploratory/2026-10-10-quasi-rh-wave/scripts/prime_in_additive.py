"""Model for note Q: slot prime p ~ Z^{ls} moved into the additive variable s = p s'.
Variants:
  V0 (naive, J-note): signal retained, theta_eff = max(0, 1/12 - (1-beta)*ls/b); A-slot length lA = l - ls.
  V1 (honest, psi = conj eta): same direct side but principal signal multiplied by P^{-beta}
      => comparison B(1-ls) = 11/12 - lA/4 - b/12 + max(0, theta_eff*b, extra terms) + k/2.
Extra direct-side terms: equal-prime block ((b-ls)/12 - ls/2)_+, nonexceptional (b - ly/2 + kappa*ls/2) with kappa=1 (worst case).
beta: 'fb' = 7/8 fixed (feedback), 'sc' = self-consistent (beta = B).
"""
import sys; sys.path.insert(0, '/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/scripts')
import numpy as np, exponent_model as em
from scipy.optimize import minimize, brentq

def Blow_Q(b, lA, ls, P, beta, variant, kappa=1.0):
    lx, ly, h = em.geom(b, lA); M = lx + ly
    th = max(0.0, 1/12 - (1-beta)*ls/b)
    gram = max(0.0, th*b, (b-ls)/12 - ls/2, b - ly/2 + kappa*ls/2)
    k = max(0.0, (1 + 3*lA - 2*M)/4, M + lA - 1, (3*lA - 1)/2)
    base = 11/12 - lA/4 - b/12 + gram + k/2
    return base if variant == 'V0' else base/(1-ls)

def Bach(b, lA, ls, P, betamode, variant, detail=False):
    ok, c = em.feasible(b, lA, P)
    if not ok or ls < 0 or ls > em.geom(b, lA)[1]/2:
        return (np.inf, {}) if detail else np.inf
    hm, cls = em.Hmod(b, lA, P); hf = em.Hfloor(b, lA, P); hi = em.Hint(b, lA, P)
    rows = max(hm, hf, hi)
    if betamode == 'fb':
        bl = Blow_Q(b, lA, ls, P, 7/8, variant)
    else:  # self-consistent: smallest B with B >= Blow_Q(b,lA,ls,P,B)
        f = lambda B: B - Blow_Q(b, lA, ls, P, B, variant)
        bl = brentq(f, 0.5, 0.99) if f(0.5) < 0 < f(0.99) else (0.5 if f(0.5) >= 0 else np.inf)
    B = max(bl, rows)
    if detail:
        return B, dict(Blow=bl, Hmod=hm, Hfloor=hf, Hint=hi, cls=cls, active=[k for k, v in dict(Blow=bl,Hmod=hm,Hfloor=hf,Hint=hi).items() if v > B-1e-7])
    return B

def opt(betamode, variant, ls_fixed=None):
    P = dict(em.DEFAULT); best = (np.inf, None)
    for b in np.linspace(0.02, 0.35, 8):
        for lA in np.linspace(0.10, 0.30, 9):
            for ls in ([ls_fixed] if ls_fixed is not None else np.linspace(0.0, 0.12, 7)):
                v = Bach(b, lA, ls, P, betamode, variant)
                if v < best[0]: best = (v, (b, lA, ls))
    if ls_fixed is None:
        r = minimize(lambda p: Bach(p[0], p[1], p[2], P, betamode, variant), best[1], method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=800))
        x = r.x
    else:
        r = minimize(lambda p: Bach(p[0], p[1], ls_fixed, P, betamode, variant), best[1][:2], method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-10, maxiter=800))
        x = (r.x[0], r.x[1], ls_fixed)
    B, det = Bach(x[0], x[1], x[2], P, betamode, variant, detail=True)
    return B, x, det

if __name__ == '__main__':
    P = dict(em.DEFAULT)
    print("baseline (ls=0):", opt('fb', 'V0', ls_fixed=0.0)[:2])
    for variant in ['V0', 'V1']:
        for bm in ['fb', 'sc']:
            B, x, det = opt(bm, variant)
            print(f"{variant} beta={bm}: B={B:.6f} at b={x[0]:.4f} lA={x[1]:.4f} ls={x[2]:.4f} active={det['active']} class={np.round(det['cls'],4)} Blow={det['Blow']:.5f} Hmod={det['Hmod']:.5f} Hfloor={det['Hfloor']:.5f}")
    # scan ls for V0 fb and V1 fb at fixed geometry re-optimised over (b,lA)
    for variant in ['V0', 'V1']:
        for ls in [0.0, 0.02, 0.04, 0.06, 0.08, 0.10]:
            B, x, det = opt('sc', variant, ls_fixed=ls)
            print(f"  {variant} sc ls={ls:.2f}: B={B:.6f} b={x[0]:.4f} lA={x[1]:.4f} active={det['active']}")

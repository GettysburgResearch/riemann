# Quick reconstruction of the Part II nonprincipal endpoint exponent E(h; delta, x) for general (b, ell)
# E(h) = C0 + delta*(1/2+ell) + x*delta*ell - h*(1-R*)   with C0 = -1/4 + 5 ell/4 + b/6, h = (1+b+3 ell)/2
# R* from Prop 19.2 / eq (20.8) with alpha = 5/6, kappa = 3/4 (no Delta/4 loss):
import numpy as np
from scipy.optimize import minimize
alpha = 5/6
def Rstar(delta, x):
    Dx = 3 - 17*x/9
    Px = (2 - 8*x/9)*(1 - x)
    J = (alpha - delta)*Dx + delta*Px
    t = 1 + delta*Px/(2*J)
    return 1 - delta + (alpha - delta)*(t - 1)
def E(b, ell, delta, x):
    C0 = -1/4 + 5*ell/4 + b/6
    h = (1 + b + 3*ell)/2
    return C0 + delta*(1/2 + ell) + x*delta*ell - h*(1 - Rstar(delta, x))
def Emax(b, ell, n=241):
    ds = np.linspace(0, 5/6, n); xs = np.linspace(0, 1/2, n)
    D, X = np.meshgrid(ds, xs, indexing='ij')
    vals = E(b, ell, D, X)
    i = np.unravel_index(np.argmax(vals), vals.shape)
    return vals[i], ds[i[0]], xs[i[1]]
B = lambda ell: 11/12 - ell/4
print("paper (b,ell)=(1/8,1/6): Emax =", Emax(1/8, 1/6), " -E* at delta_c? B=", B(1/6))
# sanity: -E* lower bound 49/440640 = %.3e
print("49/440640 =", 49/440640)
# Liu's values
import math
bnew = -4/29 + 230*math.sqrt(921)/26709; lnew = (33 + 8*math.sqrt(921))/1653
print("Liu b_new, ell_new =", bnew, lnew, " B_new =", B(lnew), " Emax =", Emax(bnew, lnew, 401))
# optimize: maximize ell subject to Emax(b,ell) <= 0, b > 0
best = None
for b in np.linspace(0.0, 0.3, 61):
    lo, hi = 0.0, 0.4
    for _ in range(40):
        mid = (lo+hi)/2
        if Emax(b, mid, 121)[0] <= 0: lo = mid
        else: hi = mid
    if best is None or lo > best[1]: best = (b, lo)
print("best (b, ell) on grid:", best, " B =", B(best[1]))
# refine around best
b0, l0 = best
for b in np.linspace(b0-0.01, b0+0.01, 41):
    lo, hi = l0-0.01, l0+0.01
    for _ in range(40):
        mid = (lo+hi)/2
        if Emax(b, mid, 401)[0] <= 0: lo = mid
        else: hi = mid
    if lo > best[1]: best = (b, lo)
print("refined (b, ell):", best, " B =", B(best[1]), " active class:", Emax(best[0], best[1], 801))

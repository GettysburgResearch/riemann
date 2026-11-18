# Adversarial (optimised) search for violations of Lamzouri (2.4)/(2.5) with MT and flat kernels.
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(7)
s2 = np.sqrt(2)
# MT density f0(x) = cos(s2 x)/(s2 sin(1/s2)) on [-1/2,1/2]; K(xi) = int f0(x) e^{-2 pi i xi x} dx (entire)
def K_MT(z):
    z = np.asarray(z, dtype=complex); w = 2*np.pi*z
    c = 1/(s2*np.sin(1/s2))
    # int_{-1/2}^{1/2} cos(a x) cos(w x) dx = sum of sin terms
    def I(k):
        k = np.where(np.abs(k)<1e-12, 1e-12, k)
        return 2*np.sin(k/2)/k
    return c*0.5*(I(s2+w) + I(s2-w))
def K_flat(z):
    z = np.asarray(z, dtype=complex); out = np.ones_like(z); nz = np.abs(z)>1e-12
    out[nz] = np.sin(np.pi*z[nz])/(np.pi*z[nz]); return out
print("K_MT(0) =", K_MT(np.array([0.0]))[0])
def slack(params, n1, r, k, K, which):
    x1 = params[:n1]; xr = params[n1:n1+r]; xp = params[n1+r:n1+r+k]; yp = np.abs(params[n1+r+k:])+1e-6
    pts = np.concatenate([x1, xr, xp+1j*yp, xp-1j*yp]).astype(complex)
    mult = np.concatenate([np.ones(n1), 2*np.ones(r), np.ones(2*k)])
    D = pts[:,None]-pts[None,:]
    S = np.real((mult[:,None]*mult[None,:]*K(D)**2).sum()); Z = mult.sum()
    if which=="2.4": return n1 - (2*Z - S)
    return (n1 + r + 2*k) - (1.5*Z - 0.5*S)
best = {}
for K, kn in ((K_MT,"MT"), (K_flat,"flat")):
    for which in ("2.4","2.5"):
        bmin = np.inf
        for trial in range(60):
            n1, r, k = rng.integers(0,6), rng.integers(0,3), rng.integers(0,4)
            if n1+r+k == 0: continue
            p0 = np.concatenate([rng.uniform(0, 4, n1+r+k), rng.uniform(0.0, 0.5, k)])
            res = minimize(slack, p0, args=(n1,r,k,K,which), method="Nelder-Mead", options={"maxiter":4000, "xatol":1e-9, "fatol":1e-12})
            bmin = min(bmin, res.fun)
        best[(kn,which)] = bmin
print("min optimised slack (>=0 expected; 0 = extremal):", best)

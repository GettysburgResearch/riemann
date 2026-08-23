import numpy as np
from math import comb, log, sqrt
exec(open('sieve_common.py').read())  # provides mu, eta, NMAX, v, ln2

Xmin, Xmax = 64.0, 2.0e4
s = 0.3 + 2.0j

# LHS: direct quadrature of V*(X) X^{-s} dX/X on fine log grid (midpoint rule)
M = 1200000
lx = np.linspace(log(Xmin), log(Xmax), M+1)
xm = np.exp(0.5*(lx[:-1]+lx[1:])); wq = np.diff(lx)

def Vstar_vec(Xv):
    out = np.zeros(len(Xv))
    for i, X in enumerate(Xv):
        X23 = X**(2/3); X13 = X**(1/3)
        dmax = int(X23)
        d = np.arange(int(np.floor(X13))+1, dmax+1)
        d = d[mu[d] != 0]
        ehi = np.floor(X23/d).astype(np.int64)
        elo = np.floor(X23/(2*d)).astype(np.int64)
        tot = 0.0
        for di, eh, el in zip(d, ehi, elo):
            if eh <= el: continue
            e = np.arange(el+1, eh+1)
            y = di*e/X23
            tot += mu[di]*di**(-0.5)*np.sum(eta[e]*e**(-0.5)*v(y))
        out[i] = tot*sqrt((2/3)*log(X))/X**(1/6)
    return out

# too slow for 1.2M pts; instead integrate PER PAIR analytically-supported (exact Fubini both sides).
# Honest independent check: LHS via pair-driven X-integrals with INDEPENDENT parametrization (X-variable
# quadrature per pair), RHS via t-variable formula. Different variables, same truncation set.
lhs = 0.0+0.0j; rhs = 0.0+0.0j
demax = Xmax**(2/3)
pairs = 0
for e in range(1, int(demax)+1):
    if eta[e] == 0: continue
    dlo = e+1
    dhi = int(demax/e)
    for d in range(dlo, dhi+1):
        if mu[d] == 0: continue
        de = d*e
        Xlo = max(Xmin, de**1.5)
        Xhi = min(Xmax, d**3, (2*de)**1.5)
        if Xhi <= Xlo: continue
        pairs += 1
        # LHS piece: integral over X of mu(d)eta(e)(de)^{-1/2} v(de X^{-2/3}) sqrt((2/3)logX) X^{-1/6-s} dX/X
        K = 400
        lxp = np.linspace(log(Xlo), log(Xhi), K+1)
        xmp = np.exp(0.5*(lxp[:-1]+lxp[1:])); wqp = np.diff(lxp)
        integ = v(de*xmp**(-2/3))*np.sqrt((2/3)*np.log(xmp))*xmp**(-1/6-s)
        lhs += mu[d]*eta[e]*de**(-0.5)*np.sum(integ*wqp)
        # RHS piece: (3/2)(de)^{-3/4-1.5 s} int_{t1}^{t2} v(1/t) sqrt(log(de t)) t^{-1/4-1.5s} dt/t
        t1 = max(1.0, Xmin**(2/3)/de)
        t2 = min(2.0, d/e, Xmax**(2/3)/de)
        if t2 <= t1: continue
        ltp = np.linspace(log(t1), log(t2), K+1)
        tmp = np.exp(0.5*(ltp[:-1]+ltp[1:])); wtp = np.diff(ltp)
        integ2 = v(1.0/tmp)*np.sqrt(np.log(de*tmp))*tmp**(-0.25-1.5*s)
        rhs += mu[d]*eta[e]*(1.5)*de**(-0.75-1.5*s)*np.sum(integ2*wtp)
print("pairs:", pairs)
print("LHS (X-var):", lhs)
print("RHS (t-var):", rhs)
print("absdiff:", abs(lhs-rhs))

# Assembly check: does sum over pairs of the X-restricted term reproduce V*(X) pointwise?
for X in [500.0, 5000.0, 15000.0]:
    X23 = X**(2/3)
    tot = 0.0
    for e in range(1, int(X23)+1):
        if eta[e] == 0: continue
        for d in range(e+1, int(X23/e)+1):
            if mu[d] == 0: continue
            de = d*e
            if de**1.5 <= X < min(d**3, (2*de)**1.5):
                tot += mu[d]*eta[e]*de**(-0.5)*v(de*X**(-2/3))
    direct = Vstar_vec(np.array([X]))[0]
    assembled = tot*sqrt((2/3)*log(X))/X**(1/6)
    print(f"X={X}: V*direct={direct:+.8f} assembled={assembled:+.8f} diff={direct-assembled:+.1e}")

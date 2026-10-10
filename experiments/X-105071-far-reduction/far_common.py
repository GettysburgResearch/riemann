import numpy as np
from math import log, sqrt, pi, comb
ln2 = log(2.0); GAMMA1 = 14.134725141734695
def sieves(NMAX):
    mu = np.ones(NMAX+1, dtype=np.int8); is_c = np.zeros(NMAX+1, dtype=bool); primes = []
    for p in range(2, NMAX+1):
        if not is_c[p]:
            primes.append(p); mu[p::p] *= -1
            for q in range(p*p, NMAX+1, p*p): mu[q] = 0
            for q in range(p*p, NMAX+1, p): is_c[q] = True
    eta = np.zeros(NMAX+1); eta[1] = 1.0
    for p in primes:
        newe = eta.copy(); pk = p; k = 1
        while pk <= NMAX:
            c = comb(2*k, k)/4.0**k
            idx = np.arange(1, NMAX//pk + 1); idx = idx[idx % p != 0]
            newe[idx*pk] += c*eta[idx]
            pk *= p; k += 1
        eta = newe
    return mu, eta
def build_fields(Xmin, Xc, M, mu, eta, corners):
    """corners: list of (r1, r2) half-open (r1, r2]; r2 may be np.inf.
       Returns xg, VA (all pairs, d>X^{1/3}), VC (corner-restricted)."""
    EM = int(Xc**(2/3))+2
    ee = np.arange(0, EM+1, dtype=float); ee[0] = 1
    w0 = np.where(np.arange(EM+1) >= 1, eta[:EM+1]*ee**-0.5, 0.0)
    P0 = np.cumsum(w0); P1 = np.cumsum(w0*np.log(ee))
    xg = np.linspace(log(Xmin), log(Xc), M, endpoint=False)
    VA = np.zeros(M); VC = np.zeros(M)
    dfull = np.arange(0, EM+1); okmu = mu[dfull] != 0
    for i, x in enumerate(xg):
        X = np.exp(x); X23 = X**(2/3)
        dlo, dhi = int(np.floor(X**(1/3)))+1, int(X23)
        sel = dfull[dlo:dhi+1][okmu[dlo:dhi+1]]
        if len(sel) == 0: continue
        d = sel.astype(np.float64)
        cw = mu[sel]*d**-0.5; lnd = np.log(d)
        eh = np.floor(X23/d).astype(np.int64); el = np.floor(X23/(2*d)).astype(np.int64)
        np.clip(eh, 0, EM, out=eh); np.clip(el, 0, EM, out=el)
        alpha = 1.0 + (lnd - (2/3)*x)/ln2
        VA[i] = np.sum(cw*(alpha*(P0[eh]-P0[el]) + (P1[eh]-P1[el])/ln2))
        tot = 0.0
        for (r1, r2) in corners:
            ehi = np.minimum(eh, np.ceil(d/r1).astype(np.int64)-1)      # r > r1: e <= ceil(d/r1)-1
            if np.isinf(r2): elo = el.copy()
            else: elo = np.maximum(el, np.ceil(d/r2).astype(np.int64)-1) # r <= r2: e >= ceil(d/r2)
            g = ehi > elo
            if g.any():
                tot += np.sum((cw*(alpha*(P0[ehi]-P0[elo]) + (P1[ehi]-P1[elo])/ln2))[g])
        VC[i] = tot
        wgt = sqrt((2/3)*x)/np.exp(x/6.0)
        VA[i] *= wgt; VC[i] *= wgt
    return xg, VA, VC
def band_mass(F, freq, a, b):
    m = (freq >= a) & (freq <= b)
    return np.sum(np.abs(F[m])**2)*(freq[1]-freq[0])

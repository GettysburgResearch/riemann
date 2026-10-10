import numpy as np
from math import log, sqrt, pi
exec(open('sieve_common.py').read())

Xmin, Xc = 64.0, 2.0e4
# prefix sums for fast V*: P0(m)=sum_{e<=m} eta e^{-1/2}, P1 with ln e
EM = int(Xc**(2/3))+2
ee = np.arange(0, EM+1, dtype=float); ee[0] = 1
P0 = np.cumsum(np.where(np.arange(EM+1) >= 1, eta[:EM+1]*ee**-0.5, 0.0))
P1 = np.cumsum(np.where(np.arange(EM+1) >= 1, eta[:EM+1]*ee**-0.5*np.log(ee), 0.0))
sqd_cache = {}
def Vstar_fast(X):
    X23 = X**(2/3)
    dlo, dhi = int(np.floor(X**(1/3)))+1, int(X23)
    key = (dlo, dhi)
    if key not in sqd_cache:
        d = np.arange(dlo, dhi+1); msk = mu[d] != 0
        sqd_cache.clear(); sqd_cache[key] = (d[msk], mu[d[msk]]*d[msk]**-0.5, np.log(d[msk]))
    d, cw, lnd = sqd_cache[key]
    eh = np.floor(X23/d).astype(np.int64); el = np.floor(X23/(2*d)).astype(np.int64)
    alpha = 1.0 + (lnd - (2/3)*log(X))/ln2
    tot = np.sum(cw*(alpha*(P0[eh]-P0[el]) + (P1[eh]-P1[el])/ln2))
    return tot*sqrt((2/3)*log(X))/X**(1/6)

# x-side sampling
M = 2**20
xg = np.linspace(log(Xmin), log(Xc), M, endpoint=False)
dx = xg[1]-xg[0]
Vg = np.array([Vstar_fast(np.exp(x)) for x in xg])
print("V* sampled, M =", M, " V* rms:", sqrt(np.mean(Vg**2)))

for h in (0.02, 0.01):
    ph = Vg*np.exp(-h*xg)
    J = np.sum(ph**2)*dx
    # FFT: hat(psi)(t) = int psi(x) e^{-itx} dx ; pad to 2^24
    NP = 2**24
    F = np.fft.fft(ph, NP)*dx
    freq = np.fft.fftfreq(NP, d=dx)*2*pi   # e^{-2pi i k n/N}: t = 2pi*freq
    Jp = np.sum(np.abs(F)**2)*(freq[1]-freq[0])/(2*pi)
    print(f"h={h}: J(h) x-side = {J:.6f}   (1/2pi)int|G|^2 dt (FFT band) = {Jp:.6f}  ratio {Jp/J:.6f}")
    # spot-check G at a few t via pair formula (independent path)
    def G_pair(s):
        tot = 0.0+0.0j
        demax = Xc**(2/3)
        for e in range(1, int(demax)+1):
            if eta[e] == 0: continue
            for d in range(e+1, int(demax/e)+1):
                if mu[d] == 0: continue
                de = d*e
                Xlo = max(Xmin, de**1.5); Xhi = min(Xc, d**3, (2*de)**1.5)
                if Xhi <= Xlo: continue
                t1 = max(1.0, Xmin**(2/3)/de); t2 = min(2.0, d/e, Xc**(2/3)/de)
                K = 64
                lt = np.linspace(log(t1), log(t2), K+1)
                tm = np.exp(0.5*(lt[:-1]+lt[1:])); wt = np.diff(lt)
                ig = v(1.0/tm)*np.sqrt(np.log(de*tm))*tm**(-0.25-1.5*s)
                tot += mu[d]*eta[e]*1.5*de**(-0.75-1.5*s)*np.sum(ig*wt)
        return tot
    for tt in (1.7, 4.7116, 9.3):
        s = h+1j*tt
        gp = G_pair(s)
        # interpolate FFT value at t=tt
        k = np.argmin(np.abs(freq-tt))
        print(f"  t={tt}: G_pair={gp:.6f}  G_fft(t={freq[k]:.4f})={F[k]:.6f}")
    # window scan around gamma1/3
    g13 = 14.134725141734695/3
    for (a,b,lab) in ((g13-0.5,g13+0.5,'win g1/3 +-0.5'), (g13-0.15,g13+0.15,'win +-0.15'),
                      (2.0,3.0,'ctrl [2,3]'), (7.0,8.0,'ctrl [7,8]')):
        msk = (freq>=a)&(freq<=b)
        m2 = np.sum(np.abs(F[msk])**2)*(freq[1]-freq[0])
        print(f"  {lab}: int|G|^2 dt = {m2:.5f}")
np.save('Vg.npy', Vg); np.save('xg.npy', xg)

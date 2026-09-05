import numpy as np
from math import log, sqrt, pi
exec(open('sieve_common.py').read())
# 1) kernel closed form k(beta) = int_1^2 v(1/t) t^{-beta-1} dt =? 1/beta - (1-2^{-beta})/(beta^2 ln2)
for beta in (0.5, 0.5+7.067j, 2.0-3.0j):
    K = 200000
    lt = np.linspace(0, log(2), K+1); tm = np.exp(0.5*(lt[:-1]+lt[1:])); wt = np.diff(lt)
    num = np.sum(v(1.0/tm)*tm**(-beta)*wt)
    cf = 1/beta - (1-2.0**(-beta))/(beta**2*ln2)
    print(f"beta={beta}: quad={num:.10f} closed={cf:.10f} |diff|={abs(num-cf):.2e}")
print("k(1/2) =", 2 - (1-2**-0.5)/(0.25*ln2))
z0 = 0.25 - 1j*14.134725141734695/2
print("|z*| =", abs(z0), " |k(1/2)/z*| =", abs((2-(1-2**-0.5)/(0.25*ln2))/z0))
# 2) corner-part of V*: pairs with d/e in (1,1.25] or [1.75,2) vs all (d>e)
Xmin, Xc = 64.0, 2.0e4
xg = np.load('xg.npy'); dx = xg[1]-xg[0]
def Vstar_split(X):
    X23 = X**(2/3)
    tot_all = 0.0; tot_cor = 0.0
    dlo = int(np.floor(X**(1/3)))+1
    for d in range(dlo, int(X23)+1):
        if mu[d] == 0: continue
        el, eh = int(np.floor(X23/(2*d))), int(np.floor(X23/d))
        if eh <= el: continue
        e = np.arange(el+1, eh+1)
        y = d*e/X23
        s0 = eta[e]*e**-0.5*v(y)
        r = d/e
        cor = (r > 1) & ((r <= 1.25) | (r >= 1.75))
        tot_all += mu[d]*d**-0.5*np.sum(s0)
        tot_cor += mu[d]*d**-0.5*np.sum(s0[cor])
    w = sqrt((2/3)*log(X))/X**(1/6)
    return tot_all*w, tot_cor*w
sub = xg[::64]  # 16384 sample points
VA = np.zeros(len(sub)); VC = np.zeros(len(sub))
for i, x in enumerate(sub):
    VA[i], VC[i] = Vstar_split(np.exp(x))
print("rms V* (all):", sqrt(np.mean(VA**2)), " rms corner part:", sqrt(np.mean(VC**2)),
      " ratio:", np.mean(VC**2)/np.mean(VA**2))
# window content of corner part
for h in (0.01,):
    dxs = sub[1]-sub[0]
    for nm, vv in (("all", VA), ("corner", VC)):
        ph = vv*np.exp(-h*sub); F = np.fft.fft(ph, 2**20)*dxs
        fr = np.fft.fftfreq(2**20, d=dxs)*2*pi
        g13 = 14.134725141734695/3
        wm = np.sum(np.abs(F[(np.abs(fr-g13) <= 0.15)])**2)*(fr[1]-fr[0])
        cm = np.sum(np.abs(F[(fr >= 7) & (fr <= 8)])**2)*(fr[1]-fr[0])
        print(f"  {nm}: win(+-0.15)={wm:.5f} ctrl[7,8]={cm:.5f}")

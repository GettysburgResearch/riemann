# far_num2: direct test of (FAR-WIN). Build unweighted field psi0(x), frequency-localize
# at gamma_1/3 (smooth bump, half-width r0), fit the pinch amplitude c~ x^{-1/2} e^{i g13 x},
# measure residual weighted mass ratio  ratio(h) = int x|a_res|^2 e^{-2hx} / int x|a_pinch|^2 e^{-2hx}.
# (FAR-WIN) with eps_1 < 1 needs limiting ratio < 1/(3 pi) = 0.1061. Also: corner field share.
import numpy as np, json, sys, time
from math import log, sqrt, pi
sys.path.insert(0, __file__.rsplit('/',1)[0])
from far_common import *
t0 = time.time()
Xmin, Xc, M = 64.0, 2.0e5, 2**18
mu, eta = sieves(int(Xc**(2/3))+2)
cornersB = [(1.0,1.25),(1.75,np.inf)]
xg, VA, VCB = build_fields(Xmin, Xc, M, mu, eta, cornersB)
wg = np.sqrt((2/3)*xg)
psi0 = VA/wg; psi0c = VCB/wg          # unweighted fields
dx = xg[1]-xg[0]; NP = 2**22
g13 = GAMMA1/3.0; cB = 0.0478289351609; cBs = cB/sqrt(pi)
def project(field, r0):
    F = np.fft.fft(field, NP)*dx
    fr = np.fft.fftfreq(NP, d=dx)*2*pi
    u = (fr - g13)/r0
    w = np.where(np.abs(u) < 1, np.exp(1.0 - 1.0/np.maximum(1e-12, 1.0-u**2)), 0.0)
    a = np.fft.ifft(F*w)[:M]/dx      # complex amplitude on xg
    return a
out = {"Xc": Xc, "targets": {"ratio_max_for_eps1_lt_1": 1/(3*pi), "|cB|/sqrt(pi)": cBs}}
rows = []
for r0 in (0.15, 0.30, 0.50):
    a = project(psi0, r0); ac = project(psi0c, r0)
    xa, xb = 5.0, 11.5
    m = (xg >= xa) & (xg <= xb)
    ph = np.exp(1j*g13*xg[m]); env = xg[m]**-0.5
    # least-squares fit of complex c~ : a ~ c~ * env * ph
    num = np.sum(a[m]*np.conj(env*ph)); den = np.sum(env**2)
    ct = num/den
    apin = ct*env*ph
    ares = a[m]-apin
    row = {"r0": r0, "|c_fit|": abs(ct), "pred": cBs, "fit/pred": abs(ct)/cBs}
    for h in (0.04, 0.02, 0.01, 0.0):
        wgt = xg[m]*np.exp(-2*h*xg[m])
        num_r = np.sum(np.abs(ares)**2*wgt); den_r = np.sum(np.abs(apin)**2*wgt)
        numc = np.sum(np.abs(ac[m])**2*wgt)
        row[f"ratio_h{h}"] = float(num_r/den_r); row[f"corner_share_h{h}"] = float(numc/den_r)
    rows.append(row)
    print(f"r0={r0}: |c_fit|={abs(ct):.5f} (pred {cBs:.5f}, ratio {abs(ct)/cBs:.3f}); "
          f"res/pinch ratio h=0.02: {row['ratio_h0.02']:.4f}  h=0: {row['ratio_h0.0']:.4f}  "
          f"corner/pinch h=0.02: {row['corner_share_h0.02']:.4f}   [need < {1/(3*pi):.4f} for eps1<1]")
    print(f"   implied eps_1 (h=0.02) = {sqrt(row['ratio_h0.02']*3*pi):.3f}")
out["rows"] = rows
json.dump(out, open(__file__.rsplit('/',1)[0]+"/far_num2_out.json","w"), indent=1)
print(f"done {time.time()-t0:.1f}s")

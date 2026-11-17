#!/usr/bin/env python3
"""SKEPTIC: high-precision recheck of Lemma A (C1-L2). The float64 version in sk_li_theorem.py part (B) suffers
catastrophic cancellation in log|z| for gamma >~ 1e5 (reported ratio 3.51 is a float artifact). mpmath 60 digits."""
import json, mpmath as mp, numpy as np
mp.mp.dps = 60
worst = 0; worstphi = 0; worstlo = 1
for b in np.linspace(0.001, 0.999, 120):
    for g in list(np.linspace(14, 30, 40)) + list(np.geomspace(30, 1e9, 60)):
        b_ = mp.mpf(b); g_ = mp.mpf(g)
        if abs(b_ - mp.mpf(1)/2) < 1e-12: continue
        z = 1 - 1/mp.mpc(b_, g_); a = abs(mp.log(abs(z))); ph = abs(mp.arg(z))
        worst = max(worst, a/(abs(b_ - mp.mpf(1)/2)/(g_**2 - 1)))
        worstphi = max(worstphi, ph*g_)
        worstlo = min(worstlo, ph - (1/g_)*(1 - 1/(3*g_**2)))
out = {"max a/(|beta-1/2|/(gamma^2-1)) (<=1 required)": float(worst), "max phi*gamma (<=1.0013 claimed)": float(worstphi),
       "min phi - (1/gamma)(1-1/(3gamma^2)) (>=0 required)": float(worstlo)}
print(out)
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_lemmaA_mp.json", "w"), indent=1)

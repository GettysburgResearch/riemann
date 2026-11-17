"""SKEPTIC (C4): validate the explicit-formula normalisation used by both implementations
against the ZEROS side, for single Legendre test functions g = phi_j (even j) on [-L, L].
Zeros side: W(g) = 2 sum_{gamma>0} |h_g(gamma)|^2 (real even g), first 100000 Arb ordinates
plus smooth tail (2j+1)/(pi L) (log(G/2pi)+1)/G  (average of |h_j|^2 ~ (2j+1)/(L r^2)).
Arithmetic side: diagonal entry from sk_profile.assemble.  Non-rigorous (double precision zeros side).
"""
import sys, os, math, json
import numpy as np
from scipy.special import spherical_jn
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from sk_profile import assemble

ZD = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/data"
g = np.concatenate([np.loadtxt(os.path.join(ZD, f), usecols=1) for f in ("zeros_1_50000.tsv", "zeros_50001_100000.tsv")])
G = g[-1]
out = []
mp.mp.dps = 30
for L in (0.3, 0.6, 1.0):
    W = assemble(L, 3, 60)
    for idx, j in enumerate((0, 2, 4)):
        hj = math.sqrt((2 * j + 1) / (2 * L)) * L * 2 * spherical_jn(j, g * L)
        zs = 2 * np.sum(hj ** 2)
        tail = (2 * j + 1) / (math.pi * L) * (math.log(G / (2 * math.pi)) + 1) / G
        out.append({"L": L, "j": j, "arith": float(W[idx, idx]), "zeros_100000": float(zs), "tail": tail,
                    "zeros_plus_tail": float(zs + tail), "diff": float(W[idx, idx]) - float(zs + tail)})
        print(json.dumps(out[-1]), flush=True)
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic/sk_validate.json", "w"), indent=1)

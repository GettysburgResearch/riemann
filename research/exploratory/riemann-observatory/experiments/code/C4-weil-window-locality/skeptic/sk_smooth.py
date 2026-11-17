"""SKEPTIC (C4-0(d)): even-sector profile near the coincidence window L_c = (1/2)log(gamma_1/2pi) = 0.4053787,
n_even = 16 (N = 32 equivalent), independent implementation sk_profile.assemble; prints -ln lambda and
first/second differences on a uniform grid of step 0.01 plus L_c itself."""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
from sk_profile import assemble
mp.mp.dps = 40
Lc = 0.5 * math.log(14.134725141734693 / (2 * math.pi))
Ls = [0.37, 0.38, 0.39, 0.40, 0.41, 0.42, 0.43, 0.44]
rows = []
for L in Ls + [Lc]:
    lam = min(mp.eigsy(assemble(L, 16, 70), eigvals_only=True))
    rows.append({"L": L, "lam": float(lam), "mlog": float(-mp.log(lam))})
    print(rows[-1], flush=True)
g = [r["mlog"] for r in rows[:len(Ls)]]
d1 = [g[i + 1] - g[i] for i in range(len(g) - 1)]
d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
print("first diff", d1); print("second diff", d2)
json.dump({"L_c": Lc, "rows": rows, "d1": d1, "d2": d2}, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality/skeptic/sk_smooth.json", "w"), indent=1)

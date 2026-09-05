# far_num1: reproduce corner raw/window split independently; window-ratio scaling
# over 3+ window widths and 3 h values. Xc larger than lane P2's (2e5 vs 2e4).
import numpy as np, json, sys, time
from math import log, sqrt, pi
sys.path.insert(0, __file__.rsplit('/',1)[0])
from far_common import *
t0 = time.time()
Xmin, Xc, M = 64.0, 2.0e5, 2**18
NM = int(Xc**(2/3))+2
mu, eta = sieves(NM)
print(f"sieves to {NM} done {time.time()-t0:.1f}s; sum eta[:100]={eta[:100].sum():.6f}")
cornersA = [(1.0,1.25),(1.75,2.0)]        # doc variant: (1,1.25] U (1.75,2]
cornersB = [(1.0,1.25),(1.75,np.inf)]     # P2_num5 code variant: (1,1.25] U (1.75,inf)
xg, VA, VCA = build_fields(Xmin, Xc, M, mu, eta, cornersA)
_,  _,  VCB = build_fields(Xmin, Xc, M, mu, eta, cornersB)
print(f"fields built {time.time()-t0:.1f}s  rmsVA={sqrt(np.mean(VA**2)):.5f}")
res = {"Xc": Xc, "M": M}
res["raw_ratio_A"] = float(np.mean(VCA**2)/np.mean(VA**2))
res["raw_ratio_B"] = float(np.mean(VCB**2)/np.mean(VA**2))
print("RAW mean-square corner/all: docA(1,1.25]U(1.75,2] =", f"{res['raw_ratio_A']:.4f}",
      " codeB(1,1.25]U(1.75,inf) =", f"{res['raw_ratio_B']:.4f}", " [lane P2 quoted 0.77 for B-style]")
dx = xg[1]-xg[0]; NP = 2**22
g13 = GAMMA1/3.0
tab = []
for h in (0.04, 0.02, 0.01):
    row = {"h": h}
    for nm, vv in (("all", VA), ("cornerA", VCA), ("cornerB", VCB)):
        F = np.fft.fft(vv*np.exp(-h*xg), NP)*dx
        fr = np.fft.fftfreq(NP, d=dx)*2*pi
        for r0 in (0.05, 0.15, 0.30, 0.50):
            row[f"{nm}_win{r0}"] = band_mass(F, fr, g13-r0, g13+r0)
        row[f"{nm}_ctrl78"] = band_mass(F, fr, 7.0, 8.0)
        row[f"{nm}_line"] = float(np.sum(np.abs(F)**2)*(fr[1]-fr[0]))
    tab.append(row)
    for r0 in (0.05, 0.15, 0.30, 0.50):
        ra = row[f"cornerA_win{r0}"]/row[f"all_win{r0}"]; rb = row[f"cornerB_win{r0}"]/row[f"all_win{r0}"]
        print(f" h={h} r0={r0}: winmass all={row[f'all_win{r0}']:.5f} cornerB={row[f'cornerB_win{r0}']:.5f} ratioB={rb:.4f} ratioA={ra:.4f}")
    print(f" h={h} ctrl[7,8]: all={row['all_ctrl78']:.5f} cornerB={row['cornerB_ctrl78']:.5f}")
res["table"] = tab
json.dump(res, open(__file__.rsplit('/',1)[0]+"/far_num1_out.json","w"), indent=1)
print(f"done {time.time()-t0:.1f}s")

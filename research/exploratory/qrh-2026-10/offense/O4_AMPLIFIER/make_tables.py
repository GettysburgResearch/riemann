"""make_tables.py -- print the markdown tables of README.md section 5 from results/*.json (EMPIRICAL)."""
import glob
import json
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, "results")

amp = []
for f in ("amp_main.json", "amp_D8000.json"):
    p = os.path.join(R, f)
    if os.path.exists(p):
        amp += json.load(open(p))["results"]

print("| D | H/(DL) | ratio_b for L = 13, 31, 61, 127, 251, 499 (prime) | randphase range | enrichment (prime) | max principal share |")
print("|---|---|---|---|---|---|")
for D in sorted({x["D"] for x in amp}):
    for hf in sorted({x["Hfac"] for x in amp if x["D"] == D}):
        pr = sorted([x for x in amp if x["D"] == D and x["Hfac"] == hf and x["design"] == "prime"], key=lambda x: x["L"])
        rp = [x for x in amp if x["D"] == D and x["Hfac"] == hf and x["design"] == "randphase"]
        rb = ", ".join(f"{x['ratio_b']:.3f}" for x in pr)
        rr = f"{min(x['ratio_b'] for x in rp):.3f}-{max(x['ratio_b'] for x in rp):.3f}" if rp else "-"
        en = ", ".join(f"{x['enrich']:.0f}" for x in pr)
        ps = max(x["P_share"] for x in pr)
        print(f"| {D} | {hf:g} | {rb} (L = {', '.join(str(x['L']) for x in pr)}) | {rr} | {en} | {ps:.1e} |")

kap = []
for D in sorted({x["D"] for x in amp}):
    for hf in sorted({x["Hfac"] for x in amp if x["D"] == D}):
        pr = [x for x in amp if x["D"] == D and x["Hfac"] == hf and x["design"] == "prime"]
        if len(pr) >= 3:
            sl = np.polyfit(np.log([x["n_amp"] for x in pr]), np.log([x["ratio_b"] for x in pr]), 1)[0]
            kap.append((D, hf, sl))
allr = [x["ratio_b"] for x in amp]
print()
print(f"ratio_b range over all cells: {min(allr):.3f} - {max(allr):.3f} ({len(allr)} cells)")
print("kappa_emp (slope of log ratio_b vs log #primes): " +
      "; ".join(f"D={D},H={hf:g}DL: {s:+.4f}" for D, hf, s in kap))
print(f"max |kappa_emp| = {max(abs(s) for _, _, s in kap):.4f}")

print()
print("| D | theta | rows | M_amp/(pi(L) diag) | kappa_emp | lambda_max/diag | off rms | random scale | slope vs log N(ll') | principal share |")
print("|---|---|---|---|---|---|---|---|---|---|")
for f in sorted(glob.glob(os.path.join(R, "tm_theta*.json"))):
    for x in json.load(open(f))["results"]:
        print(f"| {x['D']} | {x['theta']:g} | {x['n_u']} | {x['M_amp_over_L_diag']:.4f} | {x['kappa_emp']:+.4f} | "
              f"{x['lambda_max_over_diag']:.3f} | {x['off_rms']:.4f} | {x['random_twist_scale']:.4f} | "
              f"{x['slope_logoff_vs_logNr']:+.3f} | {x['principal_share']:.1e} |")

#!/usr/bin/env python3
"""Re-optimise the Sep 30 Part II model (scripts/threshold_calculus.py, imported unchanged) with the Gram
loss dial theta: gram exponent max(0, theta_frac*b/6*... , 2b - ly') where the P_a^{1/6} term is scaled.
theta_scale = 1 is the paper (Prop. 15.2); 0 removes the P_a^{1/6} term (keeps P_a^2/Y').
Floating point, finite; Nelder-Mead from the paper geometry (single start to stay within CPU budget)."""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import threshold_calculus as TC

def make_low(theta_scale):
    def low_threshold(lx, ly, ell, inp=TC.PAPER, nd=201):
        M = lx + ly; b = ly - lx; h = 1 - lx + ell
        worst = -9.0
        for dd in (np.linspace(0, ell, nd) if ell > 0 else [0.0]):
            Mp, lp = M - 2*dd, ell - dd
            EB = TC.energy_exponent(Mp, lp, inp)
            gram = max(0.0, theta_scale*b/6, 2*b - (ly - dd))
            sep = (-(ly - dd) + gram + EB)/2
            worst = max(worst, sep - dd/2)
        return 1 - lx/2 - h/6 + worst
    return low_threshold

if __name__ == '__main__':
    out = {}
    for ts in [float(a) for a in sys.argv[1:]] or [1.0, 0.0]:
        TC.low_threshold = make_low(ts)
        r = TC.optimise(11/12, starts=[(17/48, 23/48, 1/6), (0.29, 0.58, 0.13)])
        out[str(ts)] = {k: (v if not isinstance(v, tuple) else list(v)) for k, v in r.items()}
        print(ts, r, flush=True)
    json.dump(out, open(os.path.join(os.path.dirname(__file__), '..', 'results', 'o3_theta_opt.json'), 'w'), indent=1, default=str)

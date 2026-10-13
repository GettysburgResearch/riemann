#!/usr/bin/env python3
"""O7: full Part II model (../../../scripts/threshold_calculus.py, imported UNCHANGED, monkeypatched in
memory only) with Gram dial (O3 convention), raised floor delta0 and floor saving theta_F.
Floating point, Nelder-Mead, finite grids: EMPIRICAL model values, not certificates.
usage: python3 full_model_floor.py gram(paper|zero) counts(paper|DH) delta0 thetaF [delta0 thetaF ...]"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import threshold_calculus as TC

_R_orig = TC.R_bin

def make_low(scale):
    def low_threshold(lx, ly, ell, inp=TC.PAPER, nd=201):
        M = lx + ly; b = ly - lx; h = 1 - lx + ell
        worst = -9.0
        for dd in (np.linspace(0, ell, nd) if ell > 0 else [0.0]):
            Mp, lp = M - 2*dd, ell - dd
            EB = TC.energy_exponent(Mp, lp, inp)
            gram = max(0.0, scale*b/6, 2*b - (ly - dd))
            sep = (-(ly - dd) + gram + EB)/2
            worst = max(worst, sep - dd/2)
        return 1 - lx/2 - h/6 + worst
    return low_threshold

def setup(gram, d0, thF):
    TC.DELTA0 = d0
    TC.low_threshold = make_low(1.0 if gram == 'paper' else 0.0)
    def R_bin(delta, x, d, kappa, ell, inp=TC.PAPER):
        if delta <= d0 + 1e-12:
            return 1.0 - thF
        return _R_orig(delta, x, d, kappa, ell, inp)
    TC.R_bin = R_bin

if __name__ == '__main__':
    gram, counts = sys.argv[1], sys.argv[2]
    vals = [float(eval(a)) for a in sys.argv[3:]]
    inp = TC.Inputs(counts=counts)
    out = {}
    for d0, thF in zip(vals[::2], vals[1::2]):
        setup(gram, d0, thF)
        r = TC.optimise(11/12, inp, starts=[(17/48, 23/48, 1/6), (0.29, 0.58, 0.13), (0.27, 0.54, 0.19)])
        key = f"gram={gram},counts={counts},delta0={d0:.5f},thetaF={thF:.5f}"
        out[key] = {k: (list(v) if isinstance(v, tuple) else float(v)) for k, v in r.items()}
        print(key, out[key], flush=True)
    fn = os.path.join(os.path.dirname(__file__), '..', 'results', f"full_{gram}_{counts}.json")
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    json.dump(out, open(fn, 'w'), indent=1, default=str)

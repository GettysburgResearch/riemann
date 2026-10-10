#!/usr/bin/env python3
"""Run one named scenario of the threshold calculus and write results/<name>.json.
Usage: python3 sensitivity.py <scenario>   (see SCENARIOS)"""
import json, sys, time, os
from threshold_calculus import Inputs, optimise

SCENARIOS = {
    'A_paper_bp11_12':      (11/12, Inputs()),
    'B_paper_bp7_8':        (7/8,   Inputs()),
    'C_extrap_kappa_bp7_8': (7/8,   Inputs(kappa_floor=None)),
    'D_DHcounts':           (11/12, Inputs(counts='DH')),
    'E_optimal_energy':     (11/12, Inputs(energy='optimal')),
    'F_DH_and_optimal':     (11/12, Inputs(counts='DH', energy='optimal')),
    'G_trivial_counts':     (11/12, Inputs(counts='trivial')),
    'S1_plaincap4':         (11/12, Inputs(plain_cap=4.0)),
    'S2_invcap1':           (11/12, Inputs(inv_cap=1.0)),
    'S3_alpha3_4':          (11/12, Inputs(alpha=0.75)),
    'S4_tmax2':             (11/12, Inputs(tmax=2.0)),
    'S5_z0_033':            (11/12, Inputs(z0=0.33)),
    'S6_dsel0':             (11/12, Inputs(d_sel=0.05)),
}

if __name__ == '__main__':
    name = sys.argv[1]
    bp, inp = SCENARIOS[name]
    t0 = time.time()
    res = optimise(bp, inp)
    res = {k: (float(v) if isinstance(v, (int, float)) else str(v)) for k, v in res.items()}
    res.update(scenario=name, beta_prev=bp, seconds=round(time.time() - t0, 1), inputs=vars(inp))
    out = os.path.join(os.path.dirname(__file__), '..', 'results', name + '.json')
    json.dump(res, open(out, 'w'), indent=1)
    print(name, json.dumps(res), flush=True)

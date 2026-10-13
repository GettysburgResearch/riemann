#!/usr/bin/env python3
"""Tables and fits for O3b (EMPIRICAL, floating point, finite).  Reads ../results/na_Q*.json, kub_Q*.json."""
import json, glob, math, os, sys
import numpy as np
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'results')
def fit(xs, ys):
    xs = np.log(np.array(xs, float)); ys = np.log(np.array(ys, float))
    A = np.vstack([xs, np.ones_like(xs)]).T
    c, res, *_ = np.linalg.lstsq(A, ys, rcond=None)
    n = len(xs)
    if n > 2:
        s2 = ((ys - A @ c) ** 2).sum() / (n - 2)
        se = math.sqrt(s2 / ((xs - xs.mean()) ** 2).sum())
    else: se = float('nan')
    return c[0], se
out = {}
print('## Annulus grid (OP-G / OP-A)\n')
print('| Q | P_a | Y\' | #s | Gram excess | n_exc (MP rule) | R_full | base_c (mean) | base_m (mean) | R_Bu | R_mu->1 | R(mu->+-1) | R_noxi | diag (xi) | P_a^{-1/12} |')
print('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
grid = {}
for f in sorted(glob.glob(os.path.join(R, 'na_Q*.json')), key=lambda p: int(p.split('na_Q')[1].split('.')[0])):
    d = json.load(open(f)); Q = d['Q']
    for r in d['recs']:
        grid.setdefault(Q, []).append(r)
        print(f"| {Q} | {r['P_a']} | {r['Yp']} | {r['ns']} | {r['excess']:+.3f} | {r['nexc']} | {r['R_full']:.4f} | {r['base_cphase_full'][0]:.4f} | {r['base_mphase_full'][0]:.4f} | {r['R_Bu_full']:.4f} | {r['R_mu1_full']:.4f} | {r['ctrl_mu_pm1_full'][0]:.4f} | {r['R_noxi_full']:.4f} | {abs(complex(*r['diag_xi_full'])):.1e} | {r['P_a']**(-1/12):.3f} |")
print('\nFits of log R against log P_a at fixed Q (slope +- s.e.):\n')
for Q, rs in grid.items():
    P = [r['P_a'] for r in rs]
    s1 = fit(P, [r['R_full'] for r in rs]); s2 = fit(P, [r['base_cphase_full'][0] for r in rs]); s3 = fit(P, [r['base_mphase_full'][0] for r in rs])
    print(f"* Q = {Q}: R_full slope {s1[0]:+.2f} +- {s1[1]:.2f}; base_c slope {s2[0]:+.2f} +- {s2[1]:.2f}; base_m slope {s3[0]:+.2f} +- {s3[1]:.2f}")
    out[f'fitP_Q{Q}'] = dict(R_full=s1, base_c=s2, base_m=s3)
print('\nFits of log R against log Q at fixed P_a:\n')
for P in [1, 4, 16, 64, 256, 1024]:
    Qs = [Q for Q in grid]; rr = [next(r for r in grid[Q] if r['P_a'] == P) for Q in Qs]
    s1 = fit(Qs, [r['R_full'] for r in rr]); s2 = fit(Qs, [r['base_cphase_full'][0] for r in rr]); s3 = fit(Qs, [r['base_mphase_full'][0] for r in rr])
    print(f"* P_a = {P}: R_full slope {s1[0]:+.2f} +- {s1[1]:.2f}; base_c {s2[0]:+.2f} +- {s2[1]:.2f}; base_m {s3[0]:+.2f} +- {s3[1]:.2f}")
    out[f'fitQ_P{P}'] = dict(R_full=s1, base_c=s2, base_m=s3)
# ratios R_full / base_c
rat = [r['R_full'] / r['base_cphase_full'][0] for Q in grid for r in grid[Q]]
print(f"\nR_full / base_c over all {len(rat)} grid points: median {np.median(rat):.2f}, range [{min(rat):.2f}, {max(rat):.2f}]")
print(f"R_full / base_c 90th pct: fraction of points with R_full above the base_c 90th percentile: "
      f"{np.mean([r['R_full'] > r['base_cphase_full'][1] for Q in grid for r in grid[Q]]):.2f}")
# ---- Kubota cumulative
print('\n## Kubota-residue test (OP-K)\n')
kub = {}
for f in sorted(glob.glob(os.path.join(R, 'kub_Q*.json'))):
    if 'test' in f: continue
    d = json.load(open(f)); kub[d['Q']] = d
for Q in sorted(kub):
    d = kub[Q]; nB = d['normB']
    print(f"\n### Q = {Q}, Z = {d['Z']}, #m = {d['nM']}\n")
    print('| Y | #s | P_a=Y^2/Q | G/G_diag - 1 | G_rand/G_diag - 1 | SNR T/RW (theta) | R_exc est (theta) | (mu->1) | (mu->+-1) | (theta->rand phase) | (m-phase) | noise floor |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for r in d['recs']:
        ex = r['gram'] - r['gram_diag']
        if ex <= 0:
            continue
        Rk = [r['T'][i] / (math.sqrt(ex) * nB[i]) for i in range(5)]
        fl = r['RW'][0] / (math.sqrt(ex) * nB[0])
        print(f"| {r['Y']} | {r['ns']} | {r['Y']**2/Q:.3g} | {r['gram']/r['gram_diag']-1:+.3f} | {r['gram_randcol']/r['gram_diag']-1:+.3f} | {r['T'][0]/r['RW'][0]:.2f} | {Rk[0]:.4f} | {Rk[1]:.4f} | {Rk[2]:.4f} | {Rk[3]:.4f} | {Rk[4]:.4f} | {fl:.4f} |")
    # exponent of Gram excess vs P_a over upper half of the Y range
    rs = [r for r in d['recs'] if r['gram'] > 1.02 * r['gram_diag']]
    if len(rs) >= 3:
        s = fit([r['Y'] ** 2 / Q for r in rs], [r['gram'] / r['gram_diag'] - 1 for r in rs])
        print(f"\nGram excess fit: (G/G_diag - 1) ~ P_a^{{{s[0]:.3f} +- {s[1]:.3f}}} over {len(rs)} checkpoints (prediction from [S30] Prop 15.2: 1/6 = 0.167)")
        out[f'gram_excess_Q{Q}'] = s
json.dump(out, open(os.path.join(R, 'fits.json'), 'w'), indent=1)

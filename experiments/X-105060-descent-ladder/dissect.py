"""Reproduce and dissect the flagged random trials with high-precision mpmath roots."""
import numpy as np, mpmath as mp
from stress_tests import build_poly, classify_roots, gaps_meeting_window, gap_weight, \
    window_counts, analyze_rung, EPS

mp.mp.dps = 40

def gen_trial(seed, upto):
    rng = np.random.default_rng(seed)
    keep = None
    for trial in range(upto+1):
        nreal = rng.integers(6, 11)
        reals = np.sort(rng.uniform(0, 10, nreal))
        for i in range(1, len(reals)):
            reals[i] = max(reals[i], reals[i-1] + 0.05)
        reals = [-1.0] + list(reals) + [reals[-1] + 1.0]
        npair = rng.integers(1, 4)
        pairs = [(float(rng.uniform(reals[1], reals[-2])),
                  float(rng.uniform(0.05, 0.5)), 1) for _ in range(npair)]
        keep = (reals, pairs)
    return keep

def mp_roots(coef):
    return mp.polyroots([mp.mpf(c) for c in coef], maxsteps=200, extraprec=120)

def dissect(trial_id, seed=7):
    reals, pairs = gen_trial(seed, trial_id)
    print(f"--- trial {trial_id}")
    print("reals:", [round(r,4) for r in reals])
    print("pairs:", [(round(x,4), round(y,4)) for (x,y,m) in pairs])
    coef = build_poly(reals, pairs)
    d1 = np.polyder(coef)
    # numpy classification (what stress_tests used)
    r_np, p_np = classify_roots(d1)
    # mpmath classification (40 dps)
    rts = mp_roots(list(d1))
    r_mp, p_mp = [], []
    for z in rts:
        if abs(mp.im(z)) < mp.mpf('1e-25'):
            r_mp.append(float(mp.re(z)))
        elif mp.im(z) > 0:
            p_mp.append((float(mp.re(z)), float(mp.im(z))))
    r_mp.sort()
    print("F' roots numpy: reals:", [round(r,5) for (r,m) in r_np for _ in range(m)])
    print("               pairs:", [(round(x,5), round(y,6)) for (x,y,m) in p_np])
    print("F' roots mpmath: reals:", [round(r,5) for r in r_mp])
    print("                pairs:", [(round(x,5), round(y,6)) for (x,y) in p_mp])
    # per-gap audit with mpmath roots
    aw, bw = reals[1] + 0.01, reals[-2] - 0.01
    reals_g = [(r,1) for r in reals]
    gaps = gaps_meeting_window(reals_g, aw, bw)
    for gp in gaps:
        a, b = gp
        n1 = sum(1 for r in r_mp if a + 1e-12 < r < b - 1e-12)
        w, over = gap_weight(gp, pairs)
        if n1 != 1 or w > 0:
            print(f"  gap ({a:.4f},{b:.4f}) g={b-a:.4f}: n'={n1} extra={n1-1} weight={w:.4f} over={len(over)}")
    print()

for t in [146, 186]:
    dissect(t)

# find which trials had threshold violations: re-run search recording ids
from stress_tests import random_search

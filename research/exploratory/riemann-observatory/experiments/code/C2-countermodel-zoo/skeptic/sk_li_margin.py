"""SKEPTIC: smallest positive value of lambda_n(xi~) just before the first negative n (robustness of sk_li.py)."""
import sys, json, numpy as np
sys.argv = [sys.argv[0], sys.argv[1], sys.argv[2] + '/zeros_1_50000.tsv', sys.argv[2] + '/zeros_50001_100000.tsv']
import sk_li
out = {}
for beta, gam, n0, n1 in [(0.6, 14.0, 20500, 20854), (0.75, 14.0, 7100, 7476), (0.6, 30.0, 111500, 112537), (0.75, 30.0, 40400, 40907)]:
    ns = np.arange(n0, n1 + 1)
    lx, _ = sk_li.lam_xi(ns)
    q = np.array([sk_li.lam_Q(int(n), beta, gam) for n in ns])
    tot = lx + q
    i = int(np.argmin(tot))
    out[f'{beta},{gam}'] = dict(window=[n0, n1], min_value=float(tot[i]), at_n=int(ns[i]), all_positive=bool(np.all(tot > 0)))
    print(out[f'{beta},{gam}'], flush=True)
json.dump(out, open(sys.argv[1] + '/sk_li_margin.json', 'w'), indent=1)

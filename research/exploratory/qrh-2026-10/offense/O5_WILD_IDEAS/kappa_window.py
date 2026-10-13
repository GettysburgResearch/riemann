"""kappa_window.py -- EMPIRICAL (binary64, finite; proves nothing): the kappa-law quantity on a single
dyadic row window D^(1-eta)/2 < N u <= D^(1-eta) for the true sextic Moebius family (nu = 1, W of
moments/common.py), against iid random +-1 signs on the same columns.  Reports
  kappa_hat = (log(M_window/Diag_window)) / (eta log D)   (kappa = 1 would be the positivity loss,
  kappa = 0 is diagonal size), where Diag_window = #rows * sum_n w_n^2 (naive, ignores coprimality).
Run: python3 -I kappa_window.py   (single thread; ~1-3 min)
"""
import math, os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, "..", "..", "moments")))
import numpy as np
import eisenstein as E
import common as C

lib = C.load_kernel()
rng = np.random.default_rng(2026)
out = []
for D in (2000.0, 8000.0, 32000.0):
    prs = E.prime_ideals(int(2 * D) + 10)
    pd = C.PrimeData(prs)
    ns, facs, norms, w = C.family(prs, D)
    trees = {"mu": C.Tree(facs, w)}
    for s in range(3):
        trees[f"rand{s}"] = C.Tree(facs, np.abs(w) * rng.choice([-1.0, 1.0], size=len(w)))
    for eta in (0.1, 0.2, 0.3, 0.5):
        Hhi = D ** (1 - eta)
        bm = int(2 * math.sqrt(Hhi / 3)) + 2
        segs, (a, b, N) = C.lattice_segments(Hhi, bmin=-bm)
        keep = N > Hhi / 2
        rows = int(keep.sum())
        diag = rows * float(np.sum(w ** 2))
        rec = {"D": D, "eta": eta, "rows": rows, "cols": int(len(w))}
        for name, tr in trees.items():
            A = C.eval_rows(lib, pd, tr, segs, workers=1)
            M = float(np.sum(np.abs(A[keep]) ** 2))
            rec[name] = round(M / diag, 4)
        rec["kappa_hat_mu"] = round(math.log(rec["mu"]) / (eta * math.log(D)), 4)
        out.append(rec)
        print(rec, flush=True)
json.dump(out, open(os.path.join(HERE, "kappa_window.json"), "w"), indent=1)

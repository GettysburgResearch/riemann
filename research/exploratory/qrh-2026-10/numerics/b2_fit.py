"""
b2_fit.py -- least-squares log-log slopes for the B2 ladder (EMPIRICAL; a finite fit is not a
theorem).  Usage: python3 -I b2_fit.py results/b2_ladder_d0.json [results/b2_ladder_dl.json ...]
"""
import json
import sys

import numpy as np


def slope(x, y):
    x, y = np.log(np.asarray(x, float)), np.log(np.asarray(y, float))
    A = np.vstack([x, np.ones_like(x)]).T
    (k, c), *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(k)


def main():
    out = {}
    for fn in sys.argv[1:]:
        d = json.load(open(fn))
        R = d["rungs"]
        Z = [r["Z"] for r in R]
        rows = [r["rows"] for r in R]
        res = dict(Z=Z, rows=rows, slope_rows=slope(Z, rows))
        for lb in ("true", "rand_c1", "rand_c2", "rand_cuberoot"):
            for la in ("true", "rand0", "rand1"):
                try:
                    v = [r["cells"][lb][la]["S_over_CS_rms"] for r in R]
                    u = [r["cells"][lb][la]["S_over_U_rms"] for r in R]
                    ls = [r["cells"][lb][la]["Ls_over_Ds"] for r in R]
                    le = [r["cells"][lb][la]["Ls_over_lamb2"] for r in R]
                except KeyError:
                    continue
                res[f"{lb}|{la}"] = dict(S_over_CS=v, slope_S_over_CS=slope(Z, v),
                                         S_over_U=u, Ls_over_Ds=ls, Ls_over_lamb2=le,
                                         slope_Ls_over_lamb2=slope(Z, le))
        res["random_prediction_slope"] = -0.5 * res["slope_rows"]
        out[fn] = res
        print(fn, "rows slope", round(res["slope_rows"], 3),
              "random-phase prediction for S/CS slope", round(-0.5 * res["slope_rows"], 3))
        for k, v in res.items():
            if isinstance(v, dict):
                print(f"  {k:24s} slope(S/CS)={v['slope_S_over_CS']:+.3f}  S/CS=" +
                      " ".join(f"{x:.3g}" for x in v["S_over_CS"]) + "  S/U=" +
                      " ".join(f"{x:.2f}" for x in v["S_over_U"]) + "  Ls/Ds=" +
                      " ".join(f"{x:.2f}" for x in v["Ls_over_Ds"]))
    return out


if __name__ == "__main__":
    main()

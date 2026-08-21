#!/usr/bin/env python3
"""Task 1: per-fibre aggregate feasibility for all integer fibres at each cut,
plus boundary fibres; contrast with nested-license infeasibility counts."""
import numpy as np
from fast import sieve_mu_np, gamma_arrays, greedy_fast

def nested_deficit_fast(x, mu):
    n = int(np.floor(x))
    ks = np.nonzero(mu[1:n+1])[0] + 1
    T = (4*np.sqrt(x/ks) - 3)/np.sqrt(ks)
    H = np.cumsum(mu[ks]*T)
    od = mu[ks] == -1
    if not od.any(): return 0.0, None
    Hod = H[od]
    i = int(np.argmin(Hod))
    return float(max(0.0, -Hod[i])), int(ks[od][i])

CUTS = [89, 101, 149, 211, 401, 1009, 4001, 10007]

def main():
    N = 10007
    mu = sieve_mu_np(N)
    ga = gamma_arrays(N)
    eps = 1e-6
    print(f"{'C':>6} {'#fib':>5} {'nested-bad':>10} {'agg-bad':>7} "
          f"{'min m2 (x)':>18} {'min m3 (x)':>18} {'min m_sc (x)':>18} {'min TB (x)':>18}")
    for C in CUTS:
        xs = [float(x) for x in range(2, C)] + [C - eps]
        nbad = 0; abad = []
        mins = {k: (1e18, None) for k in ("m2", "m3", "m_sc", "TB")}
        for x in xs:
            d, t = nested_deficit_fast(x, mu)
            if d > 1e-9: nbad += 1
            r = greedy_fast(x, mu, ga)
            if not r.get("feasible", False):
                abad.append((x, r.get("why", "aggregate")))
            for k in mins:
                v = r.get(k)
                if v is not None and v < mins[k][0]:
                    mins[k] = (v, x)
        fmt = lambda k: f"{mins[k][0]:+.6f}@{mins[k][1]:.6g}"
        print(f"{C:>6} {len(xs):>5} {nbad:>10} {len(abad):>7} "
              f"{fmt('m2'):>18} {fmt('m3'):>18} {fmt('m_sc'):>18} {fmt('TB'):>18}")
        if abad:
            print("   FIRST aggregate failures:", abad[:5])
    print("\nBoundary-fibre margins:")
    for C in CUTS:
        x = C - eps
        r = greedy_fast(x, mu, ga)
        d, t = nested_deficit_fast(x, mu)
        print(f"C={C:>6}: x={x:.6f}  TB={r['TB']:+.6f}  m2={r['m2']:+.6f}  m3={r['m3']:+.6f}  "
              f"m_sc={r['m_sc']:+.6f}  G2={r['G2']:+.6f}  G3={r['G3']:+.6f}  "
              f"nested_deficit={d:.6f}@t={t}  feasible={r['feasible']}")

if __name__ == "__main__":
    main()

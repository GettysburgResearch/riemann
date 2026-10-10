"""
exact_diag1.py -- checks the density form of the diagonal used in make_tables.py.

For k = 1 the exact diagonal is sum_n W(Nn/D)^2 #{u : 0 < N u <= H, (u, n) = 1}
= sum_n W^2 sum_{d | n} mu(d) L0(H / Nd)  (inclusion-exclusion, exact lattice counts);
make_tables.py uses L0(H) * sum_n W^2 prod_{p|n} (1 - 1/Np).  This prints the ratio.

Usage: python3 -I exact_diag1.py results/moments.json [max_H]
"""
import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402

import common as C  # noqa: E402
import eisenstein as E  # noqa: E402


def main():
    mo = json.load(open(sys.argv[1]))
    maxH = float(sys.argv[2]) if len(sys.argv) > 2 else 2e7
    Ds = [r["D"] for r in mo["results"]]
    primes = E.prime_ideals(2 * max(Ds))
    xmax = maxH
    _, (_, _, N) = C.lattice_segments(xmax, bmin=-int(2 * (xmax / 3) ** 0.5) - 2)
    Ns = np.sort(N)

    def L0(x):
        return np.searchsorted(Ns, x, side="right")

    out = []
    for r in mo["results"]:
        D = r["D"]
        ns, facs, norms, w = C.family(primes, D)
        gN = np.array([np.prod([1 - 1 / primes[p].N for p in f]) for f in facs])
        for h in r["per_H"]:
            H = h["H"]
            if H > maxH:
                continue
            ex = 0.0
            for f, wt in zip(facs, w):
                tot = 0
                for m in range(len(f) + 1):
                    for sub in itertools.combinations(f, m):
                        Nd = int(np.prod([primes[p].N for p in sub])) if sub else 1
                        tot += (-1) ** m * int(L0(H / Nd))
                ex += wt * wt * tot
            dens = float(L0(H)) * float(np.sum(w ** 2 * gN))
            out.append((D, h["label"], ex / dens, h["M"]["1"] / ex))
            print(f"D={D} {h['label']}: exact/density = {ex/dens:.5f};  M2/exact_diag = {h['M']['1']/ex:.4f}",
                  flush=True)
    json.dump(out, open(os.path.join(os.path.dirname(sys.argv[1]), "exact_diag1.json"), "w"), indent=1)


if __name__ == "__main__":
    main()

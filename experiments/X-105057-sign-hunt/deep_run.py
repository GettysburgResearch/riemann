import json, math, time, numpy as np
import fast_O

out = {"rows": []}
# dense grid: 6 points/octave, X = 1e4 .. 1e9
Xs = []
x = 10**4
while x <= 10**9:
    Xs.append(int(x))
    x *= 2 ** (1/6)
Xs = sorted(set(Xs))
mu = fast_O.mobius_np(fast_O.UN_for(10**9)[1] + 10)
for X in Xs:
    U, N = fast_O.UN_for(X)
    h = fast_O.build_h(U, N, mu)
    O, D = fast_O.band_O_D(U, N, h)
    r = {"X": X, "U": U, "N": N, "O": O, "D": D, "H": D + O}
    out["rows"].append(r)
    print(json.dumps(r), flush=True)
with open("out_deep_dense.json", "w") as f:
    json.dump(out, f)

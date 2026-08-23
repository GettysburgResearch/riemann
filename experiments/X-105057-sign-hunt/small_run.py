import json, numpy as np
import fast_O
mu = fast_O.mobius_np(20000)
# complete census: every integer X in [30, 10000] (O depends on X via (U,N) only)
seen = {}
rows = []
for X in range(30, 10001):
    U, N = fast_O.UN_for(X)
    if N <= U + 1: continue
    if (U, N) in seen: continue
    seen[(U, N)] = X
    h = fast_O.build_h(U, N, mu)
    O, D = fast_O.band_O_D(U, N, h)
    rows.append({"X": X, "U": U, "N": N, "O": O, "D": D})
pos = [r for r in rows if r["O"] > 0]
print("distinct (U,N) configs:", len(rows), " with O>0:", len(pos))
Xpos = sorted(r["X"] for r in pos)
print("largest X with O>0:", max(Xpos) if Xpos else None)
print("first 40 O>0 X:", Xpos[:40])
print("last 15 O>0 X:", Xpos[-15:])
# max O among positives, and O at crossover region
if pos:
    mx = max(pos, key=lambda r: r["O"]); print("max positive O:", mx)
# threshold: largest X* s.t. O>0 at X*; check all X in [X*, 10000] negative
json.dump({"rows": rows}, open("out_small.json", "w"))

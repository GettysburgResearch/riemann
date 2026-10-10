import json, time, numpy as np
import fast_O
Xs = [2*10**9, 4*10**9, 10**10, 2*10**10, 4*10**10, 10**11, 2*10**11, 4*10**11, 10**12]
out = {"rows": []}
mu = None
Nmax = fast_O.UN_for(Xs[-1])[1]
t0 = time.time()
mu = fast_O.mobius_np(Nmax)
print(f"# sieve to {Nmax}: {time.time()-t0:.0f}s", flush=True)
for X in Xs:
    U, N = fast_O.UN_for(X)
    t0 = time.time()
    h = fast_O.build_h(U, N, mu)
    O, D = fast_O.band_O_D(U, N, h)
    del h
    r = {"X": X, "U": U, "N": N, "O": O, "D": D, "H": D + O, "t": round(time.time()-t0,1)}
    out["rows"].append(r)
    print(json.dumps(r), flush=True)
    with open("out_big.json", "w") as f:
        json.dump(out, f)

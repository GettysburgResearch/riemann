import json, fast_O
out = {"rows": []}
Xs = []
x = 10**4
while x <= 10**8:
    Xs.append(int(x)); x *= 2 ** (1/3)
Nmax = max(max(fast_O.UN_for(X, th)[1] for X in Xs) for th in (0.25, 1/3, 0.4))
mu = fast_O.mobius_np(Nmax)
for th in (0.25, 1/3, 0.4):
    for X in Xs:
        U, N = fast_O.UN_for(X, th)
        if N <= U + 1: continue
        h = fast_O.build_h(U, N, mu)
        O, D = fast_O.band_O_D(U, N, h)
        out["rows"].append({"theta": th, "X": X, "U": U, "N": N, "O": O, "D": D, "H": D+O})
json.dump(out, open("out_theta.json", "w"))
for th in (0.25, 1/3, 0.4):
    rs = [r for r in out["rows"] if r["theta"] == th]
    pos = [r for r in rs if r["O"] > 0]
    print("theta=%.3f: %d pts, O>0: %d, O range [%.3f, %.3f], H range [%.3f, %.3f]" % (
        th, len(rs), len(pos), min(r['O'] for r in rs), max(r['O'] for r in rs),
        min(r['H'] for r in rs), max(r['H'] for r in rs)))
    if pos: print('  positives:', [(r['X'], round(r['O'],3)) for r in pos])

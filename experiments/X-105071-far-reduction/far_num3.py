# far_num3: (i) Hooley-Tenenbaum Delta^2 mean values: S2(x)=sum_{n<=x}Delta(n)^2 vs x(log x)^c,
# vs sum d(n)^2 ~ x log^3 x/pi^2 (the trivial C_0=3 anchor); (ii) corner coefficients
# c_n(delta) = sum_{de=n, d/e in (1,1+delta]} mu(d)eta(e) (+ r~2 corner): verify |c_n|<=2Delta(n),
# measure sum c_n^2 delta-scaling. Anchors: Hooley 1979; Hall-Tenenbaum Divisors; MV mean value.
import numpy as np, json, sys, time
from math import log, sqrt, pi
sys.path.insert(0, __file__.rsplit('/',1)[0])
from far_common import sieves
t0 = time.time()
X = 300000
mu, eta = sieves(X)
checkpoints = [10**4, 3*10**4, 10**5, 3*10**5]
deltas = [0.25, 0.125, 0.0625]
S_d2 = 0.0; S_D2 = 0.0; S_D1 = 0.0
Sc2 = {d: 0.0 for d in deltas}; viol = 0
res_rows = []
BS = 50000
acc = {}
ck = 0
for b0 in range(1, X+1, BS):
    b1 = min(b0+BS-1, X)
    divs = [[] for _ in range(b1-b0+1)]
    for d in range(1, b1+1):
        st = ((b0 + d - 1)//d)*d
        for n in range(st, b1+1, d): divs[n-b0].append(d)
    for n in range(b0, b1+1):
        D = divs[n-b0]
        ld = [log(t) for t in D]
        k = len(D); S_d2 += k*k
        # Delta(n): max count of divisors in a log-window of length 1
        best = 0; j = 0
        for i in range(k):
            if j < i: j = i
            while j+1 < k and ld[j+1] < ld[i] + 1.0: j += 1
            if j-i+1 > best: best = j-i+1
        S_D2 += best*best; S_D1 += best
        # corner coefficients around r=1 and r=2 (r = d/e = d^2/n)
        for dl in deltas:
            c = 0.0
            for d in D:
                e = n//d
                if e*d != n: continue
                r = d/e
                if (1.0 < r <= 1.0+dl) or (2.0/(1.0+dl) < r <= 2.0):
                    c += mu[d]*eta[e]
            Sc2[dl] += c*c
            if dl == 0.25 and abs(c) > 2*best + 1e-9: viol += 1
    while ck < len(checkpoints) and checkpoints[ck] <= b1:
        x = checkpoints[ck]; L = log(x)
        row = {"x": x, "S_Delta2/x": S_D2/b1*(b1/x if x==b1 else 1.0)}
        # NB: checkpoints align with block ends only for 3e5; recompute properly below
        ck += 1
    if b1 in checkpoints or b1 == X:
        L = log(b1)
        c_exp = log(S_D2/b1)/log(L)
        row = {"x": b1, "S_d2/(x L^3/pi^2)": S_d2/(b1*L**3/pi**2),
               "S_Delta2/x": S_D2/b1, "c_fit(S_Delta2 ~ x L^c)": c_exp,
               "S_Delta1/x": S_D1/b1,
               **{f"S_c2/x d={dl}": Sc2[dl]/b1 for dl in deltas}}
        res_rows.append(row)
        print(f"x={b1}: sum d^2/(xL^3/pi^2)={row['S_d2/(x L^3/pi^2)']:.3f}  sum D^2/x={S_D2/b1:.3f} "
              f"(c_fit={c_exp:.3f})  sum D/x={S_D1/b1:.3f}")
        print(f"   corner sum c^2/x: " + "  ".join(f"d={dl}: {Sc2[dl]/b1:.4f}" for dl in deltas)
              + f"   |c|<=2Delta violations: {viol}")
print(f"delta-scaling of sum c^2 (x={X}): ratios "
      f"{Sc2[0.25]/Sc2[0.125]:.2f} (0.25/0.125), {Sc2[0.125]/Sc2[0.0625]:.2f} (0.125/0.0625)")
json.dump({"rows": res_rows}, open(__file__.rsplit('/',1)[0]+"/far_num3_out.json","w"), indent=1)
print(f"done {time.time()-t0:.1f}s")

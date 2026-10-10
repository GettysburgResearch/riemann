#!/usr/bin/env python3
"""Lane 2 RIGOROUS certification of M_2, M_3, M_sc > 0 on [1e6, 5*P61].

Scheme (soundness argument in NOTES.md §§2-6):
 * M_sc: Corollary C — one rigorous evaluation at x0 = 1e6 (M_sc(x0) - eps > 0)
   plus Lemma B1 (dM_sc/dt = -(3/2) M_sc/(4 sqrt(x/e*)-3), sign-preserving on
   C^1 pieces) plus Lemma A (activation jumps weakly UP, even activations
   neutral) gives M_sc(x) > 0 for ALL x >= x0. No grid needed.
 * M_2, M_3: adaptive grid t_i = log x_i. On [x_i, x_{i+1}]:
     Msc_hi = M_sc(x_i) + eps_sc,i + JB_i,   JB_i = (3/4) sum_{odd d in (x_i,x_{i+1}]} d^{-1/2}
     L_j    = 2 Msc_hi max(C_j, rhobar_j - C_j) + |c_j^inf| (4/3) Msc_hi + Ttilde_j + SAFETY
     Ttilde_j = tgbar_j * sum_{d act(x_{i+1}), x_i/d < Ycut} d^{-1/2}
              + C_j * sum_{d: x_i/d >= Ycut} (1/sqrt(x_i/d - 1) + 0.25 (x_i/d-1)^{-1.5}) d^{-1/2}
     CERTIFIED iff  M_j(x_i) - eps_j,i - L_j * (t_{i+1}-t_i) > 0  for j = 2,3.
   Sound because: |dM_j/dt| <= L_j on every C^1 piece in the interval (Lemma B2
   with 0 <= M_sc <= Msc_hi from Cor. C + (B1)-shrink + jump budget (A2');
   rho_j(e*) in [0, rhobar_j]); margins are continuous at kinks; jumps at
   activations are weakly UP (Lemma A) so forward Lipschitz propagation from
   the left endpoint is conservative.
Constants rhobar_j, tgbar_j, Ycut from validate_out.json (cellwise-exact +
analytic tails; see validate.py section 4).
"""
import json
import numpy as np
from math import log, sqrt, exp
import time
import common as C

SAFETY = 1e-6      # absorbs float rounding in the certificate assembly itself
HMIN = 1e-5        # minimal interval width in log x before declaring failure

with open("/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/T105040/lane2/validate_out.json") as f:
    V = json.load(f)["consts"]
RHOBAR = {2: V["rhobar2"], 3: V["rhobar3"]}
TGBAR = {2: V["tgbar2"], 3: V["tgbar3"]}
YCUT = V["Ycut"]
assert V["gdev_ok2"] and V["gdev_ok3"] and V["Qneg2"] == 0 and V["Qneg3"] == 0
# sanity: hardcoded slack rhobars in common.eval_point error budget must dominate
assert RHOBAR[2] <= 1.25 and RHOBAR[3] <= 0.50

import os
X0, X1 = float(os.environ.get("CERT_X0", 1e6)), float(os.environ.get("CERT_X1", 5 * C.P61))
d = C.LAT["d"]; invsq_all = C.LAT["invsq"]
odd_cum = C.LAT["odd_invsq_cum"]

# ---------- M_sc anchor (Corollary C) ----------
p0 = C.eval_point(X0)
msc_floor = p0["M_sc"] - p0["eps_sc"]
print(f"ANCHOR x0=1e6: M_sc = {p0['M_sc']:.9f} - eps {p0['eps_sc']:.2e} "
      f"=> rigorous M_sc(1e6) >= {msc_floor:.9f} > 0: {msc_floor > 0}")
assert msc_floor > 0
# TB positivity beyond P61 (for Lemma A/B validity there):
A_top = 1.0
for p in C.PRIMES:
    A_top *= (1 - 1 / p)
B_top = 1.0
for p in C.PRIMES:
    B_top *= (1 - 1 / sqrt(p))
tb_p61 = 4 * sqrt(float(C.P61)) * A_top - 3 * B_top
print(f"TB for x >= P61: 4 sqrt(x)*{A_top:.6f} - 3*{B_top:.6f} >= {tb_p61:.4e} > 0")
assert tb_p61 > 0 and A_top > 0
# Q >= 0 for Y >= T0 (needed by Lemma A jump-up for M_j; Y < T0 done cellwise):
# Q >= 4 C_j sqrt(Y) - |c_j^inf| log Y - |k_j^inf| - C_j |Elo(Y)|; the RHS has
# positive derivative for sqrt(Y) > |c^inf|/(2 C_j) (tiny), so min at Y = T0.
for j in (2, 3):
    Elo = float(C.E_envelope(np.array([C.T0 * 1.0]), np.array([log(C.T0)]))[0])
    qlo = (4 * C.CJ[j] * sqrt(C.T0) - abs(C.CINF[j]) * log(C.T0)
           - abs(C.KINF[j]) - C.CJ[j] * Elo)
    print(f"Q_Y({j}) >= {qlo:.1f} > 0 for all Y >= T0 (monotone bound)")
    assert qlo > 0 and sqrt(C.T0) > abs(C.CINF[j]) / (2 * C.CJ[j])

cache = {}
def ev(x):
    if x not in cache:
        cache[x] = C.eval_point(x)
    return cache[x]

def interval_bound(x1, x2):
    """Return (ok, info) certifying M_2, M_3 > 0 on [x1, x2]."""
    p = ev(x1)
    h = log(x2) - log(x1)
    i1 = int(np.searchsorted(d, x1, side="right"))
    i2 = int(np.searchsorted(d, x2, side="right"))
    JB = 0.75 * float(odd_cum[i2] - odd_cum[i1])
    msc_hi = p["M_sc"] + p["eps_sc"] + JB
    # Ttilde over divisors active at x2
    dd = d[:i2]; iv = invsq_all[:i2]
    Ylo = x1 / dd                       # for d > x1 this is < 1 -> near bucket
    near = Ylo < YCUT
    far = ~near
    s_near = float(np.sum(iv[near]))
    ym1 = Ylo[far] - 1.0
    s_far_r = float(np.sum((1.0 / np.sqrt(ym1) + 0.25 * ym1 ** -1.5) * iv[far]))
    info = dict(x1=x1, x2=x2, h=h, JB=JB, msc_hi=msc_hi)
    ok = True
    for j in (2, 3):
        Ttilde = TGBAR[j] * s_near + C.CJ[j] * s_far_r
        L = (2 * msc_hi * max(C.CJ[j], RHOBAR[j] - C.CJ[j])
             + abs(C.CINF[j]) * (4.0 / 3.0) * msc_hi + Ttilde + SAFETY)
        floor = p[f"M{j}"] - p[f"eps{j}"] - L * h
        info[f"L{j}"] = L
        info[f"floor{j}"] = floor
        if floor <= 0:
            ok = False
    return ok, info

# ---------- adaptive certification ----------
print("== adaptive grid certification of M_2, M_3 on [1e6, 5*P61] ==", flush=True)
t0 = time.time()
init = np.geomspace(X0, X1, 401)
stack = [(float(init[i]), float(init[i + 1])) for i in range(len(init) - 1)][::-1]
cert = []
fails = []
worst = {2: (1e18, None), 3: (1e18, None)}
maxL = {2: 0.0, 3: 0.0}
nev = 0
while stack:
    x1, x2 = stack.pop()
    ok, info = interval_bound(x1, x2)
    nev += 1
    if ok:
        cert.append(info)
        for j in (2, 3):
            if info[f"floor{j}"] < worst[j][0]:
                worst[j] = (info[f"floor{j}"], x1)
            maxL[j] = max(maxL[j], info[f"L{j}"])
    else:
        if info["h"] <= HMIN:
            fails.append(info)
            print(f"  !! FAILURE at [{x1:.6e},{x2:.6e}] floors "
                  f"{info['floor2']:.4f}/{info['floor3']:.4f}", flush=True)
        else:
            xm = exp(0.5 * (log(x1) + log(x2)))
            stack.append((xm, x2))
            stack.append((x1, xm))
    if nev % 200 == 0:
        print(f"  [{nev} intervals done, {len(stack)} pending, "
              f"{time.time()-t0:.0f}s] at x={x1:.3e}", flush=True)

print(f"== DONE in {time.time()-t0:.0f}s: {len(cert)} certified intervals, "
      f"{len(fails)} FAILURES ==")
for j in (2, 3):
    print(f"  M{j}: worst certified interval floor = {worst[j][0]:.6f} at x1 = "
          f"{worst[j][1]:.6e}; max Lipschitz bound used = {maxL[j]:.3f}")
print(f"  M_sc: > 0 on [1e6, inf) by Corollary C from anchor "
      f"(M_sc(1e6) >= {msc_floor:.6f})")
if not fails:
    print("CERTIFIED: M_2(x) > 0, M_3(x) > 0, M_sc(x) > 0 for all real x in "
          f"[1e6, {X1:.6e}] (= 5*P61).")
res = dict(n_cert=len(cert), n_fail=len(fails),
           worst2=worst[2], worst3=worst[3], maxL2=maxL[2], maxL3=maxL[3],
           msc_anchor=msc_floor, intervals=[{k: float(v) for k, v in c.items()}
                                            for c in cert][:100000],
           fails=[{k: float(v) for k, v in c.items()} for c in fails])
with open("certificate.json", "w") as f:
    json.dump(res, f, default=float)
print("saved certificate.json")

#!/usr/bin/env python3
"""EMPIRICAL model of Lemma 18.3 (lem:centered-lattice-cancellation) over Z[omega].

Status: EMPIRICAL. Ordinary IEEE double precision (numpy). Nothing here is certified,
directed or interval arithmetic. Finite ranges only; no asymptotic statement is inferred.

Source: paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
        sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3,
        Lemma 18.3 at lines 14545-14680, coefficient form at 13953-13996.

Model (the manuscript's conventions, l. 568-600):
  O = Z[omega]; S = {primes above 6} = {(2), (1 - omega)}; ideal sums run over primary
  generators z = a + b omega with z = 1 mod 3 (a = 1, b = 0 mod 3) and odd norm.
  q_z = a^2 - a b + b^2.
  L_i(X, t) = sum_z theta(z) 1_{(z, R*) = 1} q_z^{it} W_i(q_z / X)          (lemma's L_i)
  S_c       = L_1(U_1) L_2(U_2) - L_1(V_1) L_2(V_2),  U_1 U_2 = V_1 V_2 = T  (centred)
  The lemma claims |S_c| << Z^eps (1+|t|)^{2J} T / min(U_1, U_2, V_1, V_2).
  We report rho = |S_c| * min / T (should stay bounded, up to divisor-type factors of the mask)
  and |S_c| / T (should tend to 0), against the uncentred volume |L_1 L_2| / T (order one).

Characters theta (conductor supported on S, hence in a fixed finite family):
  principal; cubic (z mod 2 in F_4^*); sextic (cubic times the quadratic character
  read off z^3 mod 4).
Controls that must FAIL (main terms do not cancel, or the error is not O(1)):
  C1 product mismatch V_2 -> 1.05 V_2; C2 different norm powers t_1 != t_2 on the two plain
  variables; C3 different masks in the two rectangles; C4 sharp cutoff profile 1_[1,2].

Run: OMP_NUM_THREADS=1 python3 -I theta_row_lattice.py out.json [Nmax]
"""
import json
import math
import sys
import time

import numpy as np

T0 = time.time()
OUT = sys.argv[1] if len(sys.argv) > 1 else None
NMAX = int(float(sys.argv[2])) if len(sys.argv) > 2 else int(1.2e7)
RES = {"source_sha256": "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3",
       "label": "EMPIRICAL (ordinary float64; not certified)", "Nmax": NMAX}
CHECKS = []


def record(name, ok, detail):
    CHECKS.append({"check": name, "pass": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + "   " + json.dumps(detail, default=str)[:400])
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# enumeration of primary odd generators
# ---------------------------------------------------------------------------
def enumerate_primary(nmax):
    As, Bs = [], []
    bmax = int(math.isqrt(int(4 * nmax / 3))) + 2
    for b in range(-(bmax // 3 + 1) * 3, bmax + 3, 3):     # b = 0 mod 3
        rem = nmax - 0.75 * b * b
        if rem < 0:
            continue
        s = math.sqrt(rem)
        lo = math.ceil(b / 2 - s)
        hi = math.floor(b / 2 + s)
        lo += (1 - lo) % 3                                  # a = 1 mod 3
        if lo > hi:
            continue
        a = np.arange(lo, hi + 1, 3, dtype=np.int64)
        As.append(a)
        Bs.append(np.full(a.shape, b, dtype=np.int64))
    a = np.concatenate(As)
    b = np.concatenate(Bs)
    n = a * a - a * b + b * b
    keep = (n <= nmax) & (n % 2 == 1)                       # odd norm: coprime to (2)
    a, b, n = a[keep], b[keep], n[keep]
    order = np.argsort(n, kind="stable")
    return a[order], b[order], n[order]


A_, B_, N_ = enumerate_primary(NMAX)
LOGN = np.log(N_.astype(np.float64))
print("enumerated %d primary odd elements with norm <= %d in %.1fs" % (len(N_), NMAX, time.time() - T0))
RES["n_points"] = int(len(N_))


# ---------------------------------------------------------------------------
# characters (values as exponent k in mu_6, i.e. theta = exp(2 pi i k / 6))
# ---------------------------------------------------------------------------
def mul_mod(a1, b1, a2, b2, mod):
    # (a1 + b1 w)(a2 + b2 w) = a1 a2 - b1 b2 + (a1 b2 + a2 b1 - b1 b2) w
    return (a1 * a2 - b1 * b2) % mod, (a1 * b2 + a2 * b1 - b1 * b2) % mod


def cubic_k(a, b):
    """theta_3: z mod 2 in F_4^* = {1, w, w^2}; returns exponent in mu_6 (0, 2, 4)."""
    a2, b2 = a % 2, b % 2
    k = np.where((a2 == 1) & (b2 == 0), 0, np.where((a2 == 0) & (b2 == 1), 1, 2))
    return (2 * k) % 6


def quad_k(a, b):
    """quadratic character from z^3 mod 4 = 1 + 2y, y = y0 + y1 w; value (-1)^{y0}: exponent 0 or 3."""
    a4, b4 = a % 4, b % 4
    s1, s2 = mul_mod(a4, b4, a4, b4, 4)
    c1, c2 = mul_mod(s1, s2, a4, b4, 4)
    y0 = ((c1 - 1) // 2) % 2
    return 3 * y0


CHARS = {"principal": np.zeros(len(N_), dtype=np.int8),
         "cubic_cond2": cubic_k(A_, B_).astype(np.int8),
         "sextic_cond4": ((cubic_k(A_, B_) + quad_k(A_, B_)) % 6).astype(np.int8)}
ROOTS6 = np.exp(2j * np.pi * np.arange(6) / 6)


def char_of(name, a, b):
    a = np.asarray([a], dtype=np.int64)
    b = np.asarray([b], dtype=np.int64)
    if name == "principal":
        return 0
    if name == "cubic_cond2":
        return int(cubic_k(a, b)[0])
    return int((cubic_k(a, b)[0] + quad_k(a, b)[0]) % 6)


# multiplicativity sanity check on random pairs (exact integer arithmetic)
rng = np.random.default_rng(1)
idx = rng.integers(0, len(N_), size=(4000, 2))
okm = True
for i, j in idx[:4000]:
    a1, b1, a2, b2 = int(A_[i]), int(B_[i]), int(A_[j]), int(B_[j])
    a3, b3 = a1 * a2 - b1 * b2, a1 * b2 + a2 * b1 - b1 * b2
    assert a3 % 3 == 1 and b3 % 3 == 0
    for nm in ("cubic_cond2", "sextic_cond4"):
        okm &= (char_of(nm, a1, b1) + char_of(nm, a2, b2)) % 6 == char_of(nm, a3, b3)
nontriv = {nm: int(np.count_nonzero(CHARS[nm])) for nm in CHARS}
record("M0 characters are multiplicative on primary elements and nontrivial", okm and
       nontriv["cubic_cond2"] > 0 and nontriv["sextic_cond4"] > 0,
       {"pairs": 4000, "nonzero exponents": nontriv,
        "sextic order-6 values": int(np.count_nonzero(CHARS["sextic_cond4"] % 2 == 1))})


# ---------------------------------------------------------------------------
# prime ideals outside S, primary generators, divisibility tests
# ---------------------------------------------------------------------------
def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = bytearray(len(s[p * p::p]))
    return [p for p in range(n + 1) if s[p]]


def primary_of(a, b):
    """Return the associate of a + b w that is = 1 mod 3."""
    units = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]  # 1, w, w^2, -1, -w, -w^2
    for ua, ub in units:
        x, y = a * ua - b * ub, a * ub + ua * b - b * ub
        if x % 3 == 1 and y % 3 == 0:
            return x, y
    raise ValueError


def prime_ideals(limit_norm):
    out = []
    for p in primes_upto(limit_norm):
        if p in (2, 3):
            continue
        if p % 3 == 1:
            # find a + b w of norm p
            found = None
            for bb in range(1, int(math.isqrt(4 * p // 3)) + 2):
                disc = 4 * p - 3 * bb * bb
                if disc < 0:
                    break
                r = math.isqrt(disc)
                if r * r == disc and (bb + r) % 2 == 0:
                    found = ((bb + r) // 2, bb)
                    break
            a, b = found
            for (x, y) in (primary_of(a, b), primary_of(a - b, -b)):   # pi and its conjugate
                rho = (-x * pow(y, -1, p)) % p          # w = rho mod pi
                out.append({"norm": p, "gen": (x, y), "kind": "split", "p": p, "rho": rho})
        elif p * p <= limit_norm:
            x, y = primary_of(p, 0)
            out.append({"norm": p * p, "gen": (x, y), "kind": "inert", "p": p})
    out.sort(key=lambda d: (d["norm"], d["gen"]))
    # remove the duplicate conjugate when pi = conj(pi) can't happen for split p; keep distinct
    seen, uniq = set(), []
    for d in out:
        key = (d["norm"], d["gen"])
        if key not in seen:
            seen.add(key)
            uniq.append(d)
    return uniq


PRIMES = prime_ideals(2000)


def divisible(pr):
    if pr["kind"] == "split":
        return (A_ + B_ * pr["rho"]) % pr["p"] == 0
    return (A_ % pr["p"] == 0) & (B_ % pr["p"] == 0)


# check the divisibility test against the norm: pi | z implies N(pi) | N(z)
okd = True
for pr in PRIMES[:12]:
    dv = divisible(pr)
    okd &= bool(np.all(N_[dv] % pr["norm"] == 0)) and int(dv.sum()) > 0
record("M1 divisibility tests consistent with norms (first 12 prime ideals)", okd,
       {"primes": [(p["norm"], p["gen"]) for p in PRIMES[:12]]})


def mask_for(prs):
    m = np.ones(len(N_), dtype=bool)
    for pr in prs:
        m &= ~divisible(pr)
    return m


# ---------------------------------------------------------------------------
# profiles and L_i(X, t)
# ---------------------------------------------------------------------------
def bump(lo, hi):
    def W(y):
        u = (2 * y - lo - hi) / (hi - lo)
        out = np.zeros_like(y, dtype=np.float64)
        ins = np.abs(u) < 1
        out[ins] = np.exp(1.0 - 1.0 / (1.0 - u[ins] ** 2))
        return out
    W.support = (lo, hi)
    W.name = "bump[%g,%g]" % (lo, hi)
    return W


def sharp(lo, hi):
    def W(y):
        return ((y >= lo) & (y < hi)).astype(np.float64)
    W.support = (lo, hi)
    W.name = "sharp[%g,%g)" % (lo, hi)
    return W


W1, W2 = bump(1.0, 3.0), bump(0.5, 2.0)
S1, S2 = sharp(1.0, 2.0), sharp(0.5, 2.0)


def I_of(W, t, n=400001):
    lo, hi = W.support
    y = np.linspace(lo, hi, n)
    f = W(y) * np.exp(1j * t * np.log(y))
    h = (hi - lo) / (n - 1)
    return h * (f.sum() - 0.5 * (f[0] + f[-1]))


C_SET = math.pi / (6 * math.sqrt(3))   # density of primary odd generators per unit norm


def L(X, t, W, chi="principal", mask=None):
    lo, hi = W.support
    i0 = np.searchsorted(N_, lo * X, side="left")
    i1 = np.searchsorted(N_, hi * X, side="right")
    if hi * X > NMAX:
        raise ValueError("scale %g exceeds enumeration" % X)
    if i1 <= i0:
        return 0j
    sl = slice(i0, i1)
    w = W(N_[sl] / X)
    if mask is not None:
        w = w * mask[sl]
    ph = np.exp(1j * t * LOGN[sl])
    k = CHARS[chi][sl]
    if chi != "principal":
        ph = ph * ROOTS6[k]
    return complex(np.sum(w * ph))


def mask_const(prs, chi):
    c = 1.0 + 0j
    for pr in prs:
        c *= 1 - ROOTS6[char_of(chi, *pr["gen"])] / pr["norm"]
    return c


def main_term(X, t, W, prs, chi="principal"):
    if chi != "principal":
        return 0j
    return C_SET * mask_const(prs, chi) * X ** (1 + 1j * t) * I_of(W, t)


# ---------------------------------------------------------------------------
# E1: Moebius identity used in the proof (exact identity, float evaluation)
# ---------------------------------------------------------------------------
R4 = PRIMES[:4]
M4 = mask_for(R4)
worst = 0.0
for chi in ("principal", "sextic_cond4"):
    for X in (60.0, 700.0, 9000.0):
        for t in (0.0, 3.7):
            lhs = L(X, t, W1, chi, M4)
            rhs = 0j
            for sub in range(1 << len(R4)):
                ds = [R4[i] for i in range(len(R4)) if sub >> i & 1]
                qd = math.prod(d["norm"] for d in ds)
                kd = sum(char_of(chi, *d["gen"]) for d in ds) % 6
                rhs += (-1) ** len(ds) * ROOTS6[kd] * qd ** (1j * t) * L(X / qd, t, W1, chi, None)
            worst = max(worst, abs(lhs - rhs) / max(1.0, abs(lhs)))
record("E1 mask inclusion-exclusion L = sum_d mu(d) theta(d) q_d^{it} L^0(X/q_d) (proof step, l. 14628-14633)",
       worst < 1e-10, {"R*": [p["norm"] for p in R4], "max rel dev": worst})

# ---------------------------------------------------------------------------
# E2: main term c_{theta,R*} X^{1+it} I(t), coefficient independent of X and t
# ---------------------------------------------------------------------------
rows = []
R6 = PRIMES[:6]
M6 = mask_for(R6)
for t in (0.0, 3.7, 20.0):
    for X in (30.0, 300.0, 3000.0, 30000.0, 300000.0, 3000000.0):
        Lv = L(X, t, W1, "principal", M6)
        mt = main_term(X, t, W1, R6)
        rows.append({"t": t, "X": X, "L/main": [round((Lv / mt).real, 9), round((Lv / mt).imag, 9)],
                     "|L-main|": abs(Lv - mt), "|L-main|/X": abs(Lv - mt) / X})
top = [r for r in rows if r["X"] == 3000000.0]
okc = all(abs(complex(*r["L/main"]) - 1) < 2e-3 for r in top)
okb = all(r["|L-main|"] <= 2 ** len(R6) * (1 + r["t"]) for r in rows)
record("E2 masked principal sum = c_{R*} X^{1+it} I(t) + O(2^omega (1+|t|)): one coefficient for all X, t",
       okc and okb, {"R*": [p["norm"] for p in R6], "|L/main - 1| at X=3e6 for t=0,3.7,20":
                     [abs(complex(*r["L/main"]) - 1) for r in top],
                     "max |L-main| per t": {str(tt): max(r["|L-main|"] for r in rows if r["t"] == tt)
                                            for tt in (0.0, 3.7, 20.0)},
                     "2^omega(R*)": 2 ** len(R6)})
RES["E2_main_term"] = rows
# nonprincipal: no main term
nrows = []
for chi in ("cubic_cond2", "sextic_cond4"):
    for X in (3000.0, 300000.0, 3000000.0):
        nrows.append({"chi": chi, "X": X, "|L|/X": abs(L(X, 3.7, W1, chi, M6)) / X})
record("E2b nonprincipal theta in the fixed family: no main term (|L|/X small)",
       all(r["|L|/X"] < 1e-3 for r in nrows if r["X"] >= 3e5), nrows)
RES["E2b_nonprincipal"] = nrows


# ---------------------------------------------------------------------------
# E3: centred scaling, and the uncentred volume term
# ---------------------------------------------------------------------------
def centred(T, y1exp, chi, prs, mask, t=3.7, Wa=W1, Wb=W2, t2=None, mask2=None, v2fac=1.0, prs2=None):
    X1 = X2 = math.sqrt(T)
    V1 = T ** y1exp
    V2 = v2fac * T / V1
    t2 = t if t2 is None else t2
    m2 = mask if mask2 is None else mask2
    prs2 = prs if prs2 is None else prs2
    P1 = L(X1, t, Wa, chi, mask) * L(X2, t2, Wb, chi, mask)
    P2 = L(V1, t, Wa, chi, m2) * L(V2, t2, Wb, chi, m2)
    mn = min(X1, X2, V1, V2)
    S = P1 - P2
    pred_unc = main_term(X1, t, Wa, prs, chi) * main_term(X2, t2, Wb, prs, chi)
    pred_S = pred_unc - main_term(V1, t, Wa, prs2, chi) * main_term(V2, t2, Wb, prs2, chi)
    return {"T": T, "min": mn, "|S_c|/T": abs(S) / T, "rho=|S_c|*min/T": abs(S) * mn / T,
            "|uncentred|/T": abs(P1) / T, "pred |uncentred|/T": abs(pred_unc) / T,
            "pred |S|/T (main terms)": abs(pred_S) / T}


Tlist = [1e5, 1e6, 1e7, 1e8, 1e9]
E3 = []
for chi in ("principal", "sextic_cond4"):
    for prs_name, prs in (("none", []), ("R6", R6)):
        mask = None if not prs else M6
        for y1 in (0.25, 0.4):
            for T in Tlist:
                r = centred(T, y1, chi, prs, mask)
                r.update({"chi": chi, "mask": prs_name, "min_exp": y1})
                E3.append(r)
RES["E3_centred"] = E3
pr = [r for r in E3 if r["chi"] == "principal"]
ok_rho = all(r["rho=|S_c|*min/T"] <= (64 if r["mask"] == "R6" else 1) for r in pr)
ok_unc = all(abs(r["|uncentred|/T"] / r["pred |uncentred|/T"] - 1) < 0.01 for r in pr if r["T"] >= 1e8)
ok_pred0 = all(r["pred |S|/T (main terms)"] < 1e-12 for r in E3)
last = [r for r in pr if r["T"] == 1e9]
ok_gap = all(r["|uncentred|/T"] > 30 * r["|S_c|/T"] for r in last)
record("E3 principal centred difference: main terms cancel exactly (pred 0); rho = |S_c| min/T <= 2^omega(R*); "
       "uncentred |L1 L2|/T matches the volume main term; |S_c| << uncentred at T=1e9",
       ok_rho and ok_unc and ok_pred0 and ok_gap,
       {"max rho (no mask)": max(r["rho=|S_c|*min/T"] for r in pr if r["mask"] == "none"),
        "max rho (R6)": max(r["rho=|S_c|*min/T"] for r in pr if r["mask"] == "R6"),
        "uncentred/T at 1e9 (none,R6)": sorted({round(r["|uncentred|/T"], 5) for r in last}),
        "|S_c|/T at 1e9": [("%s,%s" % (r["mask"], r["min_exp"]), "%.2e" % r["|S_c|/T"]) for r in last]})
sx = [r for r in E3 if r["chi"] != "principal" and r["T"] >= 1e7]
record("E3b sextic theta (conductor 4, in the fixed family): no main term, both terms small",
       all(r["|uncentred|/T"] < 1e-3 and r["|S_c|/T"] < 1e-3 for r in sx),
       {"max |uncentred|/T, T>=1e7": max(r["|uncentred|/T"] for r in sx)})

# ---------------------------------------------------------------------------
# E4: controls that must fail
# ---------------------------------------------------------------------------
ctrl = []
R_no7 = PRIMES[2:6]
M_no7 = mask_for(R_no7)
for T in (1e6, 1e7, 1e8, 1e9):
    base = centred(T, 0.4, "principal", R6, M6)
    c1 = centred(T, 0.4, "principal", R6, M6, v2fac=1.05)
    c2 = centred(T, 0.4, "principal", R6, M6, t2=0.0)
    c3 = centred(T, 0.4, "principal", R6, M6, mask2=M_no7, prs2=R_no7)
    base0 = centred(T, 0.4, "principal", [], None)
    c4 = centred(T, 0.4, "principal", [], None, Wa=S1, Wb=S2)
    ctrl.append({"T": T, "min": base["min"], "rho_base_R6": base["rho=|S_c|*min/T"],
                 "rho_base_nomask": base0["rho=|S_c|*min/T"],
                 "C1 product mismatch": [c1["|S_c|/T"], c1["pred |S|/T (main terms)"], c1["rho=|S_c|*min/T"]],
                 "C2 t1 != t2": [c2["|S_c|/T"], c2["pred |S|/T (main terms)"], c2["rho=|S_c|*min/T"]],
                 "C3 mask mismatch": [c3["|S_c|/T"], c3["pred |S|/T (main terms)"], c3["rho=|S_c|*min/T"]],
                 "C4 sharp cutoff (no mask)": [c4["|S_c|/T"], None, c4["rho=|S_c|*min/T"]]})
RES["E4_controls"] = ctrl
RES["E4_columns"] = "[|S|/T measured, |S|/T predicted from non-cancelling main terms, rho=|S| min/T]"
last = ctrl[-1]
for key in ("C1 product mismatch", "C2 t1 != t2", "C3 mask mismatch"):
    meas, pred, rho = last[key]
    record("E4 control %s: |S|/T tracks the non-cancelling main term; rho >> centred rho (bound FAILS as expected)"
           % key, abs(meas / pred - 1) < 0.1 and rho > 10 * last["rho_base_R6"]
           and ctrl[-1][key][2] > ctrl[-2][key][2] > ctrl[-3][key][2],
           {"T=1e9 measured |S|/T": meas, "predicted": pred, "rho": rho, "rho centred": last["rho_base_R6"],
            "rho by T": [round(c[key][2], 3) for c in ctrl]})
rs = [c["C4 sharp cutoff (no mask)"][2] for c in ctrl]
r0 = [c["rho_base_nomask"] for c in ctrl]
record("E4 control C4 sharp cutoff: rho grows with min and far exceeds the smooth case (O(1) error lost)",
       rs[-1] > 10 * r0[-1] and rs[-1] > rs[0],
       {"min by T": [round(c["min"], 1) for c in ctrl], "rho sharp": [round(x, 3) for x in rs],
        "rho smooth": [float("%.3g" % x) for x in r0]})

# ---------------------------------------------------------------------------
# E5: divisor-type loss: rho against the number of prime factors of the mask
# ---------------------------------------------------------------------------
E5 = []
T5, y5 = 1e9, 1.0 / 3.0          # min scale = 1000
V1 = T5 ** y5
mask = np.ones(len(N_), dtype=bool)
for k in range(0, 17):
    if k > 0:
        mask &= ~divisible(PRIMES[k - 1])
    prs = PRIMES[:k]
    r = centred(T5, y5, "principal", prs, mask)
    # number of divisors d | R* with q_d in [V1/30, 3 V1]  (where the lattice error is O(1))
    norms = [p["norm"] for p in prs]
    near = 0
    for sub in range(1 << k):
        qd = 1
        for i in range(k):
            if sub >> i & 1:
                qd *= norms[i]
        if V1 / 30 <= qd <= 3 * V1:
            near += 1
    E5.append({"omega(R*)": k, "2^omega": 2 ** k, "#d near min scale": near,
               "rho": r["rho=|S_c|*min/T"], "rho/max(1,#near)": r["rho=|S_c|*min/T"] / max(1, near)})
RES["E5_divisor_loss"] = E5
record("E5 divisor-type loss: rho <= 2^omega(R*) and tracks the divisors of R* near the min scale",
       all(e["rho"] <= 2 ** e["omega(R*)"] + 1 for e in E5),
       [(e["omega(R*)"], e["#d near min scale"], round(e["rho"], 3)) for e in E5])

# ---------------------------------------------------------------------------
# E6: angular twist (infinite-order Hecke character (z/|z|)^{6k}): absent from the lemma;
# shown only to illustrate that the error grows polynomially in the angular height.
# ---------------------------------------------------------------------------
ang = []
ARG = np.arctan2(B_ * math.sqrt(3) / 2, A_ - B_ / 2)
for kk in (1, 4, 16, 64):
    for X in (1e4, 1e6):
        lo, hi = W1.support
        i0, i1 = np.searchsorted(N_, lo * X), np.searchsorted(N_, hi * X, side="right")
        val = np.sum(W1(N_[i0:i1] / X) * np.exp(1j * 6 * kk * ARG[i0:i1]))
        ang.append({"k": kk, "X": X, "|L_ang|": abs(val), "|L_ang|/X": abs(val) / X})
RES["E6_angular"] = ang
record("E6 angular twist has no main term; error grows with the angular height (illustration only)",
       all(a["|L_ang|/X"] < 0.05 for a in ang if a["X"] >= 1e6),
       [(a["k"], a["X"], "%.3g" % a["|L_ang|"]) for a in ang])

# ---------------------------------------------------------------------------
# E7: direct double sum equals the product form (the factorisation used in the proof)
# ---------------------------------------------------------------------------
def direct_double(X1, X2, Y1, Y2, t, chi, mask):
    def pts(W, lo_s, hi_s):
        lo, hi = W.support
        i0, i1 = np.searchsorted(N_, lo * lo_s), np.searchsorted(N_, hi * hi_s, side="right")
        return slice(i0, i1)
    s1 = pts(W1, min(X1, Y1), max(X1, Y1))
    s2 = pts(W2, min(X2, Y2), max(X2, Y2))
    n1, n2 = N_[s1].astype(float), N_[s2].astype(float)
    c1 = ROOTS6[CHARS[chi][s1]] * mask[s1] * np.exp(1j * t * LOGN[s1])
    c2 = ROOTS6[CHARS[chi][s2]] * mask[s2] * np.exp(1j * t * LOGN[s2])
    D = np.outer(W1(n1 / X1), W2(n2 / X2)) - np.outer(W1(n1 / Y1), W2(n2 / Y2))
    return complex(c1 @ D @ c2)


dd = direct_double(100.0, 100.0, 10.0, 1000.0, 3.7, "sextic_cond4", M4)
pf = L(100.0, 3.7, W1, "sextic_cond4", M4) * L(100.0, 3.7, W2, "sextic_cond4", M4) - \
    L(10.0, 3.7, W1, "sextic_cond4", M4) * L(1000.0, 3.7, W2, "sextic_cond4", M4)
record("E7 direct double sum over (l1, l2) with D_b equals L1 L2 - L1 L2", abs(dd - pf) < 1e-9 * max(1, abs(pf)),
       {"direct": [dd.real, dd.imag], "product": [pf.real, pf.imag]})

RES["checks"] = CHECKS
RES["seconds"] = time.time() - T0
print("%d/%d PASS (E4 controls PASS when the bound is shown to FAIL for the mutated input); %.0fs"
      % (sum(c["pass"] for c in CHECKS), len(CHECKS), time.time() - T0))
if OUT:
    with open(OUT, "w") as fh:
        json.dump(RES, fh, indent=1, default=lambda o: o if not isinstance(o, complex) else [o.real, o.imag])

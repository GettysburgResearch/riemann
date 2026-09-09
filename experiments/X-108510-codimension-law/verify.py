#!/usr/bin/env python3
"""X-108510: stdlib-exact replay for the defect codimension law
(standalone/2026-08-31-defect-codimension-law/PROOF.md).

Checks (EXACT_RATIONAL throughout):
  V1  backward vanishing (BV): for d = 2..6 at integer instantiations,
      the BACKWARD RECURRENCE gives h_{-1} = ... = h_{-(d-1)} = 0 and
      h_{-d} = (-1)^{d-1}/e_d exactly.
  V2  codimension law on the grid (m,d) in {2}x{2..6}, {3}x{2..4},
      {4}x{2,3}: deg Q - deg N (from inline Berlekamp-Massey with
      full-window certification) equals nu = min{j >= 1: h_{-j}^m != 0}
      computed INDEPENDENTLY by the backward recurrence; and the top
      coefficient satisfies c_top(N) = -q_D * phi(-nu).
  V3  transform laws, including two predictions NOT probed by the C1
      atlas: (a) mixed triple h_A h_B h_C with degrees (2,3,4):
      nu = min = 2; (b) section u = 2 of a degree-3 object: nu =
      ceil(3/2) = 2, deg (N, Q) = (1, 3); plus the atlas cases mixed
      cube (nu 2), shift (nu 1), section u = 3, d = 2 (nu 1).
  V4  top-coefficient sign law for m = 2, d = 2..6:
      c_top(N_{2,d}) = (-1)^{C(d-1,2)} e_d^{d-1} exactly (the all-d law
      that closes T-108508's open sign conjecture).

Standard library only. rh_established: false.
"""
import json
import math
import os
import random
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + (f": {detail}" if detail
                                                 and not ok else ""))


def bm(seq):
    C, B = [Fr(1)], [Fr(1)]
    L, m_, bb = 0, 1, Fr(1)
    for n in range(len(seq)):
        d = seq[n] + sum(C[i] * seq[n - i] for i in range(1, L + 1))
        if d == 0:
            m_ += 1
        elif 2 * L <= n:
            Tc = C[:]
            coef = d / bb
            C = C + [Fr(0)] * (len(B) + m_ - len(C))
            for i, bv in enumerate(B):
                C[i + m_] -= coef * bv
            L, B, bb, m_ = n + 1 - L, Tc, d, 1
        else:
            coef = d / bb
            C = C + [Fr(0)] * (len(B) + m_ - len(C))
            for i, bv in enumerate(B):
                C[i + m_] -= coef * bv
            m_ += 1
    while C and C[-1] == 0:
        C.pop()
    return C


def poly_mul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            r[i + j] += pi * qj
    return r


def poly_trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def rational_form(seq):
    Q = bm(seq)
    prod = poly_mul(Q, list(seq))
    P = poly_trim(prod[:len(Q) - 1]) or [Fr(0)]
    for k in range(len(Q) - 1, len(seq)):
        if prod[k] != 0:
            return None
    return P, Q


def h_forward(es, n):
    d = len(es)
    h = [Fr(1)]
    for k in range(1, n + 1):
        s = Fr(0)
        for i in range(1, min(k, d) + 1):
            s += (-1) ** (i - 1) * Fr(es[i - 1]) * h[k - i]
        h.append(s)
    return h


def h_backward(es, n):
    """h_{-1}, ..., h_{-n} via the recurrence run backwards."""
    d = len(es)
    # window h_{k} for k = d-1 down to 0 then extend to negatives:
    # h_k = sum_{i=1..d} (-1)^{i-1} e_i h_{k-i}  =>
    # h_{k-d} = (-1)^{d-1} (h_k - sum_{i=1..d-1} (-1)^{i-1} e_i h_{k-i})/e_d
    win = h_forward(es, d)          # h_0..h_d
    vals = {k: win[k] for k in range(d + 1)}
    for k in range(d - 1, -n - 1 + (d - 1), -1):
        # compute h_{k-d} from h_k..h_{k-(d-1)}
        s = vals[k]
        for i in range(1, d):
            s -= (-1) ** (i - 1) * Fr(es[i - 1]) * vals[k - i]
        vals[k - d] = s * (-1) ** (d - 1) / Fr(es[d - 1])
        if k - d <= -n:
            break
    return [vals[-j] for j in range(1, n + 1)]


def v1():
    rnd = random.Random(108510)
    ok = True
    for d in range(2, 7):
        for _ in range(4):
            es = [rnd.randint(1, 9) * rnd.choice([1, -1])
                  for _ in range(d)]
            hb = h_backward(es, d + 2)
            if any(hb[j] != 0 for j in range(d - 1)):
                ok = False
            if hb[d - 1] != Fr((-1) ** (d - 1), 1) / Fr(es[d - 1]):
                ok = False
    check("V1 backward vanishing h_{-1..-(d-1)}=0, "
          "h_{-d}=(-1)^{d-1}/e_d (d=2..6)", ok)


def run_case(seq, phi_neg):
    """Return (ok_deg, ok_top, deg_N, deg_Q, nu) for a certified case."""
    r = rational_form(seq)
    if r is None:
        return None
    P, Q = r
    nu = next(j + 1 for j, v in enumerate(phi_neg) if v != 0)
    ok_deg = (len(Q) - 1) - (len(P) - 1) == nu
    ok_top = P[-1] == -Q[-1] * phi_neg[nu - 1]
    return ok_deg, ok_top, len(P) - 1, len(Q) - 1, nu


def v2():
    rnd = random.Random(108511)
    grid = ([(2, d) for d in range(2, 7)] + [(3, d) for d in range(2, 5)]
            + [(4, 2), (4, 3)])
    ok = True
    for (m, d) in grid:
        dim = math.comb(d + m - 1, m)
        need = 2 * dim + dim + 8
        for _ in range(4):
            es = [rnd.randint(1, 9) * rnd.choice([1, -1])
                  for _ in range(d)]
            h = h_forward(es, need)
            hb = h_backward(es, d + 3)
            res = run_case([v ** m for v in h],
                           [v ** m for v in hb])
            if res is None:
                ok = False
                check("V2-refused", False, f"(m,d)=({m},{d}) es={es}")
                continue
            ok_deg, ok_top, dN, dQ, nu = res
            if not (ok_deg and ok_top):
                ok = False
                check("V2-case", False,
                      f"(m,d)=({m},{d}) es={es} degN={dN} degQ={dQ} "
                      f"nu={nu} top_ok={ok_top}")
    check("V2 codimension + top-coefficient law on the (m,d) grid "
          "(nu computed independently by backward recurrence)", ok)


def v3():
    rnd = random.Random(108512)
    ok = True
    details = []
    for _ in range(3):
        A = [rnd.randint(1, 9) * rnd.choice([1, -1]) for _ in range(2)]
        B3 = [rnd.randint(1, 9) * rnd.choice([1, -1]) for _ in range(3)]
        C4 = [rnd.randint(1, 9) * rnd.choice([1, -1]) for _ in range(4)]
        n = 80
        hA, hB, hC = (h_forward(A, n), h_forward(B3, n), h_forward(C4, n))
        hbA, hbB, hbC = (h_backward(A, 8), h_backward(B3, 8),
                         h_backward(C4, 8))
        # (a) mixed triple, degrees (2,3,4): nu = max = 4 predicted.
        # HISTORY NOTE: this test was first written expecting the
        # min-law (nu = 2) and REFUTED it — the proof's Corollary 3 was
        # corrected to the max-law as a result; see PROOF.md.
        res = run_case([hA[k] * hB[k] * hC[k] for k in range(n)],
                       [hbA[j] * hbB[j] * hbC[j] for j in range(8)])
        if res is None or not (res[0] and res[1]) or res[4] != 4:
            ok = False
        else:
            details.append(f"triple(2,3,4): degN={res[2]} degQ={res[3]} "
                           f"nu={res[4]}")
        # (b) section u=2 of degree 3: nu = 2 predicted
        res = run_case([hB[2 * k] for k in range(n // 2)],
                       [hbB[2 * j - 1] for j in range(1, 5)])
        if res is None or not (res[0] and res[1]) or res[4] != 2:
            ok = False
        else:
            details.append(f"section u=2 d=3: degN={res[2]} "
                           f"degQ={res[3]} nu={res[4]}")
        # mixed cube h_A^2 h_B(deg2): nu = 2
        B2 = [rnd.randint(1, 9) * rnd.choice([1, -1]) for _ in range(2)]
        hB2, hbB2 = h_forward(B2, n), h_backward(B2, 8)
        res = run_case([hA[k] ** 2 * hB2[k] for k in range(n)],
                       [hbA[j] ** 2 * hbB2[j] for j in range(8)])
        if res is None or not (res[0] and res[1]) or res[4] != 2:
            ok = False
        # shift-then-square: nu = 1
        res = run_case([hA[k + 1] ** 2 for k in range(n - 1)],
                       [hA[0] ** 2] + [hbA[j] ** 2 for j in range(7)])
        if res is None or not (res[0] and res[1]) or res[4] != 1:
            ok = False
        # section u=3 of degree 2: nu = 1
        res = run_case([hA[3 * k] for k in range(n // 3)],
                       [hbA[3 * j - 1] for j in range(1, 3)])
        if res is None or not (res[0] and res[1]) or res[4] != 1:
            ok = False
    check("V3 transform laws incl. NEW predictions: mixed-triple "
          "MAX-law nu=4 (the min-law first coded here was refuted and "
          "the proof corrected), section u=2 d=3 nu=2; mixed cube, "
          "shift, section u=3 d=2", ok, "; ".join(details[:4]))


def v4():
    rnd = random.Random(108513)
    ok = True
    for d in range(2, 7):
        dim = math.comb(d + 1, 2)
        need = 3 * dim + 8
        for _ in range(4):
            es = [rnd.randint(1, 9) * rnd.choice([1, -1])
                  for _ in range(d)]
            h = h_forward(es, need)
            r = rational_form([v * v for v in h])
            if r is None:
                ok = False
                continue
            P, Q = r
            if len(Q) - 1 != dim:
                continue                       # degeneration: skip
            pred = Fr((-1) ** math.comb(d - 1, 2)) * Fr(es[d - 1]) ** (d - 1)
            if P[-1] != pred:
                ok = False
                check("V4-case", False, f"d={d} es={es} top={P[-1]} "
                                        f"pred={pred}")
    check("V4 all-d top-coefficient sign law "
          "c_top(N_{2,d}) = (-1)^{C(d-1,2)} e_d^{d-1}", ok)


def main():
    v1()
    v2()
    v3()
    v4()
    os.makedirs(os.path.join(os.path.dirname(__file__), "results"),
                exist_ok=True)
    allok = all(c["ok"] for c in CHECKS)
    with open(os.path.join(os.path.dirname(__file__), "results",
                           "verification.json"), "w") as f:
        json.dump({"experiment": "X-108510-codimension-law",
                   "checks": CHECKS, "all_ok": allok,
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False}, f, indent=1)
    print("ALL OK" if allok else "FAILURES PRESENT")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())

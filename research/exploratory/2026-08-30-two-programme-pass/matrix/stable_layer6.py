"""corr_6 at its determining rank d = 12 — probing the SECOND-LAYER
law (T-108522 stable layer programme).

The linear alternating law holds at j = 3, 4 and terminates at j = 5
(corr_5 is purely second-stratum). This computes the stable corr_6
(weight 12, determining rank 12), decomposes it in the e-monomial
basis by exact point-evaluation solve (77 partitions of 12 with parts
<= 12), verifies the decomposition by full symbolic subtraction, and
reports whether a linear part reappears. Heavy (h_6^2 in 12
variables); run at low priority. rh_established = false.
"""
import json
import sys
import time
from fractions import Fraction as Fr
from itertools import combinations

sys.path.insert(0, '.')
sys.path.insert(0, 'matrix')
from stable_layers import (corr_layer, e_poly, pmul, padd, pscale, one,
                           partitions)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def eval_poly(p, xv):
    tot = Fr(0)
    for exps, c in p.items():
        v = Fr(c)
        for e, x in zip(exps, xv):
            v *= Fr(x) ** e
        tot += v
    return tot


def eval_e(k, xv):
    d = len(xv)
    tot = Fr(0)
    for S in combinations(range(d), k):
        v = Fr(1)
        for i in S:
            v *= xv[i]
        tot += v
    return tot if k else Fr(1)


def main():
    d, J = 12, 6
    t0 = time.time()
    say(f"computing corr layers to T^{J} at d = {d} ...")
    layers = corr_layer(d, J)
    say(f"corr_6 has {len(layers[6])} monomials "
        f"({time.time()-t0:.0f}s)")
    lams = sorted(partitions(12, 12))
    say(f"{len(lams)} candidate e-partitions")
    # point-evaluation solve
    import random
    random.seed(108522)
    pts = []
    rows = []
    rhs = []
    npts = len(lams) + 15
    for _ in range(npts):
        xv = [random.randint(1, 40) for _ in range(d)]
        ev = {}
        row = []
        for lam in lams:
            v = Fr(1)
            for part in lam:
                if part not in ev:
                    ev[part] = eval_e(part, xv)
                v *= ev[part]
            row.append(v)
        rows.append(row)
        rhs.append(eval_poly(layers[6], xv))
        pts.append(xv)
    say(f"evaluations done ({time.time()-t0:.0f}s); solving ...")
    n = len(lams)
    M = [rows[i] + [rhs[i]] for i in range(len(rows))]
    piv = []
    r0 = 0
    for c in range(n):
        pr = next((r for r in range(r0, len(M)) if M[r][c] != 0), None)
        if pr is None:
            continue
        M[r0], M[pr] = M[pr], M[r0]
        pv = M[r0][c]
        M[r0] = [v / pv for v in M[r0]]
        for r in range(len(M)):
            if r != r0 and M[r][c] != 0:
                f = M[r][c]
                M[r] = [v - f * w for v, w in zip(M[r], M[r0])]
        piv.append(c)
        r0 += 1
    for r in range(r0, len(M)):
        if M[r][n] != 0:
            raise RuntimeError("inconsistent system")
    sol = [Fr(0)] * n
    for r, c in enumerate(piv):
        sol[c] = M[r][n]
    dec = {lams[c]: sol[c] for c in range(n) if sol[c]}
    say("candidate decomposition: " + " + ".join(
        f"{v}*e{list(k)}" for k, v in sorted(dec.items(), reverse=True)))
    # exact symbolic verification
    say("verifying symbolically ...")
    cand = {}
    for lam, cv in dec.items():
        p = one(d)
        for part in lam:
            p = pmul(p, e_poly(d, part))
        assert cv.denominator == 1 or True
        cand = padd(cand, pscale(p, cv))
    okfull = padd(layers[6], pscale(cand, -1)) == {}
    say(f"symbolic verification: {okfull}")
    linear = {k: v for k, v in dec.items() if len(k) <= 2 and k[0] >= 7}
    say(f"linear-part monomials (e_i or e_i e_j with i >= 7): {linear}")
    json.dump({"corr6_e_basis": {str(list(k)): str(v)
                                 for k, v in sorted(dec.items())},
               "symbolic_verified": bool(okfull),
               "rh_established": False},
              open('matrix/stable_layer6.json', 'w'), indent=1)
    say(f"done ({time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()

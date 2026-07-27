#!/usr/bin/env python3
"""X-9505: does leaving the arithmetic-progression cone help?

X-9504 bounded the ARITHMETIC screw route: the L-9507 deficit obeys
1 - rho ~ 3.43 S_T, so the route needs ~10^14 certified zeros.  Its recorded
next attack was to leave the equally-spaced cone, where L-9504's Gram vectors
are geometric progressions in e^{i gamma h}.

For a general node set t_1 < ... < t_m and zero-sum c, L-9501 gives, under RH,

    Q(t,c) = -sum_{i,j} c_i c_j Psi(t_i - t_j)
           = sum_gamma |P(gamma)|^2 / gamma^2,     P(gamma) = sum_j c_j e^{i gamma t_j}

so the same zero-accounting ratio applies with

    A_ij = -Psi(t_i - t_j)                                    (prime side)
    B_ij = 2 sum_{0<gamma<=T} cos(gamma (t_i - t_j)) / gamma^2 (zero side)
    rho  = max_c  c^T B c / c^T A c    over the hyperplane sum_j c_j = 0.

For FIXED nodes that maximum is a generalized eigenvalue on the zero-sum
subspace, so only the nodes need searching.  Arithmetic nodes t_j = j h
recover the L-9507 setting exactly, which is used here as a control.

The structural question: P is an exponential polynomial, hence almost
periodic in gamma and NOT decaying, so |P(gamma)|^2/gamma^2 should inherit an
irreducible 1/gamma^2 tail whatever the nodes are.  If so, no node set escapes
the X-9504 bound.  This experiment tests that.

Standard library only; IEEE binary64; DISCOVERY code, not a certificate.

Usage:
    python3 experiments/screw_free_nodes.py \
        --zeros    experiments/results/X-9503-screw-audit-ratio/zeros1000.json \
        --json-out experiments/results/X-9505-screw-free-nodes/free_nodes.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from screw_lib import Psi, jacobi_eig
from screw_audit_and_ratio import cholesky, _fsolve

_RNG_STATE = [12345]


def rnd():
    """Deterministic LCG; no random seeds from the environment."""
    _RNG_STATE[0] = (1103515245 * _RNG_STATE[0] + 12345) % (1 << 31)
    return _RNG_STATE[0] / float(1 << 31)


def zero_sum_basis(m):
    """Columns span {c in R^m : sum c = 0}: U[:,k] = e_k - e_{k+1}."""
    return [[(1.0 if i == k else (-1.0 if i == k + 1 else 0.0))
             for k in range(m - 1)] for i in range(m)]


def congruence(U, M):
    """U^T M U."""
    m, r = len(U), len(U[0])
    MU = [[sum(M[i][k] * U[k][j] for k in range(m)) for j in range(r)]
          for i in range(m)]
    return [[sum(U[k][i] * MU[k][j] for k in range(m)) for j in range(r)]
            for i in range(r)]


def pencil_max_sym(B, A):
    """lambda_max(B, A) for symmetric B and symmetric PD A."""
    L = cholesky(A)
    r = len(A)
    Y = [_fsolve(L, [B[x][c] for x in range(r)]) for c in range(r)]
    M = [_fsolve(L, [Y[k][c] for k in range(r)]) for c in range(r)]
    for i in range(r):
        for j in range(i + 1, r):
            v = 0.5 * (M[i][j] + M[j][i])
            M[i][j] = M[j][i] = v
    return max(jacobi_eig(M)[0])


class Model:
    def __init__(self, psi, zs, T):
        self.psi = psi
        self.g = [g for g in zs if g <= T]
        self.w = [2.0 / (g * g) for g in self.g]
        self.T = T

    MAX_COND = 1e12

    def rho(self, t):
        """Zero-accounting ratio, maximized over zero-sum c, for nodes t.

        Returns -inf for node sets whose restricted prime-side Gram is not
        positive definite, or is too ill-conditioned for the binary64
        Cholesky congruence to be trusted.  Without that guard the optimizer
        happily runs to nearly-coincident nodes, where the ratio is numerical
        noise rather than a spectral fact.
        """
        m = len(t)
        A = [[-self.psi(t[i] - t[j]) for j in range(m)] for i in range(m)]
        B = [[0.0] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                d = t[i] - t[j]
                s = 0.0
                for g, w in zip(self.g, self.w):
                    s += w * math.cos(g * d)
                B[i][j] = B[j][i] = s
        U = zero_sum_basis(m)
        At = congruence(U, A)
        ev = jacobi_eig(At)[0]
        lo, hi = min(ev), max(ev)
        if lo <= 0.0 or hi / lo > self.MAX_COND:
            return float("-inf")
        try:
            return pencil_max_sym(congruence(U, B), At)
        except ValueError:
            return float("-inf")


def optimize(model, m, span, restarts, rounds, warm=None):
    """Coordinate refinement over node positions, t_0 = 0 fixed.

    `warm` should be the BEST arithmetic node set, so that the free search is
    guaranteed to report at least the arithmetic control and the reported gain
    measures only what breaking equal spacing actually buys.
    """
    best_t, best_r = None, -float("inf")
    for rs in range(restarts):
        if rs == 0:
            t = list(warm) if warm else [span * j / (m - 1) for j in range(m)]
        else:
            t = sorted(rnd() * span for _ in range(m - 1))
            t = [0.0] + t
        r = model.rho(t)
        step = span / (2.0 * m)
        for _ in range(rounds):
            improved = False
            for j in range(1, m):
                for d in (step, -step):
                    cand = t[:]
                    cand[j] = cand[j] + d
                    if cand[j] < 0.0 or cand[j] > span:
                        continue
                    cand_s = sorted(cand)
                    if min(cand_s[k + 1] - cand_s[k]
                           for k in range(m - 1)) < 1e-3:
                        continue
                    rc = model.rho(cand_s)
                    if rc > r:
                        t, r, improved = cand_s, rc, True
            if not improved:
                step *= 0.5
                if step < span * 1e-4:
                    break
        if r > best_r:
            best_t, best_r = t, r
    return best_t, best_r


def best_arithmetic(model, m, span, steps=60):
    """Control: best equally-spaced node set with the same span budget."""
    best = (None, -float("inf"))
    for i in range(1, steps + 1):
        h = span / (m - 1) * i / steps
        r = model.rho([j * h for j in range(m)])
        if r > best[1]:
            best = (h, r)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zeros", required=True)
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--span", type=float, default=15.0)
    ap.add_argument("--T", type=float, default=1000.0)
    ap.add_argument("--restarts", type=int, default=6)
    ap.add_argument("--rounds", type=int, default=25)
    args = ap.parse_args()

    digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    zs = json.load(open(args.zeros))["zeros"]
    limit = int(math.exp(args.span + 0.5)) + 2
    print(f"prime-power table to e^{args.span+0.5} = {limit} ...")
    psi = Psi(limit)
    print(f"primes={psi.n_primes} prime powers={psi.n_pp}  "
          f"zeros<= {args.T}: {len([g for g in zs if g<=args.T])}")

    model = Model(psi, zs, args.T)
    print(f"\nnode span budget {args.span}  (|t_i - t_j| <= span)")
    print(f"{'m':>4} {'arith h*':>10} {'rho arith':>13} {'rho free':>13} "
          f"{'deficit arith':>14} {'deficit free':>13} {'gain':>7}")
    rows = []
    for m in (6, 10, 14, 18, 24):
        h, ra = best_arithmetic(model, m, args.span)
        warm = [j * h for j in range(m)]
        t, rf = optimize(model, m, args.span, args.restarts, args.rounds, warm)
        gain = (1.0 - ra) / (1.0 - rf) if rf < 1.0 else float("inf")
        rows.append({"m": m, "arith_h": h, "rho_arith": ra, "rho_free": rf,
                     "deficit_arith": 1 - ra, "deficit_free": 1 - rf,
                     "gain": gain, "free_nodes": t})
        print(f"{m:>4} {h:>10.5f} {ra:>13.9f} {rf:>13.9f} "
              f"{1-ra:>14.4e} {1-rf:>13.4e} {gain:>7.3f}")

    print("\nbest free node set found (m=24), as gaps t_{j+1}-t_j:")
    t = rows[-1]["free_nodes"]
    gaps = [t[j + 1] - t[j] for j in range(len(t) - 1)]
    print("  " + " ".join(f"{g:.3f}" for g in gaps))
    print(f"  gap mean {sum(gaps)/len(gaps):.4f}  min {min(gaps):.4f}  "
          f"max {max(gaps):.4f}")
    print(f"  arithmetic control gap would be {rows[-1]['arith_h']:.4f}")

    out = {"experiment": "X-9505", "agent": "claude-09",
           "script_sha256": digest,
           "environment": {"python": platform.python_version(),
                           "platform": platform.platform(),
                           "third_party_libraries": "none (standard library only)",
                           "arithmetic": "IEEE binary64"},
           "status": "EMPIRICAL - binary64 reconnaissance, not a certificate",
           "span": args.span, "T": args.T,
           "restarts": args.restarts, "rounds": args.rounds,
           "rows": rows}
    if args.json_out:
        p = Path(args.json_out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(out, indent=1, sort_keys=True))
        print(f"\nwrote {args.json_out}")


if __name__ == "__main__":
    main()

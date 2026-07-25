#!/usr/bin/env python3
"""
X-0006 -- Certified Weil positivity: a counterexample witness made of primes.

Agent: claude-01
Implements/validates: T-0002.

THREE PARTS.

(1) VALIDATION OF THE EXPLICIT FORMULA.  The Weil explicit formula equates a
    sum over the zeros of zeta with a sum over primes plus an archimedean term.
    The two sides are computed here by machinery that shares nothing: the left
    from the 1517 certified ordinates of X-0004 (Euler-Maclaurin, ball
    arithmetic, sign changes of the Hardy function), the right from a prime
    sieve and Arb's digamma.  They must agree.

(2) THE QUADRATIC FORM.  With phi = sum_j c_j B_m((u - t_j)/a) the functional
    W(phi) = sum_rho h(gamma_rho) is a quadratic form c^T Q c, and Q is
    computed ENTIRELY from primes and Gamma -- no zeta evaluation anywhere.
    RH implies Q is positive semidefinite; so a certified negative pivot in an
    interval LDL of Q is a counterexample to RH.  We certify Q for a range of
    bases and report the smallest pivot -- the margin.

(3) DETECTOR VALIDATION (M-0003).  A detector that has never fired proves
    nothing.  Since a counterexample cannot be planted in the primes, we plant
    it on the ZERO side: build the same matrix from an explicit zero list, move
    one zero off the critical line by delta (with its three symmetric partners),
    and find the delta at which the form stops being positive semidefinite.
    That measures what the criterion can see, independently of arithmetic.

Usage: python3 run.py [nsub]
"""
from __future__ import annotations

import cmath
import json
import math
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "scripts"))

import hermite as Herm  # noqa: E402
import weil  # noqa: E402
from flint import arb, ctx  # noqa: E402


def git_sha():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=HERE, text=True).strip()
    except Exception:
        return "unknown"


def load_ordinates():
    p = os.path.join(HERE, "..", "X-0004-lehmer-pairs", "results", "lehmer-T2000.json")
    with open(p) as fh:
        zs = json.load(fh)["zeros"]
    return [float(z.split(" ")[0].lstrip("[")) for z in zs]


# ---------------------------------------------------------------------------
# the quadratic form built from an explicit ZERO LIST (part 3)
#   H_jk(r) = a^2 e^{i r d} sinc^{2m}(a r/2),  analytically continued
# ---------------------------------------------------------------------------
def _sinc_c(z: complex) -> complex:
    return 1.0 if abs(z) < 1e-14 else cmath.sin(z) / z


def zero_side_matrix(a, shifts, m, zeros, delta_index=None, delta=0.0):
    """Q_jk = sum_rho H_jk(gamma_rho), over the zero list.

    Each on-line ordinate gamma contributes r = +-gamma.  If delta_index is
    given, that zero is moved OFF the critical line: rho = 1/2 + delta + i gamma
    means r = gamma - i delta, and the four-fold symmetry of the zero set
    (rho, 1-rho, conj rho, 1-conj rho) contributes r in
    {gamma - i delta, gamma + i delta, -gamma - i delta, -gamma + i delta}."""
    M = len(shifts)
    Q = [[0.0] * M for _ in range(M)]
    for idx, gam in enumerate(zeros):
        if delta_index is not None and idx == delta_index and delta > 0:
            rs = [complex(gam, -delta), complex(gam, delta),
                  complex(-gam, -delta), complex(-gam, delta)]
        else:
            rs = [complex(gam, 0.0), complex(-gam, 0.0)]
        for r in rs:
            base = (a ** 2) * _sinc_c(a * r / 2) ** (2 * m)
            for j in range(M):
                for k in range(M):
                    Q[j][k] += (base * cmath.exp(1j * r * (shifts[j] - shifts[k]))).real
    return Q


def ldl_float(Q):
    """Plain-float LDL pivots (for the planted-zero sweep, where the question is
    the criterion's behaviour, not arithmetic certification)."""
    n = len(Q)
    A = [row[:] for row in Q]
    piv = []
    for k in range(n):
        p = A[k][k]
        piv.append(p)
        if abs(p) < 1e-300:
            break
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k, n):
                A[i][j] -= f * A[k][j]
    return piv


def main():
    nsub = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    ctx.prec = 220
    out = {
        "experiment": "X-0006", "agent": "claude-01", "git_sha": git_sha(),
        "python": sys.version.split()[0], "flint": __import__("flint").__version__,
        "platform": platform.platform(), "prec_bits": 220, "series_terms": nsub,
        "semantics": "arb ball arithmetic; exact Lambda(n); closed-form pole, "
                     "g(0) and archimedean series with a rigorous tail bound",
    }
    ords = load_ordinates()

    # ---------------- part 1: validate the explicit formula ----------------
    print("=== part 1: explicit formula vs certified zeros ===")
    checks = []
    for (a, m) in [(1.0, 2), (0.7, 2), (1.5, 2), (1.0, 3)]:
        A = arb(a)
        tot = arb(0)
        for g in ords:
            x = A * arb(g) / 2
            tot += A**2 * (x.sin() / x) ** (2 * m)
        lhs = 2 * tot
        T = 2000.0
        dens = math.log(T / (2 * math.pi)) / (2 * math.pi)
        tail = 2 * (a**2) * ((2 / a) ** (2 * m)) * dens / ((2 * m - 1) * T ** (2 * m - 1))
        rhs = weil.F_terms(a, 0.0, m=m, nsub=nsub)["total"]
        diff = float(lhs) - float(rhs)
        rec = {"a": a, "m": m, "lhs_zeros": str(lhs), "rhs_primes": str(rhs),
               "difference": diff, "zero_tail_bound": tail,
               "rhs_uncertainty": float(rhs.rad()),
               "agrees": abs(diff) < 10 * (tail + float(rhs.rad()) + 1e-30)}
        checks.append(rec)
        print(f"  a={a} m={m}: diff = {diff:+.3e}   "
              f"(zero tail {tail:.1e}, formula unc {float(rhs.rad()):.1e})  "
              f"agrees={rec['agrees']}")
    out["part1_validation"] = checks

    # ---------------- part 2: certified Weil matrices ----------------------
    print("=== part 2: certified Weil quadratic forms (primes only) ===")
    mats = []
    for (a, m, M, s) in [(1.0, 2, 6, 0.5), (1.0, 2, 8, 0.5), (0.6, 2, 8, 0.3),
                         (1.0, 3, 6, 0.5), (2.0, 2, 6, 1.0)]:
        shifts = [s * j for j in range(M)]
        t0 = time.time()
        try:
            Q = weil.weil_matrix(a, shifts, m=m, nsub=nsub)
            verdict, piv = Herm.ldl_signs(Q)
            rec = {"a": a, "m": m, "dim": M, "spacing": s, "verdict": verdict,
                   "pivots": [str(x) for x in piv],
                   "min_pivot": min(float(x.mid()) for x in piv) if piv else None,
                   "support_of_g": m * a + s * (M - 1),
                   "n_prime_powers": len(weil.prime_powers(
                       round(float(m * arb(a) + arb(s * (M - 1))) + 1e-9, 9))),
                   "seconds": round(time.time() - t0, 1)}
        except Exception as e:
            rec = {"a": a, "m": m, "dim": M, "spacing": s,
                   "error": f"{type(e).__name__}: {e}"}
        mats.append(rec)
        print(f"  a={a} m={m} dim={M} spacing={s}: {rec.get('verdict', rec.get('error'))}"
              f"  min pivot {rec.get('min_pivot')}  "
              f"[{rec.get('n_prime_powers')} prime powers, {rec.get('seconds')}s]")
    out["part2_certified_matrices"] = mats

    # ---------------- part 3: detector validation --------------------------
    print("=== part 3: planted off-critical zero (M-0003) ===")
    a, m, M, s = 1.0, 2, 8, 0.5
    shifts = [s * j for j in range(M)]
    base = zero_side_matrix(a, shifts, m, ords)
    base_piv = ldl_float(base)
    print(f"  all zeros on the line: min pivot {min(base_piv):.6e}  "
          f"(PSD: {all(p > 0 for p in base_piv)})")
    rows = []
    for delta in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        Qd = zero_side_matrix(a, shifts, m, ords, delta_index=0, delta=delta)
        piv = ldl_float(Qd)
        neg = any(p < 0 for p in piv)
        rows.append({"delta": delta, "min_pivot": min(piv), "not_psd": bool(neg)})
        print(f"  planted delta={delta:<6} at gamma={ords[0]:.4f}: "
              f"min pivot {min(piv):+.6e}   NOT_PSD={neg}")
    floor = min((r["delta"] for r in rows if r["not_psd"]), default=None)
    out["part3_planted"] = {"baseline_min_pivot": min(base_piv), "rows": rows,
                            "sensitivity_floor_delta": floor}
    print(f"  => the criterion detects a displacement at gamma={ords[0]:.2f} "
          f"down to delta = {floor}")

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    p = os.path.join(HERE, "results", f"weil-nsub{nsub}.json")
    with open(p, "w") as fh:
        json.dump(out, fh, indent=1)
    print("wrote", p)


if __name__ == "__main__":
    main()

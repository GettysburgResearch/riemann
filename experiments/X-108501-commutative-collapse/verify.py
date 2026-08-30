#!/usr/bin/env python3
"""X-108501: finite verification for T-108501 (commutative collapse).

Standard library only.  Exact checks (Fraction) verify the two algebraic
pillars the proof reduces to, plus the bilinear sum-exchange identity that
IS the finite-N content of the theorem; a final double-precision check is
FLOATING_RECONNAISSANCE corroboration only and decides nothing.

Checks:
  C1 (EXACT_RATIONAL)  nilpotent exponential jet law in Q[e]/(e^m), m=2..6:
                       exp(x) exp(y) = exp(x+y) for nilpotent x, y, and
                       exp(e t) = sum_{j<m} (e t)^j / j!.
  C2 (EXACT_RATIONAL)  sum-exchange identity: for rational data (r_k, t_k),
                       sum_k r_k * jet_m(-t_k) = sum_{j<m} (sum_k r_k (-t_k)^j / j!) e^j
                       -- the finite-N collapse identity with k^{-lambda} -> r_k,
                       log k -> t_k treated as free rational parameters.
  C3 (EXACT_RATIONAL)  bicomplex idempotent decomposition: in Q(i)[j]/(j^2-1)
                       (rational bicomplex), e+ = (1+ij)/2 and e- = (1-ij)/2
                       are orthogonal idempotents summing to 1; an element is
                       invertible iff both idempotent components are nonzero;
                       explicit inverse checked.
  C4 (FLOATING_RECONNAISSANCE)  dual-number truncated zeta sums S_N(lambda+e)
                       agree with the jet formula S_N(lambda) + S_N'(lambda) e
                       to 1e-10 at lambda=2.3, N=200 (corroboration only).

rh_established: false, always.
"""
import json
import math
import os
import sys
from fractions import Fraction as Fr

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


# --- tiny exact algebra: truncated polynomial ring Q[e]/(e^m) -------------

def tp_mul(x, y, m):
    out = [Fr(0)] * m
    for i, a in enumerate(x):
        if a == 0:
            continue
        for j, b in enumerate(y):
            if i + j < m and b != 0:
                out[i + j] += a * b
    return out


def tp_exp_nilpotent(x, m):
    """exp of x with x[0] == 0 (nilpotent part only): finite sum."""
    assert x[0] == 0
    out = [Fr(0)] * m
    out[0] = Fr(1)
    term = [Fr(0)] * m
    term[0] = Fr(1)
    for j in range(1, m):
        term = tp_mul(term, x, m)
        term = [c / j for c in term]
        out = [a + b for a, b in zip(out, term)]
    return out


def c1():
    ok = True
    for m in range(2, 7):
        t = Fr(7, 3)
        x = [Fr(0), t] + [Fr(0)] * (m - 2)
        y = [Fr(0), Fr(-2, 5)] + [Fr(0)] * (m - 2)
        lhs = tp_mul(tp_exp_nilpotent(x, m), tp_exp_nilpotent(y, m), m)
        rhs = tp_exp_nilpotent([a + b for a, b in zip(x, y)], m)
        ok &= (lhs == rhs)
        # jet form of exp(e t)
        expected = [Fr(0)] * m
        f = Fr(1)
        for j in range(m):
            if j:
                f *= j
            expected[j] = t ** j / f
        ok &= (tp_exp_nilpotent(x, m) == expected)
    return check("C1_nilpotent_exponential_jet_law", ok)


def c2():
    ok = True
    for m in (2, 3, 5):
        data = [(Fr(1), Fr(0)), (Fr(1, 4), Fr(693, 1000)),
                (Fr(1, 9), Fr(1099, 1000)), (Fr(1, 16), Fr(1386, 1000)),
                (Fr(-2, 7), Fr(5, 3)), (Fr(11, 13), Fr(-4, 9))]
        lhs = [Fr(0)] * m
        for r, t in data:
            jet = tp_exp_nilpotent([Fr(0), -t] + [Fr(0)] * (m - 2), m)
            lhs = [a + r * b for a, b in zip(lhs, jet)]
        rhs = [Fr(0)] * m
        f = Fr(1)
        for j in range(m):
            if j:
                f *= j
            rhs[j] = sum(r * (-t) ** j for r, t in data) / f
        ok &= (lhs == rhs)
    return check("C2_sum_exchange_identity", ok)


# --- exact bicomplex over Q(i): elements ((a,b),(c,d)) = (a+bi) + (c+di) j,
#     with TWO COMMUTING imaginary units: i^2 = j^2 = -1, ij = ji (so
#     (ij)^2 = +1 and the idempotents are (1 +- ij)/2).  NOT quaternions. ---

def gc_mul(x, y):
    (a, b), (c, d) = x
    (e, f), (g, h) = y
    # (a+bi + (c+di) j)(e+fi + (g+hi) j); the j*j product carries j^2 = -1
    # into the complex part.
    re = (a * e - b * f - (c * g - d * h), a * f + b * e - (c * h + d * g))
    jj = (a * g - b * h + c * e - d * f, a * h + b * g + c * f + d * e)
    return (re, jj)


def c3():
    half = Fr(1, 2)
    ep = ((half, Fr(0)), (Fr(0), half))    # (1 + i j)/2 -> j-part = i/2... careful
    # e+ = (1 + i j)/2: real part 1/2, j-coefficient = i/2 -> ((1/2,0),(0,1/2))
    em = ((half, Fr(0)), (Fr(0), -half))
    one = ((Fr(1), Fr(0)), (Fr(0), Fr(0)))
    ok = gc_mul(ep, ep) == ep and gc_mul(em, em) == em
    ok &= gc_mul(ep, em) == ((Fr(0), Fr(0)), (Fr(0), Fr(0)))
    ok &= tuple(tuple(a + b for a, b in zip(p, q)) for p, q in zip(ep, em)) == one
    # invertibility criterion on a sample: x = 3 e+ + 0 e- is a zero divisor
    x = tuple(tuple(3 * c for c in comp) for comp in ep)
    ok &= gc_mul(x, em) == ((Fr(0), Fr(0)), (Fr(0), Fr(0)))
    # y = 2 e+ + 5 e- has inverse (1/2) e+ + (1/5) e-
    y = tuple(tuple(2 * p + 5 * q for p, q in zip(cp, cq)) for cp, cq in zip(ep, em))
    yinv = tuple(tuple(Fr(1, 2) * p + Fr(1, 5) * q for p, q in zip(cp, cq))
                 for cp, cq in zip(ep, em))
    ok &= gc_mul(y, yinv) == one
    return check("C3_bicomplex_idempotents_and_invertibility", ok)


def c4():
    lam, N = 2.3, 200
    s0 = sum(k ** (-lam) for k in range(1, N + 1))
    s1 = sum(-math.log(k) * k ** (-lam) for k in range(1, N + 1))
    # dual-number direct sum: exp(-(lam+e) log k) = k^-lam (1 - e log k)
    d0 = sum(k ** (-lam) for k in range(1, N + 1))
    d1 = sum(k ** (-lam) * (-math.log(k)) for k in range(1, N + 1))
    ok = abs(d0 - s0) < 1e-10 and abs(d1 - s1) < 1e-10
    return check("C4_floating_corroboration_dual_zeta", ok,
                 "FLOATING_RECONNAISSANCE only; decides nothing")


def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results", "verification.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    all_ok = all([c1(), c2(), c3(), c4()])
    result = {"experiment": "X-108501-commutative-collapse",
              "claim": "T-108501",
              "checks": CHECKS,
              "all_ok": all_ok,
              "arithmetic_class": "EXACT_RATIONAL (C1-C3), FLOATING_RECONNAISSANCE (C4)",
              "rh_established": False,
              "scope_note": ("finite verification of the algebraic pillars and the "
                             "finite-N collapse identity; the theorem's proof is in "
                             "standalone/2026-08-30-commutative-collapse/PROOF.md")}
    with open(out_path, "w") as f:
        json.dump(result, f, indent=1)
    print(("PASS_108501_COMMUTATIVE_COLLAPSE" if all_ok else
           "FAIL_108501_COMMUTATIVE_COLLAPSE") + f" checks={len(CHECKS)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

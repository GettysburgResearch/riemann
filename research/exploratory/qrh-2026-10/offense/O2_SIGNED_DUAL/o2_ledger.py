#!/usr/bin/env python3
"""O2 ledger: exact exponent bookkeeping (sympy rationals) + exact finite identity checks.

Status: PROPOSED bookkeeping; [EXACT] checks are exact integer/rational computations on finitely many
cases; nothing here proves an analytic estimate.  RH is open.

Parts
  L1  leverage law: a saving D^delta below the row-blind bound D^2 at H = D^rho gives
      sigma = 1 - delta/2 - rho/12; beats 11/12 iff delta > (1-rho)/6; target sigma* needs
      delta > 2 - 2 sigma* - rho/6.  Principal-row converse.
  L2  HB00-type Type I on the Moebius variable f of eq:initial-column-output: range where even the
      positivity level is reached (F >= D^(2/3)).
  L3  amplifier ledger (four variants) and the 'reflectable amplifier' threshold.
  C1  [EXACT] gcd-collapse identity  sum_{f | g} mu(f) chi_{n1/f}(k) conj chi_{n2/f}(k)
      = mu(g) 1_{g|k} chi_{z1}(k) conj chi_{z2}(k), with true sextic residue symbols.
  C2  [EXACT] sum_{bfm = n} phi(m)/(N b N m) = 2^omega(n)  (positivity-proxy weight).
  C3  [FLOAT] share of the positivity proxy P carried by blocks with N f < D^(2/3) and by f = 1.

Usage: python3 -I o2_ledger.py OUT.json
"""
import itertools
import json
import os
import random
import sys
from fractions import Fraction

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import signed_dual_numerics as sdn  # noqa: E402  (own code in this folder)

out = {}
rho, delta, lam, s0, sstar = sp.symbols("rho delta lambda sigma0 sigma_star", real=True)

# ---------------- L1 leverage law ----------------
m = 2 - delta                      # Mom(1,rho) bound exponent when delta < 1 - rho
sigma = sp.simplify((m - rho / 6) / 2)
assert sp.simplify(sigma - (1 - delta / 2 - rho / 12)) == 0
thr_1112 = sp.solve(sp.Eq(sigma, sp.Rational(11, 12)), delta)[0]
assert sp.simplify(thr_1112 - (1 - rho) / 6) == 0
thr_78 = sp.solve(sp.Eq(sigma, sp.Rational(7, 8)), delta)[0]
assert sp.simplify(thr_78 - (sp.Rational(1, 4) - rho / 6)) == 0
# 7/8 is reachable with delta <= 1 - rho only for rho <= 9/10 (full saving at rho = 9/10)
r78 = sp.solve(sp.Eq(thr_78, 1 - rho), rho)[0]
assert r78 == sp.Rational(9, 10)
# full saving delta = 1 - rho recovers the ladder 1/2 + 5 rho / 12
assert sp.simplify(sigma.subs(delta, 1 - rho) - (sp.Rational(1, 2) + 5 * rho / 12)) == 0
# principal-row converse: sum >= H^(1/6)|A_1|^2 with |A_1| = D^sigma0  =>  delta <= 2 - rho/6 - 2 sigma0
dmax = 2 - rho / 6 - 2 * s0
# delta > (1-rho)/6 forces sigma0 < 11/12 exactly
sol = sp.solve(sp.Eq(dmax, (1 - rho) / 6), s0)[0]
assert sp.simplify(sol - sp.Rational(11, 12)) == 0
table = []
for r in [sp.Rational(1, 2), sp.Rational(3, 5), sp.Rational(3, 4), sp.Rational(9, 10), sp.Rational(99, 100)]:
    table.append(dict(rho=str(r), delta_beat_11_12=str(thr_1112.subs(rho, r)),
                      delta_beat_7_8=str(sp.Max(thr_78.subs(rho, r), 0)),
                      delta_full=str(1 - r), sigma_full=str(sp.Rational(1, 2) + 5 * r / 12)))
out["L1"] = dict(sigma=str(sigma), threshold_11_12=str(thr_1112), threshold_7_8=str(thr_78),
                 general_threshold=str(sp.simplify(2 - 2 * sstar - rho / 6)), table=table)

# ---------------- L2 HB00 Type I on mu(f) ----------------
# main block b = 1, f ~ F = D^phi, X = D/F, rows Hd = D^2/H.  Positivity level per dyadic F: D^3/H.
# Type I with smooth f2 ~ F2 <= F and trivial (k, m1, m2) summation, Polya-Vinogradov modulus X^2:
#   D^4 X/(H F F2) <= D^3/H  <=>  F^2 F2 >= D^2 ; best F2 = F gives F >= D^(2/3).
phi = sp.symbols("phi", positive=True)
cond = sp.solve(sp.Eq(3 * phi, 2), phi)[0]
assert cond == sp.Rational(2, 3)
out["L2"] = dict(typeI_reaches_positivity_iff="F >= D^(2/3)", phi_min=str(cond),
                 note="blocks with F < D^(2/3) (incl. f = 1, which has no Moebius variable) are untouched")

# ---------------- L3 amplifier ledger ----------------
# amplified primal: sum_{Nu<=H} |A_u(D) B_u(L)|^2, L = D^lam, principal rows give H^(1/6) L^2 |A_1|^2,
# diagonal-size target H D L  =>  2 sigma = (5/6) h + 1 - lam  where H = D^h.
def sig_amp(h):
    return sp.simplify(((sp.Rational(5, 6) * h + 1 - lam)) / 2)

variants = {
    "a_CS_over_ell_plus_propR": 1 + sp.Rational(5, 2) * lam,   # H >= D L^(5/2)
    "b_crossterms_free_propR_Nf": 1 + 2 * lam,                  # H >= D L^2
    "q_quadratic_amplifier_product": 1 + 2 * lam,               # H >= D L^2 (reflection sees only D)
    "c_reflectable_length_DL": 1 + lam,                          # H >= D L  (hypothetical)
}
amp = {}
for k, h in variants.items():
    amp[k] = dict(h=str(h), sigma=str(sig_amp(h)), slope=str(sp.diff(sig_amp(h), lam)))
assert sp.simplify(sig_amp(1 + lam) - (sp.Rational(11, 12) - lam / 12)) == 0
assert sp.simplify(sig_amp(1 + 2 * lam) - (sp.Rational(11, 12) + lam / 3)) == 0
assert sp.simplify(sig_amp(1 + sp.Rational(5, 2) * lam) - (sp.Rational(11, 12) + 13 * lam / 24)) == 0
# general: if the dual reflection works once H >= D L^t, sigma = 11/12 + lam (5t - 6)/12; gain iff t < 6/5
t = sp.symbols("t", positive=True)
gen = sp.simplify(sig_amp(1 + t * lam) - sp.Rational(11, 12))
assert sp.simplify(gen - lam * (5 * t - 6) / 12) == 0
amp["general_H_ge_D_L^t"] = dict(sigma_minus_11_12=str(gen), gain_iff="t < 6/5")
amp["lambda_for_7_8_in_variant_c"] = str(sp.solve(sp.Eq(sp.Rational(11, 12) - lam / 12, sp.Rational(7, 8)), lam)[0])
out["L3"] = amp


# ---------------- L4 import-assisted range in the gcd form ----------------
# block b = 1, dual columns z ~ Z, Moebius variable g ~ G = D/Z, rows k' <~ G Z^2/H.
# inner sum I = sum_g mu(g) conj chi_{z1}(g) chi_{z2}(g) (...) is an original-family member of length G at a
# row of norm Z^6 (representative z1^5 z2).  CONDITIONAL premise (not established; uniformity in the row is an
# extrapolation of Prop. R'):  |I| << G^(11/12) (Z^6)^(1/12).  Trivial outer summation gives
#   (H/D^2) Z^2 (G Z^2/H) G^(11/12) Z^(1/2) = D^(-1/12) Z^(31/12)  (G = D/Z),
# which is <= H iff Z <= D^((12 rho + 1)/31).
zz = sp.symbols("z", positive=True)
expo = sp.simplify(-sp.Rational(1, 12) + sp.Rational(31, 12) * zz)
Gs = 1 - zz
check = sp.simplify((2 * zz + (Gs + 2 * zz - rho)) + rho - 2 + sp.Rational(11, 12) * Gs + sp.Rational(1, 2) * zz - expo)
assert check == 0
zmax = sp.solve(sp.Eq(expo, rho), zz)[0]
assert sp.simplify(zmax - (12 * rho + 1) / 31) == 0
out["L4"] = dict(bound_exponent=str(expo), z_max=str(zmax),
                 z_max_at={str(r): str(zmax.subs(rho, r)) for r in [sp.Rational(3, 5), sp.Rational(3, 4), sp.Rational(9, 10)]},
                 note="blocks with Z > z_max, including G = 1 (no Moebius variable), are not reached")

# ---------------- C1 gcd-collapse identity with true sextic symbols ----------------
P = sdn.prime_ideals(400)
P = [pi for pi in P if pi[0] <= 400]
tabs = [sdn.exponent_table(pi) for pi in P]
random.seed(20261013)
nchecks = 0
ZERO = sdn.ZERO
import numpy as np  # noqa: E402

def chi_exp(S_idx, ka, kb):
    """exponent of chi_n(k) for n = prod of prime ideals in S_idx; None if zero."""
    e = 0
    for i in S_idx:
        v = int(tabs[i](np.array([ka]), np.array([kb]))[0])
        if v >= ZERO:
            return None
        e += v
    return e % 6

def val(e):
    return 0 if e is None else complex(np.exp(2j * np.pi * e / 6))

maxerr = 0.0
ngdiv = 0
for trial in range(400):
    g = random.sample(range(len(P)), random.randint(0, 2))
    rest = [i for i in range(len(P)) if i not in g]
    z1 = random.sample(rest, random.randint(0, 2))
    rest2 = [i for i in rest if i not in z1]
    z2 = random.sample(rest2, random.randint(0, 2))
    # row k: sometimes divisible by primes of g
    ka, kb = random.randint(-60, 60), random.randint(-60, 60)
    if (ka, kb) == (0, 0):
        continue
    if random.random() < 0.5 and g:
        # multiply k by the generator-free trick: choose k in the ideal prod_g via CRT search
        for _ in range(4000):
            ka2, kb2 = random.randint(-400, 400), random.randint(-400, 400)
            if (ka2, kb2) != (0, 0) and all(int(tabs[i](np.array([ka2]), np.array([kb2]))[0]) >= ZERO for i in g):
                ka, kb = ka2, kb2
                break
    n1 = g + z1
    n2 = g + z2
    lhs = 0j
    for r in range(len(g) + 1):
        for f in itertools.combinations(g, r):
            muf = (-1) ** len(f)
            a1 = [i for i in n1 if i not in f]
            a2 = [i for i in n2 if i not in f]
            lhs += muf * val(chi_exp(a1, ka, kb)) * np.conj(val(chi_exp(a2, ka, kb)))
    gdivk = all(int(tabs[i](np.array([ka]), np.array([kb]))[0]) >= ZERO for i in g)
    rhs = ((-1) ** len(g)) * (1 if gdivk else 0) * val(chi_exp(z1, ka, kb)) * np.conj(val(chi_exp(z2, ka, kb)))
    maxerr = max(maxerr, abs(lhs - rhs))
    nchecks += 1
    ngdiv += int(bool(g) and gdivk)
assert maxerr < 1e-9, maxerr
out["C1"] = dict(cases=nchecks, cases_with_nontrivial_g_dividing_k=ngdiv, max_abs_error=maxerr,
                 note="values are 6th roots of unity or 0; error is float rounding of exp(2 pi i e/6)")

# ---------------- C2 triple-divisor weight ----------------
for trial in range(200):
    norms = random.sample([7, 13, 19, 25, 31, 37, 43, 49, 61, 67, 73, 79, 97, 103, 109, 121], random.randint(0, 5))
    tot = Fraction(0)
    for assign in itertools.product(range(3), repeat=len(norms)):
        Nb = Fraction(1); Nm = Fraction(1); ph = Fraction(1)
        for q, a in zip(norms, assign):
            if a == 0:
                Nb *= q
            elif a == 2:
                Nm *= q; ph *= (q - 1)
        tot += ph / (Nb * Nm)
    assert tot == 2 ** len(norms)
out["C2"] = "sum_{bfm=n} phi(m)/(Nb Nm) = 2^omega(n): 200 exact cases pass"

# ---------------- C3 block shares of the positivity proxy ----------------
def shares(D):
    Pn = sdn.prime_ideals(2 * D)
    norms = [pi[0] for pi in Pn]
    tot = 0.0; small = 0.0; f1 = 0.0
    cut = D ** (2 / 3)
    stack = [(0, 1, ())]
    while stack:
        i0, nn, fac = stack.pop()
        if nn > D:
            x = nn / D
            w = float(sdn.W(np.array([x]))[0])
            if w:
                # distribution of N(f) over triples (b,f,m), weights 1/Np (b), 1 (f), 1-1/Np (m)
                dist = {1.0: 1.0}
                for q in fac:
                    nd = {}
                    for nf, wt in dist.items():
                        nd[nf] = nd.get(nf, 0.0) + wt * (1 / q + (1 - 1 / q))
                        nd[nf * q] = nd.get(nf * q, 0.0) + wt
                    dist = nd
                base = x * w * w
                tot += base * sum(dist.values())
                small += base * sum(v for k, v in dist.items() if k < cut)
                f1 += base * dist[1.0]
        for i in range(i0, len(Pn)):
            n2 = nn * norms[i]
            if n2 >= 2 * D:
                break
            stack.append((i + 1, n2, fac + (norms[i],)))
    return dict(D=D, P=tot, share_F_lt_D23=small / tot, share_f_eq_1=f1 / tot)

out["C3"] = [shares(D) for D in (1000, 10000, 100000)]

with open(sys.argv[1], "w") as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps(out, indent=1, default=str))

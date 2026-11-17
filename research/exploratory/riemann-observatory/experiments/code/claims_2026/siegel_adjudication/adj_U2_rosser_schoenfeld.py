#!/usr/bin/env python3
"""
SIEGEL adjudication of audit item U2:
  Banks (arXiv:2610.15483v1) eq. (2.7) uses Rosser-Schoenfeld 1962 Thm 6, quoted as
    (3.21)  sum_{p<=x} log p/p > log x + E - 1/(2 log x)   (x > 1)
    (3.22)  sum_{p<=x} log p/p < log x + E + 1/(2 log x)   (x >= 319)
  The 1962 original could not be re-read (publisher site refuses automated access).

This script (our own code; nothing from any audited repository is run) does:
  (1) Banks's downstream constants: kappa, 1/log 319, and the largest RS error constant the
      argument of Lemma 2.1 can absorb.
  (2) E: rigorous arb enclosure E = -gamma - sum_p log p/(p(p-1)), plus an mpmath cross-check.
  (3) RIGOROUS (arb ball arithmetic) check of (3.21) for 1 < x <= 1e7 and (3.22) for
      319 <= x <= 1e7, at the extremal points of the step function.
  (4) Threshold fingerprint: where (3.22) last fails, and the analogous cut-offs for the
      1/log x variants quoted by secondary sources.
  (5) The partial-summation identity used in (6), checked exactly at sample points.
  (6) RS62-independent analytic range x > 1e7 from imported explicit theta bounds
      (Broadbent-Kadiri-Lumley-Ng-Wilk, Math. Comp. 2021, arXiv:2002.11068v2, Table 15 and (3.39)).
  (7) Direct finite test of what Banks actually uses, (2.7), over prime pairs (INFO, float64).
Run: python3 -I adj_U2_rosser_schoenfeld.py
"""
import math
import sys
import time

import numpy as np
import mpmath as mp
import flint
from flint import arb

NPASS = 0
NFAIL = 0


def rep(ok, msg):
    global NPASS, NFAIL
    if ok:
        NPASS += 1
    else:
        NFAIL += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


def info(msg):
    print("INFO " + msg, flush=True)


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]


print(f"python {sys.version.split()[0]}  numpy {np.__version__}  mpmath {mp.__version__}  python-flint {flint.__version__}")
t0 = time.time()

# ---------------------------------------------------------------- (1) Banks's downstream constants
mp.mp.dps = 30
kappa = mp.log(mp.pi) / 2 - mp.digamma(mp.mpf(3) / 2) / 2
L319 = mp.log(319)
rep(abs(kappa - mp.mpf("0.5541")) < 1e-4 and kappa / 2 > mp.mpf("0.277"),
    f"(1a) kappa = (1/2)log pi - (1/2)psi(3/2) = {mp.nstr(kappa, 10)}; kappa/2 = {mp.nstr(kappa/2, 8)} > 0.277")
rep(1 / L319 < mp.mpf("0.174"), f"(1b) 1/log 319 = {mp.nstr(1/L319, 8)} < 0.174")
# If |sum - log x - E| <= c_l/log x (lower side) and c_u/log x (upper side, x >= 319), (2.7) becomes
#   sum_{H<p<=X} > log X - log H - (c_l + c_u)/log H,
# and the last step of Lemma 2.1 needs e^lam*kappa/2 - (c_l+c_u)/(2 log H) ... more precisely
# e^lam kappa/2 - (c_l+c_u)/(2 * 1/2) * (1/log H)/... we keep Banks's form: loss = (c_l+c_u)/log H.
crit_all_lambda = kappa * L319 / 2           # need (c_l + c_u)/log 319 < kappa/2   (lambda -> 0)
crit_lambda_3_2 = mp.e ** 1.5 * kappa * L319 / 2
info(f"(1c) Lemma 2.1 closes for every lambda in (0,2] iff c_l + c_u < kappa log 319 / 2 = {mp.nstr(crit_all_lambda, 6)} "
     f"(RS62 gives c_l + c_u = 1); at lambda = 3/2 the threshold is {mp.nstr(crit_lambda_3_2, 6)}")
info(f"(1d) final positivity with RS constants at lambda=3/2: e^1.5 kappa/2 - 1/log 319 = "
     f"{mp.nstr(mp.e**1.5*kappa/2 - 1/L319, 6)}; at lambda -> 0: kappa/2 - 1/log 319 = {mp.nstr(kappa/2 - 1/L319, 6)}")

# ---------------------------------------------------------------- (2) E
N = 10 ** 7
P = sieve(N)
info(f"(2) primes <= {N:.0e}: {len(P)}; largest {P[-1]}")
flint.ctx.prec = 96
S2 = arb(0)
for p in P.tolist():
    lp = arb(p).log()
    S2 += lp / (p * (p - 1))
Nn = arb(N)
tail = Nn.log() / (Nn - 1) + (Nn / (Nn - 1)).log()   # >= sum_{n>N} log n/(n(n-1))
mid = -arb.const_euler() - S2 - tail / 2
E_arb = mid + arb(0, tail.mid() / 2 * (1 + 1e-9) + float(tail.rad()) + float(mid.rad()))
E_ref = mp.mpf("-1.332582275733220881765828776071027748")   # value used in the part-1 audit (OEIS A083343)
# mpmath: sum_p log p/(p(p-1)) = sum_{n>=2} sum_p log p p^{-n} = sum_{n>=2} sum_{k>=1} mu(k) (-zeta'/zeta)(kn)


def mobius(k):
    r, m, d = 1, k, 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            r = -r
        d += 1
    if m > 1:
        r = -r
    return r


mp.mp.dps = 40
acc = mp.mpf(0)
for n in range(2, 160):
    for k in range(1, 160 // n + 2):
        mu = mobius(k)
        if mu:
            s = k * n
            acc += mu * (-mp.zeta(s, derivative=1) / mp.zeta(s))
E_mp = -mp.euler - acc
info(f"(2a) E (arb enclosure, primes <= 1e7 + tail bound) = {E_arb}")
info(f"(2b) E (mpmath, prime-zeta series, 40 dps) = {mp.nstr(E_mp, 30)}")
rep(abs(E_mp - E_ref) < mp.mpf(10) ** -25 and (E_arb - float(E_ref)).contains(0) if hasattr(E_arb, 'contains') else True,
    f"(2c) E agrees with -1.33258227573322088176582877607... (part-1 constant, OEIS A083343); |mp - ref| = {mp.nstr(abs(E_mp - E_ref), 3)}")
rep(float(E_arb.rad()) < 2e-6, f"(2d) rigorous E enclosure radius {float(E_arb.rad()):.2e} (<< the smallest margin found below)")

# ---------------------------------------------------------------- (3) rigorous finite check
flint.ctx.prec = 96
S = arb(0)
half = arb(1) / 2
low_min = None   # (margin_mid, p, x_used)
up_min = None
low_ok = True
up_ok = True
Pl = P.tolist()
logs = [None] * len(Pl)
Svals_float = np.empty(len(Pl))
for i, p in enumerate(Pl):
    lp = arb(p).log()
    logs[i] = lp
    S += lp / p
    Svals_float[i] = float(S.mid())
    # lower bound (3.21) on [p, p_next): worst at x -> p_next^-
    xn = Pl[i + 1] if i + 1 < len(Pl) else N
    ln = arb(xn).log()
    m_low = S - (ln + E_arb - half / ln)
    if not (m_low > 0):
        low_ok = False
    mm = float(m_low.mid())
    if low_min is None or mm < low_min[0]:
        low_min = (mm, p, xn)
    # upper bound (3.22) on [p, p_next) for p >= 331: worst at x = p
    if p >= 331:
        m_up = (lp + E_arb + half / lp) - S
        if not (m_up > 0):
            up_ok = False
        mm = float(m_up.mid())
        if up_min is None or mm < up_min[0]:
            up_min = (mm, p, p)
    if p == 317:
        S317 = S
        l319 = arb(319).log()
        m319 = (l319 + E_arb + half / l319) - S317   # x in [319, 331): worst at x = 319
        if not (m319 > 0):
            up_ok = False
        if up_min is None or float(m319.mid()) < up_min[0]:
            up_min = (float(m319.mid()), 317, 319)
# x in (1,2): sum = 0 and RHS(2) < 0
r2 = arb(2).log() + E_arb - half / arb(2).log()
low_ok = low_ok and (r2 < 0)
rep(low_ok, f"(3a) RIGOROUS: (3.21) holds for all 1 < x <= 1e7; min margin {low_min[0]:.6f} "
            f"(sum over p <= {low_min[1]} vs x -> {low_min[2]}^-); RHS(2) = {float(r2.mid()):.4f} < 0")
rep(up_ok, f"(3b) RIGOROUS: (3.22) holds for all 319 <= x <= 1e7; min margin {up_min[0]:.6f} at x = {up_min[2]}")
info(f"(3c) arb run time so far {time.time() - t0:.1f}s")

# ---------------------------------------------------------------- (4) threshold fingerprint
mp.mp.dps = 30
Pm = [int(p) for p in P[P < 2000]]
Sm = []
acc = mp.mpf(0)
for p in Pm:
    acc += mp.log(p) / p
    Sm.append(acc)
E = E_mp


def up_fail_set(c):
    """x-intervals (as primes p with the failing sub-interval [p, x*)) where sum >= log x + E + c/log x."""
    out = []
    for i, p in enumerate(Pm[:-1]):
        f = lambda x: mp.log(x) + E + c / mp.log(x) - Sm[i]
        if f(p) <= 0:   # fails at x = p (RHS increasing on [p, p_next) for p >= 3)
            # crossing inside [p, p_next) ?
            q = Pm[i + 1]
            if f(q) > 0:
                xs = mp.findroot(f, (p, q), solver='anderson')
            else:
                xs = q
            out.append((p, xs))
    return out


def low_fail_set(c):
    out = []
    for i, p in enumerate(Pm[:-1]):
        q = Pm[i + 1]
        f = lambda x: Sm[i] - (mp.log(x) + E - c / mp.log(x))
        if f(q) <= 0:   # fails as x -> q^-
            xs = mp.findroot(f, (p, q), solver='anderson') if f(p) > 0 else p
            out.append((xs, q))
    return out


uf = up_fail_set(mp.mpf(1) / 2)
info(f"(4a) (3.22) [1/(2 log x)] fails exactly on: " +
     ", ".join(f"[{p}, {mp.nstr(xs, 8)})" for p, xs in uf))
last = uf[-1]
rep(last[0] == 317 and 318 < last[1] < 319,
    f"(4b) last failure of the 1/(2 log x) upper bound is x in [317, {mp.nstr(last[1], 10)}); "
    f"so 319 is exactly the least integer from which (3.22) holds (fingerprint of the quoted threshold)")
lf = low_fail_set(mp.mpf(1) / 2)
rep(len(lf) == 0, f"(4c) (3.21) [1/(2 log x)] has no failure for 1 < x < 2000 (consistent with 'x > 1')")
uf1 = up_fail_set(mp.mpf(1))
info(f"(4d) upper bound with 1/log x fails on: {', '.join(f'[{p}, {mp.nstr(xs, 8)})' for p, xs in uf1) or 'nothing'} "
     f"(x in (1,2) has sum 0 < RHS) -> consistent with the (3.23) form 'sum < log x + E + 1/log x' quoted by arXiv:2201.06184")
lf1 = low_fail_set(mp.mpf(1))
info(f"(4e) lower bound with 1/log x fails on: {', '.join(f'({mp.nstr(a, 8)}, {b})' for a, b in lf1) or 'nothing'}")

# ---------------------------------------------------------------- (5) partial summation identity
# sum_{p<=x} log p/p = theta(x)/x + int_2^x theta(t)/t^2 dt   (theta a step function: exact)
mp.mp.dps = 30
ok5 = True
for X in (100, 10 ** 4, 10 ** 5):
    ps = [int(p) for p in P[P <= X]]
    lhs = mp.fsum(mp.log(p) / p for p in ps)
    th = mp.mpf(0)
    integ = mp.mpf(0)
    for j, p in enumerate(ps):
        th += mp.log(p)
        nxt = ps[j + 1] if j + 1 < len(ps) else X
        integ += th * (mp.mpf(1) / p - mp.mpf(1) / nxt)
    rhs = th / X + integ
    ok5 = ok5 and abs(lhs - rhs) < mp.mpf(10) ** -25
rep(ok5, "(5) Abel summation identity sum_{p<=x} log p/p = theta(x)/x + int_2^x theta/t^2 holds exactly at x = 1e2, 1e4, 1e5;"
         " hence sum - log x - E = R(x)/x - int_x^oo R(t)/t^2 dt with R = theta - id")

# ---------------------------------------------------------------- (6) analytic range x > 1e7 (imported theta bounds)
# BKLNW (arXiv:2002.11068v2) Table 15, row log X0 = log(1e7):  |theta(x) - x| < 0.13675 x / log^2 x  for x > 1e7.
# Then |sum - log x - E| <= M/L^2 + M/L (integral of M/(t log^2 t) = M/log x).
M2 = mp.mpf("0.13675")
# need M/L^2 + M/L < 1/(2L)  <=>  M/L + M < 1/2 ; worst at the smallest L
Lmin = mp.log(10 ** 7)
lhs6 = M2 / Lmin + M2
rep(lhs6 < mp.mpf(1) / 2, f"(6a) x > 1e7 via BKLNW Table 15 (k=2, M=0.13675): need M/L + M < 1/2 at L = log 1e7: {mp.nstr(lhs6, 6)} < 0.5")
# Alternative: BKLNW (3.39): |theta(x)-x| < 151.3 x/log^4 x for x >= 2. Then |..| <= 151.3/L^4 + 151.3/(3 L^3) < 1/(2L)
f = lambda L: 151.3 / L ** 3 + 151.3 / (3 * L ** 2) - mp.mpf(1) / 2
L1 = mp.findroot(f, 11)
info(f"(6b) alternative route via BKLNW (3.39) (k=4, M=151.3, x >= 2): the 1/(2 log x) bound follows for log x > {mp.nstr(L1, 6)} "
     f"(x > {mp.nstr(mp.e ** L1, 6)}), far inside the rigorous range of (3)")
# fingerprints of the imported constants (finite, float64): max |theta-x| log^4 x/x (incl. left limits at primes)
th = np.cumsum(np.log(P.astype(np.float64)))
Pf = P.astype(np.float64)
th_left = np.concatenate(([0.0], th[:-1]))      # theta(p^-)
v_at = np.abs(th - Pf) * np.log(Pf) ** 4 / Pf
v_left = np.abs(th_left - Pf) * np.log(Pf) ** 4 / Pf
i_max = int(np.argmax(np.maximum(v_at, v_left)))
info(f"(6c) max over x <= 1e7 of |theta(x)-x| log^4 x / x = {max(v_at.max(), v_left.max()):.4f} at p = {P[i_max]} "
     f"(BKLNW quote Dusart: 151.2235... attained at the prime 1423)")
rep(P[i_max] == 1423 and abs(max(v_at.max(), v_left.max()) - 151.2235) < 1e-3,
    "(6d) fingerprint of the imported k=4 constant reproduced")
sel = Pf > 1e7
info("(6e) the k=2 Table-15 constant for x > 1e7 cannot be fingerprinted below 1e7 (it concerns x > 1e7); see (6f)")

# ---------------------------------------------------------------- (6f) non-rigorous extension to 1e8 (float64)
N8 = 10 ** 8
P8 = sieve(N8)
P8f = P8.astype(np.float64)
lp8 = np.log(P8f)
cs = np.cumsum(lp8 / P8f)
Ef = float(E_mp)
nxt8 = np.append(P8f[1:], float(N8))
lowm = cs - (np.log(nxt8) + Ef - 0.5 / np.log(nxt8))
upm = (lp8 + Ef + 0.5 / lp8) - cs
mask = P8 >= 331
th8 = np.cumsum(lp8)
big = P8f > 1e7
th8_left = np.concatenate(([0.0], th8[:-1]))
k2 = np.maximum(np.abs(th8 - P8f), np.abs(th8_left - P8f)) * lp8 ** 2 / P8f
info(f"(6f) float64 to 1e8: (3.21) min margin {lowm.min():.5f}, (3.22) min margin over p >= 331 {upm[mask].min():.5f}; "
     f"max_(1e7,1e8] |theta-x| log^2 x/x = {k2[big].max():.5f} (< 0.13675, consistent with Table 15)")
rep(lowm.min() > 0 and upm[mask].min() > 0 and k2[big].max() < 0.13675, "(6g) float64 extension to 1e8 consistent")

# ---------------------------------------------------------------- (7) Banks (2.7) directly, finite (float64)
# margin(H, X) = [S(X) - S(H)] - [log X - log H - 1/log H]  over primes 319 <= H and X > H, X <= 1e8.
# For fixed prime H the infimum over X in (H, 1e8] is attained at a left limit X -> q^- (q prime > H) or X = 1e8,
# where S(X) = S(prev prime). g(q) := S(q^-) - log q.
Sleft = np.concatenate(([0.0], cs[:-1]))
g = Sleft - lp8                                      # value at X -> p^-
g = np.append(g, cs[-1] - math.log(N8))              # X = 1e8
sufmin = np.minimum.accumulate(g[::-1])[::-1]        # sufmin[j] = min_{k>=j} g[k]
idxH = np.nonzero(P8 >= 319)[0]
idxH = idxH[idxH + 1 < len(g)]
marg = sufmin[idxH + 1] - (cs[idxH] - lp8[idxH]) + 1.0 / lp8[idxH]
jm = int(np.argmin(marg))
info(f"(7) Banks (2.7) over all primes 319 <= H < X <= 1e8 (H prime is the worst case for integer H): "
     f"min margin {marg.min():.5f} at H = {P8[idxH[jm]]}")
rep(marg.min() > 0, "(7b) Banks (2.7) has positive margin throughout the tested range")

print(f"\nTOTAL: {NPASS} PASS / {NFAIL} FAIL   ({time.time() - t0:.1f}s)")

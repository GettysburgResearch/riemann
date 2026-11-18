"""SIEGEL Level-2 audit, part 2, steps 8-9 (the exponent gap; parameters and small conductors).
Our own code; nothing from the audited repositories is executed.  Run: python3 -I s8_s9_gap_parameters.py

 (8a) Unified exponent table, exact fractions: each proof yields an unconditional bound
          S_-(X) <= kappa log X + e log q + O(1)   (X a power of q)
      OAI/Banks kappa = (3/4)(1 + S2/S1) <= 13/16; Kerr (3/4)(1+2/w) = 15/16 at w = 8 (13/10 threshold gives 39/40);
      Guo 1/2 + (3/2) lambda <= 11/20.  Consistency: kappa >= 1/2 is forced by the prime ideal theorem
      (S_-(x) ~ (1/2) log x for a fixed field), and kappa < 1 is what the contradiction needs.
 (8b) The generic chain  (1-kappa) A - K <= b delta A^2  (A = log X / log q)  gives the closed-form optimum
          delta* = (1-kappa)^2 / (4 b K)   at A* = 2K/(1-kappa).
      Applied to Banks (7.3): (1-kappa) = 3/16, b = C1, K = C2 + 8/5  ->  continuous optimum, compared with Banks's
      81/(5888 e^{3/2}) and with omega = 22; Guo's chain asymptotically (q -> infinity) re-optimized independently.
 (8c) "Proves too much" in the q-aspect: the least prime p1 with chi(p1) != -1.  If all odd p <= x are inert then
      S_-(x) >= M(x) - (log 2)/2; with Rosser-Schoenfeld (3.21) and Guo's (3.1) this gives
          log p1 <= (29/27) log q + c;  Barreto/van Dijk shape gives (1/2) log q + o(log q).
      Both are WEAKER than known facts (p1 <= smallest prime factor of q; Linnik-Vinogradov/Burgess p1 << q^{1/4+eps}),
      so the arithmetic layer is not "too strong" in the q-aspect.  Data: max log p1 / log q over fundamental |D| <= 2e5.
 (9a) Parameter conditions (OAI with Banks's choices; Banks Step 1; the identity defining delta0).
 (9b) Guo's single parameter choice y = q^6, x = q^70 at delta = 1/100: margin of the final contradiction with EXACT
      logarithms and the paper's own error terms, on a log grid q in [3, 1e15]; minimum location.
 (9c) Small conductors, uncertified numerics: L(sigma, chi_D) > 0 on a sigma-grid in [1/2, 1] for every fundamental
      |D| <= DMAX (Euler-Maclaurin accelerated sums, validated against mpmath.dirichlet).  Consistent with (and far
      weaker than) the certified Lu-Zaman-Zhao computation that Banks cites for q <= 1e10; not a certificate.
"""
from fractions import Fraction as F
import math
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
out = []
fails = 0
DMAX = 3000


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def info(msg):
    out.append("INFO " + msg)


# ---------------------------------------------------------------- (8a)
kap = {
    "OAI/Banks (S2/S1 <= 1/12)": F(3, 4) * (1 + F(1, 12)),
    "OAI limit H -> infinity": F(3, 4),
    "Kerr w = 8 intrinsic (3/4)(5/4)": F(3, 4) * F(5, 4),
    "Kerr as used (3/4)(13/10)": F(3, 4) * F(13, 10),
    "Guo lambda <= 1/30": F(1, 2) + F(3, 2) * F(1, 30),
    "Guo limit lambda -> 0": F(1, 2),
    "Barreto/van Dijk": F(1, 2),
}
ok = all(F(1, 2) <= k < 1 for k in kap.values())
ok &= kap["OAI/Banks (S2/S1 <= 1/12)"] == F(13, 16) and kap["Guo lambda <= 1/30"] == F(11, 20)
ok &= kap["Kerr as used (3/4)(13/10)"] == F(39, 40) and F(5, 4) < F(13, 10) < F(4, 3)
ok &= F(13, 16) + F(1, 16) == F(7, 8)
rep(ok, "(8a) leading coefficients kappa: " + "; ".join(f"{k}: {v} = {float(v):.4f}" for k, v in kap.items())
    + ". All lie in [1/2, 1): none contradicts the prime ideal theorem (kappa >= 1/2), all leave a gap below 1.")
# Guo's q-coefficient and the algebra of (3.11): log b0 + lambda (2 log p0 - log b0) at lambda = 1/30,
# log b0 = (1/2) log p0 + (1/2) log q + log 2
lam = F(1, 30)
cp0 = (1 - lam) * F(1, 2) + 2 * lam
cq = (1 - lam) * F(1, 2)
c2 = (1 - lam)
rep(cp0 == F(11, 20) and cq == F(29, 60) and c2 == F(29, 30),
    f"(8a) Guo (3.11) coefficients recomputed: log p0: {cp0}, log q: {cq}, log 2: {c2}")

# ---------------------------------------------------------------- (8b)
C1 = 2 * mp.e ** 1.5 / 9
C2 = mp.e ** 1.5 / 4
K = C2 + mp.mpf(8) / 5
c = mp.mpf(3) / 16
dstar = c ** 2 / (4 * C1 * K)
Astar = 2 * K / c
omega_star = 0.75 * Astar
delta0 = mp.mpf(81) / (5888 * mp.e ** 1.5)
delta0_exact_omega = mp.mpf(9) / (128 * 22 * C1)   # using log M = (4/3) omega L exactly (N = q^omega)
rep(delta0 < delta0_exact_omega < dstar,
    f"(8b) Banks (7.3) as a generic chain: continuous optimum delta* = (3/16)^2/(4 C1 (C2+8/5)) = {float(dstar):.6f} "
    f"at log M/L = {float(Astar):.2f} (omega* = {float(omega_star):.2f}; Banks takes omega = 22); with omega = 22 and "
    f"log M = (4/3) omega L exactly (N = q^omega is an integer power) one gets 9/(128*22*C1) = "
    f"{float(delta0_exact_omega):.6f}; Banks states 81/(5888 e^1.5) = {float(delta0):.6f} using the slack (omega+1). "
    f"Banks's constant is {float(100 * (1 - delta0 / dstar)):.1f}% below the continuous relaxation of his own chain "
    f"(part 1: 1.3% below the integer-omega optimum 3.108e-3).")


def guo_asym(A, B):
    # large-q limit of Guo's chain: ((9/20)A - B - 29/60) <= (delta/2)(AB + A^2/2), plus cap delta (A+B) <= 1
    num = 2 * (F(9, 20) * A - B - F(29, 60))
    den = A * B + A * A / 2
    return min(num / den, F(1) / (A + B))


def guo_asym_f(A, B):
    return min(2 * (0.45 * A - B - 29 / 60) / (A * B + A * A / 2), 1 / (A + B))


best = max(((guo_asym_f(a / 8, 2 + b / 2000), a / 8, 2 + b / 2000) for a in range(80, 400) for b in range(1, 400)),
           key=lambda t: t[0])
best = (F(best[0]).limit_denominator(10 ** 9), best[1], best[2])
rep(abs(float(best[0]) - 0.0609) < 0.001,
    f"(8b) Guo's chain as q -> infinity (B > 2 so that B(y) = O(q^{{1-B/2}}) -> 0): sup over (A,B) of "
    f"min(2((9/20)A - B - 29/60)/(AB + A^2/2), 1/(A+B)) = {float(best[0]):.5f} at (A,B) = ({best[1]}, {best[2]}) "
    f"(part 1 found 0.06095). Same closed form: (1-kappa)^2 = (9/20)^2 = {float(F(81, 400)):.4f} versus "
    f"(3/16)^2 = {float(F(9, 256)):.4f} for Banks: a factor {float(F(81, 400) / F(9, 256)):.2f} from kappa alone.")
info("(8b) delta* scales like (1-kappa)^2: the ordering Guo (11/20) > Kimura > Banks (13/16 effective) of the "
     "asymptotic constants is explained by the arithmetic exponent plus the analytic constants; the stated "
     "values (Guo 1/100 at q=3 by his fixed (A,B), Banks 3.07e-3 for q >= 1e10) are lower bounds for the same "
     "quantity and are mutually consistent")

# ---------------------------------------------------------------- (8c)
E_RS = -1.332582275733221
logq_coeff = F(29, 60) / F(9, 20)
rep(logq_coeff == F(29, 27),
    "(8c) Guo (3.1) + Rosser-Schoenfeld: if all odd primes <= x are inert, then (9/20) log x <= (29/60) log q + "
    f"6 + 1.333 + (log 2)/2 + 1/(2 log x), i.e. log p1 <= (29/27) log q + {float((6 + 1.3326 + math.log(2) / 2 + 0.5) / 0.45):.1f}; "
    "the exponent 29/27 > 1 is weaker than the trivial p1 <= (least prime factor of q) <= q, so the q-aspect is "
    "not 'too strong'; the strength of (3.1) is entirely in the x-slope 11/20 < 1")


def kron(D, n):
    return sp.kronecker_symbol(D, n)


def fundamental(D):
    if D % 4 == 1:
        return sp.factorint(abs(D)) and all(e == 1 for e in sp.factorint(abs(D)).values()) or abs(D) == 1
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and all(e == 1 for e in sp.factorint(abs(m)).values())
    return False


plist = list(sp.primerange(2, 2000))
worst = (0, None, None)
count = 0
for absD in range(10 ** 4, 200001):
    for D in (absD, -absD):
        if D == 1 or not fundamental(D):
            continue
        count += 1
        for p in plist:
            if kron(D, p) != -1:
                ratio = math.log(p) / math.log(absD)
                if ratio > worst[0]:
                    worst = (ratio, D, p)
                break
rep(worst[0] < 29 / 27, f"(8c) data: over {count} fundamental discriminants 1e4 <= |D| <= 2e5, the least prime p1 "
    f"with chi(p1) != -1 (split or ramified) satisfies log p1/log q <= {worst[0]:.3f} (max at D={worst[1]}, "
    f"p1={worst[2]}), far inside Guo's explicit 29/27 (+18.2/log q) and below the asymptotic 1/2 of the Barreto "
    f"shape (whose constants are not explicit, so only the order of magnitude is compared)")

# ---------------------------------------------------------------- (9a)
H_banks = 9216 * 97 ** 2
C0, c0 = 192, F(1, 4 * 97 ** 2)
ok = H_banks == 12 * C0 / c0 and F(int(C0 / c0), H_banks) == F(1, 12)
q0 = 10 ** 10
omega = 22
N0 = q0 ** omega
U0_log = F(4, 3) * omega * math.log(q0)
ok &= 319 <= H_banks <= q0 <= N0 and U0_log > math.log(8)
ok &= (H_banks ** (2 / 3)) >= 4 * 97 ** 2 and H_banks >= 8 * 97 ** 3
# identity defining delta0: 3/16 = (4/3)(omega+1) C1 delta0 + 3/32
lhs = mp.mpf(3) / 16
rhs = mp.mpf(4) / 3 * (omega + 1) * C1 * delta0 + mp.mpf(3) / 32
ok &= abs(lhs - rhs) < mp.mpf(10) ** -25
ok &= 3 * (C2 + mp.mpf(8) / 5) / (4 * omega) <= mp.mpf(3) / 32
rep(ok, f"(9a) Banks/OAI parameters: H = 9216*97^2 = {H_banks} = 12 C0/c0 (so (C0/c0)/H = 1/12); H >= 8*97^3 "
    "gives H^(2/3) >= 4*97^2; 319 <= H <= q0 = 1e10 <= N = q^22; M >= 8; delta0 solves 3/16 = (4/3)(omega+1) C1 delta0 "
    "+ 3/32 to 25 digits; 3(C2+8/5)/(4 omega) <= 3/32 iff omega >= 8(C2+8/5) = "
    f"{float(8 * (C2 + mp.mpf(8) / 5)):.4f}")
info("(9a) OAI's argument needs N >= H, U >= 3 and H^(2/3) N^(4/3) >= 2*97^2 'eventually'; with the explicit H these "
     "hold as soon as q^gamma >= 8.7e7. Banks's q0 = 1e10 is forced by his constant bookkeeping (L > 23), not by "
     "the method; below q0 his all-q constant needs LZZ (U3) - or, if Guo's Theorem 1.1 is accepted, Guo's 1/100 "
     "> 3.0e-3 for every q >= 3 makes the LZZ input unnecessary for the statement 'c = 3.0e-3 for all q'")

# ---------------------------------------------------------------- (9b) Guo uniformity in q at delta = 1/100


def guo_margin(q, delta=mp.mpf(1) / 100, A=70, Bexp=6):
    q = mp.mpf(q)
    lq = mp.log(q)
    eps = delta / lq
    kappa = (A * Bexp + mp.mpf(A) ** 2 / 2) * lq ** 2
    Bf = lambda t_log: (q + 1 + t_log / 2) * mp.e ** (-t_log / 2)
    By = Bf(Bexp * lq)
    Bxy = Bf((A + Bexp) * lq)
    E = By * (eps * kappa + Bexp * lq) + Bxy * (A + Bexp) * lq + 2 * By + 2 * mp.e ** (-Bexp * lq / 2)
    # H1(y) >= sum_{m <= sqrt y} 1/m^2
    msq = int(mp.floor(mp.e ** (Bexp * lq / 2) + mp.mpf('1e-9')))
    H1 = mp.zeta(2) - mp.zeta(2, msq + 1) if msq < 10 ** 7 else mp.zeta(2) - 1 / mp.mpf(msq)
    J = eps * kappa + E / H1
    lower = (A - Bexp) * lq - 2 - J / 2
    upper = (mp.mpf(11) / 20 * A + mp.mpf(29) / 60) * lq + 6
    return lower - upper


grid = sorted(set([3, 4, 5, 7, 8, 11, 12, 13] + [int(10 ** (k / 4)) for k in range(2, 61)]))
margins = [(q, guo_margin(q)) for q in grid]
mn = min(margins, key=lambda t: t[1])
rep(all(m > 0 for _, m in margins) and mn[0] == 3,
    f"(9b) Guo's chain at delta = 1/100 with (x,y) = (q^70, q^6), exact logs: contradiction margin > 0 on "
    f"{len(grid)} conductors in [3, 1e15]; minimum {float(mn[1]):.4f} at q = {mn[0]} (paper's rational version: "
    f"(451/60) log 3 - 8 = {451 / 60 * math.log(3) - 8:.4f}, slightly smaller because of rounded certificates); "
    f"margin at 1e15: {float(margins[-1][1]):.1f}")
# the parameter conditions of Lemma 5.1 for every q >= 3
okc = all((mp.mpf(76) / 100 < 1) and (mp.mpf(q) ** 6 >= max(q, 100)) for q in grid)
rep(okc, "(9b) Lemma 5.1 hypotheses for every q >= 3: eps log(xy) = 76 delta <= 0.76 < 1, y = q^6 >= max(q, 100), "
    "beta > 1/2; Prop 3.1 needs nothing")

# ---------------------------------------------------------------- (9c) small conductors, L(sigma, chi_D) > 0


def chi_table(D):
    q = abs(D)
    return np.array([int(sp.kronecker_symbol(D, n)) for n in range(1, q + 1)], dtype=np.float64)


def L_values(D, sigmas, Kp=20):
    q = abs(D)
    ch = chi_table(D)  # chi(1..q)
    n = np.arange(1, Kp * q + 1, dtype=np.float64)
    chn = np.tile(ch, Kp)
    a = np.arange(1, q + 1, dtype=np.float64)
    X = Kp * q + a
    vals = []
    for s in sigmas:
        head = np.sum(chn * n ** (-s))
        if abs(s - 1) < 1e-12:
            integ = -np.sum(ch * np.log(X)) / q
        else:
            integ = np.sum(ch * X ** (1 - s)) / (q * (s - 1))
        t = integ + np.sum(ch * (0.5 * X ** (-s) + s * q * X ** (-s - 1) / 12
                                 - s * (s + 1) * (s + 2) * q ** 3 * X ** (-s - 3) / 720))
        vals.append(head + t)
    return vals


# validation against mpmath.dirichlet
val_err = 0.0
for D in (-3, -4, 5, 8, -163, 1009, -2999):
    q = abs(D)
    chl = [int(sp.kronecker_symbol(D, k)) for k in range(q)]
    for s in (0.5, 0.8, 1.0):
        if s == 1.0:   # exact: L(1,chi) = -(1/q) sum_a chi(a) digamma(a/q)  (mpmath.dirichlet is unstable at s = 1)
            ref = -mp.fsum(chl[a] * mp.digamma(mp.mpf(a) / q) for a in range(1, q)) / q
        else:
            ref = mp.dirichlet(s, chl)
        val_err = max(val_err, abs(float(ref) - L_values(D, [s])[0]))
rep(val_err < 1e-8, f"(9c) Euler-Maclaurin accelerated L(sigma, chi) agrees with mpmath.dirichlet to {val_err:.1e} "
    "(7 characters x sigma in {0.5, 0.8}; at sigma = 1 against the digamma formula)")
minval = (1e9, None, None)
nD = 0
for absD in range(3, DMAX + 1):
    for D in (absD, -absD):
        if not fundamental(D):
            continue
        nD += 1
        lq = math.log(absD)
        sig = [0.5 + 0.025 * k for k in range(20)] + [1 - 1 / (5 * lq), 1 - 1 / (100 * lq), 1.0]
        v = L_values(D, sig)
        m = min(v)
        if m < minval[0]:
            minval = (m, D, sig[v.index(m)])
rep(minval[0] > 0, f"(9c) uncertified: for all {nD} fundamental discriminants 3 <= |D| <= {DMAX}, L(sigma, chi_D) > 0 at "
    f"23 grid points in [1/2, 1] (including 1 - 1/(5 log q) and 1 - 1/(100 log q)); min value {minval[0]:.4f} at "
    f"D = {minval[1]}, sigma = {minval[2]:.3f}. Includes D = 8 (the field all four papers exclude from the "
    "construction). Consistent with every stated constant; not a certificate (grid only).")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")

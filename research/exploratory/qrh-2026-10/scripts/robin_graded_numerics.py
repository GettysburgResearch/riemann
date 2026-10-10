#!/usr/bin/env python3
"""EMPIRICAL sanity check for ROBIN_GRADED.md (QRH research wave, October 2026).

What it computes (floating point; NOT directed, NOT certified):
  1. Self-test: enumerates colossally abundant (CA) numbers from the critical-epsilon
     description and compares the first terms with the published list (OEIS A004490).
  2. At the first CA number N with largest prime p, for p on a grid up to PMAX:
        Z_CA(p) = (log f(N) - gamma) * sqrt(p) * log(p),  f(N) = sigma(N)/(N log log N).
     Under RH (Ramanujan/Robin) Z_CA should tend to lie in [-(2*sqrt2-2)-beta, -(2*sqrt2-2)+beta].
  3. At the primorial N_k with p = p_k:
        Z_P(p) = (log(N_k/phi(N_k)) - gamma - log log log N_k) * sqrt(p) * log(p).
     Under RH (Nicolas 1983/2012) Z_P should tend to lie in [2-beta, 2+beta].
  4. The QRH-conditional envelope of ROBIN_GRADED.md, in the same normalisation:
        E(p) = C * p^(theta-1) / log p * sqrt(p) * log p = C * p^(theta-1/2),  theta = 7/8,
     with C_crude = 17 * 0.0465 (Lemma K) and C_refined = 0.0465 (Remark K').
  5. (optional, --psi1) a small check of Ingham's absolutely convergent explicit formula
     for psi_1(x) = int_0^x psi(t) dt with the first few hundred zeros (mpmath).

Scope: finite floating-point evidence about the *size* of f at CA numbers and primorials.
It proves nothing, and in particular it neither tests nor supports QRH-IMPORT or RH.
Arithmetic class: IEEE double / x87 long double sums; no rounding contract.
Run: nice -n 10 python3 robin_graded_numerics.py [--pmax 1e8] [--psi1]
"""
import argparse
import math
import sys

import numpy as np

GAMMA = 0.57721566490153286061
BETA = 2.0 + GAMMA - math.log(4.0 * math.pi)  # sum_rho 1/(rho(1-rho)) = 0.0461914179...
RAM = 2.0 * math.sqrt(2.0) - 2.0             # 0.8284..., Ramanujan's structural CA constant
SUM_RHO_BOUND = 0.0465                       # unconditional bound for sum 1/|rho|^2 (ROBIN_GRADED Sec. 3)
THETA = 7.0 / 8.0


def sieve(n):
    """Primes <= n (odd-only sieve)."""
    n = int(n)
    if n < 2:
        return np.zeros(0, dtype=np.int64)
    m = (n - 1) // 2  # index i <-> 2i+1, i>=1
    s = np.ones(m + 1, dtype=bool)
    s[0] = False
    r = int(math.isqrt(n))
    for i in range(1, (r - 1) // 2 + 1):
        if s[i]:
            p = 2 * i + 1
            s[(p * p - 1) // 2::p] = False
    odd = 2 * np.nonzero(s)[0] + 1
    return np.concatenate(([2], odd)).astype(np.int64)


def ca_exponent(p, eps, rmax=200):
    """Exponent of prime p in the CA number of parameter eps (Alaoglu-Erdos criterion):
    a_p >= r  iff  eps*log p <= log((1-p^{-r-1})/(1-p^{-r}))."""
    lp = math.log(p)
    a = 0
    for r in range(1, rmax):
        crit = math.log1p(-p ** (-(r + 1))) - math.log1p(-p ** (-r))
        if eps * lp <= crit:
            a = r
        else:
            break
    return a


def ca_critical(p, r):
    """Critical epsilon at which the exponent of p rises from r-1 to r."""
    return (math.log1p(-p ** (-(r + 1))) - math.log1p(-p ** (-r))) / math.log(p)


def selftest_ca():
    """Enumerate CA numbers via sorted critical epsilons; compare with OEIS A004490 head."""
    known = [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720, 1441440, 4324320,
             21621600, 367567200, 6983776800, 160626866400, 321253732800,
             9316358251200, 288807105787200, 2021649740510400]
    ps = [int(q) for q in sieve(100)]
    crit = sorted({ca_critical(p, r) for p in ps for r in range(1, 12)}, reverse=True)
    out = []
    for i in range(len(crit) - 1):
        eps = 0.5 * (crit[i] + crit[i + 1])
        n = 1
        for p in ps:
            a = ca_exponent(p, eps)
            if a == 0:
                break
            n *= p ** a
        if not out or n != out[-1]:
            out.append(n)
        if len(out) >= len(known):
            break
    ok = out[:len(known)] == known
    return ok, out[:len(known)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmax", type=float, default=1e8)
    ap.add_argument("--psi1", action="store_true")
    args = ap.parse_args()

    ok, got = selftest_ca()
    print(f"[selftest] CA enumeration matches OEIS A004490 head (20 terms): {ok}")
    if not ok:
        print("  got:", got)
        sys.exit(1)

    P = sieve(args.pmax)
    pf = P.astype(np.float64)
    print(f"[sieve] {len(P)} primes <= {args.pmax:.3g}")
    # cumulative sums in long double
    mert = np.cumsum((-np.log1p(-1.0 / pf)).astype(np.longdouble))   # sum_{p<=x} -log(1-1/p)
    theta = np.cumsum(np.log(pf).astype(np.longdouble))              # theta(x)

    # grid of indices: primes nearest to 10^{3}, 10^{3.25}, ..., up to pmax
    exps = np.arange(3.0, math.log10(args.pmax) + 1e-9, 0.25)
    rows = []
    for e in exps:
        k = int(np.searchsorted(P, 10.0 ** e, side="right")) - 1
        p = int(P[k])
        lp = math.log(p)
        scale = math.sqrt(p) * lp
        # --- primorial N_k
        logNk = float(theta[k])
        logfphi = float(mert[k]) - GAMMA - math.log(math.log(logNk))
        ZP = logfphi * scale
        # --- first CA number with largest prime p: eps just below the critical value of p
        eps = ca_critical(p, 1) * (1.0 - 1e-13)
        # primes with exponent >= 2 satisfy p <= x_2 ~ sqrt(2 p log p / log p) small; handle explicitly
        small = P[: int(np.searchsorted(P, max(3, int(10 * math.sqrt(p))), side="right"))]
        extra_logN = 0.0
        extra_logsig = 0.0
        a_small = [ca_exponent(int(q), eps) for q in small]
        for q, a in zip(small, a_small):
            q = float(q)
            if a >= 2:
                extra_logN += (a - 1) * math.log(q)
                # log((1-q^{-a-1})/(1-q^{-2})) : the part beyond exponent 1
                extra_logsig += math.log1p(-q ** (-(a + 1))) - math.log1p(-q ** (-2))
        # check that the last small prime has exponent 1 and that p itself has exponent 1
        assert a_small[-1] <= 1 and ca_exponent(p, eps) == 1
        # exponent-1 part over all primes <= p: log prod (1-q^{-2})/(1-q^{-1})
        lsig1 = float(mert[k]) + float(np.sum(np.log1p(-1.0 / pf[: k + 1] ** 2)))
        logN = logNk + extra_logN
        logsig = lsig1 + extra_logsig
        logf = logsig - math.log(math.log(logN)) - GAMMA
        ZCA = logf * scale
        Ecrude = 17 * SUM_RHO_BOUND * p ** (THETA - 0.5)
        Eref = SUM_RHO_BOUND * p ** (THETA - 0.5)
        rows.append((p, logNk, ZP, logN, ZCA, Eref, Ecrude))

    print()
    print("Normalisation: Z = (log f - gamma) * sqrt(p) * log p ; envelope E = C p^(7/8-1/2)")
    print(f"RH bands (asymptotic): Z_P in [2-b, 2+b] = [{2-BETA:.4f}, {2+BETA:.4f}];"
          f" Z_CA in [-(2r2-2)-b, -(2r2-2)+b] = [{-RAM-BETA:.4f}, {-RAM+BETA:.4f}]")
    print(f"{'p':>11} {'logN_k':>12} {'Z_P':>9} {'logN_CA':>12} {'Z_CA':>9} {'E_ref':>9} {'E_crude':>9}")
    for (p, lNk, ZP, lN, ZCA, Er, Ec) in rows:
        print(f"{p:>11d} {lNk:>12.1f} {ZP:>9.4f} {lN:>12.1f} {ZCA:>9.4f} {Er:>9.3f} {Ec:>9.3f}")

    if args.psi1:
        import mpmath as mp
        mp.mp.dps = 20
        M = 300
        zs = [mp.zetazero(j) for j in range(1, M + 1)]
        T = float(zs[-1].imag)
        print(f"\n[psi1] Ingham explicit formula check with {M} zero pairs (T = {T:.1f})")
        Pp = sieve(200)
        for x in (20.5, 50.5, 100.5):
            # psi_1(x) = sum_{n<=x} Lambda(n) (x-n)
            s = 0.0
            for q in Pp:
                q = int(q)
                if q > x:
                    break
                qq = q
                while qq <= x:
                    s += math.log(q) * (x - qq)
                    qq *= q
            zsum = 0.0
            for z in zs:
                zsum += 2 * float(mp.re(mp.power(x, z + 1) / (z * (z + 1))))
            # zeta'(-1)/zeta(-1) via mpmath
            c1 = float(mp.diff(mp.zeta, -1) / mp.zeta(-1))
            tail = sum(x ** (1 - 2 * r) / (2 * r * (2 * r - 1)) for r in range(1, 60))
            rhs = x * x / 2 - zsum - x * math.log(2 * math.pi) + c1 - tail
            tb = 2 * x ** 1.5 * (math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
            print(f"  x={x:6.1f}  psi_1 exact={s:12.4f}  formula={rhs:12.4f}  diff={s-rhs:+.4f}"
                  f"  (zero-tail bound ~{tb:.3f})")


if __name__ == "__main__":
    main()

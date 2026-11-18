"""CRIT23 Level-2 audit, part 1: step S2 of Alpoge-Furman arXiv:2608.13637v2.

(A) Lemma 2.1 (Poisson-Gabor identity) for the ACTUAL AF test function phi (C^infinity chi, both windows) at
    complex z, z' with |Im| < 1/2:  sum_k phihat(z-a_k) phihat(z'-a_k) = L (phi^2)^(z-z'),  a_k = T0 + 2 pi k/L.
    Also: the BILINEAR trace sum_k phihat(z-a_k)^2 = a L^2 for complex z (exact "trace m" for off-line zeros),
    whereas the SESQUILINEAR sum_k |phihat(z-a_k)|^2 = L int phi^2 e^{2uy} > a L^2 (y = Im z).
(B) The explicit formula (2.2)/(2.11) in AF's exact normalisation, tested against the first 100,000 zeta zeros
    (Arb-certified table EXP-0001): sum_rho F^(gamma_rho) = int F^(tau) nu_X(tau) dtau for
    F^(tau) = phihat(tau-al) phihat(tau-al'), supp F in [-log X, log X], including NON-EVEN F (al != 0) -- the case
    AF actually use in (2.11) although (2.1) is stated for even F (finding F3). The literal (2.1) with the one-sided
    prime sum -2 sum Lambda(n)/sqrt(n) F(log n) is also evaluated, to show it is only right for even F.
    One case is literally an entry of AF's G~+E~ at T = 2 pi X (X = 50): al = alpha_k, al' = alpha_k'.

Non-rigorous floating point (the zero ordinates are certified to 1e-20, the quadratures are not).
Run: python3 -I s2_gabor_explicit_formula.py"""
import sys, os, gzip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.special import psi as digamma
from af_testfn import TestFunction

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.join(HERE, "..", "..", "..", "results", "zeros", "zeta_zeros_1_100000_arb.tsv.gz")


def part_A(out):
    out.append("=" * 100)
    out.append("PART A. AF Lemma 2.1 with the actual C^2 (here C^inf) taper, complex arguments")
    out.append("=" * 100)
    rng = np.random.default_rng(7)
    for window in ("flat", "MT"):
        for L in (5.0, 7.0):
            tf = TestFunction(L, window, zmax=480.0)
            h = 2 * np.pi / L
            T0 = 37.3
            K = int(np.ceil(460 / h))
            for trial in range(4):
                c = rng.uniform(-3, 3)
                z = c + rng.uniform(-2, 2) + 1j * rng.uniform(-0.49, 0.49)
                zp = c + rng.uniform(-2, 2) + 1j * rng.uniform(-0.49, 0.49)
                ks = np.arange(-K, K + 1)
                # centre the lattice near the points to keep |z - a_k| <= 460 over the summed range
                k0 = int(round((np.real(z) - T0) / h))
                al = T0 + h * (ks + k0)
                lhs = np.sum(tf.hat(z - al) * tf.hat(zp - al))
                rhs = L * tf.hat_phi2(np.array([z - zp]))[0]
                bil = np.sum(tf.hat(z - al) ** 2)
                ses = np.sum(np.abs(tf.hat(z - al)) ** 2)
                ses_pred = L * tf.hat_phi2(np.array([2j * np.imag(z)]))[0].real
                out.append(f"  {window:4s} L={L} z={z:.3f} z'={zp:.3f}: |lhs-rhs|={abs(lhs-rhs):.1e} (|rhs|={abs(rhs):.3f}); "
                           f"bilinear sum/aL^2 = {bil/(tf.a*L*L):.12f}; sesquilinear sum/aL^2 = {ses/(tf.a*L*L):.6f} "
                           f"(pred {ses_pred/(tf.a*L*L):.6f})")


def load_zeros(gmax):
    g = []
    with gzip.open(ZEROS, "rt") as f:
        for line in f:
            n, mid, rad = line.split("\t")
            x = float(mid)
            if x > gmax:
                break
            g.append(x)
    return np.array(g)


def von_mangoldt_terms(X):
    """list of (n, Lambda(n)) for prime powers n <= X."""
    n = int(np.floor(X))
    sieve = np.ones(n + 1, dtype=bool); sieve[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    res = []
    for p in np.nonzero(sieve)[0]:
        q = p
        while q <= n:
            res.append((int(q), float(np.log(p))))
            q *= p
    return sorted(res)


def gl_nodes(a, b, panel=0.2, k=20):
    x, w = np.polynomial.legendre.leggauss(k)
    edges = np.arange(a, b + panel, panel)
    xs = (0.5 * (edges[1:] - edges[:-1])[:, None] * x[None, :] + 0.5 * (edges[1:] + edges[:-1])[:, None]).ravel()
    ws = (0.5 * (edges[1:] - edges[:-1])[:, None] * w[None, :]).ravel()
    return xs, ws


def part_B(out):
    out.append("=" * 100)
    out.append("PART B. Explicit formula (2.2) in AF's normalisation vs the first zeta zeros (Arb table)")
    out.append("=" * 100)
    X = 50.0
    L = np.log(X)
    T = 2 * np.pi * X
    h = 2 * np.pi / L
    W = 420.0                       # |phihat(x)| < 1e-12 for |x| > ~320 (checked in af_testfn validation)
    zeros = load_zeros(2000.0)
    pp = von_mangoldt_terms(X)
    for window in ("flat", "MT"):
        tf = TestFunction(L, window, zmax=W + 60)
        a = tf.a
        cases = [("even F (al=al'=0)", 0.0, 0.0),
                 ("non-even F (al=al'=30)", 30.0, 30.0),
                 ("non-even complex F (al=30, al'=31.7)", 30.0, 31.7),
                 (f"AF entry (G~+E~)_kk' at T=2piX={T:.2f}: k=10,k'=11", T + 10 * h, T + 11 * h),
                 (f"AF diagonal entry k=k'=20 at T={T:.2f}", T + 20 * h, T + 20 * h)]
        for (lab, al, alp) in cases:
            # zero side: gamma_rho = +-gamma_n (all zeros in this range are simple and on the line)
            gam = np.concatenate([zeros, -zeros])
            sel = (np.abs(gam - al) < W) | (np.abs(gam - alp) < W)
            Fz = tf.hat_real(gam[sel] - al) * tf.hat_real(gam[sel] - alp)
            zero_side = np.sum(Fz)
            # prime/archimedean side: numerical integral of F^ nu_X over a window covering the support of F^
            lo = min(al, alp) - W; hi = max(al, alp) + W
            if al == 0.0:
                lo, hi = -W, W
            tau, wt = gl_nodes(lo, hi)
            Fh = tf.hat_real(tau - al) * tf.hat_real(tau - alp)
            mu = digamma(0.25 + 0.5j * tau).real / (2 * np.pi) - np.log(np.pi) / (2 * np.pi)
            g = X ** (0.5 + 1j * tau) / (0.5 + 1j * tau)
            Pi = g.real / np.pi
            PX = np.zeros_like(tau)
            for (n, lam) in pp:
                PX -= lam / np.sqrt(n) * np.cos(tau * np.log(n)) / np.pi
            I_mu = np.sum(wt * Fh * mu); I_Pi = np.sum(wt * Fh * Pi); I_P = np.sum(wt * Fh * PX)
            prime_side = I_mu + I_Pi + I_P
            # analytic pieces: int F^ Pi_X = F^(i/2) + F^(-i/2);  int F^ P_X = -sum Lambda/sqrt n (F(log n) + F(-log n))
            Fhat_pm = tf.hat(np.array([0.5j - al, -0.5j - al])) * tf.hat(np.array([0.5j - alp, -0.5j - alp]))
            pole = Fhat_pm.sum()
            logs = np.array([np.log(n) for (n, _) in pp]); lams = np.array([lam for (_, lam) in pp]); ns = np.array([n for (n, _) in pp])
            Fp = tf.F_of_x(logs, al, alp); Fm = tf.F_of_x(-logs, al, alp)
            prime_two_sided = -np.sum(lams / np.sqrt(ns) * (Fp + Fm))
            prime_literal_21 = -2 * np.sum(lams / np.sqrt(ns) * Fp)        # AF (2.1) applied literally
            rhs_21_literal = pole + I_mu + prime_literal_21
            out.append(f"  [{window}] {lab}")
            out.append(f"      zero side  sum_rho F^(gamma_rho)            = {zero_side:.12f}")
            out.append(f"      (2.2) int F^ nu_X (numerical quadrature)    = {prime_side:.12f}   diff = {abs(zero_side-prime_side):.1e}")
            out.append(f"        pieces: int F^ mu = {I_mu:.10f}; int F^ Pi_X = {I_Pi:.10f} vs F^(i/2)+F^(-i/2) = {pole.real:.10f}{pole.imag:+.1e}i; "
                       f"int F^ P_X = {I_P:.10f} vs -sum Lam/sqrt(n)(F(log n)+F(-log n)) = {prime_two_sided.real:.10f}{prime_two_sided.imag:+.1e}i")
            out.append(f"      (2.1) applied literally (one-sided prime sum) = {rhs_21_literal.real:.10f}{rhs_21_literal.imag:+.3e}i   "
                       f"diff from zero side = {abs(zero_side - rhs_21_literal):.2e}")
            if "AF" in lab:
                out.append(f"      => (G~+E~)_kk' = {zero_side/(a*L*L):.12f} (zero side) vs {prime_side/(a*L*L):.12f} (prime side, eq. 2.11)")


if __name__ == "__main__":
    out = []
    part_A(out)
    part_B(out)
    print("\n".join(out))

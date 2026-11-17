"""CRIT23 Level-2 audit, part 2, step S6: end-to-end NORMALISATION check of the second-moment evaluations on actual
zeta zeros (first 100000 zeros, Arb table, gamma <= 74920.8; all are simple and on the line, so this exercises only
the on-line case and says nothing about the off-line robustness that is the new content of AF/LZ).

(A) Alpoge-Furman normalisation, I = [T, 2T), L = log(T/2pi), X = T/2pi, phi as in AF (2.7) with a C^inf taper chi:
    zero side   Z  = sum_{gamma, gamma' in I} Phi(gamma - gamma')^2 / (a^2 L^2)         (K ~ L Phi, Lemma 2.1)
    prime side  M  = iint_{I x I} Phi(tau - tau')^2 nu_X(tau) nu_X(tau') / (a^2 L^2)  (full, numerical, all terms)
    main terms  Mm = [2 pi b L int_I mu^2 + (T/pi) sum_{n<=X} Lambda(n)^2/n g(log n)] / (a^2 L^2)   (Props 5.3, 5.4)
    and the asymptotic R(psi) N(T,2T).  Z = M up to edge effects (explicit formula); M - Mm = the terms AF bound by
    Props 5.2-5.5 (off-diagonal O_1, O_2, cross terms); Mm/N -> R(psi) at rate O(1/L) (taper, s8 part (c)).
(B) Lamzouri/BGSTB24 normalisation, all zeros with 0 < gamma <= T, L = log T:
    S_w = sum K_delta(z - z')^2 w,  S = sum K_delta(z - z')^2,  z = -gamma L/(2 pi), w = 4/(4 + (gamma-gamma')^2),
    compared with C_delta (T/2pi) log T and with C_delta N(T); also the classical Fejer case r = (1-|a|)_+ (r^ = sinc^2),
    whose BGSTB24/Montgomery constant is 4/3.

Non-rigorous floating point.  Finite-T numbers converge to the asymptotic constants only at rate O(1/log T).
Run: python3 -I s6_zero_side_data.py"""
import gzip
import os
import numpy as np
from scipy.special import psi as digamma
from scipy.signal import fftconvolve
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.join(HERE, "..", "..", "..", "results", "zeros", "zeta_zeros_1_100000_arb.tsv.gz")
SQ2 = np.sqrt(2.0)


def load_zeros():
    g = []
    with gzip.open(ZEROS, "rt") as f:
        for line in f:
            g.append(float(line.split("\t")[1]))
    return np.array(g)


def chi_np(t):
    t = np.asarray(t, dtype=float); out = np.zeros_like(t)
    m = (t > 0) & (t < 1); tm = t[m]
    a = np.exp(-1 / tm); b = np.exp(-1 / (1 - tm)); out[m] = a / (a + b); out[t >= 1] = 1.0
    return out


def gl(a, b, n=40, panels=1):
    xg, wg = np.polynomial.legendre.leggauss(n)
    edges = np.linspace(a, b, panels + 1)
    X = np.concatenate([(e1 - e0) / 2 * xg + (e1 + e0) / 2 for e0, e1 in zip(edges[:-1], edges[1:])])
    W = np.concatenate([(e1 - e0) / 2 * wg for e0, e1 in zip(edges[:-1], edges[1:])])
    return X, W


def mangoldt(nmax):
    lam = np.zeros(nmax + 1)
    for p in range(2, nmax + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            q = p
            while q <= nmax:
                lam[q] = np.log(p); q *= p
    return lam


def pair_sum(gam, fun, dmax):
    """sum over ordered pairs (i,j) with |gam_i - gam_j| <= dmax of fun(gam_i - gam_j, i, j); gam sorted."""
    tot = 0.0
    n = gam.size
    hi = np.searchsorted(gam, gam + dmax, side='right')
    maxoff = int((hi - np.arange(n)).max())
    for off in range(0, maxoff):
        i = np.arange(0, n - off)
        j = i + off
        ok = (gam[j] - gam[i]) <= dmax
        if not ok.any():
            break
        d = gam[j[ok]] - gam[i[ok]]
        v = fun(d)
        tot += v.sum() * (1 if off == 0 else 2)
    return tot


def part_A(gam, lam):
    print("(A) Alpoge-Furman normalisation on actual zeros")
    for window in ("flat", "MT"):
        sqpsi = (lambda s: np.ones_like(s)) if window == "flat" else (lambda s: np.sqrt(np.cos(SQ2 * s)))
        R = 4 / 3 if window == "flat" else 0.5 + 1 / (SQ2 * np.tan(1 / SQ2))
        for T in (5000.0, 15000.0, 30000.0):
            L = np.log(T / (2 * np.pi)); X = T / (2 * np.pi)
            Xa, Wa = gl(-L / 2, -L / 2 + 1, 40, 4); Xb, Wb = gl(-L / 2 + 1, L / 2 - 1, 40, 40); Xc, Wc = gl(L / 2 - 1, L / 2, 40, 4)
            U = np.concatenate([Xa, Xb, Xc]); Wu = np.concatenate([Wa, Wb, Wc])
            phi2_fn = lambda u: (chi_np(L / 2 + u) * chi_np(L / 2 - u) * sqpsi(np.clip(u / L, -0.5, 0.5))) ** 2
            phi2 = phi2_fn(U)
            a = np.sum(Wu * phi2) / L; b = np.sum(Wu * phi2 ** 2) / L
            xg = np.arange(0, 80.0001, 0.002)
            Phi = np.zeros(xg.size)
            for k0 in range(0, xg.size, 4000):
                Phi[k0:k0 + 4000] = np.cos(np.outer(xg[k0:k0 + 4000], U)) @ (Wu * phi2)
            spl = CubicSpline(xg, Phi)
            # zero side
            I = (gam >= T) & (gam < 2 * T)
            gI = gam[I]
            Z = pair_sum(gI, lambda d: spl(d) ** 2, 80.0) / (a * a * L * L)
            NI = gI.size
            # prime side, full: grid on I
            h = 0.02
            tau = np.arange(T, 2 * T, h) + h / 2           # midpoint rule
            mu = (1 / (2 * np.pi)) * np.real(digamma(0.25 + 0.5j * tau)) - np.log(np.pi) / (2 * np.pi)
            Pi = (1 / np.pi) * np.real(np.exp((0.5 + 1j * tau) * L) / (0.5 + 1j * tau))
            ns = np.nonzero(lam[:int(X) + 1])[0]
            an = lam[ns] / np.sqrt(ns); yn = np.log(ns)
            P = np.zeros(tau.size)
            for k0 in range(0, tau.size, 20000):
                P[k0:k0 + 20000] = -(1 / np.pi) * (np.cos(np.outer(tau[k0:k0 + 20000], yn)) @ an)
            nu = mu + Pi + P
            xk = np.arange(-40.0, 40.0 + h / 2, h)
            ker = spl(np.abs(xk)) ** 2
            conv = fftconvolve(nu, ker, mode='same') * h
            M = np.sum(nu * conv) * h / (a * a * L * L)
            convm = fftconvolve(mu, ker, mode='same') * h
            Mmumu = np.sum(mu * convm) * h / (a * a * L * L)
            # main terms (Props 5.3, 5.4): 2 pi b L int mu^2 + (T/pi) sum a_n^2 g(y_n)
            gvals = np.array([np.sum(Wu * phi2 * phi2_fn(U + y)) for y in yn])
            Mm = (2 * np.pi * b * L * np.sum(mu ** 2) * h + (T / np.pi) * np.sum(an ** 2 * gvals)) / (a * a * L * L)
            Nsmooth = T / (2 * np.pi) * (np.log(T / (2 * np.pi)) + 2 * np.log(2)) - T / (2 * np.pi)
            print(f"   {window:4s} T={T:7.0f} L={L:.3f} N(I)={NI} (smooth {Nsmooth:.0f}): Z/N = {Z/NI:.5f}, M/N = {M/NI:.5f},"
                  f" Mm/N = {Mm/NI:.5f}, M[mu,mu]-only/N = {Mmumu/NI:.5f}; R(psi) = {R:.5f}; (Z-M)/N = {(Z-M)/NI:+.2e}")


def part_B(gam):
    print("(B) Lamzouri / BGSTB24 normalisation (0 < gamma <= T, L = log T)")
    delta = 0.05
    Xa, Wa = gl(0, 0.5 - delta, 40, 20); Xb, Wb = gl(0.5 - delta, 0.5, 40, 10)
    X = np.concatenate([Xa, Xb]); W = np.concatenate([Wa, Wb])
    f0 = np.cos(SQ2 * X) / (SQ2 * np.sin(1 / SQ2))
    fd = chi_np((0.5 - X) / delta) ** 2 * f0
    fd /= 2 * np.sum(W * fd)
    Xs = np.concatenate([-X[::-1], X]); Ws = np.concatenate([W[::-1], W]); fs = np.concatenate([fd[::-1], fd])
    Cd = float(np.sum(Ws * fs * fs) + np.sum(np.abs(Xs[:, None] - Xs[None, :]) * (Ws * fs)[:, None] * (Ws * fs)[None, :]))
    ug = np.arange(0, 300.0001, 0.002)
    Kd = np.zeros(ug.size)
    for k0 in range(0, ug.size, 4000):
        Kd[k0:k0 + 4000] = 2 * (np.cos(2 * np.pi * np.outer(ug[k0:k0 + 4000], X)) @ (W * fd))
    splK = CubicSpline(ug, Kd)
    print(f"   window: MT with smooth taper delta={delta}: C_delta = {Cd:.6f};  |K_delta(u)| at u=50,150,300: "
          f"{abs(splK(50.0)):.1e}, {abs(splK(150.0)):.1e}, {abs(Kd[-1]):.1e}")
    for T in (10000.0, 30000.0, float(gam[-1])):
        g = gam[gam <= T]
        L = np.log(T); NT = g.size
        scale = L / (2 * np.pi)
        dmax = 300.0 / scale
        S = pair_sum(g, lambda d: splK(d * scale) ** 2, dmax)
        Sw = pair_sum(g, lambda d: splK(d * scale) ** 2 * 4 / (4 + d * d), dmax)
        main = T / (2 * np.pi) * L
        # Fejer: sinc^2 with weight, tail beyond U=300 corrected by ~ N/(pi^2 U) (average sin^2 = 1/2, density <= 1)
        sinc2 = lambda d: np.sinc(d * scale) ** 2 * 4 / (4 + d * d)
        Sf = pair_sum(g, sinc2, dmax) + NT / (np.pi ** 2 * 300.0)
        print(f"   T={T:8.1f}: N(T)={NT}, (T/2pi)logT={main:.0f} (ratio N/main = {NT/main:.4f});"
              f"  S_w/main = {Sw/main:.5f}, S/main = {S/main:.5f}, S/N = {S/NT:.5f}  [C_delta = {Cd:.5f}];"
              f"  Fejer S_w/main = {Sf/main:.5f}, /N = {Sf/NT:.5f}  [4/3]")


if __name__ == "__main__":
    gam = load_zeros()
    lam = mangoldt(5000)
    part_A(gam, lam)
    part_B(gam)

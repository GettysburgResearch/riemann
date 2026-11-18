"""CRIT23 Level-2 audit, part 2, step S7 (Lamzouri arXiv:2609.02882v2, Lemma 3.2 and (3.2)-(3.3): exact removal of
the BGSTB24 weight w(rho-rho') = 4/(4-(rho-rho')^2)), plus two checks on the imported BGSTB24 chain (arXiv:2306.04799v1).

(a) sympy: with Q^''(z) = (2 pi i z)^2 Q^(z) and r = Q - Q''/(4 log^2 T), one has r^(z) w(D) = K(z)^2 at
    z = i D log T/(2 pi) for every complex D = rho - rho' (no reality or RH assumption).
(b) numerics (numpy Gauss-Legendre, double precision): the same identity at complex z for off-line D, with a smooth window
    f_delta = psi_delta^2 f_0 / A_delta (Lamzouri's construction, MT profile, delta = 0.1).
(c) the Q''-term of Lemma 3.2: Q''(0) + 2 int_0^1 a Q''(a) da = Q''(0) + 2 Q(0) (integration by parts), a fixed number,
    so after the factor 1/(4 log^2 T) it contributes O(T / log T) = o(N).
(d) BGSTB24 Lemma 3: int dt / ((1+t^2)(1+(t+a)^2)) = 2 pi / (4 + a^2) for complex a, |Im a| < 1.
(e) BGSTB24 proof of Theorem 1: size of the error x^{1-2 eta(T log^2 T)} log^3 T at x = T relative to x, with
    Korobov-Vinogradov eta = c/((log t)^{2/3} (log log t)^{1/3}) versus the classical eta = c / log t
    (shows why the KV region, not just any zero-free region, is used; input-set note P2-F4).

Non-rigorous floating point (numpy double; mpmath 30 digits in (d),(e)).  Run: python3 -I s7_weight_removal.py"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 30


def part_a():
    z, Lg, D = sp.symbols('z Lg D')
    K = sp.Function('K')
    Qhat = K(z) ** 2
    Qpp_hat = (2 * sp.pi * sp.I * z) ** 2 * Qhat
    rhat = Qhat - Qpp_hat / (4 * Lg ** 2)
    w = 4 / (4 - D ** 2)
    expr = sp.simplify((rhat * w).subs(z, sp.I * D * Lg / (2 * sp.pi)) - Qhat.subs(z, sp.I * D * Lg / (2 * sp.pi)))
    print("(a) sympy: r^(z) w(D) - K(z)^2 at z = i D log T/(2 pi)  ->", expr)
    print("    and r^(z) = (1 + pi^2 z^2/log^2 T) K(z)^2:", sp.simplify(rhat - (1 + sp.pi ** 2 * z ** 2 / Lg ** 2) * Qhat))


import numpy as np

SQ2 = np.sqrt(2.0)
DELTA = 0.1


def chi_np(t):
    t = np.asarray(t, dtype=float); out = np.zeros_like(t)
    m = (t > 0) & (t < 1); tm = t[m]
    a = np.exp(-1 / tm); b = np.exp(-1 / (1 - tm)); out[m] = a / (a + b); out[t >= 1] = 1.0
    return out


def dchi_np(t):
    t = np.asarray(t, dtype=float); out = np.zeros_like(t)
    m = (t > 0) & (t < 1); tm = t[m]
    a = np.exp(-1 / tm); b = np.exp(-1 / (1 - tm))
    out[m] = a * b * (1 / tm ** 2 + 1 / (1 - tm) ** 2) / (a + b) ** 2
    return out


def gl(a, b, n=40, panels=1):
    x, w = np.polynomial.legendre.leggauss(n)
    edges = np.linspace(a, b, panels + 1)
    X = np.concatenate([(e1 - e0) / 2 * x + (e1 + e0) / 2 for e0, e1 in zip(edges[:-1], edges[1:])])
    W = np.concatenate([(e1 - e0) / 2 * w for e0, e1 in zip(edges[:-1], edges[1:])])
    return X, W


def f0_np(x):
    x = np.asarray(x, dtype=float)
    return np.where(np.abs(x) <= 0.5, np.cos(SQ2 * x) / (SQ2 * np.sin(1 / SQ2)), 0.0)


def f0p_np(x):
    x = np.asarray(x, dtype=float)
    return np.where(np.abs(x) <= 0.5, -SQ2 * np.sin(SQ2 * x) / (SQ2 * np.sin(1 / SQ2)), 0.0)


def psid(x):
    return chi_np((0.5 - np.abs(x)) / DELTA)


def psid_p(x):
    x = np.asarray(x, dtype=float)
    return dchi_np((0.5 - np.abs(x)) / DELTA) * (-np.sign(x)) / DELTA


XA, WA = gl(-0.5, 0.5, 40, 20)
A_delta = float(np.sum(WA * psid(XA) ** 2 * f0_np(XA)))


def fd(x):
    return psid(x) ** 2 * f0_np(x) / A_delta


def fdp(x):
    return (2 * psid(x) * psid_p(x) * f0_np(x) + psid(x) ** 2 * f0p_np(x)) / A_delta


def conv(f, g, a):
    """(f*g)(a) for an array of a in [0,1]; supports in [-1/2,1/2]."""
    out = np.zeros(a.size)
    for i, ai in enumerate(a):
        lo, hi = max(-0.5, ai - 0.5), min(0.5, ai + 0.5)
        if hi > lo:
            X, W = gl(lo, hi, 40, 8)
            out[i] = np.sum(W * f(X) * g(ai - X))
    return out


def part_b_c():
    XQ, WQ = gl(0.0, 1.0, 40, 16)
    Qv = conv(fd, fd, XQ); Qppv = conv(fdp, fdp, XQ)      # (f*f)'' = f'*f'
    XF, WF = gl(0.0, 0.5, 40, 10)
    print(f"(b) Lamzouri construction, delta = {DELTA}: A_delta = {A_delta:.15f}, int f_delta = {2*np.sum(WF*fd(XF)):.15f}")

    def hatQ(vals, z):
        return 2 * np.sum(WQ * vals * np.cos(2 * np.pi * z * XQ))

    def Khat(z):
        return 2 * np.sum(WF * fd(XF) * np.cos(2 * np.pi * z * XF))

    logT = np.log(1e6)
    worst = 0.0
    for D in (0.3 + 0.7j, -0.7 + 1.9j, 0.05 - 0.4j, 0.9 + 0.0j, -0.45 + 3.3j, 0.0 + 12.0j):
        z = 1j * D * logT / (2 * np.pi)
        K2 = Khat(z) ** 2
        rh = hatQ(Qv, z) - hatQ(Qppv, z) / (4 * logT ** 2)
        w = 4 / (4 - D ** 2)
        rel = abs(rh * w - K2) / abs(K2)
        worst = max(worst, rel)
        print(f"    D = rho-rho' = {D!s:>14s}: z = {z:.4f}, K(z)^2 = {K2:.6e}, |r^(z) w(D) - K(z)^2|/|K(z)^2| = {rel:.2e}")
    print(f"    max relative difference = {worst:.2e} (quadrature level)")
    q0 = conv(fd, fd, np.array([0.0]))[0]; qpp0 = conv(fdp, fdp, np.array([0.0]))[0]
    ibp = qpp0 + 2 * np.sum(WQ * XQ * Qppv)
    print(f"(c) Q(0) = {q0:.12f} (= int f_delta^2), Q''(0) = {qpp0:.10f};"
          f" Q''(0) + 2 int_0^1 a Q''(a) da = {ibp:.10f}  vs  Q''(0) + 2 Q(0) = {qpp0 + 2*q0:.10f}")
    Cdelta = q0 + 2 * np.sum(WQ * XQ * Qv)
    CMT = 0.5 + 1 / (SQ2 * np.tan(1 / SQ2))
    print(f"    C_delta = Q(0) + 2 int_0^1 a Q(a) da = {Cdelta:.12f}  (C_MT = {CMT:.12f}; C_delta - C_MT = {Cdelta - CMT:.3e},"
          f" >= 0 as CCLM optimality predicts)")


def part_d():
    print("(d) BGSTB24 Lemma 3 integral identity at complex a, |Im a| < 1 (breakpoints at the near-real poles t = -Re a):")
    for a in (mp.mpc('0.7', '0.3'), mp.mpc('-2.5', '-0.9'), mp.mpc('5', '0.99'), mp.mpc('0', '0.5'), mp.mpc('-1.3', '0.0')):
        pts = sorted(set([-mp.inf, -10, 0, 10, mp.inf, -mp.re(a) - 0.5, -mp.re(a), -mp.re(a) + 0.5]))
        lhs = mp.quad(lambda t: 1 / ((1 + t ** 2) * (1 + (t + a) ** 2)), pts, maxdegree=10)
        rhs = 2 * mp.pi / (4 + a ** 2)
        print(f"    a = {mp.nstr(a, 4):>12s}: |lhs - rhs| = {mp.nstr(abs(lhs - rhs), 3)}")


def part_e():
    print("(e) BGSTB24 Thm 1 proof, x = T: log(E/x) = -2 eta(T log^2 T) log T + 3 log log T, with l = log T")
    print("    (E/x must be O(1); it is, for large T, with Korobov-Vinogradov, and is ~ e^{-2c} log^3 T with eta = c/log t)")
    for c in (mp.mpf('0.05'), mp.mpf('0.5')):
        for k in (1, 2, 4, 6, 8, 10, 12, 15):
            l = mp.mpf(10) ** k
            logt = l + 2 * mp.log(l)
            eta_kv = c / (logt ** (mp.mpf(2) / 3) * mp.log(logt) ** (mp.mpf(1) / 3))
            eta_cl = c / logt
            lkv = -2 * eta_kv * l + 3 * mp.log(l)
            lcl = -2 * eta_cl * l + 3 * mp.log(l)
            print(f"    c={mp.nstr(c,2):>4s} log T=1e{k:<2d}: log(E/x) KV = {mp.nstr(lkv, 6):>12s}   classical = {mp.nstr(lcl, 6):>10s}")
    print("    -> classical: log(E/x) ~ 3 log log T - 2c -> +inf; KV: -> -inf (eventually, for any fixed c > 0).")


if __name__ == "__main__":
    part_a()
    part_b_c()
    part_d()
    part_e()

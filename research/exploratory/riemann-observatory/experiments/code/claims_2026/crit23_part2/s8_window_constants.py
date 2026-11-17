"""CRIT23 Level-2 audit, part 2, step S8 (window optimisation constants).

(a) sympy exact: R(psi0) = 4/3; C(f) for f = cos(sqrt2 x)/(sqrt2 sin(1/sqrt2)) on [-1/2,1/2] equals
    C_MT = 1/2 + cot(1/sqrt2)/sqrt2 (Lamzouri Lemma 3.2 / AF Lemma 5.6), symbolic, not just quadrature.
(b) Lamzouri's construction: C_delta = C(f_delta), f_delta = psi_delta^2 f0 / A_delta, tends to C_MT as delta -> 0
    (the limit step of Lemma 3.2), with C_delta >= C_MT throughout (consistent with CCLM17 Cor. 14).
(c) AF's T-dependent test function: the finite-L main-term ratio
       R_L := (b L^3 + 2 int_0^L y g(y) dy) / (a^2 L^3),  a = ||phi||_2^2/L, b = ||phi||_4^4/L, g = phi^2 * phi^2,
    tends to R(psi) as L -> infinity, at rate O(1/L) (the chi-taper of width 1 is 1/L of the window).
(d) Knausgard (3.1)/(eq:C): the closed form C(f) = 4/3 + 1/2 sum a_j^2 + pi^-2 sum((-1)^j a_j/j^2 - a_j^2/(4 j^2)) for
    f = 1 + sum a_j cos(2 pi j u), derived symbolically here (including the vanishing of all cross terms j != k),
    then evaluated for KN's three windows and compared with the stated rational upper bounds C_0, C_0', C_0''.
(e) Remark (LZ 2.2 / AF): C(f) >= 1 for every admissible f (any certificate needs C < 2 to be nontrivial); spot values.

Run: python3 -I s8_window_constants.py"""
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 30
SQ2 = np.sqrt(2.0)


def part_a():
    s, t, x = sp.symbols('s t x', real=True)
    R0 = sp.integrate(1, (s, -sp.Rational(1, 2), sp.Rational(1, 2))) + \
        sp.integrate(sp.integrate(sp.Abs(s - t), (s, -sp.Rational(1, 2), sp.Rational(1, 2))), (t, -sp.Rational(1, 2), sp.Rational(1, 2)))
    print("(a) sympy: R(psi0) =", sp.nsimplify(R0))
    c = 1 / (sp.sqrt(2) * sp.sin(1 / sp.sqrt(2)))
    f = c * sp.cos(sp.sqrt(2) * x)
    I2 = sp.integrate(f ** 2, (x, -sp.Rational(1, 2), sp.Rational(1, 2)))
    # inner(t) = int |t - x| f(x) dx, split at x = t
    inner = sp.integrate((t - x) * f, (x, -sp.Rational(1, 2), t)) + sp.integrate((x - t) * f, (x, t, sp.Rational(1, 2)))
    I3 = sp.integrate(sp.simplify(inner * f.subs(x, t)), (t, -sp.Rational(1, 2), sp.Rational(1, 2)))
    C = sp.simplify(I2 + I3)
    CMT = sp.Rational(1, 2) + sp.cot(1 / sp.sqrt(2)) / sp.sqrt(2)
    print("    C(f_MT) symbolic - C_MT simplifies to:", sp.simplify(sp.trigsimp(C - CMT)), "; numerically",
          sp.N(C - CMT, 30), "; C_MT =", sp.N(CMT, 25))
    print("    inner(t) + f(t)/c... stationarity: d^2/dt^2 [f + inner] =", sp.simplify(sp.diff(f.subs(x, t) + inner, t, 2)))


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


def Cfun(fvals, X, W):
    """C(f) = int f^2 + iint |s-t| f(s) f(t) for f sampled at Gauss nodes X (on [-1/2,1/2]) with weights W."""
    fw = fvals * W
    return float(np.sum(fw * fvals) + np.sum(np.abs(X[:, None] - X[None, :]) * fw[:, None] * fw[None, :]))


def part_b():
    CMT = 0.5 + 1 / (SQ2 * np.tan(1 / SQ2))
    print("(b) Lamzouri Lemma 3.2: C_delta -> C_MT  (psi_delta = chi((1/2-|x|)/delta), f_delta = psi_delta^2 f0 / A_delta)")
    for delta in (0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001):
        # panels concentrated in the taper region
        X1, W1 = gl(-0.5, -0.5 + delta, 40, 8); X2, W2 = gl(-0.5 + delta, 0.5 - delta, 40, 10); X3, W3 = gl(0.5 - delta, 0.5, 40, 8)
        X = np.concatenate([X1, X2, X3]); W = np.concatenate([W1, W2, W3])
        f0 = np.cos(SQ2 * X) / (SQ2 * np.sin(1 / SQ2))
        fd = chi_np((0.5 - np.abs(X)) / delta) ** 2 * f0
        fd /= np.sum(W * fd)
        Cd = Cfun(fd, X, W)
        print(f"    delta={delta:6.3f}: C_delta = {Cd:.12f},  C_delta - C_MT = {Cd - CMT:.3e},  (C_delta-C_MT)/delta = {(Cd-CMT)/delta:.4f}")


def part_c():
    print("(c) AF finite-L main-term ratio R_L = (b L^3 + 2 int_0^L y g(y) dy)/(a^2 L^3) -> R(psi)")
    CMT = 0.5 + 1 / (SQ2 * np.tan(1 / SQ2))
    for name, sqpsi, Rlim in (("flat", lambda s: np.ones_like(s), 4 / 3),
                              ("MT", lambda s: np.sqrt(np.cos(SQ2 * s)), CMT)):
        for L in (5.0, 10.0, 20.0, 50.0, 100.0, 1000.0):
            # phi^2(u) = chi(L/2+u)^2 chi(L/2-u)^2 psi(u/L); quadrature on u in [-L/2, L/2]
            Xa, Wa = gl(-L / 2, -L / 2 + 1, 40, 4); Xb, Wb = gl(-L / 2 + 1, L / 2 - 1, 40, 40); Xc, Wc = gl(L / 2 - 1, L / 2, 40, 4)
            U = np.concatenate([Xa, Xb, Xc]); Wu = np.concatenate([Wa, Wb, Wc])
            phi2 = (chi_np(L / 2 + U) * chi_np(L / 2 - U) * sqpsi(U / L)) ** 2
            a = np.sum(Wu * phi2) / L; b = np.sum(Wu * phi2 ** 2) / L
            # 2 int_0^L y g(y) dy = int int |u - v| phi2(u) phi2(v) du dv  (g = phi2 * phi2, phi2 even)
            pw = phi2 * Wu
            S = np.sum(np.abs(U[:, None] - U[None, :]) * pw[:, None] * pw[None, :])
            RL = (b * L ** 3 + S) / (a * a * L ** 3)
            print(f"    {name:4s} L={L:7.1f}: a={a:.6f} b={b:.6f}  R_L = {RL:.10f}  R_L - R = {RL - Rlim:+.3e}  L(R_L-R) = {L*(RL-Rlim):+.4f}")


def part_d():
    u = sp.symbols('u', real=True); v = sp.symbols('v', real=True)
    J = 3
    a = sp.symbols('a1:%d' % (J + 1))
    f = 1 + sum(a[j] * sp.cos(2 * sp.pi * (j + 1) * u) for j in range(J))
    h = sp.Rational(1, 2)
    I2 = sp.integrate(sp.expand(f ** 2), (u, -h, h))
    fv = f.subs(u, v)
    inner = sp.integrate(sp.expand((u - v) * fv), (v, -h, u)) + sp.integrate(sp.expand((v - u) * fv), (v, u, h))
    I3 = sp.integrate(sp.expand(inner * f), (u, -h, h))
    C = sp.simplify(sp.expand(I2 + I3))
    formula = sp.Rational(4, 3) + h * sum(a[j] ** 2 for j in range(J)) + \
        sum(((-1) ** (j + 1) * a[j] / (j + 1) ** 2 - a[j] ** 2 / (4 * (j + 1) ** 2)) for j in range(J)) / sp.pi ** 2
    print("(d) KN (eq:C) symbolic check with 3 cosine terms (cross terms included):  C - formula =",
          sp.simplify(sp.expand(C - formula)))
    wins = {"first": ([193305, -23105, 29166, 13952, -21009, 41052], (266541, 200000), "1.3327049582"),
            "second": ([122290, -45012, 16241, 1887, 2711, 3731, -5307, 2982, -5153, 5358], (6639737, 5000000), "1.32794727"),
            "third": ([200566, 19, -9358, 9283, -6746, 8170], (6662319, 5000000), "1.33246363")}
    for name, (coef, (pn, pd), stated) in wins.items():
        aj = [mp.mpf(c) / 10 ** 6 for c in coef]
        Cf = mp.mpf(4) / 3 + sum(x ** 2 for x in aj) / 2 + sum(((-1) ** j * aj[j - 1] / j ** 2 - aj[j - 1] ** 2 / (4 * j ** 2))
                                                          for j in range(1, len(aj) + 1)) / mp.pi ** 2
        # independent quadrature
        X, W = gl(-0.5, 0.5, 40, 30)
        fx = 1 + sum(float(aj[j]) * np.cos(2 * np.pi * (j + 1) * X) for j in range(len(aj)))
        Cq = Cfun(fx, X, W)
        print(f"    {name:6s}: closed form C(f) = {mp.nstr(Cf, 14)} (stated {stated}...), quadrature {Cq:.12f};"
              f" bound {pn}/{pd} = {pn/pd:.7f}, margin {float(mp.mpf(pn)/pd - Cf):.3e};  min f on grid = {fx.min():.4f}")


def part_e():
    print("(e) C(f) >= 1: lower bound from Remark LZ 2.2 / AF; spot values:")
    X, W = gl(-0.5, 0.5, 40, 30)
    for name, fx in (("flat", np.ones_like(X)), ("MT", np.cos(SQ2 * X)), ("triangle", 1.5 - 2 * np.abs(X)),
                     ("cos(pi x)", np.cos(np.pi * X)), ("1+0.4cos(2pi x)", 1 + 0.4 * np.cos(2 * np.pi * X))):
        f = fx / np.sum(W * fx)
        print(f"    {name:16s}: C = {Cfun(f, X, W):.10f}")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()

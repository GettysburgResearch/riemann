"""CRIT23 Level-2 audit, part 2, step S6 (Alpoge-Furman arXiv:2608.13637v2, Section 5: unconditional prime-side
second moment).  Independent re-implementation from the paper's text; no author code is used.

(a) AF Lemma 5.1 / (5.5): sum_{n<=x} Lambda(n)^2/n = (log x)^2/2 + O(log x) and
    sum_{n<=x} Lambda(n)^2/n (log x - log n) = (log x)^3/6 + O((log x)^2)       [numerical, x <= 2e7]
(b) Theorem 5.7 partial summation: sum_{n<=X} Lambda(n)^2/n (psi*psi)(log n / L) = L^2 int_0^1 w (psi*psi)(w) dw + O(L)
    for psi0 and psiMT, L = log X                                                   [numerical]
(c) Theorem 5.7 main constant: (int psi^2 + 2 int_0^1 w (psi*psi)) / (int psi)^2 = R(psi)   [30 digits]
(d) Prop 5.2 error bookkeeping: the displayed bounds |E1| << L^3 B^2 log L and |E2| << L^3 B^2 l log L, divided by
    (a L^2)^2, against N(T,2T) ~ X L.  Witness for finding P2-F1.
(e) Prop 5.5, the term M[P_X, Pi_X]: the sup-norm argument written in the proof gives O(L X), not O(L^2 sqrt X);
    a direct numerical evaluation at T = 3e4 (main part, edges ignored) shows the true size is far below both.

Non-rigorous floating point (numpy double / mpmath 30 digits).  Run: python3 -I s6_prime_side_af.py"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30
SQ2 = np.sqrt(2.0)


def mangoldt(nmax):
    """Lambda(n) for 0 <= n <= nmax (float array), by a smallest-prime-factor sieve."""
    lam = np.zeros(nmax + 1)
    is_p = np.ones(nmax + 1, dtype=bool)
    is_p[:2] = False
    for p in range(2, int(nmax ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p::p] = False
    primes = np.nonzero(is_p)[0]
    for p in primes:
        lp = np.log(p)
        q = p
        while q <= nmax:
            lam[q] = lp
            q *= p
    return lam


def conv_flat(w):
    w = np.abs(w)
    return np.clip(1 - w, 0, None)


def conv_mt(w):
    """(psiMT*psiMT)(w) for psiMT = cos(sqrt2 s) 1_[-1/2,1/2]; closed form derived in the audit:
       1/2 (1-w) cos(sqrt2 w) + sin(sqrt2 (1-w)) / (2 sqrt2),  0 <= w <= 1."""
    w = np.abs(w)
    out = 0.5 * (1 - w) * np.cos(SQ2 * w) + np.sin(SQ2 * (1 - w)) / (2 * SQ2)
    return np.where(w <= 1, out, 0.0)


def main():
    NMAX = 20_000_000
    lam = mangoldt(NMAX)
    n = np.arange(NMAX + 1, dtype=float)
    n[0] = 1
    a2 = lam ** 2 / n                    # Lambda(n)^2 / n
    cs = np.cumsum(a2)
    logn = np.log(n)
    print("(a) AF Lemma 5.1 (5.5): Mertens-type sums")
    for x in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 2 * 10 ** 7):
        lx = np.log(x)
        s1 = cs[x]
        s2 = float(np.sum(a2[:x + 1] * (lx - logn[:x + 1])))
        print(f"   x={x:>9d}: S1-(log x)^2/2 = {s1 - lx**2/2:9.4f}  (/log x = {(s1 - lx**2/2)/lx:7.4f});"
              f"  S2-(log x)^3/6 = {s2 - lx**3/6:9.4f}  (/log^2 x = {(s2 - lx**3/6)/lx**2:7.4f})")
    # (b) partial summation in Theorem 5.7
    print("(b) Thm 5.7 partial summation: sum_{n<=X} Lambda^2/n (psi*psi)(log n/L) vs L^2 int_0^1 w(psi*psi)")
    I_flat = 1.0 / 6.0
    I_mt = float(mp.quad(lambda w: w * (0.5 * (1 - w) * mp.cos(mp.sqrt(2) * w)
                                        + mp.sin(mp.sqrt(2) * (1 - w)) / (2 * mp.sqrt(2))), [0, 1]))
    for X in (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 2 * 10 ** 7):
        L = np.log(X)
        for name, conv, I in (("flat", conv_flat, I_flat), ("MT", conv_mt, I_mt)):
            s = float(np.sum(a2[2:X + 1] * conv(logn[2:X + 1] / L)))
            print(f"   X={X:>9d} {name:4s}: sum = {s:12.4f}, L^2*I = {L*L*I:12.4f}, diff/L = {(s - L*L*I)/L:8.4f}")
    # (c) main constant of Theorem 5.7
    print("(c) Thm 5.7 main constant (int psi^2 + 2 int_0^1 w (psi*psi)) / (int psi)^2 versus R(psi)")
    s2 = mp.sqrt(2)
    CMT = mp.mpf(1) / 2 + mp.cot(1 / s2) / s2
    for name, psi, conv, Rclaim in (
            ("flat", lambda s: mp.mpf(1), lambda w: 1 - w, mp.mpf(4) / 3),
            ("MT", lambda s: mp.cos(s2 * s), lambda w: (1 - w) * mp.cos(s2 * w) / 2 + mp.sin(s2 * (1 - w)) / (2 * s2), CMT)):
        ipsi = mp.quad(psi, [-0.5, 0.5])
        ipsi2 = mp.quad(lambda s: psi(s) ** 2, [-0.5, 0.5])
        iw = mp.quad(lambda w: w * conv(w), [0, 1])
        # direct (psi*psi)(w) by quadrature at one point, to confirm the closed form
        w0 = mp.mpf('0.37')
        direct = mp.quad(lambda s: psi(s) * psi(w0 - s), [w0 - 0.5, 0.5])
        val = (ipsi2 + 2 * iw) / ipsi ** 2
        print(f"   {name}: value = {mp.nstr(val, 25)}, R claimed = {mp.nstr(Rclaim, 25)}, diff = {mp.nstr(val - Rclaim, 3)};"
              f" closed-form (psi*psi)(0.37) check diff = {mp.nstr(direct - conv(w0), 3)}")
    # (d) Prop 5.2 bookkeeping
    print("(d) Prop 5.2: the displayed bounds, implied constants set to 1, divided by (a L^2)^2 and by N ~ X L")
    print("    T          L      E1/(L^4 N)   E2/(L^4 N)   logL/L^2    logL/L")
    for T in (1e4, 1e6, 1e8, 1e12, 1e20, 1e40):
        L = np.log(T / (2 * np.pi)); X = T / (2 * np.pi); B2 = (L + 4 * np.sqrt(X)) ** 2; N = X * L
        E1 = L ** 3 * B2 * np.log(L); E2 = L ** 3 * B2 * L * np.log(L)
        print(f"   {T:8.0e}  {L:7.2f}   {E1/L**4/N:10.3e}   {E2/L**4/N:10.3e}   {np.log(L)/L**2:9.3e}   {np.log(L)/L:9.3e}")
    print("    -> E2/(a^2 L^4) ~ 16 X log L = (16 log L / L) N: the proof yields O(N log L / L), not O(N log L / L^2);"
          " still o(N).")
    # (e) Prop 5.5, M[P_X, Pi_X]
    print("(e) Prop 5.5: sup-bound for M[P_X,Pi_X] = T * (3 sqrt X/T) * (3 sqrt X/pi) * 2 pi b L = 18 b L X  vs  L^2 sqrt X")
    for T in (1e4, 1e8, 1e12, 1e20):
        L = np.log(T / (2 * np.pi)); X = T / (2 * np.pi)
        print(f"   T={T:8.0e}: 18 L X = {18*L*X:10.3e},  L^2 sqrt X = {L*L*np.sqrt(X):10.3e},  ratio = {18*X/(L*np.sqrt(X)):9.3e};"
              f"  18 L X/(L^2 N) = {18*L*X/(L*L*X*L):8.3e} (relative size after normalisation)")
    # direct main-part evaluation at T = 3e4, flat window, g(y) ~ (L - |y|)_+ (taper ignored), edges ignored:
    #   M ~ -2 sum_n a_n g(y_n) int_T^{2T} Pi_X(tau) cos(tau y_n) dtau,  a_n = Lambda(n)/sqrt(n)
    T = 3e4; L = np.log(T / (2 * np.pi)); X = T / (2 * np.pi)
    ns = np.nonzero(lam[:int(X) + 1])[0]
    an = lam[ns] / np.sqrt(ns); yn = np.log(ns); gn = np.clip(L - yn, 0, None)
    h = 0.01
    tau = np.arange(T, 2 * T + h / 2, h)
    Pi = (1 / np.pi) * np.real(np.exp((0.5 + 1j * tau) * L) / (0.5 + 1j * tau))
    wts = np.full(tau.size, h); wts[0] = wts[-1] = h / 2
    J = np.zeros(ns.size)
    for i0 in range(0, ns.size, 64):
        J[i0:i0 + 64] = (np.cos(np.outer(yn[i0:i0 + 64], tau)) * (Pi * wts)).sum(axis=1)
    M = -2 * np.sum(an * gn * J)
    print(f"   direct main part at T=3e4 (L={L:.3f}, X={X:.1f}, {ns.size} prime powers): M[P_X,Pi_X] ~ {M:.4e};"
          f"  L^2 sqrt X = {L*L*np.sqrt(X):.3e},  L X = {L*X:.3e},  N(T,2T) ~ {X*L:.3e}")


if __name__ == "__main__":
    main()

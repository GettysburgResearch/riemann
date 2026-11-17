"""CRIT23 adjudication of finding P1-F1 (AF arXiv:2608.13637v2, proof of Prop 4.2 "Trace").

Independent re-implementation from the AF text (no AF code, no code from the part-1 audit is imported or run).
Non-rigorous double-precision floating point unless a line says "analytic".

AF objects (AF Sections 1.7, 2.2, 2.3):
  phihat(z) = int phi(u) e^{-iuz} du;  phi(u) = chi(L/2+u) chi(L/2-u) psi(u/L)^{1/2};
  L = log(T/2pi), X = e^L, h = 2pi/L, alpha_k = T + k h, d = floor(L T / 2pi);
  I = [T, 2T), I' = [T - sqrt T, 2T + sqrt T);  a = ||phi||_2^2 / L;
  tr G~ = (aL^2)^{-1} sum_{Re gamma in I'} m_rho sum_{0<=k<d} phihat(gamma - alpha_k)^2.
Poisson-Gabor (AF Lemma 2.1): sum_{k in Z} phihat(z - alpha_k)^2 = a L^2 for every z.
  head(z) := sum_{0<=k<d} phihat(z-alpha_k)^2,   tail(z) := sum_{k not in [0,d)} phihat(z-alpha_k)^2 = aL^2 - head(z).

Two different C^infinity cut-offs chi are used to show the conclusions do not depend on chi:
  chiA(t) = f(t)/(f(t)+f(1-t)), f(t) = exp(-1/t);   chiB(t) = normalised integral of the bump e^{-1/(s(1-s))}.
Windows: psi0 (flat) for everything; psi_MT for the single-point witness.

Run:  python3 -I adj_P1F1_trace.py  (from this directory; reads the EXP-0001 zero table read-only).
"""
import gzip
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.normpath(os.path.join(HERE, "..", "..", "..", "results", "zeros", "zeta_zeros_1_100000_arb.tsv.gz"))


# ---------------------------------------------------------------- cut-offs and test function
def chiA(t):
    t = np.asarray(t, float)
    out = np.where(t >= 1, 1.0, 0.0)
    m = (t > 0) & (t < 1)
    ti = t[m]
    f1, f2 = np.exp(-1 / ti), np.exp(-1 / (1 - ti))
    out[m] = f1 / (f1 + f2)
    return out


_SB = np.linspace(0.0, 1.0, 400001)
_bump = np.zeros_like(_SB)
_bump[1:-1] = np.exp(-1.0 / (_SB[1:-1] * (1 - _SB[1:-1])))
_CB = np.concatenate([[0.0], np.cumsum(0.5 * (_bump[1:] + _bump[:-1]) * np.diff(_SB))])
_CB /= _CB[-1]


def chiB(t):
    """integrated standard bump: chiB(t) = int_0^t e^{-1/(s(1-s))} ds / int_0^1 (same); trapezoid table + interpolation."""
    t = np.asarray(t, float)
    return np.interp(np.clip(t, 0.0, 1.0), _SB, _CB)


class Phi:
    """phi on [0, L/2] by composite Gauss-Legendre; phihat(z) = 2 int_0^{L/2} phi(u) cos(zu) du (phi even)."""

    def __init__(self, L, chi, window="flat", zmax=400.0, npan=16):
        self.L = L
        x, w = np.polynomial.legendre.leggauss(npan)
        width = min(0.02, 1.0 / zmax)
        us, ws = [], []
        for A, B in ((0.0, L / 2 - 1.0), (L / 2 - 1.0, L / 2)):
            n = max(4, int(math.ceil((B - A) / width)))
            e = np.linspace(A, B, n + 1)
            lo, hi = e[:-1, None], e[1:, None]
            us.append((0.5 * (hi - lo) * x + 0.5 * (hi + lo)).ravel())
            ws.append((0.5 * (hi - lo) * w).ravel())
        self.u, self.w = np.concatenate(us), np.concatenate(ws)
        ph = chi(L / 2 + self.u) * chi(L / 2 - self.u)
        if window == "MT":
            ph = ph * np.sqrt(np.cos(math.sqrt(2) * self.u / L))
        self.ph = ph
        self.wp = 2 * self.w * ph
        self.a = 2 * np.sum(self.w * ph ** 2) / L

    def hat(self, z, chunk=2000):
        z = np.asarray(z)
        flat = z.ravel()
        out = np.empty(flat.shape, dtype=complex if np.iscomplexobj(flat) else float)
        for s in range(0, flat.size, chunk):
            out[s:s + chunk] = np.cos(np.outer(flat[s:s + chunk], self.u)) @ self.wp
        return out.reshape(z.shape)


def grid(T):
    L = math.log(T / (2 * math.pi))
    h = 2 * math.pi / L
    d = math.floor(L * T / (2 * math.pi))
    return L, h, d


def head_tail(P, T, gam, W):
    """head, tail for one point gam (real or complex), summing k with |Re gam - alpha_k| <= W; rest neglected."""
    L, h, d = grid(T)
    r = gam.real if isinstance(gam, complex) else gam
    klo, khi = math.floor((r - W - T) / h), math.ceil((r + W - T) / h)
    k = np.arange(klo, khi + 1)
    v = P.hat(gam - (T + k * h)) ** 2
    inside = (k >= 0) & (k < d)
    return v[inside].sum(), v[~inside].sum(), v.sum()


def load_zeros():
    g = []
    with gzip.open(ZEROS, "rt") as f:
        for line in f:
            p = line.split()
            g.append(float(p[1]))
    return np.array(g)


def main():
    out = []
    pr = lambda s="": (print(s), out.append(s), sys.stdout.flush())
    W = 300.0      # single points
    WZ = 150.0     # real-zero sums (max phihat^2 beyond 150 is ~1e-16, see (0))
    pr("CRIT23 adjudication P1-F1: independent checks (double precision, non-rigorous unless marked analytic)")
    pr("=" * 100)

    # ---- (0) decay of phihat beyond W and Poisson-Gabor sanity
    pr("(0) Implementation checks: Poisson-Gabor sum_k phihat(z-alpha_k)^2 = aL^2, and truncation error beyond W")
    for chi, nm in ((chiA, "chiA"), (chiB, "chiB")):
        T = 1e4
        L, h, d = grid(T)
        P = Phi(L, chi, zmax=W)
        xi = np.linspace(WZ, WZ + 200, 4001)
        mx = np.max(P.hat(xi) ** 2)
        for z in (12345.678, 12345.678 + 0.3j, 14000.1 - 0.45j):
            _, _, full = head_tail(P, T, z, W)
            pr(f"   {nm} T=1e4 z={z}: sum_k phihat^2 / (aL^2) - 1 = {abs(full / (P.a * L * L) - 1):.2e}")
        pr(f"   {nm}: a={P.a:.6f}  phihat(0)={P.hat(np.array([0.0]))[0]:.6f} (L-1={L - 1:.6f})  max phihat(xi)^2 on [WZ, WZ+200] (WZ={WZ:.0f}) = {mx:.2e}")
    pr("=" * 100)

    # ---- (B) alpha_d
    pr("(B) Slip (b): alpha_d = T + d h with d = floor(LT/2pi); AF Prop 4.2 proof asserts alpha_k notin [T,2T) for k notin [0,d)")
    for T in (1e3, 2e3, 1e4, 3e4):
        L, h, d = grid(T)
        ad = T + d * h
        pr(f"   T={T:>7.0f}: LT/2pi={L * T / (2 * math.pi):.4f}  alpha_(d-1)={T + (d - 1) * h:.4f}  alpha_d={ad:.4f}  "
           f"in [T,2T)? {T <= ad < 2 * T}   2T-alpha_d={2 * T - ad:.4f} < h={h:.4f}")
    pr("   (analytic) d h = h floor(T/h) in (T-h, T], so alpha_d in (2T-h, 2T], with alpha_d < 2T iff LT/2pi is not an integer.")
    pr("   For Re gamma in [3T/2, alpha_d): |Re gamma - alpha_d| = D_rho - (2T - alpha_d) < D_rho, but >= D_rho - h.")
    pr("=" * 100)

    # ---- (C) single-point witness
    pr("(C) Slip (a), single real point gamma = T - sqrt(T)/2 in I'\\I  (D_rho = dist(gamma,{T,2T}) = sqrt(T)/2)")
    for chi, nm, win in ((chiA, "chiA", "flat"), (chiB, "chiB", "flat"), (chiA, "chiA", "MT")):
        for T in (2e3, 1e4, 1e5, 1e6):
            L, h, d = grid(T)
            P = Phi(L, chi, win, zmax=W)
            X = math.exp(L)
            g = T - math.sqrt(T) / 2
            D = math.sqrt(T) / 2
            hd, tl, full = head_tail(P, T, g, W)
            aL2 = P.a * L * L
            shape = math.sqrt(X) * L * D ** -3 / aL2
            # analytic (chi-independent) lower bound: |phihat(r)| <= TV(phi)/|r| <= 2/|r|, so
            # head <= sum_{j>=0} 4/(D+jh)^2 <= 4/D^2 + (4/h)/D  and tail/aL^2 >= 1 - head_bound/aL^2
            hb = 4 / D ** 2 + 4 / (h * D)
            amin = (L - 2) / L * (1.0 if win == "flat" else math.cos(1 / math.sqrt(2)))   # a >= this (phi^2 >= psi on bulk)
            pr(f"   {nm}/{win:4s} T={T:>8.0f} L={L:.3f}: head/aL^2={hd / aL2:.3e}  tail/aL^2={tl / aL2:.12f}  "
               f"[analytic: tail/aL^2 >= {1 - hb / (amin * L * L):.5f}]  AF shape X^1/2 L D^-3/(aL^2)={shape:.3e}  "
               f"ratio={tl / aL2 / shape:.3e}  (TL={T * L:.3e})")
    pr("   (analytic) tail/aL^2 -> 1 while the displayed per-zero bound X^{1/2} L D^-3/(aL^2) = 8(2pi)^{-1/2}/(a L T) -> 0,")
    pr("   so the ratio grows like T L and no fixed implied constant makes the displayed per-zero bound true on I'\\I.")
    pr("=" * 100)

    # ---- (D) real zeros
    pr("(D) Real zeta zeros (table EXP-0001; all on the line and simple): trace decomposition")
    G = load_zeros()
    pr(f"   zero table: {G.size} zeros, max ordinate {G[-1]:.3f}")
    for chi, nm in ((chiA, "chiA"), (chiB, "chiB")):
        for T in (2e3, 6e3, 2e4, 3e4):
            L, h, d = grid(T)
            P = Phi(L, chi, zmax=WZ)
            aL2 = P.a * L * L
            X = math.exp(L)
            sT = math.sqrt(T)
            inI = (G >= T) & (G < 2 * T)
            inIp = (G >= T - sT) & (G < 2 * T + sT)
            outer = inIp & ~inI
            Dr = np.minimum(np.abs(G - T), np.abs(G - 2 * T))
            # per-zero normalised head; zeros at distance > WZ from both T and 2T: head/aL^2 = 1 (in I) or 0 (in I'\I) to ~1e-15
            hn = np.where(inI, 1.0, 0.0)
            near = inIp & (Dr <= WZ)
            for i in np.nonzero(near)[0]:
                hd, tl, full = head_tail(P, T, float(G[i]), WZ)
                hn[i] = hd / aL2
            trG = hn[inIp].sum()
            NI, NIp, Nout = int(inI.sum()), int(inIp.sum()), int(outer.sum())
            err_I = (1 - hn[inI]).sum()                 # sum over I of tail/aL^2
            head_out = hn[outer].sum()                  # sum over I'\I of head/aL^2
            rest = inIp & (Dr >= 1)
            tail_rest = (1 - hn[rest]).sum()            # what AF claim is << X^{1/2}
            tail_rest_out = (1 - hn[rest & outer]).sum()
            pr(f"   {nm} T={T:>6.0f} L={L:.3f} d={d}: N(I)={NI} N(I')={NIp} N(I'\\I)={Nout} trG~={trG:.4f}  "
               f"trG~-N(I)={trG - NI:+.4f}  trG~-N(I')={trG - NIp:+.4f}")
            pr(f"        sum_I tail/aL^2={err_I:.4f}  sum_(I'\\I) head/aL^2={head_out:.4f}  "
               f"sum_(I', D>=1) tail/aL^2={tail_rest:.2f} (of which I'\\I: {tail_rest_out:.2f})  X^1/2={math.sqrt(X):.2f}  "
               f"ratio={tail_rest / math.sqrt(X):.2f}  vs L*sqrt(2/pi)={L * math.sqrt(2 / math.pi):.2f}")
    pr("   (analytic) N(T-sqrt T, T) + N(2T, 2T+sqrt T) = (sqrt T / pi) log(T/2pi) + O(log T) (Riemann-von Mangoldt), so the")
    pr("   D>=1 sum is >= (1-o(1)) sqrt(T) L / pi, which is not << X^{1/2} = (T/2pi)^{1/2}: the ratio tends to infinity like L.")
    pr("=" * 100)

    # ---- (R) the repair bound for off-line points in I'\I
    pr("(R) Repair input: for z in I'\\I (real part at distance D from I, |Im z| = y), |head(z)| vs X^{1/2} min(L^2, L D^-3)")
    for T in (2e3, 2e4):
        L, h, d = grid(T)
        P = Phi(L, chiA, zmax=W)
        X = math.exp(L)
        for y in (0.0, 0.25, 0.49):
            row = []
            for D in (0.0, 0.5, 1.0, 3.0, 10.0, 30.0):
                z = complex(T - D, y)
                hd, tl, full = head_tail(P, T, z, W)
                bound = math.sqrt(X) * min(L * L, L * D ** -3 if D > 0 else float("inf"))
                row.append(f"D={D:>4}: |head|/bound={abs(hd) / bound:.2e}")
            pr(f"   T={T:.0f} y={y}: " + "  ".join(row))
    pr("   (all ratios bounded => |head_rho| << X^{1/2} min(L^2, L D^-3) is consistent; analytic proof in the adjudication)")
    with open(os.path.join(HERE, "adj_P1F1_trace.out"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

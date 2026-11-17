"""CRIT23 Level-2 audit, part 1: step S5 (trace normalisation, localisation, tail) of Alpoge-Furman
arXiv:2608.13637v2 (Section 2.2, Props 4.2, 4.3, Cor 4.5).

(A) d = floor(LT/2pi) versus N(T,2T): AF Section 2.2 asserts d = N(T,2T) + O(L).  Witness from the Arb zero table.
(B) The grid point alpha_d: AF Prop 4.2 asserts "k notin [0,d)  =>  alpha_k notin [T,2T)".  Witness for k = d.
(C) Prop 4.2's per-zero bound |Re gamma - alpha_k| >= D_rho for k notin [0,d), applied to zeros with
    Re gamma in I' \\ I (outside [T,2T)): direct computation shows the "tail" is ~ a L^2 (the whole sum), not small.
(D) Real zeta zeros at T = 2000 and T = 6000: tr G~ split by zeros in I and in I' \\ I; compare with N(I), N(I').
(E) Per-zero tail at the window edge (D_rho = 0) for complex gamma: scaling ~ e^{L|y|} L^2 (relevant to F7).
(F) Prop 4.3 tail ||E~||_1 for the real zeros in the table outside I'.

phihat on long real ranges is tabulated by FFT of phi (trapezoid rule, spectrally accurate for C^inf compactly
supported phi) and cubic-spline interpolated; validated against direct quadrature.  Non-rigorous floating point.
Run: python3 -I s5_trace_tail.py"""
import sys, os, gzip
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.interpolate import CubicSpline
from af_testfn import TestFunction, phi

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.join(HERE, "..", "..", "..", "results", "zeros", "zeta_zeros_1_100000_arb.tsv.gz")


def load_zeros():
    g = []
    with gzip.open(ZEROS, "rt") as f:
        for line in f:
            g.append(float(line.split("\t")[1]))
    return np.array(g)


def N_count(zeros, t1, t2):
    """number of zeros with t1 < gamma <= t2 (all simple in the table range)."""
    return int(np.searchsorted(zeros, t2, side="right") - np.searchsorted(zeros, t1, side="right"))


def phihat_table(L, window, xmax=400.0, dx_target=0.004):
    U = np.pi / dx_target                 # x-spacing = pi / U
    n = 1 << int(np.ceil(np.log2(2 * U / 2e-3)))
    du = 2 * U / n
    u = -U + du * np.arange(n)
    p = phi(u, L, window)
    # phihat(x_j) = sum_n phi(u_n) e^{-i u_n x_j} du ;  x_j = 2 pi j /(n du)
    F = np.fft.fft(np.fft.ifftshift(p)) * du
    x = 2 * np.pi * np.fft.fftfreq(n, d=du)
    order = np.argsort(x); x = x[order]; F = F[order].real
    keep = np.abs(x) <= xmax
    return CubicSpline(x[keep], F[keep])


def main():
    out = []
    zeros = load_zeros()
    out.append(f"zero table: {len(zeros)} zeros up to gamma = {zeros[-1]:.3f}")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(A) d = floor(LT/2pi) vs N(T,2T)   [AF Sec 2.2 claims d = N(T,2T) + O(L)]")
    for T in (1000.0, 5000.0, 10000.0, 30000.0):
        L = np.log(T / (2 * np.pi)); d = int(np.floor(L * T / (2 * np.pi)))
        NT = N_count(zeros, T, 2 * T)
        smooth = (T / (2 * np.pi)) * (L + 2 * np.log(2) - 1)
        out.append(f"   T={T:8.0f}  L={L:.4f}  d={d:7d}  N(T,2T)={NT:7d}  d-N={d-NT:7d}  "
                   f"-(2log2-1)T/2pi={-(2*np.log(2)-1)*T/(2*np.pi):9.1f}  (d-N)/L={(d-NT)/L:9.1f}  (d-N)/N={(d-NT)/NT:.4f}  "
                   f"smooth N - N = {smooth-NT:.1f}")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(B) alpha_d = T + 2 pi d / L  versus [T, 2T)")
    for T in (1000.0, 2000.0, 10000.0, 30000.0):
        L = np.log(T / (2 * np.pi)); d = int(np.floor(L * T / (2 * np.pi))); h = 2 * np.pi / L
        ad = T + h * d
        out.append(f"   T={T:8.0f}: LT/2pi={L*T/(2*np.pi):.4f}, alpha_(d-1)={T+h*(d-1):.4f}, alpha_d={ad:.4f} "
                   f"{'IN' if ad < 2*T else 'NOT in'} [T,2T)  (2T - alpha_d = {2*T-ad:.4f}, h = {h:.4f})")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(C) Prop 4.2 per-zero tail for a REAL point gamma = T - sqrt(T)/2 (in I' \\ I)")
    tf_cache = {}
    for window in ("flat", "MT"):
        for T in (2000.0, 10000.0):
            L = np.log(T / (2 * np.pi)); d = int(np.floor(L * T / (2 * np.pi))); h = 2 * np.pi / L
            X = T / (2 * np.pi)
            tf = TestFunction(L, window, zmax=200.0); aL2 = tf.a * L * L
            tab = phihat_table(L, window)
            # validation of the FFT table
            xs = np.linspace(-150, 150, 301) + 0.123
            err = np.max(np.abs(tab(xs) - tf.hat_real(xs)))
            gam = T - np.sqrt(T) / 2
            ks = np.arange(d); al = T + h * ks
            diff = gam - al
            near = np.abs(diff) <= 390
            head = np.sum(tab(diff[near]) ** 2)                      # sum over k in [0,d) (far terms < 1e-20 each)
            tail = aL2 - head                                        # Lemma 2.1: full-lattice sum = a L^2 exactly
            D = np.sqrt(T) / 2
            claimed_shape = X ** 0.5 * L * D ** -3                   # AF: e^{L/2} C^2 * L min(L^3, D^-3), constant dropped
            out.append(f"   [{window}] T={T:.0f} (FFT table max err {err:.1e}): gamma = T - sqrt(T)/2, D_rho = {D:.2f}: "
                       f"head/aL^2 = {head/aL2:.3e}, tail/aL^2 = {tail/aL2:.10f};  AF bound shape X^(1/2) L D^-3 / (aL^2) = "
                       f"{claimed_shape/aL2:.3e}  -> ratio actual/claimed-shape = {tail/claimed_shape:.3e}")
            tf_cache[(window, T)] = (tf, tab)
    out.append("   asymptotically: actual tail/aL^2 -> 1 while X^(1/2) L D^-3/(aL^2) ~ T^(1/2) T^(-3/2) / L -> 0, so no fixed implied")
    out.append("   constant can make the displayed per-zero inequality true for zeros in I' \\ I.")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(D) Real zeta zeros: tr G~ = sum_{Re gamma in I'} ||v_rho||^2 / (aL^2)   (all zeros here are simple, on the line)")
    for window in ("flat", "MT"):
        for T in (2000.0, 6000.0, 20000.0):
            L = np.log(T / (2 * np.pi)); d = int(np.floor(L * T / (2 * np.pi))); h = 2 * np.pi / L
            tf = TestFunction(L, window, zmax=100.0); aL2 = tf.a * L * L
            tab = phihat_table(L, window)
            lo, hi = T - np.sqrt(T), 2 * T + np.sqrt(T)
            gz = zeros[(zeros >= lo) & (zeros < hi)]
            contrib = np.empty(len(gz))
            for j, gm in enumerate(gz):
                k0 = int(np.ceil((gm - 390 - T) / h)); k1 = int(np.floor((gm + 390 - T) / h))
                k0 = max(k0, 0); k1 = min(k1, d - 1)
                if k1 < k0:
                    contrib[j] = 0.0; continue
                al = T + h * np.arange(k0, k1 + 1)
                contrib[j] = np.sum(tab(gm - al) ** 2) / aL2
            inI = (gz >= T) & (gz < 2 * T)
            trG = contrib.sum()
            NI = int(inI.sum()); NIp = len(gz)
            out.append(f"   [{window}] T={T:.0f} L={L:.3f} d={d}: N(I)={NI}, N(I')={NIp}, tr G~={trG:.4f};  "
                       f"tr G~ - N(I) = {trG-NI:+.4f},  tr G~ - N(I') = {trG-NIp:+.4f};  "
                       f"sum over I'\\I zeros = {contrib[~inI].sum():.4f} (#={int((~inI).sum())});  min/max per-zero in I: "
                       f"{contrib[inI].min():.6f}/{contrib[inI].max():.6f}")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(E) per-zero tail at the window edge, D_rho = 0, complex gamma = 2T - i y:  sum_{k>=d} |phihat|^2 / (e^{L|y|} L^2)")
    for window in ("flat",):
        for L in (4.0, 6.0, 8.0, 10.0):
            tf = TestFunction(L, window, zmax=420.0); h = 2 * np.pi / L
            ks = np.arange(0, int(400 / h))
            for y in (0.0, 0.25, 0.49):
                z = 0.0 - 1j * y                     # put the edge at 0: alpha_k = k h for k >= 0 are the excluded points
                tail = np.sum(np.abs(tf.hat(z - h * ks)) ** 2)
                out.append(f"   L={L:4.1f} y={y:.2f}: tail = {tail:10.4f},  tail/(e^(L y) L^2) = {tail/(np.exp(L*y)*L*L):.4f},  "
                           f"tail/(e^(L y) L^4) = {tail/(np.exp(L*y)*L**4):.5f}")
    # ---------------------------------------------------------------------------------------------------
    out.append("=" * 100)
    out.append("(F) Prop 4.3: ||E~||_1 <= sum_{Re gamma notin I'} ||v_rho||^2/(aL^2), real zeros from the table (both signs)")
    for T in (2000.0, 6000.0):
        L = np.log(T / (2 * np.pi)); d = int(np.floor(L * T / (2 * np.pi))); h = 2 * np.pi / L
        tf, tab = TestFunction(L, "flat", zmax=100.0), phihat_table(L, "flat")
        aL2 = tf.a * L * L
        lo, hi = T - np.sqrt(T), 2 * T + np.sqrt(T)
        gz = zeros[((zeros < lo) & (zeros > T - 390)) | ((zeros >= hi) & (zeros < 2 * T + 390))]
        s = 0.0
        for gm in gz:
            k0 = max(int(np.ceil((gm - 390 - T) / h)), 0); k1 = min(int(np.floor((gm + 390 - T) / h)), d - 1)
            if k1 >= k0:
                al = T + h * np.arange(k0, k1 + 1)
                s += np.sum(tab(gm - al) ** 2) / aL2
        out.append(f"   T={T:.0f}: sum over zeros with sqrt(T) <= dist(gamma, I) <= 390: {s:.3e}  (AF bound shape X^(1/2)/T = {np.sqrt(T/(2*np.pi))/T:.3e}; "
                   f"zeros farther than 390 contribute < 1e-20 each in this table)")
    print("\n".join(out))


if __name__ == "__main__":
    main()

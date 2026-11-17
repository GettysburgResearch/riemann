#!/usr/bin/env python3
"""CRIT23 dossier: independent closing checks (exploration layer, no new mathematical claim).

Run from this directory:  python3 -I dossier_checks.py > dossier_checks.out

(A) Ball-arithmetic (python-flint / Arb) enclosures of the headline constants of
    Alpoge-Furman arXiv:2608.13637v2 (AF) and Lamzouri arXiv:2609.02882v2 (LZ), and a check that
    each stated decimal / percentage is a strict lower bound for its constant.
(B) Exact-rational checks of the Knausgard arXiv:2610.08965v1 (KN) constants as stated in its Lean
    statements (KN Section 8), and their comparison with the LZ constants (enclosures from (A)).
(C) Sharpness of the flat-window certificate for the information it uses (AF Section 7.2(a)-(b)):
    an explicit conjugation-invariant configuration with exactly 1/3 of its zeros in off-line pairs
    whose flat-window second moment per zero tends to 4/3 and on which N0s >= 2N - sum K^2 is an
    equality in the limit; the same configuration is excluded by the Montgomery-Taylor window.
(D) Conditional illustration (HYPOTHETICAL INPUT, not a theorem): what the same certificate would
    give with the flat window of Fourier support Delta if the all-zeros form factor were
    min(|alpha|, 1) on [-Delta, Delta]. Delta <= 1 is the unconditional range.
(E) Independent re-check of the two explicit witnesses of the adjudicated finding P1-F1
    (AF Prop 4.2 proof), using the Arb-certified zero table of Observatory EXP-0001.

Everything in (A), (B), (E) is ball arithmetic or exact rational arithmetic. (C) and (D) use
sympy exact algebra plus mpmath floating point (marked as such in the output); they are
illustrations of the method's limits, not proofs about zeta zeros.
"""
import gzip
import os
from fractions import Fraction

import flint
from flint import arb, acb, ctx
import mpmath as mp
import sympy as sp

ctx.prec = 256
mp.mp.dps = 40

HERE = os.path.dirname(os.path.abspath(__file__))
ZEROS = os.path.normpath(os.path.join(HERE, "..", "..", "..", "results", "zeros",
                                      "zeta_zeros_1_100000_arb.tsv.gz"))


def show(label, x, digits=30):
    print(f"  {label:<46s} {x.str(digits, radius=True)}")


def strictly_greater(x, q):
    """True iff the ball x lies strictly above the rational q (proved by the enclosure)."""
    return bool(x > arb(flint.fmpq(q.numerator, q.denominator)))


print("CRIT23 dossier checks")
print("python-flint", flint.__version__, "| mpmath", mp.__version__, "| sympy", sp.__version__,
      "| working precision", ctx.prec, "bits")
print()

# ---------------------------------------------------------------- (A)
print("(A) Arb enclosures of the AF / LZ constants")
r2 = arb(2).sqrt()
u = 1 / r2
C_MT = arb(1) / 2 + u.cot() / r2          # = 1/c_MT in AF; second-moment constant of the MT window
C0 = 2 - C_MT                              # LZ (1.1): 3/2 - cot(1/sqrt2)/sqrt2
C1 = (3 - C_MT) / 2                        # LZ: (C0 + 1)/2
C2 = (1 + 2 * r2 + 2 * C0) / (3 + 2 * r2)  # LZ Theorem 1.1
box = (2 + C0) / 3                         # BGSTB25 box value quoted by LZ
t = u.tan()
c_MT_lean = r2 * t / (1 + t / r2)          # AF Appendix A Lean form of c_MT
show("C_MT = 1/2 + cot(1/sqrt2)/sqrt2", C_MT)
show("C0 = 2 - C_MT", C0)
show("C1 = (3 - C_MT)/2", C1)
show("C2 = (1+2sqrt2+2C0)/(3+2sqrt2)", C2)
show("(2 + C0)/3  (box value, not unconditional)", box)
show("1/c_MT(Lean form) - C_MT", 1 / c_MT_lean - C_MT, 5)
print("  1/c_MT(Lean) - C_MT contains 0:", (1 / c_MT_lean - C_MT).contains(0))
print("  C1 - (C0 + 1)/2 contains 0:",
      (C1 - (C0 + 1) / 2).contains(0))
checks = [
    ("C0 > 0.6725  (AF '0.6725', LZ 'more than 67.25%')", C0, Fraction(6725, 10000)),
    ("C0 > 2/3", C0, Fraction(2, 3)),
    ("C1 > 0.8362  (AF '0.8362', LZ 'more than 83.62%')", C1, Fraction(8362, 10000)),
    ("C1 > 5/6", C1, Fraction(5, 6)),
    ("C2 > 0.8876  (LZ 'more than 88.76%')", C2, Fraction(8876, 10000)),
    ("C0 > 0.417293 (PRZZ20 on-line record)", C0, Fraction(417293, 1000000)),
]
for lab, x, q in checks:
    print(f"  {lab:<56s} proved by enclosure: {strictly_greater(x, q)}")
print()

# ---------------------------------------------------------------- (B)
print("(B) KN constants (exact rationals from the Lean statements, KN Section 8)")
q = Fraction(1645064, 1960733)
kn = {
    "distinct_zeros_839      q": q,
    "simple_zeros_678        2q-1": Fraction(1329395, 1960733),
    "simple_critical_zeros_673  s0": Fraction(1669159, 2478195),
    "average_simple_and_critical_8367": Fraction(2073677, 2478195),
    "simple_or_critical_8891": Fraction(3376433, 3797325),
    "simple_or_critical_8893": Fraction(50652159, 56956375),
}
for k, v in kn.items():
    print(f"  {k:<36s} {v.numerator}/{v.denominator} = {mp.mpf(v.numerator) / v.denominator}")
print("  2q - 1 == 1329395/1960733 :", 2 * q - 1 == Fraction(1329395, 1960733))
s0 = kn["simple_critical_zeros_673  s0"]
print("  (1 + s0)/2 == 2073677/2478195 :", (1 + s0) / 2 == Fraction(2073677, 2478195))
cmp = [
    ("q  > C1 (LZ/AF distinct)", q, C1),
    ("2q-1 > C0 (simple zeros, any location)", 2 * q - 1, C0),
    ("s0 > C0 (simple on the line)", s0, C0),
    ("(1+s0)/2 > C1 (LZ average)", (1 + s0) / 2, C1),
    ("50652159/56956375 > C2 (LZ simple-or-line)", kn["simple_or_critical_8893"], C2),
]
for lab, v, c in cmp:
    gap = arb(flint.fmpq(v.numerator, v.denominator)) - c
    print(f"  {lab:<44s} {bool(gap > 0)}   gap = {gap.str(8, radius=False)}")
stated = [("q >= 0.83900459675 (KN Thm 1.1 decimal)", q, Fraction(83900459675, 10**11)),
          ("2q-1 >= 0.67800919 (KN Cor 1.2 decimal)", 2 * q - 1, Fraction(67800919, 10**8)),
          ("s0 >= 0.673538 (KN Thm 1.3 decimal)", s0, Fraction(673538, 10**6))]
for lab, v, d in stated:
    print(f"  {lab:<44s} {v >= d}")
print()

# ---------------------------------------------------------------- (C)
print("(C) Sharpness of the flat-window certificate for the information it uses (illustration)")
print("    Rescaled points on Z (flat window: K(x) = sin(pi x)/(pi x) vanishes at nonzero integers).")
print("    Each block of 6 consecutive integers: 4 simple on-line points, 1 'heavy' site, 1 empty site.")
print("    Heavy site = an on-line double, or an off-line pair n +/- i*eps (two simple off-line zeros).")


def K_flat(z):
    z = mp.mpc(z)
    if z == 0:
        return mp.mpf(1)
    return mp.sin(mp.pi * z) / (mp.pi * z)


def f_mt(s):
    return mp.cos(mp.sqrt(2) * s)


MT_norm = mp.quad(f_mt, [-0.5, 0.5])


def K_mt(z):
    # Fourier transform of the MT window normalised to integral 1, at complex z (exact closed form)
    z = mp.mpc(z)
    a = mp.sqrt(2)
    w = 2 * mp.pi * z
    # int_{-1/2}^{1/2} cos(a s) cos(w s) ds = sum of two sinc-type terms
    def half(b):
        return mp.mpf(1) / 2 if b == 0 else mp.sin(b / 2) / b
    return (half(a - w) + half(a + w)) / MT_norm


def config(M, eps, heavy):
    pts = []  # (z, multiplicity)
    for b in range(M):
        base = 6 * b
        for j in range(4):
            pts.append((mp.mpc(base + j), 1))
        if heavy == "double":
            pts.append((mp.mpc(base + 4), 2))
        else:
            pts.append((mp.mpc(base + 4, eps), 1))
            pts.append((mp.mpc(base + 4, -eps), 1))
    return pts


def second_moment(pts, K):
    s = mp.mpc(0)
    for z, m in pts:
        for w, n in pts:
            s += m * n * K(z - w) ** 2
    return s


M = 25
for heavy, eps in [("double", 0), ("pair", mp.mpf("0.1")), ("pair", mp.mpf("0.01")),
                   ("pair", mp.mpf("0.001"))]:
    pts = config(M, eps, heavy)
    N = sum(m for _, m in pts)
    N0s = sum(1 for z, m in pts if m == 1 and z.imag == 0)
    Nd = len(pts)
    S = second_moment(pts, K_flat)
    cert = 2 * N - S.real
    cert_d = (3 * N - S.real) / 2
    print(f"  heavy={heavy:<6s} eps={str(eps):<6s} N={N} N0s={N0s} Nd={Nd} "
          f"|Im S|={float(abs(S.imag)):.1e} S/N={float(S.real / N):.6f} "
          f"2N-S={float(cert):.4f} (N0s={N0s}) (3N-S)/2={float(cert_d):.4f} (Nd={Nd})")
pts = config(M, 0, "double")
N = sum(m for _, m in pts)
S_mt = second_moment(pts, K_mt)
print(f"  same 'double' configuration, MT window: S/N = {float(S_mt.real / N):.6f} "
      f"vs C_MT = {C_MT.str(10)}: exceeds C_MT -> excluded by the MT second moment: "
      f"{bool(S_mt.real / N > float(C_MT.mid()) + 1e-6)}")
print("  (floating point, mpmath 40 digits; K_flat(n)=0 exactly at nonzero integers, so the eps=0")
print("   case is exact: S/N = (4 + 4)/6 = 4/3 and 2N - S = N0s.)")
print()

# ---------------------------------------------------------------- (D)
print("(D) HYPOTHETICAL (conditional) input: flat window of Fourier support Delta, form factor")
print("    min(|alpha|,1) on [-Delta,Delta] for the sum over all zeros. Only Delta <= 1 is known")
print("    unconditionally (BGSTB24 Lemma 5; AF Section 5). Delta > 1 is beyond current knowledge.")
D, a = sp.symbols("Delta alpha", positive=True)
# f = 1/Delta on [-Delta/2, Delta/2]; r = f*f has density (Delta - |alpha|)/Delta^2 on [-Delta, Delta]
C_le1 = sp.simplify(1 / D + 2 * sp.integrate((D - a) * a, (a, 0, D)) / D**2)
C_ge1 = sp.simplify(1 / D + 2 * (sp.integrate((D - a) * a, (a, 0, 1))
                                  + sp.integrate((D - a), (a, 1, D))) / D**2)
print("  C(Delta) for Delta <= 1 :", sp.simplify(C_le1), "   (AF Rem 6.1: H = 2 - 1/l - l/3)")
print("  C(Delta) for Delta >= 1 :", sp.simplify(C_ge1))
for Dv in [sp.Rational(1, 2), 1, sp.Rational(3, 2), 2, 4, 10]:
    Cv = (C_le1 if Dv <= 1 else C_ge1).subs(D, Dv)
    # numerical cross-check by direct double quadrature of int f^2 + int int f f min(|s-t|,1)
    Dn = mp.mpf(Dv)
    def inner(s):
        bps = sorted({-Dn / 2, Dn / 2, s} | {b for b in (s - 1, s + 1) if -Dn / 2 < b < Dn / 2})
        return mp.quad(lambda tt: min(abs(s - tt), 1), bps)
    obps = sorted({-Dn / 2, Dn / 2} | {b for b in (-Dn / 2 + 1, Dn / 2 - 1) if -Dn / 2 < b < Dn / 2})
    num = 1 / Dn + mp.quad(inner, obps) / Dn**2
    print(f"  Delta={str(Dv):<4s} C={str(sp.nsimplify(Cv)):<8s} quad={mp.nstr(num, 12):<14s} "
          f"2-C={mp.nstr(2 - mp.mpf(sp.N(Cv, 30)), 8):<11s} (3-C)/2={mp.nstr((3 - mp.mpf(sp.N(Cv, 30))) / 2, 8)}")
print()

# ---------------------------------------------------------------- (E)
print("(E) Re-check of the P1-F1 witnesses (AF Prop 4.2 proof), Arb arithmetic")
gam = None
with gzip.open(ZEROS, "rt") as fh:
    for line in fh:
        idx, g, rad = line.split("\t")
        if idx == "10085":
            gam = arb(g, rad)
            break
print("  zero #10085 from EXP-0001:", gam.str(25, radius=True))
T = arb(10000)
pi = arb.pi()
L = (T / (2 * pi)).log()
h = 2 * pi / L
dval = (L * T / (2 * pi)).floor()
print("  T = 1e4: L =", L.str(10), " h =", h.str(10), " d = floor(LT/2pi) =", dval.str(12),
      " (LT/2pi =", (L * T / (2 * pi)).str(15), ")")
inI1 = bool(gam > T - T.sqrt()) and bool(gam < T)
Drho = T - gam
alpha_m59 = T - 59 * h
dist = abs(gam - alpha_m59)
print("  gamma in I' \\ I = [T - sqrt T, T):", inI1, "  D_rho = dist(gamma,{T,2T}) =", Drho.str(10))
print("  alpha_{-59} =", alpha_m59.str(12), " |gamma - alpha_{-59}| =", dist.str(8),
      " < D_rho:", bool(dist < Drho), "  (k = -59 is outside [0, d))")
print("  slip (b): alpha_d = T + d*h versus 2T")
for Tv in [1000, 2000, 10000, 30000]:
    T = arb(Tv)
    L = (T / (2 * pi)).log()
    h = 2 * pi / L
    x = L * T / (2 * pi)
    dv = x.floor()
    unique = x.floor().unique_fmpz() is not None
    ad = T + dv * h
    print(f"    T={Tv:<6d} d={dv.str(10):<12s} alpha_d={ad.str(12):<16s} 2T-alpha_d={(2*T-ad).str(6):<12s}"
          f" alpha_d in [T,2T): {bool(ad < 2*T) and bool(ad >= T)}  floor unambiguous: {unique}")
print()
print("done")

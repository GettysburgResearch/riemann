#!/usr/bin/env python3
"""SIEGEL dossier checks (our own code; run with `python3 -I dossier_checks.py [paths...]`).

Sections
  (H) sha256 of the audited source files (OAI paper.pdf / paper.tex / Lean challenge; arXiv PDFs from the
      session cache), compared with the hashes recorded in ARCHITECTURE.md / audit_part1.md / adjudication_U4.md.
  (A) arb ball-arithmetic enclosures of the headline constants of OAI, Banks, Guo and Kimura (Remark 7).
  (B) method ceilings: the generic chain (1-k)A - K <= b*delta*A^2, Banks's continuous optimum, and the
      asymptotic ceiling of Guo's comparison (Lemma 5.1 + Prop 3.1 shape) for several arithmetic inputs,
      including the closed form 3 - 2*sqrt(2) for the ideal input (kappa = 1/2, e = 0, y -> q).
      Also the auditor's heuristic exponent count kappa(m) = (1+m)/(2m).
  (C) consequences: the implied L(1,chi) lower bound g(q) (audit_part1 §9 recipe) and an explicit bound X0
      for imaginary quadratic fields whose class group has exponent <= 2 (auditor's arithmetic).
Nothing from any audited repository is imported or executed. Paths are read as data only.
"""
import hashlib, math, os, sys, time
from fractions import Fraction as F

import flint
from flint import arb, ctx
import mpmath
import sympy as sp

ctx.prec = 200


def Q(fr):
    """exact rational -> arb ball"""
    fr = F(fr)
    return arb(fr.numerator) / arb(fr.denominator)

mpmath.mp.dps = 40
T0 = time.time()
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))


def info(s):
    print("INFO " + s)


# ----------------------------------------------------------------------------------------------- (H)
print("== (H) source hashes ==")
OAI = "/home/user/openai/math"
CACHE = "/tmp/claude-0/-home-user-riemann/e62aa4cb-6226-5e37-8f52-ea0fa055746f/scratchpad/fulltext/arxiv"
if len(sys.argv) > 1:
    OAI = sys.argv[1]
if len(sys.argv) > 2:
    CACHE = sys.argv[2]
EXPECTED = {
    OAI + "/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf":
        "fab9f6e84ece2a37d834b2c031d8eb14e81413d9f6270791e7b5468b295214ef",
    OAI + "/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex":
        "b011ba9c1f55ee2164292492c55e0c6d75c458eb30d4808808f9953823b8ded4",
    OAI + "/lean/ComparatorChallenges/SiegelZeros.lean":
        "bedaac0248a641910f79a380d9702d82c6bfbbfd3760a69d27c72c5d8fb136ce",
    OAI + "/lean/ComparatorChallenges/SiegelZeros.json":
        "620696740156c4503f27ac17760adf1b638f621ad81ab4cde7a0f8df32c4b643",
    CACHE + "/2610.15483/paper.pdf": "54891704515ba9d58ae60ce4c16f4b368a377a9732ca98e26172209fa0647d6f",
    CACHE + "/2610.21099/paper.pdf": "30dc40c959735eaaddd3609919695f87258ec2807fb615a9a4386702f3536116",
    CACHE + "/2610.30476/paper.pdf": "f3058ae2a77e5c8e277cf90ed0faf8f745b8b638442b3439dfbf230e93e47a7e",
    CACHE + "/2610.21511/paper.pdf": "5987fa4df134c5d94faf92a0278af96fcf18ac6adfb25adaddb7d6ff63e5e733",
}
for path, exp in EXPECTED.items():
    if not os.path.exists(path):
        info("missing (not checked): " + path)
        continue
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    check("sha256 " + os.path.relpath(path, "/"), h == exp, h[:16] + "...")

# ----------------------------------------------------------------------------------------------- (A)
print("\n== (A) headline constants (arb, 200 bits) ==")
e32 = Q(F(3, 2)).exp()
C1 = 2 * e32 / 9
C2 = e32 / 4
delta0 = arb(81) / (5888 * e32)
check("Banks delta0 = 81/(5888 e^{3/2}) > 3.0e-3", delta0 > Q(F(3, 1000)), str(delta0.mid()))
check("Banks delta0 = 9/(128*23*C1) (same number)", abs(delta0 - arb(9) / (128 * 23 * C1)) < arb(10) ** -50)
om = 8 * (C2 + Q(F(8, 5)))
check("Banks omega = ceil(8(C2+8/5)) = 22", (om > 21) and (om < 22), str(om.mid()))

g_margin = Q(F(451, 60)) * arb(3).log() - 8
check("Guo (5.15): (451/60) log 3 - 8 > 0", g_margin > 0, str(g_margin.mid()))
gA_margin = Q(F(4453, 960)) * arb(7).log() - 8
check("Guo App. A: (4453/960) log 7 - 8 > 0", gA_margin > 0, str(gA_margin.mid()))
H1 = sum(F(1, m * m) for m in range(1, 8)) + (F(1, 8) - F(1, 28))
check("Guo (5.7): sum_{m<=7} 1/m^2 + int_8^28 dt/t^2 = 282431/176400 > 8/5", H1 == F(282431, 176400) and H1 > F(8, 5))
check("Guo (5.11): 73/270*(287/10+6)+76/10000+4/7 = 1176629/118125 < 10",
      F(73, 270) * (F(287, 10) + 6) + F(76, 10000) + F(4, 7) == F(1176629, 118125) and F(1176629, 118125) < 10)
check("Guo (5.12)-(5.14): 70-6-35/2 = 93/2 and 11/20*70+29/60 = 2339/60, gap 451/60",
      F(70) - 6 - F(35, 2) == F(93, 2) and F(11, 20) * 70 + F(29, 60) == F(2339, 60) and F(93, 2) - F(2339, 60) == F(451, 60))

c0 = F(1, 4 * 97 ** 2)
C0 = F(192)
check("OAI Lem 6: C0/c0 = 192*4*97^2 = 7226112", C0 / c0 == 7226112)
check("Banks H = 12*C0/c0 = 9216*97^2 = 86713344", 12 * (C0 / c0) == 9216 * 97 ** 2 == 86713344)
check("OAI master: (3/4)(1+1/12) = 13/16 and 13/16 + 1/16 = 7/8 < 1",
      F(3, 4) * (1 + F(1, 12)) == F(13, 16) and F(13, 16) + F(1, 16) == F(7, 8))
Nn = sp.symbols("N", positive=True)
check("OAI Cor 4: 4096 N^4 = (8N)^4 > (4N-3)^4 for N >= 1, since 8N - (4N-3) = 4N+3 > 0 and 4N-3 >= 1",
      sp.expand(8 * Nn - (4 * Nn - 3)) == 4 * Nn + 3 and all(4096 * n ** 4 > (4 * n - 3) ** 4 for n in range(1, 2000)))

# Kimura Remark 7: max_eta eta^2 e^{-eta}/(16+8e^eta)
fk = lambda t: t ** 2 * mpmath.e ** (-t) / (16 + 8 * mpmath.e ** t)
eta_star = mpmath.findroot(lambda t: mpmath.diff(fk, t), 1.23)
kmax = fk(eta_star)
check("Kimura Rem. 7: max_eta eta^2 e^-eta/(16+8e^eta) ~ 1.02e-2 at eta ~ 1.23",
      abs(kmax - mpmath.mpf("0.0102")) < 5e-5 and abs(eta_star - mpmath.mpf("1.23")) < 0.01,
      "max=%s at eta=%s" % (mpmath.nstr(kmax, 8), mpmath.nstr(eta_star, 6)))

# ----------------------------------------------------------------------------------------------- (B)
print("\n== (B) method ceilings ==")
# generic chain: (1-k)A - K <= b delta A^2  =>  delta* = (1-k)^2/(4 b K) at A* = 2K/(1-k)
dstar_banks = (Q(F(3, 16)) ** 2) / (4 * C1 * (C2 + Q(F(8, 5))))
check("Banks chain continuous optimum (3/16)^2/(4 C1 (C2+8/5)) = 3.244e-3 (audit_part2 §4.3)",
      abs(dstar_banks - arb("0.003244")) < arb("1e-6"), str(dstar_banks.mid()))


def guo_phi(A, B, k, e):
    """Guo's chain as q -> infinity: contradiction iff delta < 2((1-k)A - B - e)/(AB + A^2/2),
    subject to Lemma 5.1's cap eps*log(xy) <= 1, i.e. delta <= 1/(A+B). x = q^A, y = q^B."""
    return min(2 * ((1 - k) * A - B - e) / (A * B + A * A / 2), 1 / (A + B))


def guo_ceiling(k, e, Bmin):
    best = (-1, None, None)
    # B enters negatively in the first term and in the cap, so the sup is at B -> Bmin; scan anyway.
    for B in [Bmin + 1e-9 + 0.02 * i for i in range(0, 150)]:
        lo, hi = 1e-3, 400.0
        # unimodal in A on the relevant range: ternary search, then local refine
        for _ in range(200):
            m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
            if guo_phi(m1, B, k, e) < guo_phi(m2, B, k, e):
                lo = m1
            else:
                hi = m2
        A = (lo + hi) / 2
        v = guo_phi(A, B, k, e)
        if v > best[0]:
            best = (v, A, B)
    return best


rows = [("Guo as stated (11/20, 29/60), y >= q^{2+}", 11 / 20, 29 / 60, 2.0, 0.06095),
        ("Barreto/van Dijk shape (1/2, 1/4), y >= q^{2+}", 0.5, 0.25, 2.0, None),
        ("ideal arithmetic (1/2, 0), y >= q^{2+}", 0.5, 0.0, 2.0, None),
        ("Guo (11/20, 29/60), hypothetical y -> q", 11 / 20, 29 / 60, 1.0, None),
        ("Barreto shape (1/2, 1/4), hypothetical y -> q", 0.5, 0.25, 1.0, None),
        ("ideal arithmetic (1/2, 0), hypothetical y -> q", 0.5, 0.0, 1.0, None)]
ceil_vals = {}
for lab, k, e, Bm, ref in rows:
    v, A, B = guo_ceiling(k, e, Bm)
    ceil_vals[lab] = v
    info("%-50s ceiling %.5f at A = %.3f, B = %.3f" % (lab, v, A, B))
check("Guo chain ceiling as stated reproduces audit_part1/part2 value 0.0609",
      abs(ceil_vals[rows[0][0]] - 0.06095) < 2e-4)
check("ideal-arithmetic ceiling with y -> q equals 3 - 2 sqrt 2 = 0.171573 (numerics)",
      abs(ceil_vals[rows[5][0]] - (3 - 2 * math.sqrt(2))) < 1e-6)
# closed form: at k=1/2, e=0, B=1: first term = 2(A-2)/(A^2+2A), maximised at A = 2+2sqrt2; cap 1/(A+1)
A_ = sp.symbols("A", positive=True)
t1 = 2 * (A_ / 2 - 1) / (A_ + A_ ** 2 / 2)
crit = sp.solve(sp.diff(t1, A_), A_)
Aopt = [c for c in crit if c.is_positive][0]
check("closed form: argmax A = 2 + 2 sqrt 2, value 3 - 2 sqrt 2, equal to the cap 1/(A+1) there",
      sp.simplify(Aopt - (2 + 2 * sp.sqrt(2))) == 0 and sp.simplify(t1.subs(A_, Aopt) - (3 - 2 * sp.sqrt(2))) == 0
      and sp.simplify(1 / (Aopt + 1) - (3 - 2 * sp.sqrt(2))) == 0)
check("every ceiling in the table is below LZZ's computed 1/5 and below (1/2) log 3",
      all(v < 0.2 for v in ceil_vals.values()) and 0.2 < 0.5 * math.log(3))
# auditor heuristic: m conjugate coordinates besides theta, lattice rank 2^r, m <= 2^(r-1):
# size slope log N / log U = (1+m)/2^r ; usable inert primes fraction m/2^(r-1) ; kappa = ratio = (1+m)/(2m)
tab = []
for r in range(2, 7):
    for m in sorted({2, 3, 2 ** (r - 1)}):
        if m <= 2 ** (r - 1):
            tab.append((r, m, F(1 + m, 2 ** r), F(m, 2 ** (r - 1)), F(1 + m, 2 * m)))
for r, m, s, u, kap in tab:
    info("r=%d (degree %2d field), m=%2d coords: size slope %s, usable inert fraction %s, kappa %s = %.4f"
         % (r, 2 ** r, m, s, u, kap, float(kap)))
check("heuristic kappa(m) = (1+m)/(2m): m=2 gives 3/4 (OAI l.131-132), m>1 needed, kappa -> 1/2",
      F(3, 4) == F(1 + 2, 4) and all(t[4] > F(1, 2) for t in tab) and F(1 + 32, 64) - F(1, 2) == F(1, 64))

# ----------------------------------------------------------------------------------------------- (C)
print("\n== (C) consequences (auditor's derivations; conditional on the theorem with the stated c) ==")


def g_lower(q, c, k):
    """audit_part1 §9: L(1,chi) log q >= c e^{-kc}[1 - e^c(3/2+log q) e^{kc/2} q^{-k/2}
                                                    - (q+1+(k/2) log q) e^{kc} q^{-k/2}]"""
    q = arb(q); c = Q(c); k = arb(k); L = q.log()
    return c * (-k * c).exp() * (1 - c.exp() * (Q(F(3, 2)) + L) * (k * c / 2).exp() * q ** (-k / 2)
                                 - (q + 1 + k / 2 * L) * (k * c).exp() * q ** (-k / 2))


g10 = g_lower(10, F(1, 100), 4)
check("g(10) with c = 1/100, k = 4 equals 0.007671 (audit_part1 §9)", abs(g10 - arb("0.007671")) < arb("5e-7"),
      str(g10.mid()))
check("h(D) >= (0.00767/pi) sqrt|D|/log|D| = 0.00244 sqrt|D|/log|D| for D < -4", arb("0.00767") / arb.pi() > arb("0.00244"))

# exponent <= 2: h(D) = 2^{t-1}, t = omega(|D|) (genus theory). h(D) = sqrt|D| L(1,chi)/pi for D < -4.
cL = 0.00767
hl = lambda D: cL * math.sqrt(D) / (math.pi * math.log(D))
primes = list(sp.primerange(2, 400))
prim = [1]
for p in primes:
    prim.append(prim[-1] * p)
# on [prim[k], prim[k+1]) omega <= k. hl increasing for D > e^2.
k_all = None
for k in range(1, 60):
    if all(hl(prim[j]) > 2 ** (j - 1) for j in range(k, 60)):
        k_all = k
        break
# X0: smallest D such that hl(D') > 2^{omega_max(D')-1} for all D' >= D
kk = k_all - 1  # interval [prim[kk], prim[kk+1]) needs hl > 2^{kk-1}
lo, hi = prim[kk], prim[kk + 1]
target = 2 ** (kk - 1)
for _ in range(200):
    mid = (lo + hi) / 2
    if hl(mid) > target:
        hi = mid
    else:
        lo = mid
X0 = hi
info("no exponent-2 class group at all once |D| >= p_%d# = %.4e (there omega <= k forces h <= 2^(k-1) < h_lower)" % (k_all, prim[k_all]))
info("explicit bound: exponent-2 class group => |D| < X0 = %.4e (omega <= %d there)" % (X0, kk))
min12 = 2 * prim[12]  # 3*4*5*...*37: replace the prime 2 by the prime discriminant -4
info("fields with omega >= 12 (h >= 2048, beyond Kimura's h <= 2000 list) need |D| >= %.4e" % min12)
check("X0 is finite, lies in the omega = 14 range and below 2e16", k_all == 15 and prim[14] < X0 < 2e16, "%.4e" % X0)

# ----------------------------------------------------------------------------------------------- summary
npass = sum(1 for _, ok in RESULTS if ok)
nfail = len(RESULTS) - npass
print("\nSUMMARY: %d PASS / %d FAIL, %.1f s" % (npass, nfail, time.time() - T0))
print("versions: python %s, python-flint %s, mpmath %s, sympy %s" % (sys.version.split()[0], flint.__version__,
                                                                      mpmath.__version__, sp.__version__))

"""SIEGEL Level-2 audit, part 1: constants and their mutual consistency (our own code, independent of
architecture_checks/check_constants.py).  Exact rationals (fractions) + mpmath at 40 digits.
Run: python3 -I s3_constants_consistency.py

 (G) Guo 2610.30476v1: every rational certificate of (2.2), (2.5), Lemma 2.1, (3.11), (3.12)-(3.16), small cases,
     (5.6)-(5.15), App. A; plus brute-force checks of the elementary identities (3.12)-(3.14).
 (B) Banks 2610.15483v1 Section 7: H, omega, delta0, the absorbed constants; OAI Lemma 6 <-> Banks H.
 (O) OAI: Cor 4 budget, master inequality 13/16 + 1/16 = 7/8.
 (K) Kerr 2610.21099v1: exact r, W, E_p at large D versus D^3/384, 5D^4/6144, D^4/(1536p); threshold 5/4 < 13/10 < 4/3.
 (X) Recomputed optimization: the largest delta that Guo's own inequality chain (Prop 3.1 + Lemma 5.1 + Prop 4.1,
     with exact logarithms instead of rational certificates) excludes, as a function of q, optimizing the free
     exponents x = q^A, y = q^B.  Shows where 1/100 and 1/64 sit and why Banks's 3.0e-3 is smaller (method
     efficiency, not disagreement).  Banks's recipe optimized over (lambda, omega) for comparison.
"""
from fractions import Fraction as F
import math
import itertools
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


LOG = {n: mp.log(n) for n in (2, 3, 5, 7, 10, 100, 319, 9999, 10000)}

# ---------------- (G) Guo (2.2): series certificates ----------------
def series_bounds(x, m):
    z = F(x - 1, x + 1)
    Lm = 2 * sum(z ** (2 * j + 1) / (2 * j + 1) for j in range(m))
    Rb = 2 * z ** (2 * m + 1) / ((2 * m + 1) * (1 - z * z))
    return Lm, Lm + Rb   # Lm < log x < Lm + Rb


l2lo, l2hi = series_bounds(2, 1)
l3lo, l3hi = series_bounds(3, 2)
l5lo, l5hi = series_bounds(5, 3)
l7lo, l7hi = series_bounds(7, 9)
rep(l2hi <= F(7, 10), f"(G2.2) log 2 < {float(l2hi):.6f} <= 7/10 from (x,m)=(2,1)")
rep(F(13, 12) <= l3lo and l3hi <= F(11, 10), f"(G2.2) 13/12 <= {float(l3lo):.6f} < log 3 < {float(l3hi):.6f} <= 11/10 from (3,2) (both ends attained exactly: L=13/12, L+R=11/10)")
rep(l5hi <= F(13, 8), f"(G2.2) log 5 < {float(l5hi):.6f} <= 13/8 from (5,3)")
rep(F(35, 18) <= l7lo and l7hi <= F(39, 20), f"(G2.2) 35/18 <= {float(l7lo):.6f} < log 7 < {float(l7hi):.6f} <= 39/20 from (7,9)")
rep(2 * F(7, 10) + 2 * F(13, 8) <= 5 and 2 * LOG[2] + 2 * LOG[5] < 5, "(G2.2) log 100 = 2log2 + 2log5 < 7/5 + 13/4 = 4.65 < 5")

# (2.5)
cert25 = F(11, 10) / 9 + F(13, 8) / 25 + F(39, 20) / 49 + F(1, 6) * ((3 * F(7, 10) + 1) / 8 + (F(7, 10) + F(13, 8) + 1) / 10)
exact25 = LOG[3] / 9 + LOG[5] / 25 + LOG[7] / 49 + (mp.mpf(1) / 6) * ((3 * LOG[2] + 1) / 8 + (LOG[10] + 1) / 10)
rep(cert25 == F(30607, 88200) and cert25 < F(7, 20), f"(G2.5) certificate = {cert25} = {float(cert25):.6f} (stated 30607/88200) < 7/20; exact-log value {mp.nstr(exact25, 8)}")
# V and the loss in (2.6)
V = F(7, 20) + F(11, 360) + F(7, 16)
rep(V == F(589, 720) and V < F(33, 40), f"(G2.6) V bound 7/20 + 11/360 + 7/16 = {V} < 33/40")
loss = F(33, 40) + F(49, 40) - F(13, 108) + F(3, 50)
loss_exact = mp.mpf(33) / 40 + mp.mpf(7) / 4 * LOG[2] - LOG[3] / 9 + (1 + LOG[100]) / 100
rep(loss == 2 - F(7, 675), f"(G2.6) loss certificate = {loss} = 2 - 7/675; with exact logs (V kept at 33/40): {mp.nstr(loss_exact, 8)}")
Vtrue = mp.nsum(lambda k: 0, [1, 1])
# true V = sum_p log p/(p(p-1))
Vt = mp.mpf(0)
for p in sp.primerange(2, 200000):
    Vt += mp.log(p) / (p * (p - 1))
rep(Vt < mp.mpf(33) / 40, f"(G2.6) true V = sum_p log p/(p(p-1)) = {mp.nstr(Vt, 8)} (+tail < 1e-5) < 33/40")

# ---------------- (G) Section 3 identities, brute force ----------------
ok = True
for s0 in range(1, 25):
    for k in range(0, 60):
        lhs = 2 * sum(min(k, s0 - 1 - s) for s in range(s0))
        rhs = (2 * s0 - 1) * k - k * k
        if lhs < rhs or (k < s0 and lhs != rhs) or (k >= s0 and lhs - rhs != (k - s0) * (k - s0 + 1)):
            ok = False
rep(ok, "(G3.12) 2 sum_s min(k, s0-1-s) >= (2s0-1)k - k^2, equality for k<s0, difference (k-s0)(k-s0+1) otherwise (s0<25, k<60)")
ok = True
for p0 in range(3, 400):
    for p in [x for x in range(3, p0 + 1) if sp.isprime(x)]:
        a, b = divmod(p0, p)
        S = sum(r // p for r in range(p0))
        S2 = sum((r // p) ** 2 for r in range(p0))
        if S != p * a * (a - 1) // 2 + a * b or F(S) != F(p0 * (p0 - p), 2 * p) + F(b * (p - b), 2 * p):
            ok = False
        if F(S) < F(p0 * (p0 - 1), 2 * p) - F(p0, 2) or F(S2) > F(p0 * (p0 - 1) * (2 * p0 - 1), 6 * p * p):
            ok = False
rep(ok, "(G3.13-3.14) floor-sum identity and both inequalities, all p0 < 400, odd primes p <= p0")
# (3.11) coefficient algebra
lp0, lq, l2s, lam = sp.symbols('lp0 lq l2 lam')
logb0 = lp0 / 2 + lq / 2 + l2s
expr = sp.expand(logb0 + lam * (2 * lp0 - logb0))
expr30 = sp.expand(expr.subs(lam, sp.Rational(1, 30)))
rep(sp.simplify(expr30 - (sp.Rational(11, 20) * lp0 + sp.Rational(29, 60) * lq + sp.Rational(29, 30) * l2s)) == 0,
    f"(G3.11) log b0 + (1/30)(2 log p0 - log b0) = {expr30}")
# sum_{r<p0,s<s0} (r+s)
ok = all(sum(r + s for r in range(p0) for s in range(s0)) * 2 == p0 * s0 * (p0 + s0 - 2) for p0 in range(1, 40) for s0 in range(1, 12))
rep(ok, "(G3.11) sum_{r<p0, s<s0} (r+s) = p0 s0 (p0+s0-2)/2")
# (3.16) remainder terms
t1 = (10000 * F(7, 5) + 4 * 10) / 9999
t2 = F(301, 10) * (10 + F(7, 5)) / 20000
t3 = F(7, 60) * F(301, 10)
t4 = F(22, 15) * F(7, 10)
rep(t1 == F(14040, 9999) and t1 < F(141, 100), f"(G3.16) term1 14040/9999 = {float(t1):.6f} < 141/100 (exact logs at p0=1e4: {mp.nstr(((LOG[10000]*0+mp.log(4))*10000 + 4*LOG[10000])/9999, 7)})")
rep(t2 < F(1, 50), f"(G3.16) term2 (301/10)(10+7/5)/20000 = {float(t2):.6f} < 1/50")
rep(t3 == F(2107, 600) and t3 < F(53, 15), f"(G3.16) term3 7/60*301/10 = 2107/600 = {float(t3):.6f} < 53/15")
rep(t4 == F(77, 75), "(G3.16) term4 (22/15)(7/10) = 77/75; (22/15) = 29/30 + 1/2 collects both log 2 terms")
rep(F(141, 100) + F(1, 50) + F(53, 15) + F(77, 75) == F(599, 100), "(G3.16) 141/100 + 1/50 + 53/15 + 77/75 = 599/100 < 6")
rep(F(301, 10) > 30 + F(30, 333), "(G3.16) p0/s0 < 30 + 30/333 < 301/10")
rep(F(9, 20) * 10 + F(7, 5) == F(59, 10) and F(89, 60) * F(7, 5) == F(623, 300),
    "(G3) small cases: (9/20)*10 + 7/5 = 59/10; (89/60)(7/5) = 623/300")
# monotonicity claims for t >= 10000
tt = [10000 * 1.5 ** k for k in range(60)]
mono = all(a > b for a, b in zip([t / (t - 1) for t in tt], [t / (t - 1) for t in tt[1:]])) and \
       all(a > b for a, b in zip([math.log(t) / (t - 1) for t in tt], [math.log(t) / (t - 1) for t in tt[1:]])) and \
       all(a > b for a, b in zip([(math.log(t) + math.log(4)) / t for t in tt], [(math.log(t) + math.log(4)) / t for t in tt[1:]]))
rep(mono, "(G3.16) t/(t-1), log t/(t-1), (log t + log 4)/t decreasing on t >= 10^4 (grid)")

# ---------------- (G) Section 5 ----------------
H1 = sum(F(1, m * m) for m in range(1, 8)) + F(1, 8) - F(1, 28)
rep(H1 == F(282431, 176400) and H1 > F(8, 5), f"(G5.6) sum_{{m<=7}} 1/m^2 + int_8^28 dt/t^2 = {H1} = {float(H1):.6f} > 8/5")
rep(sum(F(1, m * m) for m in range(1, 28)) >= H1, "(G5.6) sum_{m<=27} 1/m^2 >= that certificate")
By = (4 + 3 * F(11, 10)) / 27
rep(By == F(73, 270), f"(G5.7) (4 + 3 log 3)/27 < (4 + 33/10)/27 = 73/270; exact {mp.nstr((4 + 3 * LOG[3]) / 27, 8)}")
Bxy = (4 + 38 * LOG[3]) * mp.power(3, -38)
rep(Bxy < mp.mpf(50) * mp.power(3, -38) < mp.mpf(1) / 10000, f"(G5.8) (4 + 38 log 3) 3^-38 = {mp.nstr(Bxy, 5)} < 50*3^-38 < 1e-4")
c59 = (F(73, 135) + F(2, 27)) * F(12, 13)
rep(c59 == F(332, 585) and c59 < F(4, 7), f"(G5.9) (73/135 + 2/27)(12/13) = {c59} < 4/7")
kap = 70 * 6 + F(70 * 70, 2)
rep(kap == 2870, "(G5) kappa/log^2 q = 70*6 + 70^2/2 = 2870; eps*kappa/log q = 2870 delta <= 28.7")
E510 = F(73, 270) * (F(287, 10) + 6) + F(76, 10000) + F(4, 7)
rep(E510 == F(1176629, 118125) and E510 == 10 - F(4621, 118125), f"(G5.10) error certificate = {E510} = {float(E510):.6f} < 10")
J = F(287, 10) + F(5, 8) * 10
rep(J == F(699, 20) and J < 35, "(G5.11) J/log q < 287/10 + (5/8)*10 = 699/20 < 35")
low = 70 - 6 - F(35, 2)
up = F(11, 20) * 70 + F(29, 60)
rep(low == F(93, 2) and up == F(2339, 60) and low - up == F(451, 60), "(G5.12-5.14) 93/2 vs 2339/60, gap 451/60")
rep(F(451, 60) * F(13, 12) == 8 + F(103, 720), f"(G5.15) (451/60)(13/12) = 8 + 103/720; with exact log 3: {mp.nstr(mp.mpf(451) / 60 * LOG[3], 8)} > 8")
# monotonicity of f_k(q) = (q + 1 + k/2 log q) q^{-k/2} on q >= 3, k in {4,6,50,76}
okm = True
for k in (4, 6, 50, 76):
    qs = [3 + 0.25 * j for j in range(4000)]
    vals = [(q + 1 + k / 2 * math.log(q)) * q ** (-k / 2) for q in qs]
    okm &= all(a > b for a, b in zip(vals, vals[1:]))
    # sign of derivative formula
    okm &= all((1 - k / 2) * q - k * k / 4 * math.log(q) < 0 for q in qs)
rep(okm, "(G5) f_k(q) decreasing on [3, 1003] for k in {4,6,50,76} and the derivative bracket is negative")

# ---------------- (G) Appendix A ----------------
ByA = (8 + 2 * F(39, 20)) / 49
rep(ByA == F(17, 70), f"(GA) B(y) <= (8 + 2 log 7)/49 < (8+39/10)/49 = 17/70 exactly (strict via log 7 < 39/20); exact {mp.nstr((8 + 2 * LOG[7]) / 49, 8)}")
rep((8 + 25 * LOG[7]) * mp.power(7, -25) < 57 * mp.power(7, -25) < mp.mpf(1) / 10000, "(GA) B(xy) <= (8+25 log 7) 7^-25 < 57*7^-25 < 1e-4")
kapA = 46 * 4 + F(46 * 46, 2)
rep(kapA == 1242 and F(1242, 64) == F(621, 32), "(GA) kappa = 1242 log^2 q, eps kappa/log q <= 621/32")
EA = F(17, 70) * (F(621, 32) + 4) + F(50, 10000) + (F(17, 35) + F(2, 49)) * F(18, 35)
rep(EA == 6 - F(21863, 548800), f"(GA) error certificate = {EA} = 6 - 21863/548800 = {float(EA):.6f}")
JA = F(621, 32) + F(5, 8) * 6
rep(JA == F(741, 32), "(GA) J/log q < 741/32")
gapA = (46 - 4 - JA / 2) - (F(11, 20) * 46 + F(29, 60))
rep(gapA == F(4453, 960) and gapA * F(35, 18) == 8 + F(3523, 3456),
    f"(GA) gap 4453/960, (4453/960)(35/18) = 8 + 3523/3456; exact log 7: {mp.nstr(mp.mpf(4453) / 960 * LOG[7], 8)} > 8")
rep(50 * F(1, 64) == F(25, 32) and 2 * 7 ** 2 >= 0 and 7 ** 2 >= 27, "(GA) eps log(xy) = 50 delta <= 25/32; sqrt(y) = q^2 >= 49 >= 27")

# ---------------- (B) Banks ----------------
C1 = 2 * mp.e ** 1.5 / 9
C2 = mp.e ** 1.5 / 4
H = 9216 * 97 ** 2
omega = int(mp.ceil(8 * (C2 + mp.mpf(8) / 5)))
delta0 = 9 / (128 * (omega + 1) * C1)
rep(omega == 22, f"(B) omega = ceil(8(C2+8/5)) = ceil({mp.nstr(8 * (C2 + mp.mpf(8) / 5), 8)}) = {omega}")
rep(abs(delta0 - 81 / (5888 * mp.e ** 1.5)) < 1e-30 and delta0 > mp.mpf('0.003'), f"(B) delta0 = 9/(128*23*C1) = 81/(5888 e^1.5) = {mp.nstr(delta0, 10)} >= 3.0e-3")
rep(H >= 8 * 97 ** 3 and mp.power(H, mp.mpf(2) / 3) >= 4 * 97 ** 2, f"(B) H = 9216*97^2 = {H} >= 8*97^3 = {8 * 97 ** 3}, so H^(2/3) >= 4*97^2")
rep(F(768 * 97 ** 2, H) == F(1, 12), "(B) S23/S1 <= 768*97^2/H = 1/12")
rep(F(12) * 192 * 4 * 97 ** 2 == H, "(B/O) Banks H = 12 * C0/c0 of OAI Lemma 6 (C0 = 192, c0 = 1/(4*97^2)): the OAI choice (C0/c0)/H <= 1/12 made explicit")
Lq0 = mp.log(mp.mpf(10) ** 10)
absorbed = mp.log(H) + 3 + mp.mpf(13) / 12 * mp.log(8)
rep(Lq0 > 23 and absorbed < 24, f"(B) L >= log 1e10 = {mp.nstr(Lq0, 6)} > 23; log H + 3 + (13/12) log 8 = {mp.nstr(absorbed, 6)} < 24 < (24/23) L")
s = 1 / (2 * mp.mpf(H)) + mp.mpf(13) / 24 + mp.mpf(24) / 23
rep(s < mp.mpf(8) / 5, f"(B) 1/(2H) + 13/24 + 24/23 = {mp.nstr(s, 8)} < 8/5")
rep(3 * mp.log(8) / (2 * 8) <= 1, "(B) (3/2) N^4 log M <= S1 needs 3 log M/(2M) <= 1 for M >= 8")
best = (0, None)
for lam_ in [mp.mpf(k) / 20 for k in range(5, 41)]:
    c1 = mp.e ** lam_ / (2 * lam_ ** 2)
    c2 = mp.e ** lam_ / 4
    for om in range(5, 80):
        d0 = (mp.mpf(3) / 16 - 3 * (c2 + mp.mpf(8) / 5) / (4 * om)) / (mp.mpf(4) / 3 * (om + 1) * c1)
        if d0 > best[0]:
            best = (d0, (lam_, om))
out.append(f"INFO (B) Banks's recipe optimized over lambda in [1/4,2], integer omega: best delta0 = {mp.nstr(best[0], 6)} at "
           f"lambda={mp.nstr(best[1][0], 3)}, omega={best[1][1]} (stated: 3.0696e-3 at lambda=3/2, omega=22)")

# ---------------- (O) OAI ----------------
okc = all((4 * N - 3) ** 4 < 4096 * N ** 4 for N in range(1, 2000))
rep(okc, "(O) Cor 4: (4N-3)^4 < 4096 N^4 = T1T2T3/8, and T_j >= 32N >= 6(N-1) gives T_j - 3(N-1) >= T_j/2")
rep(F(3, 4) * (1 + F(1, 12)) == F(13, 16) and F(13, 16) + F(1, 16) == F(7, 8), "(O) master: (3/4)(1 + 1/12) = 13/16; 13/16 + 1/16 = 7/8 < 1")

# ---------------- (K) Kerr counts ----------------
for Dg in (2000, 8000):
    r = 0
    W = 0
    Ep = {11: 0, 101: 0}
    for i in range(Dg + 1):
        rem = (Dg - i) // 8  # j + k <= rem
        cnt = (rem + 1) * (rem + 2) // 2
        r += cnt
        sjk = sum(t * (t + 1) for t in range(rem + 1))  # sum over j+k<=rem of (j+k) = sum_t t*(t+1)
        W += i * cnt + sjk
        for p in Ep:
            Ep[p] += (i // p) * cnt
    out.append(f"INFO (K) D={Dg}: r/(D^3/384) = {r / (Dg ** 3 / 384):.5f}, W/(5D^4/6144) = {W / (5 * Dg ** 4 / 6144):.5f}, "
               f"E_11/(D^4/(1536*11)) = {Ep[11] / (Dg ** 4 / (1536 * 11)):.5f}, E_101/(D^4/(1536*101)) = {Ep[101] / (Dg ** 4 / (1536 * 101)):.5f}")
rep(F(5, 4) < F(13, 10) < F(4, 3), "(K) threshold ratio W/(D^4/1536) -> 5/4 < 13/10 < 4/3; needs gamma/30 > 13/20 + C + o(1)")
v = sp.Matrix([[1, sp.sqrt(sp.Symbol('q', positive=True)), sp.sqrt(2)],
               [1, -sp.sqrt(sp.Symbol('q', positive=True)), sp.sqrt(2)],
               [1, -sp.sqrt(sp.Symbol('q', positive=True)), -sp.sqrt(2)]])
qq = sp.Symbol('q', positive=True)
g1 = sp.Matrix([1, 1, 1]); g2 = sp.Matrix([sp.sqrt(qq), -sp.sqrt(qq), -sp.sqrt(qq)])
g3 = sp.Matrix([sp.sqrt(2), sp.sqrt(2), -sp.sqrt(2)]); g4 = sp.Matrix([sp.sqrt(2 * qq), -sp.sqrt(2 * qq), sp.sqrt(2 * qq)])
det = sp.simplify(sp.Matrix.hstack(g1, g2, g3).det())
kern = sp.simplify(sp.sqrt(2 * qq) * g1 + sp.sqrt(2) * g2 - sp.sqrt(qq) * g3 - g4)
rep(sp.simplify(det - 4 * sp.sqrt(2 * qq)) == 0 and kern == sp.zeros(3, 1), f"(K) det(g1,g2,g3) = {det}; v = (sqrt(2q), sqrt2, -sqrt q, -1) in ker (q>0 branch)")


# ---------------- (X) Guo-chain optimization ----------------
def guo_delta_star(q, A, B):
    """Largest delta for which Guo's chain (exact logs, same inequalities) is contradictory at x=q^A, y=q^B.
    Returns 0 if the side conditions fail.  Conditions: y >= max(q,100), beta >= 1/2, eps*log(xy) <= 1."""
    L = math.log(q)
    if B < 1 or B * L < math.log(100) or A <= B:
        return 0.0
    logy = B * L
    H1 = sum(1 / m ** 2 for m in range(1, int(math.isqrt(int(math.exp(logy)))) + 1)) if logy < math.log(1e12) else math.pi ** 2 / 6 - math.exp(-logy / 2)
    By = math.exp(L - logy / 2) + (1 + 0.5 * logy) * math.exp(-logy / 2)
    Bxy = math.exp(L - (A + B) * L / 2) + (1 + 0.5 * (A + B) * L) * math.exp(-(A + B) * L / 2)
    y_m12 = math.exp(-logy / 2)
    kap = A * B + A * A / 2           # kappa / L^2
    # J <= delta*kap*L + [By (delta*kap*L + B L) + Bxy (A+B) L + 2By + 2 y^-1/2] / H1
    # need: (A - B) L - 2 - J/2 >= (11/20) A L + (29/60) L + 6   (strictness supplied by the strict bounds)
    lhs_const = ((A - B) - 0.55 * A - 29 / 60) * L - 8
    fixed = (By * B * L + Bxy * (A + B) * L + 2 * By + 2 * y_m12) / H1
    slope = kap * L * (1 + By / H1)
    dmax = (2 * lhs_const - fixed) / slope
    dmax = min(dmax, 1 / (A + B), L / 2)
    return max(dmax, 0.0)


def best_delta(q):
    best = (0.0, None)
    for A in [a / 2 for a in range(4, 401)]:
        for B in [1.0, 1.5, 2, 2.1, 2.25, 2.5, 3, 3.5, 4, 5, 6, 8]:
            d = guo_delta_star(q, A, B)
            if d > best[0]:
                best = (d, (A, B))
    return best


rows = []
for q in [3, 4, 5, 7, 8, 11, 100, 10 ** 4, 10 ** 10, 10 ** 30, 10 ** 100]:
    d, ab = best_delta(q)
    rows.append((q, d, ab))
    out.append(f"INFO (X) q={q:.3g}: best delta excluded by Guo's chain = {d:.5f} at (A,B)={ab};  "
               f"fixed (70,6): {guo_delta_star(q, 70, 6):.5f};  fixed (46,4): {guo_delta_star(q, 46, 4):.5f}")
rep(guo_delta_star(3, 70, 6) > 0.01, f"(X) at q=3 with Guo's (A,B)=(70,6): delta* = {guo_delta_star(3, 70, 6):.5f} > 1/100 (consistent with the 8.258 > 8 margin)")
rep(min(guo_delta_star(q, 46, 4) for q in range(7, 2000)) > 1 / 64, f"(X) min_{{7<=q<2000}} delta*(q; 46, 4) = {min(guo_delta_star(q, 46, 4) for q in range(7, 2000)):.5f} > 1/64")
rep(min(guo_delta_star(q, 70, 6) for q in range(3, 2000)) > 0.01, f"(X) min_{{3<=q<2000}} delta*(q; 70, 6) = {min(guo_delta_star(q, 70, 6) for q in range(3, 2000)):.5f} > 1/100")
# q -> infinity: B(y) -> 0 requires y = q^B with B > 2 (B(y) ~ q^{1-B/2}); the constants -2, +6 become negligible.
asym = max(min(2 * (0.45 * A - Bq - 29 / 60) / (A * Bq + A * A / 2), 1 / (A + Bq))
           for A in [a / 100 for a in range(300, 4000)] for Bq in [2.0001])
out.append(f"INFO (X) q -> infinity limit of Guo's chain (B -> 2+): sup_A min(2((9/20)A - B - 29/60)/(AB + A^2/2), 1/(A+B)) = {asym:.5f}")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")

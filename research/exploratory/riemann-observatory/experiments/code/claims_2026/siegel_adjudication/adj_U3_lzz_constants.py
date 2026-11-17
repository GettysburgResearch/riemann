# Independent recomputation of the analytic constants of Lu-Zaman-Zhao (arXiv:2602.03626v2):
#   C2 (Thorner-Zaman Prop 2.10), C4, C8, C16 (LZZ Prop 5.2 via Lemma 5.3),
#   the 1.912 constant (LZZ Thm 6.3 / Lemma 4.4), and phi, rho, K, E (LZZ Thm 6.3, Cor 6.4)
#   for the four r values of LZZ Table 1.
# Our own code; ball arithmetic (python-flint arb). Formulas transcribed from the v2 LaTeX source.
import flint
from flint import arb, ctx
ctx.prec = 200

pi = arb.pi()
one = arb(1)

def zeta(s):
    return arb(s).zeta()

# ---- Thorner-Zaman Prop 2.10: 2*sum_j (-1)^j log zeta(j+3/2) <= 1.4988, sup_t exp(...) <= 2.97655
def alt_logzeta(a, step, J=400):
    # sum_{j>=0} (-1)^j log zeta(a + j*step); alternating with decreasing terms -> enclose by partial sums
    s = arb(0)
    parts = []
    for j in range(J + 1):
        s += (-1) ** j * zeta(a + j * step).log()
        parts.append(s)
    return parts[-2], parts[-1]  # consecutive partial sums bracket the limit

lo, hi = alt_logzeta(arb(3) / 2, 1)
print("TZ24: 2*sum (-1)^j log zeta(j+3/2) in [", (2 * lo).str(10), ",", (2 * hi).str(10), "]  (stated <= 1.4988)")
S_tz = arb(2) * hi if hi > lo else arb(2) * lo
import mpmath as mp
mp.mp.dps = 30
def tz_expo(t):
    t = mp.mpf(t)
    return mp.log(1 / (2 * mp.pi)) / 4 + mp.mpf('1.4988') + (79 + 210 * t**2 - 48 * t**4) / (1536 * (t**2 + 1) ** 3)
ts = [i / 1000 for i in range(0, 20001)]
best = max(ts, key=lambda t: tz_expo(t))
print("TZ24: sup_t exp(...) attained near t =", best, " value =", mp.nstr(mp.e ** tz_expo(best), 12), " (stated <= 2.97655)")

# ---- LZZ Lemma 5.3 iteration: C_{2^{k+1}} = sqrt(C_{2^k}) * exp(P_k / 2^{k+3}) * prod_j zeta(1 + 1/2^{k+1} + j/2^k)^{(-1)^j}
def P_k(k, t=0):
    k = arb(k); t = arb(t)
    a = arb(2) ** (2 * k)
    return (-(t ** 4) / (4 * a) + 35 * t ** 2 / (32 * a ** 2) + one / (4 * a) - arb(5) / (32 * a ** 2) + arb(61) / (192 * a ** 3)) / (t ** 2 + 1) ** 3

def sup_P(k):
    # numerical sup over t (mpmath grid) to check the claim that the sup is at t=0
    def h(t):
        a = mp.mpf(2) ** (2 * k)
        return (-(t ** 4) / (4 * a) + 35 * t ** 2 / (32 * a ** 2) + 1 / (4 * a) - mp.mpf(5) / (32 * a ** 2) + mp.mpf(61) / (192 * a ** 3)) / (t ** 2 + 1) ** 3
    grid = [mp.mpf(i) / 500 for i in range(0, 50001)]
    tb = max(grid, key=h)
    return tb, h(tb), h(0)

C = {2: arb('2.97655')}
for k in (1, 2, 3):
    tb, hb, h0 = sup_P(k)
    lo, hi = alt_logzeta(1 + one / 2 ** (k + 1), one / 2 ** k, J=1001)
    L = hi if hi > lo else lo   # upper of the two brackets
    Cnext = C[2 ** k].sqrt() * (P_k(k) / 2 ** (k + 3)).exp() * L.exp()
    C[2 ** (k + 1)] = Cnext
    print(f"k={k}: sup_t P attained at t={mp.nstr(tb,6)} (h(tb)={mp.nstr(hb,12)}, h(0)={mp.nstr(h0,12)});  C_{2**(k+1)} = {Cnext.str(10)}")
print("stated: C4=5.13781, C8=9.49562, C16=18.23874")

# ---- 1.912 constant (Lemma 4.4 with b=7/8)
b = arb(7) / 8
c1912 = pi / b - 4 * (b ** -2 - 1).sqrt() * (((1 - b) / (1 + b)).sqrt()).atan() - 2 * (2 * b).log()
print("Lemma 4.4 bracket at b=7/8:", c1912.str(12), " (stated <= 1.912)")
# numerical check of the closed form: int_{-pi/2}^{pi/2} cos t log(1 + 1/(b cos t)) dt
f = lambda t: mp.cos(t) * mp.log(1 + 1 / (mp.mpf(7) / 8 * mp.cos(t)))
print("   direct quadrature:", mp.nstr(mp.quad(f, [-mp.pi / 2, 0, mp.pi / 2]), 12))

# ---- Theorem 6.3 / Corollary 6.4 constants
Cst = {2: arb('2.97655'), 4: arb('5.13781'), 8: arb('9.49562')}  # stated values used by LZZ
gamma = arb.const_euler()

def constants(r, Cst=Cst):
    r = arb(r)
    r1 = r + arb(7) / 8
    th = {0: pi / 2,
          1: ((r + arb(1) / 8) / r1).acos(),
          2: ((r + arb(1) / 4) / r1).acos(),
          3: ((r + arb(1) / 2) / r1).acos(),
          4: ((r + arb(3) / 4) / r1).acos(),
          5: arb(0)}
    A = lambda n, m: th[m].sin() - th[n].sin()
    B = lambda n, m: (th[n] - th[m]) / 2 + (th[n].sin() * th[n].cos() - th[m].sin() * th[m].cos()) / 2
    phi = r * A(1, 5) / (pi * r1) + B(0, 1) / (pi * (8 * r + 1)) + B(1, 5) / pi
    rho = -(2 * A(0, 1) / (pi * r1) + 2 * B(0, 1) / (pi * (r + arb(1) / 8)))
    K1 = (2 * Cst[8].log() + (2 * r + 2).log() / 8) * B(0, 1) / (pi * (r + arb(1) / 8))
    Kk = {}
    for k in (2, 3):
        Y = arb(15) / 8 + arb(2) ** (k - 4) + 2 * r
        T1 = (r + arb(2) ** (k - 5)) / (pi * r1) * A(k - 1, k) + B(k - 1, k) / pi
        T2 = (r + arb(2) ** (k - 4)) / (pi * r1) * A(k - 1, k) + B(k - 1, k) / pi
        Kk[k] = (arb(2) ** (6 - k) * Cst[2 ** (4 - k)].log() + 2 * Y.log()) * T1 \
              - (arb(2) ** (6 - k) * Cst[2 ** (5 - k)].log() + Y.log()) * T2
    for k in (4, 5):
        Y = arb(7) / 8 + arb(2) ** (3 - k)
        T1 = (r + 1 - arb(2) ** (2 - k)) / (pi * r1) * A(k - 1, k) + B(k - 1, k) / pi
        T2 = (r + 1 - arb(2) ** (3 - k)) / (pi * r1) * A(k - 1, k) + B(k - 1, k) / pi
        Kk[k] = -(arb(2) ** (k - 1) * Cst[2 ** (k - 3)].log() + 2 * Y.log()) * T1 \
              + (arb(2) ** (k - 1) * Cst[2 ** (k - 2)].log() + Y.log()) * T2
    z = flint.acb(2 + r) - flint.acb(r1) * flint.acb(0, th[3]).exp()
    KR = 2 * (abs(z).log() - (2 * pi).log()) * ((r + arb(1) / 2) / (pi * r1) * A(3, 5) + B(3, 5) / pi)
    digamma = flint.acb((3 + r) / 2).digamma().real
    K = arb('1.912') / (pi * r1) + KR + K1 + Kk[2] + Kk[3] + Kk[4] + Kk[5] - (2 * pi).log() + gamma / 2 + 1 + digamma / 2
    E = K + rho * (1 + 1 / r).log()
    # sanity: the log q coefficients of J1..J5 should sum to phi
    return phi, rho, K, E

ln10 = arb(10).log()
table = [('1.4', '0.22946', '1.1740'), ('1.0', '0.23504', '1.2002'), ('1.6', '0.22675', '1.1614'), ('1.3', '0.23083', '1.1805'), ('1.2', '0.23222', '1.1870'), ('1.1', '0.23362', '1.1936')]
print("\nTable 1 rows (lambda=1.6,1.3,1.2,1.1) plus code presets lambda=1.4, 1.0 (presets.c, c=0.1 runs) recomputation (phi, E must be <= the stated values for the stated table to be valid upper bounds):")
for lam, phis, Es in table:
    r = arb(lam) / (10 * ln10)
    phi, rho, K, E = constants(r)
    print(f"lambda={lam}: r={r.str(8)}  phi={phi.str(10)} (stated {phis})  rho={rho.str(8)}  K={K.str(8)}  E={E.str(10)} (stated {Es})"
          f"  phi_ok={bool(phi <= arb(phis))} E_ok={bool(E <= arb(Es))}")

# same with our recomputed C4, C8 (upper brackets) to see sensitivity
Cre = {2: arb('2.97655'), 4: C[4], 8: C[8]}
print("\nWith our recomputed C4, C8:")
for lam, phis, Es in table:
    r = arb(lam) / (10 * ln10)
    phi, rho, K, E = constants(r, Cre)
    print(f"lambda={lam}: E={E.str(10)} (stated {Es})")

# ---- Banks side: the deduction of the all-q constant from LZZ Thm 1.1, and how far Banks's own bookkeeping reaches
import mpmath as mp
mp.mp.dps = 40
delta0 = mp.mpf(81) / (5888 * mp.e ** mp.mpf(1.5))
C1 = 2 * mp.e ** mp.mpf(1.5) / 9; C2 = mp.e ** mp.mpf(1.5) / 4
H = 9216 * 97 ** 2
print("\nBanks: delta0 = 81/(5888 e^1.5) =", mp.nstr(delta0, 12), " >= 3.0e-3:", delta0 >= mp.mpf('3.0e-3'),
      ";  9/(128*23*C1) =", mp.nstr(mp.mpf(9) / (128 * 23 * C1), 12))
print("LZZ gives c0 > 1/5 =", 0.2, " > 3.0e-3: True")
Kb = mp.log(H) + 3 + mp.mpf(13) / 12 * mp.log(8)
print("Banks Step 3 bounded term K = log H + 3 + (13/12) log 8 =", mp.nstr(Kb, 10), "; H =", H)
# with omega = 22 fixed (delta0 unchanged), Step 4 needs C2 + 1/(2H) + 13/24 + K/L <= 22/8
Lmin = Kb / (mp.mpf(22) / 8 - C2 - mp.mpf(1) / (2 * H) - mp.mpf(13) / 24)
print("omega=22 bookkeeping closes for L >=", mp.nstr(Lmin, 8), " i.e. q >=", mp.nstr(mp.e ** Lmin, 6), "(also needs q >= H =", H, ")")
# smallest delta0 obtainable from Banks's formula when q is just above H (omega grows as L shrinks)
for qq in [H, 10**8, 10**9, mp.e ** Lmin]:
    L = mp.log(qq)
    om = mp.ceil(8 * (C2 + mp.mpf(1) / (2 * H) + mp.mpf(13) / 24 + Kb / L))
    print(f"  q={mp.nstr(qq,6)}: omega={int(om)}, delta0=9/(128(omega+1)C1)={mp.nstr(9/(128*(om+1)*C1),6)}")
# classical explicit bound quoted by LZZ (Bordignon, per LZZ's summary; original not checked): beta <= 1 - 80/(sqrt q log^2 q)
f = lambda q: 80 / (mp.sqrt(q) * mp.log(q)) - mp.mpf('3.0e-3')
print("Bordignon-type bound gives (1-beta)log q >= 3.0e-3 only for q <=", mp.nstr(mp.findroot(f, 3e6), 6))

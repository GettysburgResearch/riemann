"""Does the O(1/j) -> O(1/j^2) correction move L-16005's downstream conclusions?
(a) crossover j where |E_j| overtakes |Xi(2 pi alpha j)|
(b) the certification boundary alpha <~ 0.4  (table (v))
(c) the artifact-dominance table (iv)
Plus: the ONSET index of the asymptotic regime, and Phi'' sign (needed for the
rigorous O(j^-2) bound).
"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, pi, exp, quad, cos, nstr, log, e
from core import Phi, dPhi, Xi, E_j, tail_cutoff

mp.dps = 40

# ---------- Phi'' sign on the relevant range -----------------------------
print("### Phi'' sign scan on [0.30, 5.0]  (Phi convex there => int_T^inf |Phi''| = |Phi'(T)|)")
t = mpf('0.30'); bad = []
while t <= 5:
    if dPhi(t, 2) <= 0:
        bad.append(float(t))
    t += mpf('0.01')
print("   negative/zero Phi'' samples on the grid:", bad if bad else "NONE (Phi'' > 0 throughout)")
print("   Phi''(0.0)=", nstr(dPhi(mpf(0), 2), 6), " Phi''(0.1)=", nstr(dPhi(mpf('0.1'), 2), 6),
      " Phi''(0.2)=", nstr(dPhi(mpf('0.2'), 2), 6))
print()

# ---------- exact eps(T) and the L-16005(ii) bound -----------------------
C4 = sum(mpf(n)**4*exp(-pi*(mpf(n)**2-1)) for n in range(1, 31))
C2 = sum(mpf(n)**2*exp(-pi*(mpf(n)**2-1)) for n in range(1, 31))


def eps_bound(T):
    U = exp(2*mpf(T))
    return 4*(pi**2*C4*U**mpf('1.25')/(pi-mpf('1.25')) + mpf('1.5')*pi*C2*U**mpf('0.25')/(pi-mpf('0.25')))*exp(-pi*U)


def eps_true(T):
    T = mpf(T)
    return 2*quad(lambda t: Phi(t), [T, T+mpf('0.25'), T+1, tail_cutoff()])


# ---------- the certification table, recomputed --------------------------
print("### (b) CERTIFICATION BOUNDARY, table (v) recomputed.  Comparison index j=10 as in L-16005.")
print("B1 = L-16005(iii) bound 2 Phi(T)/(pi alpha j)          [the O(1/j) bound]")
print("B2 = corrected rigorous bound 4|Phi'(T)|/(2 pi alpha j)^2 = |Phi'(T)|/(pi^2 alpha^2 j^2)")
print("     (rigorous given Phi'' >= 0 on (T,inf), scanned above)")
hdr = (f"{'alpha':>6} {'T':>8} {'eps(T) bnd':>12} {'eps(T) true':>12} {'B1(j=10)':>12} "
       f"{'B2(j=10)':>12} {'|E_10| true':>12} {'|Xi_10|':>12} {'old?':>6} {'new?':>6}")
print(hdr); print('-'*len(hdr))
rows = []
for astr in ['1.1', '1.0', '0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '0.35', '0.3', '0.25']:
    a = mpf(astr); T = 1/(2*a); j = 10
    eb, et = eps_bound(T), eps_true(T)
    B1 = 2*Phi(T)/(pi*a*j)
    B2 = 4*abs(dPhi(T, 1))/(2*pi*a*j)**2
    Etrue = abs(E_j(a, j))
    X = abs(Xi(2*pi*a*j))
    old = 'yes' if eb < X else 'no'
    new = 'yes' if min(eb, B2) < X else 'no'
    print(f"{astr:>6} {nstr(T,5):>8} {nstr(eb,4):>12} {nstr(et,4):>12} {nstr(B1,4):>12} "
          f"{nstr(B2,4):>12} {nstr(Etrue,4):>12} {nstr(X,4):>12} {old:>6} {new:>6}")
    rows.append((astr, float(eb), float(B2), float(Etrue), float(X)))
print()

# ---------- (a) crossover ------------------------------------------------
print("### (a) CROSSOVER: smallest j with |E_j| > |Xi(2 pi alpha j)|")
for astr in ['1.1', '1.0', '0.7', '0.5', '0.4', '0.3']:
    a = mpf(astr)
    cross = None
    tab = []
    for j in range(1, 13):
        E = abs(E_j(a, j)); X = abs(Xi(2*pi*a*j))
        tab.append((j, float(E), float(X), float(E/X)))
        if cross is None and E > X:
            cross = j
    print(f"  alpha={astr}: crossover at j={cross};  ratios |E_j|/|Xi_j| j=1..6: " +
          ", ".join(f"{r[3]:.3g}" for r in tab[:6]))
print()

# ---------- onset of the asymptotic regime -------------------------------
print("### ONSET of the j^-2 regime.  Expansion parameter is lambda/omega with")
print("    lambda = 2 pi e^{2T} = 2 pi e^{1/alpha}  (log-derivative scale of Phi at T),")
print("    omega = 2 pi alpha j  =>  regime needs  j >> e^{1/alpha}/alpha =: j*(alpha).")
lab1 = 'lambda=|Phi2/Phi1|(T)'
lab2 = 'j*(a)=e^{1/a}/a'
lab3 = 'first j: j^2|E_j|/C>0.9'
print(f"{'alpha':>6} {'T':>7} {lab1:>22} {lab2:>16} {lab3:>24}")
print('-'*90)
for astr in ['1.0', '0.7', '0.5', '0.4', '0.3']:
    a = mpf(astr); T = 1/(2*a)
    lam = abs(dPhi(T, 2)/dPhi(T, 1))
    jstar = exp(1/a)/a
    found = None
    for j in range(1, 121):
        C = 2*abs(dPhi(T, 1))/(2*pi*a)**2
        r = j*j*abs(E_j(a, j))/C
        if r > mpf('0.9'):
            found = j
            break
    print(f"{astr:>6} {nstr(T,4):>7} {nstr(lam,6):>22} {nstr(jstar,6):>16} {str(found):>22}")

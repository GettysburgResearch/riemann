# s6_theta_cusps.py -- numerical test of the cusp expansions used in paper2.tex (l.3102-3142, Lemma 6.4):
#   theta(gamma_+ w), gamma_+ = (1 0; omega 1) = DR gamma_10:  coefficients t_+(l) = omega tau_2(omega l) ebreve(l)
#   theta(gamma_- w), gamma_- = (1 0; omega^2 1) = DR gamma_19: coefficients t_-(l) = omega^2 tau_1(omega^2 l) ebreve(l)
# with tau_1, tau_2 from DR (5.13)-(5.14), no constant term (DR (5.15), j >= 10).
# theta itself is evaluated from the infinity expansion DR (5.6)-(5.8) at the (high) point gamma_sigma w.
# Also: negative controls (wrong phase, wrong unit pairing) to show the test is discriminating.
import sys, os, time, math, cmath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_theta import *

t0 = time.time()
th = FourierSeries(tau, 3, 7.0, const=SIGMA)
lam4 = cv(LAM) ** 4
def tplus(m, sh):   # coefficient at mu = m / lambda^4
    mu = cv(m) / lam4
    return OMEGA * tau2(mul(OM, m), 4) * ebreve(mu)
def tminus(m, sh):
    mu = cv(m) / lam4
    return OMEGA ** 2 * tau1(mul(OM2, m), 4) * ebreve(mu)
Rc = 6.0
Fp = FourierSeries(tplus, 4, Rc)
Fm = FourierSeries(tminus, 4, Rc)
print("terms: theta %d, F+ %d, F- %d, build %.1fs" % (len(th.mu), len(Fp.mu), len(Fm.mu), time.time() - t0))
# Lemma 6.4 support/size: every nonzero coefficient of t_+- has lambda-adic valuation -4 and |coef| <= 9|b|
def check_support(fn):
    worst = 0; cnt = 0
    for m in lattice_points(Rc, 4):
        t = fn(m, 4)
        if abs(t) == 0: continue
        cnt += 1
        u, fac = factor(m)
        assert all(p != LAM for p, e in fac), "support off lambda^-4"
        b2 = 1
        for p, e in fac:
            assert e % 3 in (0, 1)
            b2 *= norm(p) ** (e // 3)
        worst = max(worst, abs(t) / (9 * math.sqrt(b2)))
    return cnt, worst
print("support/size t_+: nonzero %d, max |t|/(9|b|) = %.12f" % check_support(tplus))
print("support/size t_-: nonzero %d, max |t|/(9|b|) = %.12f" % check_support(tminus))

gp = ((1, 0), (OMEGA, 1)); gm = ((1, 0), (OMEGA ** 2, 1))
for label, g, F, base in [("gamma_+ (DR gamma_10)", gp, Fp, -OMEGA ** 2), ("gamma_- (DR gamma_19)", gm, Fm, -OMEGA)]:
    for delta in (0.25 + 0.1j, -0.2 + 0.25j, 0.05 - 0.3j):
        z = base + delta; v = 0.5
        z2, v2 = act(g, z, v)
        lhs = th(z2, v2); rhs = F(z, v)
        print("%s at z=%s v=%.2f (theta evaluated at height %.2f): theta(g w)=%s  series=%s  rel.err %.2e"
              % (label, np.round(z, 3), v, v2, np.round(lhs, 8), np.round(rhs, 8), abs(lhs - rhs) / abs(lhs)))
# negative control: swap the roles (series for t_- used at gamma_+)
z = -OMEGA ** 2 + 0.25 + 0.1j; z2, v2 = act(gp, z, 0.5)
print("negative control (t_- series vs theta(gamma_+ w)): rel.err %.2e" % (abs(th(z2, v2) - Fm(z, 0.5)) / abs(th(z2, v2))))
print("total %.1fs" % (time.time() - t0))

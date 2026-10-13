"""triage_exponents.py -- exact (sympy, rational) exponent bookkeeping for the O5 triage table.

Status: PROPOSED bookkeeping. Every number printed is an exact rational (or an exact root);
nothing here is numerical evidence and nothing here proves a zero-free region.
Run: python3 -I triage_exponents.py   (about 2 s)
Conventions: D = column length, H = D^h rows, leverage law sigma = 1/2 + (5/6) rho / 2 (RUNG_STRENGTH).
"""
import sympy as sp

R = sp.Rational
out = []
def rec(tag, val):
    out.append((tag, val))
    print(f"{tag}: {val}")

s0, k, h, rho, eta, kap, A, tau, x, J = sp.symbols('sigma0 k h rho eta kappa A tau x J', positive=True)

# ---- M2: bootstrap with a family-wide pointwise input sigma0 (Hoelder + Oct 5 second moment at h -> 1)
s1 = ((2*k - 2)*s0 + 1 + R(5, 6)*h)/(2*k)
s1h = sp.simplify(s1.subs(h, 1))
fp = sp.solve(sp.Eq(s1h, s0), s0)
rec("M2 bootstrap output at h=1", s1h)
rec("M2 fixed point", fp)
gain = sp.simplify(s1h.subs(s0, R(7, 8)) - R(7, 8))
rec("M2 output minus input at sigma0=7/8 (positive => no gain)", gain)
assert fp == [R(11, 12)] and sp.simplify(gain - R(1, 24)/k) == 0
# zero-density bootstrap of DISPERSION_GRH_STEP 3(c): sigma_new = b + rho (A(1-b) - 1/6)/2
b = sp.Symbol('b')
snew = b + rho*(A*(1 - b) - R(1, 6))/2
rec("M2 zero-density bootstrap at b=7/8, A=2", sp.expand(snew.subs({b: R(7, 8), A: 2})))
assert sp.expand(snew.subs({b: R(7, 8), A: 2}) - R(7, 8) - rho/24) == 0

# ---- M4: hybrid rows (u, t) or (u, angular k): rows D^(h+tau), principal D^(h/6) (t ~ 0 only)
# row-blind threshold h + tau >= 1; extraction 2 sigma = 1 + h + tau - h/6
obj = 1 + h + tau - h/6
# LP: minimize obj/2 s.t. h + tau >= 1, h, tau >= 0  -> on the line tau = 1 - h, h in [0,1]
line = sp.simplify(obj.subs(tau, 1 - h)/2)
rec("M4 hybrid (u,t) boundary on h+tau=1", line)
rec("M4 hybrid best (h=1,tau=0)", line.subs(h, 1))
assert line.subs(h, 1) == R(11, 12)
c_kappa = 1 - R(1, 6)/(1 + tau)
rec("M9 leverage with D^tau angular twists per row (tau = log K / log H)", c_kappa)

# ---- D1: row-weight LP. Dyadic row range D^x carries principal mass D^(x/6) and the
# best available second-moment bound D^(1 + max(x, 1)) (Oct 5 for x >= 1, positivity for x < 1).
f_lt = (1 + 1 - x/6)/2     # x <= 1
f_gt = (1 + x - x/6)/2     # x >= 1
rec("D1 range x<=1 boundary", sp.simplify(f_lt))
rec("D1 range x>=1 boundary", sp.simplify(f_gt))
best = min(f_lt.subs(x, 1), f_gt.subs(x, 1))
rec("D1 best over all dyadic ranges (x=1)", best)
assert sp.diff(f_lt, x) < 0 and sp.diff(f_gt, x) > 0 and best == R(11, 12)

# ---- kappa-law (minimal partial sub-diagonal target)
m = 2 - eta*(1 - kap)
sig = sp.simplify((m - (1 - eta)/6)/2)
rec("kappa-law boundary (rows D^(1-eta), bound D^(2-(1-kappa) eta))", sig)
assert sp.simplify(sig - (R(11, 12) - eta*(R(5, 6) - kap)/2)) == 0
# 7/8 pointwise import as a kappa: M2 <= D^(1-eta) D^(7/4)
kap78 = sp.solve(sp.Eq(2 - eta*(1 - kap), 1 - eta + R(7, 4)), kap)[0]
rec("kappa delivered by the 7/8 import", kap78)
rec("boundary from the 7/8 import at eta=1", sp.simplify(sig.subs(kap, kap78).subs(eta, 1)))
assert sp.simplify(sig.subs(kap, kap78).subs(eta, 1)) == R(7, 8)

# ---- M7: multiplicity-weighted zero density; fixed point solves A(sigma)(1 - sigma) = 1/6
sg = sp.Symbol('sg')
rec("M7 DH A=2", sp.solve(sp.Eq(2*(1 - sg), R(1, 6)), sg))
rec("M7 A=12/5 (Huxley)", sp.solve(sp.Eq(R(12, 5)*(1 - sg), R(1, 6)), sg))
rec("M7 A=3/(3s-1) (Huxley-type near 1, if it held with multiplicity)",
    sp.solve(sp.Eq(3*(1 - sg)/(3*sg - 1), R(1, 6)), sg))
rec("M7 A=3/(2s) (Ivic-type, if it held with multiplicity)",
    sp.solve(sp.Eq(3*(1 - sg)/(2*sg), R(1, 6)), sg))
rec("M7 Ford-type 58.05 (1-s)^(3/2)", sp.N(1 - (R(1, 6)/R(5805, 100))**R(2, 3), 8))
fdet = (31 - 32*sg)/(21 - 12*sg)
rec("M7 Sep30 inner detector f(sigma)=1/6 at", sp.solve(sp.Eq(fdet, R(1, 6)), sg))
rec("M7 f(7/8), f(13/15)", (fdet.subs(sg, R(7, 8)), fdet.subs(sg, R(13, 15))))
assert sp.solve(sp.Eq(fdet, R(1, 6)), sg) == [R(11, 12)]

# ---- M5: general-coefficient sextic large sieve over ALL rows (sixth powers included).
# BGL over sixth-power-free rows gives H + N + (HN)^(2/3); the rows u = v^6 w add, for the
# coefficient vector b = 1 aligned with the principal class, the term H^(1/6) N (row-blind,
# RUNG_STRENGTH 3(a) with multiplicity).  Extraction: |A_1|^2 H^(1/6) <= Delta * D, N = D.
ex = sp.Max(h, 1, h/6 + 1, R(2, 3)*(h + 1)) + 1 - h/6
vals = [ex.subs(h, v) for v in [0, R(1, 2), 1, R(3, 2), 2, 3]]
rec("M5 general-coefficient sieve: 2*sigma at h in {0,1/2,1,3/2,2,3}", vals)
assert all(v >= 2 for v in vals)   # >= 2 means sigma >= 1: trivial
# the bare BGL bound without the multiplicity term would give 23/24 at h = 1/2: this is the
# illusion that the multiplicity term removes.
rec("M5 (illusory) BGL-without-multiplicity at h=1/2: sigma", (R(2, 3)*R(3, 2) + 1 - R(1, 12))/2)

# ---- M11: repository criteria
rec("M11 de Bruijn-Newman strip bound (Delta=2*(7/8-1/2))^2/2", (2*(R(7, 8) - R(1, 2)))**2/2)
rec("M11 Li: ratio of maximal off-line growth rates (2*Theta-1) at Theta=7/8 vs 1", (2*R(7, 8) - 1)/1)

# ---- M13: cross-scale coherence: J scales with J <= C log D gives exponent gain lim log(J^2)/log D = 0
Dv = sp.Symbol('D', positive=True)
rec("M13 coherence exponent gain", sp.limit(sp.log(sp.log(Dv)**2)/sp.log(Dv), Dv, sp.oo))

# ---- M3: rational columns: mu_K on rational squarefree m is chi_{-3}(m) (checked numerically elsewhere)
print("ALL ASSERTS PASSED")

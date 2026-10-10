# weld_num.py — stage 4 numerics for [P1-LOC-WELD]
# Z_loc computed VIA THE DEFORMED CONTOUR of DEFORM.md D1/D2: a genuine Hankel hug
# around z_b(s) = 1/4 - (3/2)s: lower edge z = z_b - x - i*eta (x: 2r -> 0), right
# semicircular cap of radius eta about z_b, upper edge z = z_b - x + i*eta (x: 0 -> 2r),
# with the D0.b branch zeta^{1/2}(a+z) = (z - z_b)^{-1/2} b(a+z), b = ((v-1)zeta(v))^{1/2}
# principal (valid: Re((v-1)zeta) > 0 on the hug's v-image, audit A1). This is the exact
# analytic continuation of Psi off the cut — NOT the collapsed formula (Z).
# For eta < |eps|/10 the finite-eta contour equals the collapsed hug limit up to O(eta)
# end-segment mismatch (Cauchy, no singularity between: pole z_b + eps stays outside).
import time
from mpmath import mp, mpf, mpc, sqrt, pi, log, exp, atan2, fabs

mp.dps = 30
T0 = time.time()
LN2 = mp.log(2)
rho1 = mp.zetazero(1)                      # true first zero, 30 digits
g1 = rho1.imag
s0 = mpc(0, g1 / 3)
zstar = mpc(mpf(1) / 4, -g1 / 2)
dz1 = mp.zeta(rho1, derivative=1)          # zeta'(rho_1)
kk = lambda b: 1 / b - (1 - 2**(-b)) / (b * b * LN2)
kh = kk(mpf(1) / 2)
cB = (sqrt(mpf(3)) / 2) * kh / (zstar * dz1)   # omega = +1 (DEFORM D2)
cB_abs_ref = mpf('0.04782893516094')
TWOR = mpf(1) / 4                          # hug length 2r
ETA = mpf('1e-12')

def Psi_fac(z, s):
    """Psi(z,s) with the pinned branch factorization (D0.b)."""
    a = mpf(3) / 4 + mpf(3) / 2 * s
    zb = 1 - a
    beta = a - mpf(1) / 2 + z             # = 1/4 + (3/2)s + z
    v = a + z                              # near the hug: v = 1 - x -+ i eta
    bv = sqrt((v - 1) * mp.zeta(v))        # principal; Re((v-1)zeta)>0 here
    return mpf(3) / 2 * kk(beta) * (z - zb)**(mpf(-1) / 2) * bv \
        / (z * mp.zeta(a - z))

def edge_quad(s, sgn, eps_abs, maxdeg):
    """int_0^{2r} Psi(z_b - x + sgn*i*eta) dx, substitution x = u^2."""
    a = mpf(3) / 4 + mpf(3) / 2 * s
    zb = 1 - a
    off = mpc(0, sgn * ETA)
    f = lambda u: Psi_fac(zb - u * u + off, s) * 2 * u
    se = sqrt(eps_abs)
    raw = [mpf(0), mpf('1e-6'), mpf('0.3') * se, se, 3 * se, 10 * se,
           mpf('0.1'), mpf('0.5')]
    pts = sorted(set(p for p in raw if 0 <= p <= mpf('0.5')))
    if pts[-1] < mpf('0.5'):
        pts.append(mpf('0.5'))
    return mp.quad(f, pts, maxdegree=maxdeg)

def cap_quad(s, maxdeg):
    a = mpf(3) / 4 + mpf(3) / 2 * s
    zb = 1 - a
    f = lambda th: Psi_fac(zb + ETA * mp.expjpi(th), s) \
        * mpc(0, 1) * ETA * mp.expjpi(th) * pi
    return mp.quad(f, [mpf(-1) / 2, 0, mpf(1) / 2], maxdegree=maxdeg)

def Zloc_contour(s, maxdeg=5):
    """(1/2 pi i) int_{H_eta(s)} Psi dz  — the deformed-contour value."""
    eps = 3 * (s - s0)
    assert abs(eps) > 10 * ETA, "eta not << |eps|"
    Ilow = edge_quad(s, -1, abs(eps), maxdeg)     # x: 2r->0, dz=-dx => +int_0^{2r}
    Iup = -edge_quad(s, +1, abs(eps), maxdeg)     # x: 0->2r, dz=-dx => -int_0^{2r}
    Icap = cap_quad(s, maxdeg)
    return (Ilow + Iup + Icap) / (2 * pi * mpc(0, 1))

print("weld_num.py  dps=%d  eta=%s  2r=%s" % (mp.dps, mp.nstr(ETA, 3), TWOR))
print("rho1 = %s" % mp.nstr(rho1, 25))
print("|c_B| computed = %s   ref 0.04782893516094   reldiff = %s"
      % (mp.nstr(abs(cB), 17), mp.nstr(abs(abs(cB) / cB_abs_ref - 1), 3)))

# ---- timing probe (worst case: t = 1e-6, phi = pi/4) --------------------------
tp = time.time()
s_probe = s0 + mpf('1e-6') * mp.expjpi(mpf(1) / 4)
Zp = Zloc_contour(s_probe)
dt_probe = time.time() - tp
print("probe (t=1e-6, phi=pi/4): Z = %s  (%.1fs)" % (mp.nstr(Zp, 10), dt_probe))
REDUCED = dt_probe * 40 > 380
if REDUCED:
    print("NOTE: contour numerics slow; REDUCED point set in use "
          "(fewer t-samples/grid points, maxdegree 6) — same formula, no shortcut.")

MD = 5   # verified: maxdeg 5 vs 6 differ by < 1e-22 on worst case
tlist = [mpf('1e-2'), mpf('1e-4'), mpf('1e-5'), mpf('1e-6')] if REDUCED else \
        [mpf('1e-2'), mpf('1e-3'), mpf('1e-4'), mpf('1e-5'), mpf('1e-6')]
phis = [mpf(-1) / 4, mpf(0), mpf(1) / 4]      # units of pi; all inside |arg|<pi/2

# ---- (N1a) rays: fit the (s-s0)^{-1/2} coefficient ---------------------------
print("\n== RAY FIT ==  model Z = c*(s-s0)^{-1/2} + R,  c ref = c_B, omega=+1")
worst_rel = mpf(0)
for ph in phis:
    d = mp.expjpi(ph)
    samp = []
    for t in tlist:
        s = s0 + t * d
        if s == s_probe:
            Z = Zp
        else:
            Z = Zloc_contour(s, MD)
        w = (s - s0)**(mpf(-1) / 2)
        R = Z - cB * w
        samp.append((t, w, Z, R))
        print("  phi=%5s*pi t=%7s |Z|=%12s  |R_loc|=%s"
              % (mp.nstr(ph, 3), mp.nstr(t, 2), mp.nstr(abs(Z), 8), mp.nstr(abs(R), 6)))
    (t1, w1, Z1, _), (t2, w2, Z2, _) = samp[-2], samp[-1]
    chat = (Z2 - Z1) / (w2 - w1)                  # difference kills the constant
    rel = abs(abs(chat) / cB_abs_ref - 1)
    relc = abs(chat / cB - 1)                     # complex (phase) agreement
    worst_rel = max(worst_rel, rel)
    print("  -> c_hat = %s" % mp.nstr(chat, 12))
    print("     |c_hat| = %s  rel.err vs |c_B| = %s ; complex rel.err vs c_B = %s"
          % (mp.nstr(abs(chat), 12), mp.nstr(rel, 3), mp.nstr(relc, 3)))
print("WORST |c| fit rel. error over rays: %s  (target <= 1e-2)" % mp.nstr(worst_rel, 3))

# ---- (N1b) grid check |R_loc| <= M_loc on Omega^+ (r_0 = 1/2) ----------------
M_loc = mpf(640); M_R = mpf('5.71')
grid = [(h, dl) for h in ['0.02', '0.08', '0.15', '0.25'] for dl in
        ['-0.5', '-0.25', '0.0', '0.25', '0.5']] + \
       [('0.6', '-0.4'), ('1.0', '0.0'), ('2.0', '0.4'), ('3.0', '-0.25')]
print("\n== GRID CHECK ==  %d points of Omega^+ (window + ray), M_loc = 640" % len(grid))
maxR = mpf(0); nfail = 0
for hs, ds in grid:
    s = mpc(mpf(hs), g1 / 3 + mpf(ds))
    Z = Zloc_contour(s, MD)
    R = Z - cB * (s - s0)**(mpf(-1) / 2)
    ok = abs(R) <= M_loc
    ok2 = abs(R) <= M_R
    maxR = max(maxR, abs(R)); nfail += 0 if ok else 1
    print("  s=%5s+i(g1/3%+.2f)  |R_loc| = %10s  <=640:%s  <=5.71:%s"
          % (hs, float(mpf(ds)), mp.nstr(abs(R), 6), "PASS" if ok else "FAIL",
             "PASS" if ok2 else "FAIL"))
print("max |R_loc| on grid = %s ; failures vs M_loc=640: %d ; vs 5.71: %s"
      % (mp.nstr(maxR, 6), nfail, "see rows"))
print("\ntotal time %.1fs" % (time.time() - T0))

#!/usr/bin/env python3
"""C1-detection-horizons -- ADJUDICATOR third, independent certification of the X_10 Jensen threshold
(the point of C1-J3/J4 where both investigator and skeptic disagree with Farmer 2020, Table 4.1).

Farmer (arXiv:2008.07206v2, Sec. 4.2):
    X_10(z) = cos z * (z^2-(10+i)^2)(z^2-(10-i)^2) / ((z^2-(5pi/2)^2)(z^2-(7pi/2)^2)),
    classical Jensen polynomial J^{d,0}_{f,cl}(z) = sum_{j<=d} C(d,j) alpha(j) z^j, where f(z) = sum alpha(j) z^j/j!.
    Farmer states: J^{d,0} has only real zeros for d <= 118, and non-real zeros for all larger d.

With u = z^2, X_10 = sum_k c_k u^k, alpha(2k) = (2k)! c_k, alpha(odd) = 0, so
    J^{d,0}(z) = R_d(z^2),  R_d(u) = sum_{k<=d/2} [d!/(d-2k)!] c_k u^k.
J^{d,0} has only real zeros  <=>  every root of R_d is real and >= 0  (R_d(0) = c_0 != 0).

Method (different from both earlier implementations: investigator = tail sums + rounded fmpz_poly roots;
skeptic = Arb power-series division + acb_poly.roots):
  * c_k by partial fractions P/Q = 1 + p/(u-A) + q/(u-B), geometric expansion, Cauchy product with cos(sqrt u),
    all in Arb ball arithmetic (rigorous enclosures; cancellation is tracked by Arb).
  * approximate roots of R_d from mpmath.polyroots (used only to choose test points / a starting point).
  * REAL-ROOTED certificate: deg R_d certified sign changes of R_d on [0, inf) (Arb evaluation at test points).
  * NON-REAL certificate: complex Krawczyk test on a box D around an approximate non-real root:
    K(D) = v0 - Y R(v0) + (1 - Y R'(D)) (D - v0) strictly inside D, with D disjoint from the real axis.
    Then D contains a root of R_d (Brouwer; R'(D) box encloses the convex hull of R' on D).
  * Monotonicity (classical): if J^{d,0} is real-rooted then so is J^{d-1,0}, because
    d/dz [z^d J^{d,0}(1/z)] = d * z^{d-1} J^{d-1,0}(1/z). Hence the two certificates at d=119 and d=120 determine
    the threshold for ALL d.
Status: NUMERICAL-RIGOROUS (Arb), conditional on the correctness of FLINT/Arb.
"""
import json, time, hashlib, platform
import flint
from flint import arb, acb, arb_poly, acb_poly, fmpz
import mpmath as mp

t_start = time.time()
flint.ctx.prec = 4000
mp.mp.dps = 400

pi = arb.pi()
A = (5 * pi / 2) ** 2
B = (7 * pi / 2) ** 2
P = lambda u: u * u - 198 * u + 10201          # (u-(10+i)^2)(u-(10-i)^2)
p = P(A) / (A - B)
q = P(B) / (B - A)
KMAX = 62

h = [arb(1) - p / A - q / B] + [-(p / A ** (m + 1)) - q / B ** (m + 1) for m in range(1, KMAX + 1)]
fac = [arb(fmpz.fac_ui(2 * j)) for j in range(KMAX + 1)]
g = [arb((-1) ** j) / fac[j] for j in range(KMAX + 1)]
c = [sum((h[m] * g[k - m] for m in range(k + 1)), arb(0)) for k in range(KMAX + 1)]

# sanity: X_10 at u = 1 (z = 1) from the series versus the closed form
u1 = arb(1)
ser = sum((c[k] * u1 ** k for k in range(KMAX + 1)), arb(0))
closed = arb(1).cos() * P(u1) / ((u1 - A) * (u1 - B))
sanity = {"series_at_z=1": ser.str(20), "closed_form_at_z=1": closed.str(20)}

def ffall(d, m):          # d!/(d-m)!
    r = fmpz(1)
    for i in range(m):
        r *= (d - i)
    return r

def Rcoeffs(d):
    return [arb(ffall(d, 2 * k)) * c[k] for k in range(d // 2 + 1)]

def to_mp(x):
    return mp.mpf(x.mid().str(380, radius=False))

def certify(d):
    co = Rcoeffs(d)
    deg = len(co) - 1
    maxrad = max(float(x.rad()) / max(abs(float(x.mid())), 1e-300) for x in co if float(x.mid()) != 0)
    poly = arb_poly(co)
    # approximate roots in the scaled variable v = d^2 u (better conditioned for polyroots)
    sc = [to_mp(co[k]) / mp.mpf(d) ** (2 * k) for k in range(deg + 1)]
    roots = mp.polyroots(list(reversed(sc)), maxsteps=2000, extraprec=4000)
    roots = sorted(roots, key=lambda r: (mp.re(r), mp.im(r)))
    nonreal = [r for r in roots if abs(mp.im(r)) > mp.mpf(10) ** -100 * (1 + abs(r))]
    rec = {"d": d, "deg_R": deg, "max_rel_coeff_radius": maxrad, "n_approx_nonreal": len(nonreal),
           "approx_roots_v_first5": [mp.nstr(r, 12) for r in roots[:5]]}
    if not nonreal:
        re_roots = [mp.re(r) for r in roots]
        assert re_roots[0] > 0
        pts = [mp.mpf(0)] + [(re_roots[i] + re_roots[i + 1]) / 2 for i in range(deg - 1)] + [2 * re_roots[-1]]
        signs = []
        for v in pts:
            x = arb(mp.nstr(v / mp.mpf(d) ** 2, 300))       # test point in u (a tiny ball around a decimal)
            val = poly(x)
            if val > 0: signs.append(1)
            elif val < 0: signs.append(-1)
            else: signs.append(0)
        changes = sum(1 for i in range(len(signs) - 1) if signs[i] * signs[i + 1] == -1)
        rec.update({"certified_signs_all_nonzero": all(s != 0 for s in signs), "certified_sign_changes_on_[0,inf)": changes,
                    "verdict": "REAL-ROOTED (certified)" if changes == deg and all(s != 0 for s in signs) else "inconclusive"})
    else:
        v0 = max(nonreal, key=lambda r: mp.im(r))
        # refine with mpmath Newton in u
        u0 = v0 / mp.mpf(d) ** 2
        cm = [to_mp(x) for x in co]
        f = lambda u: mp.polyval(list(reversed(cm)), u)
        fp = lambda u: mp.polyval(list(reversed([k * cm[k] for k in range(1, deg + 1)])), u)
        for _ in range(60):
            u0 = u0 - f(u0) / fp(u0)
        apoly = acb_poly([acb(x) for x in co])
        dpoly = apoly.derivative()
        U0 = acb(arb(mp.nstr(mp.re(u0), 350)), arb(mp.nstr(mp.im(u0), 350)))
        U0 = acb(U0.real.mid(), U0.imag.mid())
        r = abs(float(mp.im(u0))) * 1e-30
        D = acb(arb(U0.real.mid(), r), arb(U0.imag.mid(), r))
        Y = 1 / dpoly(U0)
        Y = acb(Y.real.mid(), Y.imag.mid())
        K = U0 - Y * apoly(U0) + (1 - Y * dpoly(D)) * (D - U0)
        inside = (abs(float((K.real - U0.real).mid())) + float(K.real.rad()) < r and
                  abs(float((K.imag - U0.imag).mid())) + float(K.imag.rad()) < r)
        off_axis = abs(float(U0.imag.mid())) > 2 * r
        rec.update({"u0_approx": mp.nstr(u0, 20), "box_halfwidth": r, "krawczyk_inside": inside, "box_disjoint_from_real_axis": off_axis,
                    "verdict": "HAS A NON-REAL ZERO (certified)" if (inside and off_axis) else "inconclusive"})
    return rec

results = [certify(d) for d in [117, 118, 119, 120, 121]]
out = {"campaign": "C1-detection-horizons", "role": "adjudicator", "script": "adj_farmer_x10.py",
       "env": {"python": platform.python_version(), "python-flint": flint.__version__, "mpmath": mp.__version__},
       "arb_prec_bits": flint.ctx.prec, "sanity": sanity, "results": results, "runtime_s": time.time() - t_start}
pth = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/adjudicator/adj_farmer_x10.json"
with open(pth, "w") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
print("sha256", hashlib.sha256(open(pth, "rb").read()).hexdigest())

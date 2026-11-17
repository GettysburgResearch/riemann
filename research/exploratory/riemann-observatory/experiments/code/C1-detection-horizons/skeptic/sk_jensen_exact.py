#!/usr/bin/env python3
"""SKEPTIC independent check of C1-J3/J4: thresholds of the classical Jensen polynomials J^{d,0}_{X_j,cl}
(Farmer 2020, eq. (2.2): sum_k C(d,k) X^{(k)}(0) z^k) for Farmer's toy X_j.
Independent algorithm: Taylor coefficients by ARB power-series division in u=z^2 (cos(sqrt u) * P(u) / Q(u)),
not by the investigator's mpmath tail sums; ball coefficients are kept (no rounding to integers), so the
certificate is for the exact (unrounded) polynomial.
Certificates (python-flint / Arb):
  non-real: acb_poly.roots() isolates all roots; a ball whose imaginary part excludes 0 is a certified non-real root;
  real-rooted: R(u) evaluated in Arb at points separating the (sorted) approximate roots; deg(R) certified sign
  changes on (0,inf) certify that all roots of R are real and positive, i.e. J is real-rooted.
NUMERICAL-RIGOROUS (ball arithmetic) for the stated polynomials."""
import sys, time, json, math
import flint
from flint import arb, acb, arb_poly, acb_poly
t0 = time.time()
def coeffs_X(j, a, b, N, prec):
    flint.ctx.prec = prec
    j = arb(j); a2 = a*a; b2 = b*b
    q0, q1 = a2*b2, -(a2 + b2)
    c = []; f = arb(1)
    for n in range(N + 1):
        if n > 0: f = f*(2*n)*(2*n - 1)
        c.append((-1)**n/f)
    h = []
    for n in range(N + 1):
        v = c[n] - (q1*h[n - 1] if n >= 1 else 0) - (h[n - 2] if n >= 2 else 0)
        h.append(v/q0)
    P = [(j*j + 1)**2, -2*(j*j - 1), arb(1)]
    X = [sum(P[i]*h[n - i] for i in range(3) if n - i >= 0) for n in range(N + 1)]
    return X     # coefficient of u^n = z^{2n}
def R_poly(X, d):
    co = []; f = arb(1)
    for n in range(d//2 + 1):
        if n > 0: f = f*(2*n)*(2*n - 1)
        co.append(arb(math.comb(d, 2*n))*f*X[n])
    return co
def analyse(X, d):
    co = R_poly(X, d)
    maxrel = max(float(abs(c.rad()/c.mid())) if c.mid() != 0 else 0 for c in co)
    flint.ctx.prec = 3000
    co3 = [arb(c.mid(), c.rad()) for c in co]
    P = acb_poly([acb(c) for c in co3])
    rts = P.roots()
    nonreal = [r for r in rts if not r.imag.contains(0)]
    # real-rootedness certificate by sign changes of R on (0, inf)
    re_sorted = sorted(float(r.real.mid()) for r in rts)
    Pr = arb_poly(co3)
    pts = [re_sorted[0]/2] + [(re_sorted[i] + re_sorted[i + 1])/2 for i in range(len(re_sorted) - 1)] + [re_sorted[-1]*2]
    signs = []
    for p in pts:
        v = Pr(arb(p))
        signs.append(1 if v > 0 else (-1 if v < 0 else 0))
    cert_changes = sum(1 for s1, s2 in zip(signs[:-1], signs[1:]) if s1*s2 == -1)
    return {"d": d, "deg_R": len(co) - 1, "max_rel_coeff_radius": maxrel, "n_root_balls": len(rts),
            "certified_nonreal_roots": len(nonreal), "certified_sign_changes_on_(0,inf)": cert_changes,
            "J_real_rooted_certified": cert_changes == len(co) - 1 and min(re_sorted) > 0,
            "J_nonreal_certified": len(nonreal) > 0,
            "example_nonreal": [str(r) for r in nonreal[:1]]}
res = []
flint.ctx.prec = 200
pi = arb.pi()
plans = [
  (10, (5, 7), [117, 118, 119, 120, 121]),               # Farmer's stated X_10: 5pi/2, 7pi/2 moved
  (20, (9, 11), [747, 748, 749, 750, 751]),              # moved 9pi/2, 11pi/2
  (20, (11, 13), [470, 474, 476, 477, 478, 479]),        # moved 11pi/2, 13pi/2 (closest to 20)
]
for j, (ka, kb), ds in plans:
    N = max(ds)//2 + 2
    prec = 14000 if j == 20 else 6000
    flint.ctx.prec = prec
    a = arb(ka)*arb.pi()/2; b = arb(kb)*arb.pi()/2
    t1 = time.time()
    X = coeffs_X(j, a, b, N, prec)
    # validate against closed form at z=7.3 (u=z^2): X(z) = cos z * P/Q
    z = arb("7.3"); u = z*z
    ser = sum(X[n]*u**n for n in range(N + 1))
    closed = z.cos()*((u - (arb(j)**2 - 1))**2 + 4*arb(j)**2)/((u - a*a)*(u - b*b))
    for d in ds:
        r = analyse(X, d); r.update({"j": j, "moved": [f"{ka}pi/2", f"{kb}pi/2"], "series_vs_closed_at_z=7.3": float(abs(ser - closed)),
                                     "coeff_sec": round(time.time() - t1, 1)})
        res.append(r); print(r, flush=True)
out = {"rows": res, "runtime_s": time.time() - t0, "python-flint": flint.__version__}
json.dump(out, open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C1-detection-horizons/skeptic/sk_jensen_exact.json", "w"), indent=1)
print("runtime", out["runtime_s"])

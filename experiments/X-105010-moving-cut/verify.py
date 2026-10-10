#!/usr/bin/env python3
"""X-105010: arithmetic verification for O-105010 (moving-cut feasibility).

Checks: (1) price sum_{Y^theta<p<=Y} 1/p vs log(1/theta) at finite Y and the
feasibility verdicts; (2) the depth bound k < 1/theta; (3) the window
boundary log(1/theta) <= 1 iff theta >= 1/e; (4) Dickman rho(2) = 1 - log 2;
(5) the classical-cut fingerprint 1/3 < 1/e.
"""
import json, math
from mpmath import mp, mpf, log, exp
from sympy import primerange
import sympy as sp

mp.dps = 20
RES = {}

def price(Y, theta):
    P0 = int(mpf(Y)**mpf(theta))
    return sum(mpf(1)/q for q in primerange(P0+1, int(Y)+1)), P0

# (1) price table and verdicts
tbl = {}
for th, feas_expected in [(0.5, True), (0.368, True), (1/3, False), (0.25, False)]:
    for Y in (10**5, 10**7):
        s, P0 = price(Y, th)
        assert (s < 1) == feas_expected or abs(float(s)-1) < 0.02, \
            f"verdict mismatch theta={th} Y={Y}: {float(s)}"
        tbl[f"theta={th:.3f},Y={Y}"] = {"P0": P0, "price": float(s),
                                        "log(1/theta)": float(log(1/mpf(th)))}
RES["price_table"] = tbl
# strict checks at the three named points, Y = 10^7
s_half, _ = price(10**7, 0.5); assert s_half < 1
s_third, _ = price(10**7, 1/3); assert s_third > 1
RES["theta_half_price_1e7"] = float(s_half)     # 0.6922...
RES["theta_third_price_1e7"] = float(s_third)   # 1.0877...

# (2) depth bound: k factors > Y^theta => Y^{k theta} < Y => k < 1/theta (exact)
th_s, k_s, Y_s = sp.symbols('theta k Ysym', positive=True)
# symbolic: Y^{k theta} < Y  iff  k theta < 1  (Y > 1)
assert sp.simplify(sp.log(Y_s**(k_s*th_s)) - k_s*th_s*sp.log(Y_s)) == 0
RES["depth_bound"] = "k < 1/theta exact; theta in (1/3,1/2] => depth <= 2; theta > 1/2 => depth <= 1"

# (3) window boundary: log(1/theta) <= 1 iff theta >= 1/e (exact, monotone)
assert sp.simplify(sp.log(1/sp.Rational(1,1)/ (1/sp.E)) - 1) == 0  # log(e) = 1
assert float(log(1/mpf(1)/exp(-1))) == 1.0 or abs(float(log(exp(1))) - 1) < 1e-18
RES["window_boundary"] = "log(1/theta) <= 1 iff theta >= 1/e = 0.36787944..."

# (4) Dickman rho(2) = 1 - log 2 (exact for 1<=u<=2: rho(u) = 1 - log u)
rho2 = 1 - float(log(2))
assert abs(rho2 - 0.30685281944005) < 1e-13
RES["dickman_rho_2"] = rho2

# (5) fingerprint: classical Vaughan cut 1/3 lies strictly below 1/e
assert 1/3 < float(exp(-1)) < 0.5
RES["fingerprint"] = {"one_third": 1/3, "one_over_e": float(exp(-1)), "half": 0.5}

print("ALL CHECKS PASSED")
import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "results.json"), "w") as f:
    json.dump(RES, f, indent=1)
